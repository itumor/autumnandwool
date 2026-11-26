# FIN-23 — closeout check 2026-11-26

## Task
October monthly finance review — due 2026-11-06

## What the deliverable requires
- Completed `business-os/finance/monthly-finance-2026-10.md` (template `monthly-finance-review-template.md`); one-line money fact; every number labelled Actual/Forecast/Illustrative with source.
- §1 Cash October 2026: opening bank balance 2026-10-01; receipts (Stripe, PayPal, Etsy, other payouts); payments by category; closing balance 2026-10-31; buffer/headroom; forecast variance vs `cash-forecast-2026-10-26.md`.
- §2 Payroll/contractors (none expected ruling C13; confirm).
- §3 Profitability by SKU (only sold SKUs; owner-confirmed `business-os/sku-economics.csv` costs; CM1 %; CM2 EUR/order vs minimum contribution FIN-05).
- §4 Profitability by channel, never blended (site organic, Google free listings, Etsy, creators, paid, markets).
- §5 Returns/refunds (test orders #00003/#00004 excluded; listed); §6 anomalies carried from `anomaly-log.md`; §7 max 3 owner decisions.
- October exports per owner form row 19 (`accountant-pack-2026-10.md` s1 list); tie-out notes vs FIN-21 accountant pack draft; owner sends; Finance books nothing.

## Repo evidence found
- `business-os/finance/monthly-finance-2026-10.md` — prepared skeleton; every figure TODO; states 0 real site orders to 2026-10-19; test orders excluded; known anomalies; 3 pre-filled decisions.
- `business-os/finance/monthly-finance-review-template.md` (FIN-22); `business-os/finance/accountant-pack-2026-10.md` (FIN-21 draft; s1 items 1–12 MISSING; s3 tie-out notes; accountant deadline TODO).
- `business-os/finance/owner-inputs-wave2.md` row 19 — October exports request, due 2026-11-03.
- `business-os/finance/cash-forecast-2026-10-26.md` — forecast baseline; variance N/A (forecast starts 2026-10-26 per skeleton).
- `business-os/finance/anomaly-log.md` — test orders #00003/#00004 amounts TODO; duplicate titles; placeholder stock; Squarespace 2% FEE [VERIFY]; PayPal [VERIFY] in pack.
- `PROJECT-HANDBOOK.md` s7 — 2 test orders placed + refunded; storefront fully sellable; Stripe chain proven; no real orders known.
- `evidence/first-sale-2026-11-02/owner-unblock.md` — "store sellable, 0 real orders" as of 2026-11-02; PayPal pending (FIN-15); not October data.
- `business-os/sku-economics.csv` — 0 costed SKUs; `products_Oct-17_10-46-00PM.csv` is a products export, not orders.
- No October Squarespace Orders CSV, Stripe payout report, bank statement, or invoices anywhere in repo.

## Verdict
HELD — owner/live data not in repo

## Missing inputs
- Owner row 19 exports after month-end: Squarespace Orders CSV 2026-10-01..10-31; Stripe payout report + fee lines; October bank statement; invoices.
- Invoices: Squarespace plan/domain/backup; software (MailerLite, Canva, AI); yarn/materials; packaging/shipping; ads; accountant + bank fees; market stalls; creator/contractor.
- Confirm PayPal status / no PayPal receipts (FIN-15); confirm ads/creators EUR 0; confirm payroll none; confirm Etsy October activity + Etsy statement (decision 9).
- Tie-out test orders #00003/#00004: amounts + Stripe charge/refund/fee-not-returned lines; accountant answers fee question.
- Owner-confirmed per-SKU costs (FIN-03/G1; `sku-cost-proposals-staging.csv` not confirmed); confirm Squarespace plan + 2% fee [VERIFY]; VAT 21% per country [VERIFY accountant].
- Owner decisions §7: cash buffer FIN-07 (+ fixed-cost list FIN-06 rows 2,6), Squarespace plan upgrade, minimum contribution FIN-05; headroom needs opening/closing bank balances.

## Next action
Owner supplies row-19 October exports + invoices after month-end; then re-open prepared skeleton `business-os/finance/monthly-finance-2026-10.md` and fill it from those exports.
