#!/bin/bash
# Reminds Claude to reindex the journal search after writing
# to an indexed directory.
# PostToolUse hook for Write/Edit. Sync (fast path check).
# Emits hookSpecificOutput JSON so additionalContext
# actually reaches Claude (plain stdout would only land
# in the transcript, not the model's view).
#
# Two things to set for your setup:
#   INDEXED  the folder(s) your search index covers, as a grep -E
#            pattern matched against the file path (forward slashes).
#            The original watches several folders inside one journal
#            root, e.g. "journal/(entries|decisions)/".
#   MSG      what Claude should run to rebuild the index. The
#            original names its search server's reindex tool.
#
# Test it after installing. This one reminds rather than blocks, so the
# first should print a JSON line containing the reminder, the second nothing:
#   echo '{"tool_input":{"file_path":"/x/journal/2026-01-01.md"}}' | bash ~/.claude/hooks/reindex-journal.sh
#   echo '{"tool_input":{"file_path":"/x/notes/todo.md"}}' | bash ~/.claude/hooks/reindex-journal.sh

INDEXED="journal/"
MSG="REMINDER: You just wrote to an indexed journal directory. Call reindex_journal to update the search index."

LOG="$HOME/.claude/hooks/hook-log.txt"

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | python -c "import sys,json; print(json.load(sys.stdin).get('tool_input',{}).get('file_path',''))" 2>/dev/null)

if [ -z "$FILE_PATH" ]; then
  exit 0
fi

# Normalize backslashes for cross-separator matching.
NORM_PATH=$(echo "$FILE_PATH" | sed 's|\\|/|g')

# Only fire for indexed directories
if echo "$NORM_PATH" | grep -qE "$INDEXED"; then
  echo "$(date '+%Y-%m-%d %H:%M') | reindex-journal | FIRED: $FILE_PATH" >> "$LOG"

  python -c "
import json, sys
print(json.dumps({
  'hookSpecificOutput': {
    'hookEventName': 'PostToolUse',
    'additionalContext': sys.argv[1],
  }
}))
" "$MSG"
fi

exit 0
