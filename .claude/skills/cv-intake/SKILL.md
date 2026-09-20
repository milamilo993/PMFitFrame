---
name: cv-intake
description: Take in the user's CV in any form - a PDF, DOCX, DOC, Pages, RTF, TXT or MD file attached to the chat or dropped in the folder, or resume text pasted straight into the message - extract the text, deduce level, save to pm-profile/, and invoke competencies skill for Ravi Mehta assessment. Use whenever the user supplies a CV or resume for the first time, replaces the one on file, or pastes something that reads like a resume.
---
# CV intake

Turn whatever the user hands you into one canonical text file at `pm-profile/cv.md`, deduce their seniority level, keep the original alongside it, and then invoke the `competencies` skill to assess them against the Ravi Mehta framework. Every other skill reads `cv.md` and `competencies.md` — nothing else should ever have to parse a PDF or manually assess competencies again.

## Step 1 — locate the CV

Three ways it arrives. Handle whichever applies; do not ask the user to switch methods.

**Attached to the chat.** The content is already in the conversation. Use it directly — no filesystem hunting.

**Dropped in the folder.** Run `ls ./pm_profile` (allowed) and use what is there. If the user says they put it somewhere else, ask for the full path rather than searching for it — searching the disk is forbidden by rule 2 of `CLAUDE.md`.

**Pasted as text.** Treat the message body as the CV. Skip straight to Step 3.

If nothing has actually arrived yet, say so in one line and stop. Do not guess.

## Step 2 — extract the text

| Format | How |
| --- | --- |
| `.md`, `.txt` | Read directly. |
| `.pdf` | Read tool, `pages` parameter. If it comes back empty or as gibberish the PDF is a scan — see below. |
| `.docx` | `textutil -convert txt -stdout <file>` |
| `.doc` | `textutil -convert txt -stdout <file>` |
| `.rtf` | `textutil -convert txt -stdout <file>` |
| `.pages` | Try `unzip -p <file> 'QuickLook/Preview.pdf' > <tmp>.pdf` and read that. Newer Pages files often omit the preview — if it fails, stop and ask the user to export to PDF or Word. Do not attempt to decode the raw Pages format. |

`textutil` is macOS-native, so there is nothing to install.

**Scanned PDFs.** If extraction yields no usable text, say exactly that and ask for a text-bearing version. Do not invent content from a filename, and do not describe the layout as if it were the content.

## Step 3 — sanity-check before saving

Extraction fails quietly more often than it fails loudly. Before writing, confirm all of:

- More than ~200 words. A shorter result usually means a failed parse, not a short CV.
- A name and at least one contact detail are present.
- At least one role with dates is recognisable.
- No mojibake, no page furniture (`Page 1 of 3`), no ligature damage (`ﬁ`, `ﬂ`).

If any check fails, report which one in a single line and ask for a different format. A silently mangled CV poisons every skill downstream, so failing here is much cheaper than proceeding.

## Step 4 — save

Do not ask for permission. Once the Step 3 checks pass, write the files immediately — this is the one carve-out from rule 6 of `CLAUDE.md`, and it applies only to a CV arriving through this skill.

Write:

- `pm-profile/cv.md` — the extracted text, lightly cleaned: real headings, roles in reverse-chronological order, bullets preserved. Do not rewrite, summarise, improve, or reorder the user's wording. This is a transcription, not an edit.
- `pm-profile/cv-original.<ext>` — a verbatim copy of the file the user supplied. Skip when the CV arrived as pasted text.
- `pm-profile/competencies.md` — the **Level** section only, per Step 4b. The pillars below it wait for Step 6.

Then tell the user, in one line each, where it landed — the file paths — followed by a short extraction summary: name, current title, number of roles detected, date range, word count, and the deduced `<level-slug>` from Step 4b. This is a report, not a request: never wait for a yes before saving.

Replacing a CV already on file is the exception: `cv.md` existing means other skills have been built on it, so confirm before overwriting.

## Step 4b — deduce the level and record it as `<level-slug>`

The CV is the only place seniority can be read from evidence rather than aspiration, so derive it here, once, and let every other skill reuse it. This is the project's `<level-slug>`. It lives in the **Level** section at the top of `pm-profile/competencies.md`, which is why that file is created here at intake rather than waiting for Step 6.

**The vocabulary.** Exactly one of these. Do not invent a variant; if none fits, pick the closest and say why in the evidence line.

The ladder is **function-neutral** — it describes scope and headcount, not a discipline. It applies unchanged to a product manager, a designer, a data scientist or an engineer. Where a row says "direction", read it in the user's own function: technical direction for an engineer, product direction for a PM.

| Slug | Reads as |
| --- | --- |
| `junior-ic` | 0–2 years, executing defined tasks |
| `mid-ic` | 2–5 years, owns features or a product area end to end |
| `senior-ic` | Owns a domain, makes trade-offs unsupervised, mentors informally |
| `staff-ic` | Influence across teams, sets patterns others follow, no headcount |
| `principal-ic` | Sets direction at org level |
| `lead-ic` | Hands-on, owns a team's direction and delivery, no formal headcount (an engineering tech lead, a lead PM) |
| `people-manager` | Headcount, hiring, performance; manages individual contributors and is mostly out of the hands-on work |
| `senior-manager` | Manages managers or several teams |
| `director-plus` | Org-level leadership, budget, strategy |

Two of these were named for the engineering track and were renamed to stop them mislabelling non-engineering CVs: `tech-lead` is now `lead-ic`, and `eng-manager` is now `people-manager`. A profile written before that change may still carry an old slug — treat `tech-lead` as `lead-ic` and `eng-manager` as `people-manager`, and correct it when you next touch the file. A profile written before the level moved may also still have a separate `pm-profile/level.md`; fold it into `competencies.md` and delete it.

**How to deduce it.** Weigh these in order, and let the strongest evidence win rather than averaging:

1. **The current title, taken literally.** A "Senior Software Engineer" or "Senior Product Manager" is `senior-ic` until something outweighs it. Title inflation and deflation both exist, so it is evidence, not proof.
2. **Scope described in the bullets.** Cross-team or platform-wide ownership, patterns others adopt, being the named DRI for an org's standards — those are `staff-ic` signals even under a senior title. Owning one service, or one product area, is not.
3. **Headcount.** Direct reports, hiring, performance management move it to the manager track — `people-manager` when the reports are individual contributors, `senior-manager` only when they are themselves managers or span several teams. A team supervised on a project does not count, and neither does mentoring.
4. **Years, as a sanity check only.** Fifteen years in a `mid-ic` slug is a signal you have misread the scope, not evidence for the slug.

**What to write.** Create `pm-profile/competencies.md` with the **Level** section filled in and the pillars left for Step 6:

```markdown
# Competencies

## Level

- **Current:** <level-slug>
- **Target:** unknown — set in this section when the user states what they want next

### Evidence
- <the title and dates it comes from>
- <the scope signal that confirmed or overrode the title>

### Notes
Deduced by `cv-intake` from `cv.md` on <date>. Override by editing this section; every skill
reads it rather than re-deriving, so a correction here propagates everywhere.

## Pillars

*Not yet self-rated — see Step 6.*
```

Writing this much without asking is deliberate and is covered by the Step 4 carve-out: the Level section is a mechanical deduction from the CV, with the same provenance as `cv.md` itself, and every other skill needs a level to read from the moment intake finishes. The self-rated half of the file is different — the pillar ratings in Step 6 are the user's own claims, and those still need a yes.

**Current versus target matters.** `cv-intake` can only establish *current* level, because the CV is history. Target level comes from what the user says they want. Keep them distinct even though they now sit in the same section: a `senior-ic` aiming at `staff-ic` is a different search from a `senior-ic` who wants to stay put, and conflating them produces bad verdicts in both directions.

**Say it out loud.** Add the slug to the extraction summary in Step 4 as one extra line, and say it is a deduction the user can correct. Getting this wrong quietly miscalibrates every later assessment, so it is worth the one line.

**Who consumes it.** Do not explain the mechanism to the user, just record it. For your own reference:

- `competencies.md` holds it in the **Level** section, so pillar self-ratings are read against the right bar. This is the one source; nothing else stores a level of its own.
- `preferences.md` restates the target as `**Target level:** <level-slug>` in its Role section, because that is where the user states what they want next. It is a copy of the Level section's Target line, not a second opinion — update both in the same pass.
- `role-fit` compares the posting's implied level against `<level-slug>` and flags a mismatch in either direction.
- `interview-prep` holds the grading bar at `<level-slug>` rather than at a hardcoded seniority.

## Step 5 — invoke competencies skill and resume flow

Immediately, in the same response, without waiting for another message:

1. One line confirming what was saved, by filename.
2. Invoke the `competencies` skill (it will run in this response, extract from the CV, present findings, and ask for validation).
3. After competencies finishes, one line on what the profile is still missing: `preferences.md` — and why it would help (comp floor, deal-breakers, role shape).
4. The six-option menu from `CLAUDE.md`, verbatim.

The user is onboarded from this point in the session. Do not consult the boot `STATE:` line again — it was computed before the CV existed and is now stale.

## Step 6 — offer to build `preferences.md` (competencies auto-handled)

The CV says what the user has done; the competencies skill now assesses those against the Ravi Mehta framework automatically. But `preferences.md` is different — it holds what they want next (comp floor, location, deal-breakers, role shape), and without it `role-fit` cannot screen on any of those axes and falls back to "unassessable, flag don't guess"; `tailor-resume` and `cover-letter` have no guidance on what to lead with.

Do not just note that it is missing — **offer to build it right here, while the CV and competencies are fresh in context.** This is the cheapest moment in the whole project to do it.

Offer once, in one line:

> *Want me to build `preferences.md` now? Eight questions, two batches of four — about five minutes, and they gate every assessment from here on.*

If the user declines, proceed and do not ask again this session. `role-fit` will offer it again when it actually bites. If the user would rather write it by hand, say where it goes and the shape below so it stays machine-readable.

### `preferences.md`

Do not invent a parallel question set. The canonical one lives in `role-fit`, section **3b** of `.claude/skills/role-fit/SKILL.md` — read it and use it: eight questions, two `AskUserQuestion` batches of four, concrete options rather than open prompts, and the same output structure (`**Target level:** <level-slug>` in the Role section, a **Screening rules** section that turns the answers into mechanical tests, a **Tensions** section naming answers that conflict). One question set, one file format, wherever the offer is made.

The target level is the point of contact with `competencies.md`. The Level section in `competencies.md` holds `**Target:** unknown` until this conversation happens; once the role-shape answer lands, update that Target line in the same pass as writing `preferences.md`, so the two never disagree.

Rule 6 of `CLAUDE.md` applies: show the draft and get a yes before writing.
