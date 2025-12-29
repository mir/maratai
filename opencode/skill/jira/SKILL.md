---
name: jira
description: Manage Jira issues via atlassian cli tool (acli). Use for tickets, bugs, stories, epics, sprints, and others.
compatibility: opencode
---

## What I do

- View and search Jira issues using JQL queries
- Create, edit, and transition issues (bugs, stories, tasks, epics)
- Manage comments and attachments on issues
- Work with boards, sprints, and dashboards
- Execute ACLI commands for Atlassian products

## When to use me

Use this when working with Jira tickets, issues, sprints, or boards.
Ask clarifying questions if the project key or issue type is unclear.

# Prerequisites

ACLI must be installed and authenticated:

```bash
# Install via Homebrew
brew tap atlassian/homebrew-acli
brew install acli

# Authenticate (opens browser for OAuth)
# After the login through browser is done, acli requires 'enter' key to be pressed
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

## View
```bash
# list projects
acli jira project list
acli jira project view --key "PROJ"
# view issues
acli jira workitem view PROJ-123
# search with jql
acli jira workitem search --jql "project=PROJ AND status='In Progress'"
# show comments
acli jira workitem comment list --key "PROJ-123"
# list attachments
acli jira workitem attachment list --key "PROJ-123"
```

Common JQL examples:
- `assignee=currentUser()` - My assigned issues
- `project=PROJ AND sprint in openSprints()` - Current sprint
- `reporter=currentUser() AND created >= -7d` - My recent issues
- `labels=urgent AND status!=Done` - Urgent incomplete items

## Managing issues
```bash
# create
acli jira workitem create --project PROJ --type Bug --summary "Login fails" --description "Users cannot login with SSO"
# edit
acli jira workitem edit --key "PROJ-123" --summary "Updated title"
# change status
acli jira workitem transition --key "PROJ-123" --status "In Progress"
# comment
acli jira workitem comment create --key "PROJ-123" --body "Started investigation"
# assign
acli jira workitem assign --key "PROJ-123" --assignee "@me"
# clone
acli jira workitem clone --key "PROJ-123" --to-project "PROJ"
```

# Board and Sprint Commands

```bash
# Search boards
acli jira board search --name "Team Board"
## List sprints
acli jira board list-sprints --id 123
## List sprint workitems
acli jira sprint list-workitems --sprint 456 --board 123
```

# Dashboard Commands

```bash
## Search dashboards
acli jira dashboard search --name "Team Dashboard"
```

# Output Formatting

Use `--json` for structured output that can be parsed:
```bash
acli jira workitem view PROJ-123 --json
```

# Destructive Commands (Confirm First)
Only run these after explicit confirmation.
```bash
## Delete comment
acli jira workitem comment delete --key "PROJ-123" --id 12345

## Delete issue
acli jira workitem delete --key "PROJ-123"

## Delete attachment
acli jira workitem attachment delete --id 67890
```

# Task Guidelines
- If command fails check the auth status: `acli jira auth status`
- Use --help for `acli` to discrover additional managing tools, if the described ones are not enough.
- Use JQL for complex searches
- For bulk operations write python scripts
- Use `--json` when you need to parse results programmatically
- Transition issues require valid status names from the workflow

# Things to avoid
- Do not run destructive commands (delete) without user confirmation
- Do not modify issues without understanding current state first
- Do not create duplicate issues - search first
- Do not assume project keys - list projects first if unsure
