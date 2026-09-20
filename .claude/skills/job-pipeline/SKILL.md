---
name: job-pipeline
description: Maintain job-pipeline/ as the single source of truth for every role the user is tracking. Three operations only - create an entry, update a status, publish the pipeline board. Pipeline state is never printed into the conversation; it is shown only as the published board artifact. Use when the user picks the pipeline menu option, asks where things stand, or reports news on a role (applied, heard back, interview booked, rejected, offer). Other skills call this one to record what they produce; it does not assess fit, tailor CVs, or prep interviews itself.
---

# Job pipeline

Bookkeeping for `job-pipeline/`. It records state; it does not judge roles. And it never renders that state into the conversation — the only display surface for the pipeline is the board artifact published by `pipeline-artifacts`. Fit assessment belongs to `role-fit`, company and product research to `company-research`, interview material to `interview-prep`, CV work to `tailor-resume`, letters to `cover-letter` — this skill stores what they produce and keeps the status straight.

## Files

```
job-pipeline/
├── overview.md                        index — three tables, nothing else
├── strategy.md                        optional, the current search-strategy read
└── applications/<company-slug>/       one folder per company
    ├── <role-slug>.md                 the role file, one per role at that company
    ├── fit-assessment.md              written by role-fit
    ├── company-product-analysis.md    written by company-research
    ├── cover-letter.md                written by cover-letter
    ├── cv.md                          written by tailor-resume
    ├── interview-prep-<stage>.md      written by interview-prep
    └── <name>-artifact-url.txt        published artifact URLs, written by pipeline-artifacts
```

`applications/<company-slug>/` is the one rule every skill follows. `<company-slug>` is a URL-friendly version of the company name, lowercase, hyphenated, no location and no role in it. Create the folder on first write; nothing else in this project decides where a company's files go.

`company-product-analysis.md` is company-level and shared across roles. If a second role at the same company is ever tracked, every role-specific file takes the role slug as a prefix — `<role-slug>-fit-assessment.md`, `<role-slug>-cover-letter.md`, `<role-slug>-cv.md` — and the company folder stays one folder.

The index has **no Notes column and no Reason column**. Anything discursive lives in the role file.

## Status vocabulary

One vocabulary. Every entry has exactly one status from this list, written as the bare word — never a sentence.

| Status | Meaning | Table |
|---|---|---|
| `Shortlisted` | Worth applying, not started | Considering |
| `Passed` | Decided against applying | Considering |
| `Drafting` | Application in preparation | Active |
| `Outreach` | Contact made, nothing submitted | Active |
| `Applied` | Submitted, no response yet | Active |
| `Screening` | Recruiter screen or intro call | Active |
| `Interviewing` | Hiring-manager, case, or panel rounds | Active |
| `Final` | Final round done, decision pending | Active |
| `Offer` | Offer received, undecided | Active |
| `Rejected` | They said no, at any stage | Closed |
| `Declined` | User turned down an offer | Closed |
| `Withdrawn` | User pulled out before a decision | Closed |
| `Lapsed` | Applied, no response, given up on | Closed |
| `Expired` | Posting closed before applying | Closed |

**The table is derived from the status, never chosen separately.** When a status changes, move the row in the same edit. A `Rejected` row sitting in Active is a bug, not a judgement call — check this on every write.

**Ageing.** An `Applied` row whose `As of` date is more than 60 days old becomes `Lapsed` and moves to Closed. Apply this on every operation that touches the index, append a `History` line to each affected role file reading `<date> — Lapsed — aged out, no response in 60 days`, and report the count in one line (a count, not a list of the rows). Without it the Active table silently fills with dead applications and stops meaning anything. Ageing is the one status change made without asking; everything else needs the user or a calling skill to say so.

## Index format

All three tables share the same columns, so advancing a role is a cut-and-paste plus one status edit, never a reshape.

```markdown
# Job pipeline

> Last updated: YYYY-MM-DD

## Active - an outcome is still possible

| Role | Company | Location | Status | As of | Next action | File |
| --- | --- | --- | --- | --- | --- | --- |

## Considering — assessed but never entered, or explicitly passed on

| Role | Company | Location | Status | As of | Next action | File |
| --- | --- | --- | --- | --- | --- | --- |

## Closed - no further action

| Role | Company | Location | Status | As of | File |
| --- | --- | --- | --- | --- | --- | 
```

- **As of** — date the current status was reached, `YYYY-MM-DD`.
- **Next action** — a verb, with a date where known: `Follow up 2026-09-15`. Closed and `Passed` rows use `—`.
- **File** — relative link to the role file, `applications/<company-slug>/<role-slug>.md`.

Sort every table by `As of`, newest first.

## Role file format

```markdown
# <Role> — <Company>

- **Status:** <status>  ·  **As of:** YYYY-MM-DD
- **Location:** ·  **Link:** ·  **Contacts:**

## Job description
<verbatim, as supplied>

## History
- YYYY-MM-DD — <status> — <what happened>
```

Other skills append their own sections below `History` — `role-fit` writes the fit assessment, `company-research` the research document, `tailor-resume` and `cover-letter` their outputs, `interview-prep` its notes. Leave whatever they wrote alone.

The Status line here and the index row must agree. On conflict the role file wins, because it has the history; correct the index to match.

## Operation 1 — create an entry

Needs role title and company. Location, link, and the JD text are taken if offered, asked for only if the user seems to expect otherwise.

1. Write `job-pipeline/applications/<company-slug>/<role-slug>.md`, creating the company folder if it doesn't exist, pasting the JD verbatim if supplied. Never paraphrase a JD — other skills read it later.
2. Add the index row, table chosen by status. Default `Shortlisted` unless the user says otherwise.
3. Refresh the board — `overview.md` changed, so run Operation 3.
4. Confirm in one line, naming the file, plus the board link.

If an entry for that company and role already exists, say so and update it instead of creating a duplicate.

## Operation 2 — update a status

1. Set the new status in the role file, update **As of**, append a `History` line saying what happened.
2. Update the index row, and move it if the new status belongs to a different table.
3. Refresh the board — `overview.md` changed, so run Operation 3.
4. Confirm in one line: old status → new status, plus the board link.

Free text the user gives you ("CEO round went OK, decision next week") goes in the History line and `Next action`. It never goes in the Status cell.

## Operation 3 — publish the pipeline board

This replaces printing. There is no terminal renderer and no inline table: the pipeline is shown to the user as a published Artifact page and nothing else.

1. Apply the ageing rule first, so the board reflects it.
2. Invoke the `pipeline-artifacts` skill, Operation 2. It reads `job-pipeline/overview.md`, renders the three tables, redeploys to the board's existing URL (`job-pipeline/.pipeline-artifact-url`), and hands back the link.
3. Give the user that link. One line. Nothing around it — no tables, no counts beyond the ageing line, no summary, no ranking, no "you have four active roles".

If publishing fails, say that it failed and why, in one line. **Do not fall back to pasting the tables** — a retyped index in the transcript is exactly what the board replaces, and a stale one is worse than no answer. Offer to retry instead.

If `job-pipeline/` has no index yet, say so in one line and offer to start one.

## Being called by another skill

Other skills use this one rather than writing to `job-pipeline/` themselves, so status stays in one place. They may ask for:

- the path to a role's file, so they can append to it;
- an entry created for a role they have just taken in;
- a status advanced after something happened.

Do that one thing and hand control back. Do not publish the board, assess a role, or suggest next steps when called this way — the calling skill is mid-task and owns the board refresh at the end of its own flow (skip step 3 of Operations 1 and 2).
