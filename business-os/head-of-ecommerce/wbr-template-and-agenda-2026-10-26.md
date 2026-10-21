# Weekly Business Review — agenda + template, first run Mon 26 Oct 2026 (DRAFT)

Author: Head of E-commerce / GM (agent), 2026-10-21. Skill: `aw-weekly-business-review`. Covers week
`week_start` 2026-10-19 (Mon) to 2026-10-25 (Sun) = baseline row (ruling C16).

## 1. Data request — owner, by Mon 26 Oct 09:00 (about 15 minutes)
| # | Item | Source | Fills |
|---|---|---|---|
| 1 | Orders 19-25 Oct, export or screenshot (exclude test #00003/#00004) | Squarespace > Commerce > Orders | `orders_site`, `gross_sales_eur`, `returns_eur`, `new_customers`, `repeat_customers`, `units_sold` |
| 2 | Etsy orders 19-25 Oct (or "Etsy closed") | Etsy shop stats | `orders_etsy` |
| 3 | Sessions 19-25 Oct, total and by source | GA4 `G-7TV8PK060Z` > Reports > Acquisition (screenshot) | `sessions` |
| 4 | Ad and creator spend (confirm EUR 0 if nothing ran) | Meta/Google accounts, creator log | `ad_spend_eur`, `creator_cost_eur` |
| 5 | Merchant Center Diagnostics: approved / pending / disapproved | MC screenshot | Gate G6 |
| 6 | Answers to the 24 Oct decision pack | [owner-decision-pack-2026-10-24.md](owner-decision-pack-2026-10-24.md) | Gates, priority SKUs |
| 7 | Any dispatch in the week (none expected) | Ops log | `on_time_dispatch_pct` |

Department inputs the GM reads (not owner): Finance cash forecast 26 Oct, Production capacity list 23 Oct,
CRO/SEO/Growth weekly notes if present in `business-os/<dept>/`.

## 2. Agenda (30 minutes, owner + GM)
| Min | Item | Output |
|---|---|---|
| 0-5 | One line + scorecard (outputs: revenue, orders, contribution) | Agreed facts for the week |
| 5-12 | Controllable inputs: sessions by source, MC status, PDP fixes shipped, SKUs safe to promote, creator/gift status | What moved, what did not |
| 12-18 | Gate tracker G0-G9: changes, items past due | [gate-tracker.md](gate-tracker.md) updated |
| 18-25 | Decisions (max 3) | Owner yes/no |
| 25-30 | Owner Monday batch: max 15-min tasks, ordered by gate | One list for the week |

## 3. Template (copy to `business-os/reviews/wbr-YYYY-MM-DD.md` once the owner approves that folder)
```markdown
# WBR week of 2026-10-19 — DRAFT for owner
**One line:** <single most important fact>

## Scorecard
| KPI | This wk | Last wk | 4-wk avg | Flag |
|---|---|---|---|---|
| Net revenue ex VAT (EUR) | | n/a (first row) | n/a | |
| Orders (site / Etsy) | | n/a | n/a | |
| Sessions | | n/a | n/a | |
| Conversion rate | | n/a | n/a | |
| AOV (EUR) | | n/a | n/a | |
| CAC new customers (EUR) | | n/a | n/a | |
| Gross margin % | TODO: no SKU costs (G1) | | | |
| Contribution after acquisition (EUR) | TODO: no SKU costs (G1) | | | |
| On-time dispatch % | | | | |
| Sell-through | TODO: real stock (decision 4) | | | |

## Variances (only flagged lines; rule: >20% and >EUR 50, or any order change under 10/week)
## Inputs we control
## Gates (changes since last week)
## Decisions for owner (max 3)
| # | Decision | Evidence | Owner | By | Reversible / approval |
## Owner Monday batch (max 15-min tasks, by gate)
## Missing data / TODO
## Proposed kpi-weekly.csv row (owner pastes after approval)
```

## 4. Proposed baseline row skeleton (fill only from item 1-7 above; blank = unknown)
Header order matches `business-os/kpi-weekly.csv`:
```
week_start,sessions,orders_site,orders_etsy,new_customers,repeat_customers,gross_sales_eur,returns_eur,net_revenue_ex_vat_eur,product_cost_eur,shipping_packaging_payment_eur,ad_spend_eur,creator_cost_eur,conversion_rate,aov_eur,cac_eur,gross_margin_pct,contribution_eur,on_time_dispatch_pct,units_sold,units_available,notes
2026-10-19,,,,,,,,,,,,,,,,,,,,,"Baseline. TODO owner: Squarespace orders (excl. test #00003/#00004), Etsy orders, GA4 sessions, spend confirm. product_cost/shipping TODO until SKU costs (G1). units_available TODO until stock count (decision 4)"
```
Derivations once filled: net revenue = (gross - returns) / 1.21 (accountant confirms per-country VAT); conversion =
orders_site / sessions; AOV = net revenue / all orders; CAC = (ad + creator) / new customers; contribution only when
cost columns exist.

## 5. Decisions likely on 26 Oct (proposals, max 3)
1. Confirm the provisional 5 SKUs if not done 24 Oct (owner, reversible).
2. Approve channels A + B for test ([first-meeting-proposal.md](first-meeting-proposal.md)) (owner, reversible, EUR 0 until gift cap).
3. Lock the production-input session date this week (G0) (owner, reversible).

DRAFT for owner. Not posted or sent.
