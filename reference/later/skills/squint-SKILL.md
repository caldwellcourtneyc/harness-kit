---
name: squint
description: "Cold-reader-first critique for websites, interactive pieces, documents, decks, visualizations, and other artifacts. Use when the user asks to squint at something, review, critique, assess, inspect, take a look, look something over, give candid feedback, perform a skeptical pass, or judge whether an artifact is ready. This skill judges an artifact as its audience will meet it; it is distinct from a render check of a visual build Claude just made, /codehealth (code correctness and vibecoding risks), and design-system consistency checks. Adapt the review to the artifact's audience, purpose, medium, and stage. Review without changing the artifact unless the current request explicitly authorizes changes."
---

<!-- Kit note (delete this comment when you install): from Courtney's /squint. Placeholder to
fill: <your taste file>, if you keep one. Install at ~/.claude/skills/squint/SKILL.md, and put
the web adapter from squint-references/web-interactive.md (next to this file in the kit) at
~/.claude/skills/squint/references/web-interactive.md. -->

# Squint — artifact review

Named for the squint test: the first unguarded look, where you see whether the
thing holds up before you can read any of the detail. That is the posture —
meet the artifact the way its audience will, not the way its maker explains it.

## Workflow at a glance

1. Establish the artifact contract (medium, audience, encounter context, stage).
2. Cold read the artifact and record findings BEFORE opening any brief, history,
   or taste file.
3. Informed pass: read the context docs; keep cold-read findings visible.
4. Diagnose each material finding: direction, clarity, execution, or QA.
5. Report: verdict first, then the cold-read purpose and claim, the
   findings that matter most (every blocking one, however many), any
   other findings one line each, what should stay settled, one next
   move, the strongest counterargument, untested surfaces.

Each step is expanded below. Do not skip step 2 or reorder 2 and 3 — the
cold read loses its value the moment context loads.

## Core boundary

Treat review as read-only. Do not modify the artifact, source, configuration,
history, deployment state, or supporting files unless the current request
explicitly authorizes changes. Approval to review is not approval to fix.

## Establish the artifact contract

Infer or identify the artifact's medium, audience, encounter context, intended
effect, stage, constraints, and settled decisions. Ask one question only when
an unknown answer would materially change the review.

Scale the pass to the stage. Judge rough direction for concept and composition,
not finish. Judge pre-ship work for the full experience and production risk.

## Run two passes

1. Cold read the artifact before using its brief, history, or rationale.
2. Record what a context-free reader can understand, where attention goes,
   what is unexplained, and what may cause abandonment.
3. Then read the relevant brief, history, design guidance, settled decisions,
   and taste file.
4. Keep the cold-read findings visible. Context can explain a choice but cannot
   repair confusion in the artifact.

For the user's own work, consult `<your taste file>` (if one exists)
when visual or editorial judgment matters. Use medium-specific design and UX
skills when available.

**Reviewing your own build, or an audience unlike you: delegate the cold read.**
An author cannot self-administer the cold read — the context is already loaded
and cannot be set down. The same is true when the reviewer already knows the
artifact's genre and the audience does not (a kid, a novice, a first-timer):
what is obvious to the reviewer is exactly what the audience will trip on, and
the review will call it "clear." Delegate, and tell the reader who the audience
is.
Spawn a subagent that has none of the build history, and instruct it to *render
the artifact and review the screenshots before it is permitted to read the
source*. Source contains author comments, variable names, and structure that
leak the brief. This is the difference between a cold read and an impression of
one, and on 2026-08-05 it surfaced defects the author had missed across five
sessions of building the same page.

## Review by purpose

Prioritize only the dimensions that materially affect the artifact:

- **Meaning:** clarity, truth, argument, evidence, narrative, and cold-reader comprehension.
  Two checks that only fire across a *set*, so they survive item-by-item proofreading:
  - **Parallel-item consistency.** Where an artifact presents parallel items (tests,
    criteria, options, steps, chips, tiers), check the set for consistent polarity,
    numbering, ordering, and register. Every item can be individually correct while the
    set is incoherent — seven pass/fail tests where four fail on "yes" and three fail on
    "no" make the reader re-derive the polarity each time. Also check that the same
    entity carries the same label everywhere it appears.
  - **Labels written from the maker's seat.** Annotations, captions, and column heads
    that instruct whoever *operates* the thing instead of explaining it to whoever
    *reads* it. They feel informative to the author, who supplies the missing context
    for free. Symptom: process vocabulary ("stated or inferred", "name the
    alternatives") where the reader needs a consequence ("drops the wrong age group").
- **Experience:** hierarchy, sequencing, interaction, pacing, and medium fit.
- **Craft:** visual conviction, editorial character, coherence, originality, and generic defaults.
- **Integrity:** accessibility, responsive behavior, technical quality, factual accuracy,
  and production readiness.

Use the following precedence when guidance conflicts:

1. Purpose, audience, truth, and accessibility.
2. The current request, project constraints, and settled decisions.
3. Medium-specific UX and design principles.
4. The user's taste file, if one exists.
5. Generic conventions.

Let taste choose among solutions that already work. Do not use taste to excuse
confusion or accessibility failures. Do not let generic best practice erase a
deliberate point of view. Name a real conflict instead of silently choosing.

## Diagnose before proposing

Classify material findings as:

- **Direction:** the underlying idea or structure is wrong.
- **Clarity:** the intended meaning does not reach a cold reader.
- **Execution:** the idea is sound but its treatment is weak.
- **QA:** the intended treatment is broken or incomplete.

Do not generate options before diagnosing the cause. When options are warranted,
vary the load-bearing decision and start boldly. If every option misses, identify
the common miss before producing another round.

## Adapt to the medium

Read `references/web-interactive.md` for websites and interactive artifacts.
For other media, apply the core workflow and the relevant installed document,
presentation, spreadsheet, PDF, visualization, or design skill. Add a new
adapter only after repeated real use demonstrates medium-specific needs.

## Report the review

Lead with a candid verdict. Then provide:

1. The apparent purpose and claim from the cold read.
2. The findings that matter most, prioritized, with evidence and
   consequence. Usually three to five; if more would block the artifact
   from doing its job, list every one of them. Then any other real
   findings, one line each, so nothing found is dropped.
3. What is working and should remain settled.
4. One recommended next move.
5. The strongest counterargument and what would change the recommendation.
6. Untested surfaces or review limitations.

Distinguish review evidence from preference. Avoid exhaustive chronology,
generic praise, and equal weight for unequal problems.

## Lessons log

The rows below come from the harness this skill was built in, with the projects left out. Add your own as you use it.

| Date | Lesson | Change made |
|------|--------|-------------|
| 2026-07-27 | Initial version. | — |
| 2026-08-05 | **Parallel-item consistency.** On a pipeline visualization, a grid of seven pass/fail tests flipped polarity between cards — four rejected on "yes", three on "no" — under a heading promising a consistent bar. Every card proofread clean individually; the defect existed only across the set. The user caught it by comparing against an earlier version; the author (Claude, who wrote all seven) had reread that section repeatedly and never saw it. Partially corroborated by the cold pass, which independently found the same class of defect in a chip row whose meaning shifted mid-set. | Added as a named check under **Meaning**. |
| 2026-08-05 | **Labels written from the maker's seat.** Same artifact: funnel annotations read "stated by the source, or inferred and triaged" — an instruction to whoever runs the pipeline, not an explanation to whoever reads the page. Author-blind by construction, because the author supplies the missing context automatically. NOTE: this one was fixed before the cold pass ran, so it is **not independently corroborated** — it rests on a single context. Demote or drop it if two more reviews pass without it firing. | Added as a named check under **Meaning**. |
| 2026-08-05 | Running squint as a **subagent that renders the artifact and reviews the screenshots before it is permitted to read source** produced findings the author had missed across five build sessions, including a cross-graphic numbering contradiction and a full contrast audit. Confirms the skill's step-2/step-3 ordering is the load-bearing part: an author cannot self-administer a cold read, however carefully they try. | Added "Reviewing your own build: delegate the cold read" to **Run two passes**. |
| 2026-08-10 | **Parallel-item consistency corroborated, second independent context.** On a long-form essay, a delegated cold reader with no knowledge of this skill found the essay's "four moves" framework named differently in four places, moves 3-4 never repeating a name — exactly the defect class the 2026-08-05 entry encoded. Same review also produced a cautionary pair: the session Claude nearly reported the cold reader's scroll-reveal finding as "corroborating" a HANDOFF item because section labels matched — different page, different defect. Cross-referencing cold-read findings against project history needs the same verify-before-claiming discipline as the findings themselves. | Second full context recorded; the check stands. (The demote-clock on the 2026-08-05 *maker's-seat* entry is untouched — it is the provisional one, and this session makes no claim on it.) |
| 2026-09-10 | **The reviewer's own expertise is a confound, not just the author's context.** Squint on a children's game (another agent's build, so not "own work") judged the tile interaction "clear and works on touch." Two adults then failed the first screen in thirty seconds: the mechanic (two tiles become one) was never shown, only described. The reviewer already knew the kind of game it was, so the mechanic was obvious to them and the cold read was not cold. A delegated cold read run afterwards, with the audience named as a young child, found the copy problems the original review missed. | "Delegate the cold read" widened from own-builds to any artifact whose audience's expertise differs from the reviewer's; the delegation prompt names the audience. |
| 2026-09-22 | **A status-bearing picture claims more than the user confirmed.** A first-time setup guide for a hardware product (Claude's own build, already screenshotted step by step by the author). The delegated cold reader, told the audience was a first-time owner, found the two worst defects: the illustration showed the device lit and "Ready" before the user had confirmed either, and the end screen said "You're all set" with every step ticked after "Not yet" answers, or after jumping straight to the end. Each screen looked correct alone; the lie only shows when you trace state against what the user actually said. The author's pass missed both because it checked that screens *rendered*, not what they *asserted*. | Recorded as a defect class for interactive artifacts: any indicator that reads as a status (a light, a check, a success line) must follow confirmed state, and the review should trace it. Delegation corroborated again (fourth context). The maker's-seat check did not fire in this review, which counts toward its demote clock. |
| 2026-09-23 | **Caps hide findings.** A prompt audit against Opus 5.5 found the fixed "three to five findings" and "avoid laundry-list critique" make current models drop real findings they noticed; the user wanted every blocking finding however many there are. | Report item 2: the findings that matter most (every blocking one), then the rest one line each. "Laundry-list" dropped from the avoid line. |
| 2026-09-25 | **A live product needs reviewers the cold read can't replace, and live state moves under the review.** Pre-launch squint on a live web app: three parallel reviewers (a cold read of the live site as its audience, a backend cost/abuse reviewer, a measured web-hygiene pass). The two worst findings (a permissions gap, and a model the app depended on that had been retired months earlier) came from the backend pass querying LIVE state (DB column grants, the secrets list, provider deprecation pages), which several earlier Claude reviews that read code alone had missed. Second lesson: the backend reviewer read a promo code as 60 days / 200 uses, and a later query showed 30 / 500. The reviewer wasn't wrong; the user had edited the code in the dashboard in between, and Claude reported it to them as a correction. | For live products, pair the cold read with a live-state backend pass. Before calling a reviewer's number wrong, re-read the source: the data may have changed, not the reviewer. |
