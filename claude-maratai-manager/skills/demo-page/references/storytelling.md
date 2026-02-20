# Storytelling Guide for Demo Pages

## Audience first

Before writing, answer these questions:

1. **Who are they?** End users, stakeholders, executives, or a mix?
2. **What do they already know?** Can you assume familiarity with the product, or is this their first exposure?
3. **What decision are they making?** Approving budget? Adopting the feature? Just staying informed?
4. **What's their pain threshold?** Are they frustrated enough to change behavior, or just mildly inconvenienced?
5. **How much time do they have?** 30-second skim or 5-minute deep dive?

The typical demo audience is **end users and stakeholders**. They care about:
- What they can do now that they couldn't before
- What frustration goes away
- How much effort it takes to benefit

---

## Core principle: problems, not features

Every section starts from a **user problem**, not a feature name:

| Feature-oriented (avoid) | Problem-oriented (use) |
|---|---|
| "File Upload to BigQuery" | "I have a spreadsheet and need answers from it" |
| "Granular Access Control" | "I can't control who sees my team's data" |
| "Skill Auto-Generation" | "My team's knowledge goes stale every week" |
| "Scheduled Prompts Redesign" | "Editing my weekly report automation is painful" |

---

## The problem → solution frame

Each section follows this mental structure (don't make these literal headings — weave them into heading + lead):

1. **The pain:** What was annoying, slow, or impossible before?
2. **The change:** What can the user do now?
3. **The proof:** The screenshot shows the solution in action.
4. **The example:** A concrete, relatable step-by-step scenario that makes the benefit tangible.

Example:
- Pain: "You had a CSV with this quarter's data, but getting it into DataChat meant filing a ticket and waiting."
- Change: "Now you drop it into the chat."
- Proof: Screenshot of the upload context card with schema and row count, followup question
- Example: "1. Export last week's ad spend from the dashboard as CSV. 2. Drop the file into DataChat. 3. Ask 'Which campaign had the highest CPC?' and get the answer."

This becomes:
- **Heading:** "Your Spreadsheet, Instantly Queryable"
- **Lead:** "Drop a CSV, Excel, or JSON file into the chat and start asking questions. No tickets, no waiting."

---

## Headings

Write from the user's perspective. Name the outcome or the relief, not the mechanism.

**Rules:**
- 3-6 words
- No jargon, version numbers, or ticket IDs
- The heading should resonate with someone who uses the product daily
- Think: what would the user say to a colleague about this?

**Good examples (problem-aware):**
- "Your Spreadsheet, Instantly Queryable"
- "Share What You Know"
- "Your Data, Your Rules"
- "Reports That Write Themselves"
- "Edit Without Leaving the Page"

**Bad examples:**
- "Skills Evolution" (vague, internal language)
- "Granular Access Control" (jargon)
- "Scheduled Prompts Redesign" (implementation-focused)
- "File Upload to BigQuery" (too technical)
- "DC-1234: Fix Upload Bug" (ticket ID)
- "Create, Share, Evolve" (marketing-speak that doesn't connect to a real problem)

---

## Lead text

1-2 sentences. Describe the before/after from the user's perspective.

**Good:**
> You had to file a ticket to get spreadsheet data into the system. Now you drop it into the chat and start asking questions.

> Analysts built personal shortcuts but had no way to pass them to teammates. Now any skill can be shared with a link or by name.

> Every field on the page is editable in place. Click, change, save — no more switching between read and edit modes.

**Bad:**
> We added inline editing with a click-to-edit pattern and BigQuery SQL snippets.

> This PR introduces a new React component for file upload with drag-and-drop support and progress indicators.

> The skill activation pipeline now supports dynamic tool loading via the skills registry API.

**Principles:**
- Start with the old pain or limitation ("You used to...", "Before this...")
- Follow with the new reality ("Now...", "This week...")
- If there's no clear "before", just describe what's possible in plain language
- One sentence is often enough — don't pad

---

## Transitions

The italic lines between sections connect the *resolution* of one user problem to the *existence* of the next.

**Pattern:** Solving problem A reveals or enables problem B.

**Good examples:**
- *"Now that anyone can bring their own data, the next question is: how does the system know what to do with it?"*
- *"More people creating skills means more need to control who can see and use them."*
- *"With data and permissions sorted, the last piece is keeping it all running without manual effort."*

**Bad examples:**
- *"Next, we'll look at activated skills."* (no connection, just sequencing)
- *"Another feature we shipped is access control."* (listing, not narrating)
- *"Moving on to the next section."* (meta, breaks immersion)

**Tips:**
- Frame as a natural consequence the user would feel: "OK, but now I need..."
- Keep to one sentence
- The transition should make both problems feel real

---

## Theme

Find a 2-4 word phrase that captures the *user benefit*, not the product direction.

**Look for patterns:**
- "Do It Yourself" — users handle things that required engineering before
- "Work Together Better" — sharing, teams, permissions
- "From Question to Answer" — end-to-end flow reduction
- "Less Waiting, More Doing" — friction removal, speed
- "Stay in Control" — permissions, governance, visibility

**Fallback:** If the features are truly disconnected, use "What's New in DataChat".

**Don't force it.** A strained theme is worse than a generic one.

---

## Closing section

Don't re-list features with the same descriptions used in the sections. Summarize each as a **user outcome**:

**Good:**
- Upload spreadsheets and query them instantly from the chat
- Create personal skills and share them with your team
- Control table and skill access per user or Google Group
- Edit and trigger scheduled reports without leaving the page

**Bad:**
- We implemented file upload functionality that allows users to upload CSV, Excel, and JSON files which are then ingested into BigQuery tables.
- Added granular access control with Google Groups sync

**Teaser:** Add "Coming soon..." in italic. Frame as user benefit:
- *"Coming soon: find past conversations faster, and richer chart options..."*
- *"Coming soon: team workspaces and easier data sharing..."*

**Attribution:** Always end with "DataChat — Analytics Division, Semrush"

---

## What to avoid

| Anti-pattern | Why it's bad | Do this instead |
|---|---|---|
| Feature names as headings | Users don't know your feature names | Name the problem being solved or the outcome |
| "What changed / How it helps" blocks | Reads like a changelog appendix | Integrate the value into the lead text |
| Dense implementation paragraphs | Audience isn't reading the code | 1-2 sentences focused on outcome |
| Marketing buzzwords ("Evolve", "Empower") | Feels hollow without a concrete problem | Ground every phrase in a specific user situation |
| Step numbers on screenshots | Feels like a manual, not a demo | Let images and captions speak |
| Identical section structure throughout | Monotonous, reader disengages | Alternate layout patterns (A, B, C) |
| Tiny screenshot crops stretched wide | Looks pixelated and unprofessional | Skip small crops, describe in text |
| Every element fading in | Tiresome after 3 sections | Animate headings only (IntersectionObserver) |
| Technical language in user text | BigQuery table IDs, API endpoints | Plain language, user perspective |
| Footer that re-lists everything | Redundant, anticlimactic | Short punchy summary + teaser |
