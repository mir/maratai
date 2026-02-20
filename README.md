maratai
=======

Reusable [Agent Skills](https://agentskills.io), workflow templates, and helper
scripts that keep Marat's multi-agent coding assistants in sync. The repository
centralizes the instructions used by Claude Code, OpenCode, Codex CLI, and
Gemini CLI so they can be edited once and deployed to any compatible tool.

Repository Layout
-----------------
- `claude-maratai-dev/` – Claude Code plugin for development workflows
  with skills for auto-commit and feature planning.
- `claude-maratai-manager/` – Claude Code plugin for management
  workflows with Atlassian integration (Jira & Confluence), Google Docs/Sheets
  export, and weekly reporting tools.
- `claude-maratai-data/` – Claude Code plugin for data analytics
  workflows with database querying via command-line clients (psql,
  mysql, clickhouse-client, bq, snowsql, etc.).
- `agentskills/` – Canonical Agent Skills (SKILL.md files) following the
  open [Agent Skills standard](https://agentskills.io). Deployable to any
  compatible CLI tool.
- `opencode.json` – OpenCode-specific configuration (MCP and formatter
  settings), kept at repo root.
- `transfer_from_claude.py` – utility that copies Markdown from
  `claude-maratai-dev/` and `claude-maratai-manager/` to `agentskills/`,
  transforming frontmatter for Agent Skills format.
- `sync_skills.sh` – multi-target sync script that deploys skills from
  `agentskills/` to one or more CLI tool config directories, with path variable
  substitution, orphan cleanup, and interactive target selection.

Supported Targets
-----------------
| Target     | Skills directory              | Path variable    | Detection              |
|------------|-------------------------------|------------------|------------------------|
| opencode   | `~/.config/opencode/skill/`   | `${OPENCODE_DIR}` | `~/.config/opencode/` exists |
| codex      | `~/.codex/skills/`            | `${CODEX_DIR}`   | `~/.codex/` exists     |
| gemini     | `~/.gemini/skills/`           | `${GEMINI_DIR}`  | `~/.gemini/` exists    |

During sync, the canonical `${AGENTSKILLS_DIR}` variable in `.md` and `.py`
files is replaced with the target-specific path variable (e.g.
`${OPENCODE_DIR}`). Binary files are copied as-is.

Daily Workflow
--------------
1. Edit or add skills inside `claude-maratai-dev/` (or `claude-maratai-manager/`
   for management tools) first so metadata stays consistent across platforms.
2. Run `./transfer_from_claude.py` (requires [uv](https://github.com/astral-sh/uv))
   to refresh the Agent Skills copies with proper frontmatter transformation.
3. Use the sync script when you are ready to deploy skills locally:

   ```bash
   ./sync_skills.sh                    # interactive target selection
   ./sync_skills.sh -t opencode        # sync to opencode only
   ./sync_skills.sh -t opencode,codex  # sync to multiple targets
   ./sync_skills.sh -n                 # dry-run (preview changes)
   ./sync_skills.sh -d -t codex        # show diffs for codex target
   ./sync_skills.sh -n -d              # dry-run with diffs
   ```

   The script creates missing directories, replaces existing files, performs
   path variable substitution, and removes orphaned files in each target.

Adding or Updating Skills
-------------------------
- Keep YAML front matter at the top of each `SKILL.md` file; the metadata is
  used by all supported tools.
- Use `${AGENTSKILLS_DIR}` for path references in canonical SKILL.md files.
  The sync script substitutes the correct variable per target during deploy.
- Prefer short, action-oriented descriptions and keep output format sections in
  Markdown so they render cleanly in every client.
- Confirm any Mermaid diagrams render by pasting them into your client before
  shipping changes.

Skill Reference (maratai-dev)
-----------------------------
- **`skills/commit/`** – auto-commit with smart branching. Captures outstanding
  changes, branches off `main` when needed, stages, commits with a concise
  message, pushes, and prompts the user to file a merge request via `glab`.

Skill Reference (maratai-manager)
---------------------------------
- **`skills/week-report/`** – weekly status writer. Inspects repo changes for
  the past 7 days, groups related changes, and prepares a demo-ready report.
- **`skills/jira-confluence/`** – Jira and Confluence integration via OAuth 2.0.
  Access issues, projects, sprints, and wiki pages through Python scripts with
  compact YAML output to save tokens. Run `scripts/auth.py login` for setup.
  Includes workflows:
  - **`workflows/jira-cleanup.md`** – ticket hygiene workflow for analyzing
    stale tickets, finding duplicates, and cleaning up backlogs.
  - **`workflows/jira-status-update.md`** – matches git commits from the last
    7 days against Jira tickets to draft status update comments.
- **`skills/google-docs-sheets/`** – Export Google Docs and Google Sheets to
  Markdown. Uses Google APIs with read-only scopes. Prefers gcloud ADC
  authentication with browser OAuth fallback. Useful for ingesting Google
  Workspace content for summarization or analysis.
- **`skills/demo-page/`** – Generate a polished, self-contained HTML demo page
  from any source material (feature descriptions, ticket lists, release notes,
  or free-form conversation). Tells a narrative story about real user problems
  being solved rather than a plain changelog.

Skill Reference (maratai-data)
-------------------------------
- **`skills/data-analyst/`** – Database analytics via command-line clients
  (psql, mysql, clickhouse-client, bq, snowsql, etc.). Explores schemas,
  runs analytical SQL queries, formats results as markdown tables, and follows
  best practices (CTEs, LIMIT, EXPLAIN ANALYZE, date functions). Connection
  managed via `DB_HOST`, `DB_PORT`, `DB_DATABASE`, `DB_USER`, `DB_PASSWORD`
  environment variables.

Claude Code Plugins
-------------------
To install the Claude Code plugins, run these commands inside Claude Code's
interactive mode:

1. Add the marketplace (one-time setup):
   ```
   /plugin marketplace add mir/maratai
   ```

2. Install the plugins:
   ```
   /plugin install maratai-dev@maratai    # Development workflows
   /plugin install maratai-manager@maratai # Management workflows (Atlassian)
   /plugin install maratai-data@maratai    # Data analytics (multi-database)
   ```

3. Verify installation:
   ```
   /plugin marketplace list   # List configured marketplaces
   /plugin                    # Open interactive plugin browser
   ```

Troubleshooting
---------------
- The transfer script transforms Claude Code frontmatter to Agent Skills format
  (removes `name`, `model`, `tools` fields; adds `mode: subagent` for agents).
- When new dependencies are needed for the Python script, update the inline
  `uv` metadata block inside `transfer_from_claude.py`.
- Keep an eye on trailing commas in JSON files such as `opencode.json`;
  tool validation may be stricter than local tooling.
- The `sync_skills.sh` script removes orphaned files from each target directory
  that don't exist in `agentskills/`. Use `--dry-run` to preview changes first.
