# /// script
# dependencies = [
#   "httpx>=0.27",
#   "keyring>=25.0",
#   "pyyaml>=6.0"
# ]
# requires-python = ">=3.12"
# ///
"""
Shared utilities for Atlassian API scripts.
Provides HTTP client with automatic token refresh and YAML output formatting.
Supports both OAuth (pure Python) and Basic Auth (API token).
"""

import base64
import functools
import json
import sys
import time
from contextlib import contextmanager
from typing import Any, Callable

import httpx
import keyring
import yaml

# Import OAuth token handling
from oauth import (
    load_tokens,
    save_tokens,
    load_client_info,
    AtlassianMCPOAuth,
    OAuthError,
)

SERVICE_NAME = "atlassian-claude-skill"


class AtlassianError(Exception):
    """Base exception for Atlassian API errors."""
    pass


class AuthenticationError(AtlassianError):
    """Token expired, invalid, or missing."""
    pass


class NotFoundError(AtlassianError):
    """Resource not found."""
    pass


class RateLimitError(AtlassianError):
    """API rate limit exceeded."""
    pass


class ConfigurationError(AtlassianError):
    """Missing configuration."""
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
        pass  # Key doesn't exist


def get_auth_type() -> str:
    """Get the configured authentication type ('basic' or 'oauth')."""
    return get_stored_value("auth_type") or "oauth"


def get_basic_auth_header() -> str:
    """
    Get Basic Auth header value for API token authentication.
    Raises AuthenticationError if credentials not configured.
    """
    email = get_stored_value("api_email")
    api_token = get_stored_value("api_token")

    if not email or not api_token:
        raise AuthenticationError(
            "API token not configured. Run: uv run scripts/auth.py setup-token"
        )

    auth_string = base64.b64encode(f"{email}:{api_token}".encode()).decode()
    return f"Basic {auth_string}"


def get_valid_token() -> str:
    """
    Get a valid OAuth access token, refreshing if necessary.
    Raises AuthenticationError if no valid token available.
    Only used for OAuth auth type.
    """
    tokens = load_tokens()
    if not tokens:
        raise AuthenticationError(
            "Not authenticated. Run: uv run scripts/auth.py login"
        )

    access_token = tokens.get("access_token")
    if not access_token:
        raise AuthenticationError(
            "No access token found. Run: uv run scripts/auth.py login"
        )

    expires_at = tokens.get("expires_at", 0)

    # Check if token is expired or expiring within 5 minutes
    if time.time() > expires_at - 300:
        # Try to refresh
        refresh_token = tokens.get("refresh_token")
        if not refresh_token:
            raise AuthenticationError(
                "Token expired and no refresh token. Run: uv run scripts/auth.py login"
            )

        client_info = load_client_info()
        if not client_info:
            raise AuthenticationError(
                "No client info. Run: uv run scripts/auth.py login"
            )

        oauth = AtlassianMCPOAuth()
        try:
            new_tokens = oauth.refresh_tokens(refresh_token, client_info["client_id"])
            save_tokens(new_tokens)
            access_token = new_tokens["access_token"]
        except OAuthError as e:
            raise AuthenticationError(
                f"Token refresh failed: {e}. Run: uv run scripts/auth.py login"
            )

    return access_token


def get_cloud_id() -> str:
    """Get the stored cloud ID."""
    cloud_id = get_stored_value("cloud_id")
    if not cloud_id:
        raise ConfigurationError(
            "No cloud ID stored. Run: uv run scripts/auth.py login"
        )
    return cloud_id


class AtlassianClient:
    """HTTP client for Atlassian APIs with automatic token refresh."""

    def __init__(self):
        self.auth_type = get_auth_type()

        if self.auth_type == "basic":
            # Basic Auth uses direct site URLs
            site_url = get_stored_value("site_url")
            if not site_url:
                raise ConfigurationError(
                    "Site URL not configured. Run: uv run scripts/auth.py setup-token"
                )
            self.jira_base = f"{site_url}/rest/api/3"
            self.confluence_base = f"{site_url}/wiki"
            self.cloud_id = None
        else:
            # OAuth uses cloud API URLs
            self.cloud_id = get_cloud_id()
            self.jira_base = (
                f"https://api.atlassian.com/ex/jira/{self.cloud_id}/rest/api/3"
            )
            self.confluence_base = (
                f"https://api.atlassian.com/ex/confluence/{self.cloud_id}"
            )

    def _get_headers(self) -> dict:
        """Get authorization headers."""
        if self.auth_type == "basic":
            auth_header = get_basic_auth_header()
        else:
            token = get_valid_token()
            auth_header = f"Bearer {token}"

        return {
            "Authorization": auth_header,
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def _handle_response(self, response: httpx.Response) -> dict | list:
        """Handle API response, raising appropriate errors."""
        if response.status_code == 401:
            raise AuthenticationError(
                "Authentication failed. Run: uv run scripts/auth.py login"
            )
        if response.status_code == 404:
            raise NotFoundError("Resource not found")
        if response.status_code == 429:
            raise RateLimitError("Rate limited. Please wait and retry.")

        response.raise_for_status()
        return response.json()

    def get(self, url: str, params: dict | None = None) -> dict | list:
        """Make GET request to Atlassian API."""
        with httpx.Client(timeout=30.0) as client:
            response = client.get(url, headers=self._get_headers(), params=params)
            return self._handle_response(response)

    def post(self, url: str, json_data: dict | None = None) -> dict | list:
        """Make POST request to Atlassian API."""
        with httpx.Client(timeout=30.0) as client:
            response = client.post(url, headers=self._get_headers(), json=json_data)
            return self._handle_response(response)

    def put(self, url: str, json_data: dict | None = None) -> dict | list:
        """Make PUT request to Atlassian API."""
        with httpx.Client(timeout=30.0) as client:
            response = client.put(url, headers=self._get_headers(), json=json_data)
            return self._handle_response(response)

    # Jira convenience methods
    def jira_get(self, endpoint: str, params: dict | None = None) -> dict | list:
        """GET request to Jira API."""
        return self.get(f"{self.jira_base}{endpoint}", params)

    def jira_post(self, endpoint: str, json_data: dict | None = None) -> dict | list:
        """POST request to Jira API."""
        return self.post(f"{self.jira_base}{endpoint}", json_data)

    def jira_put(self, endpoint: str, json_data: dict | None = None) -> dict | list:
        """PUT request to Jira API."""
        return self.put(f"{self.jira_base}{endpoint}", json_data)

    # Confluence convenience methods
    def confluence_get(self, endpoint: str, params: dict | None = None) -> dict | list:
        """GET request to Confluence API."""
        return self.get(f"{self.confluence_base}{endpoint}", params)


def yaml_output(data: Any, stream=sys.stdout) -> None:
    """
    Output data as YAML to stdout.
    Uses pure block style for all structures (no inline JSON-like formatting).
    """
    # Custom representer to force block style for dicts
    def represent_dict(dumper, data):
        return dumper.represent_mapping('tag:yaml.org,2002:map', data.items(), flow_style=False)

    # Custom representer to force block style for lists
    def represent_list(dumper, data):
        return dumper.represent_sequence('tag:yaml.org,2002:seq', data, flow_style=False)

    # Create custom dumper class
    class BlockStyleDumper(yaml.SafeDumper):
        pass

    BlockStyleDumper.add_representer(dict, represent_dict)
    BlockStyleDumper.add_representer(list, represent_list)

    yaml.dump(
        data,
        stream,
        Dumper=BlockStyleDumper,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        width=120,
    )


def error_output(message: str) -> None:
    """Output error message as YAML to stderr."""
    yaml.dump({"error": message}, sys.stderr, default_flow_style=False)
    sys.exit(1)


# ---------------------------------------------------------------------------
# MCP Utilities - shared functions for MCP client operations
# ---------------------------------------------------------------------------

def parse_mcp_result(result: Any) -> tuple[dict | list | None, str | None]:
    """
    Parse MCP tool result, handling JSON strings, lists and error responses.

    Returns:
        (parsed_result, error_message) - error_message is None if no error
    """
    # Handle list of content blocks (MCP returns list when multiple content items)
    if isinstance(result, list) and result:
        for item in result:
            if isinstance(item, dict) and item.get("type") == "text":
                text = item.get("text", "{}")
                try:
                    result = json.loads(text)
                    break
                except json.JSONDecodeError:
                    if "Failed to" in text or "Error" in text:
                        return None, text
                    return None, f"Invalid response: {text[:100]}"
        else:
            # No text block found
            return None, "No text content in MCP response"

    # Parse JSON string if needed
    if isinstance(result, str):
        try:
            result = json.loads(result)
        except json.JSONDecodeError:
            # Check if it looks like an error message
            if "Failed to" in result or "Error" in result:
                return None, result
            return None, f"Invalid response: {result[:100]}"

    # Check for MCP error response format: {"error": true, "message": "..."}
    if isinstance(result, dict) and result.get("error"):
        return None, result.get("message", "Operation failed")

    return result, None


@contextmanager
def mcp_client_context():
    """
    Context manager for MCP client lifecycle.

    Usage:
        with mcp_client_context() as client:
            result = client.call_tool(...)
    """
    # Import here to avoid circular imports
    from mcp_client import AtlassianMCPClient

    client = AtlassianMCPClient()
    try:
        yield client
    finally:
        client.close()


def command_handler(func: Callable) -> Callable:
    """
    Decorator for consistent error handling in CLI commands.

    Handles AuthenticationError, MCPError, and generic exceptions,
    outputting errors in YAML format and exiting with code 1.
    """
    # Import here to avoid circular imports
    from mcp_client import MCPError, AuthenticationError as MCPAuthError

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (AuthenticationError, MCPAuthError) as e:
            yaml.dump(
                {"error": {"message": str(e), "hint": "Run: uv run scripts/auth.py login"}},
                sys.stderr,
                default_flow_style=False,
            )
            sys.exit(1)
        except MCPError as e:
            yaml.dump(
                {"error": {"message": f"MCP error: {e}"}},
                sys.stderr,
                default_flow_style=False,
            )
            sys.exit(1)
        except ConfigurationError as e:
            yaml.dump(
                {"error": {"message": str(e), "hint": "Run: uv run scripts/auth.py login"}},
                sys.stderr,
                default_flow_style=False,
            )
            sys.exit(1)
        except Exception as e:
            yaml.dump(
                {"error": {"message": str(e)}},
                sys.stderr,
                default_flow_style=False,
            )
            sys.exit(1)

    return wrapper
