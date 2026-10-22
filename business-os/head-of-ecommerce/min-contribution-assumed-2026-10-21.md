# Minimum contribution, break-even CAC and priority-5 re-check, ON ASSUMPTIONS (GM-05, GM-12, GM-16) — DRAFT for owner

Author: GM (agent), 2026-10-21, wave 3, assumption mode. **No number here is a confirmed cost.** Inputs come from three
registers:
- costs: `business-os/knitwear-making/assumptions-wave3.md` + `sku-cost-proposals-2026-10-21.md` (A-PRD-01..21)
- shipping and packaging: `business-os/operations/assumptions-wave3.md` (A-OPS-02/03/05/06/08/10)
- decisions: `business-os/head-of-ecommerce/assumptions-wave3.md` (A-GM-05, -09, -20, -21)

`unit_economics.py --selftest`: ok. `unit_economics.py`: 0 costed / 82 TODO (22 visible). Nobody has written the
assumed costs into `sku-economics.csv`, so the script's output does not reflect them. The figures below are a hand
calculation in the same CM layers. Finance re-runs the script after the owner confirms costs (G1).

**One line:** on these assumptions, free shipping makes **every priority SKU lose money on US/CA/AU orders** and leaves
little or nothing on EU-other orders. Only Latvia and Estonia/Lithuania orders leave enough contribution for any paid
acquisition. The hero cardigan has the thinnest CM2 of the five.

## Inputs (all ASSUMPTION)
| Layer | Value | A-ID |
|---|---|---|
| Net revenue | price / 1.21 | VAT 21% LV; accountant confirms per country (OSS) |
| Materials + labour | Production per-SKU value (EUR 12/h, title-based yarn class) | A-PRD-01, -06..10, -20, -21 |
| Packaging | EUR 1.50 per order (Ops owns the number; Production's 3.00 placeholder is replaced) | A-OPS-10 |
| Payment | price x 4.8% + EUR 0.25 (Stripe EEA premium 2.8% + 0.25, plus Squarespace Basic 2%) | FIN public rates; A-GM-05 (Basic) |
| Shipping (free to customer, paid by us) | LV 5.00, EE/LT 6.00, EU-other 22.00, US/CA/AU 28.00 + US duty 15% of net + EUR 3.00 | A-OPS-02, -03, -05, -06, -08 |
| Returns allowance | 5% of net revenue | A-GM-21 (same value Production used) |
| Minimum contribution per order | **EUR 10** (sensitivity 5 / 15) | A-GM-20 |

## CM2 per priority SKU and destination = break-even CAC (EUR, ASSUMPTION)
| SKU | Price | Net | M+L | CM1 % | CM2 LV | CM2 EE/LT | CM2 EU-other | CM2 US/CA/AU |
|---|---|---|---|---|---|---|---|---|
| P1 Merino Raglan Cardigan | 160 | 132.23 | 97.32 | 26.4% | 13.87 | 12.87 | -3.13 | -31.96 |
| P2 Dusty Pink Merino Raglan | 155 | 128.10 | 81.68 | 36.2% | **25.82** | 24.82 | 8.82 | -19.39 |
| P3 Classic Lambswool Crew | 136 | 112.40 | 70.50 | 37.3% | **23.00** | 22.00 | 6.00 | -19.86 |
| P4 Hat & Scarf Set | 110 | 90.91 | 55.51 | 38.9% | 18.82 | 17.82 | 1.82 | -20.81 |
| P5 Rib-Knit Beanie | 45 | 37.19 | 13.33 | 64.2% | 13.09 | 12.09 | -3.91 (XS parcel 14-19 instead of 22: about -1 to +4) | -18.49 |
| Alt 1 Merino Turtleneck | 110 | 90.91 | 65.54 | 27.9% | 8.79 | 7.79 | -8.21 | -30.84 |
| Alt 2 Long Shawl Cardigan | 145 | 119.83 | 97.52 | 18.6% | 2.61 | 1.61 | -14.39 | -41.36 |

Formula: CM2 = net - M+L - 1.50 - (price x 0.048 + 0.25) - shipping - 0.05 x net (US also - 0.15 x net - 3.00).
Note: Production's indicative CM2 (`sku-cost-proposals` file) uses a flat EUR 12 shipping and EUR 3 packaging, so its
values sit between the LV and EU-other columns here. The values in this file supersede it because Operations owns
shipping and packaging.

## Max CAC (bid ceiling) = CM2 - minimum contribution (EUR 10), ASSUMPTION
| SKU | LV | EE/LT | EU-other | US/CA/AU | Promotable with paid traffic? |
|---|---|---|---|---|---|
| P2 Dusty Pink | 15.82 | 14.82 | -1.18 | no | Yes, LV + EE/LT only |
| P3 Lambswool Crew | 13.00 | 12.00 | -4.00 | no | Yes, LV + EE/LT only |
| P4 Hat & Scarf Set | 8.82 | 7.82 | no | no | Marginal, LV only |
| P1 Raglan Cardigan | 3.87 | 2.87 | no | no | No (organic only) |
| P5 Beanie | 3.09 | 2.09 | no | no | No: organic gift and add-on (Production agrees) |

Sensitivity: at a EUR 5 minimum, P1 and P5 reach about EUR 8 in LV and P4 about 14. At EUR 15, only P2 (10.82) and P3
(8.00) stay positive in LV. The ranking is the same at all three levels.

## A-GM-20: why EUR 10 (method `finance/min-contribution-method.md`)
Fixed-cost scenarios EUR 100 / 175 / 250 per month (A-GM-09, illustrative) at 10 / 20 / 40 orders per month (illustrative).
The Mid case of 175 / 20 gives 8.75 per order, rounded up to EUR 10. Floor EUR 5. At EUR 10, 2 of 5 priority SKUs can carry paid
traffic in the Baltics, so a test is possible later without taking a loss. EUR 15 would leave room only for P2/P3, and EUR 5
would let thin SKUs into paid spend.

## GM-12 re-check of the priority 5 (on assumed CM2)
- **Keep the 5 for organic promotion.** They were picked on readiness, and readiness has not changed. Neither alternate beats
  them: the turtleneck's CM2 is 8.79 LV and the shawl cardigan's is 2.61 LV. **No swap.**
- **Order for any paid or creator effort:** P2 Dusty Pink > P3 Lambswool Crew > P4 Hat & Scarf Set > P1 Cardigan ≈ P5 Beanie.
- **P1 Cardigan:** it is the "hero" on looks, but its CM2 is the thinnest (26% CM1). Real minutes (260 assumed) decide it. If timing
  shows 180 minutes, CM2 LV rises by about EUR 16. Owner priority: time the cardigan first (PRD-06).
- **Gift SKU for creators (A-GM-17):** the beanie is still right for gifting. Its landed gift cost is small (13.33 + 1.50 + 5.00 =
  about EUR 20 in LV), but each gifted beanie must be recovered by orders. Hat set Black second.

## Decisions for owner (proposals; A-GM rows in the register)
| # | Decision | Evidence | KPI effect | Cost | Owner / by | Reversible |
|---|---|---|---|---|---|---|
| 1 | Minimum contribution per order **EUR 10** (A-GM-20) | Table above | Sets bid ceiling; protects operating profit | EUR 0 | Owner, 4 Nov | Yes |
| 2 | **US/CA/AU free shipping: decide by 31 Oct** whether to charge shipping (e.g. a flat fee) or set a minimum order. On these assumptions every priority-SKU US order loses EUR 18-32 | CM2 US column; A-OPS-06/08 (L confidence) | Stops loss-making orders; may cut US conversion | EUR 0 (settings change by owner) | Owner, 31 Oct (decision 21) | Yes |
| 3 | Any future paid test targets **LV + EE/LT only**, SKU P2 or P3 | Max CAC table | Keeps CM3 at or above EUR 10 | EUR 0 now (A-GM-08) | Owner, 20 Nov | Yes |

## What makes these numbers real (owner, in order of effect)
1. Time 3 units of P1, P2, P3 (labour is 55-65% of M+L; A-PRD-01/21).
2. Carrier actually used + one real label price LV and DE (A-OPS-02/05).
3. Stripe account fee line from one charge (premium vs standard: about EUR 2 per order).
4. Squarespace plan from the Billing screenshot (2% = EUR 0.90-3.20 per order).

DRAFT for owner. Assumptions, not facts. Nothing written to `sku-economics.csv`. Not sent.
