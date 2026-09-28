# Memory index (example project)

> **Kit note (not part of the index):** this is a real per-project `MEMORY.md` from Courtney's
> harness, cut down to the entries about how Claude should work. Entries about her life, her
> business, and her private tools were removed, and "she" became "the user." The memory files
> the lines point to are not included.
>
> **How the format works.** One line per stored fact: a link to the memory file, then a short
> hook phrase that tells a future session when to open the full file. Claude Code loads this
> index automatically at the start of every session. The files behind it load only on demand,
> when a hook phrase matches the work at hand. That is why each hook says *when* the fact
> matters, not only *what* it is.

- [Match scale: build product, not component](match-scale-build-product-not-component.md) — visual samples must show the product slice, not a lone component; never dress a capability gap (no image-gen) as an aesthetic principle
- [Route reference lookups to agents](route-reference-lookups-to-agents.md) — big reference loads (claude-api skill, doc dumps) go in a subagent's context, not the main loop's, unless the main loop must apply them
- [Watch for expressed confusion](watch-for-expressed-confusion.md) — the user's spontaneous "I don't know what I'm looking at" moments beat structured analysis; pull that thread immediately, never interview for it
- [Overnight dispatch protocol](overnight-dispatch-protocol.md) — unattended overnight builds: prompt-as-file + the user's QA rounds + scoped bypass + setting the table for morning
- [Caveats must propagate into instructions](caveats-must-propagate-into-instructions.md) — a stated limit on what you can verify has to survive into the steps that follow it, or become a test the user can run
- [Mechanizing a gate migrates friction](mechanizing-a-gate-migrates-friction.md) — a hook that fixes the detectable face of a recurring miss pushes it to the judgment face; name that face and route it to the scan, don't call the behavior solved
- [Skills beat standing agents for now](skills-beat-standing-agents-for-now.md) — solo operator: prefer skills (no state to rot) over persistent named agents; a "for now" not "never" — agents earn their place at scale
- [Verify motion by driving it](verify-motion-by-driving-it.md) — static screenshots don't verify motion/interaction; capture multi-frame + drive scroll/hover/click, or dispatch a real event and read state; Playwright's synthetic mouse won't fire pointer events in cursor:none areas on this box
- [Show machinery when it exists](show-machinery-when-it-exists.md) — for a systems viz, animate the real mechanism (components + flow), not an abstract concept with a pulse on it; NOT absolute — metaphor is right when the concept itself is the subject
- [Originality is expression, not idea](originality-is-expression-not-idea.md) — shareable content must be our own representation, not a redraw of someone's diagram however improved; ideas aren't ownable, expressions are; keep derivative studies internal + marked
- [Critique, not verify, on visual builds](feedback-critique-not-verify-on-visual-builds.md) — before calling visual work done, run the design-critique pass (would a designer sign this), not just render/link verification; open bold when the brief says bold; "look at each page" is the tell I've been verifying not critiquing
- [Initiation is the scarce resource](initiation-is-the-scarce-resource.md) — harness principle the user endorsed 2026-09-02: the system carries the activation energy; triggers live on the system's side, never on the user remembering
- [Interview me more](feedback-interview-me-more.md) — use existing context first, then ask when the user's thinking is still latent; capture before interpreting
- [Agent-shaped vs workflow-shaped](agent-shaped-vs-workflow-shaped.md) — the test for reaching for an agent: do the steps depend on what you discover along the way? Most "agent" work is workflow-shaped in costume; per-task judgment, not a verdict
- [Options in chat, selection in doc](options-in-chat-selection-in-doc.md) — react-to menus go in the message; the durable doc records only what the user picked, never the rejected variants
- [User-voice docs: first person, no meta](user-voice-docs-first-person-no-meta.md) — scripts, talking points, public blurbs are "I" throughout and carry zero correction notes or decision stamps; questions go in chat
- [Session transcripts filed by cwd](session-transcripts-filed-by-cwd.md) — local .jsonl transcripts sit under the slug of the folder the session was opened in, not the project it built; grep all slugs to find a build session
- [Journal is read by Claude, not the user](journal-read-by-claude-not-user.md) — the user doesn't read entries themselves; write for retrieval (searchable TL;DR, pointers, the user's exact words)
