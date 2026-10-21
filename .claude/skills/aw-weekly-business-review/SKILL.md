---
name: aw-weekly-business-review
description: Use when preparing the Monday weekly business review / weekly P&L review for Autumn & Wool, adding a week to business-os/kpi-weekly.csv, or answering "how did we do last week and what do we scale or stop".
---

# Weekly Business Review (WBR)

## Purpose
One page, every Monday, that tells the owner: what happened last week, why, and the 1-3 scale/stop decisions to
make. Built from `business-os/kpi-weekly.csv`. Output metrics (revenue, contribution) are reported; discussion
focuses on controllable inputs (sessions by channel, conversion, ad spend, SKUs safe to promote, dispatch).

## Inputs (where each number comes from)
| Field in `kpi-weekly.csv` | Source of truth | Note |
|---|---|---|
| `orders_site`, `gross_sales_eur`, `returns_eur` | Squarespace Orders export (owner pastes/exports) | GA4 has **no** purchase events (plan gate). Never take orders from GA4 |
| `orders_etsy` | Etsy shop stats / orders (owner) | Keep separate from site |
| `sessions` | GA4 `G-7TV8PK060Z`, Reports > Acquisition | Pageview-only tracking |
| `ad_spend_eur`, `creator_cost_eur` | Meta/Google ad accounts, creator log | 0 if nothing ran; say so |
| `product_cost_eur`, `shipping_packaging_payment_eur` | `business-os/sku-economics.csv` x units sold | TODO while cost columns are blank |
| `units_available` | Production Manager safe-to-promote list (`aw-production-capacity` if present) | |
| `on_time_dispatch_pct` | Ops log | |

Context: `business-os/README.md` sections 2, 9, 10; `PROJECT-HANDBOOK.md` sections 7-8 (baselines, owner open items).

## Procedure
1. **Collect.** List which inputs the owner has supplied for the week (`week_start` = Monday, ISO date). Any field
   with no source = blank cell + `TODO:` in `notes`. Never estimate orders, revenue or costs.
2. **Derive** (only from filled fields):
   - `net_revenue_ex_vat_eur` = (gross_sales - returns) / 1.21 (LV VAT 21%; confirm rate per order country with accountant)
   - `conversion_rate` = orders_site / sessions
   - `aov_eur` = net_revenue_ex_vat / (orders_site + orders_etsy)
   - `cac_eur` = (ad_spend + creator_cost) / new_customers (new-customer CAC, not blended)
   - `gross_margin_pct` = (net_revenue - product_cost) / net_revenue
   - `contribution_eur` = net_revenue - product_cost - shipping_packaging_payment - ad_spend - creator_cost
3. **Draft the row** for `kpi-weekly.csv`. Do not write to the CSV directly; put the proposed row in the review
   file. The human appends it after approval.
4. **Compare** to last week and to the 4-week average (once 4 rows exist). Flag a variance when it is
   >20% week-on-week **and** >EUR 50 (or any change in orders while volume is under 10/week, since small numbers swing).
5. **Explain each flag** in 2-4 sentences: what changed, the driver with numbers (volume vs price vs mix:
   volume effect = delta orders x last-week AOV; price/mix effect = delta AOV x this-week orders), whether it will
   persist, action (none / monitor / investigate / decide). No vague "timing" or "various".
6. **Check the guardrails**: CAC vs break-even CAC per SKU (`python3 business-os/unit_economics.py`, `contrib`
   column, see `aw-unit-economics`). Any campaign with CAC above break-even = stop/fix candidate.
7. **Decisions.** Propose at most 3, each: decision, evidence, owner, deadline, reversible? Spend increases are
   always "owner approves".
8. **Save** to `business-os/reviews/wbr-YYYY-MM-DD.md` (create folder if missing). Mark it DRAFT.

## Output template
```markdown
# WBR week of YYYY-MM-DD — DRAFT for owner
**One line:** <the single most important fact this week>

## Scorecard
| KPI | This wk | Last wk | 4-wk avg | Flag |
|---|---|---|---|---|
| Net revenue ex VAT (EUR) | | | | |
| Orders (site / Etsy) | | | | |
| Sessions | | | | |
| Conversion rate | | | | |
| AOV (EUR) | | | | |
| CAC new customers (EUR) | | | | |
| Gross margin % | | | | |
| Contribution after acquisition (EUR) | | | | |
| On-time dispatch % | | | | |
| Sell-through | | | | |

## Variances (only flagged lines)
<KPI>: up/down EUR X (Y%) vs last week. Driver: ... Outlook: one-off/continuing. Action: ...

## Inputs we control
Sessions by channel, PDP fixes shipped, SKUs safe to promote, campaigns live, creator posts.

## Decisions for owner (max 3)
| # | Decision | Evidence | Owner | By | Approval needed |

## Missing data / TODO
- <field>: <who supplies it>

## Proposed kpi-weekly.csv row
week_start,sessions,...   (exact column order of the CSV header)
```

## Guardrails
- Orders and revenue only from Squarespace Orders + Etsy. GA4 is sessions only.
- Zero is a real value only when the source confirms it; otherwise blank + TODO.
- Test orders (e.g. #00003/#00004, refunded) are excluded from revenue.
- Do not set revenue targets until real conversion, margin and CAC exist (README section 10).
- Read-only on the store. Never post the review anywhere; the owner shares it.
- Not accounting advice; the accountant reconciles.

## Sources
- Anthropic `knowledge-work-plugins`, finance/skills/variance-analysis/SKILL.md —
  https://github.com/anthropics/knowledge-work-plugins (Apache-2.0). Adapted: threshold-plus-amount flagging,
  price/volume decomposition, 4-part variance narrative (driver, outlook, action), "no vague explanations".
- Anthropic `knowledge-work-plugins`, small-business/skills/monday-brief/SKILL.md (Apache-2.0). Adapted: one page,
  one "most important" line, name missing sources in one line, never post without approval.
- Commoncog, "Colin Bryar on Amazon's Weekly Business Review" — https://commoncog.com/colin-bryar-amazon-weekly-business-review/
  (copyrighted article, idea only, own words): controllable input vs output metrics; spend discussion on exceptions.
- Admetrics, "Contribution Margin for DTC" — https://www.admetrics.io/en/post/contribution-margin-dtc-ecommerce-91013
  (vendor blog, idea only): track contribution before and after ad spend; new-customer CAC, not blended.
