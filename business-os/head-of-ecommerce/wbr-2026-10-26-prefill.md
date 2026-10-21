# WBR week of 2026-10-19 — PRE-FILLED DRAFT on assumptions (for Mon 26 Oct)

Author: GM (agent), 2026-10-21, task GM-07. Template: `wbr-template-and-agenda-2026-10-26.md`. Pre-filled on the wave-3
registers: `head-of-ecommerce/assumptions-wave3.md` (A-GM-*), `knitwear-making/assumptions-wave3.md` (Production),
`operations/assumptions-wave3.md` (Operations). **Every cell marked ASSUMED is a placeholder, not a reported number.**
On Mon 26 Oct, GM replaces each ASSUMED/TODO cell with the owner's export and moves this to `business-os/reviews/wbr-2026-10-26.md`.
Orders and revenue come only from the Squarespace Orders export and Etsy (GA4 has no purchase events).

**One line (provisional):** at the last check (19 Oct) the store had 0 real orders and about 64 visits per 30 days. The week's job
is to get the owner to confirm the 15 wave-3 assumptions (`owner-unblock-pack.md` top section). Without that, no cost or CAC
number can become real.

## Scorecard
| KPI | This wk (19-25 Oct) | Last wk | 4-wk avg | Flag | Basis |
|---|---|---|---|---|---|
| Net revenue ex VAT (EUR) | TODO: Squarespace export | n/a (first row) | n/a | | Owner export. Not assumed |
| Orders (site / Etsy) | TODO / TODO | n/a | n/a | any order = flag (volume < 10/wk) | Context only, not a value: 0 real orders up to 19 Oct (handbook s7). Test #00003/#00004 excluded |
| Sessions | TODO: GA4 | n/a | n/a | | Context: ~64 per 30 days, so roughly 15 per week would be "normal" (illustrative) |
| Conversion rate | derive | n/a | n/a | | orders_site / sessions |
| AOV (EUR) | derive | n/a | n/a | | net revenue / all orders |
| CAC new customers (EUR) | n/a if spend is 0 | n/a | n/a | | ASSUMED spend EUR 0 (A-GM-07, A-GM-08). Owner confirms per account |
| Gross margin % | ASSUMED per Production register (CM1 per SKU), applied only to units actually sold | | | | `knitwear-making/assumptions-wave3.md` |
| Contribution after acquisition (EUR) | derive from sold units x assumed CM2 - spend | | | | Production + Ops registers. Labelled "on assumed costs" |
| On-time dispatch % | n/a if no order shipped | | | | Ops log |
| Sell-through | ASSUMED stock per Production register | | | | Not the 17 Oct export placeholders (beanie 220, turtleneck 360) |

## Inputs we control (status 21 Oct; GM updates on 26 Oct)
- Sessions by channel: GA4 screenshot TODO owner. UTM taxonomy assumed approved (A-GM-12), so links tag from this week.
- Merchant Center: approved count TODO owner (row 3). Gate G6.
- PDP fixes shipped: none (product data frozen; A-GM-19 proposals only). CRO has 5 priority PDP packs ready.
- SKUs safe to promote: none GREEN. Production register gives assumed costs. A SKU stays AMBER until the owner confirms costs (G1).
- Campaigns live: none. Paid EUR 0 (A-GM-08). Creator gifts: 0 shipped (A-GM-17; waits on G4).

## Gates (assumption mode: drafting may proceed, the gate itself is not cleared)
| Gate | Real status | Proceeding on |
|---|---|---|
| G0 production inputs | Not cleared | Production register (times, yarn, labour, stock) |
| G1 costs confirmed | Not cleared | Production register costs -> CM2 "assumed" |
| G3 cash | Not cleared | A-GM-09 scenarios. Spend verdicts are conditional |
| G5 delivery/cutoffs | Not cleared | Operations register |
| G7 measurement | Not cleared | A-GM-05 stay on Basic, A-GM-06 UTM-only attribution |
| G8 claims | Not cleared | A-GM-10 allowed wording |
| G9 legal | Not cleared | A-GM-16 returns, A-GM-14 consent (strictest) |
| G2, G4, G6 | Not cleared | No assumption possible (need GREEN list, PayPal, MC approval) |

## Decisions for owner (max 3)
| # | Decision | Evidence | Owner | By | Reversible / approval |
|---|---|---|---|---|---|
| 1 | Tick or correct the 15 wave-3 assumptions (top of `owner-unblock-pack.md`) | 7 departments built on them in wave 3. Each correction is a one-line change and a re-run | Owner | 28 Oct | Yes. Corrections are free |
| 2 | Set a 2-hour production-timing session this week, so the assumed costs for the 5 priority SKUs can be replaced with timed ones (G0) | Every CM2, min contribution and CAC cap rests on assumed costs today | Owner | 25-28 Oct | Yes |
| 3 | Approve test channels A + B at EUR 0 media (A-GM-07) | `first-meeting-proposal.md` | Owner | 26 Oct | Yes, no spend |

## Owner Monday batch (max 15-minute tasks, by gate)
1. Orders export 19-25 Oct + Etsy count + GA4 acquisition screenshot + "ad spend EUR 0" yes/no (row 10).
2. Merchant Center Diagnostics screenshot (row 3).
3. Wave-3 assumption ticks (15 rows, about 15 minutes).
4. Billing + Discounts screenshots (row 17). This confirms or overturns A-GM-05/06.

## Missing data / TODO
- sessions, orders_site, orders_etsy, new/repeat customers, gross_sales, returns, units_sold: owner export (row 10).
- ad_spend_eur, creator_cost_eur: ASSUMED 0 until the owner confirms per account.
- units_available: Production register (assumed) until physical count (decision 4).

## Proposed kpi-weekly.csv row (owner pastes only after the real export; ASSUMED values are not pasted)
```
week_start,sessions,orders_site,orders_etsy,new_customers,repeat_customers,gross_sales_eur,returns_eur,net_revenue_ex_vat_eur,product_cost_eur,shipping_packaging_payment_eur,ad_spend_eur,creator_cost_eur,conversion_rate,aov_eur,cac_eur,gross_margin_pct,contribution_eur,on_time_dispatch_pct,units_sold,units_available,notes
2026-10-19,,,,,,,,,,,,,,,,,,,,,"Baseline (C16). TODO owner: Squarespace orders excl. test #00003/#00004, Etsy orders, GA4 sessions, ad/creator spend confirm (assumed 0, A-GM-08). Costs: assumed per knitwear-making/assumptions-wave3.md, not pasted until owner confirms G1"
```

DRAFT for owner. Not posted or sent.
