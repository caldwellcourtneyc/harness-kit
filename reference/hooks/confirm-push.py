#!/usr/bin/env python
"""PreToolUse guard: every push, GitHub write, and deploy needs your yes, every time.

Kit note: a portable version of a live hook. Later shelf. The moment for it: your first
repo with a remote, or your first deploy. Wire it in settings.json on the Bash matcher
(and PowerShell, if you use it); see settings-hooks-example.json.

What it blocks:
  - `git push` (including `git -C <path> push`), but not `git stash push`
  - `gh` commands that create or change something other people can see: repo create/edit/
    delete, PR create/comment/merge/review/close, issue create/comment/close, releases, gists.
    Read-only gh (view, list, status, clone) is never blocked.
  - deploy and publish commands: vercel, netlify, supabase functions deploy, npm publish,
    wrangler, firebase, fly. Add your own to DEPLOY below.

How the yes works: Claude asks you in chat, you say yes to THIS push, and Claude re-runs
the exact command with a marker in front: `PUSH_OK=1 git push ...` (bash) or
`$env:PUSH_OK='1'; git push ...` (PowerShell). The marker is a speed bump, not a lock: its
job is to make the ask happen. Claude should never add it without your yes for this push.

Why it exists: "ask before pushing" written as an instruction kept getting skipped once
work had momentum, or after "always allow" was clicked for git. In the source harness,
widening this hook from git push alone to also cover gh writes and deploys is what cut
push-related friction, where the written rule alone had not.

Precision: only matches a command in command position (start of a line, or after ; & | ( {),
so a commit message or an echo that merely mentions "git push" does not trip it. Heredoc
bodies are stripped first, so writing a doc about pushing doesn't trip it either.
Known gap (fine for a speed bump, not for an adversary): a push hidden inside a quoted
`bash -c "..."` payload slips past.

Test it after installing (it should print BLOCKED and exit 2, then pass silently):
  echo '{"tool_input":{"command":"git push origin main"}}' | python ~/.claude/hooks/confirm-push.py; echo "exit $?"
  echo '{"tool_input":{"command":"git status"}}' | python ~/.claude/hooks/confirm-push.py; echo "exit $?"
"""
import json
import re
import sys

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)  # can't parse -> don't block real work

cmd = data.get("tool_input", {}).get("command", "")
if not cmd or "PUSH_OK" in cmd:
    sys.exit(0)

# Drop heredoc bodies so a doc that mentions `git push` doesn't count as a push.
stripped = re.sub(r"(<<-?\s*['\"]?(\w+)['\"]?[^\n]*)\n.*?\n\2\b", r"\1", cmd, flags=re.S)

START = r"(?m)(?:^|[;&|({]\s*)(?:\w+=\S+\s+)*"
GIT_PUSH = START + r"git(?:\s+-C\s+\S+)?(?:\s+--?\S+)*\s+push\b"
GH_WRITE = START + (
    r"gh\s+(?:repo\s+(?:create|edit|delete|archive)"
    r"|pr\s+(?:create|comment|merge|review|close|reopen|edit|ready)"
    r"|issue\s+(?:create|comment|close|reopen|edit|delete)"
    r"|release\s+(?:create|edit|delete|upload)"
    r"|gist\s+create)\b"
)
DEPLOY = START + (
    r"(?:npx\s+)?(?:supabase\s+functions\s+deploy"
    r"|vercel\s+(?:deploy|--prod|link|env\s+(?:add|rm))"
    r"|netlify\s+deploy|npm\s+publish|wrangler\s+(?:deploy|publish)"
    r"|firebase\s+deploy|fly\s+deploy)\b"
)

HOW = (
    " Ask the user for a yes to THIS action; earlier approvals don't carry over. Once they "
    "say yes, re-run the exact command with the marker: bash `PUSH_OK=1 <command>` or "
    "PowerShell `$env:PUSH_OK='1'; <command>`. Never add the marker without their yes."
)

for pattern, what in (
    (GIT_PUSH, "git push sends your commits to a shared remote."),
    (GH_WRITE, "this gh command creates or changes something other people can see."),
    (DEPLOY, "this command deploys or publishes to a hosted service."),
):
    if re.search(pattern, stripped, re.I):
        sys.stderr.write("BLOCKED: " + what + HOW + "\n")
        sys.exit(2)

sys.exit(0)
