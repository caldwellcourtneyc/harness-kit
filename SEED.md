# SEED: the bootstrap protocol

**You are the user's Claude, reading this inside the Harness Kit.** Your job is not to install Courtney's harness. It is to grow your user's, using this kit's guide and reference files as worked examples of what a mature harness looks like, and your user's answers as the raw material for theirs.

Read `guide/architecture.md` and `guide/retrieval.md` before Phase 1. Read the other guide docs as their phases arrive.

## Ground rules

- **Additive only.** Never overwrite or delete anything in the user's existing setup. If something of theirs conflicts with something you're building, show them both and let them choose.
- **Their versions, not copies.** Reference files marked as Courtney's calibration are examples of the *kind* of thing that goes in a slot. The content must come from your user. Copying her calibrations would make you behave like you're working for her.
- **Show before you write.** Every file you create or change in `~/.claude`, show it first and get a yes. That includes CLAUDE.md lines, memory entries, skills, and hooks.
- **Small and running beats complete and abandoned.** The failure this kit exists to prevent is overwhelm: the first time this setup was handed to someone, only the journal survived. Bias every phase toward the minimum that works, with a clear trigger for adding more later.
- **Pace by their energy, not by the protocol.** Each phase is a natural session boundary. Ending early is fine; write down where you stopped (in their CLAUDE.md check-in line or a note) so the next session resumes.

## Phase 0: Inventory (look before asking)

Before interviewing, look at what they already have: `~/.claude/CLAUDE.md` and any project CLAUDE.md files, `~/.claude/rules/`, skills and commands, hooks in `~/.claude/settings.json`, auto memory (`~/.claude/projects/<project>/memory/`; check whether it's on and what's already in `MEMORY.md`), any journal or notes folder and how it's used, and MCP servers. Report what you find in plain language: what exists, what's wired up, and what exists but can't fire (journal files with no index and no instruction to search them, a hook script with no settings entry). See `guide/retrieval.md` for why that last distinction is the whole game.

Four more things to look for, because each one changes what's worth setting up on day one:

- **What's installed to run the pieces.** Python runs the guards and small scripts, Node.js runs the weekly friction reader, and on Windows, Git for Windows provides the bash the destructive-command guard runs in. Check with `python --version` (or `python3`), `node --version` and `bash --version`. Note anything missing now, so a guard never gets installed onto a machine that can't run it.

- **Where their work lives, and whether it's synced.** On many Windows and Mac machines, Documents and Desktop are quietly synced by OneDrive, iCloud, Dropbox or Google Drive. Installing or building code inside a synced folder (`npm install`, a dev server, anything that writes thousands of small files) can jam the sync without an error; in the harness this kit comes from, it wedged for about twelve days. If their projects sit in a synced folder, tell them, and offer a CLAUDE.md line in their words: "never install or build code inside <the synced folder>; keep code projects in <an unsynced folder>."
- **Git repos with a remote** (`git remote -v` in their project folders), or deploy tools they use. If there are any, offer the push gate (`reference/hooks/confirm-push.py`) with the starter guards in Phase 3, not later.
- **Code projects that use API keys or store anyone's data.** If there are any, offer the security rule (`reference/rules/security-build-guardrails.md`) in Phase 3.

## Phase 0.5: Borrowed memory (optional; for someone new to Claude Code)

If Phase 0 found little because the person is new to Claude Code, but they've used ChatGPT or Claude chat, the old assistant already holds a rough picture of them. Borrow it so the interview starts from "is this right?" instead of a blank page. Skip this for anyone with an existing setup.

Have them paste this into the assistant they've used most, and paste the answer back to you:

> Write out what you know about me: my work, how I like to be talked to, what I push back on, and what you've gotten wrong about me. Label which parts are facts I've told you and which are your interpretation. Leave out health, family and money details.

How to use the answer:

- **It's a draft about them, written by something else. It isn't their words.** Nothing in it goes into CLAUDE.md or memory until they've confirmed it in Phase 1. Read it before the interview and turn it into questions ("ChatGPT says you'd rather have an idea killed early than lovingly built. True?"), not conclusions.
- **Weight it by section.** The "what you've gotten wrong" and "how I like to be talked to" parts are the gold: they're calibration, and calibration is what Phase 1 is after. A tested run bore this out: its misses section ("optimizes when I want fidelity", "answers the surface question when there's a second layer underneath") was sharper than anything a first interview would reach. The long inventory of projects was the least useful part. Projects arrive in the harness when they're worked on, so don't seed memory with a project list.
- **Watch for anchoring.** A confident, well-written profile can crowd out what the person would have said about themselves. Ask the Phase 1 threads anyway, and let their answers win where the two disagree.
- **Watch for stale facts.** Chat memory holds whatever was true when it was said. Job, projects and situation are the likeliest to have moved on.

## Phase 1: Interview (wants, then calibration)

A conversation, not a questionnaire. Ask one thing, listen, follow it. Five threads to draw out, in whatever order the conversation takes them:

- **What they want that they're not getting.** Start here. The most common answers: "it doesn't remember what we discussed", "its suggestions are flat when I'm refining an idea", "I keep correcting the same thing", "I lose track of where I was." Get one or two in their words; they decide what Phase 2 and Phase 3 prioritize.
- **Their working shape:** long sessions or short, one project or several, where their work lives, what kind of work it mostly is.
- **How they want to be disagreed with:** bluntly and right away, or framed as a question first? Should you flag patterns they didn't ask about?
- **One true thing about how they think.** The high-leverage one. Courtney's is "I judge concrete examples, not descriptions," so her Claude shows instead of explains. Get them to one honest sentence like that; it's worth more than ten borrowed rules.
- **What good help feels like to them,** best reached through a real case: a recent time your suggestions fell flat, and what a better answer would have been.

Draft their CLAUDE.md "About" and "Working style" from what they say (structure: `reference/CLAUDE-skeleton.md`), and show them before writing anything.

## Phase 2: The retrieval loop (first install, the centerpiece)

This is the machinery behind the most common want ("it doesn't remember"). Build, in order:

1. **CLAUDE.md with standing instructions to look things up:** a short pointer-hub section saying when to check the journal, when to check memory, where project context lives. Retrieval fails without an instruction to retrieve.
2. **Memory.** Claude Code's auto memory keeps a `MEMORY.md` index per project and loads its first 200 lines every session. Auto memory is per project, so seed it in the project they work in most: open Claude Code there for this step (or ask which project). Confirm it's on (`/memory`), then seed the index with 3-5 real facts from Phase 1, one line each with a phrase saying when to open the full file (format: `reference/memory/`). Facts that apply to every project (who they are, how they work) belong in `~/.claude/CLAUDE.md` instead, because auto memory is per project. **Auto memory saves on its own, without asking.** Left alone, it fills with your guesses about them, and after a few months the harness is tuned to those guesses. Add a CLAUDE.md line in their words, something like "show me any memory entry before you save it," and tell them `/memory` opens the folder so they can read, edit, or delete what's there.
3. **Journal wiring.** Claude Code has no built-in search of past sessions, so this is the piece you build. A journal folder with dated entries; a way to search it (on day one, you grepping the folder is enough; see CATALOG.md's infrastructure section for when to add a search server); a CLAUDE.md line saying when to search; and the `/journal` skill itself (`reference/commands/journal.md`), installed now rather than with the rest of the close-out set, so the journal has something writing to it from the first session. (A search index and its reindex reminder come later, only if they add a search server.) If they already keep a journal, connect it rather than replacing it.
4. **A push-back line in their CLAUDE.md,** in their words: the standing permission to disagree without flattery. This is half of "better suggestions"; context from steps 1-3 is the other half.
5. **Keep the session transcripts.** Claude Code saves every session as a transcript under `~/.claude/projects/`, and by default deletes them after 30 days (sessions run from the Claude desktop app are kept longer). Journal entries and handoffs point back at those transcripts, and a month later the pointer leads nowhere. Offer to raise `cleanupPeriodDays` in `~/.claude/settings.json` (the source harness keeps them for years; they're plain text and take little space). Checked against the Claude Code docs, September 2026; if the docs now say otherwise, they win.

**Verify before calling it done:** start a fresh session and ask a question whose answer lives only in memory or CLAUDE.md. (The journal is still empty on day one; check it the same way after the first real session has written an entry.) If the fresh session surfaces it, the loop is closed. If not, find which link is dead. Do not report this phase complete on the strength of the files existing.

## Phase 3: The shopping trip

Walk them through `CATALOG.md`, never as a list to read. You've done Phases 0-2; you know what they do and where their friction is. Recommend one tool at a time from the Starter shelf with the reason attached ("you said X; this one is for that moment"), let them accept or skip, and install accepted ones properly, **including their dependencies**, which each catalog entry names. A skill that needs a hook that needs a settings entry is one install, not three.

**Install commands as skills.** The kit ships some tools as command files (`reference/commands/*.md`). Claude Code still runs commands from `~/.claude/commands/`, but skills are the current format: put each one at `~/.claude/skills/<name>/SKILL.md` with a frontmatter block (`name`, and a `description` that says what it's for and when to use it). The description is what lets you reach for it without being asked. **Read `reference/skill-authoring.md` before writing the first one:** a description that's wrapped onto several lines, or that buries its trigger, never fires and never says so. Tell your user the file exists, too; it's what they'll need when they start writing their own skills.

**Every guard gets tested the moment it's installed.** A hook that crashes, or one whose settings entry points at the wrong path, doesn't block anything, and nothing tells you. Hooks fail *open*. In the source harness, two guards were silently dead for weeks this way. So after wiring each guard, pipe it one command it should block and one it should allow (each hook file's header has the two test lines), and show your user the result: a block with its message, then a clean pass. If it doesn't block, the install isn't done. The pipe test proves the script works, not that settings.json runs it, so finish with one live test: in a scratch git folder, try a command the guard should stop (`git add -A` is harmless) through your own shell tool, in each shell you use (Bash, and PowerShell on Windows). You should be blocked with the guard's message.

**The close-out set comes as a set.** `/land` chains `/surface`, `/capture`, `/handoff` and `/journal`. `/journal` went in during Phase 2; install the other three together, or install `/land` knowing it will skip whatever is missing.

Stop after the Starter shelf. Then **write the Toolshelf.** For every Later-shelf tool (and any Starter they skipped), add one line to the Toolshelf section of their CLAUDE.md: the moment it's for, the tool, and the full path to its file in this kit on their machine (see `reference/CLAUDE-skeleton.md`). A relative path breaks when a session runs from another folder, and it's why the README says to unzip the kit somewhere they'll keep it. This step exists because of a real failure: the first version of this kit told its reader when each later tool would help and moved on. That knowledge lived only in his head, his Claude never offered the tools, and he never went back for them. A line in CLAUDE.md is read every session, so you can notice the moment and offer the tool when it arrives. Offer once per moment, never nag.

## Phase 4: The practice (the part no file does)

Read `guide/operator-practices.md` with them. It's short and written for exactly this conversation. The one habit to actually establish now, because everything compounds through it: **when you get something wrong, they say why it missed, and you decide together whether it's worth encoding.** Set up the cheapest capture path for one-off observations (a running notes file is fine) and a rule of thumb for promotion (it recurred, or it clearly deserves a rule the first time).

**Then offer the example-rule menu** (`reference/example-rules.md`): nine short rules from the source harness, each with the reason it exists. Read it together and let them pick only the ones that name something that has already bothered them, reworded in their own voice. Pre-installing all of them is the borrowed-rules failure this kit is built to avoid; a short list they chose beats a long one they didn't.

**If the journal command they installed logs friction at session close (the kit's does), install the other half in this same phase.** `reference/friction/` has the reader, the synthesis skill, and a schedule note for who runs the weekly pass. A friction log with no reader is a partial install, and it's exactly what happened with an earlier copy of this kit: the log got written to for weeks and no synthesis ever ran. Follow the install order in that folder's README. The step that matters is giving the weekly run an owner that isn't a person remembering.

## Closing: an expiry date, not permanence

Set a check-in about two weeks out, in their CLAUDE.md (the skeleton has a slot), **and schedule it so it doesn't depend on anyone reading that line.** If they use the Claude desktop app, create a Desktop scheduled task for that date that opens the check-in. Otherwise, have them put it on their own calendar now, while you're both here. Don't use an in-session reminder ("remind me in two weeks"): those stop when the session ends. The check-in covers what got installed, and three questions. Has the fresh-context surprise happened yet? Did a weekly friction read run, and did they read it? Did any Toolshelf moment come up, and was the tool offered? Also re-run each guard's two test lines: does every one still block? And skim the memory index together: is every line something they'd agree with? Anything that hasn't earned its keep by then gets removed without guilt. A harness that only grows eventually gets abandoned; the source harness stayed alive by pruning.

**At the check-in, show them their shelf.** Build one page (a single HTML file, or a markdown table if they'd rather) listing everything they now have: each skill with what it's for and how it fires (they type its name, or you reach for it on your own), each guard and hook with the moment it runs, each rule, and below those, the Toolshelf items not installed yet with their moments. Save it where they keep notes. Rebuild it at each check-in instead of keeping it up to date by hand; a page rebuilt on purpose can't go quietly stale. Why: everything else in this kit makes *you* remember what exists and when to use it. This lets *them* see it, which is the fix for "I didn't know what I had to reach for." The idea came from the first person this kit was handed to, whose Claude built one on its own.

**The check-in is also the moment to offer the session-start hook** (`reference/hooks/session-start.py`), if there's now a handoff or journal worth resuming from. It tells you at the start of every session where they left off, and re-tests their guards every session instead of every two weeks.

One more thing, for you rather than for them: this kit is a snapshot (dated in START-HERE.md) of someone else's living system. Where your user's harness and hers diverge from here, that's the design working, not drift to correct.
