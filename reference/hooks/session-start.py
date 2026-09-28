#!/usr/bin/env python
"""SessionStart hook: tell Claude where you left off, and prove your guards still work.

Kit note: later shelf. The moment for it: the two-week check-in. By then there's a handoff
and a journal to resume from, and guards worth re-testing. Set JOURNAL_DIR and GUARDS below,
then wire it on the SessionStart event (see settings-hooks-example.json).
The idea came from the first person this kit was handed to, whose Claude built one like it.

Why a hook: /pickup does the "where was I?" job, but only when someone remembers to run it.
And a guard that crashes, or loses its settings.json entry, stops blocking without a word.
This runs at the start of every session, so neither depends on anyone remembering.

What it prints (Claude sees it as context before its first reply; keep it short, because
it's paid for every session):
  - whether this folder has a HANDOFF.md, and how old it is
  - your newest journal entry, and how old it is
  - for each guard: is it wired in settings.json, and does it block its test command?

Hard limit: it never prints more than MAX_LINES lines, and it never fails the session.
Resist adding project-specific checks here; that's how these hooks grow until they're noise.

Test it after installing (it should print a short "[harness]" block and exit 0):
  echo '{"source":"startup"}' | python ~/.claude/hooks/session-start.py; echo "exit $?"
"""
import json
import os
import shutil
import subprocess
import sys
import time

MAX_LINES = 8
JOURNAL_DIR = "<your journal folder>"   # e.g. ~/notes/journal ; leave as-is to skip
HOOKS = os.path.join(os.path.expanduser("~"), ".claude", "hooks")
SETTINGS = os.path.join(os.path.expanduser("~"), ".claude", "settings.json")

# Each installed guard, with one command it must block. Remove any you didn't install.
GUARDS = [
    ("deny-destructive.sh", "git reset --hard HEAD~1"),
    ("deny-credential-paths.py", "git add .env"),
    ("deny-git-add-all.py", "git add -A"),
    # ("confirm-push.py", "git push origin main"),   # if you installed the push gate
]


def age(path):
    days = (time.time() - os.path.getmtime(path)) / 86400
    return "today" if days < 1 else f"{int(days)} day{'s' if int(days) != 1 else ''} ago"


def guard_line():
    try:
        settings = open(SETTINGS, encoding="utf-8").read()
    except OSError:
        settings = ""
    ok, problems = 0, []
    for name, bad in GUARDS:
        script = os.path.join(HOOKS, name)
        if not os.path.exists(script):
            problems.append(f"{name} is missing")
            continue
        if name not in settings:
            problems.append(f"{name} isn't wired in settings.json")
            continue
        # On Windows a bare "bash" can start WSL's bash (System32 is searched before PATH), which
        # can't see C:/ paths; shutil.which uses PATH like a terminal does. Forward slashes because
        # Git's bash reads backslashes as escapes.
        runner = ([shutil.which("bash") or "bash", script.replace("\\", "/")] if name.endswith(".sh")
                  else [sys.executable, script])
        try:
            r = subprocess.run(runner, input=json.dumps({"tool_input": {"command": bad}}),
                               capture_output=True, text=True, timeout=5)
            if r.returncode == 2:
                ok += 1
            else:
                problems.append(f"{name} did NOT block its test command")
        except Exception:
            problems.append(f"{name} couldn't run")
    if not GUARDS:
        return None
    if not problems:
        return f"Guards: all {ok} wired and blocking their test commands."
    return ("WARNING, guards: " + "; ".join(problems) +
            ". Tell the user before doing anything risky, and offer to fix it.")


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}
    cwd = data.get("cwd") or os.getcwd()
    lines = ["[harness] session start"]

    handoff = os.path.join(cwd, "HANDOFF.md")
    if os.path.exists(handoff):
        lines.append(f"This folder has a HANDOFF.md, updated {age(handoff)}. Read it before starting work here.")

    jdir = os.path.expanduser(JOURNAL_DIR)
    if "<" not in JOURNAL_DIR and os.path.isdir(jdir):
        entries = [os.path.join(jdir, f) for f in os.listdir(jdir) if f.endswith(".md")]
        if entries:
            newest = max(entries, key=os.path.getmtime)
            lines.append(f"Newest journal entry: {os.path.basename(newest)} ({age(newest)}).")

    g = guard_line()
    if g:
        lines.append(g)

    print("\n".join(lines[:MAX_LINES]))


try:
    main()
except Exception:
    pass  # a broken check must never block or slow the session
sys.exit(0)
