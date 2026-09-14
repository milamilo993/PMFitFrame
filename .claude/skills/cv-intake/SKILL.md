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

Show the user a five-line summary first — name, current title, number of roles detected, date range, word count — and get a yes. This satisfies rule 6 of `CLAUDE.md` without dumping the whole CV back at them.

On yes, write:

- `pm-profile/cv.md` — the extracted text, lightly cleaned: real headings, roles in reverse-chronological order, bullets preserved. Do not rewrite, summarise, improve, or reorder the user's wording. This is a transcription, not an edit.

## Step 5 — resume the flow

Immediately, in the same response, without waiting for another message:

1. One line confirming what was saved, by filename.
2. One line on whether `competencies.md` or `preferences.md` is still missing and why each would help.
3. The four-option menu from `CLAUDE.md`, verbatim.

The user is onboarded from this point in the session. Do not consult the boot `STATE:` line again — it was computed before the CV existed and is now stale.
