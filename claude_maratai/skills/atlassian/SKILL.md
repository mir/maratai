---
name: atlassian
description: Access Jira issues and Confluence pages via Python scripts with OAuth 2.0 authentication. Use when user asks about Jira tickets, issues, bugs, stories, epics, sprints, or Confluence pages, wiki, documentation. Outputs compact YAML to save tokens. Requires one-time OAuth setup. (plugin:maratai@maratai)
---

# Atlassian Skill

Access Jira and Confluence content via Python scripts. All output is YAML format for minimal token usage.

## Setup (First Time Only)

### OAuth Login

No prerequisites required - pure Python implementation.

```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/auth.py login
```

This opens your browser for Atlassian OAuth consent. No need to create an OAuth app - uses Atlassian's official MCP authentication with automatic client registration.

## Jira Commands

### Fetch a ticket
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py get PROJ-123
```

Output includes: key, id, type, status, summary, description, author, assignee, parent, comments, attachments.

### Search with JQL
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py search "project=DEMO AND status='In Progress'"
```

Common JQL examples:
- `assignee=currentUser()` - My assigned issues
- `project=PROJ AND sprint in openSprints()` - Current sprint
- `reporter=currentUser() AND created >= -7d` - My recent issues
- `labels=urgent AND status!=Done` - Urgent incomplete items

### Get comments
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py comments PROJ-123
```

### List projects
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py projects
```

## Confluence Commands

### Fetch a page
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/confluence.py get 123456789
```

Output includes: id, title, space, content, author, ancestors, updated.

### Search with CQL
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/confluence.py search "type=page AND space=TEAM"
```

Common CQL examples:
- `type=page AND title~'architecture'` - Pages with "architecture" in title
- `space=TEAM AND lastModified >= now('-7d')` - Recent team pages
- `creator=currentUser()` - My pages
- `label='important'` - Pages with label

### Get child pages
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/confluence.py children 123456789
```

### List spaces
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/confluence.py spaces
```

### Get parent pages (ancestors)
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/confluence.py ancestors 123456789
```

## Authentication Status

Check if authenticated:
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/auth.py status
```

## Example Output

### Jira Issue
```yaml
issue:
  key: PROJ-123
  id: "10001"
  type: Story
  status: In Progress
  summary: Implement OAuth flow
  description: |
    Full description text...
  created: "2024-01-15T10:30:00Z"
  author: {name: John Doe, account_id: "5f9e8d7c"}
  assignee: {name: Jane Smith, account_id: "5f9e8d7d"}
  parent: {key: PROJ-100, summary: "Epic: Auth"}
  comments:
    - {author: John Doe, created: "2024-01-15T11:00:00Z", body: "Started work"}
  attachments:
    - {filename: screenshot.png, size: 45678}
```

### Confluence Page
```yaml
page:
  id: "123456789"
  title: Architecture Overview
  space: {key: TEAM, name: Team Space}
  content: |
    ## Architecture
    This document describes...
  ancestors:
    - {id: "123456780", title: Documentation}
  author: {name: Alice, account_id: "5f9e8d7e"}
  updated: "2024-01-18T15:30:00Z"
```

## Troubleshooting

### "Not authenticated" error
Run: `uv run --directory /path/to/skill scripts/auth.py login`

### "Token expired" error
Run `auth.py login` again to re-authenticate. OAuth tokens auto-refresh, but refresh tokens can expire after extended periods of inactivity.

### "No cloud ID" error
Re-authenticate: `uv run --directory /path/to/skill scripts/auth.py login`
