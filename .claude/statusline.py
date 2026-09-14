#!/usr/bin/env python3
"""Statusline: model | ctx <in>/<out> | $cost.

Reads the statusline JSON payload on stdin and walks the session transcript
(JSONL) backwards for the most recent `message.usage` block. Stdlib only —
jq is not installed on this machine, which is why the old shell version
printed an empty model and a dash for tokens.
"""
import json
import os
import sys


def human(n):
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}k"
    return str(n)


def latest_usage(path):
    """Last line in the transcript carrying a message.usage block."""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            lines = fh.readlines()
    except OSError:
        return None
    for line in reversed(lines):
        line = line.strip()
        if not line or '"usage"' not in line:
            continue
        try:
            usage = (json.loads(line).get("message") or {}).get("usage")
        except (ValueError, AttributeError):
            continue
        if usage:
            return usage
    return None


def main():
    try:
        payload = json.load(sys.stdin)
    except ValueError:
        payload = {}

    model = ((payload.get("model") or {}).get("display_name")) or "claude"
    cost = (payload.get("cost") or {}).get("total_cost_usd") or 0.0
    transcript = payload.get("transcript_path") or ""

    tok = "—"
    if transcript and os.path.isfile(transcript):
        usage = latest_usage(transcript)
        if usage:
            inp = (
                (usage.get("input_tokens") or 0)
                + (usage.get("cache_read_input_tokens") or 0)
                + (usage.get("cache_creation_input_tokens") or 0)
            )
            tok = f"{human(inp)} in / {human(usage.get('output_tokens') or 0)} out"

    try:
        cost = float(cost)
    except (TypeError, ValueError):
        cost = 0.0

    sys.stdout.write(f"{model} | ctx {tok} | ${cost:.4f}")


if __name__ == "__main__":
    main()
