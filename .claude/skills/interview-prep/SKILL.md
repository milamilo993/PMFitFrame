---
name: interview-prep
description: Use this skill whenever user is preparing for an upcoming interview or interview-stage conversation in her job search — a meet-and-greet, recruiter screen, hiring manager call, panel, technical/case round, or final/executive round. Two modes: (1) generates a calibrated written prep doc (questions to expect and questions to ask) grounded in the company's fit assessment; (2) runs a live, turn-by-turn mock interview where user answers behavioral/situational questions out loud and gets assessed and coached toward a senior/principal-level answer. Triggers on "prep for interview", "interview prep", "prepping for [company] call", "mock questions", "meet and greet prep", "practice interview questions with me", "mock interview", "quiz me on behavioral questions".
---

# Interview Prep

Prepares user for a specific upcoming conversation in her job search. Two distinct modes — pick based on what they's asking for:

- **Mode A — Prep document.** they want a written brief before a call. Produces a calibrated question list saved to the company's folder, `job-pipeline/applications/<company-slug>/`. See "Mode A" below.
- **Mode B — Live mock interview.** they wants to practice out loud, in the conversation, right now. You play interviewer; they answers; you assess and help her rebuild the answer. See "Mode B" below.

Never dump the entire question bank regardless of mode or stage.

## Reference library — the book behind the questions

This skill does not invent interview questions from memory. It runs off a **book**: one or more interview guides sitting in `.claude/skills/interview-prep/docs/` as `.md` files extracted from the source PDF, carrying `<!-- page N -->` markers. The book supplies the question bank and the grading rubric; the user's own files (`fit-assessment.md`, `cv.md`, and `competencies.md`, which carries the `<level-slug>` in its Level section) supply the calibration. Both modes draw on it.

**What ships.** The repo ships with *The Heap Book of Questions*, a free interview question guide, plus whatever else the user has added. That is the default bank. This project was originally built against *Cracking the PM Interview* (McDowell & Bavaro) and *Decode & Conquer* (Lewis Lin) — both paid books, neither redistributable, so no condensation of them is in this repo. Never cite them as though they were on disk.

**Any book works.** The library is source-agnostic: whatever `.md` files are in `docs/` at that moment *are* the bank. A user who owns a paid guide drops its extracted markdown into `docs/` and it becomes the source with no change to this skill. Say this plainly when the library looks thin, when the user asks why a question feels generic, or when they ask what the questions are based on — they should know which book is answering them, and that they can swap it.

Working rules:

- **Check the folder before you rely on it** — `ls .claude/skills/interview-prep/docs` — and read any `.md` in it. This is the skill's own reference material, so rule 2 of `CLAUDE.md` does not apply to it. Don't read a whole book into context: grep for the topic, then read the pages around the hit.
- **Use the `.md` files, never the `.pdf` alongside them.** The markdown is the extracted, cleaned text; re-parsing a PDF when the `.md` exists wastes the session and loses the page markers.
- **A PDF with no `.md` sibling is not yet usable.** Tell the user the book is present but unextracted and offer to extract it before proceeding.
- **If `docs/` holds no usable `.md` at all**, say so in one line — the question bank is empty and the questions will be generic — offer to extract a book the user supplies, and fall back to the rubric written into this skill. Don't silently pretend a bank exists.
- **Cite the page** whenever a question or framework comes from the book, e.g. "per `the-heap-book-of-questions.md` p.62". That lets the user go to the printed page and check it.
- **Some pages are marked `*(no extractable text — image-only page)*`.** That means a figure or cover, not missing content — don't report it as a gap and don't try to infer what the image said.

What to use it for, and what not to:

- **Do** use it as the question bank and the framework source — technical question sets, behavioural patterns, interviewer-side perspective, common candidate mistakes, how answers get graded.
- **Don't** let it set the calibration. The stage, the seniority and the honest gaps come from `fit-assessment.md` and `pm-profile/competencies.md`. A generic question from a book, asked at the wrong level, is worse than no question.
- **Don't** paste book text into the reply as the deliverable. Questions get adapted to the user's actual profile and the specific role; the source is a reference, not the output.

## Mode A — Prep Document

1. **Identify the conversation.** Get from user (ask if not given):
   - Company and role
   - Stage/format: meet-and-greet / intro, recruiter screen, hiring manager, panel, technical or case round, final/executive round
   - Duration
   - Who they's meeting (name, title, if known)

2. **Ground it in what's already known.** Look for and read:
   - `job-pipeline/applications/<company-slug>/fit-assessment.md` — pulls the honest gap assessment, bridging strategy, "what to expect in the process," and top prep priorities already written for this company. This is the primary source of *content* — the question bank below only supplies *form*.
   - `job-pipeline/applications/<company-slug>/company-product-analysis.md` — if it exists (produced by the `company-research` skill), pulls product positioning, competitive landscape, and key tensions. Use this to ground product-sense and case-round questions in real specifics about the company rather than generic frameworks, and to give user real ammunition for "questions to ask them." If it doesn't exist and the round is a panel/case or later stage, suggest running `company-research` first — going in without it means product-sense answers stay generic.
   - `pm-profile/cv.md` and `pm-profile/competencies.md` — for metrics, gaps, and self-rated pillars to draw on or avoid overclaiming.
   - Any prior outreach notes in the same company folder (e.g. `outreach-to-*.md`) for context already established with this contact (what's already been said, what's already been asked/answered).
   - If no fit assessment exists yet for this company, say so and offer to build one first (see the role-fit assessment pattern used elsewhere in this project) — going into a conversation without one means prep is generic rather than grounded.

3. **Calibrate depth to stage.** The question pool comes from the book(s) in `docs/` (grep for the topic, read around the hit), used as a pool and not as a script. Books group their material differently — map the stage onto that book's own chapters rather than assuming a fixed category numbering:
   - **Meet-and-greet / intro:** rapport and motivation questions only, ~6-10 questions max. No case studies, no CIRCLES, no technical drilling. The goal is mutual fit exploration, not evaluation.
   - **Recruiter screen:** rapport, plus logistics and motivation framing.
   - **Hiring manager:** rapport + behavioral/STAR + one light product-sense question, not several.
   - **Panel / case round:** full product sense, calibrated to sub-type (design/improvement/growth/strategy/launch — pick the one closest to the role's actual mandate), plus technical questions if the role is technical/platform-leaning, plus AI-PM material if the role is AI-native or AI-adjacent.
   - **Final/executive round:** leadership and communication, with emphasis on strategic narrative over tactical execution detail.
   - If the book on file has nothing on a stage's topic (many guides skip AI-PM entirely), say so in one line and tell the user a different book in `docs/` would cover it — don't quietly fill the hole from memory.
   - Rule of thumb for volume: roughly 1 substantive question per 2–3 minutes of expected discussion time, leaving room for the interviewer's own tangents.

4. **Write the output.** Save to `job-pipeline/applications/<company-slug>/interview-prep-<stage-slug>.md` (e.g. `interview-prep-meet-and-greet.md`, `interview-prep-hiring-manager.md`). Structure:
   - Context line: who, what stage, duration, date
   - Framework reminder (only the ones relevant to this stage — e.g. don't explain CIRCLES for a rapport-only call)
   - The calibrated question list, grouped logically, each with a one-line hook to *this specific role* (pulled from the fit assessment) where relevant — not generic prompts
   - A short "questions user should ask them" section — tailored to genuine open threads from the fit assessment or prior conversation (e.g. compensation/funding stage questions flagged as open, or a follow-up on something the contact already said)
   - If there's a known gap flagged in the fit assessment likely to surface at this stage, name it plainly with the honest bridging line already drafted — don't leave user to improvise a gap answer live for the first time in the room

5. **Publish the prep doc as an Artifact.** Invoke `pipeline-artifacts` Operation 1 with the path to the file just written. It publishes the page, tracks the URL in the `<same-name>-artifact-url.txt` sibling, and hands the URL back. Do this for every prep doc, every stage — the user reads these on a phone in a car park ten minutes before the call, and a markdown file on disk is no use there.
   - One artifact per stage, never one page for all stages. `interview-prep-hr-screen.md` and `interview-prep-technical.md` are separate pages with separate URLs.
   - Re-running prep for the same stage updates the same URL rather than making a second page, because the URL tracker sibling already exists.

6. **Refresh the board so the doc is reachable from the pipeline.** Invoke `pipeline-artifacts` Operation 2. It re-renders `job-pipeline/overview.md` and puts a labelled link to this prep page in that role's **File** column, alongside the fit assessment. Hand the user both links: the prep page and the board.
   - If the stage itself is new information for the pipeline (a screen booked, a round scheduled), pass that to `job-pipeline` Operation 2 first as a status change, then refresh the board once — not twice.
   - This skill's job is still the prep doc. Don't re-run the fit assessment or the outreach steps; those are separate skills.

## Mode B — Live Mock Interview Practice

An interactive loop, not a document. You are the interviewer; user answers in the conversation; you coach. Run it turn by turn — never front-load a list of questions and never answer on user's behalf.

### 0. Set up the round

Ask (if not already clear from context): which company/round is this for, and is there a specific set of expected questions already identified (e.g. a fit assessment's "What to Expect in the Process" section) to prioritize over the general bank. Ground every question in:
- That company's `job-pipeline/applications/<company-slug>/fit-assessment.md` — especially "What to Expect in the Process" and the honest gap list. Real, already-identified likely questions beat generic bank questions — use them first.
-  `pm-profile/cv.md` and `pm-profile/competencies.md` — this is where user's documented stories live (metrics, team scope, the governance-framework story, etc.). Treat these as the baseline, not the ceiling: user will often surface new stories or details live during practice that aren't written down anywhere yet. That's expected and good. When they introduces something new, ask user to confirm it's accurate as stated (numbers, scope, outcome) before building it into a rebuilt answer — the constraint is truthfulness to user's actual experience, not prior documentation. Never invent or embellish a detail yourself; if a number or outcome is missing, ask user for it rather than filling it in.
- **The book(s) in `docs/`** — the question source and the primary rubric for this mode. Grep for the behavioral and storytelling chapters and work from those: the book's own question categories (leadership and influence, challenges, mistakes and failures, successes, teamwork, or whatever taxonomy it uses) drive question selection, and its story-quality checklist drives grading. Cite the page when a question or a grading criterion comes from it. See "Reference library" above for what is on file and what to tell the user about it — in particular, that the bank is whatever book sits in `docs/`, and that they can swap in their own.
- **The bar below** — the assessment dimensions in step 2 are this skill's own floor. Apply them on top of whatever the book says, and rely on them alone (saying so) if the library is empty.

### 1. Ask one question at a time

Pick a single question, state it plainly as an interviewer would (no meta-commentary about which category it's from), and stop. Wait for user's answer. Do not ask a second question in the same turn.

### 2. Assess user's answer against a <level-slug> bar

They are calibrating for Senior/Principal level, not APM/mid-level — hold the bar there. For behavioral/situational questions, run the answer through the book's checklist first, then through the floor below — the content check first, then the delivery check:

**Content (five-question checklist + SAR):** substantial / understandable / says something specific about her / really about her, not "we" / shows they "gets" other people — plus:
- **S.A.R. structure and Nugget First:** does they open with a one-line thesis before diving in? Is Situation short, Action the bulk of the answer, Result quantified wherever a real number exists (pull from `pm-profile/cv.md` — never let her leave a result vague if a real number is already documented)?
- **Ownership language / "owner vs. participant":** "I" for her specific decisions and judgment calls, "we" for team execution — the single most common senior-candidate failure mode, and one every interview guide flags. Watch for it on every answer, not just when it's egregious.
- **Good vs. great achievement:** would this result have happened anyway, or was it specifically caused by her judgment call? If the story doesn't make that causal link clear, push on it — this is a sharper version of "quantify the result."
- **Altitude:** does the answer operate at strategy/outcome level (business terms, cross-functional influence, judgment under ambiguity) or stay in tactical/execution detail? Named, real gap for her (coaching needs: "strategic narrative — practice articulating work in business terms to executives, not just product terms to engineers") — call it out specifically when the answer drifts tactical.
- **Honesty about gaps:** if the question touches a known gap (e.g. credit-risk domain, data-access negotiation), does they name it plainly and briefly, or does they dodge or over-apologize? Both are misses.

**Delivery (DIGS layer — Dramatize the situation, Indicate alternatives, Go through what you did, Summarize impact):** are the real stakes dramatized rather than flattened into generic activity ("emails and meetings")? Is there a genuine alternative/tradeoff named, so the choice reads as deliberate rather than the only obvious move? Does the story read as a story — named people, real conflict, a landed resolution — rather than a status update?

- **Conciseness:** senior answers are tight — if it would run past ~90 seconds to 2 minutes spoken, flag it as too long and identify what to cut.
- **Anticipate the follow-up:** after grading the core answer, consider whether the standard follow-ups (How did the team react? What did you learn? What would you do differently? What was the baseline/counterfactual?) would expose a weak spot — flag it now rather than let her get caught by it live.

**If the question is case/strategy-shaped rather than behavioral** (e.g. "how would you sequence entry into a new market"), skip the above entirely and structure/assess against a market-entry or strategy framework from the book in `docs/` instead — typically market characteristics, competitive environment, company fit, applied concretely rather than just recited. If the library has no such framework, say so and use those three headings directly.

### 3. Give rationale, then a rebuilt answer

Structure the feedback as:
- **What's working** — cite the specific line/moment, not a general compliment.
- **What needs improvement** — specific and actionable, tied to the checklist above, not vague ("be more confident").
- **Rebuilt answer** — write an improved version in her voice, grounded in facts either already establitheyd in her profile/fit-assessment docs or newly confirmed by her in this session. If they introduces a new story or detail, confirm it's accurate as stated before using it (a quick "just to confirm — is that right?" is enough), then build the rebuilt answer around it. If a detail needed to make the answer land (e.g. a specific number) is missing, ask her for it rather than inventing one — don't silently fill gaps.

### 4. Continue the loop

After the rebuilt answer, ask whether they wants to: try the same question again in her own words, move to the next question, or drill into a specific weak spot (e.g. "let's do three more result-quantification reps"). Keep going until they says they's done.

### 5. Save the session

When the practice session ends, save the politheyd answers (not the full back-and-forth) to `job-pipeline/applications/<company-slug>/mock-interview-answers.md` — one clean, reusable version per question covered, so they can review it before the real conversation without re-deriving it.

## Notes

- Pull questions and frameworks from the reference library in `docs/` rather than generating them from memory, and cite the page. See "Reference library" above. If the user has never been told what the bank is built on, tell them once: which book is on file, and that dropping another extracted book into `docs/` replaces it.
- Keep the tone of the output the way user writes to herself in this project: direct, honest about gaps, no inflated confidence. The fit assessments already model this voice — match it.
- Don't invent conversation stages or interviewers that weren't mentioned — ask rather than assume.
- If user already has notes from a previous round with the same company (e.g. a reply from the contact, like Lars's description of the role scope), fold that context in explicitly rather than re-deriving it generically.
