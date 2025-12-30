#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "google-api-python-client>=2.130",
#   "google-auth>=2.29",
#   "google-auth-httplib2>=0.2",
#   "google-auth-oauthlib>=1.2"
# ]
# requires-python = ">=3.12"
# ///
"""
Export Google Sheets tabs to Markdown tables.
"""

import argparse
import re
import sys
from pathlib import Path

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Add parent directory to path for common module
sys.path.insert(0, str(Path(__file__).parent))

from common import DEFAULT_SCOPES, AuthError, InputError, extract_id, sanitize_filename, get_credentials

DEFAULT_OUTPUT_DIR = "./exports"


def log(message: str) -> None:
    print(message, file=sys.stderr)


def extract_gid(value: str) -> int | None:
    match = re.search(r"gid=([0-9]+)", value)
    if not match:
        return None
    return int(match.group(1))


def get_sheets_service(client_secrets: str | None):
    creds, source = get_credentials(DEFAULT_SCOPES, client_secrets)
    log(f"Auth source: {source}")
    return build("sheets", "v4", credentials=creds, cache_discovery=False)


def fetch_sheet_metadata(sheets_service, spreadsheet_id: str) -> tuple[str, list[dict]]:
    metadata = (
        sheets_service.spreadsheets()
        .get(
            spreadsheetId=spreadsheet_id,
            fields="properties.title,sheets.properties",
        )
        .execute()
    )
    title = metadata.get("properties", {}).get("title", "spreadsheet")
    sheets = [sheet.get("properties", {}) for sheet in metadata.get("sheets", [])]
    return title, sheets


def fetch_sheet_values(sheets_service, spreadsheet_id: str, sheet_title: str) -> list[list[str]]:
    range_name = format_sheet_range(sheet_title)
    response = (
        sheets_service.spreadsheets()
        .values()
        .get(spreadsheetId=spreadsheet_id, range=range_name)
        .execute()
    )
    return response.get("values", [])


def trim_columns(rows: list[list[str]]) -> tuple[list[list[str]], int]:
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
    text = "" if value is None else str(value)
    text = text.replace("\r", "")
    text = text.replace("\n", "<br>")
    text = text.replace("|", "\\|")
    return text


def format_sheet_range(sheet_title: str) -> str:
    if re.search(r"[ !'\\[\\]#:]", sheet_title):
        escaped = sheet_title.replace("'", "''")
        return f"'{escaped}'"
    return sheet_title


def render_markdown_table(rows: list[list[str]], header_row: int) -> str:
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
    prefix = "#" * heading_level
    return f"{prefix} {sheet_title}\n\n{table_md}\n"


def write_sheet_file(
    output_dir: str | None,
    spreadsheet_title: str,
    sheet_title: str,
    content: str,
) -> Path | None:
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
    if selected_titles:
        selected = [sheet for sheet in sheets if sheet.get("title") in selected_titles]
        return selected

    if gid is not None:
        selected = [sheet for sheet in sheets if sheet.get("sheetId") == gid]
        return selected

    return sheets


def handle_export(args: argparse.Namespace) -> int:
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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Export Google Sheets tabs to Markdown tables")
    subparsers = parser.add_subparsers(dest="command", required=True)

    export_parser = subparsers.add_parser("export", help="Export tabs to Markdown files")
    export_parser.add_argument("sheet", help="Spreadsheet ID or URL")
    export_parser.add_argument(
        "--stdout", action="store_true", help="Print Markdown to stdout"
    )
    export_parser.add_argument(
        "--output-dir",
        help="Directory to write Markdown (default: ./exports when --stdout not set)",
    )
    export_parser.add_argument(
        "--tab",
        action="append",
        help="Sheet tab title to export (can be repeated)",
    )
    header_group = export_parser.add_mutually_exclusive_group()
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
    export_parser.add_argument(
        "--client-secrets",
        help="Path to OAuth client secrets JSON for browser login fallback",
    )

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "export" and args.no_header:
        args.header_row = 0

    try:
        if args.command == "export":
            return handle_export(args)
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
