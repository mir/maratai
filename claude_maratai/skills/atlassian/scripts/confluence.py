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
Confluence API operations script.

Commands:
    get <PAGE_ID>         - Fetch a page with content
    search <CQL>          - Search pages using CQL
    children <PAGE_ID>    - Get child pages
    attachments <PAGE_ID> - Get page attachments
"""

import argparse
import html
import re
import sys
from pathlib import Path

# Add parent directory to path for common module
sys.path.insert(0, str(Path(__file__).parent))

from common import (
    AtlassianClient,
    AtlassianError,
    yaml_output,
    error_output,
)


def html_to_text(html_content: str) -> str:
    """Convert HTML content to plain text."""
    if not html_content:
        return ""

    # Remove script and style elements
    text = re.sub(r"<script[^>]*>.*?</script>", "", html_content, flags=re.DOTALL)
    text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL)

    # Convert common elements to text equivalents
    text = re.sub(r"<br\s*/?>", "\n", text)
    text = re.sub(r"</p>", "\n\n", text)
    text = re.sub(r"</div>", "\n", text)
    text = re.sub(r"</li>", "\n", text)
    text = re.sub(r"<li[^>]*>", "- ", text)
    text = re.sub(r"<h[1-6][^>]*>", "\n## ", text)
    text = re.sub(r"</h[1-6]>", "\n", text)

    # Remove all remaining HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Decode HTML entities
    text = html.unescape(text)

    # Clean up whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip()

    return text


def format_page(page: dict, include_content: bool = True) -> dict:
    """Format page data for YAML output."""
    result = {
        "id": page.get("id"),
        "title": page.get("title"),
        "status": page.get("status"),
    }

    # Space info
    space = page.get("space")
    if space:
        result["space"] = {
            "key": space.get("key"),
            "name": space.get("name"),
        }

    # Version/dates
    version = page.get("version")
    if version:
        result["version"] = version.get("number")
        result["updated"] = version.get("createdAt")
        author = version.get("by")
        if author:
            result["author"] = {
                "name": author.get("displayName"),
                "account_id": author.get("accountId"),
            }

    # Created date from history
    history = page.get("history")
    if history:
        result["created"] = history.get("createdDate")

    # Ancestors (parent pages)
    ancestors = page.get("ancestors", [])
    if ancestors:
        result["ancestors"] = [
            {"id": a.get("id"), "title": a.get("title")} for a in ancestors
        ]

    # Content
    if include_content:
        body = page.get("body", {})
        storage = body.get("storage", {})
        content_value = storage.get("value", "")
        if content_value:
            result["content"] = html_to_text(content_value)

    return result


def cmd_get(args):
    """Fetch a page with content."""
    try:
        client = AtlassianClient()

        # Use v1 API for full content with storage format
        page = client.confluence_get(
            f"/wiki/rest/api/content/{args.page_id}",
            params={
                "expand": "body.storage,space,version,ancestors,history",
            },
        )

        yaml_output({"page": format_page(page)})

    except AtlassianError as e:
        error_output(str(e))


def cmd_search(args):
    """Search pages using CQL."""
    try:
        client = AtlassianClient()

        response = client.confluence_get(
            "/wiki/rest/api/content/search",
            params={
                "cql": args.cql,
                "limit": args.limit,
                "expand": "space,version,ancestors",
            },
        )

        results = response.get("results", [])

        result = {
            "search": {
                "cql": args.cql,
                "total": response.get("totalSize", len(results)),
                "returned": len(results),
                "pages": [
                    {
                        "id": p.get("id"),
                        "title": p.get("title"),
                        "type": p.get("type"),
                        "space": p.get("space", {}).get("key"),
                        "updated": p.get("version", {}).get("when"),
                        "url": p.get("_links", {}).get("webui"),
                    }
                    for p in results
                ],
            }
        }

        # Add pagination links
        links = response.get("_links", {})
        if links.get("next"):
            result["search"]["has_more"] = True

        yaml_output(result)

    except AtlassianError as e:
        error_output(str(e))


def cmd_children(args):
    """Get child pages."""
    try:
        client = AtlassianClient()

        response = client.confluence_get(
            f"/wiki/rest/api/content/{args.page_id}/child/page",
            params={
                "limit": args.limit,
                "expand": "version",
            },
        )

        children = response.get("results", [])

        result = {
            "children": {
                "parent_id": args.page_id,
                "total": response.get("size", len(children)),
                "pages": [
                    {
                        "id": c.get("id"),
                        "title": c.get("title"),
                        "status": c.get("status"),
                        "updated": c.get("version", {}).get("when"),
                    }
                    for c in children
                ],
            }
        }

        yaml_output(result)

    except AtlassianError as e:
        error_output(str(e))


def cmd_attachments(args):
    """Get page attachments."""
    try:
        client = AtlassianClient()

        response = client.confluence_get(
            f"/wiki/rest/api/content/{args.page_id}/child/attachment",
            params={
                "limit": args.limit,
                "expand": "version",
            },
        )

        attachments = response.get("results", [])

        result = {
            "attachments": {
                "page_id": args.page_id,
                "total": response.get("size", len(attachments)),
                "items": [
                    {
                        "id": a.get("id"),
                        "title": a.get("title"),
                        "filename": a.get("title"),
                        "media_type": a.get("metadata", {})
                        .get("mediaType", a.get("extensions", {}).get("mediaType")),
                        "size": a.get("extensions", {}).get("fileSize"),
                        "download_url": a.get("_links", {}).get("download"),
                    }
                    for a in attachments
                ],
            }
        }

        yaml_output(result)

    except AtlassianError as e:
        error_output(str(e))


def cmd_ancestors(args):
    """Get ancestor (parent) pages."""
    try:
        client = AtlassianClient()

        page = client.confluence_get(
            f"/wiki/rest/api/content/{args.page_id}",
            params={"expand": "ancestors"},
        )

        ancestors = page.get("ancestors", [])

        result = {
            "ancestors": {
                "page_id": args.page_id,
                "page_title": page.get("title"),
                "parents": [
                    {"id": a.get("id"), "title": a.get("title")} for a in ancestors
                ],
            }
        }

        yaml_output(result)

    except AtlassianError as e:
        error_output(str(e))


def main():
    parser = argparse.ArgumentParser(
        description="Confluence API operations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # get command
    get_parser = subparsers.add_parser("get", help="Fetch a page with content")
    get_parser.add_argument("page_id", help="Page ID (numeric)")

    # search command
    search_parser = subparsers.add_parser("search", help="Search pages using CQL")
    search_parser.add_argument("cql", help="CQL query string")
    search_parser.add_argument(
        "--limit", "-l", type=int, default=25, help="Max results (default: 25)"
    )

    # children command
    children_parser = subparsers.add_parser("children", help="Get child pages")
    children_parser.add_argument("page_id", help="Parent page ID")
    children_parser.add_argument(
        "--limit", "-l", type=int, default=50, help="Max results (default: 50)"
    )

    # attachments command
    attach_parser = subparsers.add_parser("attachments", help="Get page attachments")
    attach_parser.add_argument("page_id", help="Page ID")
    attach_parser.add_argument(
        "--limit", "-l", type=int, default=50, help="Max results (default: 50)"
    )

    # ancestors command
    ancestors_parser = subparsers.add_parser("ancestors", help="Get parent pages")
    ancestors_parser.add_argument("page_id", help="Page ID")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        "get": cmd_get,
        "search": cmd_search,
        "children": cmd_children,
        "attachments": cmd_attachments,
        "ancestors": cmd_ancestors,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
