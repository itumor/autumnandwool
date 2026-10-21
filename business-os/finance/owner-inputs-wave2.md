# Owner inputs for Finance, wave 2 — ONE form, DRAFT for owner (2026-10-21)

Ask: fill the "Your answer" column. 15 rows, most take one line. Earliest due 2026-10-24.
This form replaces the scattered asks in `owner-finance-inputs-2026-10-21.md`, `min-contribution-method.md`,
`spend-checks-q4-2026.md` and `payment-paths-and-payouts.md` (those stay as detail sheets; answer here, Finance copies).
Rules: balances and dates only, no card or full bank account numbers. Finance logs in nowhere, pays nothing, sends nothing.
Not accounting, tax or investment advice; the accountant has the final word.

Wave-2 check (2026-10-21): other departments' wave-1 files were read. None supplies a cost, rate, balance or perk
price yet, so every row below still needs the owner (sources at the end).

## A. Cash (unblocks FIN-07, FIN-17, all spend verdicts, FIN-08 roll-forward)
| # | Question | Why | Due | Unblocks | Your answer |
|---|---|---|---|---|---|
| 1 | Bank balance EUR + as-of date (ISO); Stripe, Etsy, PayPal balances + dates | Without it the forecast shows net change only; no "can we afford" answer is possible | 2026-10-28 | FIN-07, FIN-17, FIN-16 verdicts, FIN-23 | |
| 2 | Fixed-cost list: item, EUR, monthly/yearly, next pay date (fill table in `owner-finance-inputs-2026-10-21.md` s2) | Buffer = 8 weeks of fixed costs; overhead share per order | 2026-10-28 | FIN-07, FIN-05, FIN-26 | |
| 3 | Squarespace plan name (Basic / Core / Advanced) and billing (monthly/annual) | Basic = 2% store fee on every order (EUR 0.90-3.30 per order at current prices) | 2026-10-28 (upgrade decision 2026-11-04) | FIN-03 (`payment_eur`), FIN-16 s1 | |
| 4 | Stripe and Etsy payout schedule + lag sale -> bank (days) (Stripe > Settings > Payouts; Etsy > Finances) | When cash arrives | 2026-10-28 | FIN-08 roll-forward, FIN-17 | |
| 5 | Committed spend already approved (item, EUR, pay date) | Goes in its real week | 2026-10-28 | FIN-08, FIN-17 | |
| 6 | Approve cash buffer: 8 weeks of fixed costs (EUR figure computed by Finance once row 2 is filled) | Trigger to pause uncommitted spend | 2026-10-28 (after row 2) | FIN-07 | [ ] approve 8 weeks  [ ] other: ____ weeks / EUR ____  initials + date: |

## B. Product cost and margin (unblocks FIN-03, FIN-05, FIN-18, FIN-19)
| # | Question | Why | Due | Unblocks | Your answer |
|---|---|---|---|---|---|
| 7 | Approve the GM's 5 priority SKUs (`business-os/head-of-ecommerce/priority-5-sku-proposal-2026-10-21.md`) or swap | Which 5 SKUs get break-even CAC first | 2026-10-24 | FIN-03 | |
| 8 | Production inputs G0: yarn grams + EUR per garment, minutes per garment, labour rate EUR/h (via Production timing sheet, PRD-06/07) | `materials_labour_eur` | 2026-10-28 (8 SKUs by 2026-10-31) | FIN-03, FIN-05 | |
| 9 | Confirm cost proposals and write them into `sku-economics.csv` yourself (G1). Staging sheet: `sku-cost-proposals-staging.csv` | Finance never writes the CSV | 5 SKUs 2026-11-04, 22 SKUs 2026-11-11 | FIN-03, FIN-05 | |
| 10 | Returns allowance per order: your assumption (EUR or % of net) | Last CM2 column; no return history exists | 2026-11-04 | FIN-03 | |
| 11 | Minimum contribution per order, EUR (Finance proposes once rows 2 and 9 are in; method in `min-contribution-method.md`) | Max CAC = CM2 - minimum | 2026-11-04 (fallback 2026-11-11) | FIN-05, FIN-27 | EUR ____ initials + date: |
| 12 | Carrier(s) and price per region for one sweater parcel (LV, EU-18, EE/LT, US/CA/AU, other); fill `business-os/operations/carrier-rates.md` with Operations | `shipping_eur`; free-shipping keep/drop per region (decision 21) | carrier choice 2026-10-28, rates 2026-11-11 | FIN-03, FIN-18 | |
| 13 | Gift perks you would offer (gift note, wrap, gift receipt) and their unit cost EUR + minutes | Perks cut CM2 on every gift order (decision 31) | 2026-11-11 | FIN-19 | |

## C. Payments, markets, accountant (unblocks FIN-15, FIN-17, FIN-21..25)
| # | Question | Why | Due | Unblocks | Your answer |
|---|---|---|---|---|---|
| 14 | Connect PayPal (decision 14), then one test order + refund; send Finance the order number and refund date | Second payment path; test order excluded from sales | 2026-10-31 | FIN-15 | order #____ refunded on ____ |
| 15 | Market stall: which one (if any), fee + extras quoted, physical units you would bring | Stall verdict needs fee, stock and cash after fee. Baltic EXPO fee is non-refundable | Baltic EXPO ASAP; KuKu 2026-11-10; White Xmas 2026-12-14 | FIN-17 | |
| 16 | Physical stock count for the 22 visible SKUs (esp. turtleneck 360, beanie 220) and which 3 duplicate-title pairs are true duplicates | Stock drives stall and promo verdicts; also year-end inventory | 2026-10-31 (5 priority 2026-10-24) | FIN-03, FIN-17, FIN-25 | |
| 17 | Accountant: name, monthly document deadline (day), VAT return frequency + due dates, year-end deadline, stock-count method for 31 Dec | Pack due dates and VAT payment weeks are guesses until answered | 2026-11-06 | FIN-21, FIN-23, FIN-24, FIN-25 | |
| 18 | Send `accountant-questions-2026-10-21.md` to the accountant (you send, not Finance) | VAT/OSS, Etsy fees, markets, gifts | 2026-11-06 | FIN-25, FIN-26 | sent on: |
| 19 | October exports after month-end: Squarespace Orders CSV, Stripe payout report, bank statement, invoices (list in `accountant-pack-2026-10.md` s1) | October pack and review | 2026-11-03 | FIN-23 (FIN-21 tie-out) | |
| 20 | Squarespace Orders export for week 2026-10-19..10-25 and GA4 sessions for the same week | First `kpi-weekly.csv` baseline row | 2026-10-26 | FIN-11 | |
| 21 | Squarespace backup copy site: keep, export or let expire (trial ends 2026-11-01); plan fee if kept | Second plan fee in the forecast | 2026-10-31 | FIN-16 s6, FIN-08 | |

## Sources checked in wave 2 (2026-10-21)
- `business-os/operations/carrier-rates.md`: template only, "no rate is filled"; carrier choice = owner decision 8.
- `business-os/head-of-ecommerce/priority-5-sku-proposal-2026-10-21.md`: provisional 5 SKUs, all CM2 unknown.
- `plans/2026-2027/status/production.md`: PRD-06/07/09 blocked on owner; PRD files blocked by write hook.
- `business-os/ecommerce-cro/2026-10-21-pdp-copy-proposals.md` l.111 and `business-os/customer-experience/support-macros.md`:
  gift wrap / note "not offered, cost unknown", decision 31 open.
- `business-os/growth/budget-proposal-2026-12.md`: December paid test EUR 0 unless 6/6 gates pass by 2026-11-20.
- Stall fees: only KuKu EUR 50.00 published (`spend-checks-q4-2026.md` s2).
