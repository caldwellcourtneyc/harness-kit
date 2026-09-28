# Writing skills that actually fire

Read this before writing or editing any file in `~/.claude/skills/` (or `~/.claude/commands/`). The seed uses it in Phase 3 when it installs the kit's tools as skills, and it's the reference for every skill you write after that.

**Why it exists:** a skill that never triggers looks exactly like a skill that works. It sits in the folder, `/name` still runs it, and nothing tells you Claude has stopped reaching for it on its own. In the source harness, an audit found 7 of 12 commands had lost their triggers this way, some of them for months, from the formatting mistake described first below.

## The description is the whole trigger

In `~/.claude/skills/<name>/SKILL.md`, the frontmatter `description:` is the only part Claude sees before deciding whether to use the skill. The body loads *after* the skill has already fired. So:

- **Everything about when to use it goes in the description.** A trigger that only appears in the body never fires.
- **Keep it on one line.** Never hard-wrap it. In a command file, the description is the first line of the file and *only* that line, so a wrapped opening paragraph cuts the description off at the first line break. Real example: a decision skill presented itself for months as "Decision clarity partner. Use when facing an ambiguous" with every trigger condition below the cut.
- **Key words first.** Lists of skills get truncated around the first 100 characters. Put what it is in those 100, and when to fire it right after.
- **Be a little pushy.** Claude tends to under-use skills. Name the plain phrasings that should fire it, including ones that don't use the skill's name ("build a page," not only "do UX thinking").

## Don't shadow a built-in name

Claude Code ships its own skills and commands (`/code-review`, `/security-review` and others; type `/` to see the current list), and plugins add more. Before naming yours:

- **Exact matches are worst.** A skill named the same as a built-in makes it unclear which one runs.
- **Near-matches are almost as bad.** One hyphen apart (`/codereview` vs. `/code-review`) confuses both you and Claude. Rename.
- **If yours overlaps a built-in in purpose,** say the division of labor in the description: "Distinct from the built-in /security-review, which checks pending changes; this one audits the whole project."

## Keeping the body honest

- **Check tool names against the live session** before writing them into a skill. MCP tool names change when a server updates, and a skill that names a tool that no longer exists fails quietly.
- **Skills that should improve get a lessons table** (date, lesson, change). A table nobody has touched in months, on a skill that gets used, means lessons aren't being written back.
- **Temporary sections get an expiry date and a named decision** ("on <date>, decide whether to keep X"). A bare "remove after <date>" gets ignored.

## A quick check after writing one

Start a fresh session and describe, in plain words, a situation the skill is for, without naming it. If Claude doesn't reach for it, the description is the problem.
