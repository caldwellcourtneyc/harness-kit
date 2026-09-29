Loss-prevention sweep that routes important items from the current session to durable storage. Surfaces what would be lost if the session ended right now AND what the user flagged inline ("let's capture this" / "love this" / "don't lose this" / "important") that hasn't been routed yet. Use mid-session for curiosity check-ins, at session end for the sweep, or any time the loss-worry hits.

<!-- Kit note (delete this comment when you install): from Courtney's /capture. The sweep-and-route
method is general; the destination list is her storage map made generic, so rewrite it to match
where your things actually live. Placeholders to fill: <your journal folder>, <your task tracker>,
<your taste file>, <your system-work folder>, <your project map>. Drop any destination you don't
keep. Install as a skill at ~/.claude/skills/capture/SKILL.md (see SEED.md, "Installing a skill"). -->

## What This Is

A routing skill that proposes WHERE each captured item should go. /capture overlaps with /journal on journal-bound items but has broader scope — many destinations beyond the journal entry. Different from /surface (which catches what Claude didn't say) and /handoff (which writes the HANDOFF.md).

The point is to make capture more clearly defined — replacing the verbalized "love all this, let's capture" + end-of-session vibes-check with a structured sweep.

## When to Invoke

**The user invokes when:**
- Mid-session curiosity ("did we get everything so far?")
- End of session as the durable sweep
- Anytime the worry hits ("are we losing something?")
- During open-ended thinking, if they want to route flagged items

**Claude invokes unprompted when:**
- The user signals session wrap ("let's wrap up," "I'm done," "good session")
- A substantive decision or pattern lands without explicit capture
- An open-ended exploration is ending (mode shift)

## When NOT to Fire

- Trivial sessions with no substantive content
- Inside an active /decide flow — /decide is exploring; capture comes after
- Auto-firing mid-exploration (user-invoked is fine; Claude-auto would kill it)

## Protocol

**Read the decline log first, and calibrate from it; never suppress a kind because of it.** Read the last ~40 lines of `~/.claude/refs/capture-declines.md` (skip if it doesn't exist yet). The user's reasons are the signal: each decline says what made that item not worth saving (a one-off pick isn't a standing preference; a point about images doesn't apply to an AI that doesn't make them). A new item of the same kind → destination gets proposed only if it clears the bar those reasons set, and says in a few words how it differs from what was turned down. Don't hold back a whole pair because it has been declined before. (An earlier version held back any pair declined twice in 60 days; it was retired the first time it fired, because the user wanted calibration, not suppression.) Inline flags are always proposed.

**Start with the dodge.** What's the most important thing from this session that has no durable home yet? Name it before scanning.

**Then sweep by destination.** Items come from two sources:

1. **Inline flags** — anything the user verbalized as "capture this," "love this," "don't lose this," "important," etc. Highest priority; route them first.
2. **Retroactive scan** — items neither party flagged but that would be lost without /capture firing.

Skip destinations with no items. Per item, format as:

`- [kind → destination] short description. (one-line rationale)`

If an item belongs in more than one place, primary destination = where the canonical record lives; secondary destinations get a pointer/link.

### Kinds of items to scan for

- **Patterns / insights** — Claude failure modes, the user's work patterns, project dynamics
- **Decisions** — what was decided or deferred
- **Action items / open threads** — clear next steps not yet done
- **Raw insights** — half-formed ideas worth keeping
- **References** — external sources, names, vocabulary
- **Taste preferences** — encoded preference signals

### Destinations

- **Code comments** — conventions/invariants that govern code (schema rules, non-obvious constraints, "don't do X here" warnings). MOST durable: travels with the code, survives every doc rewrite.
- **Project canon** — project `CLAUDE.md` / `README` for cross-cutting "things to know" (architecture, conventions, gotchas a new session needs).
- **Journal** — session capture, `<your journal folder>/YYYY-MM-DD.md`
- **Handoff** — project HANDOFF.md updates for continuity
- **Memory** — patterns, preferences, references for future sessions (auto-memory file)
- **Open threads** — `<your task tracker>`
- **Taste profile** — `<your taste file>`

**Decisions, Artifacts, Audits — route by scope.** These three destinations have two homes depending on whether the item is project-specific or cross-cutting system work:
- **Project-specific** (a decision or doc about one project): that project's `Decisions/` or `Artifacts/` folder.
- **Cross-cutting system work** (harness, skills, hooks, memory architecture, session facilitation — anything about how the whole system runs): `<your system-work folder>`, with its own `Decisions/`, `Artifacts/`, `Audits/`, and `HANDOFF-<topic>.md` at its root. The journal's folder is NOT the hub for system-work artifacts.
- Filename convention unchanged: `YYYY-MM-DD-title.md`.

Close with the open kicker (see Output Format).

## Durability

Findability asks "how will they find it." Durability asks "will it still
be here when they look." The HANDOFF and journal are NOT durable canon —
the HANDOFF gets compressed each cycle (round specs collapse to one-line
"Landed" summaries); the journal is searchable history, not live truth.

Before proposing a destination, ask of each item:

**"Does this need to outlive the HANDOFF's rewrite cycle?"**

- **No — it's pickup state** (status, next steps, what-landed, stale-line
  warnings, "deferred to fresh session"): HANDOFF/journal is correct. It
  SHOULD expire. Most items are this.
- **Yes — it's a standing decision, convention, or invariant** (a rule
  future code must respect, an architectural choice + its why, a "chose X
  over Y"): it needs a canonical home that survives doc rewrites —
  - Governs code → **code comment** at the code it governs (most durable)
  - Cross-cutting project knowledge → **project `CLAUDE.md` / README**
  - "Why X over Y" rationale → **Decisions ADR**
  - …then the canonical copy lives there; the HANDOFF/journal keeps a
    one-line POINTER to it (never the only copy). "Climb the ladder" means
    relocate-and-point, not delete-from-continuity.

The failure this prevents: burying a durable convention in a round's
HANDOFF section, then losing it when that section compresses. (Concrete:
2026-05-30 — the daily-log TEXT-timestamp convention + the no-migration-
versioning risk lived HANDOFF/journal-only until relocated to `schema.ts`.)

## Findability

Routing without findability is just dumping. Every proposal should
answer two things: where does it go, and how will the user find it
later.

### Per-item findability gates

Before proposing a destination:

1. **Duplicate check** — quick search the candidate destination for
   similar existing entries. If found, propose updating that entry,
   not creating a parallel one.

For each new file or entry:

2. **Name well** — filenames include date (YYYY-MM-DD) + topic slug.
   Existing entries get retrievable header anchors. Never `notes.md`.

3. **Surfaceable summary** — every new file gets a 1–2 line TL;DR or
   headline at the top, in the destination's native format. Imagine
   searching for this in 6 weeks — what would you search for?

4. **Pointer updates** — flag the after-save indexing the destination
   needs:
   - New memory file → MEMORY.md pointer added
   - Journal entry → reindex the journal search after save
   - New project folder/artifact → `<your project map>` update
   - Other destination-specific indices

5. **Tag for the destination's convention** — match existing tag
   shape (journal: `#tags`; taste profile: category header; memory:
   frontmatter or none). When unclear, check an existing entry.

Optional but useful: cross-link back to the source journal entry
when the capture came from a specific session — makes "find what
came from that conversation" possible.

## Output Format

A list grouped by destination. Each item one line. Empty destinations omitted entirely.

Then an **open kicker** at the end with two specific catches:
1. Items that fit none of the destinations above
2. Items so substantive they need new scaffolding — a project folder, artifact category, or container that doesn't exist yet. If found, surface the scaffolding need as its own recommendation — the user decides whether and where to create the new container.

## After the answer: log the declines

For each proposed item the user turns down, by name or by "everything except X", append one line to `~/.claude/refs/capture-declines.md` (create it if missing):

`YYYY-MM-DD | <kind> -> <destination> | <what was proposed, a few words> | "<their words, if any>"`

Log only what was declined, never what was approved. Silence is not a decline, so an item passed over gets no line. The same log takes declines of the other proposals /land makes (a handoff, for example), with that as the kind. The reader is this skill's own first step, above. Added 2026-09-24, after a review of past sessions found captures re-proposed and declined four times in a month.

## Tone

- Direct, specific
- Brief — each item is one-liner
- Honest about empty destinations (omit them, don't pad)
- Don't pre-write — propose, the user actions

## What This Is Not

- Not /surface (that catches unshared insights from Claude)
- Not /handoff (single-project continuity doc; /capture is multi-destination routing that may include HANDOFF.md updates among its outputs)

/capture is the routing decision; the destination skills do the writing. Overlap with /journal is expected — both touch journal-bound items.
