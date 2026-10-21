---
name: aw-unit-economics
description: Use when working out per-SKU profit, contribution margin, break-even or maximum CAC, which products to prioritise or promote, or whether a channel/campaign makes money for Autumn & Wool (business-os/sku-economics.csv, unit_economics.py).
---

# Unit Economics (per SKU and per channel)

## Purpose
Answer three questions with real numbers: what does each order of each SKU leave after variable costs, how much
can we pay to acquire a customer for it, and which channels are above or below that line. Feeds the README
section 12 decisions (5 priority products, 2 test channels, minimum contribution per order).

## Files
- `business-os/sku-economics.csv` — one row per product: price incl. VAT, VAT rate, five variable-cost columns,
  `target_cac_eur`. Cost columns are blank until the owner/Production Manager fills them.
- `python3 business-os/unit_economics.py` — report. `contrib` = contribution before acquisition = **break-even
  CAC**. `margin` = contrib / net revenue. `after CAC` uses `target_cac_eur`. Rows with blank costs are listed as TODO.
- `python3 business-os/unit_economics.py --selftest` — checks the maths (EUR 155 sweater -> 33.10 / 15.10).
- **Never run `init`** (it re-seeds the sheet; it refuses if the file exists, keep it that way).

## Layers (use these names in every output)
| Layer | Formula | Tells you |
|---|---|---|
| Net revenue | price / (1 + vat_rate) | What we keep from the customer |
| CM1 product margin | net - materials_labour | Product strength (gross margin) |
| CM2 contribution before acquisition | CM1 - shipping - payment - packaging - returns_allowance | Break-even CAC |
| CM3 contribution after acquisition | CM2 - CAC | Real first-order profit |
| Max CAC | CM2 - minimum contribution per order (owner decision) | Ad/creator bid ceiling |

## Procedure
1. Run `python3 business-os/unit_economics.py --selftest`, then `python3 business-os/unit_economics.py`. Paste
   the output as-is; do not recompute differently.
2. Report coverage first: costed vs TODO, how many TODO are visible products (22 visible of 82). If key
   visible SKUs are TODO, the main deliverable is a **cost-collection request** (step 7), not analysis.
3. For costed SKUs, rank by CM2 (EUR) and margin %. Flag:
   - CM1 margin < 40% of net (thin product margin for handmade apparel; benchmark, not a rule)
   - CM2 < owner's minimum contribution per order -> not promotable with paid traffic
   - `after CAC` < 0 -> "loses money" at target CAC
4. **Priority shortlist** (max 5): CM2 x stock x readiness. Readiness = real photo per colour, size info, on the
   Production Manager's safe-to-promote list (`aw-production-capacity` if present). Stock is from the sheet
   (Oct 17 export) and may be stale; say so. Very high stock values (e.g. 360 turtlenecks, 220 beanies) need owner
   confirmation before planning on them.
5. **Channel check** (once orders exist): CAC per channel = channel spend / new customers from that channel
   (UTM or discount code). Compare each to the CM2 of the SKUs it sold. Never blend channels.
6. **Repeat / LTV**: only from observed repeat orders in Squarespace + Etsy. With zero direct orders, LTV is
   "unknown"; do not use Etsy history or benchmarks as a stand-in for direct-store LTV.
7. **Cost-collection request** for TODO rows: list SKU, title, price, which columns are blank, and who supplies
   them (materials+labour = founder/production; shipping = carrier rates per region; payment = Stripe/PayPal fee
   schedule actually on the account; returns allowance = owner's assumption, label it as such).
8. Save to `business-os/reviews/unit-economics-YYYY-MM-DD.md`. Propose cost values only as a separate
   "proposed, owner to confirm" table; never write guessed numbers into `sku-economics.csv`.

## Output template
```markdown
# Unit economics YYYY-MM-DD — DRAFT
Coverage: N costed / M TODO (V visible TODO). Selftest: ok/fail.

## Per SKU (costed only)
| SKU | Price | Net | CM1 % | CM2 EUR (break-even CAC) | Target CAC | CM3 | Stock | Flag |

## Priority shortlist (max 5)
| Rank | SKU | Why (CM2, stock, readiness) | Max CAC at min contribution EUR X |

## Channels (if orders exist)
| Channel | Spend | New customers | CAC | Avg CM2 of SKUs sold | Verdict scale/hold/stop |

## Cost data needed
| SKU | Missing columns | Who supplies |

## Decisions for owner
- Minimum contribution per order: EUR __ (proposal + reasoning)
```

## Decision rules (adapted, conservative)
- CM3 < 0 on first order and no observed repeat rate -> stop or fix price/cost; do not scale.
- CM3 > 0 but thin (< minimum contribution) -> hold spend, optimise conversion/AOV first.
- CM3 >= minimum contribution, stock and capacity available -> owner may approve a capped test.
- Payback beyond a few months strains cash for a small brand; check `aw-cash-flow` before any spend increase.

## Guardrails
- Variable costs only in CM2. Salaries, software, rent are overhead (handled in `aw-cash-flow`).
- Payment fees: use the account's actual Stripe/PayPal rates, not remembered ones. TODO if unknown.
- Never invent costs, stock or conversion rates. Illustrative numbers must be labelled "illustrative".
- Product data is frozen: price changes are proposals to the owner, never edits.
- Not financial advice; the accountant confirms VAT treatment (OSS for EU cross-border sales).

## Sources
- lyndonkl/claude, skills/financial-unit-economics/SKILL.md — https://github.com/lyndonkl/claude (README says
  "open source; use freely", no formal licence file found -> treated as non-permissive; ideas only, own words):
  fully loaded variable costs, no blended channel CAC, LTV only from observed cohorts, LTV/CAC + payback decision ladder.
- Polar Analytics, "What is contribution margin" — https://www.polaranalytics.com/post/what-is-contribution-margin
  and Admetrics DTC contribution-margin guide (vendor blogs, idea only): CM1/CM2/CM3 layering; max CAC =
  contribution minus profit buffer.
- Compared and not used: afadtc/afa-dtc-skills `afa-dashboard` (SKILL.md body not visible, no licence stated);
  ClaudSkills "financial-accounting" (SaaS/ASC 606 focused, wrong fit).
