---
name: land
description: Close out the session: check the clock, say anything held back, save what's worth keeping, update the handoff, write the journal entry, and check for unpushed work. Use on /land, or when the user signals the session is ending ("let's wrap up", "that's it for today", "before we stop").
---

<!-- Kit note (delete this comment when you install): the day-one close-out. Install at
~/.claude/skills/land/SKILL.md. It calls /journal, so install the day-one journal with it.
The full version this grows toward is reference/skills/land-SKILL.md and the tools it
calls (/surface, /capture, /handoff). -->

# Land

Every session writes to the stores the next session reads. Without this, memory and the journal starve.

1. **Clock.** Run `date` (or `Get-Date` in PowerShell) and say it: "Landing as of Tuesday 2026-09-29, 4:10pm." Never ask the user the time.
2. **Anything unsaid.** If you held something back this session (a concern, a better idea, a blind spot), say it now in a few lines. If not, skip it.
3. **What's worth keeping.** List what this session decided or learned that a future session would need, and propose where each item goes: a memory note, a CLAUDE.md line, the project's handoff, or just the journal. Show the exact text for anything going into memory or CLAUDE.md, and write only what the user says yes to.
4. **Handoff.** If the work continues in another session, update `HANDOFF.md` at the project root, or create it:
   ```
   # Handoff: <project>
   **Updated:** <date>
   ## Goal: one or two lines
   ## Where it stands: what's done, checked against the files, not memory
   ## Next step: the first thing the next session should do
   ## Open questions
   ```
   Update it; don't rewrite it. Skip this for one-off sessions.
5. **Journal.** Run /journal. It shows its draft before saving anything.
6. **Ship check.** If a repo was touched, run `git status` and offer to commit anything uncommitted. Pushing or deploying needs the user's yes for that push. Wrapping up is not a yes.

Say which steps you skipped, one line each. Before writing a past-tense claim ("pushed", "updated"), check that it's true on disk.

## Growing this

The kit's full close-out (`reference/skills/land-SKILL.md` and the tools it calls) adds a routing sweep, a one-question read check, a next-session prompt and more. Add a piece when you miss it, not before.
