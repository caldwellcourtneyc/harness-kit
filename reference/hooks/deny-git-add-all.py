#!/usr/bin/env python
"""PreToolUse guard: block `git add -A` / `--all` / `.`

Why this exists: staging everything sweeps in untracked files from OTHER
parallel sessions running in the same repo. It happened at least twice
("only commit your own stuff") and cost cleanup time each time. Stage by
explicit path instead. If -A is genuinely wanted, run it yourself outside
the agent.

Precision: only the argument segment of each `git add ...` invocation is
checked (up to the next && || ; | or newline), so `git add ./src/file.js`
and a stray `-A` token elsewhere in a chained command do NOT false-trigger.
Known gap (acceptable for a guardrail, not an adversary): `git -C <path>
add .` bypasses. Exit 2 blocks the tool call.

Test it after installing (first should print BLOCKED and exit 2, second pass silently):
  echo '{"tool_input":{"command":"git add -A"}}' | python ~/.claude/hooks/deny-git-add-all.py; echo "exit $?"
  echo '{"tool_input":{"command":"git add src/app.js"}}' | python ~/.claude/hooks/deny-git-add-all.py; echo "exit $?"
"""
import sys, json, re

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)  # can't parse -> don't block

cmd = data.get("tool_input", {}).get("command", "")

# Isolate each `git add <args>` segment and test only its own arguments.
for m in re.finditer(r"\bgit\s+add\b(.*?)(?:&&|\|\||;|\n|$)", cmd, re.S):
    args = m.group(1)
    # a whole-token -A, --all, or "." / "./"  (NOT "./path", NOT "..")
    if re.search(r"(?<!\S)(?:-A|--all|\.(?:/)?)(?!\S)", args):
        sys.stderr.write(
            "BLOCKED: `git add -A/--all/.` stages everything, including other "
            "parallel sessions' untracked files. Stage by explicit path "
            "(git add path/to/file). If you truly need to stage all, run it yourself.\n"
        )
        sys.exit(2)

sys.exit(0)
