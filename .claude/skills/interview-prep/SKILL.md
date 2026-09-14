---
name: interview-prep
description: Use this skill whenever user is preparing for an upcoming interview or interview-stage conversation in her job search — a meet-and-greet, recruiter screen, hiring manager call, panel, technical/case round, or final/executive round. Two modes: (1) generates a calibrated written prep doc (questions to expect and questions to ask) grounded in the company's fit assessment; (2) runs a live, turn-by-turn mock interview where user answers behavioral/situational questions out loud and gets assessed and coached toward a senior/principal-level answer. Triggers on "prep for interview", "interview prep", "prepping for [company] call", "mock questions", "meet and greet prep", "practice interview questions with me", "mock interview", "quiz me on behavioral questions".
---

# Interview Prep

Prepares user for a specific upcoming conversation in her job search. Two distinct modes — pick based on what they's asking for:

- **Mode A — Prep document.** they wants a written brief before a call. Produces a calibrated question list saved to the company's application folder. See "Mode A" below.
- **Mode B — Live mock interview.** they wants to practice out loud, in the conversation, right now. You play interviewer; they answers; you assess and help her rebuild the answer. See "Mode B" below.

Never dump the entire question bank regardless of mode or stage.

## Mode A — Prep Document

1. **Identify the conversation.** Get from user (ask if not given):
   - Company and role
   - Stage/format: meet-and-greet / intro, recruiter screen, hiring manager, panel, technical or case round, final/executive round
   - Duration
   - Who they's meeting (name, title, if known)

2. **Ground it in what's already known.** Look for and read:
   - `applications/<location>/<company>/fit-assessment.md` — pulls the honest gap assessment, bridging strategy, "what to expect in the process," and top prep priorities already written for this company. This is the primary source of *content* — the question bank below only supplies *form*.
   - `applications/<location>/<company>/company-product-analysis.md` — if it exists (produced by the `company-research` skill), pulls product positioning, competitive landscape, and key tensions. Use this to ground product-sense and case-round questions in real specifics about the company rather than generic frameworks, and to give user real ammunition for "questions to ask them." If it doesn't exist and the round is a panel/case or later stage, suggest running `company-research` first — going in without it means product-sense answers stay generic.
   - `profile/00-overview.md` and `coaching/00-coaching-needs.md` — for metrics, gaps, and self-rated pillars to draw on or avoid overclaiming.
   - Any prior outreach notes in the same application folder (e.g. `outreach-to-*.md`) for context already establitheyd with this contact (what's already been said, what's already been asked/answered).
   - If no fit assessment exists yet for this company, say so and offer to build one first (see the role-fit assessment pattern used elsewhere in this project) — going into a conversation without one means prep is generic rather than grounded.

3. **Calibrate depth to stage.** Use `references/question-bank.md` as the source pool, not a script:
   - **Meet-and-greet / intro:** Category 1 (Common/Rapport) only, ~6-10 questions max. No case studies, no CIRCLES, no technical drilling. The goal is mutual fit exploration, not evaluation.
   - **Recruiter screen:** Category 1 plus logistics/motivation framing.
   - **Hiring manager:** Category 1 + Category 7 (Behavioral/STAR) + light Category 2 (one product-sense question, not several).
   - **Panel / case round:** Full Category 2 (Product Sense) calibrated to sub-type (design/improvement/growth/strategy/launch — pick the one closest to the role's actual mandate), plus Category 3 (Technical) if the role is technical/platform-leaning, plus Category 4 (AI PM) if the role is AI-native or AI-adjacent.
   - **Final/executive round:** Category 6 (Leadership & Communication) + Category 8, with emphasis on strategic narrative over tactical execution detail.
   - Rule of thumb for volume: roughly 1 substantive question per 2–3 minutes of expected discussion time, leaving room for the interviewer's own tangents.

4. **Write the output.** Save to the company's application folder as `interview-prep-<stage-slug>.md` (e.g. `interview-prep-meet-and-greet.md`, `interview-prep-hiring-manager.md`). Structure:
   - Context line: who, what stage, duration, date
   - Framework reminder (only the ones relevant to this stage — e.g. don't explain CIRCLES for a rapport-only call)
   - The calibrated question list, grouped logically, each with a one-line hook to *this specific role* (pulled from the fit assessment) where relevant — not generic prompts
   - A short "questions user should ask them" section — tailored to genuine open threads from the fit assessment or prior conversation (e.g. compensation/funding stage questions flagged as open, or a follow-up on something the contact already said)
   - If there's a known gap flagged in the fit assessment likely to surface at this stage, name it plainly with the honest bridging line already drafted — don't leave user to improvise a gap answer live for the first time in the room

5. **Update the pipeline/tracker if useful** — via the `job-pipeline` skill, which republishes the board rather than printing it — but this skill's job is the prep doc — not re-running the fit assessment or outreach steps, which are separate.

## Mode B — Live Mock Interview Practice

An interactive loop, not a document. You are the interviewer; user answers in the conversation; you coach. Run it turn by turn — never front-load a list of questions and never answer on her behalf.

### 0. Set up the round

Ask (if not already clear from context): which company/round is this for, and is there a specific set of expected questions already identified (e.g. a fit assessment's "What to Expect in the Process" section) to prioritize over the general bank. Ground every question in:
- That company's `fit-assessment.md` — especially "What to Expect in the Process" and the honest gap list. Real, already-identified likely questions beat generic bank questions — use them first.
-  `job-pipeline/overview.md` and `competencies.md` — this is where her documented stories live (metrics, team scope, the governance-framework story, etc.). Treat these as the baseline, not the ceiling: user will often surface new stories or details live during practice that aren't written down anywhere yet. That's expected and good. When they introduces something new, ask her to confirm it's accurate as stated (numbers, scope, outcome) before building it into a rebuilt answer — the constraint is truthfulness to her actual experience, not prior documentation. Never invent or embellish a detail yourself; if a number or outcome is missing, ask her for it rather than filling it in.
- `references/cracking-the-pm-interview-behavioral.md` — the primary assessment rubric and question-category source for this mode (condensed from McDowell & Bavaro's *Cracking the PM Interview*, Ch. 11-12). Use its five-question story-quality checklist and category list (Leadership & Influence, Challenges, Mistakes & Failures, Successes, Teamwork) as the main structure for both picking questions and grading answers.
- `references/decode-and-conquer.md` — a second assessment layer (condensed from Lewis Lin's *Decode & Conquer*, Ch. 12 & 16), used alongside the above, not instead of it. Adds: the credibility/likability grading dimensions (especially "owner vs. participant" and "good vs. great achievement" — was the result actually caused by her, or would it have happened anyway), and the DIGS storytelling structure (Dramatize the situation, Indicate alternatives, Go through what you did, Summarize impact) as a delivery-quality check layered on top of the SAR content check. Also holds the **New Market Entry Checklist** (market characteristics, competitive environment, company fit) — pull this out specifically when a case/strategy-shaped question comes up (e.g. Bislab's "how would you sequence entry into a new country market"), since that's a different question type from pure behavioral and shouldn't be forced through SAR/DIGS.
- `references/question-bank.md` Categories 1, 6, 7, 8, and the Hired Guide pool (Category 10) as a secondary/supplementary pool once the book's categories and the company-specific questions are exhausted.

### 1. Ask one question at a time

Pick a single question, state it plainly as an interviewer would (no meta-commentary about which category it's from), and stop. Wait for her answer. Do not ask a second question in the same turn.

### 2. Assess her answer against a senior/principal bar

they's calibrating for Senior/Principal level, not APM/mid-level — hold the bar there. For behavioral/situational questions, run the answer through both books together — the content check first, then the delivery check:

**Content (five-question checklist + SAR):** substantial / understandable / says something specific about her / really about her, not "we" / shows they "gets" other people — plus:
- **S.A.R. structure and Nugget First:** does they open with a one-line thesis before diving in? Is Situation short, Action the bulk of the answer, Result quantified wherever a real number exists (pull from `pm-profile/overview.md` — never let her leave a result vague if a real number is already documented)?
- **Ownership language / "owner vs. participant":** "I" for her specific decisions and judgment calls, "we" for team execution — the single most common senior-candidate failure mode, flagged independently by both books. Watch for it on every answer, not just when it's egregious.
- **Good vs. great achievement:** would this result have happened anyway, or was it specifically caused by her judgment call? If the story doesn't make that causal link clear, push on it — this is a sharper version of "quantify the result."
- **Altitude:** does the answer operate at strategy/outcome level (business terms, cross-functional influence, judgment under ambiguity) or stay in tactical/execution detail? Named, real gap for her (coaching needs: "strategic narrative — practice articulating work in business terms to executives, not just product terms to engineers") — call it out specifically when the answer drifts tactical.
- **Honesty about gaps:** if the question touches a known gap (e.g. credit-risk domain, data-access negotiation), does they name it plainly and briefly, or does they dodge or over-apologize? Both are misses.

**Delivery (DIGS layer):** are the real stakes dramatized rather than flattened into generic activity ("emails and meetings")? Is there a genuine alternative/tradeoff named, so the choice reads as deliberate rather than the only obvious move? Does the story read as a story — named people, real conflict, a landed resolution — rather than a status update?

- **Conciseness:** senior answers are tight — if it would run past ~90 seconds to 2 minutes spoken, flag it as too long and identify what to cut.
- **Anticipate the follow-up:** after grading the core answer, consider whether the standard follow-ups (How did the team react? What did you learn? What would you do differently? What was the baseline/counterfactual?) would expose a weak spot — flag it now rather than let her get caught by it live.

**If the question is case/strategy-shaped rather than behavioral** (e.g. "how would you sequence entry into a new market"), skip the above entirely and structure/assess against the New Market Entry Checklist in `references/decode-and-conquer.md` instead — market characteristics, competitive environment, company fit, applied concretely rather than just recited.

### 3. Give rationale, then a rebuilt answer

Structure the feedback as:
- **What's working** — cite the specific line/moment, not a general compliment.
- **What needs improvement** — specific and actionable, tied to the checklist above, not vague ("be more confident").
- **Rebuilt answer** — write an improved version in her voice, grounded in facts either already establitheyd in her profile/fit-assessment docs or newly confirmed by her in this session. If they introduces a new story or detail, confirm it's accurate as stated before using it (a quick "just to confirm — is that right?" is enough), then build the rebuilt answer around it. If a detail needed to make the answer land (e.g. a specific number) is missing, ask her for it rather than inventing one — don't silently fill gaps.

### 4. Continue the loop

After the rebuilt answer, ask whether they wants to: try the same question again in her own words, move to the next question, or drill into a specific weak spot (e.g. "let's do three more result-quantification reps"). Keep going until they says they's done.

### 5. Save the session

When the practice session ends, save the politheyd answers (not the full back-and-forth) to `applications/<location>/<company>/mock-interview-answers.md` — one clean, reusable version per question covered, so they can review it before the real conversation without re-deriving it.

## Notes

- Keep the tone of the output the way user writes to herself in this project: direct, honest about gaps, no inflated confidence. The fit assessments already model this voice — match it.
- Don't invent conversation stages or interviewers that weren't mentioned — ask rather than assume.
- If user already has notes from a previous round with the same company (e.g. a reply from the contact, like Lars's description of the role scope), fold that context in explicitly rather than re-deriving it generically.
