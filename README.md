maratai
=======

Reusable prompts, command templates, and helper scripts that keep Marat's
multi-agent coding assistants in sync. The repository centralizes the
instructions used by Claude and OpenCode so they can be edited once and
re-used across tools.

Repository Layout
-----------------
- `claude-maratai-dev/` – Claude plugin for development workflows with agents
  and commands for project search, code review, specification creation, and
  web research. Includes deepwiki MCP server.
- `claude-maratai-manager/` – Claude plugin for management workflows with
  Atlassian integration (Jira & Confluence) and weekly reporting tools.
- `opencode/` – OpenCode-compatible copies of the same prompts (folder names are
  singular and formatting matches OpenCode's expectations); also contains
  `opencode.json` with local MCP and formatter settings.
- `transfer_from_claude.py` – utility that copies Markdown from
  `claude-maratai-dev/` to `opencode/`, stripping or reusing front matter as needed.
- `sync_opencode.sh` – helper script that pushes the local prompts into
  OpenCode's configuration directory.

Daily Workflow
--------------
1. Edit or add prompts inside `claude-maratai-dev/` first so metadata stays
   consistent across platforms.
2. Run `./transfer_from_claude.py` (requires [uv](https://github.com/astral-sh/uv))
   to refresh the OpenCode copies while keeping any OpenCode-specific preamble.
3. Use the sync script when you are ready to try the prompts locally:

   ```bash
   ./sync_opencode.sh    # copies opencode/ → ~/.config/opencode/
   ```

   The script creates missing directories and replaces existing files so you can
   rerun it safely after every edit.

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
- **`claude-maratai-dev/commands/commit.md`** – user-only auto-commit flow. Capture
  outstanding changes, branch off `master` when needed, stage, commit with a
  concise message, push, and prompt the user to file a merge request.
- **`claude-maratai-dev/commands/plan.md`** – deep implementation planner. Collects
  inputs, drafts a markdown plan with architecture/data-flow diagrams, task
  checklist, and then invokes the plan-spec-reviewer agent.
- **`claude-maratai-dev/commands/prepare-feature.md`** – orchestration command that
  reforms a feature request, then spawns `project-search`, `web-research`, and
  `spec` agents in parallel and enforces numbered outputs under `docs/<feature>/`.
- **`claude-maratai-dev/commands/explain-feature.md`** – documentation generator for
  a specific feature. Produces overview, sequence and flow diagrams, and a
  component-by-component walkthrough with file references and state changes.

Command Reference (maratai-manager)
-----------------------------------
- **`claude-maratai-manager/commands/week_report.md`** – weekly status writer. Summaries
  recent work per project and prepares (but does not send) a Slack payload with
  the formatted report.

Agent Reference
---------------
- **`claude-maratai-dev/agents/project-search.md`** – scans the codebase for
  relevant files, outputs references, lightweight snippets, diagrams, and a
  trimmed summary in `docs/`.
- **`claude-maratai-dev/agents/product-spec.md`** – business-facing specification writer
  that distills user stories, functional requirements, edge cases, and a minimal
  end-to-end test plan without touching implementation details.
- **`claude-maratai-dev/agents/web-research.md`** – external research assistant that
  prioritizes credible sources (forums, docs, DeepWiki) and records pros/cons and
  recommendations inside `docs/`.
- **`claude-maratai-dev/agents/plan-spec-reviewer.md`** – reviewer that compares an
  implementation plan against a specification, logs critical gaps, and calculates
  coverage metrics in a standalone markdown report.

Skill Reference (maratai-manager)
---------------------------------
- **`claude-maratai-manager/skills/atlassian/`** – Jira and Confluence integration
  via OAuth 2.0. Access issues, projects, sprints, and wiki pages through Python
  scripts with compact YAML output to save tokens.

Troubleshooting
---------------
- If OpenCode metadata disappears after a transfer, verify the target file
  already contains the desired front matter; the transfer script preserves it.
- When new dependencies are needed for the Python script, update the inline
  `uv` metadata block inside `transfer_from_claude.py`.
- Keep an eye on trailing commas in JSON files such as
  `opencode/opencode.json`; OpenCode validation may be stricter than local
  tooling.
