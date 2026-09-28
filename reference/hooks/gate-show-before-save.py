#!/usr/bin/env python
"""PreToolUse gate: Claude has to show you a memory or instruction change before writing it.

Kit note: a portable, simplified version of a live hook. Later shelf. The moment for it:
you find a memory entry, or a line in your CLAUDE.md or rules, that you never approved.
Wire it on the Write|Edit matcher (see settings-hooks-example.json).

Why a hook: the seed adds a line to your CLAUDE.md asking Claude to show you any memory
entry before saving it. That line is an instruction, and instructions slip, especially
mid-task. In the source harness it slipped often enough that this gate was built. Auto
memory saves on its own by default, so without either one, the harness slowly fills with
Claude's guesses about you.

What it guards (Write or Edit into any of these):
  ~/.claude/CLAUDE.md, ~/.claude/rules/, and every project's auto memory folder
  (~/.claude/projects/<project>/memory/).

How the yes works: Claude shows you the exact text in chat. After you say yes, Claude writes
a one-time marker, then makes the write:
  ~/.claude/hooks/state/shown-ok.txt   containing:   <part of the file path> <unix seconds>
The marker is good for 10 minutes and one write, then it's used up. It doesn't prove you saw
anything (Claude writes it), but it forces the show-and-ask step into the flow, which is the
step that was being skipped.

Known gap: it only watches Claude's Write and Edit tools. A shell command that writes to
one of these files (echo >>, a script) gets past it.

Test it after installing (the first should print BLOCKED and exit 2, the second pass):
  echo '{"tool_input":{"file_path":"'$HOME'/.claude/CLAUDE.md"}}' | python ~/.claude/hooks/gate-show-before-save.py; echo "exit $?"
  echo '{"tool_input":{"file_path":"'$HOME'/notes.md"}}' | python ~/.claude/hooks/gate-show-before-save.py; echo "exit $?"
"""
import json
import os
import re
import sys
import time

HOME = os.path.expanduser("~").replace("\\", "/")
MARKER = os.path.join(HOME, ".claude", "hooks", "state", "shown-ok.txt")
WINDOW_S = 600

GUARDED = [
    re.compile(r"/\.claude/CLAUDE\.md$", re.I),
    re.compile(r"/\.claude/rules/", re.I),
    re.compile(r"/\.claude/projects/[^/]+/memory/", re.I),
]


def marker_allows(path):
    """True if a fresh marker names part of this path. Uses the marker up either way."""
    try:
        with open(MARKER, encoding="utf-8") as f:
            parts = f.read().strip().rsplit(" ", 1)
        os.remove(MARKER)
        if len(parts) != 2:
            return False
        fragment, stamp = parts[0].replace("\\", "/"), float(parts[1])
        return fragment.lower() in path.lower() and time.time() - stamp <= WINDOW_S
    except (OSError, ValueError):
        return False


try:
    data = json.load(sys.stdin)
    path = data.get("tool_input", {}).get("file_path", "").replace("\\", "/")
    if not path or not any(g.search(path) for g in GUARDED):
        sys.exit(0)
    if marker_allows(path):
        sys.exit(0)
    sys.stderr.write(
        "BLOCKED: this changes the user's memory or always-loaded instructions "
        f"({os.path.basename(path)}). Show them the exact text in chat first. After they "
        "say yes, write the marker file ~/.claude/hooks/state/shown-ok.txt containing "
        "'<part of the path> <current unix seconds>' and retry. Don't write the marker "
        "without their yes.\n"
    )
    sys.exit(2)
except SystemExit:
    raise
except Exception:
    sys.exit(0)  # a bug in the gate must never block real work
