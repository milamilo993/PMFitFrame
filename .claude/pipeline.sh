#!/usr/bin/env bash
# Render the job pipeline. Run from anywhere:  bash .claude/pipeline.sh
# Handles its own path resolution so the caller never needs to quote or escape.
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1
exec python3 .claude/show-pipeline.py "$@"
