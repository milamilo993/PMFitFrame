---
name: tailor-resume
description: Menu option 4. Use this skill whenever the user needs a CV tailored for a specific role, reordering and re-emphasizing what already exists in the master CV to lead with the most relevant experience and skills for that posting. Never invents new content. Triggers on "tailor my CV", "edit my CV for this role", "CV for [company]", "build the CV for this application", "CV edits".
---

# Tailor Resume

Produces a role-specific CV by reordering, reframing, and re-emphasizing content that already exists in the master CV, never by inventing new experience, skills, or metrics. `pm-profile/cv.md` is the single source of truth for every fact that can appear in a tailored version.

## Non-negotiable rule: never invent

Every bullet, metric, skill, and claim in a tailored CV must trace back to `pm-profile/cv.md`. Reordering, rewording, re-emphasizing, and dropping content is all fair game. Adding a fact, a metric, a skill, or a responsibility that isn't already in the master material is not, even when it would make the CV a stronger match.

If the job description calls for something the master material doesn't clearly cover (a specific tool, a kind of experience, a metric not already captured), stop and ask the user directly whether it's true and how they'd phrase it. Don't infer it, don't soften an absence into an implied presence, and don't word your way around a gap that's actually there. This is the single most important rule in this skill, a fabricated CV claim is a non-recoverable risk in a way a merely generic CV isn't.

## Read first

- `pm-profile/cv.md`, the canonical CV text and the source of every fact. Never re-parse `pm-profile/cv-original.*` when `cv.md` exists.
- `pm-profile/competencies.md` and `pm-profile/preferences.md` if present, for self-rated pillars (how strongly a claim is actually backed) and what the user wants out of the next role.
- `job-pipeline/applications/<company-slug>/fit-assessment.md` if it exists (written by `role-fit`), read it first. `<company-slug>` is the company folder defined by the `job-pipeline` skill: lowercase, hyphenated, no location and no role in it. It has already done the work of identifying which experience matters most for this role and which gap needs honest handling rather than a forced bridge.
- `job-pipeline/applications/<company-slug>/company-product-analysis.md` if it exists (written by `company-research`), for the specific language and priorities to mirror.
- `job-pipeline/applications/<company-slug>/<role-slug>.md`, the role file, for the JD verbatim.

Employment status comes fresh from `pm-profile/cv.md` every time, never from a previously tailored CV. A role that has ended is never written as current.

If no fit assessment exists yet, say so and offer to run `role-fit` first. Tailoring without it guesses at what matters instead of knowing.

## What tailoring actually changes

- **Tagline and summary emphasis.** Which two or three identity tags lead (for example, leading with a domain or skill framing rather than the last job title when the target title sits a step below the user's current level, the same pattern `cover-letter` uses). The underlying facts don't change, what leads does.
- **Key achievements order.** The same achievements every time, reordered so the one closest to the role's actual mandate leads.
- **Bullet order within a job entry.** The same bullets, reordered so the most relevant come first, hiring managers skim the first two or three lines of each entry.
- **Bullet phrasing.** Light rewording into the language of the target domain or mandate (for example, "data quality" instead of a domain-specific term that only means something inside the user's last industry), never changing what actually happened, only how it's described.
- **Skills list order.** The same skill set, reordered to put the most JD-relevant terms first, for human skimming and ATS matching alike.

## What tailoring never does

- Never adds a metric, tool, technology, or responsibility not already present in the master material.
- Never changes a metric's number, up or down. Numbers are copied exactly as `pm-profile/cv.md` states them.
- Never claims domain experience that doesn't exist. A real domain gap gets bridged honestly in the cover letter and the fit assessment, not papered over in the CV with an invented bullet.
- Never changes a job title or drops an employer name to obscure a level mismatch. The actual historical title stays exactly as it was, tailoring repositions the framing around it, not the title itself.

## Process

1. Read the fit assessment and note which one or two dimensions are the strongest case for this role, that's what should lead.
2. Start from `pm-profile/cv.md` as the structure. Don't redesign the CV per role.
3. Rewrite the tagline and summary to lead with what the fit assessment identified as strongest, using only language and facts already in the master material.
4. Reorder the key achievements and the bullets within each job entry accordingly.
5. Reorder the skills list to front-load terms matching the JD's own language, where a genuinely overlapping skill already exists in the master list. Don't add a term that isn't already there.
6. If the strongest possible tailoring still leaves a real gap the JD cares about, stop and name it plainly rather than writing around it quietly: "the JD wants X, I don't see that in your profile, is that something you have and I'm missing, or a genuine gap to handle honestly in the cover letter instead?"
7. Save as `job-pipeline/applications/<company-slug>/cv.md` and name the file you wrote in one short line. Offer an `.html` or `.pdf` export only after the user has approved the text, and ask which they want rather than assuming a rendering toolchain is installed.

## Close the loop

- Tell the user plainly what changed and why, tagline, order, phrasing, so they can catch anything that reads as overreach even within the never-invent boundary.
- If a real gap or an unlisted strength surfaces during tailoring, a skill they have that isn't captured yet, a metric not yet logged, flag it as worth adding to `pm-profile/cv.md` or `pm-profile/competencies.md` so future tailoring starts from a more complete source of truth. Show the exact text and get a yes before writing anything to `pm-profile/`.
- If this changes the role's status or next action, hand that to `job-pipeline` (Operation 2) rather than editing `overview.md` here, then invoke `pipeline-artifacts` Operation 2 and give the user the board link. Never print pipeline state into the conversation.

## Tell me when you apply

This skill produces material the user might act on without saying so. The pipeline only stays true if the moment of applying gets recorded, and nothing here can observe it happening.

So end the reply with one short line asking them to say when they have applied, so the entry moves to Applied — Active with the date and the board stays accurate. One line, in the reply, not a paragraph and not a document section. Vary the wording; do not repeat a canned sentence every time.

Ask only when applying is actually the next step for this role (an Apply or conditional-apply verdict, a CV or letter drafted, research done ahead of a submission). Skip it on a do-not-apply verdict, on a role already recorded as applied, and when the user has already told you in this session that they applied.

When they do report it, that is a `job-pipeline` status update: record the date, move the entry, republish the board, hand back the link. A reported application also often carries the deadline, the channel used (cold, referral, recruiter), and whether they sent the letter, all worth capturing in the role file while it is fresh.
