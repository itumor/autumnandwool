# Gate tracker G0-G9 — DRAFT, GM updates every Monday in the WBR

Last update: 2026-10-21 (baseline). Source of gates: `plans/2026-2027/master-plan.md` s3.
Status values: OPEN (not cleared), PARTIAL (some conditions met), CLEARED (all conditions met, evidence linked).
A gate is CLEARED only with evidence (file, screenshot, export). Nothing downstream starts before its gate.

## Summary 2026-10-21
0 of 10 gates cleared. Everything paid stays at EUR 0. The owner is the shared bottleneck on 8 of 10 gates.

| Gate | Condition | Status 21 Oct | Evidence now | Next check | Due | Who clears | Blocks |
|---|---|---|---|---|---|---|---|
| G0 | Production inputs: 3 units timed per priority SKU, yarn grams, people/hours, labour rate, physical stock | OPEN | None supplied | WBR 26 Oct | 25-31 Oct | Owner | All cost, capacity, cash numbers |
| G1 | SKU costs confirmed in `sku-economics.csv`, `unit_economics.py` run | OPEN | `unit_economics.py` 21 Oct: 0 costed / 82 TODO (22 visible TODO) | 4 Nov | 5 SKUs 4 Nov; 22 by 11 Nov | PRD proposes, owner confirms and pastes | BE_CAC, min contribution, GREEN list, any budget |
| G2 | Capacity file GREEN per SKU | OPEN | No capacity file yet; first Friday list 23 Oct (AMBER at best without G1) | 23 Oct, then Fridays | First real GREEN after 4 Nov | PRD | Any product promotion |
| G3 | Cash: opening balance, fixed costs, buffer, 13-week forecast | OPEN | Opening balance unknown; fixed costs not listed (README s8 is illustrative) | 26 Oct (forecast, net change only), 28 Oct (inputs) | 28 Oct | Owner, FIN | Any spend, hires, yarn, markets |
| G4 | Buyable store: PayPal, delivery times, size info, one returns wording, variant photos bound, claims wording | OPEN | Stripe proven (#00003/#00004 refunded). PayPal not connected; no delivery times; variant photos missing (beanie, turtleneck, hat set, cardigan Blue) | 31 Oct (PayPal) | PayPal 31 Oct; rest 14 Nov | Owner, CRO, OPS | Gifts, PR pitches, paid traffic, December push |
| G5 | Carrier-backed delivery ranges + Christmas order-by dates | OPEN | Ranges differ across sources (C8); no carrier data | 31 Oct provisional table | Carrier-backed 14 Nov; publish 20 Nov | OPS | Gift content, banner, Dec test dates, MTO stop date |
| G6 | Merchant Center approved, correct images, real stock status | OPEN | 19 Oct: 98 uploaded, 0 rejected, 0 approved; approval expected from 21 Oct `[VERIFY: owner screenshot of MC Diagnostics]` | 24 Oct | Above 0 by 28 Oct; clean 14 Nov+ | SEO, CRO, owner | Free listings, Shopping test, Pinterest catalog |
| G7 | Measurement: plan decision (Code Injection), attribution verified (discount codes may be plan-locked) | OPEN | GA4 pageviews only; discount availability unverified (decision 11) | 28 Oct (codes screenshot) | Decide 4 Nov | Owner | Conversion-objective ads, funnel read, creator codes |
| G8 | Claims evidence: "handmade", "made in Latvia/Riga", fibre %, one Etsy proof line | OPEN | Claims cleanup only partly verified; Etsy figures conflict (C1) | 31 Oct | 31 Oct | Owner, PRD | Creator DMs, market forms, ads, PDP copy, feed |
| G9 | Legal: adviser review of returns/consent/label wording | OPEN | README s11 question list exists; not sent | 3 Nov | Send 3 Nov; answer TODO | Owner, adviser | Final returns page, post-purchase emails 2-3, win-back, labels |

## Chains (what unlocks what)
- Money chain: G0 -> G1 -> min contribution (4 Nov) -> BE_CAC per priority SKU (15 Nov) -> G2 GREEN -> G3 cash
  check -> owner ceiling -> capped test (3 x BE_CAC per concept). Earliest paid test: after 20 Nov, and only if all
  six Growth gates pass (default EUR 0, ruling C10).
- Traffic chain: G6 + G4 + G8 -> free channels (Google free listings, Pinterest, creators, PR) -> any paid test.
- Season clock: gifts shipped by 30 Nov; creator content live mid-Dec; site freeze 12 Dec; MTO stops at the earliest
  regional cutoff (about 3 Dec EU, unverified, C3).

## Weekly update rule
Each Monday WBR: change status only with evidence; list any gate past due with the owner ask in the Monday batch
(max 15-minute tasks, ordered by gate, ruling C11). Log changes below.

| Date | Gate | From -> To | Evidence |
|---|---|---|---|
| 2026-10-21 | all | baseline OPEN | this file |

DRAFT for owner. No store change, no spend.
