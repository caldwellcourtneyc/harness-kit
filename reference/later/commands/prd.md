Interrogate an idea before building it — walk the design tree, resolve dependencies between decisions, reach shared understanding before any code. Use for any feature, flow, or change touching several files, user-facing behavior, non-obvious decisions, or multi-session work; also when the user asks for a PRD, says "let's spec this", "think this through before we build", or invokes /prd. Not for typos, clear bug fixes, single-line tweaks, style changes, or mechanical execution. Exits: write a PRD or move into plan mode — never straight to code.

<!-- Kit note (delete this comment when you install): from Courtney's /prd. Placeholder to fill:
<your journal search> (grep over your journal folder works on day one). The task-tracker steps
apply only if you keep one. Install as a skill at ~/.claude/skills/prd/SKILL.md (see SEED.md, "Installing a skill"). -->

Stress-test the idea before implementation. You are not planning — you are surfacing
decisions the user doesn't yet know they need to make, finding contradictions, and making
sure you both understand the full shape before a line of code. Walk the design tree until
the feature is clear enough to either capture as a PRD or move into implementation planning.

## When to Use

Invoke for any feature, flow, or change that:

- Touches more than 2-3 files
- Has user-facing behavior to design
- Involves decisions that aren't obvious
- Will span multiple sessions

**Do NOT use for:** typos, bug fixes with clear causes, single-line tweaks, style changes,
or anything where the work is "just do the thing." Small changes don't need a design tree.

## Before Asking (silent — don't narrate)

Pull context and explore code *before* the first question. Don't show the results — internalize
them and weave them into the grilling. This is what lets you ask good questions instead of ones
whose answers are already in the files.

- **Journal:** run a few targeted queries with `<your journal search>` on the feature topic.
  Catch prior decisions, abandoned attempts, related threads.
- **Existing artifacts:** look for an existing PRD or decision record in the project
  (`PRDs/`, `Decisions/PRD-*`).
- **In-flight work:** check the project's task tracker for related items already moving.
- **Project guidance:** read the project's `CLAUDE.md` if one exists.
- **Code:** explore how the feature would slot into what exists.

### Quiet start

No preamble. No "here's what I found," no "great idea, let me start by asking." Open with the
first real question, shaped by what you pulled and explored.

## How to Grill

- **One question at a time.** Don't stack. Let each answer shape the next.
- **Walk every branch.** Each choice opens sub-choices. "How users save" opens "what's saved,"
  "where," "when," "can they undo."
- **Explore, don't ask, when possible.** If the answer is in the code or journals, find it.
- **Name contradictions.** If two answers pull against each other, call it out instead of
  moving on.
- **Make it concrete.** Abstract questions get abstract answers. Drop the user into specific
  scenarios.
- Probe how this fits what exists, edge cases, failure modes, integration risk, and what you'd
  both regret not thinking about.

## Topics to Cover

These map directly to the PRD sections — grilling should naturally produce the answers the PRD
needs.

| Grilling topic | PRD section |
|---|---|
| What's broken or missing, and for whom | Problem |
| What the user experiences | Solution |
| Decisions made during grilling + why | Decisions Made |
| What's still unresolved | Open Questions |
| Thinnest end-to-end slice that proves the approach | Smallest Viable Version |

## When to Stop

Stop when ALL of these hold:

- No new branches are surfacing from your questions.
- Every contradiction has been **resolved or explicitly deferred** (see below) — none left
  silently hanging.
- The user is starting to repeat themselves or shrug at further questions.
- You can describe the full feature back to them without inventing anything.

If unsure: "I think I have the shape — want me to reflect it back before we choose an exit?"

### Contradictions: resolve or explicitly defer

A contradiction may be **resolved** during grilling, or **explicitly deferred** — but a
deferral is a decision, not a silent omission. Every deferred contradiction is named in the
PRD's Open Questions, marked as a deferral, with what it blocks.

One exception routes to a different artifact: if a **core** contradiction — one the feature's
whole shape depends on — can't be resolved even provisionally and is wholly deferred, you
don't have a PRD yet. Capture what grilling revealed as a **decision record** instead (see
Edge Cases). A PRD needs a stable enough shape to build against; a decision record is the
honest home for "we learned the idea isn't ready."

## Landing

Once grilling is complete, reflect the shape back in 2-4 sentences. Then offer the two exits —
these are the only two, and you never go straight from PRD grilling to code:

- **Write a PRD** — capture this as a durable feature doc. Good for complex features,
  multi-session work, or ideas that might wait before implementation.
- **Move into implementation planning** — go straight to planning the build (plan mode).
  Good when you're building now and session context carries you through.

## Writing the PRD

**File location:** `PRDs/PRD-YYYY-MM-DD-short-title.md` at the project root. Create `PRDs/` if
it doesn't exist. Don't mix PRDs into `Decisions/` — ADRs and PRDs are different artifacts.

**Format:**

```md
# PRD: [Feature Name]
**Date:** YYYY-MM-DD
**Status:** Draft | Ready | In Progress | Done

## Problem
What's broken or missing, and for whom. 2-3 sentences.

## Solution
What we're building. Describe the experience, not the implementation.

## Decisions Made
Choices resolved during grilling. Capture the decision AND the reasoning —
future sessions need the why.

## Open Questions
Unresolved items. Flag what blocks implementation vs. what can be figured out
during build. Name every deferred contradiction here, marked as a deferral.

## Smallest Viable Version
The thinnest slice that proves the approach end-to-end. This gets built first —
it exposes integration risk before we're deep in sunk cost.
```

Show the draft before saving.

## After Capture

- **Reindex:** make the PRD searchable for future sessions (reindex your journal search if it
  covers the project).
- **Task tracker:** if the PRD opens or resolves a tracked item, update it.
- **Confirm:** tell the user the file path and that it's been indexed.

## Edge Cases

- **Idea is too vague to grill** — help them find the shape of the question before the answer.
  "What's the problem you're trying to solve?" is a fine opener.
- **They already have a PRD in mind** — ask to see it. Grill against *that* instead of starting
  from scratch.
- **Grilling reveals the idea isn't ready** — a valid outcome. Capture what you learned as a
  decision record (deferred) instead of a PRD. This is also where a wholly-deferred core
  contradiction lands (see When to Stop).
- **They push back on questions** — read the room. If a branch isn't worth walking for this
  feature, skip it. The design tree is a guide, not a checklist.
