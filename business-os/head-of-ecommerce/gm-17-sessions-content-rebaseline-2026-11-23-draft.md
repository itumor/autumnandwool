# Sessions / content target re-baseline (GM-17, DRAFT skeleton)

Author: GM (agent), 2026-10-21. Task GM-17 (re-baseline sessions/content targets after 4 weeks of data, C9).
Due 2026-11-23. Everything below is a skeleton: no number is filled until 4 complete WBR rows exist in
`business-os/reviews/` and the owner approves the reset. Re-baseline never happens in advance of the data.

## 1. Gate to fire (do not start before)
- [ ] 4 complete WBR rows in `business-os/reviews/wbr-YYYY-MM-DD.md` (one per Monday, data batch complete).
- [ ] GM-11 weekly loop running (Mondays 2 Nov-28 Dec).
- [ ] Owner yes to re-baseline (decision point, max 3 decisions in the WBR).
If fewer than 4 rows arrive, the target date slips to the Monday after the 4th complete row; never in advance.

## 2. Inputs (all TODO until they arrive; GA4 = sessions only)
| Input | Source | Week rows used | Status |
|---|---|---|---|
| Sessions total | GA4 `G-7TV8PK060Z` weekly | rows 1-4 of `business-os/reviews/` | TODO |
| Sessions by source/medium | GA4 acquisition | rows 1-4 | TODO (A-GM-12 applies) |
| Orders (site / Etsy) | Squarespace + Etsy weekly | rows 1-4 | TODO (revenue never from GA4) |
| Net revenue ex VAT | Squarespace + Etsy (owner export) | rows 1-4 | TODO |
| Merchant Center approved count | owner screenshot | rows 1-4 | TODO (G6) |
| Content published (posts / pins / emails) | AW content calendar + `aw-content-calendar` log | rows 1-4 | TODO owner department |
| Gross margin / contribution | `unit_economics.py` after G1 | rows 1-4 (if available) | TODO |

## 3. Re-baseline method (fill in on 23 Nov)
1. Compute the 4-week averages for sessions and content outputs from the WBR rows above (no assumptions).
2. Compare against the current assumed session/content targets (`assumptions-wave3.md` A-GM-* rows referenced there).
3. Flag any line where the 4-week average differs from the assumed target by more than 20%.
4. Propose new targets as ranges (owner confirms a direction, decision 35 pattern) rather than point values.
5. Log the change in `gate-tracker.md` only if a gate condition is met, with evidence.

## 4. Re-baselined targets (DRAFT; fill only after steps 1-3)
| Channel / content | Current assumed target | 4-wk avg measured | Proposed new target | Flag (>20%) | Owner yes |
|---|---|---|---|---|---|
| Sessions (total) | TODO | TODO | TODO | | |
| Sessions organic (Google) | TODO | TODO | TODO | | |
| Sessions Pinterest | TODO | TODO | TODO | | |
| Sessions creator (UTM) | TODO | TODO | TODO | | |
| Posts published per week | TODO | TODO | TODO | | |
| Pins published per week | TODO | TODO | TODO | | |
| Email sends per week | TODO | TODO | TODO | | |
| Merchant Center approved listings | TODO | TODO | TODO | | |

## 5. Content measurement prep cross-check (CRE-24)
Align with `aw-content-calendar` reviewed KPIs and `aw-ecommerce-seo` (GSC impressions/CTR by 14 Nov baseline).
Any content target that still depends on an unverified assumption stays `ASSUMED` with its A-ID.

## 6. Decisions for owner (max 3)
| # | Decision | Evidence | Owner | By | Reversible |
|---|---|---|---|---|---|
| 1 | Accept re-baselined session targets | 4 WBR rows | | 23 Nov | Yes |
| 2 | Accept re-baselined content targets | content log | | 23 Nov | Yes |
| 3 | Keep or drop any target still unmeasurable | | | 23 Nov | Yes |

## 7. Missing data / TODO (blank until supplied)
- 4 complete WBR rows (`business-os/reviews/`).
- Content output log for weeks 2-8 Nov (owner/department).
- G1 closure so contribution columns exist (only then can a sessions->revenue link be drawn, and attribution is
  correlation only until G7 passes).

**DRAFT skeleton. No number pasted. No change to `business-os/kpi-weekly.csv` or targets until owner approves.**
