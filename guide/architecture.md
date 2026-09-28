# How the harness hangs together

Written for your Claude, readable by you. This is the map of the harness at the architecture level: the layers, what each is for, and the loop that keeps it improving. Nothing here is an install instruction; SEED.md decides what actually gets built.

## Claude Code ships the sockets

Almost every mechanism a harness uses is already built into Claude Code: a CLAUDE.md file it reads every session, a rules folder, auto memory, skills, hooks, and MCP servers for adding tools. (Checked against the Claude Code docs in September 2026. If something below disagrees with the current docs, the docs win.) The one thing it doesn't have is a way to search past sessions by content; you add that yourself.

What doesn't come in the box is what goes *in* those sockets: your instructions, your facts, your methods, your guardrails, and the habit of writing to them at the end of each session. That's what this kit is about.

## The layers, by when they load

The whole design turns on one question: **when does Claude see this?** There are three answers (always, when relevant, when something happens), and choosing the right one for each piece of knowledge is most of harness design.

| Layer | Loads | For |
|---|---|---|
| `CLAUDE.md` (`~/.claude/CLAUDE.md` for you, plus one per project) | Every session, always | Who you are, working style, standing rules, and above all **pointers**: instructions for when to go read what |
| `rules/*.md` (`~/.claude/rules/`) | Every session, always (or only when matching files are read, if the rule has a `paths:` line) | Rules that must fire without anyone remembering them. Each one is trigger + action + scope |
| Memory index (`MEMORY.md`) | Every session (Claude Code's auto memory loads the first 200 lines) | One line per stored fact, so Claude starts knowing what exists |
| Memory files | On demand, when relevant | The facts themselves. They cost nothing until needed |
| Journal | On demand, via search | The dated record of what happened and what was learned. Not built in: a folder of files plus a way to search it |
| Skills (`~/.claude/skills/<name>/SKILL.md`) | When triggered, by you (`/name`) or by Claude when the task matches the skill's description | Packaged methods: how to do a kind of task well, written once |
| Hooks (wired in `~/.claude/settings.json`) | Mechanically, on events | Enforcement that doesn't depend on Claude remembering: guards, checks, auto-indexing |

Three structural ideas worth stealing outright:

**The pointer hub.** Courtney's CLAUDE.md doesn't try to hold everything. It holds *pointers* with triggers: "when starting a project, read X"; "when I name a project you can't locate, read the project map first." The always-loaded file stays small, the knowledge lives where it can grow, and retrieval happens because an always-loaded line says when to retrieve.

**Always-on vs. recall-gated.** A rule that must never be missed (a safety guard, a discipline that failed silently before) lives in `rules/` and loads every session. Background knowledge (why a decision was made, reference material) lives in memory, found when relevant. Putting everything in always-on bloats every session. Putting operative rules in recall-gated storage means they don't fire when needed. The reference files include examples of each so the difference is visible.

**Guide vs. guarantee.** Anything in the first six rows can only *guide* Claude. It's information, and Claude can miss it or weigh it wrong. Only a hook can *guarantee*, because a hook is a script that runs whether or not Claude is thinking about the topic. So a rule of thumb for where a correction goes: if a script can detect the moment (a command about to push code, a file about to be deleted), make it a hook. If it takes judgment, make it a rule. If it's just a fact, make it a memory.

The source harness has a small piece of evidence for this, from its friction log (a running list of what went wrong, one line per item). Two fixes were made about a month apart, and each was measured over the six weeks either side of it. One was a written rule: when a page fails to load, mark every claim that depended on it as unverified. The failure it targeted went from about 6% of logged items before the rule to about 15% after. That's partly because the rule made the failure easier to notice, but it clearly didn't make it go away. The other was a hook that blocks a push until you say yes. Before it was widened, 3 of the first 8 logged items were pushes that hadn't been confirmed; after, 9 of the next 223 were push-related. Small numbers, one harness, so treat it as a hint, not proof.

The second half of that evidence matters as much: several of those nine later items were friction *caused by the hook* (a blocked push that needed a second step). **A hook moves friction; it doesn't end it.** It turns "Claude did the wrong thing silently" into "Claude had to stop and ask," which is almost always the better trade, but it's still a cost you'll feel. Expect it, and tune the hook when it blocks things it shouldn't.

**The placement test.** Before promoting anything to a rule, a memory, or a CLAUDE.md pointer, ask one question: **does this need to fire when Claude isn't already thinking about its topic?** If yes, it has to be always loaded (CLAUDE.md or a rule without a `paths:` line), or a hook, because Claude won't go looking for something it doesn't know is relevant. If it only matters once the topic is already on the table, it can live in memory or behind a pointer, where it costs nothing until needed.

## The loop (why the system gets better instead of just bigger)

Every layer above is *written by the same loop*:

1. **Something goes wrong or works well:** a miss, a correction, a pattern noticed.
2. **It gets captured cheaply:** a line in the journal, a note, a friction-log entry. No approval needed, no structure required. Capture is free.
3. **If it recurs, or the single incident clearly warrants it, it gets promoted** to the right layer: a rule if it must always fire, a memory if it's context, a skill if it's a method, a hook if it can be enforced mechanically. Promotion is deliberate and rare; most captures stay captures.
4. **Next session, it fires,** and the correction that would have evaporated is now permanent.

The rules in `reference/` each carry a dated incident at the bottom. That's the loop's fingerprint. They weren't designed in advance; they were earned, one failure at a time, and encoded with the why attached so a future session can recalibrate them instead of just obeying them.

This loop is the real answer to "why does a harnessed Claude behave differently." The files are its residue, which is why the kit installs the loop first and treats the files as examples.

## What deliberately isn't in this kit

The source harness includes pieces bound to one machine and one person's life: a live session dashboard, a task tracker with an API, scheduled routines, skills for her personal projects. They're left out because they're products of months of iteration on one exact setup and would ship broken. The patterns behind a couple of them (a shared surface both you and Claude write to; a tracker Claude updates at session end) may interest you someday, but they're the wrong first install for anyone.
