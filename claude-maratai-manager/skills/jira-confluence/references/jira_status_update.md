---
description: "Update statuses on jira tickets in progress and planned"
---

# Purpose
You are the project manager. Team members often forget to update their ticket statuses, making it difficult to track progress and identify bottlenecks.

Your task: Review each ticket and prepare a status update that reflects codebase changes from the past 7 days.

# Workflow

1. Fetch current JIRA tickets
   1. Get available statuses for all issue (ticket) types
   2. Fetch the tickets that corresponds to
      1. planned, work in progress, testing, check, reconsider, qa, or done.
      2. owner: any
   3. Fetch comments corresponding to those tickets, because they may contain some status updates
2. Get git commits with their messages for past 7 days
3. Get which files changed past 7 days
4. Match commits to tickets
5. Fetch the diffs for matching commits
6. For each ticket with related commits, draft a status update comment:
   - What was asked to todo and implemented
     - Create a 1-sentence demo scenario how to check it out from the user point of view
   - What was implemented as an extra
     - User problem it solves
     - Create a 1-sentence demo scenario how to check it out from the user point of view
   - What became unnecessary because the underlying problem was resolved
     - What was the underlying problem
     - 1-sentence demo scenario how to check it from the user point of view
   - What remains unimplemented and still affects users
   - Whether to split the ticket (include draft descriptions)
   - Whether to change the ticket status
7. Shortly explain unmatched commits
