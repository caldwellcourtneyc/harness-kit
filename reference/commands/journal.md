Capture session learnings as a journal entry. Default is a session line, TL;DR, three short mirror fields (user's words, caught by, closes), and tags; sections are added only when they earn their place (decision worth citing, failure mode, trajectory shift). Routes durable content to artifacts/decisions/memory and references it. Shows draft before saving. Use at session end or when context window is filling. For unshared insights and blind spots, run `/surface` first.

**Location:** `<your journal folder>/YYYY-MM-DD.md`

<!-- Kit note (delete this comment when you install): from Courtney's /journal. The
retrieval-not-documentation principle, the draft-first gate, and the length gate are general.
Placeholders to fill: <your journal folder>, <your code folders> (for the dev health scan), <your task tracker> (drop those lines if you
don't keep one), and <your friction folder>. The friction section points at two files you
create from the kit's reference/friction/ folder (its README walks you through it); the weekly
synthesis that reads the log lives there too, so install both halves together. The restating
check needs reference/tools/journal-overlap.py copied to ~/.claude/tools/. The Session line
points at the session transcript; Claude Code deletes old transcripts after a set number of
days (cleanupPeriodDays in settings.json), so raise that if you want the pointers to keep
working. Install as a skill at ~/.claude/skills/journal/SKILL.md (see SEED.md, "Installing a skill"). -->

---

## Default = the minimum entry

The minimum entry is the standard entry: Session line,
TL;DR (2-3 sentences naming the project), the three
mirror fields, and Tags. ~9-14 lines total. Most sessions
land here. The Session line and mirror fields are part
of the minimum, never optional sections: when an entry
gets shortened, they are not what gets cut. (Every past
format shrink cut the user's words first.)

**Adding any other section requires a named reason.** Before
drafting a section, state to yourself why it can't live
elsewhere and why it's worth retrieving later. Default
reasons that earn a section:

- **A decision was made** worth questioning or citing later
  → `## Decisions` (extracted to ADR in weekly review)
- **A failure mode was diagnosed** with non-obvious cause
  → `## Learnings` + `#failure-mode` tag
- **A project's trajectory shifted** → triggers timeline
  check (see Tidy-up)
- **An observation about the user's work** not yet in
  MEMORY but possibly should be → `## Observations`

Reasons that are NOT enough on their own:
- "We did a lot today" — work lives in commits, the task
  tracker, and artifacts. Reference, don't restate.
- "It felt important" — importance lives in durable files.
  Journal points to those.
- "The user said something interesting" — if it's a
  preference or pattern, that's a MEMORY candidate, not
  a journal section.

**Principle: retrieval, not documentation.** A tight 10-line
entry that points to the right places beats a 60-line entry
that restates the session.

**If you suspect the session has unshared meat** (held-back
insights, missed considerations, blind spots), suggest
`/surface` before drafting. The user decides what to fold
into the entry.

**Override:** If the user asks for a "full" or "meaty" entry,
expand without justifying each section.

If the user asks for "brief" or "quick," hard cap: the
minimum entry only (Session line, TL;DR, mirror fields,
Tags). Skip Tidy-up dev checks. Friction Capture still runs.

## Pre-save check

For each section you're tempted to write: if it paraphrases
an artifact, decision, or memory file that already exists,
cut the prose and keep only the link.

**Durability tripwire.** The journal is retrieval/history, not
live canon — it gets searched, not treated as source of truth.
Scan the draft for any standing decision, convention, or
invariant (a rule future code or sessions must respect), as
opposed to session history. If found, it needs a home that
outlives the journal — most-durable first: **code comment** (if
it governs code) → project **CLAUDE.md / README** (cross-cutting
knowledge) → **Decisions/** ADR (why X over Y) → **Artifacts/**
/ **MEMORY.md** / the task tracker / project timeline
(existing routing). Write it there first; the journal just
records that it happened and points to it — never the only copy.
Surface the routing to the user; don't silently relocate.

## Draft Flow

1. Assess session weight
2. Draft the journal entry
3. **Run the Length Gate (below), then show the draft — banner first — in chat**
4. Incorporate edits
5. After approval: save journal
6. Run Friction Capture (see section) — route qualifying items to the friction log

Never save without showing the draft first.

### Length Gate (mechanical — prepend to every draft)

The terse-by-default rule keeps failing because it is *self-administered*: "add a
section only for a named reason" always finds a reason from inside a draft written
with the whole session still loaded. In the harness this comes from, the user cut an
over-long entry at least four times (08-02, 08-05, 08-06 ×2), and the 08-06 ruling was
that this needs a mechanism, not a fifth restatement. The gate does not shorten the
entry — it makes the overrun **visible before the user reads it**, which is the part that
keeps sliding through. (Loosened 2026-08-16, the user's call: target 10 → 15, auto-trim
15 → 25 — the tight version was starting to over-compress entries whose sections were
earning their place. The banner and cut-list mechanics are unchanged; they were the real
fix.)

Before showing any draft, **COUNT its lines** (don't estimate — reading from loaded
context is exactly why length is invisible from the inside) and prepend this banner:

    [length: N lines vs ~15 target · beyond the minimum entry: <none | Decisions, Learnings, ...>]
    <one line per extra section: the named reason it can't live in a commit / artifact / memory instead>

**Restating check (optional, needs `journal-overlap.py` installed to `~/.claude/tools/`).**
Save the draft to a scratch file and run:

    python ~/.claude/tools/journal-overlap.py <draft file> --session <session id>

It compares each draft line against the files this session wrote (Write/Edit calls in the
transcript) and prints a `[restates: ...]` fragment. Put that fragment on the banner's
first line, after the section list. For each flagged line, replace it with a pointer to
the file unless you can name why the line earns its place. It catches copied or lightly
trimmed lines, not paraphrase, so a clean result is not proof the draft doesn't restate.

- **If N is over ~25 and the user did NOT ask for a "full" / "meaty" entry:** default
  the draft DOWN to the minimum entry before showing it, and list what you cut and where it
  routed. Show *that* version. Expanding back up is the user's call, made against the trimmed
  draft in front of them — not yours, made against the long one they never saw.
- **Show the banner wherever the draft is shown.** The banner travels with the draft.
- **Brief/quick mode:** the banner still runs; the cap is already the minimum entry, so it
  just confirms N and lists nothing.
- The existing **Override** stands: if the user asked for a full entry, expand without
  justifying each section — but still print the banner so N is on the record.

## Header Format
```
# January 16, 2026 - 10am
```
Read the clock (`date`, or `Get-Date` in PowerShell)
for the date and time. Never ask the user. If
multiple entries for the same day, append with a new
time-stamped section.

## Tone
- Conversational, not formal
- Substantive but not verbose
- Capture reactions the user expressed (delight, frustration,
  surprise), quoted, never inferred
- Bullet points are fine, but wrap them in narrative

## Sections

All sections are optional except the Session line, TL;DR, mirror fields, and Tags.
Include a section only when the session warrants it.

### TL;DR (Always)
2-3 sentences. What happened, what changed, what
matters. This is the minimum viable entry.

**Always name the project explicitly in the TL;DR's
first sentence** (e.g., "On [project], …" or "[Project]
voice work today: …"). Tags name the project too, but
the entry should be self-describing when read in
isolation — the body of a brief entry shouldn't require
the reader to look at the tags to know which project
it's about.

### Session line and mirror fields (Always)
Directly under the section header, before the TL;DR:

    **Session:** <session id> (<cwd slug>) | **Model:** <model id; note any switch> | **Author:** <Claude / Codex>, <live / backfilled YYYY-MM-DD> | **Private:** <y / n>

After the TL;DR, three short fields. "none" is a legal value for each:

- **User's words:** 1-3 lines the user said this session, quoted exactly. Include a verdict or approval when there was one, not only corrections. Anything paraphrased is marked "(paraphrase)".
- **Caught by:** for each notable miss this session, who or what caught it: the user / Claude self-review / hook or test / another model.
- **Closes:** earlier entries whose outcome this session learned: "<date> <item>: held / didn't / unknown". The journal is append-only, so outcomes are recorded forward, never by editing the old entry.

Filling the Session line: the session id is the UUID segment of the scratchpad or transcript path in your environment; the cwd slug is the `~/.claude/projects/` folder name the session is filed under. If you cannot see either, write *(not captured)*; never guess an id. Model is your own model id. Private is `y` for health, family, money, or personal-life sessions, so mining passes can skip them without a manual sort.

Why these exist: the session transcript holds the full record (with the model recorded per message), so the journal's job is the pointer plus the judgment the transcript can't hold: which of the user's words mattered, who caught what, and whether it held.

Two companion rules: feelings, energy, or satisfaction go in only when the user said them, quoted, never inferred from length or session count. Observations about the user stay descriptive (what they did); any judgment of it goes on its own line, so praise and evidence don't blend.

### What We Did
Summary of session work — what was built, changed,
decided, discussed.

**Keep it lean.** One line per item. State *what changed*,
not *how it was done*. No implementation details — those
live in code and commits. Reference commits or artifacts
when useful.

### Decisions
Decisions made this session. One line each: what was
decided, the reason in a clause, and where it lives.

    **[What]:** [reason, one clause]. → [ADR path | doc path | see session]

Add the longer form, "Considered [alternative], rejected
because [why]", only when the decision has no other
durable home. The rejected-alternative reasoning is the
part a transcript buries, so it earns space exactly when
nothing else holds it; when an ADR or doc already carries
it, the line points there instead of restating it.

Consistent format enables batch extraction during
weekly review. Not every session has decisions — only
include when something was actually decided.

### Learnings
Explicit, actionable takeaways. Be direct.

**For the user:**
- What could have saved time or friction
- Patterns worth continuing or avoiding

**For Claude:**
- Mistakes and what to do differently
- Wrong assumptions or misdiagnoses

**Failure modes are high-value content.** If something
broke and the cause was non-obvious, give it explicit
documentation — in Observations, Learnings, or its own
section. These are the entries most worth retrieving
later.

### Observations & Impressions
**Archive slot, not generator slot.** Capture only
patterns about the user's work or decision-making
that are worth retrieving later — specifically,
candidates for a MEMORY entry that aren't ready yet
(need more data, or you're flagging the pattern for
later). One or two items max in a typical entry.

Ephemeral candor — critiques, in-the-moment reactions,
blind-spot calls, unshared insights — belongs in
`/surface` output, which the user sifts and folds
archive-worthy bits into here or directly into
memory. Don't duplicate `/surface` content here.

Include only when a pattern is genuinely worth
retrieving. Skip otherwise.

### The User's Take
Include ONLY when the user provides a blurb. Shape
into journal format while staying faithful to what
they said.

**Critical rule:** Only include reactions they
explicitly state. Don't infer or fabricate.

### Open Threads
Reference open items in `<your task tracker>` — don't
duplicate their content here. Example: "New items
created: [X], [Y]. Completed: [Z]."

### Context for Future Sessions
Where we left off, gotchas, relevant history.

### Connections
Links to patterns from earlier sessions, related
work in other projects.

### Files Created/Modified
When included, embed inside Context for Future Sessions
rather than as a standalone section. Use full absolute
paths (forward slashes) — never relative paths.

## Decision Extraction

Decisions are captured journal-first in the `## Decisions`
section of each entry. ADR extraction to `Decisions/`
happens during weekly review — not end-of-session. ADR
format lives in `/decide`.

## Tags

Add tags at the end. See project CLAUDE.md for the
full tag list.

## Tidy-up (Before Drafting)

Run these checks silently. Incorporate findings into
the entry — don't present as a separate checklist.

### Dev health scan
Discover active repos: directories under `<your code folders>`
modified in the last 7 days that contain a `.git` folder.
Run `git status --short` against those in parallel.

Note uncommitted changes under Context for Future
Sessions. If clean, don't mention it.

### Unpushed-commits check
`git status --short` reports only the working tree — it stays
silent when commits are piling up locally unpushed. So for each
active repo with an upstream, ALSO run the ahead-count:

```
git -C [path] log --oneline @{u}..HEAD
```

(or `git -C [path] rev-list --count @{u}..HEAD`). If a repo is
ahead of its upstream, surface it: "N commits unpushed on
[repo] — push to [branch]?" and offer to push after journal
save. Repos with no upstream configured are skipped silently.

Why this earns a step: for a repo that isn't in a synced or
backed-up folder, pushing is the only off-machine backup, so
unpushed commits are a single on-disk copy. Failure mode
observed 2026-06-01 on one project: the remote sat ~10 days /
17 commits behind because the scan only checked working-tree
state, never ahead/behind.

### Stale branch check
For each repo:
```
git -C [path] branch --no-merged main \
  --format="%(refname:short) %(committerdate:relative)"
```
Flag branches older than 7 days.

### CURRENT_CONTEXT.md update
If the project has one, update it. If it doesn't and
the work is multi-session, suggest creating one.

### Timeline update check
Skip unless the current project has `memory/project_*.md`
files with `## Timeline` sections. Timelines track trajectory
shifts (direction changes, activation/deprioritization, major
milestones) — not incremental work or bug fixes.

If this session produced a shift, draft a terse entry:

```
- **YYYY-MM-DD** — [What shifted]. [Brief context]. → [pointer]
```

Pointer = relative path to the driver. Include the proposed
entry as a labeled block outside the journal body. After
approval, append to the memory file. No reindex needed.

If a project has real evolution but no timeline yet, surface
it as an open thread. Runs even in brief-mode.

## Friction Capture

Friction does not live in the journal body — it routes to the shared
friction log so the weekly synthesis can read it in one place. Runs every
session, including brief/quick mode (exempt from the brief-mode cap).

At session close, run the watch-for list at
`<your friction folder>/WATCH-FOR.md`
— the **core tier** plus the shared **sweep** and **blind-spot
proxy**. For each item that clears the relevance gate (recurred, cost
real time, or would change a workflow), append one line to
`<your friction folder>/FRICTION-LOG.md`
in the documented format, tagged with source, type, and evidence
strength. The type vocabulary is defined in the log's own header —
read it there rather than from memory.

- Show what you're logging before appending (same draft-first rule).
- "Clean session — nothing to log" is a complete, valid outcome. Don't pad.
- Source-neutral: log tool/workflow/setup friction, not just agent behavior.

## After Saving

1. **Run Handoff Reception Audit (if applicable)** — if this
   session picked up from a HANDOFF file at the project root,
   write a brief audit entry per the Reception Audit section
   in the /handoff skill. Append to `HANDOFF-audit-log.md`
   at the project root. Skip if no handoff was picked up.

2. **Update `<your task tracker>`** — if the session
   created, resolved, or advanced any open items, update
   them there.

3. **Reindex the journal search** so the new entry is
   searchable.
