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
    children <PAGE_ID>    - Get child pages
    spaces                - List Confluence spaces
    ancestors <PAGE_ID>   - Get parent pages
    export <CQL>          - Export pages to yaml/json/markdown files
"""

import argparse
import html
import json
import re
import sys
from pathlib import Path

# Add parent directory to path for common module
sys.path.insert(0, str(Path(__file__).parent))

import yaml

from common import get_stored_value, yaml_output, error_output
from mcp_client import AtlassianMCPClient, MCPError, AuthenticationError


def get_cloud_id() -> str:
    """Get the stored cloud ID."""
    cloud_id = get_stored_value("cloud_id")
    if not cloud_id:
        raise Exception(
            "No cloud ID stored. Run: uv run scripts/auth.py login"
        )
    return cloud_id


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
    space = page.get("space") or page.get("spaceId")
    if isinstance(space, dict):
        result["space"] = {
            "key": space.get("key"),
            "name": space.get("name"),
        }
    elif space:
        result["space"] = {"id": space}

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

    # Ancestors (breadcrumb)
    if page.get("ancestors"):
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


def cmd_get(args):
    """Fetch a page with content via MCP."""
    client = None
    try:
        cloud_id = get_cloud_id()
        client = AtlassianMCPClient()

        result = client.call_tool(
            "getConfluencePage",
            {
                "cloudId": cloud_id,
                "pageId": args.page_id,
                "includeBody": True,
            },
        )

        # Parse JSON result if string
        if isinstance(result, str):
            result = json.loads(result)

        yaml_output({"page": format_page(result)})

    except AuthenticationError as e:
        error_output(str(e))
    except MCPError as e:
        error_output(f"MCP error: {e}")
    except Exception as e:
        error_output(str(e))
    finally:
        if client:
            client.close()


def cmd_search(args):
    """Search pages using CQL via MCP."""
    client = None
    try:
        cloud_id = get_cloud_id()
        client = AtlassianMCPClient()

        result = client.call_tool(
            "searchConfluenceUsingCql",
            {
                "cloudId": cloud_id,
                "cql": args.cql,
                "maxResults": args.limit,
            },
        )

        # Parse JSON result if string
        if isinstance(result, str):
            result = json.loads(result)

        results = result.get("results", [])

        output = {
            "search": {
                "cql": args.cql,
                "total": result.get("totalSize", len(results)),
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

    except AuthenticationError as e:
        error_output(str(e))
    except MCPError as e:
        error_output(f"MCP error: {e}")
    except Exception as e:
        error_output(str(e))
    finally:
        if client:
            client.close()


def cmd_children(args):
    """Get child pages via MCP."""
    client = None
    try:
        cloud_id = get_cloud_id()
        client = AtlassianMCPClient()

        result = client.call_tool(
            "getConfluencePageDescendants",
            {
                "cloudId": cloud_id,
                "pageId": args.page_id,
                "maxResults": args.limit,
            },
        )

        # Parse JSON result if string
        if isinstance(result, str):
            result = json.loads(result)

        children = result.get("results", result) if isinstance(result, dict) else result

        output = {
            "children": {
                "parent_id": args.page_id,
                "total": len(children) if isinstance(children, list) else 0,
                "pages": [],
            }
        }

        if isinstance(children, list):
            for c in children:
                output["children"]["pages"].append({
                    "id": c.get("id"),
                    "title": c.get("title"),
                    "status": c.get("status"),
                })

        yaml_output(output)

    except AuthenticationError as e:
        error_output(str(e))
    except MCPError as e:
        error_output(f"MCP error: {e}")
    except Exception as e:
        error_output(str(e))
    finally:
        if client:
            client.close()


def cmd_spaces(args):
    """List Confluence spaces via MCP."""
    client = None
    try:
        cloud_id = get_cloud_id()
        client = AtlassianMCPClient()

        result = client.call_tool(
            "getConfluenceSpaces",
            {
                "cloudId": cloud_id,
                "maxResults": args.limit,
            },
        )

        # Parse JSON result if string
        if isinstance(result, str):
            result = json.loads(result)

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

    except AuthenticationError as e:
        error_output(str(e))
    except MCPError as e:
        error_output(f"MCP error: {e}")
    except Exception as e:
        error_output(str(e))
    finally:
        if client:
            client.close()


def cmd_ancestors(args):
    """Get ancestor (parent) pages via MCP."""
    client = None
    try:
        cloud_id = get_cloud_id()
        client = AtlassianMCPClient()

        # Get page with ancestors
        result = client.call_tool(
            "getConfluencePage",
            {
                "cloudId": cloud_id,
                "pageId": args.page_id,
                "includeBody": False,
            },
        )

        # Parse JSON result if string
        if isinstance(result, str):
            result = json.loads(result)

        ancestors = result.get("ancestors", [])

        output = {
            "ancestors": {
                "page_id": args.page_id,
                "page_title": result.get("title"),
                "parents": [
                    {"id": a.get("id"), "title": a.get("title")} for a in ancestors
                ],
            }
        }

        yaml_output(output)

    except AuthenticationError as e:
        error_output(str(e))
    except MCPError as e:
        error_output(f"MCP error: {e}")
    except Exception as e:
        error_output(str(e))
    finally:
        if client:
            client.close()


def cmd_export(args):
    """Export pages matching CQL query to files or stdout."""
    import os

    client = None
    try:
        cloud_id = get_cloud_id()
        client = AtlassianMCPClient()

        # Search for pages using CQL
        result = client.call_tool(
            "searchConfluenceUsingCql",
            {
                "cloudId": cloud_id,
                "cql": args.cql,
                "maxResults": args.limit,
            },
        )

        if isinstance(result, str):
            result = json.loads(result)

        search_results = result.get("results", [])
        if not search_results:
            error_output("No pages found matching the query")
            return

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
                if isinstance(full_page, str):
                    full_page = json.loads(full_page)
                formatted = format_page(full_page, include_content=True)
                exported_pages.append(formatted)
            except Exception as e:
                print(f"Warning: Could not fetch page {page_id}: {e}", file=sys.stderr)

        if not exported_pages:
            error_output("Failed to fetch any pages")
            return

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
                    content = format_page_markdown(page)
                elif args.format == "json":
                    content = json.dumps(page, indent=2)
                else:  # yaml
                    content = yaml.dump({"page": page}, default_flow_style=False, allow_unicode=True, sort_keys=False)

                with open(filepath, "w") as f:
                    f.write(content)

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

    except AuthenticationError as e:
        error_output(str(e))
    except MCPError as e:
        error_output(f"MCP error: {e}")
    except Exception as e:
        error_output(str(e))
    finally:
        if client:
            client.close()


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

    # children command
    children_parser = subparsers.add_parser("children", help="Get child pages")
    children_parser.add_argument("page_id", help="Parent page ID")
    children_parser.add_argument(
        "--limit", "-l", type=int, default=50, help="Max results (default: 50)"
    )

    # spaces command
    spaces_parser = subparsers.add_parser("spaces", help="List Confluence spaces")
    spaces_parser.add_argument(
        "--limit", "-l", type=int, default=50, help="Max results (default: 50)"
    )

    # ancestors command
    ancestors_parser = subparsers.add_parser("ancestors", help="Get parent pages")
    ancestors_parser.add_argument("page_id", help="Page ID")

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
        "ancestors": cmd_ancestors,
        "export": cmd_export,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
