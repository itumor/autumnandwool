# Weekly finance routine, every Monday (FIN-09, FIN-10) — DRAFT SOP

Owner: aw-finance prepares; owner supplies exports and approves; GM receives findings. Time box: 60 minutes.
Not accounting advice. Read-only: work only from exports the owner provides. No logins, no edits, no sending.

## 1. Collect (by Monday 10:00; list what is missing in the WBR "Missing data" section)
| Export | From | Covers |
|---|---|---|
| Squarespace Orders CSV | Owner | Orders, gross sales, refunds (source of truth for site orders) |
| Etsy orders + payment account activity | Owner | Etsy orders, fees, payouts (kept separate from site) |
| Stripe payouts + balance | Owner (screenshot/CSV) | Payout dates, fees per charge |
| Bank movement for the week | Owner | Actual cash in/out (truth for variance) |
| Ad + creator log | Growth / Partnerships | Spend, new customers per channel (UTM per `business-os/growth/utm-links.csv`) |
| GA4 sessions | GM/CRO | Sessions only; never orders or revenue from GA4 |

## 2. Roll the cash forecast
1. Copy last week's forecast to `business-os/finance/cash-forecast-YYYY-MM-DD.md` (Monday date).
2. Drop the past week, add week 13. Replace forecast W1 with actual bank movement.
3. Variance: forecast vs actual per line; explain every gap over EUR 100 (driver, one-off or continuing, action).
4. Re-run Base and Downside. Flag first week below buffer and below zero. If breached: flag to owner, recommend
   pausing uncommitted spend. Do not pause anything.

## 3. Check the WBR money columns (comments in the WBR draft, never the CSV)
Check each derived field against these formulas (from `aw-weekly-business-review`):
| Field | Formula | Check |
|---|---|---|
| `net_revenue_ex_vat_eur` | (gross_sales - returns) / 1.21 | Test/refunded orders excluded; VAT rate per country [VERIFY accountant] |
| `aov_eur` | net_revenue_ex_vat / (orders_site + orders_etsy) | Blank if 0 orders |
| `cac_eur` | (ad_spend + creator_cost) / new_customers | New-customer CAC, never blended across channels |
| `gross_margin_pct` | (net_revenue - product_cost) / net_revenue | TODO while cost columns blank |
| `contribution_eur` | net_revenue - product_cost - shipping_packaging_payment - ad_spend - creator_cost | TODO while cost columns blank |
| `product_cost_eur`, `shipping_packaging_payment_eur` | `sku-economics.csv` per-unit costs x units sold | TODO until owner-confirmed costs |
Rules: zero only when the source confirms zero; otherwise blank + `TODO:` in notes. Proposed row goes in the WBR; the
owner appends to `kpi-weekly.csv`. Baseline row `week_start` 2026-10-19, drafted in the WBR of 2026-10-26 (ruling C16).

## 4. CAC guardrail
For each live campaign/creator: CAC per channel vs break-even CAC (`contrib` from `unit_economics.py`) of the SKUs it
sold. Over break-even = stop/fix flag to GM with EUR impact. Today: no campaigns live, break-even CAC unknown.

## 5. Anomalies
Append to `anomaly-log.md`: refunds, duplicate orders, fee mismatches, payouts missing, test orders. Flag only.

## 6. Hand-off to GM (short findings, max 5 lines)
Format: `<finding> | EUR impact | action needed | who`.
