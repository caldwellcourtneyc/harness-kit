---
name: ux-thinking
description: Pre-build UX reasoning for interfaces and user flows. Use BEFORE writing UI code whenever the request involves anything user-facing — pages, dashboards, forms, modals, onboarding, settings, data displays — even when it doesn't say "design" (e.g. "build a page," "add a feature," "update the UI"). Handles the layer underneath the styling skills — is this the right thing to build, and will it make sense to a human? Complements design-system, visual-build, and render-verification tools, which judge how it's built; this judges what and why.
---

<!-- Kit note (delete this comment when you install): from Courtney's /ux-thinking. The method is
general. It mentions a few neighbouring tools (a design-system checker, a visual-build workflow,
a render check) by role; map those to whatever you use, or ignore them. Install at
~/.claude/skills/ux-thinking/SKILL.md. -->

# UX Thinking

A pre-build reasoning layer for user interfaces. This skill handles
what design skills don't: whether the interface makes sense to a
human before it looks good.

## When This Fires — and How Hard

Fires whenever user-facing interface work is on the table: new pages,
components, modals, forms, flows, navigation changes, or significant
UI modifications.

**Scale the pass to the change.** This is the calibration the skill
used to fumble — treating a label tweak like a new screen:

- **Full pass** (pre-build questions asked out loud): new screens,
  new flows, or changes that alter what the user is trying to
  accomplish.
- **Silent pass** (run the relevant checks in your head, state only
  what's non-obvious): adding a control to an existing screen,
  changing behavior of an existing element, layout adjustments.
- **Skip** (just do it): copy fixes, single-property style tweaks,
  changes with no decision in them.

Does NOT fire for:
- Pure styling/aesthetic passes — that's any aesthetic rules in your
  CLAUDE.md plus your styling tools
- Design-token/spacing consistency — that's a design-system check
- Backend-only work with no UI impact
- Steps inside a visual-build workflow that owns its own gates and
  build protocols; this skill's principles still apply inside that
  build, but don't re-run its questions on top of that workflow's intake

## How to Run the Questions

Work through the pre-build questions conversationally — not as a
checklist wall, and only the ones that aren't obvious from context.

**When the answer is inferable, infer it and say so in one line**
("Assuming this is for your phone-first morning check-in — building
mobile-first") rather than interrogating. The user leads on
architecture and concept; a build request is not an invitation to a
questionnaire. Ask out loud only when the answer would genuinely
change what gets built and you can't infer it.

## Core Philosophy

**Every screen answers a question.** If you can't state what question
the screen answers, the screen shouldn't exist.

**Every element earns its place.** If removing something wouldn't
confuse the user, it probably shouldn't be there.

**Users don't read, they scan.** The first thing someone sees should
be the most important thing on the screen. Not the logo. Not the nav.
The thing they came here to do.

**Confusion is a bug.** If a user has to think about what to click,
where to look, or what something means, that's not a "design
preference" — it's a failure. Treat it like a code bug.

## Pre-Build Questions

### The Big Four (always answer, even if silently)

1. **Who is this for and what are they trying to do?**
   Not "users" — specific humans with a specific goal. "Someone
   checking their mood trends for the week" is useful. "Users viewing
   data" is not.

2. **What's the one thing on this screen?**
   Every screen has a primary action or primary information. If there
   are two "primary" things, one of them isn't primary. Pick one.

3. **Phone or desktop — where will this actually be used?**
   Default assumption: both surfaces matter, and the mobile collapse
   is designed, not an accident. If the honest answer is "mostly phone," build
   mobile-first. (This question used to appear only post-build as a
   tap-target check — by then the layout is already committed.)

4. **What does the user see when there's nothing?**
   Empty states, loading states, error states. These are the states
   users see MOST (especially early) and designers think about LEAST.
   A blank screen with no guidance is abandonment fuel.

### When Relevant (ask if not obvious)

- **What did the user just do before this screen?** Context matters.
  A settings page after onboarding feels different from a settings
  page from the nav.
- **What should the user do after this screen?** If there's no clear
  next action, the screen is probably a dead end.
- **What would make someone abandon this?** Too many fields, unclear
  labels, no feedback after an action. Find the "forget it, I'll do
  this later" moment — and prevent it.
- **Is this the simplest version that works?** Start with the
  minimum. You can always add. You can never un-confuse a user who
  saw version 1.

## During Build: UX Reasoning

When a choice affects how a human will experience the interface, say
why — that's the explain-the-why habit applied to UI. Not every line; the
load-bearing calls.

### Patterns to Apply

**Information Hierarchy** — most important content is largest,
highest, or most prominent; secondary is smaller or below; tertiary
hides behind a click. Users scan in an F-pattern; put critical info
where eyes go first.

**Progressive Disclosure** — show only what's needed now; reveal
complexity as the user asks for it. Every visible option is a
decision the user has to process, even if they skip it.

**Feedback Loops** — every user action gets a visible response.
Silence after action feels broken; users click again, then leave.

**Proximity = Relationship** — things close together read as
related. Stronger than labels; you can group controls with
whitespace alone.

**Sensible Defaults** — pre-fill what you can predict; make the
happy path require zero decisions. Defaults that match expectations
are invisible; defaults that surprise are friction.

### Anti-Patterns to Catch

- **The Wall of Options:** 10+ visible controls with no grouping or
  hierarchy. Fix with progressive disclosure or sectioning.
- **Mystery Meat Navigation:** icons without labels, or labels in
  internal jargon. If it needs a tooltip to explain it, the label is
  wrong.
- **The Orphan Screen:** no clear path forward. Every screen suggests
  a next action or explicitly signals "you're done."
- **The Premature Modal:** modal content that deserves a page, or
  vice versa. If it scrolls, it's not a modal.
- **The Buried Action:** primary action below the fold, behind a
  menu, or styled like secondary content.
- **No Empty State:** great with data, blank void without. First-time
  users see the empty state first — make it explain what goes here
  and how to add it.
- **Confirmation Overload:** confirming everything trains users to
  click "yes" without reading. Reserve confirmation for destructive
  or irreversible actions.
- **Desktop-Only Thinking:** hover-dependent interactions, dense
  multi-column layouts, or tap targets under 44px that fall apart on
  the phone where the thing will actually be used.

## Post-Build Check

Run a quick mental walkthrough after building:

1. **First-time test:** someone with no context — can they figure out
   what to do in 5 seconds?
2. **Empty state test:** remove all data. Still useful?
3. **Squint test:** blur your eyes. Does the most important element
   still stand out?
4. **Mobile test:** at ~390px, does the layout collapse deliberately?
   Tap targets ≥44px and spaced to avoid mis-taps?
5. **Error recovery test:** network failure, validation error, empty
   response — does the user know what happened and what to do?

For *render* verification — does it actually look right on screen —
hand off to a render check (breakage pass, then craft pass, then show
the user). This walkthrough is about sense-making; the render check is
about pixels. They don't substitute for each other.

## Ecosystem — Who Owns What

- **ux-thinking (this skill):** is it the right thing, will a human
  understand it. Runs first, underneath everything else.
- **A visual-build workflow, if you use one:** owns the full workflow
  for visual/interactive artifacts (format-fit, type, signature).
  Don't duplicate its gates.
- **Design-system tools:** spacing, tokens, pattern consistency,
  deeper craft rigor on heavy builds.
- **Aesthetic rules in your CLAUDE.md + your taste file, if any:**
  palette, signature, visual direction. Not this skill's call — don't
  smuggle aesthetic decisions in as "UX."
- **A render check:** render-truth verification before calling any
  visual build done.

## Teaching Moments

When a UX decision is non-obvious, explain the principle as
transferable knowledge, not just "do it this way." Example: "Save
goes top-right because this page scrolls — users shouldn't have to
scroll past content they haven't edited to find the action. Primary
actions stay within reach."

## Lessons Log

| Date | Lesson | Change Made |
|------|--------|-------------|
| 2026-03-30 | Initial version | Created skill |
| 2026-07-09 | Skill-surface audit: body had gone stale — referenced a nonexistent skill, predated the render-check, visual-build, and design-system tools around it, treated mobile as a post-build afterthought, and fired at full depth on trivial tweaks. | Rebuilt body: proportionality tiers (full/silent/skip), mobile promoted into the Big Four, infer-and-state mode replaces questionnaire default, ecosystem section maps ownership across the neighbouring tools and the aesthetic rules. |
| | Further rows accrue from your own use. | |
