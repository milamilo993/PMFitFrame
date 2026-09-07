#!/usr/bin/env bash
# SessionStart hook. Runs at session start, before the user types anything.
# Does the pm-profile check itself so the model never needs a tool call,
# and so the branch is decided by code, not by model judgement.
cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/..}" 2>/dev/null || true
echo "$(date +%FT%T) fired (cwd=$PWD src=${CLAUDE_SESSION_ID:-?})" >> .claude/boot.log

shopt -s nullglob nocaseglob
all=(pm-profile/*)
cv=(pm-profile/*cv* pm-profile/*resume*)

# Fallback: any document that isn't competencies/preferences counts as a CV.
if [ ${#cv[@]} -eq 0 ]; then
  for f in "${all[@]}"; do
    case "${f,,}" in
      */competencies.md|*/preferences.md) ;;
      *.pdf|*.docx|*.md|*.txt|*.rtf|*.pages) cv+=("$f") ;;
    esac
  done
fi
shopt -u nocaseglob

echo "=== BOOT PROTOCOL (already executed — do NOT run \`ls\` yourself) ==="
if [ ${#cv[@]} -eq 0 ]; then
  echo "STATE: no CV on file."
  echo "ACTION: your first response this session must be exactly this line, nothing before or after it, then stop:"
  echo
  echo "Hi, I am your job assistant please submit the CV at least to get started but ideally competencies and preferences and context as I work better with it"
else
  echo "STATE: returning user."
  echo "ON FILE: ${cv[*]##*/}"
  missing=()
  [ -f pm-profile/competencies.md ] || missing+=("competencies.md")
  [ -f pm-profile/preferences.md ]  || missing+=("preferences.md")
  if [ ${#missing[@]} -gt 0 ]; then
    echo "MISSING: ${missing[*]}"
  else
    echo "MISSING: none"
  fi
  echo "ACTION: open your first response with one line naming the file(s) on file, one line on anything MISSING and why it helps, then the 4-option menu from CLAUDE.md verbatim. Then answer the user's message if it contained a real request."
fi
echo "REMINDER: no git, no directory scanning, no recap, no preamble."
