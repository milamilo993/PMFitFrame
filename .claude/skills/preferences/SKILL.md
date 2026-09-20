---
name: preferences
description: Build or update pm-profile/preferences.md — the user's target level, compensation floor, geography, office pattern, urgency and deal-breakers, turned into screening rules every assessment applies mechanically. Invoked by role-fit, tailor-resume, cover-letter or interview-prep when the file is missing, or by name when the user wants to change what they are looking for ("update my preferences", "my comp floor changed", "I'd relocate now").
---

# Preferences

Writes `pm-profile/preferences.md`: what the user wants out of the next role, in a form other skills can screen against without re-asking. Counterpart to `competencies` — that skill establishes what the user *is*, this one establishes what they are *looking for*.

Without this file, every assessment has the same hole: compensation, location scope, role shape and deal-breakers all collapse into "unassessable, flag don't guess". That is honest and useless, and it reopens on the next role.

## When this runs

- A skill that judges a role against the profile (`role-fit`, `tailor-resume`, `cover-letter`, `interview-prep`) found the file missing and the user said yes to building it.
- The user asks for it by name, or says something that changes a stated preference — a new comp floor, a new location, a deal-breaker that has stopped mattering.

If `pm-profile/competencies.md` does not exist either, run the `competencies` skill first: this file restates the target level in its Role section, and `competencies` is where the level vocabulary (`<level-slug>`) is established from the CV.

## 1. Read first

- `pm-profile/cv.md` — current role, market, seniority, so the question options are concrete rather than generic.
- The **Level** section of `pm-profile/competencies.md` for the current `<level-slug>` and target level if one is already set. Never re-derive the level here.
- An existing `pm-profile/preferences.md`, when this is an update rather than a first build. Change what the user actually changed; do not rewrite the rest from memory.

## 2. Ask the eight questions

The *offer* that leads here is always one line of plain text — a missing profile file is one thing to say yes or no to, and no skill in this project fires a picker to ask whether to build it. These eight questions are the opposite case: the user has already said yes, and each one has real options worth showing rather than typing out.

Use the `AskUserQuestion` tool in two batches of four — the tool takes at most four per call. Give concrete options rather than open prompts, drawn from the user's actual market and what this search has already surfaced.

**Batch 1 — the role itself**

1. Total-compensation floor, in the currency of the market being searched, as bands.
2. Role shape: senior/staff IC, tech lead, people manager, product-facing — in the `<level-slug>` vocabulary `competencies` uses.
3. Domain direction — multi-select, so "would take either" is expressible.
4. Company stage and size — multi-select.

**Batch 2 — the constraints**

5. Geography: which locations the job may be in, including remote-from-home-country — multi-select.
6. Office time tolerated: hybrid days, remote preferred, remote only, full-time office.
7. Urgency: actively looking, open but not urgent, mapping the market, must leave soon.
8. Deal-breakers — multi-select, drawn from what the search has actually surfaced (a language requirement, on-call load, no AI/ML content, delivery work dressed as product, any pay cut).

## 3. Write the file

Draft `pm-profile/preferences.md` with the answers **as stated** — this file records what the user said, not what you would advise. Sections:

- **Role** — shape and domains, carrying `**Target level:** <level-slug>` explicitly.
- **Compensation** — the floor, and what it is measured on (base + bonus + equity, which market's terms).
- **Location and working pattern.**
- **Urgency.**
- **Deal-breakers** — stated plainly, numbered.
- **Screening rules** — the same answers turned into mechanical tests a future assessment applies without interpretation, numbered `R1`, `R2`, … Each names the input it checks and the action: screen out, flag, or ask before investing further. This section is the point of the file; a preference with no rule attached gets quietly ignored six roles later.
- **Tensions** — any answers that genuinely conflict, named rather than smoothed over: a comp floor that rules out the stage they picked, "open to relocating" alongside a single-city geography, a target domain that sits on an unrated competency pillar.

**Rule 6 of `CLAUDE.md` applies**: show the draft and get a yes before writing. This is `pm-profile/`, and only `cv-intake` is exempt.

## 4. Close the loop

Two things straight after writing it:

- **Re-check the work in progress.** If a skill invoked this one mid-assessment, re-run its screening against the new rules before publishing anything. A comp floor or a deal-breaker can turn a conditional apply into a do-not-apply — that is the whole reason for having asked.
- **Re-check what is already on the board.** If a newly stated deal-breaker contradicts a verdict recorded earlier, say so and offer to revise that assessment, rather than leaving the pipeline asserting something the profile now contradicts. Do not rewrite it silently.

If the user declines to build the file, proceed without it, keep flagging the specific gaps it would have closed, and do not ask again in the same session.
