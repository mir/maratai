---
description: Analyze Jira tickets for common problems and propose cleanup actions
---
# Purpose
You are the project manager. Over time, Jira tickets accumulate issues: vague descriptions, stale discussions, incorrect statuses, and implemented features still marked as open.

Your task: Analyze active tickets against the codebase to identify problems and propose cleanup actions (update descriptions, close completed work, split large tickets, etc.).

# Workflow

## Step 1: Fetch Tickets

1. Fetch available statuses for the current project
2. Fetch Jira tickets with statuses corresponding to planned, in-progress, testing for any user
3. For each ticket, retrieve:
   - Title and description
   - All comments
   - Current assignee and reporter
   - Labels and components
   - Linked issues
   - Created date and last updated date

## Step 2: Explore Project Codebase

Since this command runs from the project folder, explore the codebase to understand the current implementation state.

### Codebase Discovery
- Identify the project structure and main components
- Find README, documentation, and architectural notes
- Locate key source directories and entry points

### Map Tickets to Code
For each fetched ticket, search the codebase for code that implements or relates to the ticket's described feature/fix.

### Implementation Status Assessment
Categorize each ticket's implementation state:
- **Fully implemented**: Code exists that satisfies all acceptance criteria
- **Partially implemented**: Some requirements met, others pending
- **Not started**: No related code found
- **Superseded**: Different approach taken than what ticket describes

## Step 3: Analyze Each Ticket

Evaluate each ticket against these common problems, incorporating code analysis findings:

### Description Issues
- **Missing acceptance criteria**: No clear definition of done
- **Vague requirements**: Ambiguous language like "improve", "fix", "handle better" without specifics
- **Missing reproduction steps**: For bugs, no steps to reproduce
- **Outdated information**: Description contradicts comments or current state
- **Scope creep**: Original scope expanded significantly through comments

### Comment Thread Issues
- **Unresolved questions**: Questions asked but never answered
- **Contradictory decisions**: Different people suggesting opposite approaches
- **Lost context**: Important decisions buried deep in comment threads
- **Off-topic discussions**: Comments unrelated to the ticket
- **Stale discussions**: Old conversations that are no longer relevant

### Status/Workflow Issues
- **Stuck tickets**: In Progress for too long without updates
- **Missing blockers**: Comments mention blockers but no linked blocking issues
- **Wrong status**: Activity suggests different status than current
- **Duplicate work**: Similar tickets exist or work already done elsewhere

### Structural Issues
- **Too large**: Should be split into smaller tickets
- **Too small**: Could be merged with related tickets
- **Missing links**: Related work exists but not linked
- **Wrong priority**: Priority doesn't match actual importance based on comments

### Implementation Mismatches (from code analysis)
- **Already implemented**: Code exists that fulfills the ticket requirements
- **Partially done**: Some requirements implemented, ticket should be updated to reflect remaining work
- **Implementation diverged**: Code took a different approach than ticket describes
- **Obsolete**: Feature/fix no longer needed based on current codebase state
- **Description outdated**: Ticket describes old architecture or patterns no longer in use

## Step 4: Generate Report

### Per-Ticket Findings

For each problematic ticket (group of tickets):

```
### [Ticket ID] - [Title]
**Status:** Current status | **Age:** X days | **Implementation:** Fully/Partially/Not started/Obsolete

**Problems:** [List specific issues found]

**Action:** [Recommended action with draft text if applicable]
```
