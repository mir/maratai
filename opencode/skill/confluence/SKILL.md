---
name: confluence
description: Access Confluence pages via Python scripts with OAuth 2.0 authentication. Use when user asks about Confluence pages, wiki, documentation.
---

# Atlassian Skill

Access Jira and Confluence content via Python scripts. All output is YAML format for minimal token usage.

### Setup OAuth

Requires [uv](https://github.com/astral-sh/uv) package manager to be installed

```bash
# install uv: curl -LsSf https://astral.sh/uv/install.sh | sh
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/auth.py login
```

This opens your browser for Atlassian OAuth consent. No need to create an OAuth app - uses Atlassian's official MCP authentication with automatic client registration.

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

### Export pages to files
```bash
# Export to markdown files
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/confluence.py export "space=TEAM" --format markdown --output-dir ./exports/

# Export to stdout (yaml default)
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/confluence.py export "type=page AND title~'architecture'"

# Export to JSON
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/confluence.py export "space=TEAM" --format json
```

Formats: yaml (default), json, markdown. Without --output-dir, outputs to stdout.

## Authentication Status

Check if authenticated:
```bash
uv run --directory ${CLAUDE_PLUGIN_ROOT}/skills/atlassian scripts/auth.py status
```
