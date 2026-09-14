---
name: company-research
description: Use this skill whenever user needs to understand a company's product, market positioning, business model, and competitive landscape before applying, before an interview, or when assessing fit. Produces a structured research document covering company overview, product deep dive, competitive landscape, target customers, business model, market tailwinds, org and culture signals, strategic signals, and what the specific role actually requires — grounded enough to answer "tell me about our product" or a competitive positioning question in an interview, not just make small talk. Triggers on "research this company", "product research for [company]", "competitive analysis", "help me understand [company]'s product", "company deep dive", "prep before I apply".
---

# Company & Product Research

Produces a grounded research document on a specific company and product before user applies, interviews, or needs to assess fit. This is the evidence base that `fit-assessment.md` and the `interview-prep` skill draw on — it doesn't replace either, it feeds them.

## When to run this

- Before writing a fit-assessment.md for a new company, especially if the domain is unfamiliar
- Before applying, if the goal is a sharper, more specific case for why this company
- Before any interview stage past a recruiter screen, so user can speak to product positioning and competitive landscape without improvising live
- Whenever user asks for "company research", "product research", "competitive analysis", or "help me understand what they build"

## 1. Identify the target and where it lives

Ask if not already clear from context:
- Company name and the specific role (title, team or domain if named)
- Which application folder this belongs to (e.g. `applications/oslo/trackunit/`) — create it if it doesn't exist yet, following the existing `<location>/<company-slug>/` convention used elsewhere in this project
- Whether a `fit-assessment.md` already exists in that folder. If so, read it first — it usually already has a first-pass company summary and named gaps. This research should deepen and correct that, not duplicate it from zero
- Whether the JD is already available (pasted earlier in conversation, or saved in the folder) — use it to know which specific product area to go deep on. A generic company profile is far less useful than one weighted toward the actual team's product surface

## 2. Research

Use WebSearch and WebFetch. Prioritize primary sources over secondary summaries:
- The company's own site: product pages, pricing page, changelog or blog, careers page (culture signals), any public roadmap
- Recent press: funding rounds, leadership changes, layoffs, major launches — anything from the last 6 to 12 months signals current strategic priority
- Competitors: identify 3 to 5 real ones, not just the obvious brand name, and how the company positions against them. Check the company's own comparison or "vs" pages if they have them — those reveal exactly which battles they think they're fighting
- Review sites (G2, Capterra, Trustpilot) for real customer language, common complaints about competitors, and what buyers actually weigh. This is often sharper positioning intel than the marketing site
- LinkedIn: team size, growth trajectory, who's currently hiring, exec backgrounds, especially the hiring manager and their manager if known
- If the product is technical or platform-shaped: enough architecture detail to have a credible engineering conversation — API model, deployment options, integration surface, whatever the JD itself signals matters. Calibrate depth the way the n8n and Jotta research already in this project does: deep enough to discuss trade-offs, not a general-audience explainer

Don't stop at the marketing pitch. The bar is the same one user's own fit assessments use: real tensions, not brochure copy. Every section should earn its place by being something that would change how they answer a question or what they ask in return.

## 3. Structure the output

Write to `applications/<location>/<company>/company-product-analysis.md`. Use these sections, dropping any that don't apply and adding company-specific ones that do:

- **TL;DR pitch** — 3 to 4 sentences: what they do, how they make money, how they're positioned, in language user could say out loud in a meet-and-greet
- **Company basics** — founded, size, funding or ownership structure, HQ, revenue if public
- **Product portfolio** — every product line, one line each, with the specific one relevant to the role marked clearly
- **Product deep dive** — the specific product area the role owns: what it is, current stage (MVP, GA, mature), technical model if relevant, how it's priced
- **Competitive landscape** — a table: competitor, type, their advantage over the company, the company's advantage over them. Real trade-offs in both directions, not one-sided
- **Target customer segments** — who buys, what pain, why this product over the alternative, primary versus secondary segments
- **Business model** — pricing structure, monetization levers, anything genuinely undecided or owned by this specific role
- **Market tailwinds** — regulatory, structural, or demand-side forces making this a good or bad time to be building this product
- **Recent strategic signals** — funding, launches, leadership changes, public statements, each with a one-line read on what it tells you about current priorities
- **Key tensions for a PM to know** — the real trade-offs this role will navigate daily. Usually the single most useful section for interview answers
- **Org and culture signals** — team size, reporting line, work culture norms (especially where the local culture isn't English-default or has a strong brand identity), anything the JD or reviews reveal about how decisions actually get made
- **What the role actually requires** — restate the JD's core mandate and the profile they're describing, then connect it back to `profile/00-overview.md` explicitly: where the fit is genuinely strong, where user would need to name and bridge a gap out loud

## 4. Optional: styled HTML version

If user wants something easier to skim on a phone before a call, render the same content as a styled HTML page using `references/html-template.html` as the visual pattern: hero header with key stats, a TL;DR callout box, card grids, a table for the competitive comparison, colored highlight and warning boxes for signals and tensions. Save alongside as `company-product-analysis.html`. This is a nice-to-have, not a substitute — the markdown is the source of truth other skills and future sessions read from.

## 5. Close the loop

- If no `fit-assessment.md` exists yet for this company, say so explicitly and offer to build one next. This research is the input; the fit assessment is the judgment call built on top of it
- If a `fit-assessment.md` already exists and this research surfaces something that changes the read (a gap that's smaller or bigger than assumed, a location or comp detail, a competitive fact that strengthens or weakens the pitch), flag it directly rather than leaving the fit assessment quietly stale
- Note that this document now exists so it's picked up naturally the next time `interview-prep` runs for this company
