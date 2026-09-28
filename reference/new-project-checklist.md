# New-project checklist

**Kit note:** later shelf. The moment for it: starting a new project. Install it where your CLAUDE.md can point at it (for example `~/.claude/new-project-checklist.md`, with a pointer line: "starting a new project → run the new-project checklist"). Trim it to what you'll actually do.

**Why it exists:** `/handoff` and `/pickup` both assume a project folder with its own CLAUDE.md, and nothing else in the kit says what goes in one. Setting a project up properly on day one is cheap; retrofitting it after something breaks is not.

## Scaffold

- [ ] A project `CLAUDE.md` (what goes in it: below).
- [ ] A `.gitignore` that keeps out `node_modules`, build output, and **every `.env` file**. Do this before the first commit, not after.
- [ ] A short note of which environment variables the project needs, where to get each, and an example value (never the real one).
- [ ] `git init` and a first commit.
- [ ] Add the project to wherever your CLAUDE.md keeps its list of projects, so Claude can find it when you name it later.
- [ ] If it's code that will use a paid API key or store anyone's data: the security rule (`reference/rules/security-build-guardrails.md`) should be installed before the first line of code. It only loads when code files are read, so on a brand-new project it may not have loaded yet.

## Three standing docs, each answering one question

Resist growing more than these.
- **CLAUDE.md**: how to work in this project, and nothing else. It loads into every session, so history and reasoning don't belong here; they cost you on every session. Point to them instead.
- **A concept or README doc**: why the project exists, the decisions and their reasons, how it's built.
- **HANDOFF.md**: where the work is right now. Written at the end of a session, checked at the start of the next.

## What the project CLAUDE.md holds

- The tech stack and key dependencies.
- The commands: how to run it, build it, test it.
- Conventions and patterns to follow, with a pointer to where the reasoning lives.
- Known issues. (Current priorities go in HANDOFF.md.)
