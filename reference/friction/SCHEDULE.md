# Schedule — who runs the weekly synthesis, and when

**Held at hypothesis strength for your setup.** This is what has worked in Courtney's system after the version that didn't. Trial it for four weeks with the kill condition below; keep whatever survives.

## The cadence

**Weekly, on a fixed day and time. Friday morning here.** Weekly is often enough that patterns have a few entries behind them and rare enough that the synthesis is a short read.

## Who runs it: the system, not a person remembering

Three ways to own the run, in the order they have earned trust here:

1. **A scheduled automation.** In Courtney's setup this is a second agent's cron automation (Codex, Fridays at 9). In Claude Code, use a scheduled task that outlives the session: a Desktop scheduled task in the Claude desktop app (it runs on your machine, so it can read the log), or a cloud routine if the log lives somewhere the cloud can reach. In-session reminders and /loop stop when the session ends, so they can't own a weekly run. The automation reads the log and the watch-for list, samples two or three real session records from the same window as a check on what the log missed, and writes **one new dated file** into the friction folder named `friction-scan-<start>_to_<end>-<agent>.md`. It modifies nothing else: not the log, not the prompts, not rules or skills. That constraint is what makes an unattended run safe, and the new-file rule is what makes its output reach a reader (see the README's delivery lesson). This is the only owner that has survived here.
2. **A standing line in CLAUDE.md.** "At the start of the first session each week, run `friction-scan.js`; if it reports more than N entries since the last synthesis, run the friction-scan skill before other work." The trigger lives on the system's side, which is the principle; but it depends on a session happening, and on Claude reading that line with attention on a busy Monday. Cheaper to set up, less reliable.
3. **A manual ritual.** "I'll run it Fridays." This is the version that stalled for two months. Listed so you recognize it, not so you pick it.

## What the run must produce

A file a person will open. Not a chat message that scrolls away, not a private memory file, not a notification. The synthesis is *for* the human who then makes the one fix; if it doesn't reach them, the loop is measuring and not preventing.

## First run

After two weeks or twenty entries, whichever first. Run the reader, then the skill. Read the result yourself. Make the one smallest fix it proposes, or write down why not.

## Kill condition (the trial half)

After four weekly runs, ask one question: **has a person read a synthesis and changed something because of it?**

- Yes → the loop is live. Keep the schedule; start tuning the watch-for prompts from what the syntheses say.
- No, because syntheses ran but weren't read → the problem is delivery. Fix where the file lands or how you're told about it before touching anything else.
- No, because the runs didn't happen → the owner is wrong. Move up the list above (from a ritual to a CLAUDE.md line, or from that to an automation).
- No, because the log is nearly empty → the capture half isn't firing. Check that the journal command actually runs the watch-for prompts at close; a skipped close-out step throws no error.

Don't add a dashboard, a second reader, or a richer report until this question has been answered yes once.
