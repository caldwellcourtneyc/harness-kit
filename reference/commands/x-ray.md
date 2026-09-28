Mutual blind-spot scan before committing to a path — surfaces what either party is assuming, missing, or hasn't checked. Fire unprompted at load-bearing decisions (vendor, schema, default behavior, security posture), before acting on an unchecked assumption, after round one of a generative or design collaboration, before launching a workflow or a fan-out of 4+ subagents, after twice-in-a-row pushback, or when the user asks "what else should we consider/ask/watch out for."

## What This Is

A structured pause to make the implicit explicit — for both
the user and Claude. The point is the pause AND the surfacing.

## When to Invoke

**The user invokes when:**
- Sensing a commitment-worthy fork
- About to greenlight a path that feels right but unexplored
- Stuck, going in circles, or pushing back without converging
- Anytime they'd otherwise type "what else should we be considering /
  asking / watching out for"

**Claude invokes unprompted when:**
- Load-bearing decision on the table (vendor, schema, default
  behavior, security posture)
- About to act on an unchecked assumption
- The user has pushed back twice in a row on a related point —
  frame is likely the issue, not details
- After round one of any generative or design collaboration,
  before polishing a direction further — fire the frame check on
  session position, not on how good the rec feels (the reliable
  trigger)
- Before launching a workflow or any fan-out of 4+ subagents. The
  spend is large and the design is frozen once agents are running.
  On 2026-09-23 a 24-agent workflow launched without one and missed
  a research brief already on disk that would have changed its
  design.

## When NOT to Fire

- Small contained changes (typo, single-line refactor)
- Mechanical execution of a decision already made
- Open-ended exploration — kills it. (The round-one
  generative-collaboration trigger is for committed design or
  decision work that's heading somewhere — NOT for open-ended
  thinking. When unsure which it is, don't fire.)
- Inside an active /decide flow — that's doing this work already

## Protocol

Seven moves. Brief beats thorough. Skip any move with nothing real
to say — manufactured filler degrades signal worse than under-firing.
Empty is a valid output. "Nothing distinctive here" beats fabricated
content.

### 1. Dodge

Most uncomfortable question you're NOT asking about this work. This
isn't an angle — it's the posture shift that makes the rest honest.
Name it before anything else.

### 2. Frame check

One line: is this the right work *right now*? If "no," surface that
and stop — the rest doesn't matter if the frame is wrong.

### 3. Four angles

- **Ask** — questions worth asking that haven't been. Target
  assumptions, direction, constraints. Include unknowns neither
  party has verified.
- **Consider** — alternatives, blind spots, unchecked assumptions
  on both sides. What's not on the table that maybe should be?
- **Watch out for** — risks, fragile assumptions, what could bite.
  Specific to this work ("this coupling between X and Y will probably
  bite when Z"), not generic.
- **If wrong** — what would we see if this is wrong? Name the
  observable sign (a number that doesn't move, a user who doesn't
  come back, an error that shows up at step 3), early enough to act
  on. If nothing would show it, say so; that is itself a finding.

One or two lines per angle.

### 4. Open kicker (optional)

What brilliant idea haven't we thought of? Backstop for anything the
four angles missed. Skip if the angles covered it.

### 5. Check the most fragile assumption

Pick the one assumption the plan most depends on and check it with a
real lookup: read the file, grep the code, count the rows, fetch the
page, query the store. Report what came back. Naming it is not
checking it. If no lookup can reach it in this session, say what
would check it and who can.

### 6. Adjustment

End with either `No action change` or `Recommended adjustment: ...` —
the scan has to land on something actionable, not trail off.

### 7. Log it

Append one line to `~/.claude/refs/x-ray-log.md` (create it if
missing):

`YYYY-MM-DD | <project> | <what was being decided, a few words> | changed the plan: yes/no | fragile assumption: held/broke/unchecked`

"Changed the plan" is yes when the scan ended in a recommended
adjustment that was taken, or the lookup in step 5 broke the
assumption. If the user's answer comes later in the session, update
the line then. The point is to be able to judge later whether the scan
changes outcomes often enough to keep firing it unprompted.

## What This Is Not

- Not /decide (that's for forks with defined paths and deeper
  exploration)
- Not /surface (that's for unshared insights at session edges)
- Not a replacement for any checkpoint questions in your
  CLAUDE.md — those still apply as flavor within each angle
