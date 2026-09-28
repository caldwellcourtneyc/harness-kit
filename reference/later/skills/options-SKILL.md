---
name: options
description: Open a visual fork with concrete variants instead of iterating one artifact through taste corrections. Generates 2-3 genuinely divergent design directions as a side-by-side compare sheet, then converts to a live dial (every axis a control on real content) once the user picks a direction and starts asking for variations inside it. Opens it for the user to react to, encodes the reactions, then builds the winner. Triggers on `/options`, "show me options", "show me a few diff options", "can I switch through a bunch of X", "I'm not sold on any of these" — or proactively at the start of any visual build where direction is open, or the moment design feedback starts looping (a second consecutive round of taste corrections on the same artifact).
---

<!-- Kit note (delete this comment when you install): from Courtney's /options. It leans on a taste
file more than the other skills do: placeholder <your taste file>. If you don't keep one yet,
the method still works; the variants just start from less. Install at
~/.claude/skills/options/SKILL.md. -->

# Options

Design iteration is where turns go: in the harness this comes from, ~84 messages a month of palette, font, and layout corrections, usually applied one round at a time to a single artifact. The method assumes the user reacts to instances better than to descriptions — so the cheap move is to put divergent instances in front of them *before* sinking rounds into one direction.

This skill mechanizes a propose-first checkpoint: propose first, anchor with concrete examples, get the reaction, then build.

## Before anything: taste file

If the user keeps a taste file (`<your taste file>`), read it before building anything, sheet or dial — this is mandatory, not optional. The file tells you which axes are already settled (don't waste a variant relitigating them) and which are open. For a dial it also sets the candidate lists: the user's marked go-to faces, their committed-palette range, their anti-defaults.

## Pick the mechanism first: sheet, or dial

Two mechanisms in sequence, not rivals. Decide which one you are in before designing
anything: the dial rules are in this section, and every section after it assumes the sheet.

- **Static compare sheet** — the opening fork, while *direction* is undecided. 2-3 divergent
  registers side by side. Everything from "Designing the variants" onward is about this.
- **Live dial** — the moment direction IS decided and the work becomes tuning known axes
  (palette, type, size, ground treatment). One self-contained HTML page, real content, every
  axis a control the user can click.

**The switch signal is explicit: the user picks a direction and starts asking for variations
inside it** ("I like D, but can I see other colour options?"). Convert in that turn, without
being asked. On 2026-07-31 that conversion took a palette exploration heading for a third
static round down to a single message, and the user then asked for the approach as standing
practice. If a session opens with direction already settled, go straight to the dial.

Dial construction rules, each learned by getting it wrong in that session:

- **Every axis independently switchable.** Coupled axes produce false reads. Tying the
  typeface to a header-style toggle made a *header* choice look like a *type* choice.
  Offering seven display/body "pairings" that used only two body faces looked like a real
  body-text choice and was not one. Split anything the user might want to move separately.
- **Give the axis they live in the deeper list.** Body text carries the page, so body faces
  need more options than display faces, not fewer.
- **Prefer two generative numbers over a row of presets.** A base size plus a step ratio
  beats "comfortable / compact", because the user can land a value instead of picking a bucket.
  Keep presets as shortcuts that move the sliders.
- **Show the resulting numbers**, not just the effect. A live readout of the computed scale
  turns a vague slider into a decision the user can hand to the build.
- **Drive the finished dial programmatically before handing it over.** Click every control,
  assert each axis moves alone, and check nothing silently fell back to a browser default. A
  dial that looks right on first paint and breaks on the third click wastes the session it
  existed to save. Webfonts especially: `document.fonts.check()` returns false for any face
  not yet painted, so force the load and measure the rendered width against a fallback. A
  font that fails silently renders as a plain sans, and the user will reject a face they never saw.

## Designing the variants

**2-3 variants, no more.** Four-plus reads as mush and dilutes reactions.

**Variants must diverge on a load-bearing axis** — palette family (warm vs cool, saturated vs muted), structural skeleton (sectioned scaffold vs spatial canvas vs modular grid), or signature element (what's the one bold move). Three tints of the same idea is the failure mode: it *looks* like a fork but every branch is the same decision.

**Each variant gets a one-line intent** — "A: cool editorial, structure carries it. B: saturated zones, one loud signature graphic. C: dark stage, motion does the teaching." The label is what the user reacts to almost as much as the render.

Guardrails (standing rules, restated because this is where they bite):
- No unconscious Claude-default (warm background + serif headers + brick-red accent + saturated support). If a variant deliberately uses it, say so.
- Start at the bold/committed end and let the user dial back — never open with the safe card-grid and escalate.
- Any standing style rules in the user's taste file apply to the generated copy inside the variants too.

## The compare sheet

Build ONE self-contained HTML file with the variants side by side (or stacked with labeled sections if the designs need width). Real content where possible, not lorem ipsum — the user is reacting to the thing, not the wireframe. Open it in the browser:

```
start "" "path\to\compare-sheet.html"      (Windows)
open path/to/compare-sheet.html            (macOS)
xdg-open path/to/compare-sheet.html        (Linux)
```

Then ask for reactions per variant, not a single winner — "B's palette + A's structure" is the common outcome and grafting is expected.

## After reactions

- **Encode before building.** Durable preferences go to `<your taste file>` — flag each: "that felt like a taste preference — want me to encode it?" Artifact-specific reactions stay with the artifact.
- **Convert to a dial** if the user picks a direction and keeps asking for variations inside it,
  rather than running a second sheet. See "Pick the mechanism first" above.
- **Build the winner**, grafting the liked pieces from runners-up. If a dial produced the
  decision, take the settled values off its readout rather than re-deriving them by eye.
- If every variant misses, that's signal, not failure — ask what the miss has in common before generating a second round (don't just spray three more).

## When NOT to fire

- The direction is already cited from an established reference (an existing brand guide or project style reference) — name it and proceed.
- Mid-build single-element tweaks ("make the icons larger") — that's normal iteration, not a fork.
- Non-visual work. Prose docs and task lists never come through here.

## What this is not

- **Not a render check** — verifying a finished render is a separate step; /options opens the fork before the build commits.
- **Not a full visual-build workflow** — /options can run inside one at the pattern/signature decision step, or standalone for any UI, page, or artifact.
