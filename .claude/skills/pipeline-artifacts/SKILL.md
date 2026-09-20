---
name: pipeline-artifacts
description: Publish or refresh the Claude Artifact pages that mirror job-pipeline state — a page per role document (fit assessments from role-fit, one interview-prep page per stage from interview-prep), and the pipeline board that mirrors job-pipeline/overview.md with every published page linked in each role's File column. Not a menu option; invoked by role-fit, interview-prep, or any other skill that writes a document under job-pipeline/ or changes overview.md, so there's always a shareable link in sync with the files on disk. Triggers on "publish the fit assessment", "publish the prep doc", "publish/update the pipeline board", or another skill needing an artifact refresh after writing to job-pipeline/.
---

# Pipeline Artifacts

Turns `job-pipeline/` files into Claude Artifacts. The board this skill publishes is the **only** place pipeline state is ever displayed — nothing in this project prints the pipeline into the terminal, so a failure here means the user sees nothing and must be told plainly rather than handed a retyped table. This skill owns no content of its own — the caller owns the underlying files, decides what changed, and invokes this skill to publish it. This skill only renders and (re)publishes.

Two operations. Run only the one asked for.

## Operation 1 — publish a role document page

Called right after another skill has written or rewritten a markdown document in `job-pipeline/applications/<company-slug>/`. Two kinds go through here:

- **`fit-assessment.md`** — written by `role-fit`.
- **`interview-prep-<stage>.md`** — written by `interview-prep`, one page per stage. Each stage gets its own artifact and its own URL; a later stage never overwrites an earlier one.

Needs: the path to that file.

1. Read the markdown.
2. Render it as an Artifact page: same sections, same order as the source — a readable document, not a redesign of the content. Follow the `artifact-design` skill: real typographic hierarchy, not a card-heavy or dashboard treatment. Keep one visual system across every page in this project so a fit assessment and a prep doc read as the same family — the reader moves between them constantly.
   - For a **fit assessment**: verdict up top, the gap table as an actual table.
   - For an **interview-prep doc**: the stage, date and duration up top; the questions as a scannable list, since this page gets read on a phone minutes before a call; expected questions and questions-to-ask visually distinct from one another; the pre-drafted gap lines given their own emphasis, because they are the part the user needs to find in three seconds under pressure.
3. URL tracking, so an updated document updates one page instead of multiplying links: the sibling file `<same-name-without-.md>-artifact-url.txt` next to the markdown, inside the same company folder (e.g. `job-pipeline/applications/acme/fit-assessment.md` → `acme/fit-assessment-artifact-url.txt`, and `acme/interview-prep-hr-screen.md` → `acme/interview-prep-hr-screen-artifact-url.txt`). If that file exists, read the URL inside and pass it as `url` to the Artifact tool. If not, publish fresh and write the returned URL into that file.
4. Return the URL to the caller in one line, and say whether it was a new page or an update to an existing one.

## Operation 2 — publish the pipeline board

Called right after `job-pipeline/overview.md` has changed.

1. Read `job-pipeline/overview.md`.
2. For each row, list that company's `applications/<company-slug>/` folder and collect **every** `*-artifact-url.txt` in it, not just the fit assessment. Render the **File** column as one labelled link per published page, in a stable order: the fit assessment first, then the interview-prep pages in stage order (recruiter/HR screen, hiring manager, technical, panel, final). Label each by what it is — "Fit assessment", "Prep: HR screen", "Prep: technical" — derived from the filename, so a row with four documents is still scannable. Keep the labels short; the column is narrow.
   If a row has no published artifact yet, fall back to a plain, non-linked tag showing the filename from the index. If a role file exists on disk but its page has never been published, that is worth one line to the user rather than silently leaving the row bare.
3. Render the three tables (Active, Considering, Closed) — same rows, columns, and sort as `overview.md` (newest `As of` first). Follow the `artifact-design` skill: this is a status dashboard, keep it clean and utilitarian, not hero-driven.
4. URL tracking: `job-pipeline/.pipeline-artifact-url`. Read it first and redeploy to that URL if present; otherwise publish fresh and write the returned URL there.
5. Share the resulting link with the user directly, in your own reply — don't bury it, and don't skip this because the change felt minor. Unlike Operation 1 (where the URL just goes back to the caller to use as it sees fit), the pipeline board link is the thing the user actually wants handed to them, and it is the whole answer: the link, not the link plus a summary of what's on it.
6. If the publish fails, say so and why. Never substitute the markdown tables into the reply as a consolation — the user has explicitly given up on terminal pipeline output.

## What this skill never does

- Never writes to the content of the markdown under `job-pipeline/` — it only reads what's already there and republishes the rendered view. A stale or wrong source file is the calling skill's problem to fix first, not something to paper over here.
- Never invents a row, status, or verdict that isn't present in the file being mirrored.
- Never pastes the pipeline tables, or a prose digest of them, into the conversation. The page is the output; the link is the delivery.
