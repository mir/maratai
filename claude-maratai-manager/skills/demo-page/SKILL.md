---
name: demo-page
description: "Create a polished, self-contained HTML demo page from any source material — feature descriptions, ticket lists, release notes, or free-form conversation. Use when asked to create a demo page, presentation, or showcase."
---

# Demo Page Generator

Create a polished, self-contained HTML demo page from any source material. The page tells a story about real user problems being solved — not a changelog, but a narrative that makes end users think "finally, that annoying thing is fixed."

## Phase 1: Gather & Understand

### Accept input

Accept free-form input from the conversation. This can be:
- Feature descriptions or bullet points
- Ticket lists or release notes
- Copy-pasted week reports or changelogs
- Verbal descriptions of what was built
- Any combination of the above

If the conversation has no material to work with, tell the user:

> Give me the material you'd like turned into a demo page — feature descriptions, ticket lists, release notes, or just describe what was built.

Stop and wait.

### Parse the input

From the provided material, separate two buckets:

- **Demo sections** — user-facing features, improvements, or changes that deserve a visual section with screenshots and narrative. These become demo sections on the page.
- **Summary items** — bug fixes, refactors, infrastructure changes, minor tweaks. These go into the closing summary as bullet points.

### Infer metadata

From the context, infer:
- **Page title** — usually "DataChat" unless the material is about a different product
- **Meta line** — a short descriptor (e.g., "Weekly Demo · Feb 14-20, 2026", "Q1 Release Highlights", "Sprint 42 Demo")
- **Output filename** — default to `docs/demo-YYYY-MM-DD.html` using today's date, or infer from context

Do not ask the user for these — propose them in Phase 2 along with the narrative variants.

---

## Phase 2: Craft the Narrative — 3 Variants

This is the core of the skill. **Propose, don't interrogate.**

### Process

1. Read [references/storytelling.md](references/storytelling.md) for the full writing guide
2. Analyze the input material
3. Propose **3 variants** as compact outlines

### The 3 variants

Present three narrative directions:

**Variant A — Controversial**
Bold angle, provocative headings. Takes a strong opinion about why these changes matter. Makes the audience feel something.

**Variant B — Informative**
Straightforward problem-then-solution. Clear, professional, no-nonsense. Each section follows a clean before/after structure.

**Variant C — Unique**
Unexpected structure or creative theme. Might reorder sections in a surprising way, use an unusual metaphor, or frame everything through an unexpected lens.

### What each variant includes

For each variant, present:
- **Theme** — 2-4 word phrase capturing the user benefit
- **Page title and meta line**
- **Section order** with:
  - Section number and category label
  - Heading (3-6 words, user perspective)
  - One-line lead sentence
  - Demo scenario — a concrete, relatable example showing the feature in action step by step.
- **Transitions** between sections (one italic sentence each)
- **Closing heading** and summary framing
- **Teaser line** for what's coming next (or a placeholder)

### Get approval

Present all three variants. The user picks one, mixes elements, or gives direction. **Single approval step** — no back-and-forth questions.

---

## Phase 3: Gather Images

Three sources — infer from context which applies, don't ask:
- create them youself using a browser
- find images in the project
- create images, diagrams, and charts using js/python
- ask user to provide pics

---

## Phase 4: Generate HTML

Read [references/design-system.md](references/design-system.md) for the complete CSS, HTML skeleton, and component markup.

The design system is optimized for screen sharing (Zoom, Google Meet). Key constraints:
- All layouts maximize image width — Pattern A is **stacked** (text above, full-width images below), not side-by-side
- All containers are 1000px max-width
- Screenshot borders are 2px with heavy shadows for compression survival
- Browser chrome is compact (6px padding) to save vertical space for content
- Caption and lead text are larger than typical for readability through video

### Assign layouts

For each section, choose a layout pattern — never use the same pattern twice in a row:

| Pattern | Name | Best for | Key trait |
|---------|------|----------|-----------|
| A | Stacked | 2-3 screenshots | Text on top, full-width images below |
| B | Cinematic | Flagship features, 1 primary + 2 supporting | Centered text, full-width hero + 2-col grid, tinted background |
| C | Narrative | 2 screenshots, explanatory features | 1000px container, full-width screenshots, callout box |

### Generate the file

Write to `docs/demo-YYYY-MM-DD.html` (default, date = today) or user-specified path. Single self-contained file with inline CSS and minimal JS (IntersectionObserver for heading animation only).

### Verify

1. List all `<img src="...">` paths in the generated HTML
2. Confirm each referenced image file exists in `docs/demo-screenshots/`
3. Note any remote image URLs (these won't be verified)
4. Tell the user: "Open `docs/demo-YYYY-MM-DD.html` in a browser to review."

## Closing section

The closing section is a dark footer that wraps up the narrative:
- `h3`: Use the closing heading from the approved variant (e.g., "What we shipped", "What's new", etc.)
- Bullet list: one short punchy line per item, framed as **user outcomes** ("Upload spreadsheets and query them instantly") not feature names ("File upload to BigQuery")
- Divider line
- Teaser: from the approved variant, framed as user benefit. Ask the user what's coming or use a generic one.
- Attribution: "DataChat — Analytics Division, Semrush"

## Quick reference

| Artifact | Location |
|----------|----------|
| Output HTML | `docs/demo-YYYY-MM-DD.html` (default) |
| Screenshots | `docs/demo-screenshots/*.png` |
| CSS & template | [references/design-system.md](references/design-system.md) |
| Writing guide | [references/storytelling.md](references/storytelling.md) |
