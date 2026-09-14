#!/usr/bin/env bash
# Claude Code statusline: shows live token usage for the session.
# Reads the statusline JSON payload on stdin, then pulls the most recent
# `usage` block out of the session transcript (JSONL) to compute tokens.
# Uses python3 rather than jq — jq is not installed on this machine.
exec python3 "$(dirname "${BASH_SOURCE[0]}")/statusline.py"
