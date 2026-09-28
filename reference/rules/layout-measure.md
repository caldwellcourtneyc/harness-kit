---
name: layout-measure
description: Don't leave dead horizontal space — elements fill the responsive width, or the space beside a deliberately-narrow element holds content. Fires when generating HTML/CSS/JSX/TSX layouts (pages, artifacts, and product UI alike).
paths:
  - "**/*.html"
  - "**/*.css"
  - "**/*.scss"
  - "**/*.jsx"
  - "**/*.tsx"
  - "**/*.vue"
  - "**/*.svelte"
  - "**/*.astro"
  - "**/*.mdx"
---

<!-- Kit note: one of three rules for visual work, with first-screenful.md (vertical) and
type-scale.md (type sizes). This is the horizontal one they both refer to. The paths: block
means it loads only when a matching file is read. Keep it as is or reword it in your terms. -->

# Layout — no dead horizontal space

The recurring miss: an element (a paragraph, a callout box, a card) sitting well short
of its container with **empty space beside it**. It's invisible in the markup — a
`max-w-3xl` on a `<p>`, a fixed-width box, both look sensible alone — and only shows in
the render, as a lopsided gap. The reader's eye reads that gap as "unfinished."

**The principle: fill the responsive width, or fill the gap with content. Never leave
dead space.**

- **Default — elements extend to fill their container.** Text, callout boxes, cards,
  and panels grow with the width available. A generous `max-width` to stop absurdly
  long lines on huge monitors is fine, but the element must still *visibly fill* a
  normal container, not float in a puddle of empty space. A narrow box alone in a wide
  row is the thing to never ship.
- **If you deliberately keep text narrower** (long-form reading on a very wide screen),
  the adjacent space must hold something — a stat rail, a figure, a pull-quote, a
  secondary panel. If you have nothing to put there, the text should just extend.
  Empty space beside capped text is the defect, not a feature.

**Readable line length is a soft ceiling, not the goal.** Don't cap text to a tight
measure and leave a gap — a reading column stranded in a wide frame. Filling the width
a bit wider than ideal beats a visible dead margin.

## The other direction is still a failure — hold both

Don't over-correct into cramming genuinely-wide content narrow: squeezed data tables,
card grids jammed to two columns, clipped charts, cramped dashboards. Wide-by-nature
blocks (tables, dashboards, dense card grids, charts, side-by-side comparisons, media
rows, wide code, full-bleed bands, nav) want room — give them it. A cramped data view
is as wrong as a dead margin.

## Verify by looking, not by reading the markup

This defect exists only in the render. Take a screenshot, or look at a real render at a normal laptop width and at phone width, and check
every section for empty space beside an element. The widths always look fine in
source — that's exactly why it ships.

## Scope

Fluid HTML/CSS/JSX/TSX/Vue/Svelte layouts, including product UI (where it's
higher-stakes and less likely to get looked at). Does NOT apply to terminal output,
markdown or chat, fixed-size slides, or the inside of a single table cell.
