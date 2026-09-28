---
name: first-screenful
description: Design the first screenful's priority stack (identity, claim, one visible action, scent) and verify it at the laptop fold band (~630px), not just at 1080p — fold problems are invisible in full-page renders. Fires when building or reviewing any scrolling page meant for an audience (site, landing page, viz, app shell).
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

# First screenful — design for the fold band, verify at laptop height

**Trigger:** building or reviewing any scrolling page meant for an audience — site,
landing page, viz, app shell. Fires at the same moment as the horizontal layout render
check (`layout-measure.md`: no dead space beside narrow elements); it is that check's vertical sibling.

**The fold is a band, not a line.** Common landing heights after browser chrome:
~630px (1366x768 laptop), ~940px (1080p desktop), ~700-800px tall by ~390 wide
(phone). Never design "to the fold"; design the first screenful's priority stack and
check it at each band edge.

**The first screenful has four jobs, in order:** identity (who is this), claim (what
is being said), one visible action (a CTA, a path, a control), and **scent** — an
element visibly sliced by the viewport edge that invites the scroll. A card cleanly
above the fold or cleanly below it is worse than one the fold cuts in half: the cut
IS the scroll cue.

**The reliable miss is the laptop band.** A hero comfortable at 1080p routinely
pushes the action and the scent below ~630px, leaving a first screenful of prose
with nothing to do and no hint of more. Fix with a height media query at desktop
widths that tightens hero rhythm, not by gutting content at all sizes — and check
whether the tightening deserves to extend up through the 1080p band too: on the
first application (a site rebuild) the fix started at `max-height: 840px` and
ended at `max-height: 1080px`, because fitting the hero to the desktop viewport
also fixed an oversized hero image and a below-fold slogan in one move.

**Verify by rendering the viewport, not the full page:** full-page screenshots hide
fold problems by construction. Take a viewport-only screenshot at 1366x768 (a headless
browser such as Playwright, with full-page capture off) and look: are all four jobs on
screen? Repeat at 1899x950 and 390x844 when the page matters.

*Origin: 2026-08-21 site rebuild — the user asked what belongs above the fold and how
that survives multiple screen types; the laptop band was the miss on an
otherwise-reviewed page, invisible in every full-page render taken until then.*
