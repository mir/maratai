#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "google-api-python-client>=2.130",
#   "google-auth>=2.29",
#   "google-auth-httplib2>=0.2",
#   "google-auth-oauthlib>=1.2",
#   "markdownify>=0.13",
#   "beautifulsoup4>=4.12"
# ]
# requires-python = ">=3.12"
# ///
"""
Export Google Docs to Markdown.
"""

import argparse
import io
import sys
from pathlib import Path

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from markdownify import markdownify

# Add parent directory to path for common module
sys.path.insert(0, str(Path(__file__).parent))

from common import DEFAULT_SCOPES, AuthError, InputError, extract_id, sanitize_filename, get_credentials

DEFAULT_OUTPUT_DIR = "./exports"


def log(message: str) -> None:
    print(message, file=sys.stderr)


def get_drive_service(client_secrets: str | None):
    creds, source = get_credentials(DEFAULT_SCOPES, client_secrets)
    log(f"Auth source: {source}")
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def fetch_doc_title(drive, doc_id: str) -> str:
    metadata = drive.files().get(fileId=doc_id, fields="name").execute()
    return metadata.get("name", "document")


def export_doc_html(drive, doc_id: str) -> str:
    request = drive.files().export_media(fileId=doc_id, mimeType="text/html")
    buffer = io.BytesIO()
    downloader = MediaIoBaseDownload(buffer, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    return buffer.getvalue().decode("utf-8")


def convert_html_to_markdown(html: str) -> str:
    return markdownify(html, strip=["img"], heading_style="ATX")


def write_markdown(
    markdown: str,
    output_dir: str | None,
    filename: str,
) -> Path | None:
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


def handle_export(args: argparse.Namespace) -> int:
    doc_id = extract_id(args.doc, "document")

    drive = get_drive_service(args.client_secrets)
    title = fetch_doc_title(drive, doc_id)
    html = export_doc_html(drive, doc_id)
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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Export Google Docs to Markdown")
    subparsers = parser.add_subparsers(dest="command", required=True)

    export_parser = subparsers.add_parser("export", help="Export a Doc to Markdown")
    export_parser.add_argument("doc", help="Doc ID or URL")
    export_parser.add_argument("--stdout", action="store_true", help="Print Markdown to stdout")
    export_parser.add_argument(
        "--output-dir",
        help="Directory to write Markdown (default: ./exports when --stdout not set)",
    )
    export_parser.add_argument("--filename", help="Override output filename")
    export_parser.add_argument(
        "--client-secrets",
        help="Path to OAuth client secrets JSON for browser login fallback",
    )

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

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
