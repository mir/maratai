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
Jira API operations script.

Commands:
    get <KEY>         - Fetch a single issue with all details
    search <JQL>      - Search issues using JQL
    comments <KEY>    - Get comments for an issue
"""

import argparse
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
    """Fetch a single issue with all details."""
    try:
        client = AtlassianClient()

        # Fields to retrieve
        fields = [
            "summary",
            "description",
            "status",
            "issuetype",
            "priority",
            "assignee",
            "reporter",
            "created",
            "updated",
            "parent",
            "labels",
            "comment",
            "attachment",
        ]

        issue = client.jira_get(
            f"/issue/{args.key}",
            params={"fields": ",".join(fields), "expand": "renderedFields"},
        )

        yaml_output({"issue": format_issue(issue)})

    except AtlassianError as e:
        error_output(str(e))


def cmd_search(args):
    """Search issues using JQL."""
    try:
        client = AtlassianClient()

        # Use the JQL search endpoint
        search_fields = [
            "summary",
            "status",
            "issuetype",
            "priority",
            "assignee",
            "created",
            "updated",
        ]

        # POST to /search/jql for newer API
        response = client.jira_post(
            "/search/jql",
            json_data={
                "jql": args.jql,
                "maxResults": args.limit,
                "fields": search_fields,
            },
        )

        issues = response.get("issues", [])
        total = response.get("total", 0)

        result = {
            "search": {
                "jql": args.jql,
                "total": total,
                "returned": len(issues),
                "issues": [
                    {
                        "key": i.get("key"),
                        "type": i.get("fields", {}).get("issuetype", {}).get("name"),
                        "status": i.get("fields", {}).get("status", {}).get("name"),
                        "priority": i.get("fields", {}).get("priority", {}).get("name") if i.get("fields", {}).get("priority") else None,
                        "summary": i.get("fields", {}).get("summary"),
                        "assignee": format_user(i.get("fields", {}).get("assignee")).get("name") if i.get("fields", {}).get("assignee") else None,
                        "created": i.get("fields", {}).get("created"),
                    }
                    for i in issues
                ],
            }
        }

        # Add pagination token if more results
        next_token = response.get("nextPageToken")
        if next_token:
            result["search"]["next_page_token"] = next_token

        yaml_output(result)

    except AtlassianError as e:
        error_output(str(e))


def cmd_comments(args):
    """Get comments for an issue."""
    try:
        client = AtlassianClient()

        response = client.jira_get(
            f"/issue/{args.key}/comment",
            params={"maxResults": args.limit, "orderBy": "-created"},
        )

        comments = response.get("comments", [])

        result = {
            "comments": {
                "issue_key": args.key,
                "total": response.get("total", len(comments)),
                "items": [
                    {
                        "id": c.get("id"),
                        "author": format_user(c.get("author")).get("name") if c.get("author") else None,
                        "created": c.get("created"),
                        "updated": c.get("updated"),
                        "body": extract_text_from_adf(c.get("body")) if isinstance(c.get("body"), dict) else c.get("body"),
                    }
                    for c in comments
                ],
            }
        }

        yaml_output(result)

    except AtlassianError as e:
        error_output(str(e))


def main():
    parser = argparse.ArgumentParser(
        description="Jira API operations",
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

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        "get": cmd_get,
        "search": cmd_search,
        "comments": cmd_comments,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
