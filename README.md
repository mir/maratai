maratai
=======

Reusable skills, workflow templates, and helper scripts that keep Marat's
multi-agent coding assistants in sync. The repository centralizes the
instructions used by Claude Code and OpenCode so they can be edited once and
re-used across tools.

Repository Layout
-----------------
- `claude-maratai-dev/` (v1.0.1) – Claude Code plugin for development workflows
  with skills for auto-commit and feature planning.
- `claude-maratai-manager/` (v1.26.0) – Claude Code plugin for management
  workflows with Atlassian integration (Jira & Confluence), Google Docs/Sheets
  export, and weekly reporting tools.
- `opencode/` – OpenCode-compatible copies of the same skills; also contains
  `opencode.json` with local MCP and formatter settings.
- `transfer_from_claude.py` – utility that copies Markdown from
  `claude-maratai-dev/` and `claude-maratai-manager/` to `opencode/`,
  transforming frontmatter for OpenCode format.
- `sync_opencode.sh` – helper script that syncs the local prompts into
  OpenCode's configuration directory (`~/.config/opencode/`), including orphan
  cleanup.

Daily Workflow
--------------
1. Edit or add skills inside `claude-maratai-dev/` (or `claude-maratai-manager/`
   for management tools) first so metadata stays consistent across platforms.
2. Run `./transfer_from_claude.py` (requires [uv](https://github.com/astral-sh/uv))
   to refresh the OpenCode copies with proper frontmatter transformation.
3. Use the sync script when you are ready to try the prompts locally:

   ```bash
   ./sync_opencode.sh         # sync opencode/ → ~/.config/opencode/
   ./sync_opencode.sh -n      # dry-run (preview changes)
   ./sync_opencode.sh -d      # show diffs for changed files
   ./sync_opencode.sh -n -d   # dry-run with diffs
   ```

   The script creates missing directories, replaces existing files, and removes
   orphaned files in the target that no longer exist in source.

Adding or Updating Skills
-------------------------
- Keep YAML front matter at the top of each `SKILL.md` file; Claude and
  OpenCode rely on the metadata.
- Prefer short, action-oriented descriptions and keep output format sections in
  Markdown so they render cleanly in every client.
- Confirm any Mermaid diagrams render by pasting them into your client before
  shipping changes.

Skill Reference (maratai-dev)
-----------------------------
- **`skills/commit/`** – auto-commit with smart branching. Captures outstanding
  changes, branches off `master` when needed, stages, commits with a concise
  message, pushes, and prompts the user to file a merge request via `glab`.
- **`skills/develop/`** – feature development planning. Starts with a user
  story, builds an implementation plan with local server commands, DB access,
  UI sketches, and testing steps. Includes two workflows:
  - **`workflows/deep-plan.md`** – comprehensive implementation planner with
    architecture diagrams, data-flow sequences, actionable task lists, and
    testing strategies.
  - **`workflows/deep-explain.md`** – documentation generator for existing
    features. Produces overview, sequence and flow diagrams, and a
    component-by-component walkthrough with file references and state changes.

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
   ```

3. Verify installation:
   ```
   /plugin marketplace list   # List configured marketplaces
   /plugin                    # Open interactive plugin browser
   ```

Troubleshooting
---------------
- The transfer script transforms Claude Code frontmatter to OpenCode format
  (removes `name`, `model`, `tools` fields; adds `mode: subagent` for agents).
- When new dependencies are needed for the Python script, update the inline
  `uv` metadata block inside `transfer_from_claude.py`.
- Keep an eye on trailing commas in JSON files such as
  `opencode/opencode.json`; OpenCode validation may be stricter than local
  tooling.
- The `sync_opencode.sh` script removes orphaned files from `~/.config/opencode/`
  that don't exist in `opencode/`. Use `--dry-run` to preview changes first.
