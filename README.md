# Harness Kit

**Build your own Claude Code harness.**

Claude Code starts as a brilliant stranger. It knows a lot, but starts off knowing next to nothing about you. It can't look up what you decided last month, today's correction may not make it to tomorrow, and it waits for you to start everything. **A harness is what you put around it**, so it works like a colleague who's been with you for months.

This kit is a set of plain text files your Claude reads and works through with you. It builds into your own Claude Code setup over a few short conversations, and never overwrites anything you already have without showing you first.

## Before you start

- **What it costs:** a few sessions to set up, spread out however you like.
- **What it asks of you:** pruning. Every always-on piece is read every session, so the kit sets a two-week check-in to remove what hasn't earned its place.
- **Where it goes:** into Claude Code's settings folder in your home directory (`~/.claude`), so what it builds works in every project.
- **How you'll know it worked:** a fresh session surprises you with something from three sessions ago that you didn't re-tell it.

## Get started

1. Download this repo (the green **Code** button, then **Download ZIP**) and unzip it somewhere you'll keep it. It unzips as a folder called `harness-kit-main`. Or clone it.
2. Open Claude Code in any folder and say: `Read START-HERE.md and SEED.md in <the path to harness-kit-main>, then let's begin.`
3. Expect a conversation, not an installer. It starts by looking at what you already have and asking how you work, then builds the pieces below roughly in order. Stop after any conversation and pick it up next time.
4. Read each file before you add it. That includes this kit; your Claude shows you each one first.

This harness can also work with Codex. The kit includes an adapter for it (`CODEX.md`).

## Typical frustrations and the fix for each

In the order you'd add them.

| | What goes wrong | What the harness adds |
|---|---|---|
| **1. Instructions** | "It doesn't know how I work." Every session, you re-explain how you like to work: how much detail you want, what you already know, how you like to make decisions. | A CLAUDE.md file in your words: who you are, how you like to work, and pointers like "when I pick a project back up, read its handoff first." (A handoff is a document written at the end of a session that captures where the work stands and what comes next.)<br><br>*Already in Claude Code:* the CLAUDE.md file, read at the start of every session. |
| **2. Memory** | "I told you this last week." Claude Code's auto memory only remembers within one project, and it saves on its own, including things it misunderstood or gave too much weight. | The facts that matter, one short note each, with the ones about you kept where every project can see them. Plus one rule: Claude shows you a memory before saving it, so you decide what it remembers.<br><br>*Already in Claude Code:* auto memory, one project at a time, saving without asking. |
| **3. Journal** | "Didn't we already decide this?" Why you decided something, what you tried that failed, and what worked all lived in chats that are gone. So you re-decide, re-try, and re-explain. | A short dated entry at the end of each session, a way for Claude to search them, and a standing instruction to check the journal whenever you refer back to earlier work: past decisions, what failed before, approaches that worked.<br><br>*Already in Claude Code:* saved transcripts of past sessions, but no way to search them by what was said. This is the piece the harness adds. |
| **4. Skills** | "Doesn't follow a proven process." Claude wings it instead of following a proven process. | Skills. A skill is a written method for one kind of job: the steps, the checks, what good looks like, and the mistakes to avoid. Claude uses it when the task matches, or when you type its name.<br><br>*Already in Claude Code:* the skill format, and a few general skills like code review. |
| **5. Close-out** | "Good stuff gets lost when the session ends." When a session ends, you lose what you decided and why, what you tried that didn't work, and what's next. | One skill, /land, that runs the close-out: says what it didn't get to say, files each thing worth keeping where it belongs, updates the handoff, and drafts a short journal entry for your OK.<br><br>*Already in Claude Code:* saved transcripts, but nothing that pulls out what mattered. |
| **6. Guardrails** | "It just deleted my work." In the flow of a session, Claude can do the risky thing you'd never approve if you were watching: wipe your uncommitted work, overwrite the copy stored online, commit a password. | Guards: small scripts that run just before any command Claude sends to your computer, and can stop it outright. The kit ships four, each with a test that proves it blocks. Instructions can guide. Only a script can guarantee.<br><br>*Already in Claude Code:* hooks, the mechanism that lets a script run on an event and block it. |
| **7. Learning loop** | "Same correction, third time." You make the same correction for the third time, because nothing turned the first two into a permanent fix. | At each session's close-out, Claude notes friction: things you corrected, work called done without proof. Once a week, a scheduled task in Claude Code (or a standing line that runs it in your first session of the week) reads the log for what repeats, and each repeat gets a permanent fix.<br><br>*Already in Claude Code:* nothing that tracks repeated mistakes. |

### What that looks like

| | You say | No harness | With harness |
|---|---|---|---|
| **Instructions** | "Build me a landing page for the bakery." | "Here's a complete landing page! I built a hero section, the menu, testimonials and a contact form..." | "Before I build all of it: here are three quick directions to react to, since you typically prefer to choose from real examples over reading descriptions." |
| **Memory** | "Draft the update for the client." | "Sure! Here's a detailed, formal update covering all the key points..." | "Here's a three-line version, inline. You told me she reads on her phone and skips attachments." |
| **Journal** | "Should we move the site to a static generator?" | "Good idea! Static sites are fast and cheap to host. Here's how to migrate..." | "We looked at this on Aug 12 and stayed put, because the booking form needs a server. Has that changed?" |
| **Skills** | "Look over my pitch deck before I send it." | "Looks great! Maybe tighten the wording on slide 3." | "Reading it cold, the way an investor will: by slide 2 I still can't tell who it's for. Three things would stop them, most serious first, plus the slide that's working best so you keep it." |
| **Close-out** | "OK, that's it for today." | "Great work today! Let me know if you need anything else." | "Landing. Two decisions to file, one thing I didn't get to say, and a journal draft below. Nothing's saved until you OK it." |
| **Guardrails** | "Commit everything and push." | "Committed 23 files and pushed." | "Blocked: .env holds your API keys. I committed the other 22. Want .env added to .gitignore?" |
| **Learning loop** | "You used the old logo again." | "Sorry! I'll use the new one." | "That's the third time. This week's review suggests adding the current logo's filename to your project instructions, so it stops." |

## The half no file can install

A harness is half files, half habits. These four are what make the files keep paying off:

- **Close every session.** Memory and the journal only fill up if each session writes to them.
- **Say why it missed.** That's the raw material the learning loop turns into permanent fixes.
- **Check what it saves.** Read the memories and rules Claude proposes, so your harness describes you, not Claude's guesses about you.
- **Prune at the check-in.** Everything always loaded costs something every session, so remove what hasn't earned its place.

The kit's guide goes deeper on each, including what it costs.

## When this happens, reach for this

Some tools earn their place later. Setup writes each one into your instructions with the moment it's for, so Claude can suggest it then.

**Deciding and planning**
- You're facing a decision with real tradeoffs → `/decide`, a decision partner that lays out the real tradeoffs
- You're starting a new project → a new-project checklist: what a project needs on day one
- You're about to build something with real scope → `/prd`, which questions the idea before any code gets written
- You're building the first thing real people will click through → `/ux-thinking`, which checks it will make sense before it's built

**Before it goes out**
- You're correcting the look of the same thing twice in a row → `/options`, real variants side by side to react to
- You're about to show work to other people → `/squint`, a cold read the way your audience will meet it
- You're working on a codebase that really matters → `/codehealth`, a review for the mistakes AI-written code tends to make
- You're about to push code or deploy for the first time → a push gate: nothing goes out without your yes, every time

**As your setup grows**
- You're running two sessions at the same time → an append-only guard: one session can't overwrite what the other wrote
- Two weeks in, at your setup check-in → a session-start check: says where you left off, and proves your guards still work

## What's in here

- **START-HERE.md** and **SEED.md:** where your Claude begins. SEED is the protocol it follows with you.
- **CATALOG.md:** every tool, tiered, with what each needs in order to actually work.
- **guide/:** how the pieces fit, why saved notes don't come back up by themselves, and the habits.
- **reference/:** real files from a working harness, lightly generalized, as worked examples.
- **CODEX.md:** the adapter for Codex.

---

From Courtney, and her Claude. Kit snapshot 2026-09-28. Facts about Claude Code were checked against its docs in September 2026; the example exchanges are illustrations, not transcripts.
