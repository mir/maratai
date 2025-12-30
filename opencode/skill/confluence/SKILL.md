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
uv run --directory ${PLUGIN_ROOT}/skill/confluence scripts/auth.py login
```

### Search with CQL
```bash
uv run --directory ${PLUGIN_ROOT}/skill/confluence scripts/confluence.py search "type=page AND space=TEAM"
```
Common CQL examples:
- `type=page AND title~'architecture'` - Pages with "architecture" in title
- `space=TEAM AND lastModified >= now('-7d')` - Recent team pages
- `creator=currentUser()` - My pages
- `label='important'` - Pages with label

```bash
# Fetch a page
uv run --directory ${PLUGIN_ROOT}/skill/confluence scripts/confluence.py get 123456789
# Get child pages
uv run --directory ${PLUGIN_ROOT}/skill/confluence scripts/confluence.py children 123456789
# List spaces
uv run --directory ${PLUGIN_ROOT}/skill/confluence scripts/confluence.py spaces
# Get parent pages (ancestors)
uv run --directory ${PLUGIN_ROOT}/skill/confluence scripts/confluence.py ancestors 123456789
# Export pages to files
uv run --directory ${PLUGIN_ROOT}/skill/confluence scripts/confluence.py export "space=TEAM" --format markdown --output-dir ./exports/
# Export to stdout (yaml default)
uv run --directory ${PLUGIN_ROOT}/skill/confluence scripts/confluence.py export "type=page AND title~'architecture'"
# Export to JSON
uv run --directory ${PLUGIN_ROOT}/skill/confluence scripts/confluence.py export "space=TEAM" --format json
```

## Authentication Status

Check if authenticated:
```bash
uv run --directory ${PLUGIN_ROOT}/skill/confluence scripts/auth.py status
```
