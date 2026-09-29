---
name: journal
description: Write a short dated journal entry for this session and log any friction. Use at session end, when /land runs, or when the user says "journal this" or "let's wrap up".
---

<!-- Kit note (delete this comment when you install): the day-one journal. Fill in
<journal folder> and install at ~/.claude/skills/journal/SKILL.md. Before the first run,
create <journal folder>/FRICTION-LOG.md and paste in the "Log format" section of the kit's
reference/friction/README.md as its header; the weekly reader that gets added at the
two-week check-in parses that format. The full version this grows toward is
reference/commands/journal.md. -->

# Journal

Entries are for finding things later, not for recording everything. A 10-line entry that points to the right files beats a 60-line one that retells the session.

**Where:** `<journal folder>/YYYY-MM-DD.md`. If today's file exists, add the new entry below the last one.

## Steps

1. **Clock.** Run `date` (or `Get-Date` in PowerShell) and use it for the header. Never ask the user the time.
2. **Draft the entry:**
   ```
   # <Month Day, Year> - <time>
   **Session:** <project>, one line on what this session was
   **TL;DR:** 2-3 sentences: what changed, what was decided, what's next.
   **In their words:** one thing the user said that captures the session, quoted.
   **Tags:** #project #topic
   ```
   Add a **Decisions** line only when a decision was made that's worth citing later.
3. **Friction check.** Four questions:
   - Where did the user correct me, ask what I meant, or have to say something twice?
   - Did I call something done or true without checking the real thing?
   - Did I act (commit, send, build) before the user said yes?
   - What cost time that wasn't a judgment call: a tool failing, something broken or out of date, a step the user did by hand?

   For each yes, draft one line in the format in `FRICTION-LOG.md`'s header (read the header; don't write the tags from memory). "Nothing to log" is a complete answer.
4. **Show the entry and any friction lines, then wait for a yes.** Nothing is written before that.
5. **Save.** Write the entry to the dated file and append the friction lines to `<journal folder>/FRICTION-LOG.md`.

## Growing this

The kit's full version (`reference/commands/journal.md`) adds decision extraction, git checks, a restating check and more. Add a piece when you miss it, not before.
