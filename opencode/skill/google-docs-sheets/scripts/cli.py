#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "google-api-python-client>=2.130",
#   "google-auth>=2.29",
#   "google-auth-httplib2>=0.2",
#   "google-auth-oauthlib>=1.2",
#   "markdownify>=0.13",
#   "beautifulsoup4>=4.12",
#   "requests>=2.31"
# ]
# requires-python = ">=3.12"
# ///
"""
Unified CLI for exporting Google Docs and Sheets to Markdown.

Usage:
    cli.py docs export <DOC_ID_OR_URL> [options]
    cli.py sheets export <SHEET_ID_OR_URL> [options]
"""

import argparse
import io
import os
import re
import sys
from pathlib import Path
from typing import Iterable

import google.auth
from google.auth.exceptions import DefaultCredentialsError, RefreshError
from google.auth.transport.requests import AuthorizedSession, Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from markdownify import markdownify


# =============================================================================
# Section 1: Constants & Exceptions
# =============================================================================

CONFIG_DIR = os.path.expanduser("~/.google-docs-sheets")
TOKEN_FILE = os.path.join(CONFIG_DIR, "token.json")
DEFAULT_SCOPES = (
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/documents.readonly",
)
CLIENT_SECRETS_ENV = "GOOGLE_CLIENT_SECRETS"
DEFAULT_OUTPUT_DIR = "./exports"

ID_PATTERNS = (
    re.compile(r"/d/([a-zA-Z0-9_-]+)"),
    re.compile(r"[?&]id=([a-zA-Z0-9_-]+)"),
)


class AuthError(Exception):
    """Authentication error."""


class InputError(Exception):
    """Invalid input error."""


# =============================================================================
# Section 2: Shared Utilities
# =============================================================================


def log(message: str) -> None:
    """Print a message to stderr."""
    print(message, file=sys.stderr)


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


# =============================================================================
# Section 3: Authentication
# =============================================================================


def ensure_config_dir() -> None:
    """Ensure the config directory exists."""
    Path(CONFIG_DIR).mkdir(parents=True, exist_ok=True)


def load_saved_credentials(scopes: Iterable[str]) -> Credentials | None:
    """Load saved OAuth credentials from disk."""
    if not os.path.exists(TOKEN_FILE):
        return None
    try:
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, scopes=scopes)
    except (ValueError, OSError):
        return None
    return creds


def save_credentials(creds: Credentials) -> None:
    """Save OAuth credentials to disk."""
    ensure_config_dir()
    with open(TOKEN_FILE, "w", encoding="utf-8") as handle:
        handle.write(creds.to_json())


def refresh_if_needed(creds: Credentials) -> Credentials:
    """Refresh credentials if expired."""
    if creds and creds.expired:
        creds.refresh(Request())
    return creds


def get_client_secrets_path(explicit_path: str | None) -> str | None:
    """Get the path to OAuth client secrets file."""
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
) -> tuple[Credentials, str]:
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


# =============================================================================
# Section 4: Google Docs Export
# =============================================================================


def get_drive_service(client_secrets: str | None) -> tuple:
    """Build Drive API service and return with credentials."""
    creds, source = get_credentials(DEFAULT_SCOPES, client_secrets)
    log(f"Auth source: {source}")
    drive = build("drive", "v3", credentials=creds, cache_discovery=False)
    return drive, creds


def fetch_doc_title(drive, doc_id: str) -> str:
    """Fetch document title from Drive API."""
    metadata = drive.files().get(fileId=doc_id, fields="name").execute()
    return metadata.get("name", "document")


def export_doc_html_via_api(drive, doc_id: str) -> str:
    """Export document HTML via Drive API (has 10MB limit)."""
    request = drive.files().export_media(fileId=doc_id, mimeType="text/html")
    buffer = io.BytesIO()
    downloader = MediaIoBaseDownload(buffer, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    return buffer.getvalue().decode("utf-8")


def export_doc_html_via_link(drive, creds, doc_id: str) -> str:
    """Export large docs via exportLinks (bypasses 10MB API limit)."""
    metadata = drive.files().get(fileId=doc_id, fields="exportLinks").execute()
    export_links = metadata.get("exportLinks", {})
    html_link = export_links.get("text/html")
    if not html_link:
        raise InputError(
            f"No HTML export link available. Available formats: {list(export_links.keys())}"
        )
    log("Using exportLinks fallback for large document")
    session = AuthorizedSession(creds)
    response = session.get(html_link)
    response.raise_for_status()
    return response.text


def export_doc_html(drive, creds, doc_id: str) -> str:
    """Export document as HTML, falling back to exportLinks for large files."""
    try:
        return export_doc_html_via_api(drive, doc_id)
    except HttpError as e:
        if "exportSizeLimitExceeded" in str(e):
            return export_doc_html_via_link(drive, creds, doc_id)
        raise


def convert_html_to_markdown(html: str) -> str:
    """Convert HTML to Markdown."""
    return markdownify(html, strip=["img"], heading_style="ATX")


def write_markdown(
    markdown: str,
    output_dir: str | None,
    filename: str,
) -> Path | None:
    """Write markdown content to a file."""
    if not output_dir:
        return None

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    final_name = filename
    if not final_name.lower().endswith(".md"):
        final_name = f"{final_name}.md"

    file_path = output_path / final_name
    file_path.write_text(markdown, encoding="utf-8")
    return file_path


def handle_docs_export(args: argparse.Namespace) -> int:
    """Handle the docs export command."""
    doc_id = extract_id(args.doc, "document")

    drive, creds = get_drive_service(args.client_secrets)
    title = fetch_doc_title(drive, doc_id)
    html = export_doc_html(drive, creds, doc_id)
    markdown = convert_html_to_markdown(html)

    output_dir = args.output_dir
    if not args.stdout and not output_dir:
        output_dir = DEFAULT_OUTPUT_DIR

    filename = args.filename or sanitize_filename(title, "document")
    output_path = write_markdown(markdown, output_dir, filename)

    if args.stdout:
        print(markdown)

    if output_path:
        log(f"Wrote: {output_path}")

    return 0


# =============================================================================
# Section 5: Google Sheets Export
# =============================================================================


def extract_gid(value: str) -> int | None:
    """Extract sheet gid from URL."""
    match = re.search(r"gid=([0-9]+)", value)
    if not match:
        return None
    return int(match.group(1))


def get_sheets_service(client_secrets: str | None):
    """Build Sheets API service."""
    creds, source = get_credentials(DEFAULT_SCOPES, client_secrets)
    log(f"Auth source: {source}")
    return build("sheets", "v4", credentials=creds, cache_discovery=False)


def fetch_sheet_metadata(sheets_service, spreadsheet_id: str) -> tuple[str, list[dict]]:
    """Fetch spreadsheet metadata."""
    metadata = (
        sheets_service.spreadsheets()
        .get(
            spreadsheetId=spreadsheet_id,
            fields="properties.title,sheets.properties(title,sheetId,sheetType)",
        )
        .execute()
    )
    title = metadata.get("properties", {}).get("title", "spreadsheet")
    sheets = [sheet.get("properties", {}) for sheet in metadata.get("sheets", [])]
    return title, sheets


def fetch_sheet_values(
    sheets_service, spreadsheet_id: str, sheet_title: str
) -> list[list[str]]:
    """Fetch values from a sheet tab."""
    range_name = format_sheet_range(sheet_title)
    response = (
        sheets_service.spreadsheets()
        .values()
        .get(spreadsheetId=spreadsheet_id, range=range_name)
        .execute()
    )
    return response.get("values", [])


def trim_columns(rows: list[list[str]]) -> tuple[list[list[str]], int]:
    """Trim empty trailing columns from rows."""
    max_cols = 0
    for row in rows:
        last_non_empty = 0
        for index, cell in enumerate(row):
            if str(cell).strip() != "":
                last_non_empty = index + 1
        if last_non_empty > max_cols:
            max_cols = last_non_empty

    if max_cols == 0:
        return rows, 0

    normalized = [row[:max_cols] + [""] * (max_cols - len(row)) for row in rows]
    return normalized, max_cols


def escape_cell(value: str) -> str:
    """Escape cell content for markdown tables."""
    text = "" if value is None else str(value)
    text = text.replace("\r", "")
    text = text.replace("\n", "<br>")
    text = text.replace("|", "\\|")
    return text


def format_sheet_range(sheet_title: str) -> str:
    """Format sheet title for A1 notation range."""
    if re.search(r"[ !'#:\[\]]", sheet_title):
        escaped = sheet_title.replace("'", "''")
        return f"'{escaped}'"
    return sheet_title


def render_markdown_table(rows: list[list[str]], header_row: int) -> str:
    """Render rows as a markdown table."""
    if not rows:
        return "*(empty)*"

    rows, max_cols = trim_columns(rows)
    if max_cols == 0:
        return "*(empty)*"

    header = None
    body = rows

    if header_row > 0 and header_row <= len(rows):
        header = rows[header_row - 1]
        body = rows[header_row:]

    if header is None:
        header = [f"Column {index + 1}" for index in range(max_cols)]
    else:
        header = [
            cell if str(cell).strip() != "" else f"Column {index + 1}"
            for index, cell in enumerate(header)
        ]

    header = [escape_cell(cell) for cell in header]

    lines = []
    lines.append("| " + " | ".join(header) + " |")
    lines.append("| " + " | ".join(["---"] * len(header)) + " |")

    for row in body:
        padded = row[:max_cols] + [""] * (max_cols - len(row))
        escaped = [escape_cell(cell) for cell in padded]
        lines.append("| " + " | ".join(escaped) + " |")

    return "\n".join(lines)


def render_sheet_section(sheet_title: str, table_md: str, heading_level: int) -> str:
    """Render a sheet section with heading and table."""
    prefix = "#" * heading_level
    return f"{prefix} {sheet_title}\n\n{table_md}\n"


def write_sheet_file(
    output_dir: str | None,
    spreadsheet_title: str,
    sheet_title: str,
    content: str,
) -> Path | None:
    """Write sheet content to a file."""
    if not output_dir:
        return None

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    safe_book = sanitize_filename(spreadsheet_title, "spreadsheet")
    safe_sheet = sanitize_filename(sheet_title, "sheet")
    filename = f"{safe_book} - {safe_sheet}.md"

    file_path = output_path / filename
    file_path.write_text(content, encoding="utf-8")
    return file_path


def select_sheets(
    sheets: list[dict],
    selected_titles: list[str] | None,
    gid: int | None,
) -> list[dict]:
    """Select sheets to export based on titles or gid."""
    # Filter out non-GRID sheets (like OBJECT charts) that can't be exported as tables
    grid_sheets = [s for s in sheets if s.get("sheetType", "GRID") == "GRID"]

    if selected_titles:
        selected = [sheet for sheet in grid_sheets if sheet.get("title") in selected_titles]
        return selected

    if gid is not None:
        selected = [sheet for sheet in grid_sheets if sheet.get("sheetId") == gid]
        if not selected:
            # Check if the gid exists but is a non-GRID sheet
            non_grid = [s for s in sheets if s.get("sheetId") == gid and s.get("sheetType") != "GRID"]
            if non_grid:
                sheet_type = non_grid[0].get("sheetType", "unknown")
                log(f"Sheet with gid={gid} is type '{sheet_type}' (not GRID) and cannot be exported as a table")
        return selected

    return grid_sheets


def handle_sheets_export(args: argparse.Namespace) -> int:
    """Handle the sheets export command."""
    if hasattr(args, "no_header") and args.no_header:
        args.header_row = 0

    spreadsheet_id = extract_id(args.sheet, "spreadsheet")
    gid = extract_gid(args.sheet)

    sheets_service = get_sheets_service(args.client_secrets)
    spreadsheet_title, sheets = fetch_sheet_metadata(sheets_service, spreadsheet_id)

    selected = select_sheets(sheets, args.tab, gid)
    if not selected:
        raise InputError("No matching tabs found. Check --tab or gid in URL.")

    output_dir = args.output_dir
    if not args.stdout and not output_dir:
        output_dir = DEFAULT_OUTPUT_DIR

    output_paths = []
    sheet_exports = []

    for sheet in selected:
        sheet_title = sheet.get("title", "Sheet")
        values = fetch_sheet_values(sheets_service, spreadsheet_id, sheet_title)
        table_md = render_markdown_table(values, args.header_row)
        sheet_exports.append((sheet_title, table_md))

        content = render_sheet_section(sheet_title, table_md, heading_level=1)
        output_path = write_sheet_file(output_dir, spreadsheet_title, sheet_title, content)
        if output_path:
            output_paths.append(output_path)

    if args.stdout:
        parts = [f"# {spreadsheet_title}\n"]
        for sheet_title, table_md in sheet_exports:
            parts.append(render_sheet_section(sheet_title, table_md, heading_level=2))
        print("\n".join(parts).strip())

    for path in output_paths:
        log(f"Wrote: {path}")

    return 0


# =============================================================================
# Section 6: CLI Parser
# =============================================================================


def add_common_export_args(parser: argparse.ArgumentParser) -> None:
    """Add common export arguments to a parser."""
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Print Markdown to stdout",
    )
    parser.add_argument(
        "--output-dir",
        help="Directory to write Markdown (default: ./exports when --stdout not set)",
    )
    parser.add_argument(
        "--client-secrets",
        help="Path to OAuth client secrets JSON for browser login fallback",
    )


def build_parser() -> argparse.ArgumentParser:
    """Build the unified CLI parser."""
    parser = argparse.ArgumentParser(
        prog="google-export",
        description="Export Google Docs and Sheets to Markdown",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s docs export 1abc123 --stdout
  %(prog)s sheets export 1abc123 --tab "Summary" --stdout
  %(prog)s docs export https://docs.google.com/document/d/1abc123/edit
  %(prog)s sheets export https://docs.google.com/spreadsheets/d/1abc123/edit#gid=0
        """,
    )

    subparsers = parser.add_subparsers(
        dest="service",
        required=True,
        metavar="SERVICE",
        help="Google service to use (docs, sheets)",
    )

    # Docs subcommand
    docs_parser = subparsers.add_parser(
        "docs",
        help="Google Docs operations",
        description="Export Google Docs to Markdown",
    )
    docs_subparsers = docs_parser.add_subparsers(
        dest="command",
        required=True,
        metavar="COMMAND",
    )

    docs_export = docs_subparsers.add_parser("export", help="Export a Doc to Markdown")
    docs_export.add_argument("doc", help="Doc ID or URL")
    docs_export.add_argument("--filename", help="Override output filename")
    add_common_export_args(docs_export)
    docs_export.set_defaults(handler=handle_docs_export)

    # Sheets subcommand
    sheets_parser = subparsers.add_parser(
        "sheets",
        help="Google Sheets operations",
        description="Export Google Sheets to Markdown tables",
    )
    sheets_subparsers = sheets_parser.add_subparsers(
        dest="command",
        required=True,
        metavar="COMMAND",
    )

    sheets_export = sheets_subparsers.add_parser(
        "export", help="Export tabs to Markdown files"
    )
    sheets_export.add_argument("sheet", help="Spreadsheet ID or URL")
    sheets_export.add_argument(
        "--tab",
        action="append",
        help="Sheet tab title to export (can be repeated)",
    )
    header_group = sheets_export.add_mutually_exclusive_group()
    header_group.add_argument(
        "--header-row",
        type=int,
        default=1,
        help="1-based header row index (default: 1)",
    )
    header_group.add_argument(
        "--no-header",
        action="store_true",
        help="Treat data as headerless (auto-generate headers)",
    )
    add_common_export_args(sheets_export)
    sheets_export.set_defaults(handler=handle_sheets_export)

    return parser


# =============================================================================
# Section 7: Main
# =============================================================================


def main() -> int:
    """Main entry point."""
    parser = build_parser()
    args = parser.parse_args()

    try:
        if hasattr(args, "handler"):
            return args.handler(args)
    except (AuthError, InputError) as exc:
        log(str(exc))
        return 2
    except HttpError as exc:
        log(f"Google API error: {exc}")
        return 3

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
