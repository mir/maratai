---
description: "Update statuses on jira tickets in progress and planned"
---

1. Fetch current JIRA tickets
   1. Fetch the available statuses
   2. Fetch the tickets that corresponds to
      1. planned, work in progress, testing, check, reconsider, qa, or done.
      2. owner: any
2. Get git commits from the last 7 days
3. Match commits to tickets (inspect code changes if commit messages are unclear)
4. For each ticket with related commits, draft a status update comment:
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
