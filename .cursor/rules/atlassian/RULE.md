---
description: Access Jira issues and Confluence pages via Python scripts with OAuth
  2.0 authentication. Use when user asks about Jira tickets, issues, bugs, stories,
  epics, sprints, or Confluence pages, wiki, documentation. Outputs compact YAML to
  save tokens. Requires one-time OAuth setup. (plugin:maratai-manager@maratai)
alwaysApply: false
---
# Atlassian Skill

Access Jira and Confluence content via Python scripts. All output is YAML format for minimal token usage.

## Setup (First Time Only)

### OAuth Login

No prerequisites required - pure Python implementation.

```bash
uv run --directory .cursor/rules/atlassian scripts/auth.py login
```

This opens your browser for Atlassian OAuth consent. No need to create an OAuth app - uses Atlassian's official MCP authentication with automatic client registration.

## Jira Commands

### Fetch a ticket
```bash
uv run --directory .cursor/rules/atlassian scripts/jira.py get PROJ-123
```

Output includes: key, id, type, status, summary, description, author, assignee, parent, comments, attachments.

### Search with JQL
```bash
uv run --directory .cursor/rules/atlassian scripts/jira.py search "project=DEMO AND status='In Progress'"
```

Common JQL examples:
- `assignee=currentUser()` - My assigned issues
- `project=PROJ AND sprint in openSprints()` - Current sprint
- `reporter=currentUser() AND created >= -7d` - My recent issues
- `labels=urgent AND status!=Done` - Urgent incomplete items

### Get comments
```bash
uv run --directory .cursor/rules/atlassian scripts/jira.py comments PROJ-123
```

### Export issues to files
```bash
# Export to markdown files
uv run --directory .cursor/rules/atlassian scripts/jira.py export "project=DEMO" --format markdown --output-dir ./exports/

# Export to stdout (yaml default)
uv run --directory .cursor/rules/atlassian scripts/jira.py export "project=DEMO"

# Export to JSON
uv run --directory .cursor/rules/atlassian scripts/jira.py export "project=DEMO" --format json
```

Formats: yaml (default), json, markdown. Without --output-dir, outputs to stdout.

### List projects
```bash
uv run --directory .cursor/rules/atlassian scripts/jira.py projects
```

### Add comment to ticket
```bash
uv run --directory .cursor/rules/atlassian scripts/jira.py comment PROJ-123 "This is my comment"
```

### Get available transitions
```bash
uv run --directory .cursor/rules/atlassian scripts/jira.py transitions PROJ-123
```

### Transition ticket status
```bash
uv run --directory .cursor/rules/atlassian scripts/jira.py transition PROJ-123 "In Progress"
# Or by transition ID
uv run --directory .cursor/rules/atlassian scripts/jira.py transition PROJ-123 --id 21
```

### Create ticket
```bash
uv run --directory .cursor/rules/atlassian scripts/jira.py create PROJ --type Story --summary "My new story"
# With more options
uv run --directory .cursor/rules/atlassian scripts/jira.py create PROJ --type Bug --summary "Bug title" --description "Details here" --priority High --labels "bug,urgent"
# With custom fields (for project-specific required fields)
uv run --directory .cursor/rules/atlassian scripts/jira.py create PROJ --type Story --summary "My story" --field "Story Points=5" --field "Team=Platform"
```

### Edit ticket
```bash
uv run --directory .cursor/rules/atlassian scripts/jira.py edit PROJ-123 --summary "Updated title"
# Update multiple fields
uv run --directory .cursor/rules/atlassian scripts/jira.py edit PROJ-123 --summary "New title" --description "New description"
# Update custom fields
uv run --directory .cursor/rules/atlassian scripts/jira.py edit PROJ-123 --field "Story Points=8" --field "customfield_10001=value"
```

### Assign ticket
```bash
uv run --directory .cursor/rules/atlassian scripts/jira.py assign PROJ-123 <account_id>
# Assign to yourself
uv run --directory .cursor/rules/atlassian scripts/jira.py assign PROJ-123 --me
# Unassign
uv run --directory .cursor/rules/atlassian scripts/jira.py assign PROJ-123 --unassign
```

### List issue types for a project
```bash
uv run --directory .cursor/rules/atlassian scripts/jira.py types PROJ
```

Issue types vary by project (e.g., Story, Bug, Epic, Task, Experiment).

### List fields for an issue type
```bash
uv run --directory .cursor/rules/atlassian scripts/jira.py fields PROJ --type Story
```

Shows all available fields for an issue type, with required fields listed first. Use this to discover custom fields before creating or editing issues.

### Get current user info
```bash
uv run --directory .cursor/rules/atlassian scripts/jira.py me
```

Returns your account_id (useful for assignments).

### Lookup user by name or email
```bash
uv run --directory .cursor/rules/atlassian scripts/jira.py lookup "John Doe"
```

## Confluence Commands

### Fetch a page
```bash
uv run --directory .cursor/rules/atlassian scripts/confluence.py get 123456789
```

Output includes: id, title, space, content, author, ancestors, updated.

### Search with CQL
```bash
uv run --directory .cursor/rules/atlassian scripts/confluence.py search "type=page AND space=TEAM"
```

Common CQL examples:
- `type=page AND title~'architecture'` - Pages with "architecture" in title
- `space=TEAM AND lastModified >= now('-7d')` - Recent team pages
- `creator=currentUser()` - My pages
- `label='important'` - Pages with label

### Get child pages
```bash
uv run --directory .cursor/rules/atlassian scripts/confluence.py children 123456789
```

### List spaces
```bash
uv run --directory .cursor/rules/atlassian scripts/confluence.py spaces
```

### Get parent pages (ancestors)
```bash
uv run --directory .cursor/rules/atlassian scripts/confluence.py ancestors 123456789
```

### Export pages to files
```bash
# Export to markdown files
uv run --directory .cursor/rules/atlassian scripts/confluence.py export "space=TEAM" --format markdown --output-dir ./exports/

# Export to stdout (yaml default)
uv run --directory .cursor/rules/atlassian scripts/confluence.py export "type=page AND title~'architecture'"

# Export to JSON
uv run --directory .cursor/rules/atlassian scripts/confluence.py export "space=TEAM" --format json
```

Formats: yaml (default), json, markdown. Without --output-dir, outputs to stdout.

## Authentication Status

Check if authenticated:
```bash
uv run --directory .cursor/rules/atlassian scripts/auth.py status
```

## Write Operations Note

Write operations (comment, transition, create, edit, assign) require the `write:jira-work` OAuth scope. If you previously authenticated with read-only permissions, re-run:
```bash
uv run --directory .cursor/rules/atlassian scripts/auth.py login
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
  author:
    name: John Doe
    account_id: "5f9e8d7c"
  assignee:
    name: Jane Smith
    account_id: "5f9e8d7d"
  parent:
    key: PROJ-100
    summary: "Epic: Auth"
  comments:
    - author:
        name: John Doe
        account_id: "5f9e8d7c"
      created: "2024-01-15T11:00:00Z"
      body: "Started work"
  attachments:
    - filename: screenshot.png
      size: 45678
```

### Confluence Page
```yaml
page:
  id: "123456789"
  title: Architecture Overview
  space:
    key: TEAM
    name: Team Space
  content: |
    ## Architecture
    This document describes...
  ancestors:
    - id: "123456780"
      title: Documentation
  author:
    name: Alice
    account_id: "5f9e8d7e"
  updated: "2024-01-18T15:30:00Z"
```

### Transitions
```yaml
transitions:
  issue_key: PROJ-123
  current_status: To Do
  total: 2
  items:
    - id: "21"
      name: Start Progress
      to_status: In Progress
    - id: "31"
      name: Done
      to_status: Done
```

### Comment Added
```yaml
comment:
  issue_key: PROJ-123
  id: "10567"
  author:
    name: John Doe
    account_id: "5f9e8d7c"
  created: "2024-01-15T10:30:00Z"
```

### Issue Created
```yaml
created:
  key: PROJ-456
  id: "10234"
  type: Story
  summary: My new story
```

### Issue Types
```yaml
types:
  project: PROJ
  total: 5
  items:
    - id: "10000"
      name: Epic
      subtask: false
    - id: "10037"
      name: Story
      subtask: false
    - id: "10166"
      name: Bug
      subtask: false
```

### Issue Fields
```yaml
fields:
  project: PROJ
  issue_type: Story
  total: 12
  items:
    - name: Summary
      key: summary
      required: true
      type: string
    - name: Story Points
      key: customfield_10001
      required: true
      type: number
    - name: Description
      key: description
      required: false
      type: string
    - name: Labels
      key: labels
      required: false
      type: array
```

### Issue Edited
```yaml
edited:
  key: PROJ-123
  fields_updated:
    - summary
    - description
```

### User Info
```yaml
user:
  account_id: "712020:abc123..."
  name: John Doe
  email: john.doe@example.com
```

## Troubleshooting

### "Not authenticated" error
Run the login command shown in Setup above.

### "Token expired" error
Run the login command again to re-authenticate. OAuth tokens auto-refresh, but refresh tokens can expire after extended periods of inactivity.

### "No cloud ID" error
Re-authenticate by running the login command shown in Setup above.

### "Permission denied" on write operations
Your OAuth token may lack write permissions. Re-authenticate to get new permissions:
```bash
uv run --directory .cursor/rules/atlassian scripts/auth.py login
```

### "Transition not found" error
The target status is not available from the current issue status. Use `transitions` command to see available options.

### "Required field missing" or field validation errors
Projects often have custom required fields (e.g., Story Points, Team). To discover required fields:
```bash
uv run --directory .cursor/rules/atlassian scripts/jira.py fields PROJ --type Story
```
Then add the required fields using `--field`:
```bash
uv run --directory .cursor/rules/atlassian scripts/jira.py create PROJ --type Story --summary "Title" --field "customfield_10001=5"
```
