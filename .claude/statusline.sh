#!/usr/bin/env bash
# Claude Code statusline: shows live token usage for the session.
# Reads the statusline JSON payload on stdin, then pulls the most recent
# `usage` block out of the session transcript (JSONL) to compute tokens.
input=$(cat)

model=$(printf '%s' "$input" | jq -r '.model.display_name // "claude"')
cost=$(printf '%s' "$input" | jq -r '.cost.total_cost_usd // 0')
transcript=$(printf '%s' "$input" | jq -r '.transcript_path // empty')

tok="—"
if [ -n "$transcript" ] && [ -f "$transcript" ]; then
  tok=$(tac "$transcript" 2>/dev/null || tail -r "$transcript") 
  tok=$(printf '%s' "$tok" | jq -rs '
    map(select(.message?.usage != null))
    | if length == 0 then "—" else
        (.[0].message.usage) as $u
        | (($u.input_tokens // 0)
          + ($u.cache_read_input_tokens // 0)
          + ($u.cache_creation_input_tokens // 0)) as $in
        | "\($in) in / \($u.output_tokens // 0) out"
      end' 2>/dev/null || echo "—")
fi

printf '%s | ctx %s | $%.4f' "$model" "$tok" "$cost"
