---
name: competencies
description: Assess PM competencies against the Ravi Mehta framework by analyzing CV, presenting findings, and capturing calibration. Invoked after cv-intake during onboarding, or anytime to update competencies after new experience.
---

# Competencies Assessment

Assesses the user's product management competencies using the Ravi Mehta 12-competency framework. Runs once after CV intake during onboarding to establish a baseline, and can be re-invoked anytime to update after acquiring new skills or experiences.

## The Framework

The Ravi Mehta framework organizes 12 PM competencies into 4 areas, each critical to driving business impact:

### Product Execution (the ability to build exceptional products)
- **Feature Specification**: Gather requirements, define functionality, set goals in clear, actionable format
- **Product Delivery**: Work with engineering/design to iteratively and quickly deliver product functionality
- **Quality Assurance**: Identify, prioritize, and resolve technical, functional, and business quality issues

### Customer Insight (the ability to understand and deliver on customer needs)
- **Fluency with Data**: Use data to generate actionable insights, connect quantified goals to business outcomes
- **Voice of the Customer**: Leverage user feedback in all forms to understand engagement and drive meaningful outcomes
- **User Experience Design**: Define UX requirements and deliver designs that are easy to use and follow best practices

### Product Strategy (the ability to drive business impact via product innovation)
- **Business Outcome Ownership**: Drive meaningful outcomes for the business by connecting product to strategic objectives
- **Product Vision & Roadmapping**: Define overall vision for the product and clear roadmap of prioritized features
- **Strategic Impact**: Understand and contribute to business strategy, bring strategy to fruition through consistent delivery

### Influencing People (the ability to rally people around the team's work)
- **Stakeholder Management**: Identify stakeholders impacted by your area and work with them to factor requirements into decisions
- **Team Leadership**: Manage and mentor direct reports to enable them to deliver, improve, and achieve career objectives
- **Managing Up**: Leverage senior managers and executives to help achieve goals and influence strategic direction

Each competency is assessed at three levels: **Needs Focus**, **On Track**, or **Outperform**.

## Mode: Initial Assessment (Onboarding)

Run this after `cv-intake` completes during first-time onboarding.

### 1. Extract competencies from CV

Read `pm-profile/cv.md` and `pm-profile/level.md`. For each of the 12 competencies, look for evidence in their experience:

**Product Execution signals:**
- Feature Specification: mentions of PRDs, requirements gathering, user stories, feature specs
- Product Delivery: shipping cadence, cross-functional coordination, sprint/release mentions, velocity
- Quality Assurance: testing mindset, QA process ownership, bug prioritization, reliability focus

**Customer Insight signals:**
- Fluency with Data: analytics, metrics, dashboards, A/B testing, data-driven, cohort analysis
- Voice of the Customer: user research, interviews, user testing, feedback loops, customer insights
- UX Design: design collaboration, interaction design, usability, UX mindset, design-led approach

**Product Strategy signals:**
- Business Outcome Ownership: revenue impact, growth, retention metrics, business goals, outcome focus
- Product Vision & Roadmapping: strategic roadmap, product vision, long-term planning, prioritization frameworks
- Strategic Impact: competitive positioning, market strategy, business strategy alignment, executive alignment

**Influencing People signals:**
- Stakeholder Management: cross-functional work, leadership alignment, buy-in, influence without authority
- Team Leadership: managed PMs/APMs, mentoring, team building, direct reports, people development
- Managing Up: executive alignment, resource negotiation, board exposure, C-level collaboration

### 2. Build the assessment

For each competency, assign one of three levels based on evidence:
- **Outperform**: Explicit evidence of mastery; core part of their experience; multiple relevant projects/roles
- **On Track**: Clear evidence; expected for their level; demonstrates the skill regularly
- **Needs Focus**: Limited or no clear evidence; area to develop; not a primary strength in their history

Provide a one-sentence rationale for each, tied to their CV.

### 3. Present findings

Show the user a radar chart visualization (using text if needed) of all 12 competencies with:
- Their assessed level for each
- A short rationale sentence for each (e.g., "Shipped 10+ features per quarter as PM at [company]" → Product Delivery: On Track)

Format as a clear, scannable assessment they can quickly review.

### 4. Validate and capture calibration

Ask the user:

> Here's my assessment of your competencies based on your CV. Does this match how you see yourself? Any adjustments, or areas where you think I missed something?

For each area they flag:
- If they disagree with a rating, ask why and update the assessment
- If they want to add nuance, capture their calibration note (e.g., "Fluency with Data: On Track, but mostly in growth metrics — less experienced with product analytics")
- If they point out a gap the CV didn't reveal, update that competency's rationale

### 5. Deduce level based on CV + competencies profile

Now that you have both CV evidence and demonstrated competencies, deduce their seniority level. Use this vocabulary:

| Slug | Reads as |
| --- | --- |
| `junior-ic` | 0–2 years, executing defined tasks |
| `mid-ic` | 2–5 years, owns features or a product area end to end |
| `senior-ic` | Owns a domain, makes trade-offs unsupervised, mentors informally |
| `staff-ic` | Influence across teams, sets patterns others follow, no headcount |
| `principal-ic` | Sets direction at org level |
| `lead-ic` | Hands-on, owns a team's direction and delivery, no formal headcount |
| `people-manager` | Headcount, hiring, performance; manages individual contributors |
| `senior-manager` | Manages managers or several teams |
| `director-plus` | Org-level leadership, budget, strategy |

**Weigh these in order**, letting strongest evidence win:

1. **Competencies profile.** Their demonstrated spikes and gaps signal their level. A user outperforming in Strategy but Needs Focus in Execution reads junior-ic or mid-ic. Outperforming in Strategy + Influencing People reads senior-ic or above.
2. **CV scope.** Domain ownership, team size, org impact.
3. **Headcount.** Formal reports move toward manager track; hands-on work alongside reports keeps them IC.
4. **Years.** Sanity check only. Fifteen years in mid-ic is a signal you've misread something.

**Report the deduction.** One line: "Based on your competencies profile and CV scope, I'm reading you as **[slug]**. This reflects [brief rationale]. If this doesn't match, let me know."

### 6. Save full assessment

Write to `pm-profile/competencies.md` with this structure:

```markdown
# Competencies

## Level

- **Current:** [deduced from CV + competencies assessment]
- **Target:** unknown — set in this section when the user states what they want next

### Evidence
- [title and scope signals from CV]
- [key competencies that informed the level deduction]

### Notes
Deduced by `competencies` skill on [date] based on CV evidence and demonstrated competencies assessment. Override by editing this section; every skill reads it rather than re-deriving, so a correction propagates everywhere.

## Competencies Assessment

**Assessment Date:** [today]

### Product Execution
- **Feature Specification:** [Level] — [Rationale]. [Calibration note if any]
- **Product Delivery:** [Level] — [Rationale]. [Calibration note if any]
- **Quality Assurance:** [Level] — [Rationale]. [Calibration note if any]

[... same for Customer Insight, Product Strategy, Influencing People ...]

## Calibration Notes

[Any adjustments or context the user provided]
```

## Mode: Update (Anytime)

User can invoke this skill anytime they've acquired new experience (completed a course, took on new scope, led a new initiative).

### 1. Load current assessment

Read `pm-profile/competencies.md`. Show the user their current assessment.

### 2. Ask what changed

> What's changed since we last assessed? New role, project, or skill you want to add?

### 3. Update specific competencies

Ask about only the competencies they mention. For each:
- Explain the current rating and rationale
- Ask if the new experience changes it, and why
- Update the assessment and save

Do not re-assess competencies they didn't mention.

## Notes

- **Grounding in evidence:** Every rating is tied to real experience from their CV or the story they just told. No generic assessments.
- **Competencies evolve with level:** Early PMs (APM/PM) spike in Execution; mid-level (Sr. PM/GPM) add Strategy; senior (Director+) emphasize Influencing People. See Ravi Mehta framework for level expectations.
- **No balanced scorecard goal:** Users will have spikes and gaps. That's intentional — the framework explicitly says "individuals should be spiky; teams should be well-rounded." Do not push them toward balance.
- **Calibration is part of the data:** Their notes explain context the CV doesn't. A user saying "I rated myself On Track in Fluency with Data, but it's really growth-specific" is more useful than a raw rating.
- **Tied to role-fit:** The role-fit skill will use this competencies assessment (plus level) to evaluate whether they're a fit for a posting. A role requiring strategic vision + data fluency will flag a user who spikes in execution but lags in both.
