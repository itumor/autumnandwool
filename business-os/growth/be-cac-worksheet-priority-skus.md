# BE_CAC worksheet, priority SKUs   Status: DRAFT, ASSUMED (GRO-15)   updated 2026-10-21 (wave 3)

aw-growth-marketing. **ASSUMPTION: BE_CAC = GM's assumed CM2 per destination (A-GRO-01), minimum contribution EUR 10
(A-GM-20), priority 5 per A-GM-02, GREEN list per `knitwear-making/capacity-2026-W43.md`; register:
`business-os/growth/assumptions-wave3.md`.** None of these numbers is a confirmed cost. Rule: no budget without a
break-even CAC (hard rule 5). An assumed BE_CAC permits **planning only**, not spend (Production: "no paid spend on any SKU
until the owner confirms its cost and stock"; A-GM-08 December paid = EUR 0).

Finance's `sku-margins-assumed-wave3.md` was not in `business-os/finance/` at run time, so the CM2 comes from
`head-of-ecommerce/min-contribution-assumed-2026-10-21.md`. FIN's file replaces it when published.

## Formulas (same as `business-os/unit_economics.py` `economics()`)
- Net = price / 1.21. CM2 = BE_CAC = net - (M+L + packaging 1.50 + payment 4.8% x price + 0.25 + shipping by zone + returns 5% of net)
- Target CAC = 0.6 x BE_CAC (`target_cac_eur` blank). Max CAC = CM2 - minimum contribution (EUR 10).
- **CAC goal = lower of Target CAC and Max CAC.** Paid-promotable only if Max CAC > 0 **and** GREEN.
- Test budget per concept = 3 x BE_CAC. Kill 1: spend >= 2 x BE_CAC with 0 orders. Kill 2: spend >= 3 x BE_CAC with CAC > BE_CAC.
- Baltic tests use the lower EE/LT BE_CAC for budget and kill lines (A-GRO-02).

## Table A: LV and EE/LT (EUR, ASSUMPTION)
| # | SKU (product_id prefix) | Price | Net | BE_CAC LV | BE_CAC EE/LT | Target CAC (0.6x) LV / EE-LT | Max CAC LV / EE-LT | **CAC goal** LV / EE-LT | Test budget/concept (3x EE/LT) | Kill 1 (2x EE/LT) | GREEN (A), max units W44 | Paid-promotable? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P2 | Merino Raglan Sweater, Dusty Pink (`69105bd9b0c4`) | 155.00 | 128.10 | 25.82 | 24.82 | 15.49 / 14.89 | 15.82 / 14.82 | **15.49 / 14.82** | 74.46 | 49.64 | GREEN, 6 from stock | **Yes, LV+EE/LT** (on assumption) |
| P3 | Women's Classic Lambswool Crew (`691059dfdc1b`) | 136.00 | 112.40 | 23.00 | 22.00 | 13.80 / 13.20 | 13.00 / 12.00 | **13.00 / 12.00** | 66.00 | 44.00 | GREEN, 8 from stock | **Yes, LV+EE/LT** (on assumption) |
| P4 | Merino Hat & Scarf Set, Black (`69105624c6bf`) | 110.00 | 90.91 | 18.82 | 17.82 | 11.29 / 10.69 | 8.82 / 7.82 | **8.82 / 7.82** | 53.46 | 35.64 | GREEN Black, 6 (2 stock + 4 MTO) | Marginal, LV only; not a test pick |
| P1 | Merino Wool Raglan Cardigan (`691050bcb0c4`) | 160.00 | 132.23 | 13.87 | 12.87 | 8.32 / 7.72 | 3.87 / 2.87 | 3.87 / 2.87 | n/a | n/a | AMBER (organic only) | No |
| P5 | Rib-Knit Beanie (`69105690dc1b`) | 45.00 | 37.19 | 13.09 | 12.09 | 7.85 / 7.25 | 3.09 / 2.09 | 3.09 / 2.09 | n/a | n/a | GREEN 1 colour, 8 MTO | No (organic, gift, add-on) |
| Alt 1 | Merino Turtleneck (`69105a8503d8`) | 110.00 | 90.91 | 8.79 | 7.79 | 5.27 / 4.67 | -1.21 / -2.21 | none | n/a | n/a | AMBER | No |
| Alt 2 | 100% Wool Long Shawl Cardigan (`69105a2903d8`) | 145.00 | 119.83 | 2.61 | 1.61 | 1.57 / 0.97 | -7.39 / -8.39 | none | n/a | n/a | AMBER | No |

## Table B: EU-other and US/CA/AU BE_CAC (EUR, ASSUMPTION)
| SKU | EU-other | US/CA/AU | Max CAC EU-other | Paid? |
|---|---|---|---|---|
| P2 | 8.82 | -19.39 | -1.18 | No |
| P3 | 6.00 | -19.86 | -4.00 | No |
| P4 | 1.82 | -20.81 | -8.18 | No |
| P1 | -3.13 | -31.96 | negative | No |
| P5 | -3.91 (XS parcel: about -1 to +4) | -18.49 | negative | No |

## Result
- **Only P2 Dusty Pink and P3 Lambswool Crew can carry paid traffic, and only in LV + EE/LT** (A-GRO-03). P2 has the
  most headroom (CAC goal EUR 14.82 in EE/LT) and is the default test SKU if a test ever runs.
- Every US/CA/AU order of a priority SKU loses money on assumed shipping + duty. No paid targeting outside the Baltics.
- Sanity check (A-GRO-05/06, L): at EUR 0.40 CPC and 1% CVR, expected CAC is about EUR 40, so break-even CPC is
  EUR 0.15-0.25 for P2. Any test should be expected to hit Kill 1 unless real CPC/CVR are much better.
- Sensitivity (GM): at a EUR 15 minimum, P2 Max CAC 10.82 and P3 8.00 (LV). Labour minutes move CM2 most: P1 at 180 min instead of 260 gains about EUR 16.

## Steps when real inputs land (moves GRO-15 from ASSUMED to DONE)
1. Owner confirms costs in `sku-economics.csv` (G1); FIN runs `python3 business-os/unit_economics.py`; replace BE_CAC columns.
2. Owner confirms minimum contribution (decision 23); recompute Max CAC and CAC goal.
3. Owner-approved capacity file: copy GREEN and max units.
4. Re-fill `test-2026-10-21-dec-first-signal.md` and `budget-proposal-2026-12.md` budget lines.

The README s9 EUR 33.10 example is illustrative and is not used.
