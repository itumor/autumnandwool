# Review templates: Q4 KPI re-baseline (SEO-27) and monthly SEO reviews (SEO-28, SEO-29), 2026-10-21. DRAFT

Author: aw-seo-marketplace. Prepared ahead; filled on the due dates with real exports. No numbers here are measured.

## A. Q4 KPI re-baseline, 23 Nov (SEO-27, ruling C9)
Inputs (all from the owner, weekly): GSC Performance exports (owner-inputs-wave2 row 6) for 4 consecutive weeks,
Merchant Center counts (row 1), GA4 sessions with source = pinterest (Growth readout), Etsy Stats (row 17, if active).

Method
1. Use only weeks with data. If fewer than 3 weekly exports exist by 23 Nov, say so and move the re-baseline to
   15 Jan (C9 fallback); do not extrapolate.
2. For each KPI: 4-week median = new baseline. Proposed Q1 target = baseline + a step the owner approves; I propose
   the step with its reasoning, never a target without a baseline.
3. Judge against contribution, not traffic: a channel with sessions but no orders is flagged, not celebrated.

| KPI | 19 Oct baseline | Wk 1 | Wk 2 | Wk 3 | Wk 4 | 4-wk median | Proposed Q1 target | Reason |
|---|---|---|---|---|---|---|---|---|
| GSC clicks per week | 90-day total 11 | | | | | | | |
| GSC impressions per week | 90-day total 388 | | | | | | | |
| CTR | 2.8% | | | | | | | |
| Queries in top 10 | TODO (export) | | | | | | | |
| Pages indexed / known | 11 / 37 | | | | | | | |
| MC approved items | TODO | | | | | | | |
| Free-listing clicks | TODO | | | | | | | |
| Pinterest outbound clicks | 0 | | | | | | | |
| GA4 sessions source = pinterest | 0 (30 days to 18 Oct) | | | | | | | |
| Etsy visits / conversion / orders | TODO (decision 9) | | | | | | | |

## B. Monthly SEO review (SEO-28 on 30 Nov, SEO-29 on 31 Dec)
File: `business-os/seo-marketplace/<YYYY-MM-DD>-seo-review.md` (aw-ecommerce-seo output format).

```
## Executive summary (top 3 issues, quick wins)
## Indexation: indexed / known, reasons not indexed (owner screenshot), change vs last month
## Findings: Issue | Impact | Evidence | Fix | Layer (copy/native/asset/owner) | Priority
## Query -> page map (query, pos, impressions, target URL, proposed title/meta) - positions 8-20 first
## On-page status: which proposals from 2026-10-21-onpage-proposals.csv the owner applied (owner confirms), which wait
## Schema: Rich Results Test screenshots (owner) for the 5 priority PDPs; Product name/image/offers present?
## llms.txt: diff against live prices, products, policy lines (incl. Etsy proof line per decision 17)
## Feed QA: rows, availability vs owner stock, variant images bound (bind-check CSV), Diagnostics
## Pinterest: pins posted, outbound clicks, GA4 sessions; keep/change/drop per board
## Etsy (if active): batch results, 30-day Stats before/after
## Proposals for next month (max 5, with owner time and EUR cost)
## Unverified
```

Checklist per month
- [ ] GSC export + indexing screenshot received (else review states "no data" for those sections)
- [ ] Rich Results Test screenshots received
- [ ] llms.txt fetched live and diffed
- [ ] Feed TSV re-read; any new rows or price changes vs live PDPs
- [ ] December only: freeze from 12 Dec (CRO-28). Review proposes no live changes for 12–24 Dec; cut-off pins edited
      or archived per the cut-off pins draft calendar
