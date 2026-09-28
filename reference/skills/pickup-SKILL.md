---
name: pickup
description: Re-enter a session after time away — reconstruct where things left off, what's uncaptured, and what was promised, then fork to continue or land. Triggers on `/pickup`, or automatically when the user signals a cold return in prose — "I wandered off from this convo", "where were we?", "what's the status here?", "did you get interrupted?", "picking this back up" — or when they return to a session that's clearly days stale.
---

# Pickup

Sessions here routinely sit idle for days and get re-entered cold. The failure modes of a cold return: responding to the newest message while dropping prior "I'll do X next" commitments, trusting a stale sense of what's on disk, and not knowing what's uncaptured. /pickup is the re-orientation pass that runs before any new work.

**This is re-entry, not close-out.** /land closes a session; /pickup reopens one. They meet at the fork at the end.

## Step 0 — Clock check

Run `date` (Bash) or `Get-Date` (PowerShell) and state the gap: *"Picking up as of Thursday 2026-07-09, 10:56pm — last activity in this session was July 5."* The idle gap is exactly when Claude's sense of "today" is most wrong. Never ask the user for the date.

## The reconstruction

Four scans, then a short readout. Do the scans; keep the readout tight.

1. **Last landed work** — what was the most recent *completed* thing? One line.
2. **In-flight commitments** — search the conversation for promises: "I'll do X next", "then we can Y", planned-but-unstarted steps, and the task list's `pending`/`in_progress` items. These are the things a cold return silently drops.
3. **Disk truth** — verify remembered state against actual file state before repeating claims from earlier in the conversation (files change between visits: other sessions, file sync, the user's own edits). If the project has a HANDOFF.md, check whether it postdates this session's last activity — a newer handoff means another session moved the work.
4. **Uncaptured value** — decisions, insights, or flagged items ("love this", "capture that") from before the gap that never got routed. This list feeds /land if they choose to close.

## The readout

3-6 lines, then the fork. Format:

> **Where we left off:** [one line]
> **Still owed:** [commitments found in scan 2, or "nothing in flight"]
> **Changed since:** [disk drift worth knowing, or omit]
> **Uncaptured:** [items, or "journal is current through the gap"]
>
> Continue with [the owed thread], or land this session?

Don't summarize the whole session — the user was there. Reconstruct only what the gap put at risk.

## The fork

- **Continue** — resume the owed thread (not just the newest message). New direction from the user overrides, but name the dropped thread in one line so the drop is a choice, not an accident.
- **Land** — hand to /land in its compressed "stale session" mode; the uncaptured list from scan 4 is its input.

## What this is not

- **Not /land** — no journaling, capturing, or handoff writing happens here; /pickup only decides what's live.
- **Not a session summary** — it reconstructs risk (dropped commitments, stale claims, unrouted value), not history.
- **Not a replacement for your session-start habit** — starting work on a *project* after absence still follows it (read project CLAUDE.md, HANDOFF, recent context). /pickup covers re-entering a *conversation*.
