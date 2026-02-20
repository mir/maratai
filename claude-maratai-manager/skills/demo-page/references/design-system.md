# Design System for Demo Pages

Complete CSS, HTML structure, and component reference for generating self-contained demo HTML pages.

**Design principle:** Optimized for screen sharing (Zoom, Google Meet). Images fill maximum width, text is large enough to read through video compression, borders are thick enough to survive encoding artifacts.

---

## Color Palette

| Role | Name | Hex | Usage |
|------|------|-----|-------|
| Background | Light gray | `#FAFAFA` | Page body |
| Text primary | Near black | `#1A1A1A` | Headings, body text |
| Text secondary | Dark gray | `#44444F` | Leads, captions, transitions (darker than typical for screen share readability) |
| Hero background | Dark zinc | `#18181B` | Hero and closing sections |
| Hero accent | Lavender | `#A78BFA` | Gradient text, theme, bullet dots |
| Border | Medium gray | `#D1D1DB` | Screenshot borders (thicker than typical) |
| Browser bar | Zinc 100 | `#F4F4F5` | Screenshot browser chrome |
| Dot | Zinc 300 | `#D4D4D8` | Browser bar dots |

### Accent colors (cycle per section)

| Order | Name | Hex | Class |
|-------|------|-----|-------|
| 1 | Violet | `#7C3AED` | `accent-violet` |
| 2 | Amber | `#D97706` | `accent-amber` |
| 3 | Teal | `#0D9488` | `accent-teal` |
| 4 | Rose | `#E11D48` | `accent-rose` |
| 5 | Blue | `#2563EB` | `accent-blue` |

### Tinted backgrounds (cinematic sections only, cycle)

| Order | Name | Hex | Class |
|-------|------|-----|-------|
| 1 | Mint | `#EDFCF8` | `bg-mint` |
| 2 | Pink | `#FFF1F3` | `bg-pink` |
| 3 | Ice | `#EFF4FF` | `bg-ice` |

---

## Complete CSS

Copy this entire block into the `<style>` tag:

```css
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  background: #FAFAFA;
  color: #1A1A1A;
  line-height: 1.6;
}

/* ── Hero ── */
.hero {
  background: #18181B;
  color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 3.5rem 2rem 3rem;
}
.hero h1 {
  font-size: 3rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  background: linear-gradient(135deg, #fff 30%, #A78BFA 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.25rem;
  opacity: 0;
  animation: heroFadeIn 0.6s ease forwards;
}
.hero .meta {
  font-size: 0.95rem;
  color: rgba(255,255,255,0.5);
  font-weight: 400;
  margin-bottom: 1.25rem;
  opacity: 0;
  animation: heroFadeIn 0.6s ease 0.15s forwards;
}
.hero .divider-line {
  width: 48px;
  height: 1px;
  background: rgba(255,255,255,0.2);
  margin-bottom: 1rem;
  opacity: 0;
  animation: heroFadeIn 0.6s ease 0.3s forwards;
}
.hero .theme {
  font-size: 1.1rem;
  font-style: italic;
  color: #A78BFA;
  font-weight: 400;
  opacity: 0;
  animation: heroFadeIn 0.6s ease 0.45s forwards;
}

@keyframes heroFadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

/* ── Section Label & Heading ── */
.section-label {
  font-size: 0.85rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 0.5rem;
}
.section-heading {
  font-size: 2.25rem;
  font-weight: 700;
  letter-spacing: -0.01em;
  color: #1A1A1A;
  margin-bottom: 0.5rem;
}
.section-lead {
  font-size: 1.15rem;
  color: #44444F;
  max-width: 640px;
}

/* Animate only headings */
.section-header {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.section-header.visible {
  opacity: 1;
  transform: translateY(0);
}

/* ── Transition lines ── */
.transition-line {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem 2rem;
  text-align: center;
  font-size: 1.1rem;
  font-style: italic;
  color: #5C5C6B;
}

/* ── Screenshot treatment (optimized for screen sharing) ── */
.screenshot {
  border-radius: 10px;
  border: 2px solid #D1D1DB;
  box-shadow: 0 4px 24px rgba(0,0,0,0.12);
  overflow: hidden;
  background: #fff;
}
.screenshot .browser-bar {
  display: flex;
  align-items: center;
  gap: 5px;
  padding: 6px 12px;
  background: #F4F4F5;
  border-bottom: 1px solid #E2E2E8;
}
.screenshot .dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #D4D4D8;
}
.screenshot img {
  width: 100%;
  display: block;
  image-rendering: -webkit-optimize-contrast;
}
.screenshot-caption {
  font-size: 1rem;
  color: #44444F;
  margin-top: 0.75rem;
  text-align: center;
  font-weight: 500;
}

/* Small crops — don't stretch */
.screenshot-natural {
  max-width: 560px;
  margin-left: auto;
  margin-right: auto;
}
.screenshot-natural img {
  width: 100%;
}

/* ── Pattern A — Stacked Layout ── */
.layout-split {
  padding: 4rem 2rem;
}
.layout-split .split-inner {
  max-width: 1000px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}
.layout-split .text-col {
  max-width: 640px;
}
.layout-split .screenshots-col {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

/* ── Pattern B — Cinematic Layout ── */
.layout-cinematic {
  padding: 4rem 2rem;
}
.layout-cinematic .cinematic-inner {
  max-width: 1000px;
  margin: 0 auto;
  text-align: center;
}
.layout-cinematic .section-lead {
  margin-left: auto;
  margin-right: auto;
}
.layout-cinematic .hero-screenshot {
  margin-top: 2rem;
}
.layout-cinematic .secondary-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  margin-top: 1.5rem;
}

/* ── Pattern C — Narrative Layout ── */
.layout-narrative {
  padding: 4rem 2rem;
}
.layout-narrative .narrative-inner {
  max-width: 1000px;
  margin: 0 auto;
}
.layout-narrative .narrative-screenshots {
  margin-top: 2rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.layout-narrative .narrative-screenshots .screenshot-wrap {
  width: 100%;
  margin: 0 auto;
}
.layout-narrative .callout-box {
  background: #fff;
  border: 1px solid #E2E2E8;
  border-left: 4px solid;
  border-radius: 8px;
  padding: 1.25rem 1.5rem;
  font-size: 1.05rem;
  color: #1A1A1A;
  margin: 0.5rem auto;
  width: 100%;
  text-align: left;
}

/* ── Closing Section ── */
.closing {
  background: #18181B;
  color: #fff;
  padding: 4rem 2rem;
}
.closing-inner {
  max-width: 640px;
  margin: 0 auto;
}
.closing h3 {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
}
.closing ul {
  list-style: none;
  margin-bottom: 2rem;
}
.closing li {
  padding: 0.45rem 0;
  font-size: 1.05rem;
  color: rgba(255,255,255,0.85);
  padding-left: 1.25rem;
  position: relative;
}
.closing li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #A78BFA;
}
.closing .closing-divider {
  width: 100%;
  height: 1px;
  background: rgba(255,255,255,0.1);
  margin: 2rem 0 1.5rem;
}
.closing .teaser {
  font-style: italic;
  font-size: 1.05rem;
  color: rgba(255,255,255,0.6);
  margin-bottom: 2rem;
}
.closing .attribution {
  font-size: 0.85rem;
  color: rgba(255,255,255,0.3);
}

/* ── Accent colors ── */
.accent-violet .section-label { color: #7C3AED; }
.accent-amber .section-label { color: #D97706; }
.accent-teal .section-label { color: #0D9488; }
.accent-rose .section-label { color: #E11D48; }
.accent-blue .section-label { color: #2563EB; }

.accent-violet .callout-box { border-left-color: #7C3AED; }
.accent-amber .callout-box { border-left-color: #D97706; }
.accent-teal .callout-box { border-left-color: #0D9488; }
.accent-rose .callout-box { border-left-color: #E11D48; }
.accent-blue .callout-box { border-left-color: #2563EB; }

/* Section tinted backgrounds */
.bg-mint { background: #EDFCF8; }
.bg-pink { background: #FFF1F3; }
.bg-ice { background: #EFF4FF; }

/* ── Responsive ── */
@media (max-width: 768px) {
  .hero h1 { font-size: 2.25rem; }
  .hero { padding: 2.5rem 1.5rem 2rem; }

  .layout-cinematic .secondary-grid {
    grid-template-columns: 1fr;
  }

  .section-heading { font-size: 1.6rem; }
}
```

---

## HTML Skeleton

Full page structure. Replace placeholders with actual content.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DataChat — {{META_LINE}}</title>
<style>
  /* paste complete CSS block here */
</style>
</head>
<body>

<!-- ═══════════ Hero ═══════════ -->
<section class="hero">
  <h1>DataChat</h1>
  <div class="meta">{{META_LINE}}</div>
  <div class="divider-line"></div>
  <div class="theme">{{THEME}}</div>
</section>

<!-- ═══════════ Sections go here ═══════════ -->
<!-- Use Pattern A, B, or C markup for each section -->
<!-- Insert transition lines between sections -->

<!-- ═══════════ Closing ═══════════ -->
<section class="closing">
  <div class="closing-inner">
    <h3>{{CLOSING_HEADING}}</h3>
    <ul>
      <li>{{SUMMARY_ITEM_1}}</li>
      <li>{{SUMMARY_ITEM_2}}</li>
      <!-- ... -->
    </ul>
    <div class="closing-divider"></div>
    <p class="teaser">{{TEASER}}</p>
    <p class="attribution">DataChat — Analytics Division, Semrush</p>
  </div>
</section>

<script>
(function() {
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('[data-animate]').forEach(function(el) {
    observer.observe(el);
  });
})();
</script>

</body>
</html>
```

---

## Component Reference

### Screenshot with browser chrome

Standard screenshot wrapper used in all layouts:

```html
<div class="screenshot">
  <div class="browser-bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>
  <img src="demo-screenshots/{{FILENAME}}.png" alt="{{ALT_TEXT}}" loading="lazy">
</div>
<p class="screenshot-caption">{{CAPTION}}</p>
```

For small/cropped screenshots that shouldn't stretch to full width, wrap in `.screenshot-natural`:

```html
<div class="screenshot-natural">
  <div class="screenshot">
    <div class="browser-bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>
    <img src="demo-screenshots/{{FILENAME}}.png" alt="{{ALT_TEXT}}" loading="lazy">
  </div>
  <p class="screenshot-caption">{{CAPTION}}</p>
</div>
```

### Transition line

Place between sections:

```html
<div class="transition-line">{{TRANSITION_TEXT}}</div>
```

### Callout box (Pattern C only)

Place between screenshots in a narrative layout. The `accent-*` class controls the left border color:

```html
<div class="callout-box accent-amber">
  {{CALLOUT_TEXT}}
</div>
```

---

## Layout Patterns

### Pattern A — Stacked Layout

Text on top, full-width screenshots below. Maximizes image size for screen sharing. Best for 2-3 screenshots.

```html
<section class="layout-split {{ACCENT_CLASS}}">
  <div class="split-inner">
    <div class="text-col">
      <div class="section-header" data-animate>
        <div class="section-label">{{NUMBER}} / {{CATEGORY}}</div>
        <h2 class="section-heading">{{HEADING}}</h2>
        <p class="section-lead">{{LEAD}}</p>
      </div>
    </div>
    <div class="screenshots-col">
      <div>
        <div class="screenshot">
          <div class="browser-bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>
          <img src="demo-screenshots/{{IMG}}" alt="{{ALT}}" loading="lazy">
        </div>
        <p class="screenshot-caption">{{CAPTION}}</p>
      </div>
      <!-- repeat for additional screenshots -->
    </div>
  </div>
</section>
```

### Pattern B — Cinematic Layout

Centered text with full-width hero screenshot and 2-column secondary grid. Best for flagship features. Add a `bg-*` tinted background class.

```html
<section class="layout-cinematic {{ACCENT_CLASS}} {{BG_CLASS}}">
  <div class="cinematic-inner">
    <div class="section-header" data-animate>
      <div class="section-label">{{NUMBER}} / {{CATEGORY}}</div>
      <h2 class="section-heading">{{HEADING}}</h2>
      <p class="section-lead">{{LEAD}}</p>
    </div>
    <div class="hero-screenshot">
      <div class="screenshot">
        <div class="browser-bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>
        <img src="demo-screenshots/{{IMG}}" alt="{{ALT}}" loading="lazy">
      </div>
      <p class="screenshot-caption">{{CAPTION}}</p>
    </div>
    <div class="secondary-grid">
      <div>
        <div class="screenshot">
          <div class="browser-bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>
          <img src="demo-screenshots/{{IMG}}" alt="{{ALT}}" loading="lazy">
        </div>
        <p class="screenshot-caption">{{CAPTION}}</p>
      </div>
      <div>
        <div class="screenshot">
          <div class="browser-bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>
          <img src="demo-screenshots/{{IMG}}" alt="{{ALT}}" loading="lazy">
        </div>
        <p class="screenshot-caption">{{CAPTION}}</p>
      </div>
    </div>
  </div>
</section>
```

### Pattern C — Narrative Layout

Wide container with full-width screenshots and optional callout box between images. Best for 2 screenshots and explanatory features.

```html
<section class="layout-narrative {{ACCENT_CLASS}}">
  <div class="narrative-inner">
    <div class="section-header" data-animate>
      <div class="section-label">{{NUMBER}} / {{CATEGORY}}</div>
      <h2 class="section-heading">{{HEADING}}</h2>
      <p class="section-lead">{{LEAD}}</p>
    </div>
    <div class="narrative-screenshots">
      <div class="screenshot-wrap">
        <div class="screenshot">
          <div class="browser-bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>
          <img src="demo-screenshots/{{IMG}}" alt="{{ALT}}" loading="lazy">
        </div>
        <p class="screenshot-caption">{{CAPTION}}</p>
      </div>
      <div class="callout-box {{ACCENT_CLASS}}">
        {{CALLOUT_TEXT}}
      </div>
      <div class="screenshot-wrap">
        <div class="screenshot">
          <div class="browser-bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>
          <img src="demo-screenshots/{{IMG}}" alt="{{ALT}}" loading="lazy">
        </div>
        <p class="screenshot-caption">{{CAPTION}}</p>
      </div>
    </div>
  </div>
</section>
```

---

## Layout Decision Tree

Choose a layout for each section:

1. **Is this the flagship feature?** -> Pattern B (Cinematic)
2. **Does the section have 2-3 screenshots?** -> Pattern A (Stacked)
3. **Does the section have 1 large screenshot with detailed text?** -> Pattern A (Stacked)
4. **Does the section have exactly 2 screenshots and needs explanation?** -> Pattern C (Narrative)
5. **Does the section have 1 primary + 2 supporting screenshots?** -> Pattern B (Cinematic)

**Constraint:** Never use the same pattern twice in a row. If the decision tree suggests the same pattern as the previous section, pick the next best option.

---

## Screen Sharing Design Notes

These decisions were made specifically because the page is presented via Zoom/Google Meet:

- **Pattern A is stacked, not side-by-side.** Side-by-side splits put images at 50% width which becomes unreadable through video compression. Stacked layout gives images full container width.
- **Screenshot borders are 2px** (not 1px) so edges survive encoding artifacts.
- **Box shadows are heavier** (0.12 opacity, 24px blur) to separate screenshots from the background even when colors wash out.
- **Browser chrome is compact** (6px padding, 8px dots) to minimize wasted vertical space — more pixels for actual content.
- **`image-rendering: -webkit-optimize-contrast`** helps with downscaled images in video feeds.
- **Caption font is 1rem/500 weight** instead of 0.85rem/400. Small light text disappears on shared screens.
- **Text secondary color is `#44444F`** (darker than typical `#5C5C6B`) to maintain contrast through compression.
- **All containers are 1000px max-width** to use more horizontal real estate.
- **Narrative screenshots are 100% width** (not 80%) — no reason to shrink them when readability matters.

---

## Image paths

All images use relative paths from the HTML file location (`docs/`):

```
demo-screenshots/01-feature-name.png
demo-screenshots/02-feature-detail.png
```

The `src` attribute should be `demo-screenshots/{{name}}.png` (no leading `docs/` since the HTML file is already in `docs/`).
