---
name: pipeline-artifacts
description: Publish or refresh the Claude Artifact pages that mirror job-pipeline state — a per-role fit-assessment page, and the pipeline board that mirrors job-pipeline/overview.md. Not a menu option; invoked by role-fit (or any other skill that writes a fit-assessment file or changes job-pipeline/overview.md) whenever that content changes, so there's always a shareable link in sync with the files on disk. Triggers on "publish the fit assessment", "publish/update the pipeline board", or another skill needing an artifact refresh after writing to job-pipeline/.
---

# Pipeline Artifacts

Turns `job-pipeline/` files into Claude Artifacts. The board this skill publishes is the **only** place pipeline state is ever displayed — nothing in this project prints the pipeline into the terminal, so a failure here means the user sees nothing and must be told plainly rather than handed a retyped table. This skill owns no content of its own — the caller owns the underlying files, decides what changed, and invokes this skill to publish it. This skill only renders and (re)publishes.

Two operations. Run only the one asked for.

## Operation 1 — publish a fit-assessment page

Called right after some other skill has written or rewritten a fit-assessment markdown file in `job-pipeline/`.

Needs: the path to that file.

1. Read the fit-assessment markdown.
2. Render it as an Artifact page: same sections, same verdict, same gap table, in the same order as the source — a readable document, not a redesign of the content. Follow the `artifact-design` skill: real typographic hierarchy (verdict up top, clear section rhythm, the gap table as an actual table), not a card-heavy or dashboard treatment.
3. URL tracking, so re-assessments update one page instead of multiplying links: the sibling file `<same-name-without-.md>-artifact-url.txt` next to the markdown (e.g. `job-pipeline/001-fit-assessment.md` → `job-pipeline/001-fit-assessment-artifact-url.txt`). If that file exists, read the URL inside and pass it as `url` to the Artifact tool. If not, publish fresh and write the returned URL into that file.
4. Return the URL to the caller in one line. Whether and how it gets surfaced further (e.g. as a File-column link elsewhere) is the caller's call, not this skill's.

## Operation 2 — publish the pipeline board

Called right after `job-pipeline/overview.md` has changed.

1. Read `job-pipeline/overview.md`.
2. For each row, look for that role's fit-assessment artifact URL (the `-artifact-url.txt` sibling described in Operation 1, next to that role's fit-assessment file). Use it as the row's **File**-column link. If no such artifact exists yet, fall back to a plain, non-linked tag showing the filename from the index.
3. Render the three tables (Active, Considering, Closed) — same rows, columns, and sort as `overview.md` (newest `As of` first). Follow the `artifact-design` skill: this is a status dashboard, keep it clean and utilitarian, not hero-driven.
4. URL tracking: `job-pipeline/.pipeline-artifact-url`. Read it first and redeploy to that URL if present; otherwise publish fresh and write the returned URL there.
5. Share the resulting link with the user directly, in your own reply — don't bury it, and don't skip this because the change felt minor. Unlike Operation 1 (where the URL just goes back to the caller to use as it sees fit), the pipeline board link is the thing the user actually wants handed to them, and it is the whole answer: the link, not the link plus a summary of what's on it.
6. If the publish fails, say so and why. Never substitute the markdown tables into the reply as a consolation — the user has explicitly given up on terminal pipeline output.

## What this skill never does

- Never writes to the content of `job-pipeline/*.md` — it only reads what's already there and republishes the rendered view. A stale or wrong source file is the calling skill's problem to fix first, not something to paper over here.
- Never invents a row, status, or verdict that isn't present in the file being mirrored.
- Never pastes the pipeline tables, or a prose digest of them, into the conversation. The page is the output; the link is the delivery.
