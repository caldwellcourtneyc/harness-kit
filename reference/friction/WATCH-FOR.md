# Watch-For List

*Kit note (2026-09-12): adapted from Courtney's live list. The structure (tiers, the relevance gate, the honesty rules) is the transferable part. The core-tier prompts are weighted toward what her Claude kept doing (in her log, prompt 3 has been the most recurrent class in every weekly scan since July 2026, ahead of acting before the gate, prompts 1, 2 and 4); keep them as a starting core and let your first two weekly syntheses promote, revise, or drop them. Her second-agent calibration tier is left out; `CODEX.md` covers adding one.*

The prompts the in-session agent runs at session close (via the journal ritual) to catch friction while it's still visible. Qualifying items go to `FRICTION-LOG.md`.

**This is a living list.** The weekly synthesis tunes it: what recurs moves into the core tier; what stops appearing after you start watching for it gets dropped. Editing this one file changes what the agent notices; that's the loop. Don't let it ossify into a static checklist.

**Why tiered:** running every prompt at equal weight every session breeds checklist fatigue and the prompts stop catching. The core tier gets real attention; the sweep is a fast pass.

---

## Core tier (real attention)

1. Did I **ship / commit / fire** anything before showing the operator?
2. Did I **build or polish before confirming the goal or form**? Did they have to ask what I was trying to do?
3. Did I **accept my own output, or assert something as fact,** without actually checking it? A render, read, or result I didn't critique (`self-accepted`), or a claim about current state, a capability, a number, or what exists, taken from memory or a handy source instead of the authoritative one (`unchecked-claim`)?
4. Did I **keep pushing a stuck path past 2-3 attempts** before escalating, switching methods, or asking?

*Any yes → write a one-line concrete example. That example IS the log entry.*

## Sweep tier (fast pass, any source)

5. Did the system make the operator **relay, sort, or re-supply** context it could have held?
6. Did useful knowledge **stay trapped in chat** that should have a durable home?
7. Did a **tool, hook, sandbox, or manual step** cost real time?
8. Did the **setup / handoff / division of labor** create drag: missing context up front, unclear ownership, wrong checkpoint?
9. Did I hit a doc, rule, hook, pointer, or index that was **wrong, stale, or silently not firing**? No error, just not true.

## Blind-spot proxy (source-neutral)

10. Where did the session carry **drag I can't fully explain**, and best guess at the cause: me, the tools, the process, or how it was set up? *(tag `weak`; a seed for the scan, not a finding)*

---

## Filters and honesty

- **Relevance gate:** log an item only if it **recurred, cost real time, or would change a workflow.** Not every minor annoyance.
- **Tag each logged item:** source (`agent` / `tool` / `workflow` / `setup`) + type + evidence (`strong` / `medium` / `weak`). Type is the clustering axis the weekly scan reads; pick it from the vocabulary in the log's header, not from memory.
- **"Clean session, nothing to log" is a complete answer.** Never pad to fill the list.
- **Source-neutral:** friction is system load, not agent-blame. A clean log has plenty of non-`agent` entries.
