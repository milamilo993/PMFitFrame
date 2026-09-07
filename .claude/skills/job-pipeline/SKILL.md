---
name: job-pipeline
description: Maintain job-pipeline/ as the single source of truth for every role the user is tracking. Three operations only - create an entry, update a status, print the pipeline. Use when the user picks the pipeline menu option, asks where things stand, or reports news on a role (applied, heard back, interview booked, rejected, offer). Other skills call this one to record what they produce; it does not assess fit, tailor CVs, or prep interviews itself.
---

# Job pipeline

Bookkeeping for `job-pipeline/`. It records state; it does not judge roles. Fit assessment belongs to `role-fit`, company and product research to `company-research`, interview material to `interview-prep`, CV work to `tailor-resume`, letters to `cover-letter` — this skill stores what they produce and keeps the status straight.

## Files

```
job-pipeline/
├── overview.md             index — three tables, nothing else
└── <company>-<role-slug>.md    one per role
```

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

**Ageing.** An `Applied` row whose `As of` date is more than 60 days old becomes `Lapsed` and moves to Closed. Apply this on every operation that touches the index, append a `History` line to each affected role file reading `<date> — Lapsed — aged out, no response in 60 days`, and report the count in one line. Without it the Active table silently fills with dead applications and stops meaning anything. Ageing is the one status change made without asking; everything else needs the user or a calling skill to say so.

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
- **File** — relative link to the role file.

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

1. Write `job-pipeline/<company>-<role-slug>.md`, pasting the JD verbatim if supplied. Never paraphrase a JD — other skills read it later.
2. Add the index row, table chosen by status. Default `Shortlisted` unless the user says otherwise.
3. Confirm in one line, naming the file.

If an entry for that company and role already exists, say so and update it instead of creating a duplicate.

## Operation 2 — update a status

1. Set the new status in the role file, update **As of**, append a `History` line saying what happened.
2. Update the index row, and move it if the new status belongs to a different table.
3. Confirm in one line: old status → new status.

Free text the user gives you ("CEO round went OK, decision next week") goes in the History line and `Next action`. It never goes in the Status cell.

## Operation 3 — print the pipeline

Run the renderer, then **reproduce its output verbatim in your reply**. Use exactly this command — a relative path, no quoting, no `cd`, no absolute path. An absolute path here contains an escaped space and triggers a permission prompt:

```
bash .claude/pipeline.sh
```

`--md` emits markdown tables. Paste them straight into your response so the user reads them inline without expanding a tool call. Do not summarise, reorder, or drop columns, and do not wrap them in a code fence — they are meant to render as tables.

`bash .claude/pipeline.sh` with no flag gives the colour terminal version instead. That is for the user to run themselves; never use it as the answer, because colour is lost the moment you retype it.

It reads `job-pipeline/overview.md` and prints all three tables with colour-coded status pills, an age tag on every `As of`, and overdue `Next action` dates in red. `Applied` rows past 60 days are flagged `!` — those are the ones the ageing rule turns into `Lapsed`.

Add no commentary, summary, or ranking around it. Only fall back to printing the markdown tables yourself if the script fails, and say that it failed.

If `job-pipeline/` has no index yet, say so in one line and offer to start one.

## Being called by another skill

Other skills use this one rather than writing to `job-pipeline/` themselves, so status stays in one place. They may ask for:

- the path to a role's file, so they can append to it;
- an entry created for a role they have just taken in;
- a status advanced after something happened.

Do that one thing and hand control back. Do not print the pipeline, assess a role, or suggest next steps when called this way — the calling skill is mid-task.
