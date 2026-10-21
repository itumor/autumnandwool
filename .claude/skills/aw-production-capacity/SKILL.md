---
name: aw-production-capacity
description: Use when planning Autumn & Wool production or stock for the week, estimating knitting/finishing hours, costing a garment's materials + labour, setting reorder points for yarn or finished stock, flagging stock risk, or publishing the weekly capacity + "safe to promote" SKU list that marketing, ads and creators must follow.
---

# Weekly capacity, costing, reorder points and safe-to-promote list

Purpose: handmade knitwear is capacity-limited. Marketing may only push SKUs that production can actually
deliver within the promised lead time. This skill produces the one weekly artifact everyone else reads:
`business-os/capacity-YYYY-Www.md` (proposal until the owner approves it). Shared by aw-production,
aw-operations, growth and ads agents.

## Inputs (read, never edit)

| Input | Where | Notes |
|---|---|---|
| Visible SKUs, store stock, price, cost columns | `business-os/sku-economics.csv` | 82 rows, 22 visible. Cost columns empty until owner fills them |
| Contribution / break-even CAC | `python3 business-os/unit_economics.py` | See aw-unit-economics |
| Demand signal | Squarespace Orders + Etsy (owner export), `business-os/kpi-weekly.csv` | GA4 has no purchase events |
| Planned promotions | growth/ads/content plans in `business-os/` | What marketing wants to push next week |
| Time per garment, yarn per garment, yarn on hand, supplier lead time | **TODO: owner/production log** | Not in any file yet. Never guess; ask |

Store stock caveat: Squarespace stock numbers (e.g. turtleneck 360, beanie 220) may be placeholders for
made-to-order items, not physical units. Treat stock as "finished units on shelf" only when the owner confirms.

## Procedure

1. **Per-SKU work content.** For each visible SKU record minutes per unit by step: knitting (manual machine),
   linking/seaming, hand finishing, washing/blocking/drying, QC + labelling, packing. Source = owner timing of a
   real unit (time 3 units, use the median). Mark `TODO` where untimed. This is the knitwear version of the
   garment-industry "standard allowed minute" (SAM): observed time x rating + allowances.
2. **Weekly available minutes.** `people x hours/day x 60 x working days x efficiency`. Default efficiency 0.75
   for hand processes until real data exists (state it as an assumption). Subtract known absences, markets,
   photo shoots, admin. Bottleneck = the step with least capacity (often finishing or drying, not knitting).
3. **Load.** Committed orders (made-to-order backlog) first, then restock of SKUs below reorder point, then
   promotion buffer. Load % = required minutes / available minutes per step. Over 85% on any step = amber,
   over 100% = red.
4. **Materials + labour cost.** `materials_labour_eur` = yarn grams x EUR/gram (with ~5-10% waste allowance,
   owner to confirm) + trims/labels + minutes x hourly labour rate (owner sets). Write proposals to a separate
   draft file, never into `sku-economics.csv` itself, unless the owner asks.
5. **Reorder points.**
   - Yarn (per colour/lot): `ROP = average weekly yarn use x supplier lead time (weeks) + safety stock`.
     Safety stock start rule: 2 weeks of use, or `z x sd(weekly use) x sqrt(lead time weeks)` once 8+ weeks of
     data exist (z 1.65 = ~95% service). Note yarn dye-lot: reorder whole-garment quantities from one lot.
   - Finished stock (made-to-stock SKUs): `ROP = weekly sales x production lead time (weeks) + safety stock`.
     With near-zero sales history, use a fixed minimum (e.g. 2 units per size/colour of priority SKUs) and say so.
6. **Lead time promise check.** Promised dispatch in FAQ = up to 5 business days for made-to-order (verify on
   live page; Merchant Center lists 4-10 business days delivery). If load means a SKU cannot ship inside the
   promise, it is NOT safe to promote.
7. **Safe-to-promote rule.** A SKU is GREEN only if all hold: visible; finished stock >= 3 units in the promoted
   sizes/colours OR made-to-order capacity for >= 5 extra units this week inside the lead time; yarn above ROP;
   no open QC defect on the SKU; contribution > 0 at target CAC (aw-unit-economics; if costs unknown, mark
   AMBER "cost unknown"); real photo per promoted colour exists. Otherwise AMBER (organic only, no paid) or RED
   (do not promote).
8. **Stock-risk report.** List SKUs below ROP, single-unit SKUs (many visible SKUs have stock 1), yarn lots
   running out, and any variant whose colour has no photo.

## Output template (`business-os/capacity-YYYY-Www.md`)

```
# Capacity + safe-to-promote — week YYYY-Www   Status: DRAFT for owner approval
Assumptions: people=?, hours=?, efficiency=0.75 (assumed), absences=...
| Step | Available min | Required min | Load % | RAG |
| SKU | Stock (confirmed?) | Units makeable this week | Yarn vs ROP | Contribution | Photo per colour | Status | Max units to promote |
## Safe to promote (GREEN): ...
## Organic only (AMBER) + why: ...
## Do not promote (RED) + why: ...
## Reorder proposals (owner buys): yarn, colour, lot, qty, supplier, needed-by
## Stock risks: ...
## TODO / missing data: ...
```

Hand the GREEN list, with "max units to promote", to growth/ads/content. Re-issue mid-week if a red step appears.

## Guardrails

- Never invent minutes, yarn weights, costs, stock or supplier lead times. Unknown = `TODO`, and the SKU drops to
  AMBER at best.
- Never change store stock, product data or `sku-economics.csv` without explicit owner instruction (product data
  is frozen). Purchases of yarn/supplies are owner decisions; you propose quantities only.
- Do not raise the promised lead time on the site yourself; propose wording to the owner.
- State every formula input so the owner can check the maths.

## Sources

- Garment SAM / capacity method (time study x rating + allowances; machines x minutes x efficiency x days):
  onlineclothingstudy.com "How to calculate garment SAM" https://www.onlineclothingstudy.com/2011/02/how-to-calculate-sam-of-garment.html
  — all rights reserved; concept only, own words.
- Reorder point / safety stock (z-score service level) and ABC thinking: compared community skills
  jmsktm/claude-settings "inventory-manager" https://github.com/jmsktm/claude-settings and
  travisjneuman/.claude "supply-chain-optimizer" https://github.com/travisjneuman/.claude — licenses not stated,
  SKILL.md bodies not inspected; nothing copied. Formulas are standard operations-management textbook forms.
- Safe-to-promote gate and stock caveats: Autumn & Wool `business-os/README.md` s.6, s.9; `hiring-plan.md`.
