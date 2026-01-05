maratai
=======

Reusable prompts, command templates, and helper scripts that keep Marat's
multi-agent coding assistants in sync. The repository centralizes the
instructions used by Claude Code, OpenCode, and Cursor so they can be edited
once and re-used across tools.

Repository Layout
-----------------
- `claude-maratai-dev/` (v1.0.1) – Claude Code plugin for development workflows with
  agents and commands for project search, code review, specification creation, and
  web research. Includes deepwiki MCP server for GitHub repository documentation.
- `claude-maratai-manager/` (v1.5.0) – Claude Code plugin for management workflows
  with Atlassian integration (Jira & Confluence), Google Docs/Sheets export, and
  weekly reporting tools.
- `opencode/` – OpenCode-compatible copies of the same prompts (folder names are
  singular: `agent/` and `command/`); also contains `opencode.json` with local
  MCP and formatter settings.
- `.cursor/rules/` – Cursor rules generated from Claude Code skills. Can be
  imported into any project via Cursor's Remote Rule feature.
- `transfer_from_claude.py` – utility that copies Markdown from
  `claude-maratai-dev/` and `claude-maratai-manager/` to `opencode/` and
  `.cursor/rules/`, transforming frontmatter for each platform.
- `sync_opencode.sh` – helper script that syncs the local prompts into
  OpenCode's configuration directory (`~/.config/opencode/`), including orphan
  cleanup.

Daily Workflow
--------------
1. Edit or add prompts inside `claude-maratai-dev/` (or `claude-maratai-manager/`
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

Adding or Updating Prompts
--------------------------
- Keep YAML front matter at the top of each Markdown file; Claude and OpenCode
  rely on the metadata.
- Prefer short, action-oriented descriptions and keep output format sections in
  Markdown so they render cleanly in every client.
- Confirm any Mermaid diagrams render by pasting them into your client before
  shipping changes.

Command Reference (maratai-dev)
-------------------------------
- **`commands/commit.md`** – auto-commit flow. Captures outstanding changes,
  branches off `master` when needed, stages, commits with a concise message,
  pushes, and prompts the user to file a merge request via `glab`.
- **`commands/plan.md`** – deep implementation planner. Collects inputs, drafts
  a markdown plan with architecture/data-flow diagrams, task checklist, and
  then invokes the plan-spec-reviewer agent.
- **`commands/prepare-feature.md`** – orchestration command that reforms a
  feature request, then spawns `project-search`, `web-research`, and `spec`
  agents in parallel and enforces numbered outputs under `docs/<feature>/`.
- **`commands/explain-feature.md`** – documentation generator for a specific
  feature. Produces overview, sequence and flow diagrams, and a
  component-by-component walkthrough with file references and state changes.
- **`commands/fix-mermaid.md`** – fixes Mermaid diagram syntax errors in
  markdown files, ensuring diagrams render correctly.

Command Reference (maratai-manager)
-----------------------------------
- **`commands/week_report.md`** – weekly status writer. Summarizes recent work
  per project and prepares (but does not send) a Slack payload with the
  formatted report.

Agent Reference (maratai-dev)
-----------------------------
- **`agents/project-search.md`** – scans the codebase for relevant files, outputs
  references, lightweight snippets, diagrams, and a trimmed summary in `docs/`.
- **`agents/product-spec.md`** – business-facing specification writer that
  distills user stories, functional requirements, edge cases, and a minimal
  end-to-end test plan without touching implementation details.
- **`agents/web-research.md`** – external research assistant that prioritizes
  credible sources (forums, docs, DeepWiki) and records pros/cons and
  recommendations inside `docs/`.
- **`agents/plan-spec-reviewer.md`** – reviewer that compares an implementation
  plan against a specification, logs critical gaps, and calculates coverage
  metrics in a standalone markdown report.

MCP Server Reference (maratai-dev)
----------------------------------
- **`deepwiki`** – Remote MCP server for querying GitHub repository documentation
  via DeepWiki. Provides tools for reading wiki structure, viewing content, and
  asking questions about repositories. Connects to `https://mcp.deepwiki.com/sse`.

Skill Reference (maratai-manager)
---------------------------------
- **`skills/jira-confluence/`** – Jira and Confluence integration via OAuth 2.0.
  Access issues, projects, sprints, and wiki pages through Python scripts with
  compact YAML output to save tokens. Run `scripts/auth.py login` for setup.
  Includes workflow references:
  - **`references/jira_cleanup.md`** – ticket hygiene workflow for analyzing
    stale tickets, finding duplicates, and cleaning up backlogs.
  - **`references/jira_status_update.md`** – matches git commits from the last
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

Cursor Rules
------------
Cursor users can import rules from this repository:

1. Open **Cursor Settings → Rules**
2. Click **+ Add Rule** next to Project Rules
3. Select **Remote Rule (Github)**
4. Enter the repository URL: `https://github.com/mir/maratai`

Available rules:
- **`jira-confluence`** – Jira and Confluence access via Python scripts with OAuth 2.0
- **`google-docs-sheets`** – Export Google Docs and Sheets to Markdown via gcloud ADC

Rules auto-sync when the source repository is updated.

Troubleshooting
---------------
- The transfer script transforms Claude Code frontmatter to OpenCode format
  (removes `name`, `model`, `tools` fields; adds `mode: subagent` for agents)
  and Cursor format (removes `name`, adds `alwaysApply: false`, transforms
  script paths from `${CLAUDE_PLUGIN_ROOT}` to `.cursor/rules/`).
- When new dependencies are needed for the Python script, update the inline
  `uv` metadata block inside `transfer_from_claude.py`.
- Keep an eye on trailing commas in JSON files such as
  `opencode/opencode.json`; OpenCode validation may be stricter than local
  tooling.
- The `sync_opencode.sh` script removes orphaned files from `~/.config/opencode/`
  that don't exist in `opencode/`. Use `--dry-run` to preview changes first.
