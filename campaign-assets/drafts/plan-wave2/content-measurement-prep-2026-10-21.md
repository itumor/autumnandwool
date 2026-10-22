DRAFT — for owner approval

# Content measurement: monthly review skeletons (CRE-25) and KPI re-baseline method (CRE-24)

Prepared 2026-10-21 (wave 2). **Not final**: both need real data. Finish dates: October review 2 Nov, November
1 Dec, December 4 Jan; re-baseline 23 Nov (ruling C9). Final files go to `business-os/content-review-2026-MM.md`
after owner approval (drafted here until then).

Data rules (Growth `utm-taxonomy.md` s1, s7): sessions from GA4 `G-7TV8PK060Z` filtered by `utm_campaign` /
`utm_content`; orders from **Squarespace Orders** only. GA4 has no purchase events, so "orders from content" means an
order placed in the same session window or a customer answer; never add platform-reported conversions. Views and
followers are context only, never a KPI.

## Part 1. Monthly review template (copy per month)

```
DRAFT — for owner approval
# Content review — 2026-MM
Period: 1-[last] [month]. Data pulled: [date] by owner (GA4 export, Squarespace Orders export).
Posts live this month: [n] (list IDs). Drafted but held: [n] + gate (G2/G8/decision 18 ...).

| Format | Pillar | Posts | UTM sessions | Product-page sessions | Orders (Squarespace) | Revenue EUR | Saves/shares (context) | Keep / change / drop |
|---|---|---|---|---|---|---|---|---|
| Making-of Reel | Making in Riga | | | | | | | |
| Texture / fit Reel | Product truth | | | | | | | |
| Styling Reel | Styling | | | | | | | |
| Founder | Kristine / Mareshop | | | | | | | |
| Carousel | Product truth | | | | | | | |
| Pin | (board) | | | | | | | |
| Stories link sticker | — | | | | | | | |

Top 3 posts by UTM sessions: ...
SKU x creative pairs for Growth paid tests (only GREEN SKUs, only if sessions > 0): ...
Rule applied: drop a format with 0 UTM sessions after 4 posts.
Photo backlog: [n of 24 colours photographed and bound].
Next month: keep / change / drop list.
Claim check result: ... Open [VERIFY]: ...
```

### October 2026 (due 2 Nov): expected content
- Posts live: likely 0-2 (W44 plan: VS-A Thu 29 Oct, VS-D Sat 31 Oct if Kristine's words arrive). If 0: the review
  states "no posts live, no content data" and lists the gates that held posts (decisions 6, 18, 20; G2; G8).
- Baseline row: Instagram/Pinterest sessions 0 of 64 (owner decision pack 31 Oct, decision 18 "current state").
- Photo backlog: 0 of 24 at 21 Oct (photo brief).

### November (due 1 Dec) and December (due 4 Jan)
Same table. November adds the W48 Black Friday read (`utm_campaign=black-friday-2026`); December adds the
order-by posts (CO-1..4) and a Q4 summary row for GRO-23 / CRE-30 comparison.

## Part 2. KPI re-baseline (23 Nov, C9)

Current targets are placeholders (Q4 calendar note, ruling C9). After 4 weeks of posts (W44-W47):

| KPI | Measure | Week 1-4 actual | Proposed target W48-W53 | Method |
|---|---|---|---|---|
| Qualified visits | UTM sessions per post, median | [from GA4] | median x 1.2, floor 1 | Median, not mean (one viral post skews) |
| Sales from content | Orders with a content UTM session (Squarespace + GA4 timing) | [n] | keep at actual if < 3; else +1/week | Squarespace Orders = truth |
| Output | Videos per week | [n] | 3-5 (hiring plan) | Count posted, not drafted |
| Output quality | Owner first-time approval rate | [approved / submitted] | ≥ 80% | From owner replies |
| Photo backlog | Colours photographed and bound | [n of 24] | 24 by 14 Nov (C7) or trim (decision 29) | Photo brief tick list |

Owner approves the targets (GM-17 aligns the session targets across departments).

## Sources

`business-os/growth/utm-taxonomy.md`; `.claude/skills/aw-content-calendar/SKILL.md` (monthly review);
`plan-wave1/content-calendar-q4-2026.md`, `content-calendar-2026-W44.md`; `business-os/head-of-ecommerce/owner-decision-pack-2026-10-31.md`
(decision 18 current state); master plan ruling C9.

## Claim check result

Pass: templates only, no customer-facing claims.

## Open [VERIFY]

- Owner provides GA4 and Squarespace Orders exports on review dates (same exports as Growth/GM Monday batch).
