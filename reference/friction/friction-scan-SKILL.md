---
name: friction-scan
description: Use when the operator asks to inspect a session, project, agent workflow, or collaboration pattern for hidden friction, courier burden, overproduction, missing verification, blessing gaps, or opportunities to reduce manual load. Especially useful after sessions, before changing durable workflow infrastructure, for the weekly workflow review, or when deciding what to automate next. Distinct from x-ray: x-ray is for pre-decision blind spots; friction-scan is for post-session or post-week workflow burden patterns.
---

*Kit note (2026-09-12): adapted from Courtney's live skill. "The operator" stands where her name does; path placeholders are marked `<friction folder>`. One addition over her live version: the weekly scan starts by running the reader script, so the headline grain comes from counts rather than from a reading pass.*

# Friction Scan

Run a focused scan of a real workflow to find where the collaboration system made the operator carry load it could have absorbed.

This is not a productivity audit, status report, vibe check, or generic retrospective. Identify specific friction from evidence and propose the smallest useful improvement.

## Use For

- Post-session workflow review.
- Weekly workflow review.
- Finding repeated courier, sorter, or context burden.
- Deciding whether a step should become a skill, script, automation, hook, rule, or visible control.
- Checking whether an agent workflow produced more overhead than relief.

Use `x-ray` instead before a load-bearing decision. Use `capture` when the primary job is routing important material to durable homes.

## Sources

Use the most relevant available evidence. Ordinary sessions of any agent are first-class evidence, not only the ones that felt bad.

For the weekly scan:

1. Run the reader first: `node friction-scan.js` (set `FRICTION_LOG` if the log isn't in the working directory). It reports entries since the last synthesis, grouped at the grain the headline should use, and says what it could not classify. Its counts are self-reported by the agents that logged them; the reader says so on every run and so should you.
2. Then read `<friction folder>/FRICTION-LOG.md` for the window. The log is the canonical record of qualifying close-out observations. Use journals and the evidence below to interpret or verify its entries.
3. Sample two or three real session records from the same window and compare them against the log. Qualifying friction the sessions show and the log missed is a finding (the capture-quality check).

Other evidence, any scan:

- Current chat or session context.
- Project files such as `HANDOFF.md`, `CLAUDE.md`, specs, or build notes.
- Journal search when prior workflow history matters.
- Git diff, terminal output, browser evidence, rendered UI, or test output when relevant.

Do not invent friction from theory. Prefer observed moments.

## Scan For

- **Courier Burden:** the operator had to copy, relay, summarize, re-explain, or move context between tools, agents, or files.
- **Sorter Burden:** the operator had to sift too much output, reconcile agent disagreement, or decide what mattered from a pile.
- **Context Supply:** the operator manually provided context the system could have retrieved, remembered, or prompted for.
- **Blessing Gap:** a decision, convention, artifact, or project truth moved forward without a clear approval moment.
- **Verification Gap:** work was declared done without enough evidence: tests, render, browser check, diff review, or reread.
- **Overproduction:** agents generated more than the operator could usefully absorb, react to, or prune.
- **Tool Mismatch:** the workflow asked the operator to use terminal commands, hidden files, keyboard shortcuts, or manual steps where a visible control or script would fit better.
- **Durability Drift:** useful knowledge stayed trapped in chat, or temporary notes started acting like canon.
- **Automation Candidate:** a repeated, low-judgment step could become a skill, script, hook, rule, or automation.
- **Human Judgment Boundary:** something should stay operator-controlled because it involves taste, approval, business meaning, or product direction.

## Evidence Strength

Label evidence honestly:

- **Strong:** git diff, terminal output, browser or render proof, saved docs, an explicit correction from the operator.
- **Medium:** journal summaries, repeated phrasing, session close-outs, a consistent pattern across sessions.
- **Weak:** inferred attention load, unobserved manual steps, or vibe from how the week felt.

If the evidence is weak, say what would need to be observed before changing the workflow.

## Output Shape

For a session scan:

```md
## Friction Scan

**Main read:** [1-3 sentence diagnosis.]

**Top friction points**
1. [Observed friction + evidence strength.]
2. [Observed friction + evidence strength.]
3. [Observed friction + evidence strength.]

**Best next improvement**
[One smallest useful change.]

**Do not automate**
[Judgment, taste, approval, or meaning boundary.]

**Possible durable home**
[Skill, CLAUDE.md, automation, hook/rule, journal, decision record, or none.]
```

For a weekly scan, write to a new dated file `friction-scan-<start>_to_<end>-<agent>.md` in the friction folder:

```md
## Weekly Friction Scan

**Main pattern this week:** [One diagnosis.]

**Repeated burdens**
1. [Pattern + evidence strength.]
2. [Pattern + evidence strength.]
3. [Pattern + evidence strength.]

**Best system improvement**
[One small change to try next week.]

**Do not automate**
[Judgment, taste, approval, or meaning boundary.]

**Needs better signal**
[Important but not well tracked.]

**Capture-quality check**
[Qualifying friction the sampled sessions showed that the log missed, or "log and sessions agree".]

**Suggested durable update**
[Skill, CLAUDE.md, automation, journal, decision record, or none.]

**Watch-for calibration**
[Promote, revise, retain, or drop a watch-for item only when the log supports it.]
```

## Rules

- Lead with the highest-leverage friction, not a full transcript summary.
- Separate observed evidence from interpretation.
- Recommend one smallest useful improvement, not a menu of possible systems.
- Do not propose dashboards, broad systems, or automation unless the workflow has earned them.
- Do not turn the operator's taste, priority, or approval role into an agent decision.
- If three or more friction points point to the same root cause, name the root cause.
- If a proposed fix could create new ceremony, call that out.
- Routine capture happens in the journal close-out. Do not require a separate per-session scan unless the operator asks for an immediate diagnostic.
- For a weekly scan, report whether provisional watch-for items gained enough evidence to promote, revise, or remove. Do not treat a candidate as a fixed trait.
- The weekly scan modifies nothing but its own new file. Changes to the log, the watch-for list, rules, or skills are proposed in the report and made by a human in a session.

## Good Recommendations

Good recommendations are concrete:

- Add a hook that blocks a push without explicit approval.
- Add a visible control instead of requiring a file to be edited by hand.
- Make harvest candidates appear only at close-out.
- Add an automation that checks stale handoff docs weekly.
- Add a CLAUDE.md rule requiring browser verification after visual UI changes.

Weak recommendations are vague:

- Improve communication.
- Use better context.
- Automate more.
- Be clearer.

## Close

End by naming whether the workflow needs:

- **No change:** friction was one-off or acceptable.
- **Prompt change:** next session instruction is enough.
- **Skill:** repeated judgment workflow.
- **Script/control:** repeated mechanical step.
- **Automation:** repeated scheduled check.
- **Durable doc update:** project convention or decision changed.
