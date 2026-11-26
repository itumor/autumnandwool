# FIN-11 — closeout check 2026-11-26

## Task
Baseline `kpi-weekly.csv` money columns, week 2026-10-19 (ruling C16), in WBR of 2026-10-26 — due 2026-10-26

## What the deliverable requires
- One baseline row, week_start 2026-10-19 (Mon 2026-10-19 to Sun 2026-10-25), exact CSV header order; money columns filled: gross_sales_eur, returns_eur, net_revenue_ex_vat_eur, product_cost_eur, shipping_packaging_payment_eur, ad_spend_eur, creator_cost_eur, conversion_rate, aov_eur, cac_eur, gross_margin_pct, contribution_eur (+ sessions, orders_site, orders_etsy, new/repeat customers, on_time_dispatch_pct, units_sold, units_available, notes).
- Sources per field: Squarespace Orders export (test orders #00003/#00004 excluded), GA4 sessions G-7TV8PK060Z 2026-10-19..25, Etsy orders, Stripe payouts/fees, `business-os/sku-economics.csv` x units sold, OPS dispatch log, PRD capacity, ad/creator logs; zero only when source confirms zero, else blank + TODO.
- Formulas (`business-os/finance/weekly-finance-routine-sop.md` s3): net_revenue_ex_vat=(gross-returns)/1.21; conversion=orders_site/sessions; AOV=net/(site+Etsy orders); CAC=(ads+creators)/new_customers; margin=(net-product_cost)/net; contribution=net-product_cost-shipping_packaging_payment-ads-creators; blank on missing inputs; zero-order rules.
- Proposed row in WBR draft `business-os/head-of-ecommerce/wbr-template-and-agenda-2026-10-26.md`; owner appends row to `business-os/kpi-weekly.csv`; Finance never writes the CSV; ruling C16.

## Repo evidence found
- `business-os/finance/kpi-baseline-2026-10-19.md` — prepared skeleton; all inputs TODO; proposed blank row; test-order exclusion note.
- `business-os/finance/weekly-finance-routine-sop.md` — s1 export list, s3 money-column formulas, owner-appends rule.
- `business-os/kpi-weekly.csv` — header only; no week 2026-10-19 row; no data rows.
- `business-os/head-of-ecommerce/wbr-template-and-agenda-2026-10-26.md` — WBR draft target exists.
- `business-os/sku-economics.csv` — 82 SKUs; cost columns blank; 0 costed SKUs; stock values look like placeholders.
- `business-os/finance/anomaly-log.md` — test orders #00003/#00004 amounts TODO; duplicate titles; placeholder stock; Squarespace 2% FEE [VERIFY].
- `business-os/partnerships/creator-tracker.csv` — header only; `business-os/growth/ads-results-log.csv` — week 2026-10-19 spend 0, sessions/orders MISSING.
- `PROJECT-HANDBOOK.md` s7 — only orders are test #00003/#00004 placed + refunded; storefront sellable.
- `evidence/first-sale-2026-11-02/owner-unblock.md` — "store sellable, 0 real orders" (2026-11-02; outside this week).
- No Squarespace Orders export, GA4 export, Stripe payout, or bank data anywhere in repo.

## Verdict
HELD — owner/live data not in repo

## Missing inputs
- Owner form row 20 (`business-os/finance/owner-inputs-wave2.md`): Squarespace Orders export week 2026-10-19..10-25 excluding test orders + GA4 sessions same week.
- Etsy orders for week + decision 9 (is Mareshop selling?) + Etsy payment activity/fees if active.
- Owner-confirmed new/repeat split (first order by email); gross_sales_eur + returns_eur; units_sold; on_time_dispatch_pct + units_available from OPS/PRD.
- Owner-confirm ad_spend_eur = 0 (ruling C10) + ad log; creator_cost_eur = 0 + updated `creator-tracker.csv`.
- Owner-confirmed per-unit costs in `business-os/sku-economics.csv` for product_cost_eur/shipping_packaging_payment_eur (FIN-03/G1; currently blank).
- Owner appends proposed row to `business-os/kpi-weekly.csv`; accountant confirms VAT 21% per country [VERIFY] for /1.21.
- Stripe lines for test orders #00003/#00004 tie-out (amounts; fee-not-returned question) if relevant.

## Next action
Owner supplies row-20 exports for week 2026-10-19..10-25 and appends the proposed row to `business-os/kpi-weekly.csv`, with the proposed row shown in the WBR of 2026-10-26.
