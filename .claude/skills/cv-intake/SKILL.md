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

Then tell the user, in one line each, where it landed — the file paths — followed by a short extraction summary: name, current title, number of roles detected, date range, and word count. This is a report, not a request: never wait for a yes before saving.

**Note:** Level deduction happens after competencies assessment (Step 5), not here. The competencies skill will assess the user against the Ravi Mehta framework and deduce level based on both CV evidence and demonstrated competencies.

Replacing a CV already on file is the exception: `cv.md` existing means other skills have been built on it, so confirm before overwriting.

## Step 4b — no level deduction here

Level deduction moves to the competencies skill (Step 5), where it can be based on both CV evidence AND demonstrated competencies. This produces a more nuanced level assessment than CV titles alone. See the competencies skill documentation for the level vocabulary and deduction process.

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

If the user declines, proceed and do not ask again this session. `role-fit`, `tailor-resume`, `cover-letter` and `interview-prep` each offer it again when it actually bites. If the user would rather write it by hand, say where it goes and the shape below so it stays machine-readable.

### `preferences.md`

Do not invent a parallel question set, and do not run one here. On a yes, **invoke the `preferences` skill** — it owns the canonical flow: eight questions in two batches of four, concrete options rather than open prompts, and the output structure (`**Target level:** <level-slug>` in the Role section, a **Screening rules** section that turns the answers into mechanical tests, a **Tensions** section naming answers that conflict). One question set, one file format, wherever the offer is made.

The offer itself is one line of plain text, never an `AskUserQuestion` picker — a missing profile file is one thing to say yes or no to, not a menu of options.

The target level is the point of contact with `competencies.md`. The Level section in `competencies.md` holds `**Target:** unknown` until this conversation happens; once the role-shape answer lands, update that Target line in the same pass as writing `preferences.md`, so the two never disagree.

Rule 6 of `CLAUDE.md` applies: show the draft and get a yes before writing.
