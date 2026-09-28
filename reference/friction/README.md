# friction/ — the friction loop, both halves

**Added to the kit 2026-09-12.** The first version of this kit shipped the *capture* half of this loop (the journal command logs friction at session close) without the *synthesis* half (anything that reads the log). The result, as the first person this setup was handed to reported it: the log got written to and never read. This folder is the missing half, plus the method that connects the two.

## What the loop is, in plain words

Courtney's own public description of it (Reddit, August 2026), which is the shortest true version:

> When I close out a session, Claude reviews for friction of every kind, not just mistakes: stuff I had to correct, work called done without proof, system stuff that cost time, or stuff it asked me about that it should've already known. It shows me what it found, and appends to a shared log once I sign off.
>
> Then once a week, a separate pass reads the log for what keeps recurring so we know what to fix. I lean toward making it mechanical where I can: if a script can catch it, it becomes a hook that blocks the move outright. For example, it was sometimes pushing without an explicit go-ahead, so now a hook won't let a push through without my sign-off, and that category basically went to zero.

That is the whole shape. Four parts, in the order data flows:

1. **Prompts at session close** (`WATCH-FOR.md`). A short tiered list the journal ritual runs. Any "yes" becomes one concrete line. "Clean session, nothing to log" is a complete answer.
2. **The log** (`FRICTION-LOG.md`, which you create; format below). Append-only, one line per item, tagged with where the fix lives, what kind of friction it was, and how strong the evidence is.
3. **The reader** (`friction-scan.js`). A zero-dependency script that counts what recurred since the last synthesis, grouped at the grain the synthesis reports at. It counts; it does not conclude.
4. **The weekly synthesis** (`friction-scan-SKILL.md`; output shape in `example-weekly-synthesis.md`). A short written report: the main pattern, the repeated burdens with evidence strength, **one** smallest improvement, what not to automate, and what the prompts should watch for next. It lands as a dated file in the friction folder, where a human reads it.

Then the fix goes where the loop says it goes: a hook if a script can catch it, a rule if it needs judgment, a prompt-list edit if the log is missing a kind of friction. And the prompts change what gets noticed next week. That feedback edge is the point; without it this is a diary.

## Why the reader and the synthesis are two things

Counting is mechanical and should be a script, so that a synthesis never starts with a reading chore (that chore is what stalled the loop here for two months). Concluding is not mechanical: how you bucket a hundred entries determines what you conclude, so the synthesis needs a declared method and a human who can say "that's not the root cause." The reader's own header explains the three things it refuses to guess. Read it before adapting it; the refusals are the design.

## The lesson this folder exists for: delivery is part of the loop

Two failures from Courtney's system, both worth more than any rule here:

- **A human-triggered weekly ritual with no owner stalled.** For two months the log grew (about eight entries a day at peak) and no synthesis ran. The fix was not "try harder"; it was giving the run an owner that isn't a person remembering. See `SCHEDULE.md`.
- **A synthesis that ran but wrote to a file nobody opened was as good as not running.** When an automation did run weekly, its output went to a private memory file. Seven correct diagnoses in a row, each recommending the same fix, and nothing changed, because no human or future session ever read them. The synthesis must land in the folder the humans and the sessions read, as a new dated file.

So the install is not done when the reader runs. It is done when a synthesis file has been read by a person and one small fix has been made because of it.

## Log format (copy this header into your `FRICTION-LOG.md`)

One line per entry:

```
YYYY-MM-DD · [surface] · [source] · [type] · [evidence] · description · [proposed fix?] · [author]
```

- **surface**: where it happened. A project name, or `claude-code`, or another agent's name.
- **source**: where the fix lives. This is the actionable field.
  - `agent`: agent behavior (a gate skipped, a claim unchecked) → rule or mechanism
  - `tool`: harness or tooling (hook, sandbox, MCP, environment) → config or hook fix
  - `workflow`: process, handoff, division of labor → process change
  - `setup`: missing context or framing up front → better elicitation
- **type**: what kind of friction. Thirteen values in five groups, below. `source` says where the fix lives; `type` says what the fix has to be.
- **evidence**: `strong` (observed: diff, terminal, render, explicit correction) · `medium` (pattern, repeated phrasing) · `weak` (inferred, felt, blind-spot guess).
- **description**: one line, concrete. What happened, not a category.
- **proposed fix**: optional, only if obvious.
- **author**: which agent wrote the line.

The separator is a middle dot with spaces (` · `). The reader parses on it, so keep it exact.

### Type vocabulary

Groups are the grain the weekly synthesis reports its headline at; types say which fix each needs.

**Acting before the gate**: `unapproved` (shipped, wrote, pushed, or spent without a yes) · `premature-build` (built before the goal or direction was settled) · `past-bail` (ground a stuck path past the 2-3 attempt bail point).

**Not checking**: `unchecked-claim` (stated something as fact without checking) · `self-accepted` (declared own work done or good without critiquing it) · `prior-work-missed` (the answer already existed and wasn't reached for).

**The machine**: `cant-verify` (the environment couldn't show the result, so the work couldn't be checked) · `environment` (a tool or platform failed, was slow, or fought back) · `cost` (tokens or money out of proportion to the answer).

**Durable state wrong**: `silently-broken` (a doc, rule, hook, pointer, or index is wrong or not firing, and throws no error) · `collision` (parallel sessions or stale shared state overwrote or contradicted each other).

**Load landed on the operator**: `manual-load` (the human relayed, sorted, or hand-did work the system could hold) · `illegible` (output the human couldn't absorb without a redo round).

*Calibration note:* this vocabulary was derived from Courtney's first 124 entries, by the rule that a type earns its label only if its entries share a fix. Start with it so the reader works on day one. After your own log passes about a hundred entries, re-derive from your entries; the groups that dominate your log may not be the ones that dominate hers. When you change the vocabulary, don't silently retag old entries; leave them as written and keep a map from old labels to new in the log header. The reader's legacy section shows what that looks like.

## Install order

1. Create `FRICTION-LOG.md` in a folder your journal command can reach. Paste the format section above as its header. Put `WATCH-FOR.md` beside it.
2. Point the journal command's friction-capture section at those two files (the kit's `reference/commands/journal.md` has that section; only the paths change).
3. Copy `friction-scan.js` somewhere runnable and set `FRICTION_LOG` in the environment, or run it from the friction folder. Run it once against the empty log to confirm it parses.
4. Install the skill (`friction-scan-SKILL.md` → `~/.claude/skills/friction-scan/SKILL.md`), paths changed, and delete the italic kit note under the frontmatter so it doesn't load every time the skill fires.
5. Give the weekly run an owner per `SCHEDULE.md`. This step is the one the earlier copy skipped.
6. First synthesis after two weeks or twenty entries, whichever comes first. Read it. Make the one fix. Only then call the loop installed.

## What is Courtney-specific in this folder

- The vocabulary (see the calibration note above).
- The core-tier prompts in `WATCH-FOR.md` are weighted toward *her Claude's* recurring friction. Yours will tune from your own first two syntheses.
- The example synthesis is about her projects. Study the shape, not the content.
- The reader's legacy-vocabulary section is the history of her log's one vocabulary change. Harmless on a fresh log; delete it if it bothers you.
- "Codex" appears in a few places because her setup runs a second agent that also writes to the log and owns the weekly run. `CODEX.md` in the kit root covers that. One agent is fine; the loop doesn't need two.

## Files

- `README.md`: this file, the method.
- `SCHEDULE.md`: who runs the weekly synthesis and when, with the kill condition.
- `WATCH-FOR.md`: the session-close prompts, adapted from Courtney's live list.
- `friction-scan.js`: the reader. Zero dependencies, read-only.
- `friction-scan-SKILL.md`: the synthesis skill.
- `example-weekly-synthesis.md`: one real weekly synthesis, verbatim, so the output shape is visible.
