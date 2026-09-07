#!/usr/bin/env python3
"""Render job-pipeline/overview.md as a colourised terminal table.

Usage:  python3 .claude/show-pipeline.py [path-to-pipeline.md]

Reads the markdown index, keeps whatever columns each table actually has,
and prints it with status colouring, age tracking and overdue highlighting.
Degrades to plain text when piped, when NO_COLOR is set, or on a dumb TERM.
"""
import os
import re
import sys
import shutil
import datetime as dt
from pathlib import Path

# ---------------------------------------------------------------- colour

# Colour is ON by default, including when stdout is a pipe -- the Claude Code
# transcript renders ANSI but is not a tty, and isatty() gating made it grey.
NOCOLOR = bool(os.environ.get("NO_COLOR")) or "--no-color" in sys.argv
COLOR = not NOCOLOR
TRUE = os.environ.get("COLORTERM", "") in ("truecolor", "24bit") or sys.platform == "darwin"


def fg(r, g, b):
    if not COLOR:
        return ""
    if TRUE:
        return f"\033[38;2;{r};{g};{b}m"
    return f"\033[38;5;{16 + 36 * (r // 51) + 6 * (g // 51) + (b // 51)}m"


def bg(r, g, b):
    if not COLOR:
        return ""
    if TRUE:
        return f"\033[48;2;{r};{g};{b}m"
    return f"\033[48;5;{16 + 36 * (r // 51) + 6 * (g // 51) + (b // 51)}m"


RESET = "\033[0m" if COLOR else ""
BOLD = "\033[1m" if COLOR else ""
DIM = "\033[2m" if COLOR else ""
ITAL = "\033[3m" if COLOR else ""

INK = fg(228, 228, 232)
MUTE = fg(128, 132, 145)
RULE = fg(72, 76, 88)
HEAD = fg(158, 206, 255)

# status -> (label ink, pill background)
STATUS = {
    "Offer":        (fg(12, 30, 12), bg(126, 231, 135)),
    "Final":        (fg(10, 26, 30), bg(122, 220, 226)),
    "Interviewing": (fg(10, 26, 30), bg(103, 196, 214)),
    "Screening":    (fg(8, 20, 34), bg(126, 174, 235)),
    "Applied":      (fg(32, 26, 6), bg(240, 200, 96)),
    "Drafting":     (fg(28, 14, 32), bg(206, 154, 236)),
    "Outreach":     (fg(28, 14, 32), bg(184, 148, 226)),
    "Shortlisted":  (fg(16, 16, 18), bg(198, 200, 208)),
    "Passed":       (MUTE, ""),
    "Rejected":     (fg(34, 10, 10), bg(232, 118, 118)),
    "Declined":     (fg(32, 20, 8), bg(214, 160, 110)),
    "Withdrawn":    (fg(32, 20, 8), bg(200, 158, 120)),
    "Lapsed":       (MUTE, ""),
    "Expired":      (MUTE, ""),
}
ACCENT = {"Active": fg(126, 231, 135), "Considering": fg(240, 200, 96), "Closed": MUTE}

TODAY = dt.date.today()
LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
DATE = re.compile(r"(\d{4}-\d{2}-\d{2})")
ANSI = re.compile(r"\033\[[0-9;]*m")


def plain(s):
    return ANSI.sub("", s)


def pad(s, w, right=False):
    gap = " " * max(0, w - len(plain(s)))
    return gap + s if right else s + gap


def clip(s, w):
    return s if len(s) <= w else s[: max(0, w - 1)] + "…"


# ---------------------------------------------------------------- parse


def parse(text):
    sections, cur = [], None
    for line in text.splitlines():
        if line.startswith("## "):
            title = line[3:].strip()
            key = re.split(r"[\s—-]", title, 1)[0].strip() or title
            cur = {"key": key, "title": title, "cols": [], "rows": []}
            sections.append(cur)
            continue
        if cur is None or not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(set(c) <= set("-: ") and c for c in cells):
            continue
        cells = [LINK.sub(r"\1", c) for c in cells]
        if not cur["cols"]:
            cur["cols"] = cells
        else:
            cur["rows"].append(cells)
    return [s for s in sections if s["cols"]]


def age(datestr):
    m = DATE.search(datestr or "")
    if not m:
        return None
    try:
        return (TODAY - dt.date.fromisoformat(m.group(1))).days
    except ValueError:
        return None


# ---------------------------------------------------------------- render


def render(sections, title, updated, width):
    out = []
    bar = RULE + "─" * width + RESET
    out.append("")
    out.append(f"  {BOLD}{HEAD}{title}{RESET}" + (f"   {DIM}{updated}{RESET}" if updated else ""))
    out.append(bar)

    for sec in sections:
        cols = sec["cols"]
        rows = sec["rows"]
        acc = ACCENT.get(sec["key"], INK)
        idx = {c.lower(): i for i, c in enumerate(cols)}
        i_status, i_asof = idx.get("status"), idx.get("as of")
        i_next, i_file = idx.get("next action"), idx.get("file")

        # decorate: age tag on "As of", overdue flag on "Next action"
        body = []
        for r in rows:
            r = list(r) + [""] * (len(cols) - len(r))
            d = age(r[i_asof]) if i_asof is not None else None
            if d is not None:
                stale = (r[i_status] if i_status is not None else "") == "Applied" and d > 60
                tag = f" {fg(232,118,118)}{d}d!{RESET}" if stale else f" {DIM}{d}d{RESET}"
                r[i_asof] = r[i_asof] + tag
            if i_next is not None and (nd := age(r[i_next])) is not None and nd >= 0:
                r[i_next] = f"{fg(232,118,118)}{r[i_next]}{RESET}"
            body.append(r)

        # widths, dropping low-value columns until it fits
        keep = list(range(len(cols)))
        while True:
            w = [max(len(plain(cols[i])), *(len(plain(r[i])) for r in body)) if body
                 else len(plain(cols[i])) for i in keep]
            w = [min(x, 34) for x in w]
            # the status pill adds a space either side
            w = [x + 2 if keep[k] == i_status else x for k, x in enumerate(w)]
            if sum(w) + 3 * len(keep) <= width or len(keep) <= 3:
                break
            for name in ("file", "location", "next action"):
                if (j := idx.get(name)) in keep:
                    keep.remove(j)
                    break
            else:
                keep.pop()

        n = len(rows)
        out.append("")
        out.append(f"  {acc}▌{RESET}{BOLD}{acc} {sec['title']}{RESET}  {DIM}({n}){RESET}")
        out.append("  " + RULE + "─" * (width - 2) + RESET)
        if not rows:
            out.append(f"  {DIM}{ITAL}empty{RESET}")
            continue
        out.append("  " + f"{DIM}   {RESET}".join(
            f"{MUTE}{pad((' ' if i == i_status else '') + cols[i].upper(), w[k])}{RESET}"
            for k, i in enumerate(keep)))
        for r in body:
            cells = []
            for k, i in enumerate(keep):
                v = clip(r[i], w[k])
                if i == i_status:
                    ink, pill = STATUS.get(plain(v), (INK, ""))
                    v = f"{pill}{ink}{BOLD} {plain(v)} {RESET}"
                elif i == i_file:
                    v = f"{DIM}{v}{RESET}"
                else:
                    v = f"{INK}{v}{RESET}"
                cells.append(pad(v, w[k]))
            out.append("  " + f"{DIM}   {RESET}".join(cells).rstrip())
    out.append("")
    return "\n".join(out)


def render_md(sections, title, updated):
    """Markdown tables: no colour, always expanded, annotations preserved."""
    out = [f"**{title}**" + (f" — {updated}" if updated else ""), ""]
    for sec in sections:
        cols, rows = sec["cols"], sec["rows"]
        idx = {c.lower(): i for i, c in enumerate(cols)}
        i_status, i_asof, i_next = idx.get("status"), idx.get("as of"), idx.get("next action")
        out.append(f"### {sec['title']} ({len(rows)})")
        out.append("")
        if not rows:
            out += ["_empty_", ""]
            continue
        out.append("| " + " | ".join(cols) + " |")
        out.append("| " + " | ".join("---" for _ in cols) + " |")
        for r in rows:
            r = list(r) + [""] * (len(cols) - len(r))
            if i_asof is not None and (d := age(r[i_asof])) is not None:
                stale = (r[i_status] if i_status is not None else "") == "Applied" and d > 60
                r[i_asof] += f" ({d}d)" + (" **!**" if stale else "")
            if i_next is not None and (nd := age(r[i_next])) is not None and nd >= 0:
                r[i_next] += " **(overdue)**"
            out.append("| " + " | ".join(r) + " |")
        out.append("")
    return "\n".join(out)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    arg = args[0] if args else "job-pipeline/overview.md"
    p = Path(arg)
    if not p.exists():
        print(f"{DIM}no pipeline at {p}{RESET}")
        return 1
    text = p.read_text(encoding="utf-8")
    title = next((l[2:].strip() for l in text.splitlines() if l.startswith("# ")), "Job pipeline")
    updated = next((l.lstrip("> ").strip() for l in text.splitlines() if l.startswith(">")), "")
    if "--md" in sys.argv:
        print(render_md(parse(text), title, updated))
        return 0
    width = min(shutil.get_terminal_size((130, 24)).columns, 200)
    print(render(parse(text), title, updated, width))
    return 0


if __name__ == "__main__":
    sys.exit(main())
