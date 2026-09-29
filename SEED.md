# SEED: the bootstrap protocol

**You are the user's Claude, reading this inside the Harness Kit.** Your job is not to install Courtney's harness. It is to grow your user's, using this kit's guide and reference files as worked examples of what a mature harness looks like, and your user's answers as the raw material for theirs.

Read `guide/architecture.md` and `guide/retrieval.md` before Step 1. `guide/operator-practices.md` is for the check-in.

## The shape: one sitting, then a scheduled check-in

Setup happens in **one sitting** (Steps 0-6 below), and finishes at a **check-in about two weeks later** that is put on the calendar during that sitting. Day one installs the thin versions of a few pieces and closes the loop: by the end, every session writes to stores the next session reads. Everything else waits for the moment it's useful, and the moments are written down so they arrive on their own.

**The reference files are the mature form.** They grew over months of use. Day one installs the thin starters in `reference/day-one/` instead, and each one grows toward its reference version when the user misses a piece, not before.

## Ground rules

- **Additive only.** Never overwrite or delete anything in the user's existing setup. If something of theirs conflicts with something you're building, show them both and let them choose.
- **Their versions, not copies.** Reference files marked as Courtney's calibration are examples of the *kind* of thing that goes in a slot. The content must come from your user. Copying her calibrations would make you behave like you're working for her. (The day-one starters are mechanism, not calibration: fill in paths, adjust wording to their voice, and keep the steps.)
- **Show before you write.** Every file you create or change in `~/.claude`, show it first and get a yes. That includes CLAUDE.md lines, memory entries, skills, and hooks.
- **Small and running beats complete and abandoned.** The first time this setup was handed to someone, only the journal survived. The other failure is the opposite: a setup so heavy it never finishes. So day one is thin, and it finishes.
- **Triggers first.** Any part of this that depends on someone remembering to come back will stop. So the pieces that bring the setup back (the Toolshelf, the scheduled check-in, the setup-in-progress line) go in at Step 2, before anything else is built. If the sitting ends early, nothing is lost.

## Step 0: Inventory (look before asking)

Before interviewing, look at what they already have: `~/.claude/CLAUDE.md` and any project CLAUDE.md files, `~/.claude/rules/`, skills and commands, hooks in `~/.claude/settings.json`, auto memory (`~/.claude/projects/<project>/memory/`; check whether it's on and what's already in `MEMORY.md`), any journal or notes folder and how it's used, and MCP servers. Report what you find in plain language: what exists, what's wired up, and what exists but can't fire (journal files with no index and no instruction to search them, a hook script with no settings entry). See `guide/retrieval.md` for why that last distinction is the whole game.

Four more things to look for, because each one changes what goes in on day one:

- **What's installed to run the pieces.** Python runs the guards and small scripts, Node.js runs the weekly friction reader (added at the check-in), and on Windows, Git for Windows provides the bash the destructive-command guard runs in. Check with `python --version` (or `python3`), `node --version` and `bash --version`. Note anything missing now, so a guard never gets installed onto a machine that can't run it.
- **Where their work lives, and whether it's synced.** On many Windows and Mac machines, Documents and Desktop are quietly synced by OneDrive, iCloud, Dropbox or Google Drive. Installing or building code inside a synced folder (`npm install`, a dev server, anything that writes thousands of small files) can jam the sync without an error; in the harness this kit comes from, it wedged for about twelve days. If their projects sit in a synced folder, tell them, and offer a CLAUDE.md line in their words: "never install or build code inside <the synced folder>; keep code projects in <an unsynced folder>."
- **Git repos with a remote** (`git remote -v` in their project folders), or deploy tools they use. If there are any, the push gate (`reference/hooks/confirm-push.py`) joins the guards in Step 5.
- **Code projects that use API keys or store anyone's data.** If there are any, offer the security rule (`reference/rules/security-build-guardrails.md`) in Step 5.

**Then judge whether their CLAUDE.md is thin.** Length doesn't decide it; what it says about the person does. Try to answer these three from their CLAUDE.md and auto memory: what their work is and how much they already know; how they want to be disagreed with; how they think or judge (one person's is "I judge concrete examples, not descriptions"). If you can't answer at least two with a line you could quote, it's thin. A 200-line file of build commands and code style can be thin in this sense.

## Step 0.5: Borrowed memory (only if their CLAUDE.md is thin)

If the file is thin but they've used ChatGPT or Claude chat, the old assistant already holds a rough picture of them. Offer to borrow it so the interview starts from "is this right?" instead of a blank page. It's an offer; they can skip it.

Have them paste this into the assistant they've used most, and paste the answer back to you:

> Write out what you know about me: my work, how I like to be talked to, what I push back on, and what you've gotten wrong about me. Label which parts are facts I've told you and which are your interpretation. Leave out health, family and money details.

How to use the answer:

- **It's a draft about them, written by something else. It isn't their words.** Nothing in it goes into CLAUDE.md or memory until they've confirmed it in Step 1. Turn it into questions ("ChatGPT says you'd rather have an idea killed early than lovingly built. True?"), not conclusions.
- **Weight it by section.** The "what you've gotten wrong" and "how I like to be talked to" parts are the gold: they're calibration, and calibration is what Step 1 is after. A tested run bore this out: its misses section ("optimizes when I want fidelity", "answers the surface question when there's a second layer underneath") was sharper than anything a first interview would reach. The long inventory of projects was the least useful part. Projects arrive in the harness when they're worked on, so don't seed memory with a project list.
- **Watch for anchoring.** A confident, well-written profile can crowd out what the person would have said about themselves. Ask the Step 1 threads anyway, and let their answers win where the two disagree.
- **Watch for stale facts.** Chat memory holds whatever was true when it was said. Job, projects and situation are the likeliest to have moved on.

## Step 1: Interview (short)

A conversation, not a questionnaire. Start from what Step 0 found ("your CLAUDE.md says 'be concise'; still true?") and ask only what it didn't answer. Three threads:

- **What they want that they're not getting.** Start here. Common answers: "it doesn't remember what we discussed", "its suggestions are flat when I'm refining an idea", "I keep correcting the same thing", "I lose track of where I was." Get one or two in their words; they decide which Toolshelf moments matter most.
- **How they want to be disagreed with:** bluntly and right away, or framed as a question first? Should you flag patterns they didn't ask about?
- **One true thing about how they think.** The high-leverage one. Courtney's is "I judge concrete examples, not descriptions," so her Claude shows instead of explains. Get them to one honest sentence like that; it's worth more than ten borrowed rules.

Their working shape (long sessions or short, one project or several) usually comes out along the way. If it doesn't, ask.

## Step 2: Triggers first (one CLAUDE.md change, plus the calendar)

Draft one set of additions to `~/.claude/CLAUDE.md` (structure: `reference/CLAUDE-skeleton.md`) and show it as a single diff:

- **About and working style,** from Step 1, only where their file doesn't already say it.
- **A push-back line** in their words: the standing permission to disagree without flattery.
- **Pointer lines:** when to read a project's HANDOFF.md, when to search the journal (Step 3 creates it), when to check memory. Retrieval fails without an instruction to retrieve.
- **"Show me any memory entry before you save it,"** in their words. Auto memory saves on its own, without asking; left alone, it fills with your guesses about them.
- **The Toolshelf.** One line per tool that isn't going in today: the moment it's for, the tool, and the full path to its file in this kit on their machine. Fill it from `CATALOG.md`: every Later-shelf tool, plus `/x-ray`, `/reframe`, `/pickup`, and the three visual rules if they build pages. A relative path breaks when a session runs from another folder, which is why the README says to unzip the kit somewhere they'll keep it. Why this exists: the first version of this kit told its reader when each later tool would help and moved on. That knowledge lived only in his head, his Claude never offered the tools, and he never went back for them. A line in CLAUDE.md is read every session, so you can notice the moment and offer the tool. Offer once per moment, never nag.
- **The check-in line,** with a date about two weeks out and what it covers (see "The check-in" below).
- **A setup-in-progress line:** "Harness setup in progress: offer to continue at Step N (kit: <full path to SEED.md>)." Update N as you go; remove the line at Step 6.

After the yes, **schedule the check-in so it doesn't depend on anyone reading that line.** If they use the Claude desktop app, create a Desktop scheduled task for that date that opens the check-in. Otherwise, have them put it on their own calendar now, while you're both here. Don't use an in-session reminder ("remind me in two weeks"): those stop when the session ends.

## Step 3: Memory, journal, transcripts

1. **Memory.** Auto memory keeps a `MEMORY.md` index per project and loads its first 200 lines every session. It's per project, so seed it in the project they work in most: ask which, and write to that project's folder under `~/.claude/projects/` (Step 0 found it). Confirm auto memory is on (`/memory`), then add 3-5 real facts from Step 1, one line each with a phrase saying when to open the full file (format: `reference/memory/`). Facts that apply to every project belong in `~/.claude/CLAUDE.md` instead. Tell them `/memory` opens the folder so they can read, edit, or delete what's there.
2. **Journal.** Claude Code has no built-in search of past sessions, so this is the piece you build. Make a journal folder (or connect the one they already keep). Create `FRICTION-LOG.md` in it, with the "Log format" section of `reference/friction/README.md` pasted in as its header. Install the day-one journal (`reference/day-one/journal-SKILL.md`) as a skill. Searching on day one is you grepping the folder, which the pointer line from Step 2 tells you to do; a search server comes later if the journal outgrows grep.
3. **Keep the session transcripts.** Claude Code saves every session as a transcript under `~/.claude/projects/` and by default deletes them after 30 days (sessions run from the Claude desktop app are kept longer). Journal entries and handoffs point back at those transcripts, and a month later the pointer leads nowhere. Offer to raise `cleanupPeriodDays` in `~/.claude/settings.json`. Checked against the Claude Code docs, September 2026; if the docs now say otherwise, they win.

**Installing a skill.** Put it at `~/.claude/skills/<name>/SKILL.md` with a frontmatter block (`name`, and a `description` that says what it's for and when to use it). The description is what lets you reach for it without being asked. **Read `reference/skill-authoring.md` before the first one:** a description that's wrapped onto several lines, or that buries its trigger, never fires and never says so. Some reference tools ship as command files (`reference/commands/*.md`); install those as skills too when their time comes.

## Step 4: The close-out

Install the day-one close-out (`reference/day-one/land-SKILL.md`) as a skill. It runs the journal from Step 3, so the two go in together. Add a CLAUDE.md line if it isn't there yet: "when the session is winding down, offer /land. Don't wait to be asked."

## Step 5: Guards, each tested

Three starter guards, plus the push gate if Step 0 found remotes: `reference/hooks/deny-destructive.sh`, `deny-credential-paths.py`, `deny-git-add-all.py` (and `confirm-push.py`). Wiring for each is in `reference/hooks/settings-hooks-example.json`. If Step 0 found code projects with keys or user data, offer the security rule here too.

**Every guard gets tested the moment it's installed.** A hook that crashes, or one whose settings entry points at the wrong path, doesn't block anything, and nothing tells you. Hooks fail *open*. In the source harness, two guards were silently dead for weeks this way. So after wiring each guard, pipe it one command it should block and one it should allow (each hook file's header has the two test lines), and show your user the result: a block with its message, then a clean pass. If it doesn't block, the install isn't done. The pipe test proves the script works, not that settings.json runs it, so finish with one live test: in a scratch git folder, try a command the guard should stop (`git add -A` is harmless) through your own shell tool, in each shell you use (Bash, and PowerShell on Windows). You should be blocked with the guard's message.

## Step 6: Prove it, then finish

Start a fresh session and ask a question whose answer lives only in memory or CLAUDE.md. (The journal is still empty; the check-in tests it.) If the fresh session surfaces the answer, the loop is closed. If not, find which link is dead. Do not report setup done on the strength of the files existing.

Then remove the setup-in-progress line, and tell them three things: the check-in date and that it's scheduled; that /land closes each session; and the one habit that makes the rest compound: **when you get something wrong, they say why it missed.** The journal's friction check picks it up from there.

## The check-in (about two weeks later)

The scheduled task or calendar entry opens this. It's the second half of setup, and also the first pruning pass.

**Review:**
- Has a fresh session surprised them with something from a past one yet? Search the journal for something from week one to prove that link.
- Re-run each guard's two test lines. Does every one still block?
- Skim the memory index together. Is every line something they'd agree with?
- Go through the Toolshelf. Did any moment come up, and was the tool offered?
- Anything that hasn't earned its keep gets removed without guilt. A harness that only grows eventually gets abandoned; the source harness stayed alive by pruning.

**Add what was deferred:**
- **The friction reader.** The log has two weeks of entries now, which is when the first read is worth running. Install the rest of `reference/friction/` per its README (the reader, the synthesis skill, and `WATCH-FOR.md` with the journal's four questions as its core tier), run the first synthesis, and give the weekly run an owner per `SCHEDULE.md`: a scheduled task, not a person remembering. A friction log with no reader is the exact failure an earlier copy of this kit had.
- **Grow the thin starters where they felt a gap.** Compare each day-one skill with its reference version and offer only the pieces they missed.
- **The practice.** Read `guide/operator-practices.md` with them. Then offer the example-rule menu (`reference/example-rules.md`): let them pick only the rules that name something that has already bothered them, reworded in their voice. Pre-installing all of them is the borrowed-rules failure this kit is built to avoid.
- **The session-start hook** (`reference/hooks/session-start.py`), if there's now a handoff or journal worth resuming from. It says where they left off at the start of every session, and re-tests their guards every session instead of every two weeks.

**Show them their shelf.** Build one page (a single HTML file, or a markdown table if they'd rather) listing everything they now have: each skill with what it's for and how it fires (they type its name, or you reach for it on your own), each guard and hook with the moment it runs, each rule, and below those, the Toolshelf items not installed yet with their moments. Save it where they keep notes. Rebuild it at each check-in instead of keeping it up to date by hand; a page rebuilt on purpose can't go quietly stale. Everything else in this kit makes *you* remember what exists; this lets *them* see it, which is the fix for "I didn't know what I had to reach for." The idea came from the first person this kit was handed to, whose Claude built one on its own.

**Set the next check-in** (monthly is plenty from here) the same way: scheduled, not remembered.

One more thing, for you rather than for them: this kit is a snapshot (dated in START-HERE.md) of someone else's living system. Where your user's harness and hers diverge from here, that's the design working, not drift to correct.
