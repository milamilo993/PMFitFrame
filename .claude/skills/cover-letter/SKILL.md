---
name: cover-letter
description: Use this skill whenever user needs a cover letter drafted for a specific role. Bridges her five core motivations to the specifics of the posting, following the structural pattern already consistent across every cover letter drafted in this project. Triggers on "write a cover letter", "draft a cover letter for [company]", "cover letter for this role".
---

# Cover Letter

Drafts a cover letter for a specific role, grounded in user's fit assessment for that company and her stated motivations, not a generic template filled in with company name and title swapped.

## Read first

- `applications/<location>/<company>/fit-assessment.md` if it exists, this is the primary source for what to lead with and which gap to name honestly. If it doesn't exist yet, say so and offer to run the fit-assessment step first, a cover letter written without it tends to read generic.
- `applications/<location>/<company>/company-overview.md` if it exists, for specific, real detail to bridge into (a named product, a stated strategic direction, a market tailwind), not brochure-copy praise.
- `profile/00-overview.md` for metrics and scope language to draw on.

## The five motivations

Every cover letter should draw on these, user's own stated framing for what she's motivated by. Not all five belong in every letter, in practice one or two carry the letter's central "what draws me to this" paragraph, and the rest surface only where the specific posting actually earns them, forcing all five into one letter reads as padding, not conviction.

1. The opportunity to make a real impact, to shape the course of a product or an industry, not just execute someone else's plan
2. Hard, complex problems and product spaces, ones that need to be properly scoped and understood before impact is possible, not vague or already-solved ones
3. Ambitious goals and business aspirations, not a maintenance mandate
4. The opportunity to work alongside great technical teams where excellence is expected at every step, not "good enough" engineering
5. Room to develop and progress further once the role's initial goals are achieved, not a dead end once the first mandate is complete

Read the posting and the fit assessment for which of these the role actually substantiates, a role with an unscoped, ambiguous mandate earns #2 directly, a company at an inflection point or expansion phase earns #1 and #3, a "trio" or engineering-close structure earns #4, an early-stage or newly defined mandate earns #5. Don't claim a motivation the posting doesn't actually support.

## Before writing: check current employment status and tense

user's Sportradar tenure ended July 2026 (`profile/00-overview.md`, "Most recent title/company"). Never write "I'm currently a Group Product Manager at Sportradar" or otherwise imply present employment there, use past tense ("Until July 2026, I was...", "Most recently, I was..."). Check this field fresh each time rather than assuming from a prior draft, if she changes roles again this will go stale the same way.

## When the target title reads as a step down or sideways

Several roles in this pipeline (Nettbil, Trackunit, CatalystOne) test at Senior PM level against a Group PM background, deliberately, per `roles/02-strategy-sept-2026.md` Priority 1. When that's the case, name it directly rather than hoping it goes unnoticed: one short paragraph stating plainly that title has never been the driver, what matters is the scope on offer (an area that needs defining and owning end to end, with real impact attached), and that this specific role's scope is a better match for what motivates her than a higher title with a narrower or already-defined mandate would be. Don't apologize for the title gap or over-explain it, state it once, directly, and move on.

## The structural pattern (consistent across every letter drafted so far)

Confirmed across Intercom, DeepL, Monterro, and Zauber, four distinct roles, industries, and stages, all following the same five-part shape:

1. **Opening hook.** Name the company's or role's actual problem in their own terms (not a generic "I'm excited about your mission"), then bridge immediately to a directly parallel problem user has already solved. The bridge should be concrete and specific, not "I have relevant experience."
2. **Proof paragraph.** Current role, scope, and 2 to 4 hard metrics, drawn from `profile/00-overview.md`'s protected metrics (50% operational cost reduction, 5ppt margin capture, 60% latency reduction + 25% coverage expansion → 15% top-line growth, 100% governance-framework adoption). Real numbers, not adjectives.
3. **"What draws me specifically" paragraph.** Names the actual sub-area or mandate of this role, not the company generically, and pulls in whichever of the five motivations above the posting genuinely earns. This is also where an honest gap gets named directly, not buried or omitted, the existing pattern never pretends a gap doesn't exist (Zauber: LLM-agent experience; DeepL: Identity/Console platform work; Monterro: no consulting background). Naming it directly and pairing it with what actually offsets it reads as more credible than avoiding it.
4. **Logistics paragraph.** Location, relocation, and visa/work-authorization status, named plainly and upfront, never left for later in the process. If something is genuinely unclear (which office, whether a work permit is needed), say so directly rather than guessing.
5. **Short close.** Sign-off, sometimes one line inviting the conversation. Never a restated summary of the letter.

## Tone and mechanics

- First person throughout, never third person (project-wide rule, see `CLAUDE.md`).
- No em or en dash as punctuation anywhere, use a comma instead (project-wide rule). A hyphen inside a compound word is fine.
- Specific numbers beat adjectives every time, "50% operational cost reduction" not "significant cost savings."
- Direct gap acknowledgment beats a dodge. The existing letters never pretend a listed requirement is already met when it isn't.
- Length: 4 to 6 paragraphs, roughly 350 to 500 words. Never pad to fill space.
- Save as `applications/<location>/<company>/cover-letter.md` first, as a draft marked "awaiting approval before HTML/PDF conversion." Only convert to `.html`/`.pdf` once user has reviewed and approved the text.

## An honest note on what "worked" actually means here

Worth saying plainly rather than assuming: as of September 2026, none of the applications that progressed furthest in this search, Jotta and Bislab to a hiring-manager+ conversation, Ardoq through a full process to a final team call, GSFleet to an offer, went through a cover letter at all. Jotta and GSFleet were CV-only, Ardoq ran on a case study, Bislab on warm outreach. The funnel diagnosis in `roles/02-strategy-sept-2026.md` found channel (warm intro vs. cold), not application content, is the dominant factor in this search, cold applications convert at roughly 3% regardless of how strong the materials are.

So this pattern is the consistent structural and tonal approach user has settled on across every letter drafted, not a proven high-converting template. Keep using it because it's honest, specific, and well-calibrated, not because it's been shown to outperform warm intro or CV-only paths, it hasn't been tested against those directly. Where a warm path exists, lead with that per `roles/target-companies.md` and Priority 2 of the current strategy, a cover letter is the cold-channel fallback, not the primary lever.
