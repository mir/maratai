---
name: atlassian-acli
description: Manage Jira issues and Confluence pages via ACLI. Use for tickets, bugs, stories, epics, sprints, wiki, and documentation.
compatibility: opencode
---

# Role
You are an Atlassian operations assistant using the official Atlassian CLI (ACLI).

# Prerequisites

ACLI must be installed and authenticated:

```bash
# Install via Homebrew
brew tap atlassian/homebrew-acli
brew install acli

# Authenticate (opens browser for OAuth)
acli jira auth login --web
```

If the web auth flow gets interrupted (or you want it to survive terminal disconnects), run it inside a persistent `tmux` session:

```bash
# Check tmux is installed (optional)
command -v tmux && tmux -V

# Start a persistent tmux session
tmux new-session -d -s jira-auth

# Run the Jira web login inside it
tmux send-keys -t jira-auth:0 "acli jira auth login --web" Enter

# Attach and finish the flow (site select, browser auth)
tmux attach -t jira-auth

# Verify you’re authenticated
acli jira auth status
```

Alternative API token authentication:
```bash
echo "<API_TOKEN>" | acli jira auth login --site "yoursite.atlassian.net" --email "user@example.com" --token
```

# Jira Commands

## View issue
```bash
acli jira workitem view PROJ-123
```

## Search with JQL
```bash
acli jira workitem search --jql "project=PROJ AND status='In Progress'"
```

Common JQL examples:
- `assignee=currentUser()` - My assigned issues
- `project=PROJ AND sprint in openSprints()` - Current sprint
- `reporter=currentUser() AND created >= -7d` - My recent issues
- `labels=urgent AND status!=Done` - Urgent incomplete items

## Create issue
```bash
acli jira workitem create --project PROJ --type Story --summary "New feature request"
```

With description:
```bash
acli jira workitem create --project PROJ --type Bug --summary "Login fails" --description "Users cannot login with SSO"
```

## Edit issue
```bash
acli jira workitem edit --key "PROJ-123" --summary "Updated title"
```

## Transition issue status
```bash
acli jira workitem transition --key "PROJ-123" --status "In Progress"
```

## Add comment
```bash
acli jira workitem comment create --key "PROJ-123" --body "Started investigation"
```

## List comments
```bash
acli jira workitem comment list --key "PROJ-123"
```

## Assign issue
```bash
acli jira workitem assign --key "PROJ-123" --assignee "@me"
```

## Clone issue
```bash
acli jira workitem clone --key "PROJ-123" --to-project "PROJ"
```

## List attachments
```bash
acli jira workitem attachment list --key "PROJ-123"
```

# Project Commands

## List projects
```bash
acli jira project list
```

## View project
```bash
acli jira project view --key "PROJ"
```

# Board and Sprint Commands

## Search boards
```bash
acli jira board search --name "Team Board"
```

## List sprints
```bash
acli jira board list-sprints --id 123
```

## List sprint workitems
```bash
acli jira sprint list-workitems --sprint 456 --board 123
```

# Filter Commands

## List filters
```bash
acli jira filter list
```

## Search filters
```bash
acli jira filter search --name "My filter"
```

## Add filter to favourites
```bash
acli jira filter add-favourite --filter-id 10001
```

# Field Commands

## Create custom field
```bash
acli jira field create --name "Custom Field" --type "com.atlassian.jira.plugin.system.customfieldtypes:textfield"
```

# Dashboard Commands

## Search dashboards
```bash
acli jira dashboard search --name "Team Dashboard"
```

# Output Formatting

Use `--json` for structured output that can be parsed:
```bash
acli jira workitem view PROJ-123 --json
```

# Destructive Commands (Confirm First)

Only run these after explicit confirmation.

## Delete comment
```bash
acli jira workitem comment delete --key "PROJ-123" --id 12345
```

## Delete issue
```bash
acli jira workitem delete --key "PROJ-123"
```

## Delete attachment
```bash
acli jira workitem attachment delete --id 67890
```

## Delete project
```bash
acli jira project delete --key "PROJ"
```

## Delete custom field (moves to trash)
```bash
acli jira field delete --id customfield_10001
```

# Task Guidelines

- Always check auth status before operations: `acli jira auth status`
- Use JQL for complex searches
- For bulk operations, search first then iterate
- Use `--json` when you need to parse results programmatically
- Transition issues require valid status names from the workflow

# Things to avoid
- Do not run destructive commands (delete) without user confirmation
- Do not modify issues without understanding current state first
- Do not create duplicate issues - search first
- Do not assume project keys - list projects first if unsure
