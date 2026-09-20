---
name: cover-letter
description: Use this skill whenever the user needs a cover letter drafted for a specific role. Bridges the user's core motivations to the specifics of the posting, following one consistent structural pattern. Menu option 5; also invoked by name or by another skill. Triggers on "write a cover letter", "draft a cover letter for [company]", "cover letter for this role".
---

# Cover Letter

Menu option 5.

Drafts a cover letter for a specific role, grounded in the fit assessment for that company and in the user's stated motivations, not a generic template with the company name and title swapped in.

## Read first

- `job-pipeline/applications/<company-slug>/fit-assessment.md` if it exists (written by `role-fit`). `<company-slug>` is the company folder defined by the `job-pipeline` skill: lowercase, hyphenated, no location and no role in it. This is the primary source for what to lead with and which gap to name honestly. If it doesn't exist yet, say so and offer to run `role-fit` first, a cover letter written without it tends to read generic.
- `job-pipeline/applications/<company-slug>/company-product-analysis.md` if it exists (written by `company-research`), for specific, real detail to bridge into (a named product, a stated strategic direction, a market tailwind), not brochure-copy praise.
- `job-pipeline/applications/<company-slug>/<role-slug>.md`, the role file, for the JD verbatim.
- `pm-profile/cv.md` for scope language and metrics. Never re-parse `pm-profile/cv-original.*` when `cv.md` exists.
- `pm-profile/preferences.md` and `pm-profile/competencies.md` if present, for what the user says they want and how strongly a claim is actually backed.

## The user's motivations

A cover letter should draw on the user's own stated framing for what motivates them, taken from `pm-profile/preferences.md` (and whatever they have said in-session), not from a generic list. Where that file doesn't state them, ask once and work from the answer.

The pattern that holds regardless of the specific list: not every motivation belongs in every letter. One or two carry the letter's central "what draws me to this" paragraph, and the rest appear only where the posting actually earns them. Forcing all of them into one letter reads as padding, not conviction.

Typical shapes worth looking for in a posting: an unscoped, ambiguous mandate earns a "hard problems that need scoping" motivation; a company at an inflection point or expansion phase earns "real impact" and "ambitious goals"; an engineering-close or trio structure earns "strong technical teams"; an early-stage or newly defined mandate earns "room to grow past the first mandate." Don't claim a motivation the posting doesn't actually support.

## Before writing: check current employment status and tense

Pull the most recent title and company fresh from `pm-profile/cv.md` every time, and check whether that role has ended. If it has, never imply present employment there, use past tense ("Until <month year>, I was...", "Most recently, I was..."). A prior draft is not a reliable source for this, it goes stale the moment the user changes roles.

## When the target title reads as a step down or sideways

Some roles are worth testing at a level below the user's last title, deliberately. When that's the case, and the user has confirmed it is deliberate, name it directly rather than hoping it goes unnoticed: one short paragraph stating plainly that title has never been the driver, that what matters is the scope on offer (an area that needs defining and owning end to end, with real impact attached), and that this role's scope fits what motivates them better than a higher title with a narrower or already-defined mandate would. Don't apologize for the gap or over-explain it, state it once and move on.

## The structural pattern

Every letter follows the same five-part shape:

1. **Opening hook.** Name the company's or role's actual problem in their own terms (not a generic "I'm excited about your mission"), then bridge immediately to a directly parallel problem the user has already solved. The bridge should be concrete and specific, not "I have relevant experience."
2. **Proof paragraph.** Current or most recent role, scope, and 2 to 4 hard metrics drawn from `pm-profile/cv.md`. Use the numbers exactly as they appear there, never round, inflate, or re-derive them. Real numbers, not adjectives.
3. **"What draws me specifically" paragraph.** Names the actual sub-area or mandate of this role, not the company generically, and pulls in whichever motivations the posting genuinely earns. This is also where an honest gap gets named directly rather than buried or omitted (for example: no experience with a named technology the JD asks for, no background in the target domain). Naming a gap directly and pairing it with what offsets it reads as more credible than avoiding it.
4. **Logistics paragraph.** Location, relocation, and visa/work-authorization status, named plainly and upfront, never left for later in the process. If something is genuinely unclear (which office, whether a work permit is needed), say so directly rather than guessing.
5. **Short close.** Sign-off, sometimes one line inviting the conversation. Never a restated summary of the letter.

## Tone and mechanics

- First person throughout, never third person. (The fit assessment is the opposite: it is written about the user in the third person.)
- No em or en dash as punctuation anywhere, use a comma instead. A hyphen inside a compound word is fine.
- Specific numbers beat adjectives every time, "cut operational cost by 50%" not "significant cost savings."
- Direct gap acknowledgment beats a dodge. Never imply a listed requirement is met when it isn't.
- Never invent a metric, employer, or responsibility that isn't in `pm-profile/cv.md`. Same rule as `tailor-resume`: if the posting wants something the profile doesn't show, ask the user whether it's true rather than writing around it.
- Length: 4 to 6 paragraphs, roughly 350 to 500 words. Never pad to fill space.

## Save and close the loop

- Save as `job-pipeline/applications/<company-slug>/cover-letter.md`, marked as a draft awaiting approval. Only convert to `.html`/`.pdf` once the user has reviewed and approved the text. Name the file you wrote in one short line.
- Tell `job-pipeline` (Operation 2) that a letter now exists for this role if it changes the status or the next action, rather than editing `overview.md` here.
- If `overview.md` changed as a result, invoke `pipeline-artifacts` Operation 2 and hand the user the board link. Never print pipeline state into the conversation.

## An honest note on what a cover letter is worth

Say this plainly when it's relevant rather than overselling the deliverable: a cover letter is a cold-channel tool. Where a warm introduction exists, that path converts far better and should lead. This structure is the consistent, honest, specific approach used across this project, not a proven high-converting template, and it has not been tested head to head against warm-intro or CV-only paths. Use it because it is calibrated and truthful, and check `job-pipeline/strategy.md` (if it exists) for the current read on which channel is actually working before assuming a letter is the right lever at all.

## Tell me when you apply

This skill produces material the user might act on without saying so. The pipeline only stays true if the moment of applying gets recorded, and nothing here can observe it happening.

So end the reply with one short line asking them to say when they have applied, so the entry moves to Applied — Active with the date and the board stays accurate. One line, in the reply, not a paragraph and not a document section. Vary the wording; do not repeat a canned sentence every time.

Ask only when applying is actually the next step for this role (an Apply or conditional-apply verdict, a CV or letter drafted, research done ahead of a submission). Skip it on a do-not-apply verdict, on a role already recorded as applied, and when the user has already told you in this session that they applied.

When they do report it, that is a `job-pipeline` status update: record the date, move the entry, republish the board, hand back the link. A reported application also often carries the deadline, the channel used (cold, referral, recruiter), and whether they sent the letter, all worth capturing in the role file while it is fresh.
