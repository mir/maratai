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
Jira API operations script.

Uses MCP client to communicate with Atlassian MCP server.

Commands:
    get <KEY>         - Fetch a single issue with all details
    search <JQL>      - Search issues using JQL
    comments <KEY>    - Get comments for an issue
    projects          - List accessible Jira projects
"""

import argparse
import json
import sys
from pathlib import Path

# Add parent directory to path for common module
sys.path.insert(0, str(Path(__file__).parent))

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


def format_user(user_data: dict | None) -> dict | None:
    """Format user data for YAML output."""
    if not user_data:
        return None
    return {
        "name": user_data.get("displayName"),
        "account_id": user_data.get("accountId"),
    }


def format_issue(issue: dict, include_comments: bool = True) -> dict:
    """Format issue data for compact YAML output."""
    fields = issue.get("fields", {})

    result = {
        "key": issue.get("key"),
        "id": issue.get("id"),
        "type": fields.get("issuetype", {}).get("name"),
        "status": fields.get("status", {}).get("name"),
        "summary": fields.get("summary"),
    }

    # Description
    description = fields.get("description")
    if description:
        # Handle ADF (Atlassian Document Format)
        if isinstance(description, dict):
            result["description"] = extract_text_from_adf(description)
        else:
            result["description"] = description

    # Dates
    result["created"] = fields.get("created")
    result["updated"] = fields.get("updated")

    # People
    result["author"] = format_user(fields.get("reporter"))
    result["assignee"] = format_user(fields.get("assignee"))

    # Priority
    priority = fields.get("priority")
    if priority:
        result["priority"] = priority.get("name")

    # Parent (for subtasks/stories in epics)
    parent = fields.get("parent")
    if parent:
        result["parent"] = {
            "key": parent.get("key"),
            "summary": parent.get("fields", {}).get("summary"),
        }

    # Labels
    labels = fields.get("labels")
    if labels:
        result["labels"] = labels

    # Comments
    if include_comments:
        comment_data = fields.get("comment", {})
        comments = comment_data.get("comments", [])
        if comments:
            result["comments"] = [
                {
                    "author": format_user(c.get("author")).get("name") if c.get("author") else None,
                    "created": c.get("created"),
                    "body": extract_text_from_adf(c.get("body")) if isinstance(c.get("body"), dict) else c.get("body"),
                }
                for c in comments
            ]

    # Attachments
    attachments = fields.get("attachment", [])
    if attachments:
        result["attachments"] = [
            {
                "filename": a.get("filename"),
                "size": a.get("size"),
                "mime_type": a.get("mimeType"),
                "url": a.get("content"),
            }
            for a in attachments
        ]

    return result


def extract_text_from_adf(adf: dict) -> str:
    """Extract plain text from Atlassian Document Format."""
    if not adf:
        return ""

    texts = []

    def extract(node):
        if isinstance(node, dict):
            if node.get("type") == "text":
                texts.append(node.get("text", ""))
            for child in node.get("content", []):
                extract(child)
        elif isinstance(node, list):
            for item in node:
                extract(item)

    extract(adf)
    return "".join(texts)


def cmd_get(args):
    """Fetch a single issue with all details via MCP."""
    client = None
    try:
        cloud_id = get_cloud_id()
        client = AtlassianMCPClient()

        result = client.call_tool(
            "getJiraIssue",
            {
                "cloudId": cloud_id,
                "issueIdOrKey": args.key,
            },
        )

        # Parse JSON result if string
        if isinstance(result, str):
            result = json.loads(result)

        yaml_output({"issue": format_issue(result)})

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
    """Search issues using JQL via MCP."""
    client = None
    try:
        cloud_id = get_cloud_id()
        client = AtlassianMCPClient()

        result = client.call_tool(
            "searchJiraIssuesUsingJql",
            {
                "cloudId": cloud_id,
                "jql": args.jql,
                "maxResults": args.limit,
            },
        )

        # Parse JSON result if string
        if isinstance(result, str):
            result = json.loads(result)

        issues = result.get("issues", [])

        output = {
            "search": {
                "jql": args.jql,
                "total": len(issues),
                "returned": len(issues),
                "issues": [],
            }
        }

        for i in issues:
            fields = i.get("fields", {})
            issue_info = {
                "key": i.get("key"),
                "type": fields.get("issuetype", {}).get("name"),
                "status": fields.get("status", {}).get("name"),
                "summary": fields.get("summary"),
            }

            # Priority
            priority = fields.get("priority")
            if priority:
                issue_info["priority"] = priority.get("name")

            # Assignee
            assignee = fields.get("assignee")
            if assignee:
                issue_info["assignee"] = assignee.get("displayName")

            # Created date
            if fields.get("created"):
                issue_info["created"] = fields.get("created")

            output["search"]["issues"].append(issue_info)

        # Add pagination info
        if result.get("nextPageToken"):
            output["search"]["has_more"] = True

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


def cmd_comments(args):
    """Get comments for an issue via MCP."""
    client = None
    try:
        cloud_id = get_cloud_id()
        client = AtlassianMCPClient()

        # First get the issue to retrieve comments
        result = client.call_tool(
            "getJiraIssue",
            {
                "cloudId": cloud_id,
                "issueIdOrKey": args.key,
            },
        )

        # Parse JSON result if string
        if isinstance(result, str):
            result = json.loads(result)

        fields = result.get("fields", {})
        comment_data = fields.get("comment", {})
        comments = comment_data.get("comments", [])

        output = {
            "comments": {
                "issue_key": args.key,
                "total": len(comments),
                "items": [
                    {
                        "id": c.get("id"),
                        "author": format_user(c.get("author")).get("name") if c.get("author") else None,
                        "created": c.get("created"),
                        "updated": c.get("updated"),
                        "body": extract_text_from_adf(c.get("body")) if isinstance(c.get("body"), dict) else c.get("body"),
                    }
                    for c in comments[:args.limit]
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


def cmd_projects(args):
    """List accessible Jira projects via MCP."""
    client = None
    try:
        cloud_id = get_cloud_id()
        client = AtlassianMCPClient()

        result = client.call_tool(
            "getVisibleJiraProjects",
            {
                "cloudId": cloud_id,
                "maxResults": args.limit,
            },
        )

        # Parse JSON result if string
        if isinstance(result, str):
            result = json.loads(result)

        projects = result.get("values", result) if isinstance(result, dict) else result

        output = {
            "projects": {
                "total": len(projects) if isinstance(projects, list) else 0,
                "items": [],
            }
        }

        if isinstance(projects, list):
            for p in projects:
                output["projects"]["items"].append({
                    "id": p.get("id"),
                    "key": p.get("key"),
                    "name": p.get("name"),
                    "type": p.get("projectTypeKey"),
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


def main():
    parser = argparse.ArgumentParser(
        description="Jira API operations (via MCP)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # get command
    get_parser = subparsers.add_parser("get", help="Fetch a single issue")
    get_parser.add_argument("key", help="Issue key (e.g., PROJ-123)")

    # search command
    search_parser = subparsers.add_parser("search", help="Search issues using JQL")
    search_parser.add_argument("jql", help="JQL query string")
    search_parser.add_argument(
        "--limit", "-l", type=int, default=25, help="Max results (default: 25)"
    )

    # comments command
    comments_parser = subparsers.add_parser("comments", help="Get comments for an issue")
    comments_parser.add_argument("key", help="Issue key (e.g., PROJ-123)")
    comments_parser.add_argument(
        "--limit", "-l", type=int, default=50, help="Max comments (default: 50)"
    )

    # projects command
    projects_parser = subparsers.add_parser("projects", help="List Jira projects")
    projects_parser.add_argument(
        "--limit", "-l", type=int, default=50, help="Max results (default: 50)"
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        "get": cmd_get,
        "search": cmd_search,
        "comments": cmd_comments,
        "projects": cmd_projects,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
