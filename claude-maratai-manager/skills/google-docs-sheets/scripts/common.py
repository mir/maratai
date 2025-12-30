import os
import re
from pathlib import Path
from typing import Iterable, Tuple

import google.auth
from google.auth.exceptions import DefaultCredentialsError, RefreshError
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

CONFIG_DIR = os.path.expanduser("~/.google-docs-sheets")
TOKEN_FILE = os.path.join(CONFIG_DIR, "token.json")
DEFAULT_SCOPES = (
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/spreadsheets.readonly",
)
CLIENT_SECRETS_ENV = "GOOGLE_CLIENT_SECRETS"


class AuthError(Exception):
    """Authentication error."""


class InputError(Exception):
    """Invalid input error."""


ID_PATTERNS = (
    re.compile(r"/d/([a-zA-Z0-9_-]+)"),
    re.compile(r"[?&]id=([a-zA-Z0-9_-]+)"),
)


def extract_id(value: str, kind: str) -> str:
    """Extract a document or spreadsheet ID from a URL or raw ID."""
    if not value:
        raise InputError(f"Missing {kind} id")

    if re.fullmatch(r"[a-zA-Z0-9_-]+", value):
        return value

    for pattern in ID_PATTERNS:
        match = pattern.search(value)
        if match:
            return match.group(1)

    raise InputError(
        f"Could not parse {kind} id from input. Expected an ID or a Google {kind} URL."
    )


def sanitize_filename(name: str, fallback: str) -> str:
    """Sanitize filenames to avoid problematic characters."""
    if not name:
        name = fallback
    sanitized = re.sub(r"[^A-Za-z0-9._ -]+", "_", name).strip()
    sanitized = re.sub(r"\s+", " ", sanitized)
    if not sanitized:
        sanitized = fallback
    return sanitized


def ensure_config_dir() -> None:
    Path(CONFIG_DIR).mkdir(parents=True, exist_ok=True)


def load_saved_credentials(scopes: Iterable[str]) -> Credentials | None:
    if not os.path.exists(TOKEN_FILE):
        return None
    try:
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, scopes=scopes)
    except (ValueError, OSError):
        return None
    return creds


def save_credentials(creds: Credentials) -> None:
    ensure_config_dir()
    with open(TOKEN_FILE, "w", encoding="utf-8") as handle:
        handle.write(creds.to_json())


def refresh_if_needed(creds: Credentials) -> Credentials:
    if creds and creds.expired:
        creds.refresh(Request())
    return creds


def get_client_secrets_path(explicit_path: str | None) -> str | None:
    if explicit_path:
        return explicit_path

    env_path = os.environ.get(CLIENT_SECRETS_ENV)
    if env_path:
        return env_path

    default_path = os.path.join(CONFIG_DIR, "client_secret.json")
    if os.path.exists(default_path):
        return default_path

    return None


def get_credentials(
    scopes: Iterable[str] = DEFAULT_SCOPES,
    client_secrets_path: str | None = None,
) -> Tuple[Credentials, str]:
    """Return credentials and a label for the auth source."""
    try:
        creds, _ = google.auth.default(scopes=scopes)
        if creds:
            creds = refresh_if_needed(creds)
            return creds, "gcloud"
    except DefaultCredentialsError:
        pass
    except RefreshError:
        pass

    creds = load_saved_credentials(scopes)
    if creds:
        try:
            creds = refresh_if_needed(creds)
            return creds, "token"
        except RefreshError:
            pass

    client_path = get_client_secrets_path(client_secrets_path)
    if not client_path:
        raise AuthError(
            "Missing OAuth client secrets. Set GOOGLE_CLIENT_SECRETS or pass --client-secrets."
        )

    ensure_config_dir()
    flow = InstalledAppFlow.from_client_secrets_file(client_path, scopes=scopes)
    creds = flow.run_local_server(port=0)
    save_credentials(creds)
    return creds, "oauth"
