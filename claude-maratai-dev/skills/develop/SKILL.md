---
name: develop
description: helps to prepare e2e plan for features implementations
disable-model-invocation: true
---

You are helping to prepare a plan before implementing the feature "$ARGUMENTS".

- Start with user story that describes the happy path with concrete examples as close to real ones as possible,
ask user to verify it.
- Create a normal plan based on that
- Include to the plan important things:
  - Commands to run local servers using tmux
  - Commands to access local db
  - Scetch of the design of new feature, if it requires one.
  - Testing plan using a browser/curl/cli/local db
- The following things are usually nice to have:
  - dataflow diagrams in ASCII
  - State handling of the application UI
  - ASCII scetch of the UI design

# Workflows

## deep-plan
Use when you need to **implement a new feature** or make significant changes to the codebase. This workflow creates a structured implementation plan with:
- Architectural diagrams (frontend, backend, database)
- Data flow sequence diagrams
- Actionable tasks with file references and code snippets
- Testing strategies

**Example triggers:** "plan in details" "build comprehensive plan" "deep plan"

## deep-explain
Use when you need to **understand an existing feature** or document how something currently works. This workflow creates comprehensive technical documentation with:
- High-level architecture overview
- Sequence and flow diagrams
- Component-by-component breakdown with code references
- State changes and data structures

**Example triggers:** "explain in details"
