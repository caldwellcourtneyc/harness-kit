#!/usr/bin/env python
"""PreToolUse guard: never replace a whole append-only file (your journal, your friction log).

Kit note: a portable version of a live hook. Later shelf. The moment for it: the first time
you run two Claude sessions at the same time. Set PROTECTED below to your own journal folder
and friction log, then wire it on the Write matcher (see settings-hooks-example.json).

What happened: a session read the day's journal in the morning. Two other sessions added
entries during the day. The first session then rewrote the whole file from its morning copy,
and three entries were gone. Cloud-sync version history didn't have them and the folder
wasn't in git; they came back only because the old text was still in that session's
transcript. Claude Code's own read-before-write check didn't help: a read from hours ago
still counts as a read.

What it does: blocks the Write tool (whole-file replace) on a protected file that already
has content. Edit still works, and Edit is the safe way to add an entry, because Edit has
to match text that is actually in the file right now, so it can't silently drop entries
another session added. Creating a new file is never blocked.

The other half of running parallel sessions: give each session its own git worktree
(`claude --worktree`, or ask Claude to set one up) so two sessions never edit the same
checkout of your code.

Test it after installing (point the path at a real, non-empty journal file):
  echo '{"tool_input":{"file_path":"<a real journal file>"}}' | python ~/.claude/hooks/protect-append-only.py; echo "exit $?"
  echo '{"tool_input":{"file_path":"/tmp/not-protected.md"}}' | python ~/.claude/hooks/protect-append-only.py; echo "exit $?"
"""
import json
import os
import re
import sys

# One regex per protected location, matched against the path with forward slashes.
# Replace these with your own.
PROTECTED = [
    (r"/<your journal folder>/[^/]+\.md$", "journal entry"),
    (r"/<your friction log folder>/FRICTION-LOG\.md$", "friction log"),
]

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)  # can't parse -> don't block real work

path = data.get("tool_input", {}).get("file_path", "")
if not path:
    sys.exit(0)
norm = path.replace("\\", "/")

for pattern, label in PROTECTED:
    if re.search(pattern, norm, re.I):
        try:
            if not os.path.exists(path) or os.path.getsize(path) == 0:
                sys.exit(0)  # a new or empty file is safe to write
        except OSError:
            sys.exit(0)
        sys.stderr.write(
            f"BLOCKED: Write would replace an existing {label} ({os.path.basename(path)}). "
            "It's append-only and other sessions may have added to it since you read it. "
            "Read it again now, then use Edit to add your new section after the last line.\n"
        )
        sys.exit(2)

sys.exit(0)
