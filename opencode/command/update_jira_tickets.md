---
description: Update statuses on jira tickets in progress and planned
---

1. Fetch JIRA tickets with status 'In Progress' or 'Planned'
2. Get git commits from the last 7 days
3. Match commits to tickets (inspect code changes if commit messages are unclear)
4. For each ticket with related commits, draft a status update comment:
   - What was implemented and how users can see/use it
   - What became unnecessary because the underlying problem was resolved
   - What remains unimplemented and still affects users
   - Whether to split the ticket (include draft descriptions)
   - Whether to change the ticket status

Important:
- Do not post comments
- Do not change ticket status
- Do not edit tickets