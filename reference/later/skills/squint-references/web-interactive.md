# Web and interactive artifact review

Use this adapter after reading the core workflow in `../SKILL.md`.

## Inspect the rendered artifact

Review the real rendered experience, not source code alone. Start with the
primary encounter size, then inspect desktop and approximately 390px when both
are relevant. Use rendered captures for composition and the live page for
behavior.

**Browser tools can fail silently.** Some report success and do nothing (a
resize that doesn't resize, typed input that never lands, a screenshot that
times out), so a naive pass believes it verified when it didn't. When a check
matters, confirm it a second way: read the page's text or accessibility tree
for structure and copy; capture at explicit viewport widths with a headless
browser (for example Playwright) for layout; drive stateful controls through
their real handlers rather than simulated clicks. When a tool cannot interact
with a control, treat that as a candidate real defect in the artifact until
disproven, not tool flakiness. Both look identical from the tool's side, and
assuming flakiness has shipped a real dead-input bug before.

Before reading supporting material, record the cold-reader experience:

- What is this within five seconds?
- Who appears to be speaking, and to whom?
- What is the central claim, task, or invitation?
- What should the reader understand, feel, believe, or do next?
- Where does the page assume context it has not supplied?
- What becomes repetitive, unclear, inert, or easy to abandon?

## Review meaning and composition

Check whether hierarchy and sequencing make the intended argument legible.
Look for dead space, stranded text measures, timid secondary devices, generic
card systems, decorative evidence, and elements that repeat rather than advance
the story. Treat screenshots and historical captures as evidence only when they
prove the accompanying claim.

Consult the project's design guidance, settled decisions, and the user's taste
file (if they keep one) during the informed pass. Do not use them to
rationalize a cold-reader failure. Name whether a concern comes from purpose,
usability, design craft, taste, or implementation.

## Review behavior

Exercise every load-bearing interaction with pointer, touch-equivalent behavior,
and keyboard when applicable. Check:

- Discoverability and a clear affordance.
- Useful accessible names and semantic roles.
- Visible keyboard focus and logical focus order.
- The full state change, including replay or reset when promised.
- Interaction pacing that helps the reader understand what changed.
- No hover-only information or pointer-only completion path.
- Deliberate mobile behavior without horizontal overflow or accidental stacking.
- Reduced-motion behavior through browser emulation when motion exists.

Inspect loading, empty, error, and recovery states only when the artifact can
actually encounter them. Check performance when it materially affects the
first impression or interaction.

## Separate critique from QA

A working interaction can still be conceptually weak. A strong composition can
still be inaccessible. Diagnose each issue at the correct layer and do not let
functional verification stand in for design critique.

For a rough visual prototype, stop after the direction is judgeable unless the
user asks for more. For a production candidate, include responsive, keyboard,
focus, reduced-motion, link, copy, and interaction verification before calling
it ready.
