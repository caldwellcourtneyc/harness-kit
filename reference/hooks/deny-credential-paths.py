#!/usr/bin/env python
r"""PreToolUse guard: block `git add` / `git commit` commands that name a credential file.

Registered in settings.json under matcher `Bash|PowerShell` (2026-09-02), replacing the
inline `python -c "..."` string that used to do this job under matcher `Bash`.

Why a file: the inline string passes through Git Bash double quotes on its way to
Python, which collapses `\\` to `\`. That turned its regex `(?:^|\s|/|\\)\.env` into an
unterminated group, so the guard crashed with exit 1 (non-blocking) on every git
add/commit and had been failing OPEN for as long as it was registered that way. A file
has no shell quoting layer, so what you read is what Python runs.

What it blocks: a git add/commit whose command names .env (and .env.local etc.),
credentials.json, secrets.<ext>, a .pem file, or an SSH private key. Terminators
include `;` so PowerShell-style chaining (`git add .env; git commit`) is caught, and
`.env.example` / `.envrc` / `environment.ts` are never matched (the token must END
right after the credential name).

What it deliberately ignores: the text of a commit message. `git commit -m "ignore
.env"` is a normal thing to type after editing .gitignore and must not be blocked.
Only -m/--message arguments are stripped; a path in quotes elsewhere still counts.

Known gap, accepted: a heredoc that MENTIONS `git add .env` is blocked, same as the
other command-text guards. Exit 2 blocks the tool call; stderr is shown to Claude.

Test it after installing (first should print BLOCKED and exit 2, second pass silently):
  echo '{"tool_input":{"command":"git add .env"}}' | python ~/.claude/hooks/deny-credential-paths.py; echo "exit $?"
  echo '{"tool_input":{"command":"git add .env.example"}}' | python ~/.claude/hooks/deny-credential-paths.py; echo "exit $?"
"""
import sys, json, re

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)  # unparseable stdin must never wedge tool use

cmd = data.get("tool_input", {}).get("command", "")
if not re.search(r"\bgit\s+(?:add|commit)\b", cmd):
    sys.exit(0)

# Drop commit-message text so a message that mentions a credential file is not a hit.
# Covers -m, --message, --message=..., and combined short flags such as -am / -sm.
scan = re.sub(r"""(?:-[A-Za-z]*m|--message)(?:=|\s+)(?:"[^"]*"|'[^']*'|\S+)""", " -m MSG ", cmd)

# The credential name must end here: whitespace, end, or a shell separator/quote.
END = r"""(?=[\s;&|"')]|$)"""
PATTERNS = [
    # .env, .env.local, .env.production ... preceded by start, whitespace, a path separator,
    # a quote, or '=' (e.g. --pathspec-from-file=.env). NOT .env.example, .envrc.
    r"""(?:^|[\s/\\"'=])\.env(?:\.[A-Za-z0-9_-]+)?""" + END,
    r"""credentials\.json""" + END,
    r"""\bsecrets\.[A-Za-z0-9]+""" + END,
    r"""\.pem""" + END,
    r"""\bid_(?:rsa|ed25519|ecdsa|dsa)""" + END,
]

# .env.example and friends are templates, not secrets: exclude them explicitly so the
# generic .env.<suffix> pattern above (which exists for .env.local/.env.production)
# does not catch them.
TEMPLATE_SUFFIXES = re.compile(r"""\.env\.(?:example|sample|template|dist)""" + END)

for p in PATTERNS:
    for m in re.finditer(p, scan):
        if TEMPLATE_SUFFIXES.search(scan[m.start():m.end() + 1]):
            continue
        sys.stderr.write(
            "BLOCKED: this git add/commit names a credential file (.env, credentials.json, "
            "secrets.*, a .pem, or an SSH key). Secrets do not go into git. If the file is "
            "genuinely safe (a template, a public key), rename it so it does not look like a "
            "secret, or stage it yourself outside the agent.\n"
        )
        sys.exit(2)

sys.exit(0)
