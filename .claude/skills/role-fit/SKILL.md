---
name: role-fit
description: Menu option 2. Use this skill whenever a user needs a fit assessment for a specific role, a structured judgment on whether to apply, what the honest gaps are, and what to lead with if she does. Produces `fit-assessment.md`, the document every other skill in this project (cv-tailor, cover-letter, interview-prep) reads first. Triggers on "assess fit for this role", "assess my profile against this one", "should I apply to X", "fit assessment for [company]", a pasted job posting or URL followed by "what do you think" or "assess this", and the `/role-fit` reference in `roles/target-companies.md`.
---

# Role Fit

Produces a structured, honest fit assessment for one specific role: what the job actually needs, where Mila's background genuinely matches, where it doesn't, and a clear verdict on whether to apply. This is the foundation document, `tailor-resume`, `cover-letter`, `interview-prep`, and `company-research` all read it first rather than re-deriving fit from scratch.

Unlike CVs and cover letters, this document is written about Mila in the third person (matches every existing fit-assessment.md in this project), it's an analytical judgment call, not a document she sends anywhere.


# Steps

## 1. Get the job posting

If given a URL, fetch it. If the fetch returns only a title (common on JS-rendered boards like Ashby, Greenhouse), search for the company's own careers-page mirror of the same posting before giving up, that usually has the full text where the ATS page doesn't. If given pasted JD text directly, use it as-is. Never guess at requirements not actually stated.

## 3. Read first

- `pm-profile/cv.md` as the source of truth for experience, protected metrics, current employment status (check fresh each time, don't assume from a prior assessment)
- the **Level** section of `pm-profile/competencies.md` for `<level-slug>`, the level deduced from the CV by `cv-intake`, plus the target level if one is set. Read it before judging seniority fit — never re-derive the level yourself, and never assume it from the posting's title
- `pm-profile/competencies.md` for self-rated pillar scores to calibrate how much evidence backs a given claim, read against the `<level-slug>` in its header
- `pm-profile/preferences.md` for stated preferences ("What I'm Looking For") in the next role, to check whether the posting actually meets them or not, and to surface any misalignment in the write-up 
- The recent entries in the job-pipeline and the `job-pipeline/strategy.md` if exists, both for prior applications to this exact company (a previous rejection or no-response is a real data point, not noise) and for patterns already established across the search (a repeated language knockout, a repeated domain gap, a repeated "do not apply" reason) that this role might repeat
- `job-pipeline/applications/<company-slug>/company-product-analysis.md`, if `company-research` has already been run for this company

## 3b. Profile preconditions — stop here if either file is missing

This skill judges a posting against the user's own profile, so both halves of that profile have to exist before the assessment is worth writing. Check `pm-profile/` and handle what is missing **before** writing anything:

- **`competencies.md` missing** → invoke the `competencies` skill. It reads `cv.md`, assesses the 12 Ravi Mehta competencies and writes the file, including the **Level** section this skill reads for `<level-slug>`. Without it, seniority gets judged with nothing to judge against, and every pillar claim is uncalibrated.
- **`preferences.md` missing** → invoke the `preferences` skill. It asks eight questions and writes the file, including the target level, the screening rules `R1`…`Rn` this assessment applies, and the tensions between them. Without it, compensation, location scope, role shape and deal-breakers all collapse into "unassessable, flag don't guess" — honest, useless, and it reopens on the next role.
- **Both missing** → say so in one line and run `competencies` first; `preferences` restates the level slug it establishes.

Offer once, in **one line of plain text — never an `AskUserQuestion` picker** — naming what the missing file gates here: *"`preferences.md` isn't on file — want me to ask you eight questions first? It gates the comp, location and deal-breaker calls on this role and every other one."* A missing profile file is not a menu of options; it is one thing to say yes or no to. On a yes, invoke the skill, which owns whatever questions follow, then come back and finish the assessment against the file it wrote. On a no, carry on without it and keep flagging the specific gaps it would have closed; do not ask again in the same session.

When a file does get written mid-assessment, re-run the screening against it before publishing — a comp floor or a deal-breaker can turn a conditional apply into a do-not-apply, which is the whole point of having asked.

## 4. Ask, don't guess, when a stated requirement turns on an unverifiable personal fact

If a hard requirement (a language fluency level, a certification, a citizenship/clearance-dependent eligibility, a specific tool) isn't captured in `pm-profile/cv.md` and the verdict genuinely hinges on it, ask user directly rather than assume either way. A guessed "do not apply" can lose a real fit; a guessed "apply" can waste her time on something that was always going to knock out. This has come up for language levels specifically, don't infer fluency from silence in the profile.

## 5. Write the assessment
Write to `job-pipeline/applications/<company-slug>/fit-assessment.md` (create the folder if it doesn't exist, where `<company-slug>` is a URL-friendly version of the company name, lowercase and hyphenated, with no location and no role in it). This is the project-wide convention defined in the `job-pipeline` skill: every file belonging to a company lives in that one folder. Header block:

```
# Role Fit Assessment — <Title>, <Company>, <Location>

**Date:**
**Deadline:** (or "None stated")
**Verdict:** One line, the conclusion and the single strongest reason for it.
```

Then, in this order:

1. **Role Deconstruction** — what problem is this hire actually solving, what does success in 12 months look like, level and scope implied (read between the lines of title vs. actual described scope, they often diverge), non-negotiable requirements as stated, then a separate short list of anything explicitly framed as "nice to have" or "ideally," these two lists get treated very differently in the gap analysis.

2. **Fit Analysis** — lettered subsections (a, b, c...), pick the dimensions that actually matter for this posting rather than a fixed checklist. Common ones seen across this project: domain/industry fit, seniority/scope fit, execution fit, technical/architecture fit, AI/ML fit, leadership/stakeholder fit, financial/commercial fit, culture/environment fit, language/logistics requirements. Each gets a **Reasoning:** paragraph (grounded in specific, named evidence from the profile, not generic claims) and a one-line **Verdict:**.

   **Seniority is judged against `<level-slug>`, not against the posting's title.** Work out the level the posting's *described scope* implies, then compare it to the current `<level-slug>` from the **Level** section of `pm-profile/competencies.md`, and to the target level if one is set. Three outcomes, each handled differently:

   - **Posting below `<level-slug>`** — an under-levelled role. Not a knockout by itself, but name it: it predicts a lower band, a narrower remit, and a retention probe in the interview. Say plainly that the title reads a step down and that the scope, not the title, is what would have to justify it.
   - **Posting at `<level-slug>`** — a lateral move. Then the question is whether it advances the target level, and if it does not, say so; a lateral move that also narrows the domain is worth naming as a direction change rather than a step.
   - **Posting above `<level-slug>`** — a stretch. Say which specific evidence is thin for that bar rather than declaring it out of reach, since a posting one level up with genuine scope overlap is often the highest-value application in a pipeline.

   A title without a seniority marker ("AI Engineer", "Software Engineer") is not evidence of a low level, only of an unstated one: derive the level from the described scope and flag that it needs confirming in the first conversation.

3. **Honest Gap Assessment** — a table: `Gap | Knockout risk | Bridging action`. Knockout risk is High/Medium/Low or, when confirmed, "Confirmed knockout." A stated hard requirement she doesn't meet is a different category from a "nice to have" she doesn't meet, don't conflate them. Distinguish a genuine gap (real, would need real work) from a perceived one (smaller than it feels, per the profile's own framing) explicitly.

4. **Bridging Strategy** — only when the verdict leans toward applying. Concrete, quotable framing language for each real gap, in Mila's voice, something she could actually say in an interview, not a description of a strategy.

5. **Verdict** — the full reasoning, not just the one-liner from the header. Name what would have to be true for this to be worth pursuing (a warm connection, a confirmed location, a level clarification) if the verdict is conditional rather than clean.

6. **What to Expect in the Process** (when the verdict is Apply or Take the call) — likely probes, questions to prepare for, what to lead with. Skip this section entirely on a clean "do not apply", there's no process to prep for.

## 6. Publish and record

Do these in order — the artifact URL from step 1 is needed for step 2:

1. **Publish the assessment artifact** — invoke the `pipeline-artifacts` skill, Operation 1, with the path to the fit-assessment file just written. It publishes/updates the Artifact page and hands back its URL.
2. **Record to Job Pipeline** — add the role to `job-pipeline/overview.md` if it doesn't exist, create one. Structure the entry (Applied — Active if already submitted, Assessed — Not Applied otherwise) with a one-line summary of the verdict and reasoning, The **File** column holds the relative path to the role file, `applications/<company-slug>/<role-slug>.md` — `pipeline-artifacts` swaps in the artifact URL from step 1 when it renders the board, so don't put the URL in `overview.md` itself.
3. **Publish the pipeline board** — invoke the `pipeline-artifacts` skill, Operation 2, now that `overview.md` has changed. It reads `overview.md` itself, republishes the board, and shares the link with the user directly — nothing further needed from this skill. Do not also print the pipeline, or any part of it, into the reply; the board is the only view of it.

## 7. What this skill never does

- Never invents a qualification, metric, or experience Mila doesn't have to make a fit look stronger, that's what the Honest Gap Assessment is for.
- Never softens a stated hard requirement into a maybe because the rest of the fit is strong. A confirmed knockout (a language fluency requirement she doesn't meet, a citizenship-gated clearance, an onsite requirement in a country outside her stated relocation scope) ends the assessment cleanly, however good everything else looks, that's a feature of the process, not a failure to find a workaround.
- Never assumes the current search-strategy calibration without checking the latest strategy file, "apply to everything" and "pause cold Director-level applications" have both been the right call at different points in this search.

## 8. Close the loop

- The role must be in `job-pipeline/overview.md` in the correct table with a concise, honest summary (step 6 above), and the board republished — this is the single most important close-the-loop step, it's how every other conversation in this project knows this role was assessed. Recorded on disk and visible on the board; never recapped as a table here.
- If domain is unfamiliar and the verdict is Apply or conditional, suggest running `company-research` next, deep company/product research strengthens both the cover letter and any later interview prep.
- If the verdict is Apply, offer to run `cv-tailor` and `cover-letter` next, don't run them automatically, the verdict itself is often worth a pause for Mila to react to first.
- If this assessment corrects something a related document already claims (a competitor list in `company-product-analysis.md`, a scope assumption in `roles/target-companies.md`), fix it there too rather than leaving two documents disagreeing.

## Tell me when you apply

This skill produces material the user might act on without saying so. The pipeline only stays true if the moment of applying gets recorded, and nothing here can observe it happening.

So end the reply with one short line asking them to say when they have applied, so the entry moves to Applied — Active with the date and the board stays accurate. One line, in the reply, not a paragraph and not a document section. Vary the wording; do not repeat a canned sentence every time.

Ask only when applying is actually the next step for this role (an Apply or conditional-apply verdict, a CV or letter drafted, research done ahead of a submission). Skip it on a do-not-apply verdict, on a role already recorded as applied, and when the user has already told you in this session that they applied.

When they do report it, that is a `job-pipeline` status update: record the date, move the entry, republish the board, hand back the link. A reported application also often carries the deadline, the channel used (cold, referral, recruiter), and whether they sent the letter, all worth capturing in the role file while it is fresh.
