# KPI baseline row, week 2026-10-19 (FIN-11, ruling C16) — PREPARED skeleton, finish 2026-10-26

Week: Monday 2026-10-19 to Sunday 2026-10-25. Goes into the WBR draft of 2026-10-26
(`business-os/head-of-ecommerce/wbr-template-and-agenda-2026-10-26.md`). Owner appends the row to `kpi-weekly.csv`;
Finance never writes the CSV. Not accounting advice.

## Inputs (fill on 2026-10-26)
| Field | Source | Value | Status |
|---|---|---|---|
| sessions | GA4 G-7TV8PK060Z, Acquisition, 2026-10-19..25 (owner screenshot or CRO weekly baseline) | | TODO owner/CRO |
| orders_site | Squarespace Orders export, same dates, excluding test orders | | TODO owner (row 20 of `owner-inputs-wave2.md`) |
| orders_etsy | Etsy orders (decision 9: is Mareshop selling?) | | TODO owner |
| new_customers / repeat_customers | Squarespace export (first order by email) | | TODO |
| gross_sales_eur, returns_eur | Squarespace export | | TODO |
| ad_spend_eur | Meta/Google: none approved (ruling C10) | 0 only if owner confirms no ads ran | TODO confirm |
| creator_cost_eur | Partnerships `creator-tracker.csv` | 0 only if confirmed | TODO confirm |
| product_cost_eur, shipping_packaging_payment_eur | `sku-economics.csv` x units sold | blank if units > 0 (0 costed SKUs) | TODO |
| on_time_dispatch_pct, units_available | OPS dispatch log, PRD capacity file | | TODO OPS/PRD |

## Derivations (only from filled fields; formulas in `weekly-finance-routine-sop.md` s3)
- net_revenue_ex_vat = (gross - returns) / 1.21; conversion = orders_site / sessions; AOV = net / (site + Etsy orders);
  CAC = (ads + creators) / new_customers; gross margin % and contribution = blank while costs are TODO.
- Zero orders: conversion 0, AOV / CAC / margin blank (division by zero), contribution blank (costs unknown).

## Proposed row (exact CSV header order; blanks stay blank)
```
week_start,sessions,orders_site,orders_etsy,new_customers,repeat_customers,gross_sales_eur,returns_eur,net_revenue_ex_vat_eur,product_cost_eur,shipping_packaging_payment_eur,ad_spend_eur,creator_cost_eur,conversion_rate,aov_eur,cac_eur,gross_margin_pct,contribution_eur,on_time_dispatch_pct,units_sold,units_available,notes
2026-10-19,,,,,,,,,,,,,,,,,,,,,"BASELINE DRAFT: TODO all inputs (owner exports due 2026-10-26); test orders #00003/#00004 excluded"
```
