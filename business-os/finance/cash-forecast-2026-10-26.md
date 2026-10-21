# Cash forecast from 2026-10-26 (FIN-08) — DRAFT for owner
Prepared 2026-10-21 ahead of the first Monday roll (2026-10-26). Re-check on 2026-10-26 with any inputs received.
Opening balance: **UNKNOWN: net change only.** No bank balance supplied (owner input due 2026-10-28). Never assumed.
Buffer: **TODO** (proposal: 8 weeks of fixed costs; fixed-cost list not supplied). Not accounting, tax or investment advice.

## Weekly view (weeks start Monday)
All payment cells are TODO because no fixed-cost list, invoices or payment dates exist. Receipts are EUR 0.00 in Base
because there are 0 real orders (the two test orders #00003/#00004 were refunded and are excluded). This is a
zero-sales base case, not a prediction that nothing will sell.

| Week | Receipts Base | Payments | Net Base | Closing Base | Closing Downside |
|---|---|---|---|---|---|
| W1 2026-10-26 | 0.00 | TODO | TODO | net change only | net change only |
| W2 2026-11-02 | 0.00 | TODO | TODO | net change only | net change only |
| W3 2026-11-09 | 0.00 | TODO | TODO | net change only | net change only |
| W4 2026-11-16 | 0.00 | TODO | TODO | net change only | net change only |
| W5 2026-11-23 | 0.00 | TODO | TODO | net change only | net change only |
| W6 2026-11-30 | 0.00 | TODO | TODO | net change only | net change only |
| W7 2026-12-07 | 0.00 | TODO | TODO | net change only | net change only |
| W8 2026-12-14 | 0.00 | TODO | TODO | net change only | net change only |
| W9 2026-12-21 | 0.00 | TODO | TODO | net change only | net change only |
| W10 2026-12-28 | 0.00 | TODO | TODO | net change only | net change only |
| W11 2027-01-04 | 0.00 | TODO | TODO | net change only | net change only |
| W12 2027-01-11 | 0.00 | TODO | TODO | net change only | net change only |
| W13 2027-01-18 | 0.00 | TODO | TODO | net change only | net change only |

**Lowest point:** cannot compute (no opening balance, no payments). **Runs below buffer:** cannot compute.

## Payment lines to fill (one row per item, in its real week)
| Line | Amount EUR | Week(s) | Source | Status |
|---|---|---|---|---|
| Squarespace plan | TODO | renewal date TODO | Owner billing page | TODO: owner |
| Squarespace backup copy (trial ends 2026-11-01) | TODO or 0.00 if left to expire | W1/W2 | Owner decision | TODO: owner |
| Tools (MailerLite, Canva, AI) | TODO | TODO | Owner | TODO: owner |
| Accountant | TODO | TODO | Accountant invoice | TODO: owner |
| VAT / tax payments | TODO | TODO | Accountant | TODO: accountant |
| Salaries / contractors | none known; no hire in Q4 2026 (ruling C13) | - | master-plan | Confirm 0.00 with owner |
| Yarn / materials | TODO | TODO | Production | TODO: PRD |
| Packaging stock | TODO | TODO | Production/OPS | TODO |
| Shipping (only when orders ship) | 0.00 in Base | - | follows orders | - |
| Ads / creators | 0.00 (EUR 0 default, ruling C10; no approved spend) | - | master-plan | Actual policy |
| Market stalls | 0.00 until owner books; candidates in `spend-checks-q4-2026.md` | - | Owner decision 27 | Not committed |

## Scenarios
- **Base:** 0 orders (current run-rate), payments as listed once known.
- **Downside:** sales 50% of Base (= 0.00), payouts one week later (no effect at 0), plus one unplanned cost
  (amount TODO; proposal: the largest single monthly fixed cost). Downside = Base payments + that cost.
- **Upside:** not shown. No evidence of a proven channel (0 real orders, 62-64 visits in 30 days).
- When the first real order arrives: receipts = net of refunds, shifted by the Stripe payout lag (TODO owner).

## Risks (max 5, by EUR impact; amounts TODO)
1. Unknown opening balance: any committed spend (stall, yarn, upgrade) may already exceed cash. Impact: whole balance.
2. Unpriced free shipping (EU, UK, NO, CH, US): each order costs carrier fees we do not know. Impact per order TODO (OPS).
3. Non-refundable stall fees (Baltic EXPO) or yarn bought before any proven order. Impact TODO.
4. VAT payable on sales at destination rates not yet confirmed (OSS). Impact TODO (accountant).
5. Squarespace Basic 2% transaction fee [VERIFY plan]: EUR 0.90-3.30 per order at current prices.

## Assumptions (each sourced)
- 0 real orders to date: `PROJECT-HANDBOOK.md` s7, `weekly-measurement-report-2026-10-19.md`.
- Test orders #00003/#00004 refunded, excluded: `PROJECT-HANDBOOK.md`.
- No paid spend approved: master-plan ruling C10 (default EUR 0 December test).
- No hire in Q4 2026: master-plan ruling C13.
- Everything else: TODO (see `owner-finance-inputs-2026-10-21.md`).

## Variance vs last week
First forecast; no prior week to compare. From 2026-11-02, compare this file's W1 to actual bank movement; explain gaps over EUR 100.

## Spend question
None asked this week. Open worksheets: `spend-checks-q4-2026.md` (verdicts need the opening balance).
