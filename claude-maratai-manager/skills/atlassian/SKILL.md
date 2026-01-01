---
name: atlassian
description: Access Jira issues and Confluence pages via Python scripts with OAuth 2.0 authentication. Use when user asks about Jira tickets, issues, bugs, stories, epics, sprints, or Confluence pages, wiki, documentation. Contains instructions to cleanup existing tickets, do status update of the tickets.
---

# Atlassian Skill

Access Jira and Confluence content via Python scripts. All output is YAML format for minimal token usage.

# Workflows

## Ticket Cleanup (`references/jira_cleanup.md`)
**Use when:** cleanup tickets, analyze tickets, stale tickets, stuck tickets, audit tickets, ticket hygiene, review backlog, find duplicates, outdated tickets

## Status Update (`references/jira_status_update.md`)
**Use when:** update ticket status, sync commits to tickets, what did I work on, progress update, weekly update, match commits to jira

# OAuth Login
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/auth.py login
```

# Jira Commands

```bash
# List projects
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py projects

## List issue types for a project
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py types PROJ

# Fetch a ticket
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py get PROJ-123

# Search with JQL
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py search "project=DEMO AND status='In Progress'"

# Get comments
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py comments PROJ-123
```

Common JQL examples:
- `assignee=currentUser()` - My assigned issues
- `project=PROJ AND sprint in openSprints()` - Current sprint
- `reporter=currentUser() AND created >= -7d` - My recent issues
- `labels=urgent AND status!=Done` - Urgent incomplete items

### Export issues to files
```bash
# Export to markdown files
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py export "project=DEMO" --format markdown --output-dir ./exports/

# Export to stdout (yaml default)
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py export "project=DEMO"

# Export to JSON
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py export "project=DEMO" --format json
```

## Edit

```bash
# Add comment to ticket
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py comment PROJ-123 "This is my comment"

# Get available transitions
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py transitions PROJ-123

# Transition ticket status
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py transition PROJ-123 "In Progress"

# Or by transition ID
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py transition PROJ-123 --id 21
```

## Create ticket
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py create PROJ --type Story --summary "My new story"
# With more options
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py create PROJ --type Bug --summary "Bug title" --description "Details here" --priority High --labels "bug,urgent"
# With custom fields (for project-specific required fields)
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py create PROJ --type Story --summary "My story" --field "Story Points=5" --field "Team=Platform"
```

## Edit ticket
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py edit PROJ-123 --summary "Updated title"
# Update multiple fields
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py edit PROJ-123 --summary "New title" --description "New description"
# Update custom fields
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py edit PROJ-123 --field "Story Points=8" --field "customfield_10001=value"
```

## Assign ticket
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py assign PROJ-123 <account_id>
# Assign to yourself
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py assign PROJ-123 --me
# Unassign
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py assign PROJ-123 --unassign
```

## List fields for an issue type
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py fields PROJ --type Story
```

## Get current user info
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py me
```

## Lookup user by name or email
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py lookup "John Doe"
```

# Confluence Commands

```bash
# Fetch a page
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/confluence.py get 123456789

# Search with CQL
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/confluence.py search "type=page AND space=TEAM"

# Get child pages
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/confluence.py children 123456789

$ List spaces
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/confluence.py spaces
```

Common CQL examples:
- `type=page AND title~'architecture'` - Pages with "architecture" in title
- `space=TEAM AND lastModified >= now('-7d')` - Recent team pages
- `creator=currentUser()` - My pages
- `label='important'` - Pages with label

# Get parent pages (ancestors)
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/confluence.py ancestors 123456789
```

# Export pages to files
```bash
# Export to markdown files
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/confluence.py export "space=TEAM" --format markdown --output-dir ./exports/

# Export to stdout (yaml default)
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/confluence.py export "type=page AND title~'architecture'"

# Export to JSON
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/confluence.py export "space=TEAM" --format json
```

# Troubleshooting

# "Not authenticated" error
Run the login command shown in Setup above.

# "Token expired" error
Run the login command again to re-authenticate. OAuth tokens auto-refresh, but refresh tokens can expire after extended periods of inactivity.

# "No cloud ID" error
Re-authenticate by running the login command shown in Setup above.

# "Permission denied" on write operations
Your OAuth token may lack write permissions. Re-authenticate to get new permissions:
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/auth.py login
```

# "Transition not found" error
The target status is not available from the current issue status. Use `transitions` command to see available options.

# "Required field missing" or field validation errors
Projects often have custom required fields (e.g., Story Points, Team). To discover required fields:
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py fields PROJ --type Story
```
Then add the required fields using `--field`:
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/jira.py create PROJ --type Story --summary "Title" --field "customfield_10001=5"
```
