---
name: cv-intake
description: Take in the user's CV in any form - a PDF, DOCX, DOC, Pages, RTF, TXT or MD file attached to the chat or dropped in the folder, or resume text pasted straight into the message - extract the text, save it to pm-profile/, and resume the onboarding flow. Use whenever the user supplies a CV or resume for the first time, replaces the one on file, or pastes something that reads like a resume.
---
# CV intake

Turn whatever the user hands you into one canonical text file at `pm-profile/cv.md`, keep the original alongside it, then pick the flow back up. Every other skill reads `cv.md` — nothing else should ever have to parse a PDF again.

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

Then tell the user, in one line each, where it landed — the file paths — followed by a short extraction summary: name, current title, number of roles detected, date range, word count, and the deduced `<level-slug>` from Step 4b. This is a report, not a request: never wait for a yes before saving.

Replacing a CV already on file is the exception: `cv.md` existing means other skills have been built on it, so confirm before overwriting.

## Step 4b — deduce the level and record it as `<level-slug>`

The CV is the only place seniority can be read from evidence rather than aspiration, so derive it here, once, and let every other skill reuse it. This is the project's `<level-slug>`.

**The vocabulary.** Exactly one of these. Do not invent a variant; if none fits, pick the closest and say why in the evidence line.

| Slug | Reads as |
| --- | --- |
| `junior-ic` | 0–2 years, executing defined tasks |
| `mid-ic` | 2–5 years, owns features end to end |
| `senior-ic` | Owns a domain, makes trade-offs unsupervised, mentors informally |
| `staff-ic` | Influence across teams, sets patterns others follow, no headcount |
| `principal-ic` | Sets technical direction at org level |
| `tech-lead` | Hands-on, owns a team's technical direction and delivery |
| `eng-manager` | Headcount, hiring, performance, mostly out of the code |
| `senior-manager` | Manages managers or several teams |
| `director-plus` | Org-level leadership, budget, strategy |

**How to deduce it.** Weigh these in order, and let the strongest evidence win rather than averaging:

1. **The current title, taken literally.** A "Senior Software Engineer" is `senior-ic` until something outweighs it. Title inflation and deflation both exist, so it is evidence, not proof.
2. **Scope described in the bullets.** Cross-team or platform-wide ownership, patterns others adopt, being the named DRI for an org's standards — those are `staff-ic` signals even under a senior title. Owning one service is not.
3. **Headcount.** Direct reports, hiring, performance management move it to the manager track. A team supervised on a project does not.
4. **Years, as a sanity check only.** Fifteen years in a `mid-ic` slug is a signal you have misread the scope, not evidence for the slug.

**What to write.** Create `pm-profile/level.md`:

```markdown
# Level

- **Current:** <level-slug>
- **Target:** unknown — set from `preferences.md` when the user states what they want next

## Evidence
- <the title and dates it comes from>
- <the scope signal that confirmed or overrode the title>

## Notes
Deduced by `cv-intake` from `cv.md` on <date>. Override by editing this file; every skill
reads it rather than re-deriving, so a correction here propagates everywhere.
```

**Current versus target matters.** `cv-intake` can only establish *current* level, because the CV is history. Target level comes from what the user says they want, and lives in `preferences.md`. Keep them separate: a `senior-ic` aiming at `staff-ic` is a different search from a `senior-ic` who wants to stay put, and conflating them produces bad verdicts in both directions.

**Say it out loud.** Add the slug to the extraction summary in Step 4 as one extra line, and say it is a deduction the user can correct. Getting this wrong quietly miscalibrates every later assessment, so it is worth the one line.

**Who consumes it.** Do not explain the mechanism to the user, just record it. For your own reference:

- `preferences.md` carries `**Target level:** <level-slug>` in its Role section.
- `competencies.md` carries `**Level:** <level-slug>` in its header, so pillar self-ratings are read against the right bar.
- `role-fit` compares the posting's implied level against `<level-slug>` and flags a mismatch in either direction.
- `interview-prep` holds the grading bar at `<level-slug>` rather than at a hardcoded seniority.

## Step 5 — resume the flow

Immediately, in the same response, without waiting for another message:

1. One line confirming what was saved, by filename.
2. One line on whether `competencies.md` or `preferences.md` is still missing and why each would help.
3. The six-option menu from `CLAUDE.md`, verbatim.

The user is onboarded from this point in the session. Do not consult the boot `STATE:` line again — it was computed before the CV existed and is now stale.
