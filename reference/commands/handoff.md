Write a HANDOFF.md for the current project so the next session can pick up where this one left off. Fires on request, proactively at context pressure or plan checkpoints, and before any 3+ turn action sequence.

---

## When This Runs

- **Manual:** the user calls `/handoff` to pause work
- **Proactive:** Claude detects context pressure or hits
  a plan checkpoint and initiates
- **Before multi-step actions:** Claude writes or updates
  a handoff before starting any sequence that spans 3+
  turns (plan execution, edit sequences, long debugging
  loops). Covers the unplanned-interruption case where
  Claude Code may crash mid-action and no one has called
  `/handoff` yet. Keep these updates lean — a fresh
  snapshot of current state, not the full ceremonial
  handoff.

**Replaces session end protocol.** When `/handoff` runs,
skip whatever session-end summary you'd normally write.
The handoff covers all of that and more.

## Two Modes — pick the right one

HANDOFFs come in two shapes. Pick deliberately at first
write; once a project is in rolling mode, stay there.

### Single-session mode (default for short threads)

The handoff is a **snapshot** — created when work pauses,
deleted when work completes. Use for any thread that's
likely to wrap inside a few sessions: bug fix, feature
add, focused refactor, debugging loop. Template below in
"Single-session template."

### Rolling mode (for long-running project state)

The handoff is a **living document** that tracks state
across many sessions for a multi-week or multi-month
project. New Opens get added; closed Opens get reduced
to breadcrumbs (not deleted, since cross-references
elsewhere in the codebase rely on the numbers). The
moving picture stays readable; durable decisions move
to specs and the HANDOFF carries pointers.

Use rolling mode when:
- Project has explicit multi-week/multi-month plan
- Multiple concurrent Opens / decisions tracked at once
- Specs at repo root own durable content; HANDOFF tracks
  the moving picture
- HANDOFF has been growing for 2+ weeks without natural
  closure point

Once in rolling mode, the bloat-prevention rules below
apply.

## Detect the Project Root and Filename

Identify the correct location and filename:

- **Location:** at the project root (the top folder
  of the repo or project you're working in). If
  unsure, ask the user.
- **Filename:** use `HANDOFF-<thread>.md` when multiple
  threads may be active in the same project (e.g.,
  `HANDOFF-auth-refactor.md`). Use plain
  `HANDOFF.md` only when there's clearly one active
  thread per project (rolling-mode HANDOFFs typically
  use the bare name). When unsure, default to per-thread
  naming — safer under concurrent work.

## Single-session template

```markdown
# Handoff

**Created:** YYYY-MM-DD
**Project:** [project name]

## Goal

What we're building/doing and why (1-2 sentences)

## Done When (acceptance criteria)

*Load-bearing / multi-session work only — skip for lean
snapshots and mechanical fixes; its absence there is correct,
not a gap.*

The checks that tell us the whole effort is complete and
correct (distinct from the per-action "Done when" under Next
Step). Write probes, not descriptions — "reload, entry
appears" not "saving works." This is a self-verification
contract for the next Claude to run before declaring done, not
a checklist for the user. Hold only criteria that have
crystallized into a real check; dimensions still being worked
out stay in Unsettled and graduate into a probe here as they
resolve.

- [ ] [Observable condition] — verify: [command, file/DB state,
      UI action, or observation that proves it]

For taste-driven work (visuals, copy, aesthetic calls), the
honest criterion is "the user signs off" — don't invent a
checkable proxy for a judgment call.

## Plan

The full scope — numbered steps or bullet outline.
Include the complete plan, not just remaining work.

## Status

- [x] Completed steps (brief — what, not how)
- [~] In progress (where exactly, what's left)
- [ ] Not started

## Discoveries

Anything the next Claude needs to know that isn't
obvious from the code:

- Failed approaches and why they failed
- Non-obvious decisions and their rationale (tag with
  `[LOCKED]` / `[PROVISIONAL]` / `[ASSUMED]` if certainty
  isn't obvious from context)
- Edge cases or gotchas found
- Dependencies or blockers

## Unsettled

Distinct from Discoveries, which are settled findings.
Unsettled is mid-thinking — what you'd test if you had
another hour. Highest-loss items if not captured. Skip
if nothing.

- [Suspicion or hypothesis] — [what would verify or kill it]

## Next Step

The first action the next Claude should take. Frame as:

- **Action:** [verb + target — file path, function, line range]
- **Done when:** [observable signal step 1 is complete]

If the next step has multiple parts, number them and frame
each the same way.

If the next step is genuinely exploratory, frame it as
exploration with a stop condition rather than forcing the
Action/Done-when shape.

## Files Touched

List of files created or modified this session.
Use absolute paths.
```

## Rolling-mode template

```markdown
# Handoff

**Last updated:** _pending — set after Status verified_
**Project:** [project name]

## Goal

What the project is building and why. 2-3 sentences.

## Plan (build sequence)

Numbered build steps with current state. Use ~~strikethrough~~
+ ✅ for done.

## Status

Compact checkbox list of milestones with dates. ~10 lines max.

## Active decisions

One ### per Open, numbered stably. Keep verbose enough to
re-acquire context (~5-15 lines each); trim aggressively
when carry-forward content already lives in a spec.

### #N [short title]
[what's open, what's decided so far, what's suspected but
unverified, what triggers closure (state as a verifiable probe
where the work allows — "X passes check Y", not "X feels
done"), what gates it / what it gates]

## Resolved decisions

Numbers preserved. Each entry is a **breadcrumb only** —
1-3 lines pointing at the spec that owns the durable
content. Do NOT duplicate spec content here.

- **#N — [title].** ✅ YYYY-MM-DD. → [SPEC.md §X / file
  path / decision-log entry]. [One-sentence headline of
  what got decided.]

## Recent sessions

Compressed entries — 2-5 lines each. Last ~30 days; older
moves to `ARCHIVE.md` or gets compressed to a single
"Earlier sessions" line pointing at git log.

## Lessons learned / Discoveries / Local dev environment

Durable knowledge about this project (Postgres gotchas,
install workarounds, conventions). Trim when items become
obvious or are captured elsewhere.

## Suggested first steps next session

The forward look. What should the next Claude do first.
Sequenced. Specific.
```

## Writing Rules (both modes)

1. **Single-session:** each handoff is a complete snapshot
   — overwrites any existing file, don't append.
2. **Rolling:** edit in place. Add to active sections;
   don't create parallel "v2" sections.
3. Write for a Claude with zero context. Assume the
   reader has only the project CLAUDE.md and this file.
4. Be specific: file paths, line numbers, function
   names. Vague handoffs are useless handoffs.
5. Include the user's stated intent if it differs from
   what's in the code (e.g., "The user wants X but we
   built Y as a stepping stone").
6. **Mark certainty inline.** Don't let provisional ideas
   read as settled — that constrains the next agent (or
   future-you) into commitments that were never made. Tag
   any decision, discovery, or plan item where status
   isn't obvious from its section:
   - `[LOCKED]` — decided, don't relitigate
   - `[PROVISIONAL]` — leaning this way, could still flip
   - `[OPEN]` — actively undecided, needs resolution
   - `[ASSUMED]` — treated as true but not verified

   Skip tags where the section already encodes status
   (items in "Unsettled" don't need `[OPEN]`; items under
   "Resolved decisions" don't need `[LOCKED]`). Use them
   inline within Plan, Discoveries, Active decisions, and
   anywhere a flat-statement could be misread as settled.
7. **Compose Status before preamble (rolling mode).**

   **First write:** the template ships with placeholder
   `**Last updated:** _pending — set after Status verified_`.
   Don't replace until After Writing step 1 passes.

   **Edit/rewrite:** BEFORE updating the existing "Last
   updated" line with a new session summary, FIRST reset it
   to the placeholder. Then update Status. Then verify per
   After Writing step 1. THEN write the real new line.

   Why: writing the preamble's new session-summary line before
   Status reflects on-disk reality encodes intent as
   completion. If the session crashes between write and the
   work landing, the next session reads the preamble as
   authoritative. Self-review fires after the write — by then
   the lie is on disk.

   Two writes to the same file by design — temporally
   separated by the work itself, not a multi-edit-batching
   violation.

   If the placeholder remains at session end (crash, abort),
   that's the safe degraded state. Next session: verify Status,
   then replace.
8. **Done When is tier-gated and Claude-facing.** Include the
   acceptance-criteria section only for load-bearing or
   multi-session work — skip it for lean snapshots and
   mechanical fixes; its absence there is correct, not a gap.
   The probes are a contract for the next Claude to verify
   before claiming done, not a to-do for the user. Keep only
   crystallized checks there; let still-emerging design
   questions sit in Unsettled and graduate into a probe as they
   resolve. For taste-driven work, "the user signs off" is the
   honest criterion — don't fabricate a checkable proxy.
   Rolling mode has no separate section: its equivalent is
   stating each Open's closure trigger as a verifiable probe,
   with still-emerging questions living in that Open's
   "suspected but unverified" line rather than an Unsettled
   section.

## After Writing

1. **Self-verify** before showing:
   - **Preamble check first.** Every completion claim in
     "Last updated" / session-summary lines must already
     appear in Status, and must match git/disk. If the
     preamble is still a placeholder, write the real line
     now — after the remaining sub-bullets pass. No new
     claims in the preamble that aren't reflected in Status.
   - Re-read each file listed in "Files Touched" — confirm
     cited line numbers and function names still match
     current state
   - Confirm the Status checklist matches what's actually
     in git history and on disk — a "completed" item that
     didn't land is a bigger lie than a wrong line number
   - Run `git status` and confirm it matches what the
     handoff claims about WIP state
   - **"Pushed" needs "CI green at \<sha\>".** A handoff
     that claims work was pushed is only half a claim until
     it also states the build/CI passed (or names the sha to
     check). "Pushed" while main is red sends the next
     session debugging a break it didn't cause. If CI status
     is unknown, say so — don't let "pushed" imply "green."
   - Fix any discrepancy in the handoff before showing
2. Show the handoff (or the diff, for rolling mode) to
   the user in chat.
3. Save to the project root after approval.
4. Tell the user the handoff is written and the next
   session will pick it up automatically.

## Pickup Protocol (for the RECEIVING session)

This is documented here so the protocol lives with
the skill. If your CLAUDE.md has a session-start rule
to check for a HANDOFF, it points here.

When a session starts and a HANDOFF file exists
(`HANDOFF.md` or any `HANDOFF-*.md`):

1. Read it fully
2. **Verify the handoff against current project state.**
   - Compare HANDOFF.md mtime to the project's most recent
     commit and most recently modified file. If the project
     moved AFTER the handoff was written, surface the drift
     before resuming.
   - For each file in "Files Touched," confirm cited line
     numbers and function names still resolve. Flag any
     mismatch.
   - Run `git status` and confirm it matches the handoff's
     claim.
   - During the session, note any moments where the handoff
     was missing context, stale, or wrong — these get logged
     in the Reception Audit at session close.
3. If the user has already directed you to continue
   the work, summarize the handoff and note any
   discrepancies — don't make them confirm twice.
   Otherwise, ask: "I found a handoff from a previous
   session. [1-2 sentence summary]. Anything to add
   or change before I pick this up?"
4. Proceed after the user confirms or has already
   indicated intent to continue
5. **(Rolling mode)** Run the bloat check below as a
   silent pass; if cleanup is warranted, surface it
   to the user before resuming feature work.

## Reception Audit

If this session picked up from a HANDOFF, write a brief
audit at session close. Append to `HANDOFF-audit-log.md`
at the project root (create if it doesn't exist).

Format:

```
### YYYY-MM-DD — picked up [filename]
- Useful: [what the handoff got right / helped most]
- Missing: [what you had to ask the user for, or had
  to discover]
- Stale: [what claims didn't match current reality]
- Add next time: [what would close the gap]
```

Keep each bullet short — one line. Skip a bullet if not
applicable. The point is to surface patterns over time,
not to grade individual handoffs.

Scan during a periodic review or when the log passes ~10 entries.
Recurring gaps are template-tuning candidates.

Skip if no handoff was picked up at session start.

## Closure Pattern (rolling mode)

The single biggest cause of HANDOFF bloat: when an Open
closes, the closure detail keeps living in HANDOFF
instead of being summarized into the spec it informed.
The result over a few weeks is a 1,400-line HANDOFF
where 60% is closed-Open verbose history.

**At closure of any Open, before marking it ✅ in HANDOFF:**

1. **Decide where the durable summary belongs.** Pick one:
   - **Spec decision log** — most common. Each canonical
     spec has a dated decision log. Append a 1-paragraph
     entry there.
   - **Spec section** — if the closure shaped how the
     spec reads, edit the relevant section directly.
   - **Code or config** (e.g., CLAUDE.md tech stack,
     `scripts/foo/README.md`) — when the decision is
     about implementation choice.
   - **Nowhere durable** — operational/historical detail
     with no future relevance. Skip to step 3.

2. **Write the durable summary** at its destination.
   Should be readable cold by a future Claude who never
   read HANDOFF.

3. **Reduce HANDOFF entry to a breadcrumb.** Move the
   Open from the active section to "Resolved decisions."
   1-3 lines max:
   - Number, title, ✅ date
   - Pointer at where the durable content lives
   - One-sentence headline of the decision

4. **Preserve the number.** Specs and other docs may
   cross-reference "Open #N." Don't renumber. The breadcrumb
   keeps the number findable.

If the closure surfaced a NEW open question, that's a
separate Open — don't fold it into the closure entry.

## Bloat-prevention hygiene (rolling mode)

Run these checks at the start of each session (silent
pass — only surface to the user if cleanup is warranted).

**Trigger a cleanup pass if any:**

- HANDOFF exceeds ~700 lines
- 5+ closed Opens have verbose closure detail (not
  breadcrumbs)
- Session log has entries older than ~30 days that
  duplicate decisions captured in specs
- More than ~3 active Opens have grown to 30+ lines each

**Cleanup pass scope (~1-2 hours):**

1. Walk closed Opens; apply the Closure Pattern
   retroactively for each.
2. Compress session-log entries to 2-5 lines. Move
   entries older than ~30 days to `ARCHIVE.md` (see
   "The archive split" below) if they captured anything
   load-bearing; delete the rest (decisions live in
   specs, code lives in git log).
3. Re-read active Opens; trim verbose ones where
   carry-forward content already lives in a spec.
4. Verify cross-references from CLAUDE.md and specs
   into HANDOFF Open numbers still resolve.
5. Single atomic commit. Easy to review or revert.

**Don't change live decisions during cleanup.** This is
a structure refactor. If you find a closed Open whose
decision now seems wrong, flag it for the user — don't
quietly re-decide.

## The archive split — `ARCHIVE.md`

One file per project, at the repo root. It holds **the record of how the thing got built**, which
nothing reads to decide anything. The handoff keeps only what a next session needs in order to
*act*.

**One name, and it is `ARCHIVE.md`.** This doc used to say `HANDOFF-archive.md`, in the cleanup
pass and in "Recent sessions" — two passing mentions and no section of its own, which is how a
convention goes unfound: one project's split on 2026-08-07 was designed from scratch by a session
that never saw either. If you meet a `HANDOFF-archive.md` in an existing project, rename it and
update the pointer rather than running two conventions.

**The test is a question, not a date:** *would a session act differently for having read this?*
If no, it is archive.

| Moves | Stays |
|---|---|
| Dated build logs, "what we built" narratives | Open items, anything unresolved |
| Per-session Status checklists | Active decisions (they get cited) |
| Superseded plans and checklists | The next-session prompt / Start here |
| Design x-rays whose conclusions reached canon | Lessons that still change behaviour |
| Closed queue items whose detail is spent | Dated *commitments* — a future date is live, not history |

**Split when the handoff is mostly narrative of what past sessions did**, or when it has grown
past the bloat triggers above. Not on a schedule.

**And demote as you land, so the split stays rare** (added 2026-08-12, after one project's
handoff grew from ~1,500 back to 2,940 lines in the five days after its split): when a landing
writes a new "Last updated" block, demote the previous session's block **in the same edit** —
its narrative moves to `ARCHIVE.md`, and what stays behind is a stub line (date, session name,
what shipped in one sentence) plus any still-live nuggets distilled out where the next session
will meet them. Steady state: the current block, at most one previous block kept whole where
its detail is still load-bearing (an unbuilt spec, an unresolved thread), and a stub list.
A project may also carry a size tripwire in its test suite (one project's test fails the build
when its handoff passes 1,800 lines) — that is the backstop, not the mechanism; this step is the
mechanism.

**Always leave a pointer at the split**, in the handoff, naming what moved and what belongs
there in future. Without it the handoff refills with exactly the same material, because the next
session has no way to know the split happened. One short section, not a sentence buried in prose.

**Give `ARCHIVE.md` a header that says what it is for and where live state lives**, so a cold
reader who opens it first is redirected in one line rather than mining it for current truth.

**Never archive to make a handoff look tidy.** The cost of over-archiving is invisible and
expensive: a session re-derives something that was already settled, or re-argues a decision whose
reasoning it cannot find. When genuinely unsure, keep it in the handoff and compress it instead.

## Session log discipline (rolling mode)

What goes in a session-log entry:

- **DO log:** new Opens captured, closed Opens (1 line
  pointing at the breadcrumb), specs created or
  meaningfully edited, schema migrations, decisions made
  this session that don't have an Open of their own.
- **DON'T log:** detailed reasoning that's already in a
  closed Open's spec destination. The closure breadcrumb
  + the spec entry are sufficient. Session log just
  notes "closed Open #N" — not the full why.
- **Format:** `### YYYY-MM-DD — [headline]` then 2-5
  lines. Files touched on a separate line at the end if
  useful.

If a session entry would duplicate what a closed Open
breadcrumb says, drop the entry. Git log + the spec is
the trail.

## Cleanup Protocol

### Single-session mode

When the handed-off work is **complete:**

1. Check if anything in the handoff should be preserved
   (decisions → journal or project CLAUDE.md, gotchas →
   project CLAUDE.md).
2. Delete the HANDOFF file (whichever name it used).
3. Mention the deletion to the user so they know the
   work is wrapped up.

### Rolling mode

The HANDOFF stays — what wraps up is individual Opens.
Apply the Closure Pattern when each Open completes.
The HANDOFF file itself only gets deleted if the entire
project is wrapped up or archived; that's a separate
deliberate decision.

## Plan Checkpoints

For any plan where the total work could plausibly
exceed one context window, insert checkpoints at
natural phase boundaries (not after every step).
Use judgment — a 4-step plan with complex steps
needs checkpoints; a 7-step plan of simple edits
doesn't.

At each checkpoint, assess:

- Is remaining work larger than what's done?
- Am I losing detail on earlier steps?
- Would a fresh context actually help?

If yes to any: write the handoff, tell the user,
and let them decide whether to continue or start fresh.

Don't wait until context is critical. Write the
handoff one phase early rather than one phase late.
