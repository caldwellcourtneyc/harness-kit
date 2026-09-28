# Catalog: every tool in the kit, tiered

**Snapshot: 2026-09-28.** A photograph of a living system, not a live feed. Trust it for the shape; expect details to drift.

**How to read an entry:** what it's for, its **tier**, what it **needs** in order to actually work, and where its **file** is. The "needs" column is there because of the kit's oldest lesson: a piece can look installed while being dead (a hook script with no settings entry, a journal nobody searches, a log nobody reads). Install each thing together with what it needs, as one install.

**Tiers:**
- **Starter:** what the seed installs, in Phases 2-4. Enough to get the retrieval loop, the close-out, better thinking at decisions, and the first guardrails.
- **Later shelf:** tools with a named moment. The seed writes each moment into your CLAUDE.md's Toolshelf section, so Claude offers the tool when the moment comes instead of it waiting on your memory.

**Skills vs. commands:** both are a markdown file that loads a method when triggered. Skills (`~/.claude/skills/<name>/SKILL.md`) are the current format, and Claude can reach for one on its own when the task matches its description. Commands (`~/.claude/commands/<name>.md`) still work. The seed installs everything as a skill.

**Before installing anything:** read the file. Kit notes at the top of a file say what to adapt; placeholders look like `<your journal folder>`.

---

## Starting or returning to work

| Tool | What it's for | Tier | Needs | File |
|---|---|---|---|---|
| `/pickup` | Re-enter after time away: reconstruct where things were, what's uncaptured, what was promised | Starter | A handoff or journal to read from | `reference/skills/pickup-SKILL.md` |
| `/handoff` | Write a HANDOFF.md so the next session picks up cleanly | Starter | Nothing | `reference/commands/handoff.md` |

## Ending a session (the close-out set)

| Tool | What it's for | Tier | Needs | File |
|---|---|---|---|---|
| `/land` | The whole close-out as one command: surface, capture, handoff, journal, ship check | Starter | The four tools below (it skips any that are missing, and says so) | `reference/skills/land-SKILL.md` |
| `/surface` | Say what went unsaid: insights, missed considerations, blind spots | Starter | Nothing | `reference/commands/surface.md` |
| `/capture` | Route everything worth keeping to where it belongs | Starter | Memory and a journal to route into | `reference/commands/capture.md` |
| `/journal` | A short dated entry, shown to you before it's saved; also logs friction | Starter | A journal folder; the reindex hook if you search with an index | `reference/commands/journal.md` |
| `/friction-scan` | The weekly read of the friction log: what recurred, one smallest fix, what to watch next | Starter, with `/journal` | The log, the watch-for prompts, the reader script, and an owner for the weekly run. All four or none | `reference/friction/` (start with its README) |

## Deciding, refining, framing

| Tool | What it's for | Tier | Needs | File |
|---|---|---|---|---|
| `/x-ray` | Blind-spot scan before committing: what are we both assuming, missing, not asking | Starter | Nothing | `reference/commands/x-ray.md` |
| `/reframe` | Name the frame the work assumes, then offer genuinely different ones | Starter | Nothing | `reference/commands/reframe.md` |
| `/decide` | A thinking partner for a call you're stuck on | Later: a decision with real tradeoffs | Nothing | `reference/later/commands/decide.md` |
| `/prd` | Question an idea before building: walk the design tree, resolve the decisions it depends on | Later: about to build something with real scope | Nothing | `reference/later/commands/prd.md` |
| `/wander` | Think out loud with no destination | Later: you want to think something through with no task at the end | Nothing | `reference/later/commands/wander.md` |

## Building and showing

| Tool | What it's for | Tier | Needs | File |
|---|---|---|---|---|
| `/options` | Two or three divergent design directions side by side, then a live control panel for the winner | Later: correcting the look of the same thing twice in a row | Works best with a taste file | `reference/later/skills/options-SKILL.md` |
| `/squint` | A critique of anything you made, read the way its audience will meet it | Later: before anything goes in front of other people | Nothing | `reference/later/skills/squint-SKILL.md` (+ its web adapter in `squint-references/`) |
| `/ux-thinking` | Will this screen or flow make sense to a person? Asked before building | Later: the first build someone will click through | Nothing | `reference/later/skills/ux-thinking-SKILL.md` |
| `/codehealth` | Code review aimed at the mistakes AI-written code tends to make | Later: the first codebase that matters | Nothing | `reference/commands/codehealth.md` |

## Hooks (the part that doesn't depend on Claude remembering)

A hook is a script Claude Code runs on an event: before a shell command, after a file write, when a session stops. It can block the action outright. **Every hook is a three-part install: the script, an entry in `~/.claude/settings.json` wiring it to its event, and a test.** A script with no entry never fires, and a script that crashes lets everything through; neither says so. So each hook file's header has two test lines, one input it should block and one it should allow. Run both after installing, and again at the two-week check-in. `reference/hooks/settings-hooks-example.json` shows the wiring for every hook below.

| Hook | Runs | What it does | Tier | File |
|---|---|---|---|---|
| Destructive-command guard | Before shell commands | Blocks `git reset --hard`, `git push --force`, `git clean -f`, `rm -rf` on broad paths, and similar | Starter | `reference/hooks/deny-destructive.sh` |
| Credential guard | Before shell commands | Blocks `git add`/`commit` that names `.env`, credential files, keys | Starter | `reference/hooks/deny-credential-paths.py` |
| Stage-everything guard | Before shell commands | Blocks `git add -A` / `.` so only files named on purpose get committed | Starter | `reference/hooks/deny-git-add-all.py` |
| Reindex reminder | After file writes | When a journal file changes, reminds Claude to update the search index, so the index can't quietly go stale | Starter, with journal search | `reference/hooks/reindex-journal.sh` |
| Push gate | Before shell commands | Stops `git push`, GitHub writes (PRs, issues, releases) and deploys until you say yes to that one | Later: your first repo with a remote, or first deploy. Starter if the seed's first look finds remotes | `reference/hooks/confirm-push.py` |
| Append-only guard | Before file writes | Stops a whole-file rewrite of your journal or friction log, so a session working from an old copy can't erase entries another session added | Later: the first time you run two sessions at once (and give each its own git worktree) | `reference/hooks/protect-append-only.py` |
| Session-start check | When a session starts | Tells Claude where you left off (this folder's handoff, your newest journal entry) and proves each guard is still wired in and blocking. Prints a few lines at most | Later: the two-week check-in | `reference/hooks/session-start.py` |
| Show-before-save gate | Before file writes | Blocks writes to memory, CLAUDE.md and rules until Claude has shown you the text and you've said yes | Later: you find a memory entry or rule you never approved | `reference/hooks/gate-show-before-save.py` |

One more hook worth building someday (a pattern only, no file in the kit): a **self-review nudge** at session stop that asks Claude to reread what it just wrote. It needs a lot of tuning before it helps more than it nags.

## Always-on rules (`~/.claude/rules/`)

Small markdown files Claude Code loads every session (or only when matching files are read, if the rule has a `paths:` line). Each one is a trigger, an action, and ideally the incident that earned it. The seed creates the folder; what goes in it comes from your own misses over time. Examples in `reference/rules/`:

| Rule | What it catches | Tier |
|---|---|---|
| `absent-source-discipline.md` | A lookup fails and Claude fills the gap with plausible content anyway | Starter (fully general) |
| `layout-measure.md`, `first-screenful.md`, `type-scale.md` | Three rules for visual work, shipped together: no dead space beside narrow elements, a first screen designed as a priority stack, and a small set of type sizes chosen on purpose | Starter if you build pages; each loads only when web files are read |
| `security-build-guardrails.md` | Keys in browser code, logins that fail open, unguarded file access, debug routes left on | Later: your first app with a paid API key or anyone's data. Starter if the seed finds code projects |

**If you build anything visual:** Claude has a house look (cream or off-white backgrounds, serif headlines, a warm brick-red accent, shadowed rounded cards, pill buttons, "01/02/03" section numbers). Nothing wrong with any of it, but it ships by default, not by choice, and everything Claude makes starts to look alike. Keep a short avoid-list of your own in a rule or your CLAUDE.md and add to it whenever you catch a default you didn't pick.

## Setup references (read by your Claude, not installed as tools)

| File | What it's for | When |
|---|---|---|
| `reference/skill-authoring.md` | How to write a skill whose trigger actually fires, and how not to shadow a built-in | Starter: the seed reads it before installing any skill. Yours to keep for writing your own |
| `reference/example-rules.md` | A menu of nine collaboration rules, each with its reason, to pick from | Starter: offered in Phase 4, never pre-installed |
| `reference/new-project-checklist.md` | What a new project needs on day one, including what goes in its CLAUDE.md | Later: starting a new project |
| `reference/backup/gitignore` | A ready `.gitignore` for backing up `~/.claude` to a private git repo, with credentials excluded | Later: the two-week check-in, if anything you built has survived |
| `reference/later/tools/yt-transcript.py` | Pulls a YouTube video's captions as text (a web fetch of the page gets nothing) | Later: the first YouTube link you want Claude to work with |

## Infrastructure (the plumbing the tools stand on)

| Piece | What it is | Tier | Notes |
|---|---|---|---|
| CLAUDE.md | The always-loaded file: who you are, how to work with you, pointers, the Toolshelf | Starter | Built into Claude Code. Structure: `reference/CLAUDE-skeleton.md` |
| Memory | A per-project folder of facts with a one-line index loaded every session | Starter | Built in (auto memory, on by default). It saves on its own, so the seed adds a "show me before you save" line |
| Journal search | Finding past work by content, mid-session | Starter: grep. Later: a search server | Not built in. Day one, Claude searching the journal folder with grep needs nothing installed. When the journal outgrows that, add an MCP search server |
| Rules folder | Always-loaded rules | Starter (just make the folder) | Built in |
| Friction loop | Session-close prompts, an append-only log, a reader script, a weekly synthesis, one fix | Starter, with the journal | `reference/friction/README.md`. The piece that needs real setup is who runs the weekly read |

---

**Not in the kit:** pieces of the source harness that are wired to one machine or one person's life (a live session dashboard, a task tracker with an API, scheduled routines, skills for personal projects). They'd arrive broken.

**The day-one footprint, in one line:** CLAUDE.md with a Toolshelf and the few rules you picked, memory, a journal you can search, the close-out set, two thinking tools, four tested guards, and the friction loop. Everything else has a named moment and will be here when it comes.
