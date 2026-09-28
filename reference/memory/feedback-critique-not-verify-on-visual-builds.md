---
name: feedback-critique-not-verify-on-visual-builds
description: "On visual builds, run a design critique pass (would a designer sign this), not just render/link verification, before calling it done; and open bold when the brief says bold"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: b79a8117-a17d-46b7-ac4b-a3d9bd90fc76
  modified: 2026-08-22T19:00:05.785Z
---

On a site rebuild (2026-08-22), two related misses recurred across rounds:

1. **Verify vs critique.** I kept presenting builds as done on the strength of
   *verification* (does it render, do the links work, no overflow) when the actual bar
   is *critique* (would a strong designer sign this). The user had to say "look at each
   page" twice before I switched modes. Rendering-and-confirming is the failure mode;
   the render is for finding what's weakest, not for confirming it's fine.

2. **Opened safe despite a start-bold brief.** The site's art was loud and begging for a
   committed direction, and I still shipped polite white-SaaS chrome for two full rounds.
   It took "this is not good enough" to reach the committed register that was obviously
   right. The start-bold rule did not fire on its own.

**Why:** both are the same root as [[pattern_verification_fails_toward_green]]
(self-built checks break in the reassuring direction) applied to design: I default to the
check that passes (it works) over the check that hurts (it's generic / underdesigned).
Encoded because it cost real rounds and the user had to push.

**How to apply:** on any visual build, before calling it done, run the critique pass
explicitly (a render-and-critique pass, or the /squint two-pass) and ask "what would a
strong designer change here" - not "does it work." Open at the bold/committed end and dial
back when the brief says bold. When the user says "LOOK at this," that is the tell that
I've been verifying when they wanted critique - switch, don't re-verify.

Related: `~/.claude/rules/first-screenful.md` · `~/.claude/rules/type-scale.md` (both
encoded this session for the specific defects the critique pass kept missing).
