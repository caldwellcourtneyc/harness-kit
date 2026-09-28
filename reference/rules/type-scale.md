---
name: type-scale
description: Define a small set of named body-text sizes as tokens and only use those — don't let font-sizes accrete into six near-identical body sizes that read as sloppy. Fires when building or reviewing any multi-section page/site/artifact with real body copy, or the moment you're about to add a third/fourth near-duplicate font-size.
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

# Type scale — a small set of sizes, chosen not drifted

**Trigger:** building or reviewing any multi-section page, site, or artifact with
real body copy. Fires alongside the horizontal layout (`layout-measure.md`) and first-screenful render
checks — it is the typographic sibling. Also fires the moment you're about to type
a third or fourth `font-size` value that's within a point or two of one already on
the page.

**The recurring miss: font sizes accrete.** Each section gets its size picked in
isolation — a card body at 16, a list at 14.5, a caption at 15.5, an intro at 17.5 —
and nothing is *wrong* alone, but the page ends up with six or seven near-identical
body sizes that read as sloppy. On a site rebuild, a single stylesheet had body text
at 14.5 / 15 / 15.5 / 16 / 16.5 / 17 / 17.5 before the user flagged it ("do the
different font sizes make sense?").

**The rule: define the scale once, then only use it.** A handful of named steps,
declared as tokens, referenced everywhere:

```
--fs-lead: 17px;   /* intros, lead paragraphs, product description */
--fs-body: 16px;   /* standard paragraphs */
--fs-card: 15px;   /* card bodies, feature / list items */
--fs-meta: 13.5px; /* captions, tags, fine print */
```

Display/heading sizes are a separate ramp (usually `clamp()` for fluidity) and can be
more numerous because the size *jumps* are large and legible — the drift problem is
specifically at the body end, where 15 vs 16 vs 17 do not read as intentional steps.

**Two working checks:**
- Before adding a new body size, ask: does an existing step do the job? If the new
  value is within ~1.5px of one already defined, use the existing one.
- When a card or box "feels a touch big," it usually is — card body copy wants to be
  a step *below* running-text body (`--fs-card`, not `--fs-body`), because it sits in
  a denser context. Reducing a point or two is the common right call, not a redesign.

**Verify by grepping, not by eye:** `grep -o 'font-size:[^;]*' style.css | sort | uniq -c`
should return a short list. A long tail of one-off px values is the smell.

*Origin: 2026-08-21 site rebuild — the user asked whether the font sizes made sense and
whether something should be encoded so I attend to them by default. The answer to both
was yes: seven body sizes collapsed to four named tokens.*
