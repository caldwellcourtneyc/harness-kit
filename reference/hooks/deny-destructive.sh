#!/bin/bash
# Blocks destructive commands before execution.
# PreToolUse hook for Bash tool.
# Exit 2 = block the command, stderr = reason shown to Claude.
#
# Uses Python for smarter matching — only checks actual
# shell commands, not content inside heredocs/strings.
#
# Test it after installing (first should print BLOCKED and exit 2, second pass silently):
#   echo '{"tool_input":{"command":"git reset --hard HEAD~1"}}' | bash ~/.claude/hooks/deny-destructive.sh; echo "exit $?"
#   echo '{"tool_input":{"command":"git status"}}' | bash ~/.claude/hooks/deny-destructive.sh; echo "exit $?"

python -c "
import sys, json, re, datetime, os

data = json.load(sys.stdin)
cmd = data.get('tool_input', {}).get('command', '')
if not cmd:
    sys.exit(0)

# Strip heredoc bodies (<<EOF...EOF, <<'EOF'...EOF)
# so we don't match patterns inside string content
stripped = re.sub(
    r'(<<\s*[\x27\"]?(\w+)[\x27\"]?[^\n]*)\n.*?\2',
    r'\1', cmd, flags=re.DOTALL
)

# Also strip content inside cat > file << patterns. Both strips keep the heredoc's OPENING
# line: the 2026-09-21 backtest found a commit-and-push chained on a heredoc opening line
# slipping past a command guard because the old regex removed the whole line, push included.
# (No backticks in these comments: this whole block is a bash double-quoted string.)
stripped = re.sub(
    r'(cat\s*>[^\n]*<<[^\n]*)\n.*?(?:ENDSCRIPT|EOF|END)',
    r'\1', stripped, flags=re.DOTALL
)

patterns = [
    (r'git\s+push\s+.*--force', 'git push --force'),
    (r'git\s+reset\s+--hard', 'git reset --hard'),
    (r'git\s+checkout\s+\.(\s|$)', 'git checkout .'),
    (r'git\s+clean\s+-f', 'git clean -f'),
    (r'git\s+branch\s+-D', 'git branch -D'),
    (r'git\s+restore\s+\.(\s|$)', 'git restore .'),
    (r'rm\s+-rf\s+/', 'rm -rf with absolute path'),
    (r'rm\s+-rf\s+\*', 'rm -rf with wildcard'),
    (r'rm\s+-rf\s+\.\.', 'rm -rf on parent directory'),
]

for pattern, label in patterns:
    if re.search(pattern, stripped):
        try:
            ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
            log = os.path.join(os.path.expanduser('~'), '.claude', 'hooks', 'hook-log.txt')
            with open(log, 'a') as f:
                f.write(f'{ts} | deny-destructive | BLOCKED: {label}\n')
        except OSError:
            pass  # logging must never turn a block into a fail-open
        print(f'BLOCKED: {label} — ask the user before running destructive commands.', file=sys.stderr)
        sys.exit(2)

sys.exit(0)
"
