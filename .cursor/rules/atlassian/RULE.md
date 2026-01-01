---
description: Access Jira issues and Confluence pages via Python scripts with OAuth 2.0 authentication. Use when user asks about Jira tickets, issues, bugs, stories, epics, sprints, or Confluence pages, wiki, documentation. Contains instructions to cleanup existing tickets, do status update of the tickets.
alwaysApply: false
---

# Atlassian Skill

Access Jira and Confluence content via Python scripts. All output is YAML format for minimal token usage.

# Workflows

## Ticket Cleanup (`references/jira_cleanup.md`)
**Use when:** cleanup tickets, analyze tickets, stale tickets, stuck tickets, audit tickets, ticket hygiene, review backlog, find duplicates, outdated tickets

## Status Update (`references/jira_status_update.md`)
**Use when:** update ticket status, sync commits to tickets, what did I work on, progress update, weekly update, match commits to jira

### OAuth Login

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

## Write Operations Note

Write operations (comment, transition, create, edit, assign) require the `write:jira-work` OAuth scope. If you previously authenticated with read-only permissions, re-run:
```bash
uv run --directory .cursor/rules/atlassian scripts/auth.py login
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
