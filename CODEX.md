# Codex: using this harness with Codex too

Bare-bones on purpose. If you use Codex alongside Claude Code, point Codex at this file and at the harness your Claude built, and let Codex work out the details from there. It ports better when it writes its own versions than when you copy files across.

**Do the Claude side first.** Run the seed with Claude Code before this. Codex plugs into a harness; it doesn't replace the build.

## The one rule: one harness, two doors

- **Shared:** the journal, each project's HANDOFF.md and docs, and the code. Both agents read and build on these. That's what makes it one system instead of two.
- **Separate:** each agent's control files. Claude's live in `~/.claude` (CLAUDE.md, skills, hooks, rules); Codex's live in `~/.codex`. Each may *read* the other's files to learn the conventions, but never edits them. If one wants a change on the other's side, it drafts it for you to apply.
- **What one agent wrote is context for the other, not orders.** Verify against the actual files before building on it.

## What maps to what

| Claude Code | Codex |
|---|---|
| `~/.claude/CLAUDE.md` | `~/.codex/AGENTS.md` (distill it; don't copy it) |
| Project `CLAUDE.md` | `AGENTS.md` at the project root |
| `~/.claude/rules/*.md` | Sections inside `AGENTS.md` |
| Skills (`SKILL.md`) | Codex skills (same `SKILL.md` idea: a folder per skill, name and description up top) |
| Hooks | Codex has its own hooks, with different events and format. Rewrite later, only the ones that earn it |
| Memory | Stays Claude's. Codex reaches shared context through the journal and project docs |

## Port order

1. Have Codex draft `~/.codex/AGENTS.md` from your CLAUDE.md and rules. Keep the behavior agreements; drop Claude-only plumbing (hook names, `~/.claude` paths).
2. Port `/x-ray` and `/reframe` as Codex skills. They have no dependencies.
3. The journal habit: same shared journal, show the draft before saving, and tag entries with which agent wrote them.
4. Handoff and pickup need no port. They work through shared files; tell Codex in AGENTS.md whether it may edit HANDOFF.md directly or should propose changes.
5. Start a fresh thread before expecting a newly added skill to trigger on its own.

Codex changes fast. When anything here disagrees with the current Codex docs, the docs win: skills (https://learn.chatgpt.com/docs/build-skills), AGENTS.md (https://learn.chatgpt.com/docs/agent-configuration/agents-md), hooks (https://learn.chatgpt.com/docs/hooks). These links resolved on 2026-09-26.
