#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "httpx>=0.27",
#   "keyring>=25.0",
#   "pyyaml>=6.0"
# ]
# requires-python = ">=3.12"
# ///
"""
Atlassian OAuth 2.0 (3LO) authentication script.

Commands:
    setup   - Store OAuth client credentials
    login   - Start OAuth flow, open browser for consent
    status  - Check authentication status
    logout  - Clear stored tokens
    refresh - Force token refresh
"""

import argparse
import secrets
import sys
import time
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlencode, urlparse

import httpx
import keyring
import yaml

SERVICE_NAME = "atlassian-claude-skill"
CALLBACK_PORT = 8765
REDIRECT_URI = f"http://localhost:{CALLBACK_PORT}/callback"

# OAuth scopes for Jira and Confluence read access
SCOPES = [
    "read:jira-work",
    "read:jira-user",
    "read:confluence-content.all",
    "search:confluence",
    "readonly:content.attachment:confluence",
    "offline_access",  # Required for refresh tokens
]


class OAuthCallbackHandler(BaseHTTPRequestHandler):
    """HTTP handler to capture OAuth callback."""

    auth_code: str | None = None
    state: str | None = None
    error: str | None = None

    def do_GET(self):
        """Handle OAuth callback GET request."""
        parsed = urlparse(self.path)

        if parsed.path != "/callback":
            self.send_response(404)
            self.end_headers()
            return

        params = parse_qs(parsed.query)

        if "error" in params:
            OAuthCallbackHandler.error = params.get("error", ["Unknown error"])[0]
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(
                b"<html><body><h1>Authentication Failed</h1>"
                b"<p>You can close this window.</p></body></html>"
            )
            return

        OAuthCallbackHandler.auth_code = params.get("code", [None])[0]
        OAuthCallbackHandler.state = params.get("state", [None])[0]

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(
            b"<html><body><h1>Authentication Successful!</h1>"
            b"<p>You can close this window and return to the terminal.</p></body></html>"
        )

    def log_message(self, format, *args):
        """Suppress HTTP server logs."""
        pass


def get_stored_value(key: str) -> str | None:
    """Retrieve a value from Keychain."""
    return keyring.get_password(SERVICE_NAME, key)


def set_stored_value(key: str, value: str) -> None:
    """Store a value in Keychain."""
    keyring.set_password(SERVICE_NAME, key, value)


def delete_stored_value(key: str) -> None:
    """Delete a value from Keychain."""
    try:
        keyring.delete_password(SERVICE_NAME, key)
    except keyring.errors.PasswordDeleteError:
        pass


def cmd_setup(args):
    """Store OAuth client credentials."""
    client_id = args.client_id
    client_secret = args.client_secret

    if not client_id or not client_secret:
        yaml.dump(
            {
                "error": "Client ID and Client Secret are required",
                "usage": "uv run scripts/auth.py setup --client-id YOUR_ID --client-secret YOUR_SECRET",
                "help": "Get credentials from https://developer.atlassian.com/console/myapps/",
            },
            sys.stderr,
            default_flow_style=False,
        )
        sys.exit(1)

    set_stored_value("client_id", client_id)
    set_stored_value("client_secret", client_secret)

    yaml.dump(
        {
            "status": "success",
            "message": "OAuth credentials stored in Keychain",
            "next_step": "Run 'uv run scripts/auth.py login' to authenticate",
        },
        sys.stdout,
        default_flow_style=False,
    )


def cmd_setup_token(args):
    """Setup using API token from environment variables."""
    import os

    email = args.email or os.environ.get("ATLASSIAN_EMAIL")
    api_token = args.token or os.environ.get("ATLASSIAN_API_TOKEN")
    site_url = args.site_url or os.environ.get("ATLASSIAN_SITE_URL")

    missing = []
    if not email:
        missing.append("ATLASSIAN_EMAIL (or --email)")
    if not api_token:
        missing.append("ATLASSIAN_API_TOKEN (or --token)")
    if not site_url:
        missing.append("ATLASSIAN_SITE_URL (or --site-url)")

    if missing:
        yaml.dump(
            {
                "error": "Missing required values",
                "missing": missing,
                "usage": "Set environment variables or use command-line arguments",
                "example_env": {
                    "ATLASSIAN_EMAIL": "you@example.com",
                    "ATLASSIAN_API_TOKEN": "your-api-token",
                    "ATLASSIAN_SITE_URL": "https://yoursite.atlassian.net",
                },
            },
            sys.stderr,
            default_flow_style=False,
        )
        sys.exit(1)

    # Normalize site URL
    site_url = site_url.rstrip("/")

    # Verify credentials by fetching cloud ID
    print("Verifying credentials...")

    import base64
    auth_string = base64.b64encode(f"{email}:{api_token}".encode()).decode()

    with httpx.Client() as client:
        # Try to access the site to verify credentials
        response = client.get(
            f"{site_url}/rest/api/3/myself",
            headers={
                "Authorization": f"Basic {auth_string}",
                "Accept": "application/json",
            },
        )

        if response.status_code == 401:
            yaml.dump(
                {"error": "Invalid credentials. Check your email and API token."},
                sys.stderr,
                default_flow_style=False,
            )
            sys.exit(1)
        elif response.status_code != 200:
            yaml.dump(
                {"error": f"Failed to verify credentials: {response.text}"},
                sys.stderr,
                default_flow_style=False,
            )
            sys.exit(1)

        user_info = response.json()

    # Store credentials
    set_stored_value("auth_type", "basic")
    set_stored_value("api_email", email)
    set_stored_value("api_token", api_token)
    set_stored_value("site_url", site_url)
    set_stored_value("site_name", site_url.replace("https://", "").replace(".atlassian.net", ""))

    yaml.dump(
        {
            "status": "success",
            "auth_type": "basic",
            "site_url": site_url,
            "user": user_info.get("displayName", email),
            "message": "API token authentication configured. You can now use Jira and Confluence scripts.",
        },
        sys.stdout,
        default_flow_style=False,
    )


def cmd_login(args):
    """Start OAuth 2.0 3LO flow."""
    client_id = get_stored_value("client_id")
    client_secret = get_stored_value("client_secret")

    if not client_id or not client_secret:
        yaml.dump(
            {
                "error": "OAuth credentials not configured",
                "fix": "Run 'uv run scripts/auth.py setup' first",
            },
            sys.stderr,
            default_flow_style=False,
        )
        sys.exit(1)

    # Generate random state for CSRF protection
    state = secrets.token_urlsafe(32)

    # Build authorization URL
    auth_params = {
        "client_id": client_id,
        "scope": " ".join(SCOPES),
        "redirect_uri": REDIRECT_URI,
        "state": state,
        "response_type": "code",
        "prompt": "consent",
        "audience": "api.atlassian.com",
    }
    auth_url = f"https://auth.atlassian.com/authorize?{urlencode(auth_params)}"

    print("Starting OAuth authentication flow...")
    print(f"Opening browser to Atlassian consent page...\n")

    # Reset handler state
    OAuthCallbackHandler.auth_code = None
    OAuthCallbackHandler.state = None
    OAuthCallbackHandler.error = None

    # Start local server
    server = HTTPServer(("localhost", CALLBACK_PORT), OAuthCallbackHandler)
    server.timeout = 120  # 2 minute timeout

    # Open browser
    webbrowser.open(auth_url)
    print(f"If browser doesn't open, visit:\n{auth_url}\n")
    print("Waiting for authentication...")

    # Wait for callback
    while OAuthCallbackHandler.auth_code is None and OAuthCallbackHandler.error is None:
        server.handle_request()

    server.server_close()

    if OAuthCallbackHandler.error:
        yaml.dump(
            {"error": f"OAuth failed: {OAuthCallbackHandler.error}"},
            sys.stderr,
            default_flow_style=False,
        )
        sys.exit(1)

    # Verify state
    if OAuthCallbackHandler.state != state:
        yaml.dump(
            {"error": "State mismatch - possible CSRF attack"},
            sys.stderr,
            default_flow_style=False,
        )
        sys.exit(1)

    # Exchange code for tokens
    print("Exchanging authorization code for tokens...")

    with httpx.Client() as client:
        response = client.post(
            "https://auth.atlassian.com/oauth/token",
            json={
                "grant_type": "authorization_code",
                "client_id": client_id,
                "client_secret": client_secret,
                "code": OAuthCallbackHandler.auth_code,
                "redirect_uri": REDIRECT_URI,
            },
            headers={"Content-Type": "application/json"},
        )

        if response.status_code != 200:
            yaml.dump(
                {"error": f"Token exchange failed: {response.text}"},
                sys.stderr,
                default_flow_style=False,
            )
            sys.exit(1)

        tokens = response.json()

    # Store tokens
    set_stored_value("access_token", tokens["access_token"])
    set_stored_value("refresh_token", tokens["refresh_token"])
    set_stored_value("expires_at", str(time.time() + tokens["expires_in"]))

    # Fetch accessible resources to get cloud ID
    print("Fetching Atlassian cloud resources...")

    with httpx.Client() as client:
        response = client.get(
            "https://api.atlassian.com/oauth/token/accessible-resources",
            headers={"Authorization": f"Bearer {tokens['access_token']}"},
        )

        if response.status_code != 200:
            yaml.dump(
                {"error": f"Failed to fetch resources: {response.text}"},
                sys.stderr,
                default_flow_style=False,
            )
            sys.exit(1)

        resources = response.json()

    if not resources:
        yaml.dump(
            {"error": "No accessible Atlassian sites found"},
            sys.stderr,
            default_flow_style=False,
        )
        sys.exit(1)

    # If multiple sites, let user choose via --site argument or default to first
    if len(resources) > 1:
        if args.site:
            # Find site by name or index
            selected = None
            for r in resources:
                if r['name'].lower() == args.site.lower() or r['url'] == args.site:
                    selected = r
                    break
            if selected is None:
                try:
                    idx = int(args.site) - 1
                    if 0 <= idx < len(resources):
                        selected = resources[idx]
                except ValueError:
                    pass
            if selected is None:
                yaml.dump(
                    {
                        "error": f"Site '{args.site}' not found",
                        "available_sites": [{"index": i + 1, "name": r["name"], "url": r["url"]} for i, r in enumerate(resources)],
                        "usage": "Use --site with site name, URL, or index number",
                    },
                    sys.stderr,
                    default_flow_style=False,
                )
                sys.exit(1)
        else:
            # Show available sites and default to first
            yaml.dump(
                {
                    "info": "Multiple Atlassian sites found, using first one",
                    "selected": {"name": resources[0]["name"], "url": resources[0]["url"]},
                    "available_sites": [{"index": i + 1, "name": r["name"], "url": r["url"]} for i, r in enumerate(resources)],
                    "tip": "Use --site to select a different site",
                },
                sys.stdout,
                default_flow_style=False,
            )
            selected = resources[0]
    else:
        selected = resources[0]

    set_stored_value("cloud_id", selected["id"])
    set_stored_value("site_name", selected["name"])
    set_stored_value("site_url", selected["url"])

    yaml.dump(
        {
            "status": "success",
            "site": {"name": selected["name"], "url": selected["url"]},
            "message": "Authentication complete! You can now use Jira and Confluence scripts.",
        },
        sys.stdout,
        default_flow_style=False,
    )


def cmd_status(args):
    """Check authentication status."""
    auth_type = get_stored_value("auth_type") or "oauth"
    site_name = get_stored_value("site_name")
    site_url = get_stored_value("site_url")

    if auth_type == "basic":
        # Basic Auth (API token)
        api_email = get_stored_value("api_email")
        api_token = get_stored_value("api_token")

        if not api_email or not api_token:
            yaml.dump(
                {
                    "authenticated": False,
                    "message": "Not authenticated. Run 'uv run scripts/auth.py setup-token'",
                },
                sys.stdout,
                default_flow_style=False,
            )
            return

        yaml.dump(
            {
                "authenticated": True,
                "auth_type": "basic (API token)",
                "site": {"name": site_name, "url": site_url},
                "user": api_email,
                "token_status": "valid (API tokens don't expire)",
            },
            sys.stdout,
            default_flow_style=False,
        )
    else:
        # OAuth
        access_token = get_stored_value("access_token")
        expires_at_str = get_stored_value("expires_at")

        if not access_token:
            yaml.dump(
                {
                    "authenticated": False,
                    "message": "Not authenticated. Run 'uv run scripts/auth.py login'",
                },
                sys.stdout,
                default_flow_style=False,
            )
            return

        expires_at = float(expires_at_str) if expires_at_str else 0
        now = time.time()
        expires_in_seconds = int(expires_at - now)

        if expires_in_seconds <= 0:
            status = "expired"
        elif expires_in_seconds < 300:
            status = "expiring_soon"
        else:
            status = "valid"

        yaml.dump(
            {
                "authenticated": True,
                "auth_type": "oauth",
                "site": {"name": site_name, "url": site_url},
                "token_status": status,
                "expires_in_minutes": max(0, expires_in_seconds // 60),
            },
            sys.stdout,
            default_flow_style=False,
        )


def cmd_logout(args):
    """Clear all stored tokens and credentials."""
    keys_to_delete = [
        "access_token",
        "refresh_token",
        "expires_at",
        "cloud_id",
        "site_name",
        "site_url",
        "auth_type",
    ]

    for key in keys_to_delete:
        delete_stored_value(key)

    # Optionally clear all credentials
    if args.all:
        delete_stored_value("client_id")
        delete_stored_value("client_secret")
        delete_stored_value("api_email")
        delete_stored_value("api_token")
        yaml.dump(
            {"status": "success", "message": "All credentials and tokens cleared"},
            sys.stdout,
            default_flow_style=False,
        )
    else:
        yaml.dump(
            {
                "status": "success",
                "message": "Tokens cleared. Credentials retained.",
                "note": "Use --all to also remove OAuth/API token credentials",
            },
            sys.stdout,
            default_flow_style=False,
        )


def cmd_refresh(args):
    """Force token refresh."""
    refresh_token = get_stored_value("refresh_token")

    if not refresh_token:
        yaml.dump(
            {"error": "No refresh token. Run 'uv run scripts/auth.py login'"},
            sys.stderr,
            default_flow_style=False,
        )
        sys.exit(1)

    client_id = get_stored_value("client_id")
    client_secret = get_stored_value("client_secret")

    with httpx.Client() as client:
        response = client.post(
            "https://auth.atlassian.com/oauth/token",
            json={
                "grant_type": "refresh_token",
                "client_id": client_id,
                "client_secret": client_secret,
                "refresh_token": refresh_token,
            },
            headers={"Content-Type": "application/json"},
        )

        if response.status_code != 200:
            yaml.dump(
                {"error": f"Token refresh failed: {response.text}"},
                sys.stderr,
                default_flow_style=False,
            )
            sys.exit(1)

        tokens = response.json()

    set_stored_value("access_token", tokens["access_token"])
    set_stored_value("refresh_token", tokens["refresh_token"])
    set_stored_value("expires_at", str(time.time() + tokens["expires_in"]))

    yaml.dump(
        {
            "status": "success",
            "message": "Token refreshed",
            "expires_in_minutes": tokens["expires_in"] // 60,
        },
        sys.stdout,
        default_flow_style=False,
    )


def main():
    parser = argparse.ArgumentParser(
        description="Atlassian OAuth 2.0 authentication",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # setup command (OAuth)
    setup_parser = subparsers.add_parser("setup", help="Store OAuth client credentials")
    setup_parser.add_argument(
        "--client-id", required=True, help="OAuth Client ID from Atlassian Developer Console"
    )
    setup_parser.add_argument(
        "--client-secret", required=True, help="OAuth Client Secret from Atlassian Developer Console"
    )

    # setup-token command (API token / Basic Auth)
    token_parser = subparsers.add_parser(
        "setup-token", help="Setup using API token (reads from env vars or arguments)"
    )
    token_parser.add_argument(
        "--email", help="Atlassian account email (or set ATLASSIAN_EMAIL env var)"
    )
    token_parser.add_argument(
        "--token", help="API token (or set ATLASSIAN_API_TOKEN env var)"
    )
    token_parser.add_argument(
        "--site-url", help="Atlassian site URL e.g. https://yoursite.atlassian.net (or set ATLASSIAN_SITE_URL env var)"
    )

    # login command
    login_parser = subparsers.add_parser("login", help="Start OAuth flow, open browser")
    login_parser.add_argument(
        "--site", help="Select site by name, URL, or index (if multiple sites available)"
    )

    # status command
    subparsers.add_parser("status", help="Check authentication status")

    # logout command
    logout_parser = subparsers.add_parser("logout", help="Clear stored tokens")
    logout_parser.add_argument(
        "--all", action="store_true", help="Also remove OAuth client credentials"
    )

    # refresh command
    subparsers.add_parser("refresh", help="Force token refresh")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        "setup": cmd_setup,
        "setup-token": cmd_setup_token,
        "login": cmd_login,
        "status": cmd_status,
        "logout": cmd_logout,
        "refresh": cmd_refresh,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
