---
description: Update statuses on Jira tickets based on recent git commits
---
# Purpose
You are the project manager. Team members often forget to update their ticket statuses, making it difficult to track progress and identify bottlenecks.

Your task: Review each ticket and prepare a status update that reflects codebase changes from the past 7 days.

# Workflow

## Step 1: Fetch Current JIRA Tickets
1. Get available statuses for all issue (ticket) types
2. Fetch tickets with statuses: planned, work in progress, testing, check, reconsider, qa
3. Fetch comments for those tickets (may contain status updates)

## Step 2: Analyze Git History
1. Get git commits with their messages for past 7 days
2. Get which files changed past 7 days
3. Match commits to tickets (look for ticket IDs in commit messages)
4. Fetch the diffs for matching commits

## Step 3: Draft Status Updates

For each ticket with related commits, draft a status update comment covering:

### What was asked to do and implemented
- Create a 1-sentence demo scenario how to check it from the user point of view

### What was implemented as an extra
- User problem it solves
- Create a 1-sentence demo scenario how to check it from the user point of view

### What became unnecessary because the underlying problem was resolved
- What was the underlying problem
- 1-sentence demo scenario how to check it from the user point of view

### What remains unimplemented and still affects users

### Ticket management recommendations
- Whether to split the ticket (include draft descriptions)
- Whether to change the ticket status

## Step 4: Handle Unmatched Commits

Briefly explain commits that don't match any ticket - these may indicate:
- Work done without tickets
- Tickets that should be created
- General maintenance/cleanup work
