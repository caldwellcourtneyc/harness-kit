*Kit note: project and product names below were generalized to their roles, "the operator" stands where Courtney's name was, and one personal item was removed from the text (the counts still reflect the full log).*

*Kit note (2026-09-12): one real weekly synthesis from Courtney's system, written by the scheduled automation described in `SCHEDULE.md`. Study the shape: one pattern, burdens with evidence strength, one smallest fix, a do-not-automate line, a capture-quality check against real sessions, and a watch-for calibration. Note that the closing line names which kind of fix the week needs, and that the report changed no files but itself.*

# Weekly Friction Scan — 2026-09-08 to 2026-09-10

**Run:** 2026-09-11 09:01 CDT  
**Sources:** `FRICTION-LOG.md`, `WATCH-FOR.md`, daily session records for September 8, 9, and 10, plus one accessible Codex task from an app project as a spot-check against the September 10 record.

## Main pattern this week

The collaboration system repeatedly judged from a convenient but non-authoritative vantage point: Claude's own read instead of the writing project's review desk, an older asset set instead of the current one, and an expert review instead of a cold user's first encounter. The surface forms differ, but the load transfer is the same: the operator or a later review had to reveal that the evidence did not match the claim or audience.

The log contains 14 entries for the window: 7 strong, 4 medium, and 3 weak. Tool/environment friction is the largest type by count (6), but most of it is medium or weak and locally recoverable. The higher-leverage cluster is evidence/judge mismatch: 3 `unchecked-claim` entries and 2 `self-accepted` entries, all but one strong.

## Repeated burdens

1. **The agent's own read or nearby evidence stood in for the real judge — strong.** An episode script in a writing project was called close to script-ready until the operator's line-by-line desk review found that it did not flow. The squint review of an app project called the interaction clear, but two adults failed the first screen within thirty seconds. These are distinct sessions with the same claim-to-judge mismatch.

2. **Current or exact state was characterized from stale or incomplete evidence — strong.** The September 8 readout called a prototype's v0.8 live and miscounted messages without a supporting tool result; on September 9, an older portrait generation was described as current. This continues the prior weeks' pattern of plausible representation becoming a current-state claim.

3. **Windows/browser/file-sync mechanics created repeated detours, but the burden was uneven — medium overall.** Six environment entries include truncated browser extraction, over-broad file-sync guards, quoting/heredoc failures, and an unscoped recursive search. Most were recoverable agent-side annoyances. The material user-facing case was the writing project's review desk: the operator repeatedly chose save locations and ended up with ambiguous filenames; the filename and remembered-handle fix shipped, though the remembered-handle path still needs a real second-save confirmation.

## Best system improvement

Trial one selective **judge-and-source line** before consequential readiness, current-state, or recipient-facing claims:

> `Judge/source: [who or what can actually validate this]; observed: [the evidence checked].`

Examples from this window would name the review desk, a cold first-time user, or the current image folder. Keep it selective; applying it to routine statements would create ceremony without reducing meaningful load.

## Do not automate

Do not automate the operator's taste, script approval, or the interpretation of a first-time user's reaction. Automate or require access to the right evidence surface; leave the judgment itself with the intended human reviewer.

## Needs better signal

The tool/environment count is high, but three of six items are weak and several are one-step recoveries. Do not promote quoting, grep, or guard-specific fixes into broader workflow rules unless they recur with material cost. The remembered-save-handle fix also needs a real second-save observation before it is treated as verified.

Codex-specific calibration remains insufficient. The accessible app-project task confirms substantive Codex implementation work in the period, but the captured failure concerned Claude's expert squint review; the log still provides no clean basis for promoting a Codex candidate into a stable trait.

## Capture-quality check

The sampled records support the September 8 and September 10 log entries closely. The September 9 news-scan session surfaced qualifying friction that the log missed: `/skill-doctor` was assigned capabilities from a one-line changelog rather than its documentation, and the operator's practical question exposed the error. The same session says this was the third consecutive news scan with an adjacent-evidence claim, and self-review also caught a fabricated version number and a misclassified result. This is medium evidence from a saved session record, but it clearly meets the relevance gate because it recurred and would change the workflow. It belongs to the same `unchecked-claim` family as the week's logged items.

## Watch-for calibration

- **Retain Claude core item 3 as the highest-value prompt.** It caught the dominant strong cluster, but its operational test should emphasize whether the evidence matches the actual judge or recipient, not merely whether something was checked.
- **Retain sweep item 7.** The environment/tool entries are numerous, but do not expand it into tool-specific prompts yet.
- **Retain sweep item 9.** The missed news-scan case again involved treating an adjacent source as authoritative.
- **Keep the Codex calibration tier provisional.** There is still not enough direct, agent-attributed Codex friction evidence to promote, revise, or drop a candidate.

## Suggested durable update

**Prompt change, not a new skill or automation.** If the operator chooses to change the watch list, narrowly revise Claude core item 3 to ask whether the checked evidence came from the real judge, audience, recipient-held artifact, or authoritative current-state source. This report does not modify `WATCH-FOR.md`.

## Close

**Workflow need: Prompt change.** The repeated problem is not absence of checking; it is checking from the wrong vantage point.
