#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "httpx>=0.27",
#   "httpx-sse>=0.4",
#   "keyring>=25.0",
#   "pyyaml>=6.0"
# ]
# requires-python = ">=3.12"
# ///
"""
Confluence API operations script.

Uses MCP client to communicate with Atlassian MCP server.

Commands:
    get <PAGE_ID>         - Fetch a page with content
    search <CQL>          - Search pages using CQL
    children <PAGE_ID>    - Get all descendant pages
    spaces                - List Confluence spaces
    tree <PAGE_ID> [...]  - Download page tree(s) with nested folders
    export <CQL>          - Export pages to yaml/json/markdown files
"""

import argparse
import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse, parse_qs

# Add parent directory to path for common module
sys.path.insert(0, str(Path(__file__).parent))

import yaml

from common import (
    get_cloud_id,
    yaml_output,
    error_output,
    parse_mcp_result,
    mcp_client_context,
    command_handler,
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


def extract_cursor_from_links(result: dict) -> str | None:
    """Extract pagination cursor from _links.next URL."""
    links = result.get("_links", {})
    next_url = links.get("next")
    if not next_url:
        return None
    parsed = urlparse(next_url)
    params = parse_qs(parsed.query)
    cursor_list = params.get("cursor", [])
    return cursor_list[0] if cursor_list else None


def search_cql_paginated(
    client, cloud_id: str, cql: str, max_results: int = 500, per_page: int = 25
) -> tuple[list, int]:
    """Fetch results from CQL search with cursor pagination.

    Returns:
        (results_list, total_size) - list of search results and total available count
    """
    all_results = []
    cursor = None
    total_size = 0

    while len(all_results) < max_results:
        params = {
            "cloudId": cloud_id,
            "cql": cql,
            "limit": min(per_page, max_results - len(all_results)),
        }
        if cursor:
            params["cursor"] = cursor

        result = client.call_tool("searchConfluenceUsingCql", params)
        result, err = parse_mcp_result(result)
        if err:
            break

        results = result.get("results", [])
        all_results.extend(results)
        total_size = result.get("totalSize", len(all_results))

        # Get next cursor
        cursor = extract_cursor_from_links(result)
        if not cursor or not results:
            break

    return all_results, total_size


def format_page(page: dict, include_content: bool = True) -> dict:
    """Format page data for YAML output."""
    result = {
        "id": page.get("id"),
        "title": page.get("title"),
        "status": page.get("status"),
    }

    # Space info
    space = page.get("space") or page.get("spaceId")
    if isinstance(space, dict):
        result["space"] = {
            "key": space.get("key"),
            "name": space.get("name"),
        }
    elif space:
        result["space"] = {"id": space}

    # Parent page ID (from API v2)
    parent_id = page.get("parentId")
    if parent_id:
        result["parent_id"] = parent_id

    # Version/dates
    version = page.get("version")
    if version:
        if isinstance(version, dict):
            result["version"] = version.get("number")
            result["updated"] = version.get("createdAt")
            author = version.get("by")
            if author:
                result["author"] = {
                    "name": author.get("displayName"),
                    "account_id": author.get("accountId"),
                }
        else:
            result["version"] = version

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

    # Content - check both body.storage (v1 API) and body (v2 API)
    if include_content:
        body = page.get("body", {})
        if isinstance(body, dict):
            # v1 API format
            storage = body.get("storage", {})
            content_value = storage.get("value", "")
            # v2 API format
            if not content_value:
                atlas_doc = body.get("atlas_doc_format", {})
                content_value = atlas_doc.get("value", "")
        else:
            content_value = str(body) if body else ""

        if content_value:
            result["content"] = html_to_text(content_value)

    return result


def format_page_markdown(page: dict) -> str:
    """Format page as markdown document."""
    def get_user_name(user_obj):
        if not user_obj:
            return "N/A"
        if isinstance(user_obj, dict):
            return user_obj.get("name", "N/A")
        return str(user_obj)

    lines = [
        f"# {page.get('title', 'Untitled')}",
        "",
    ]

    # Metadata
    if page.get("id"):
        lines.append(f"**Page ID:** {page['id']}  ")
    if page.get("status"):
        lines.append(f"**Status:** {page['status']}  ")
    if page.get("space"):
        space = page["space"]
        if isinstance(space, dict):
            space_info = f"{space.get('name', '')} ({space.get('key', '')})" if space.get('name') else space.get('key', space.get('id', ''))
        else:
            space_info = str(space)
        lines.append(f"**Space:** {space_info}  ")
    if page.get("author"):
        lines.append(f"**Author:** {get_user_name(page.get('author'))}  ")
    if page.get("updated"):
        lines.append(f"**Updated:** {page['updated']}  ")
    if page.get("version"):
        lines.append(f"**Version:** {page['version']}  ")

    # Parent page info
    if page.get("parent_id"):
        lines.append(f"**Parent ID:** {page['parent_id']}  ")
    elif page.get("ancestors"):
        breadcrumb = " > ".join([a.get("title", a.get("id", "")) for a in page["ancestors"]])
        lines.append(f"**Path:** {breadcrumb}  ")

    lines.extend(["", "---", ""])

    # Content
    if page.get("content"):
        lines.append(page["content"])
    else:
        lines.append("_No content_")

    lines.append("")
    return "\n".join(lines)


@command_handler
def cmd_get(args):
    """Fetch a page with content via MCP."""
    cloud_id = get_cloud_id()

    with mcp_client_context() as client:
        result = client.call_tool(
            "getConfluencePage",
            {
                "cloudId": cloud_id,
                "pageId": args.page_id,
                "includeBody": True,
            },
        )

        result, error_msg = parse_mcp_result(result)
        if error_msg:
            error_output(error_msg)

        yaml_output({"page": format_page(result)})


@command_handler
def cmd_search(args):
    """Search pages using CQL via MCP."""
    cloud_id = get_cloud_id()

    with mcp_client_context() as client:
        if args.all:
            # Paginated search to fetch all results up to limit
            results, total_size = search_cql_paginated(
                client, cloud_id, args.cql, max_results=args.limit
            )
        else:
            # Single page search (faster for quick queries)
            result = client.call_tool(
                "searchConfluenceUsingCql",
                {
                    "cloudId": cloud_id,
                    "cql": args.cql,
                    "limit": args.limit,
                },
            )
            result, error_msg = parse_mcp_result(result)
            if error_msg:
                error_output(error_msg)
            results = result.get("results", [])
            total_size = result.get("totalSize", len(results))

        output = {
            "search": {
                "cql": args.cql,
                "total": total_size,
                "returned": len(results),
                "pages": [],
            }
        }

        for p in results:
            content = p.get("content", {})
            page_info = {
                "id": content.get("id"),
                "title": p.get("title") or content.get("title"),
                "type": content.get("type"),
                "url": p.get("url"),
                "excerpt": p.get("excerpt", "")[:200],
            }
            # Add space if available
            space = p.get("resultGlobalContainer", {})
            if space:
                page_info["space"] = space.get("title")
            # Add last modified
            if p.get("lastModified"):
                page_info["updated"] = p.get("lastModified")

            output["search"]["pages"].append(page_info)

        yaml_output(output)


def fetch_all_descendants_cql(client, cloud_id: str, page_id: str, max_results: int = 500) -> list:
    """Fetch all descendants using CQL via MCP with cursor pagination.

    Uses ancestor= CQL query which is more reliable than getConfluencePageDescendants API.
    """
    cql = f"ancestor={page_id}"
    results, _ = search_cql_paginated(client, cloud_id, cql, max_results=max_results)

    all_pages = []
    seen_ids = set()

    for p in results:
        content = p.get("content", {})
        page_id_found = content.get("id")
        if page_id_found and page_id_found not in seen_ids:
            seen_ids.add(page_id_found)
            page_info = {
                "id": page_id_found,
                "title": p.get("title") or content.get("title"),
                "status": content.get("status", "current"),
                "parent_id": content.get("parentId"),
            }
            all_pages.append(page_info)

    return all_pages


@command_handler
def cmd_children(args):
    """Get descendant pages using CQL ancestor= query."""
    cloud_id = get_cloud_id()

    with mcp_client_context() as client:
        children = fetch_all_descendants_cql(client, cloud_id, args.page_id, args.limit)

        output = {
            "children": {
                "parent_id": args.page_id,
                "total": len(children),
                "pages": [],
            }
        }

        for c in children:
            output["children"]["pages"].append({
                "id": c.get("id"),
                "title": c.get("title"),
                "status": c.get("status"),
            })

        yaml_output(output)


@command_handler
def cmd_spaces(args):
    """List Confluence spaces via MCP."""
    cloud_id = get_cloud_id()

    with mcp_client_context() as client:
        result = client.call_tool(
            "getConfluenceSpaces",
            {
                "cloudId": cloud_id,
                "maxResults": args.limit,
            },
        )

        result, error_msg = parse_mcp_result(result)
        if error_msg:
            error_output(error_msg)

        spaces = result.get("results", [])

        output = {
            "spaces": {
                "total": len(spaces),
                "items": [
                    {
                        "id": s.get("id"),
                        "key": s.get("key"),
                        "name": s.get("name"),
                        "type": s.get("type"),
                    }
                    for s in spaces
                ],
            }
        }

        yaml_output(output)


def sanitize_folder_name(title: str, page_id: str) -> str:
    """Create a safe folder name from page title and ID."""
    safe_title = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_')[:50]
    return f"{safe_title}_{page_id}"


@command_handler
def cmd_tree(args):
    """Download page tree(s) with proper nested folder structure."""
    import os
    import time

    cloud_id = get_cloud_id()
    ext_map = {"yaml": "yaml", "json": "json", "markdown": "md"}
    ext = ext_map.get(args.format, "md")
    toc_entries = []  # [(depth, title, relative_path)]
    downloaded_ids = set()  # Track downloaded pages to avoid duplicates
    id_to_path = {}  # Map page_id -> folder_path for nested structure

    # Adaptive rate limiting state
    rate_state = {
        "delay": args.delay,
        "min_delay": args.delay,
        "max_delay": 10.0,
        "backoff_factor": 2.0,
        "success_count": 0,
        "success_threshold": 5,  # Decrease delay after N successes
    }

    def write_page(page: dict, output_path: str):
        """Write a single page to file."""
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        if args.format == "markdown":
            content = format_page_markdown(page)
        elif args.format == "json":
            content = json.dumps(page, indent=2)
        else:  # yaml
            content = yaml.dump({"page": page}, default_flow_style=False, allow_unicode=True, sort_keys=False)

        with open(output_path, "w") as f:
            f.write(content)

    def call_with_retry(client, tool_name: str, params: dict, max_retries: int = 3):
        """Call MCP tool with exponential backoff retry on failure."""
        last_error = None
        for attempt in range(max_retries):
            try:
                result = client.call_tool(tool_name, params)
                data, err = parse_mcp_result(result)
                if err:
                    raise Exception(err)
                # Success - possibly decrease delay
                rate_state["success_count"] += 1
                if rate_state["success_count"] >= rate_state["success_threshold"]:
                    rate_state["delay"] = max(rate_state["min_delay"], rate_state["delay"] / 1.5)
                    rate_state["success_count"] = 0
                return data, None
            except Exception as e:
                last_error = e
                # Increase delay on failure
                rate_state["delay"] = min(rate_state["max_delay"], rate_state["delay"] * rate_state["backoff_factor"])
                rate_state["success_count"] = 0

                if attempt < max_retries - 1:
                    wait_time = rate_state["delay"] * (attempt + 1)
                    print(f"Request failed, retrying in {wait_time:.1f}s (delay now {rate_state['delay']:.1f}s)...", file=sys.stderr)
                    time.sleep(wait_time)
                    # Reconnect by creating new client context handled by caller
        return None, str(last_error)

    def get_depth(folder_path: str) -> int:
        """Calculate depth from folder path relative to output_dir."""
        rel_path = os.path.relpath(folder_path, args.output_dir)
        if rel_path == ".":
            return 0
        return rel_path.count(os.sep) + 1

    def process_page(client, page_id: str, stats: dict, pending_queue: list):
        """Process a single page and queue its children."""
        if page_id in downloaded_ids:
            return True

        # Rate limit delay
        if rate_state["delay"] > 0:
            time.sleep(rate_state["delay"])

        # Fetch page content
        page_data, err = call_with_retry(
            client, "getConfluencePage",
            {"cloudId": cloud_id, "pageId": page_id, "includeBody": True}
        )
        if err:
            print(f"Warning: Failed to fetch page {page_id}: {err}", file=sys.stderr)
            return False

        # Use parentId from API response for correct nesting
        # page_data is JSON string, need to parse it
        if isinstance(page_data, str):
            import json as json_mod
            page_data = json_mod.loads(page_data)

        actual_parent_id = page_data.get("parentId")

        # Determine parent folder path using actual parentId from API
        if actual_parent_id and actual_parent_id in id_to_path:
            parent_path = id_to_path[actual_parent_id]
        else:
            parent_path = args.output_dir  # Root page or parent not in our set

        # Check max_depth based on nesting level (depth 0 = root, depth 1 = children, etc.)
        depth = get_depth(parent_path)
        if args.max_depth > 0 and depth > args.max_depth:
            return True

        formatted = format_page(page_data, include_content=True)
        title = formatted.get("title", "Untitled")
        folder_name = sanitize_folder_name(title, page_id)
        folder_path = os.path.join(parent_path, folder_name)
        file_path = os.path.join(folder_path, f"index.{ext}")

        # Store path for children to reference
        id_to_path[page_id] = folder_path

        # Write page
        write_page(formatted, file_path)
        downloaded_ids.add(page_id)
        stats["pages"] += 1
        print(f"Downloaded ({stats['pages']}): {title} [delay: {rate_state['delay']:.1f}s]", file=sys.stderr)

        # Track for TOC (depth is based on folder nesting)
        relative_path = os.path.relpath(file_path, args.output_dir)
        toc_depth = get_depth(folder_path) - 1  # -1 because root pages are depth 0
        toc_entries.append((toc_depth, title, relative_path))

        # Children are already discovered via CQL upfront, no need to fetch here
        return True

    # Main execution with recovery
    os.makedirs(args.output_dir, exist_ok=True)
    stats = {"pages": 0}

    # Discover ALL descendants upfront using CQL (more reliable than getConfluencePageDescendants)
    pending_queue = list(args.page_ids)
    print(f"Discovering descendants for {len(args.page_ids)} root page(s)...", file=sys.stderr)

    with mcp_client_context() as client:
        for root_id in args.page_ids:
            descendants = fetch_all_descendants_cql(client, cloud_id, root_id, max_results=args.limit * 10)
            for desc in descendants:
                desc_id = desc.get("id")
                if desc_id and desc_id not in pending_queue:
                    pending_queue.append(desc_id)

    print(f"Found {len(pending_queue)} pages to download", file=sys.stderr)
    max_connection_retries = 5
    connection_retry = 0

    while pending_queue and connection_retry < max_connection_retries:
        try:
            with mcp_client_context() as client:
                while pending_queue:
                    page_id = pending_queue.pop(0)
                    success = process_page(client, page_id, stats, pending_queue)
                    if not success:
                        # Re-queue failed page for retry
                        pending_queue.append(page_id)
            connection_retry = 0  # Reset on successful completion
        except Exception as e:
            connection_retry += 1
            wait_time = min(30, rate_state["delay"] * connection_retry * 2)
            print(f"Connection lost: {e}. Reconnecting in {wait_time:.0f}s... (attempt {connection_retry}/{max_connection_retries})", file=sys.stderr)
            print(f"Progress: {stats['pages']} pages downloaded, {len(pending_queue)} remaining", file=sys.stderr)
            time.sleep(wait_time)
            rate_state["delay"] = min(rate_state["max_delay"], rate_state["delay"] * 2)

    # Generate TOC
    if toc_entries:
        toc_lines = ["# Table of Contents", ""]
        for depth, title, path in toc_entries:
            indent = "  " * depth
            toc_lines.append(f"{indent}- [{title}]({path})")
        toc_content = "\n".join(toc_lines) + "\n"
        toc_path = os.path.join(args.output_dir, "toc.md")
        with open(toc_path, "w") as f:
            f.write(toc_content)

    output = {
        "tree": {
            "root_page_ids": args.page_ids,
            "pages_downloaded": stats["pages"],
            "output_dir": args.output_dir,
            "format": args.format,
        }
    }
    yaml_output(output)


@command_handler
def cmd_export(args):
    """Export pages matching CQL query to files or stdout."""
    import os

    cloud_id = get_cloud_id()

    with mcp_client_context() as client:
        # Search for pages using CQL with pagination
        search_results, total_size = search_cql_paginated(
            client, cloud_id, args.cql, max_results=args.limit
        )

        if not search_results:
            error_output("No pages found matching the query")

        print(f"Found {len(search_results)} of {total_size} total pages", file=sys.stderr)

        # Fetch full details for each page
        exported_pages = []
        for p in search_results:
            content = p.get("content", {})
            page_id = content.get("id")
            if not page_id:
                continue
            try:
                full_page = client.call_tool(
                    "getConfluencePage",
                    {
                        "cloudId": cloud_id,
                        "pageId": page_id,
                        "includeBody": True,
                    },
                )
                full_page, err = parse_mcp_result(full_page)
                if err:
                    print(f"Warning: Failed to fetch page {page_id}: {err}", file=sys.stderr)
                    continue
                formatted = format_page(full_page, include_content=True)
                exported_pages.append(formatted)
            except Exception as e:
                print(f"Warning: Could not fetch page {page_id}: {e}", file=sys.stderr)

        if not exported_pages:
            error_output("Failed to fetch any pages")

        # Output based on format
        if args.output_dir:
            os.makedirs(args.output_dir, exist_ok=True)

            ext_map = {"yaml": "yaml", "json": "json", "markdown": "md"}
            ext = ext_map.get(args.format, "yaml")

            for page in exported_pages:
                # Sanitize title for filename
                title = page.get("title", page.get("id", "untitled"))
                safe_title = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_')[:50]
                filename = f"{safe_title}_{page.get('id', '')}.{ext}"
                filepath = os.path.join(args.output_dir, filename)

                if args.format == "markdown":
                    file_content = format_page_markdown(page)
                elif args.format == "json":
                    file_content = json.dumps(page, indent=2)
                else:  # yaml
                    file_content = yaml.dump({"page": page}, default_flow_style=False, allow_unicode=True, sort_keys=False)

                with open(filepath, "w") as f:
                    f.write(file_content)

            output = {
                "export": {
                    "total": len(exported_pages),
                    "format": args.format,
                    "output_dir": args.output_dir,
                    "files": [f"{re.sub(r'[^\\w\\s-]', '', p.get('title', p.get('id', 'untitled'))).strip().replace(' ', '_')[:50]}_{p.get('id', '')}.{ext}" for p in exported_pages],
                }
            }
            yaml_output(output)
        else:
            # Output to stdout
            if args.format == "markdown":
                for page in exported_pages:
                    print(format_page_markdown(page))
                    print("\n---\n")
            elif args.format == "json":
                print(json.dumps({"pages": exported_pages}, indent=2))
            else:  # yaml
                print(yaml.dump({"pages": exported_pages}, default_flow_style=False, allow_unicode=True, sort_keys=False))


def main():
    parser = argparse.ArgumentParser(
        description="Confluence API operations (via MCP)",
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
    search_parser.add_argument(
        "--all", "-a", action="store_true",
        help="Paginate through all results up to limit (default: single page)"
    )

    # children command (returns all descendants, not just direct children)
    children_parser = subparsers.add_parser("children", help="Get all descendant pages")
    children_parser.add_argument("page_id", help="Parent page ID")
    children_parser.add_argument(
        "--limit", "-l", type=int, default=50, help="Max results (default: 50)"
    )

    # spaces command
    spaces_parser = subparsers.add_parser("spaces", help="List Confluence spaces")
    spaces_parser.add_argument(
        "--limit", "-l", type=int, default=50, help="Max results (default: 50)"
    )

    # tree command
    tree_parser = subparsers.add_parser("tree", help="Download page tree(s) with nested folders")
    tree_parser.add_argument("page_ids", nargs='+', help="Root page ID(s) to download")
    tree_parser.add_argument(
        "--output-dir", "-o", required=True, help="Output directory (required)"
    )
    tree_parser.add_argument(
        "--format", "-f", choices=["yaml", "json", "markdown"], default="markdown",
        help="Output format (default: markdown)"
    )
    tree_parser.add_argument(
        "--limit", "-l", type=int, default=100, help="Max children per page (default: 100)"
    )
    tree_parser.add_argument(
        "--max-depth", type=int, default=10, help="Max recursion depth (default: 10, 0=unlimited)"
    )
    tree_parser.add_argument(
        "--delay", "-d", type=float, default=0.5, help="Delay between requests in seconds (default: 0.5)"
    )

    # export command
    export_parser = subparsers.add_parser("export", help="Export pages matching CQL query")
    export_parser.add_argument("cql", help="CQL query string")
    export_parser.add_argument(
        "--format", "-f", choices=["yaml", "json", "markdown"], default="yaml",
        help="Output format (default: yaml)"
    )
    export_parser.add_argument(
        "--output-dir", "-o", help="Directory to save files (one per page)"
    )
    export_parser.add_argument(
        "--limit", "-l", type=int, default=50, help="Max pages to export (default: 50)"
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        "get": cmd_get,
        "search": cmd_search,
        "children": cmd_children,
        "spaces": cmd_spaces,
        "tree": cmd_tree,
        "export": cmd_export,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
