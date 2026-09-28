# later/: the "add it when you need it" shelf

These tools don't get installed on day one. Each has a moment when it starts paying for itself, and before that moment it's just one more thing to read. During setup, your Claude writes each tool's moment into your CLAUDE.md as a "when this happens, offer that" line. That way Claude offers the tool when the moment arrives, and you don't have to remember it exists. The two-week check-in reviews the list.

They're method files from Courtney's harness, with personal details, private system names, and machine paths taken out. Where a file needs something only you can supply (a journal folder, a taste file, a task tracker), a kit note at the top of the file says so, and the text uses a placeholder like `<your journal folder>`.

**To install one when its moment comes:** put it at `~/.claude/skills/<name>/SKILL.md` (so `options-SKILL.md` becomes `~/.claude/skills/options/SKILL.md`). Files from `commands/` need a frontmatter block added first (`name`, and a `description` saying what it's for and when to use it); Claude Code still runs `~/.claude/commands/<name>.md`, but skills are the current format. Fill in its placeholders, delete the kit note, and move its line out of the Toolshelf section of your CLAUDE.md.

## commands/

- **decide.md**: a thinking partner for a call you're stuck on. Good questions and concrete scenarios, no pros-and-cons table, and a decision record only if you want one. *Reach for it when you're facing a decision with real tradeoffs.*
- **prd.md**: questions an idea before any code gets written, one branch of the design at a time, and ends in either a short spec (a PRD) or a build plan. *Reach for it when you're about to build something with real scope: several files, something people will use, or work that spans sessions.*

## skills/

- **options-SKILL.md**: puts two or three genuinely different design directions side by side instead of tweaking one design round after round, then turns the winner into a live control panel for fine-tuning. *Reach for it the second time in a row you're correcting the look of the same thing.* It works best once you keep a taste file.
- **squint-SKILL.md**: a critique of anything you've made, read the way its audience will meet it rather than the way you'd explain it. *Reach for it before anything goes in front of other people.*
- **ux-thinking-SKILL.md**: checks whether a screen or flow will make sense to a person before it gets built. *Reach for it on your first build that someone will click through.*


## Later-shelf pieces that live elsewhere in reference/

These sit next to their starter siblings, but each has its own moment:

- **hooks/confirm-push.py** (push gate): nothing gets pushed, published to GitHub, or deployed without your yes for that one. *Your first repo with a remote, or your first deploy.*
- **hooks/protect-append-only.py** (append-only guard): a session working from an old copy of your journal can't overwrite entries another session added. Pair it with one git worktree per session for code. *The first time you run two sessions at once.*
- **hooks/session-start.py** (session-start check): at the start of every session, tells Claude where you left off and proves your guards are still wired in and blocking. Kept to a few lines on purpose. *The two-week check-in, once there's a handoff or journal to resume from.*
- **hooks/gate-show-before-save.py** (show-before-save gate): the mechanical version of the "show me before you save a memory" line, for when the line alone keeps slipping. *You find a memory entry or rule you never approved.*
- **rules/security-build-guardrails.md**: no keys in browser code, logins fail closed, file access fenced in, debug routes off. *Your first app with a paid API key or anyone's data.*
- **new-project-checklist.md**: what a project needs on day one, including what goes in its CLAUDE.md. *Starting a new project.*
- **backup/gitignore**: back up `~/.claude` to a private git repo without leaking credentials. *The two-week check-in, if anything you built has survived.*

Each hook needs its settings entry (the `_later_shelf_hooks` block in `hooks/settings-hooks-example.json`) and its two-line test before it counts as installed.

## Also on this shelf, shipped in commands/

- **codehealth.md**: a code review aimed at the mistakes Claude tends to make (needless abstraction, leftover debug code, missing error handling), with each review saved so the next one can check what got fixed. It sits in `commands/` next to the starter tools, but it's a later-shelf tool. *Reach for it on the first codebase that matters to you.*

## Not here

A few of Courtney's tools aren't in the kit at all, because they're wired to her machine or her life. The catalog says so in one line.
