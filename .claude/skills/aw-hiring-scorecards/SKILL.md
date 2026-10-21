---
name: aw-hiring-scorecards
description: Use when writing or revising a job scorecard, job post, interview kit, take-home task or candidate debrief for an Autumn & Wool role (GM, growth marketer, CRO, creative, production, ops, CX, partnerships, accountant), or deciding hiring order from business-os/hiring-plan.md.
---

# Hiring Scorecards and Interview Kits

## Purpose
Hire for outcomes, not activity. Every role gets a scorecard (mission, 3-6 measurable outcomes, 4-6
competencies) before any job post is written. Candidates are scored against it, not against gut feel.
Source of truth for roles, hiring order and 90-day goals: `business-os/hiring-plan.md`.

## Procedure
1. **Check need and timing.** Read the wave table in `hiring-plan.md`. Is the trigger met (e.g. Wave 3 only when
   orders exceed one person's packing capacity; Wave 4 only when creator tests show profitable orders)? If not,
   say so and propose a contractor/part-time or founder-covers option instead.
2. **Mission** (1-3 sentences): why the role exists, tied to revenue, profit, product quality or retention.
3. **Outcomes** (3-6, ranked): each = result + number + date, mapped to a `kpi-weekly.csv` column or a named
   deliverable. Take them from the role's "First 90 days" in `hiring-plan.md`. Bad: "manage social media".
   Good: "3-5 short videos/week from week 2; by day 60 content-attributed sessions measured via UTM".
   Unknown baselines -> "establish baseline by day 30", never an invented target.
4. **Competencies** (4-6): 2-3 role-specific (e.g. Meta + Google small-budget testing; knitwear costing;
   Squarespace commerce + GA4) + 2-3 company-wide: commercially minded (reads contribution, not views), honest
   with numbers and product claims, works with a small founder-led team, writes clearly.
5. **Interview kit** per competency: 2 behavioural questions ("Tell me about a time..."), 1 situational question
   using Autumn & Wool facts (README section 2 + illustrative order economics section 9), and probes
   ("what was the number before/after", "what did you do personally").
6. **Work sample** (paid if longer than 2 hours; payment is an owner decision): small, real-shaped task with
   public/sanitised data. Examples: GM -> 1-page 30-day plan from README; growth -> test plan capped at
   break-even CAC from the illustrative EUR 155 example; CRO -> audit one PDP screenshot; production -> cost sheet
   for a sweater from given inputs.
7. **Rubric** 1-4 per outcome-relevant competency, with anchors written per role:
   1 = no evidence / measures in views or tasks, 2 = some evidence, not their own results, 3 = clear owned result
   with numbers in a comparable setting, 4 = repeated owned results at our scale (small DTC/handmade, EU shipping).
8. **Job post** (draft only): impact-first summary, outcomes (not duty list), must-haves (max 5), location/remote,
   hours, pay as a figure or band from the owner (`TODO: owner` if not given). EU/Latvia: no age, gender, family
   or nationality requirements; state language needs honestly (English, Latvian if truly required).
9. **Debrief template**: each interviewer scores alone before discussion; evidence per score; decision hire / no
   hire; top risk and how the first 30 days would test it.
10. Save to `business-os/hiring/<role-slug>-scorecard.md` (DRAFT). Never publish posts or contact candidates.

## Output template
```markdown
# <Role> — Scorecard (DRAFT, owner to approve)
Wave: N | Trigger met? yes/no (evidence) | Reports to: | Hours/contract: TODO owner | Pay band: TODO owner

## Mission
## Outcomes (ranked)
| # | Outcome | Measure (kpi-weekly column / deliverable) | By day |
## Competencies
| Competency | What good looks like here | Rubric anchors 1-4 |
## Interview kit
### <Competency>
- Behavioural: ...  - Situational (A&W): ...  - Probes: ...
## Work sample
Task, inputs given, time cap, paid?, how scored.
## Debrief
| Interviewer | Competency | Score | Evidence |  Decision: | Top risk:
## Job post draft
```

## Standard interview question (all roles, from hiring-plan.md)
"What are the first three things you do in your area, and how will we know in 30 days if they worked?"
Reject answers measured only in views, followers or tasks done.

## Guardrails
- Pay, contract type, hours and start date are owner decisions; leave TODO.
- No legal templates (contracts, offer letters) as final; employment terms in Latvia need a local adviser.
- Score evidence, not charisma. Same questions for every candidate of a role.
- Do not store candidate personal data in this repo beyond names/initials in a debrief the owner keeps.
- Never post jobs, message candidates or schedule interviews; produce drafts only.

## Sources
- Anthropic `knowledge-work-plugins`, human-resources/skills/interview-prep/SKILL.md —
  https://github.com/anthropics/knowledge-work-plugins (Apache-2.0). Adapted: 4-6 competencies, behavioural +
  situational questions with probes, same questions per candidate, 1-4 rubric, debrief step.
- Anthropic `knowledge-work-plugins`, small-business/skills/job-post-builder/SKILL.md (Apache-2.0). Adapted:
  impact-first post, pay only as figure/band, never publish without the user.
- Geoff Smart & Randy Street, "Who: The A Method for Hiring" (book, copyrighted; idea only, own words; summary
  seen at https://findthesource.beehiiv.com/p/recruiting-2-the-scorecard): scorecard = mission + ranked
  outcomes + competencies, written before sourcing.
- Compared and not used: Workable/Indeed JD templates (duty lists, not outcomes).
