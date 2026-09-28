# CLAUDE.md skeleton: the always-loaded file, annotated

This is the *structure* of Courtney's global `~/.claude/CLAUDE.md`. Her personal content is replaced by placeholders, and a few short real lines are kept where a real line teaches better than a description (marked `> excerpt`). Every section carries a note (in blockquotes) saying what the section's job is. Your version gets built in the seed interview; this file is the map of what slots exist.

The single most important design fact: **this file loads into every session.** Everything in it is paid for every time, so it holds only (a) what must always be known and (b) pointers to everything else.

---

## About [you]

> *Job: who Claude is working for. Not a biography. The 3-5 facts that should color every response: expertise level, what you're building, how you learn. Claude adapts to whatever it knows about its reader; this is where it learns it.*

> excerpt (hers): "Learning through AI collaboration (vibecoding), no traditional coding background"

- [Your background as it bears on how Claude should explain things]
- [What you're working toward, held loosely]

## Working Style

> *Job: the standing licenses and expectations. This is where candor gets licensed. Without a written license, Claude defaults toward agreeable, which is where flat suggestions come from.*

> excerpt (hers): "Push back when warranted. No unearned praise or hollow validation."
> excerpt (hers): "If you notice a pattern worth mentioning (good or bad), mention it."

- [Your candor license, in your words]
- [How you want disagreement delivered]

## Communication

> *Job: how you think and how you read. The highest-leverage lines in the whole file are the ones that describe your cognitive style. They let Claude work with your grain.*

> excerpt (hers): "Write to be understood, not decoded." (with a note that compression, naming an idea without unpacking it, is the failure that bites hardest in documents read cold later)

- [One true thing about how you evaluate: examples vs. descriptions? detail vs. summary?]
- [Length preferences, jargon tolerance]

## Operational pointers (the pointer hub)

> *Job: retrieval triggers. Each line is "when X happens, go read Y." The file stays small because knowledge lives elsewhere; retrieval happens because these always-loaded lines say when. This section is the answer to "why doesn't my Claude bring in past context" (see guide/retrieval.md).*

- **[Trigger: e.g. "starting work on a project after absence"]** → read [the project's HANDOFF.md]
- **[Trigger: "something sounds like it happened before"]** → search [journal location]
- **[Trigger: "can't locate a project I named"]** → read [your project map file]

## Session habits

> *Job: the rituals that make context accumulate. Session start (read what exists before acting) and session end (deposit what happened). The minimum viable version is two lines.*

- Before writing or editing: read the files you're about to change; check for a HANDOFF.md
- At session end: offer `/land` (the close-out chain) when the session is winding down. Don't wait to be asked.

## Toolshelf (tools not installed yet, and when to offer them)

> *Job: make the "add it later" tools actually come back. The first copy of this kit told its reader when each later tool would help, then left that knowledge in his head. His Claude never offered any of them, and he never went back. A line here is read every session, so Claude can notice the moment and offer the tool. Each line: the moment, the tool, where its file is. When a tool gets installed, move its line out of this section (or delete it). The seed fills this in during the shopping trip; the two-week check-in reviews it.*

- **[Moment: e.g. "facing a decision with real tradeoffs"]** → offer `/decide` (kit: `<full path to the kit>/reference/later/commands/decide.md`)
- **[Moment: "about to build something with real scope"]** → offer `/prd`
- **[Moment: "about to show work to other people"]** → offer `/squint`
- **[Moment: "the first repo with a remote, or the first deploy"]** → offer the push gate (kit: `<full path to the kit>/reference/hooks/confirm-push.py`)
- **[Moment: "starting a new project"]** → offer the new-project checklist (kit: `<full path to the kit>/reference/new-project-checklist.md`)
- [One line per shelf tool the person skipped. Offer once per moment, never nag; if they decline twice, ask whether to drop the line.]

## Collaboration rules

> *Job: the encoded corrections. Each rule is written in contract form (trigger + action + scope, a few lines), with the reasoning kept elsewhere and linked. This section grows over months through the capture-freely-promote-selectively loop; it starts nearly empty. Do not pre-populate it with borrowed rules. A rule that didn't come from your own friction won't mean anything to you when it fires.*

> excerpt (hers, as a shape example; note the form: when-this / do-this / not-that):
> "**Debugging: Evidence Before Hypotheses.** When an API call fails, a deploy breaks, or behavior is unexpected, ask for the actual error message, network output, or config before proposing a fix. Don't guess from a description alone. Exception: obvious issues (typos, syntax errors, missing imports) where the cause is visible."

- [Empty at first. Your first entry arrives the first time a correction recurs.]

> *Where a rule's reasoning lives.* Keep each rule here short: trigger, action, scope. The *why* (the incident, what was tried) belongs somewhere Claude can read on demand, so it can recalibrate the rule instead of just obeying it. Auto memory won't do for a global rule, because it's per project: a reason saved while working in one project is invisible from every other. Give global reasoning its own folder (for example `~/.claude/memory/`, one file per rule) and link each rule to its file.
>
> *Links must point at real files.* If you use a link style like `[[rule-name]]` to point at those files, Claude will sometimes invent a plausible-looking link to a file that doesn't exist. It looks like depth and delivers nothing. Add a line here: "before writing a link to a file, check the file exists; if it doesn't yet, say so in the same sentence."

## Check-in

> *Job: an expiry date, so the harness gets pruned instead of only growing.*

- [Date two weeks after setup]: review what got installed. Has a fresh session surprised you with something from a past one yet? Did a weekly friction read run, and did you read it? Does every guard still block its test command? Go through the Toolshelf: did any moment come up? Remove anything that hasn't earned its keep. Then rebuild the shelf page (everything installed, and what's still on the Toolshelf) so you can see what you have.
