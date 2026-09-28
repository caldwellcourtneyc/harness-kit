---
name: land
description: Land the session: run the whole close-out chain (surface, capture, handoff, journal, ship check) as one move instead of four separate requests. Triggers on /land, or when the user signals the session is ending in plain words ("let's wrap up", "before we stop", "let's journal", "capture that and do the handoff"), or returns to a stale session just to close it ("I wandered off from this").
---

<!-- Kit note (delete this comment when you install): this is a portable version of Courtney's
/land. Hers also stages the close-out onto a live session dashboard and syncs a task tracker;
both are left out here. Install at ~/.claude/skills/land/SKILL.md. It calls the other close-out
tools by name. If one isn't installed, skip that step and say so in one line. -->

# Land

The most valuable things in a working session leak out right at the end. You solve something, make a decision, park a good side thought, then close the window, and it's gone, because it only ever lived in the chat. Landing is the deposit half of the harness: every session writes to the stores the next session reads. Without it, memory and the journal starve.

Before this existed, the close-out was typed piecemeal, three to five messages a session. /land runs the whole descent as one move.

**This is a sequencer, not a rewrite.** /surface, /capture, /handoff and /journal own their protocols. Invoke them and follow their files. /land only decides the order, applies the skip rules, and carries the timestamp through.

## Step 0: Clock check (always first)

Run `date` (or `Get-Date` in PowerShell) and state it: "Landing as of Thursday 2026-07-09, 3:40pm."

- Never trust the conversation for today's date. Sessions often span days, so the date at the start is stale by the close.
- Never ask the user what time it is. The clock is authoritative.
- If the work happened over several days, the journal entry still gets today's header; note the actual work dates in the body.

## The descent

Run in this order. Surface feeds capture, and capture routes items before the journal so the journal can point at them instead of restating them.

1. **/surface.** *Skip if the session has nothing held back.* Candid, in chat: insights not yet said, considerations missed, blind spots. A trivial or purely mechanical session skips straight to capture. Don't manufacture insights to justify the step.

2. **/capture.** The routing sweep: every item worth keeping gets a destination (memory, a rule candidate, a project doc, the journal). Propose; the user rules. This step almost never skips. It's the reason to land at all.

3. **One read to check.** *Only when the session left a real uncertainty about how the user is thinking about something, and the answer would change future work. At most one per landing.* State your current read as a sentence they can react to, not an open question: "My read is that you want this mainly for the team, not for yourself. Right?" Reacting is cheaper than writing an answer. Whatever they confirm or correct is a memory candidate: show the exact entry and get a yes before writing it. Most landings have none. Skip rather than invent one.

4. **/handoff.** *Only if the project has a HANDOFF.md or the work clearly continues in another session.* Update it, don't rewrite it. Skip silently for one-shot sessions.

5. **/journal.** With the Step 0 timestamp in the header. **Actually load the journal command and run its protocol. Don't improvise a journal from memory.** Under close-out momentum the journal step feels like a quick fire-and-forget. It isn't, and improvising it is how entries land in the wrong place and skip the user's review. Two hard stops:
   - **Show the draft and wait for the user before writing anything.** A journal written first and shown second has already failed this step. It is the most-skipped gate in a close-out, so treat a write before their reply as a bug.
   - Then its tidy-up checks, the friction review (the journal command's friction section), save to the dated file, and update the search index if you have one.

6. **Ship check.** The journal's tidy-up just gathered git state; act on it. Offer to commit anything uncommitted. **Push, deploy, or anything other people can see needs the user's explicit yes.** "Land the session" is not consent for remote actions. When you ask, name the repo, the branch, and what's in it.

7. **Next-session prompt.** *Only when the work continues in another session.* Give a ready-to-paste prompt (clear on the goal, open on the method), plus where to open it. Show it in the message itself, in a code block. Also write it into the project's HANDOFF.md so it survives if the chat is lost.

Between steps, keep the thread. Before writing any past-tense claim ("pushed X", "updated Y"), check that it's true on disk. A placeholder is better than a claim that isn't true yet.

## Landing a stale session

When the user comes back to a session days later just to close it out:

- Clock check first. The gap is exactly when the date goes most wrong.
- Compress the descent: skip /surface unless something real was held back; capture and journal what would otherwise be lost; keep the entry brief. This is salvage, not ceremony.
- If they can't remember what's uncaptured, that is the job: scan the session for unrouted decisions, flagged items and open threads, and present the list.

## Skip rules

| Step | Skip when |
|------|-----------|
| /surface | Nothing held back; trivial or mechanical session |
| /capture | Almost never; only truly empty sessions |
| One read to check | No real uncertainty that would change future work (the usual case) |
| /handoff | No HANDOFF.md and the work isn't multi-session |
| /journal | Never. The minimum entry always runs |
| Ship check | No repos touched this session |
| Next-session prompt | The work doesn't continue |

Announce skipped steps in one line ("no handoff, single-session work"). Don't silently omit them. The user should see that the chain ran, even where a step did nothing.

## What this is not

- Not a replacement for the tools it calls. Each can still run on its own mid-session.
- Not a summary generator. The outputs live where the destination tools put them; /land itself writes almost nothing of its own.

## Lessons

| Date | Lesson | Change |
|------|--------|--------|
| | Rows accrue from your own use. | |
