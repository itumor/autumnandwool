# Consolidated SKU margins, 22 visible SKUs x 4 zones (FIN-03, FIN-18, FIN-19) — DRAFT for owner

Author: aw-finance (agent), 2026-10-21, wave 3, ASSUMPTION MODE. Finance is the single owner of these per-SKU margin
figures. **Every cost here is an ASSUMPTION, not a fact.** Registers:
`business-os/knitwear-making/assumptions-wave3.md` (A-PRD), `business-os/operations/assumptions-wave3.md` (A-OPS),
`business-os/head-of-ecommerce/assumptions-wave3.md` (A-GM), `business-os/finance/assumptions-wave3.md` (A-FIN).
The GM ruled that Operations' shipping and packaging values replace Production's placeholders (W3-2, W3-3). This file
supersedes the indicative CM2 columns in Production's `sku-cost-proposals-2026-10-21.md` and the GM's
`min-contribution-assumed-2026-10-21.md` (same figures, except US payment, see F-1).
Machine-readable copy: `business-os/finance/sku-margins-assumed-wave3.csv` (39 columns, one row per SKU: the first 31
are the free-shipping basis, the 8 `w313_*` columns are the W3-13 policy, EU other and US/CA/AU).
**Update 2026-10-21 (GM rulings W3-13, W3-14):** see section "W3-13 policy" below. The free-shipping table stays for
comparison.
Not accounting, tax or investment advice. Nothing written to `sku-economics.csv`. Nothing sent.

## Coverage and method (Actual)
- `python3 business-os/unit_economics.py --selftest` -> `selftest ok` (run 2026-10-21).
- `python3 business-os/unit_economics.py` -> `0 costed, 82 TODO (22 of them visible on the store)`. The sheet is
  unchanged: the owner has confirmed no costs (G1), so the script's own report still shows nothing costed.
- The figures below were computed with the script's own `economics()` function (imported, not re-written). Inputs came
  from the registers, and price + VAT rate from `sku-economics.csv` (17 Oct export). `init` was not run. Once the owner
  confirms costs and writes them into the sheet, the LV column below is what `contrib` should show, give or take
  rounding.

## Inputs per order (all ASSUMPTION)
| Layer | Value | A-ID |
|---|---|---|
| Net revenue | price / 1.21, all zones (conservative; not a VAT treatment) | A-FIN-03 |
| Materials + labour | grams x 1.08 x yarn EUR/kg (merino 60 / lambswool 50 / wool 40) + trims + minutes x EUR 0.20 | A-PRD-01, -06..10, -18, -20, -21 |
| Packaging | EUR 1.50 | A-OPS-10 (W3-2) |
| Payment | EEA price x 4.8% + 0.25; US/CA/AU price x 5.15% + 0.25 | A-FIN-01, A-FIN-02, A-GM-05 |
| Shipping (free to customer, paid by us) | LV 5.00, EE/LT 6.00, EU other 22.00, US/CA/AU 28.00 + US duty 15% of net + EUR 3.00 | A-OPS-02, -03, -05, -06, -08 (W3-3) |
| Returns allowance | 5% of net | A-GM-21 (W3-4) |
| Minimum contribution per order | EUR 10 | A-GM-20 |
| Physical stock | listed 1-8 as listed; 12/16 = 50%; 220/360 = 0 (made to order) | A-PRD-12 |

CM1 = net - M+L. CM2 = CM1 - packaging - payment - shipping - returns = **break-even CAC**. Max CAC = CM2 - EUR 10.
Rest of World (UK, NO, CH, others) is not costed (A-OPS-07). If needed, use the US column without duty: EUR 8.58-23.45
better than US (no duty), and still below EUR 10 for every priority SKU.

## Per SKU and zone (EUR, ASSUMPTION; bold = negative)
Legend: "paid-capable" = Max CAC >= EUR 10 in LV and EE/LT. "thin for paid" = 0 to 10. "organic only" = Max CAC < 0
in LV. "dup pool" = duplicate listings share one stock pool (A-PRD-13): crew 16/8 -> pool 8 physical, side-slit 16/16
-> 8, stand-collar 12/16 -> 8, beige vest 1/1 -> 1. Do not add the two listings together.

| # | SKU (product_id) | Prio | Price | Net | M+L | CM1 % | CM2 LV | CM2 EE/LT | CM2 EU | CM2 US/CA/AU | Max CAC LV | Max CAC EE/LT | Stock listed -> assumed | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Merino Raglan Cardigan (Black) (`691050bcb0c4`) | P1 | 160.00 | 132.23 | 97.32 | 26.4 | 13.87 | 12.87 | **-3.13** | **-32.52** | 3.87 | 2.87 | 6 -> 6 | CM1<40%; thin for paid; EU loss |
| 2 | Merino Raglan Sweater, Dusty Pink (`69105bd9b0c4`) | P2 | 155.00 | 128.10 | 81.68 | 36.2 | 25.83 | 24.83 | 8.83 | **-19.92** | 15.83 | 14.83 | 6 -> 6 | CM1<40%; paid-capable LV+EE/LT |
| 3 | Women's Classic Lambswool Crew (`691059dfdc1b`) | P3 | 136.00 | 112.40 | 70.50 | 37.3 | 23.00 | 22.00 | 6.00 | **-20.33** | 13.00 | 12.00 | 16 -> 8 | CM1<40%; paid-capable LV+EE/LT |
| 4 | Merino Hat & Scarf Set (`69105624c6bf`) | P4 | 110.00 | 90.91 | 55.51 | 38.9 | 18.82 | 17.82 | 1.82 | **-21.21** | 8.82 | 7.82 | 6 -> 6 | CM1<40%; thin for paid |
| 5 | Rib-Knit Beanie (`69105690dc1b`) | P5 | 45.00 | 37.19 | 13.33 | 64.2 | 13.09 | 12.09 | **-3.91** | **-18.65** | 3.09 | 2.09 | 220 -> 0 | thin for paid; EU loss; MTO, stock placeholder |
| 6 | Merino Turtleneck, lightweight (`69105a8503d8`) | Alt1 | 110.00 | 90.91 | 65.54 | 27.9 | 8.79 | 7.79 | **-8.21** | **-31.24** | **-1.21** | **-2.21** | 360 -> 0 | CM1<40%; organic only; EU loss; MTO, stock placeholder |
| 7 | 100% Wool Long Shawl Cardigan (`69105a2903d8`) | Alt2 | 145.00 | 119.83 | 97.52 | 18.6 | 2.61 | 1.61 | **-14.39** | **-41.88** | **-7.39** | **-8.39** | 16 -> 8 | CM1<40%; organic only; EU loss |
| 8 | Distressed Wool Raglan Sweater (`69105a20b0c4`) | - | 155.00 | 128.10 | 72.72 | 43.2 | 34.79 | 33.79 | 17.79 | **-10.96** | 24.79 | 23.79 | 1 -> 1 | paid-capable LV+EE/LT; 1-2 units |
| 9 | Lambswool Raglan Crew (A) (`691059de03d8`) | - | 136.00 | 112.40 | 70.50 | 37.3 | 23.00 | 22.00 | 6.00 | **-20.33** | 13.00 | 12.00 | 16 -> 8 | CM1<40%; paid-capable LV+EE/LT; dup pool |
| 10 | Lambswool Raglan Crew (B) (`691059deb0c4`) | - | 136.00 | 112.40 | 70.50 | 37.3 | 23.00 | 22.00 | 6.00 | **-20.33** | 13.00 | 12.00 | 8 -> 8 | CM1<40%; paid-capable LV+EE/LT; dup pool |
| 11 | Long Wool Cardigan, Shawl Collar (`69105a2ab0c4`) | - | 145.00 | 119.83 | 106.70 | 11.0 | **-6.57** | **-7.57** | **-23.57** | **-51.06** | **-16.57** | **-17.57** | 12 -> 6 | CM1<40%; loses money even in LV; EU loss |
| 12 | Merino Striped Oversized Sweater (`69105a2694cd`) | - | 165.00 | 136.36 | 90.92 | 33.3 | 23.95 | 22.95 | 6.95 | **-23.08** | 13.95 | 12.95 | 1 -> 1 | CM1<40%; paid-capable LV+EE/LT; 1-2 units |
| 13 | Open-Front Wool Cardigan, Side-Slit (`69105a8403d8`) | - | 155.00 | 128.10 | 83.04 | 35.2 | 24.47 | 23.47 | 7.47 | **-21.28** | 14.47 | 13.47 | 1 -> 1 | CM1<40%; paid-capable LV+EE/LT; 1-2 units |
| 14 | Oversized Merino Turtleneck, Dusty Pink (`69105adfb0c4`) | - | 155.00 | 128.10 | 88.92 | 30.6 | 18.59 | 17.59 | 1.59 | **-27.16** | 8.59 | 7.59 | 1 -> 1 | CM1<40%; thin for paid; 1-2 units |
| 15 | Oversized Merino V-Neck Vest (`6915d24b03d8`) | - | 126.00 | 104.13 | 51.48 | 50.6 | 34.64 | 33.64 | 17.64 | **-7.42** | 24.64 | 23.64 | 2 -> 2 | paid-capable LV+EE/LT; 1-2 units |
| 16 | Oversized Wool Raglan, Beige Melange (`691055d8dc1b`) | - | 155.00 | 128.10 | 68.72 | 46.4 | 38.79 | 37.79 | 21.79 | **-6.96** | 28.79 | 27.79 | 1 -> 1 | paid-capable LV+EE/LT; 1-2 units |
| 17 | Wool V-Neck Vest, Beige (A) (`6910544d03d8`) | - | 126.00 | 104.13 | 43.92 | 57.8 | 42.20 | 41.20 | 25.20 | 0.14 | 32.20 | 31.20 | 1 -> 1 | paid-capable LV+EE/LT; 1-2 units; dup pool |
| 18 | Wool V-Neck Vest, Beige (B) (`69105a83b0c4`) | - | 126.00 | 104.13 | 43.92 | 57.8 | 42.20 | 41.20 | 25.20 | 0.14 | 32.20 | 31.20 | 1 -> 1 | paid-capable LV+EE/LT; 1-2 units; dup pool |
| 19 | Pure Wool Side-Slit Sweater (A) (`691059dc03d8`) | - | 136.00 | 112.40 | 64.56 | 42.6 | 28.94 | 27.94 | 11.94 | **-14.39** | 18.94 | 17.94 | 16 -> 8 | paid-capable LV+EE/LT; dup pool |
| 20 | Pure Wool Side-Slit Sweater (B) (`691059dd03d8`) | - | 136.00 | 112.40 | 64.56 | 42.6 | 28.94 | 27.94 | 11.94 | **-14.39** | 18.94 | 17.94 | 16 -> 8 | paid-capable LV+EE/LT; dup pool |
| 21 | Pure Wool Stand-Collar Sweater (`69105ad603d8`) | - | 136.00 | 112.40 | 68.72 | 38.9 | 24.78 | 23.78 | 7.78 | **-18.55** | 14.78 | 13.78 | 12 -> 6 | CM1<40%; paid-capable LV+EE/LT; dup pool |
| 22 | Women's wool stand collar sweater (`69105acfb0c4`) | - | 136.00 | 112.40 | 68.72 | 38.9 | 24.78 | 23.78 | 7.78 | **-18.55** | 14.78 | 13.78 | 16 -> 8 | CM1<40%; paid-capable LV+EE/LT; dup pool |

Totals (22 visible): CM2 >= EUR 10 in LV 19 / EE-LT 19 / EU other 7 / US-CA-AU 0. CM2 < 0 in LV 1 / EE-LT 1 /
EU other 5 / US-CA-AU 20. CM1 below the 40% benchmark: 14 of 22 (see F-2 in the A-FIN register).

## What this says (on assumptions only)
1. **US/CA/AU free shipping loses money on 20 of 22 SKUs** (EUR -6.96 to -51.06 per order). The two beige vests
   break even (EUR 0.14). Every priority SKU loses EUR 18.65-32.52. Even if exports turn out zero-rated for VAT
   (A-FIN-03), only P2 turns positive (EUR 1.59), and nothing reaches EUR 10.
2. **EU other is thin.** No priority SKU reaches EUR 10. The P1 cardigan and P5 beanie lose money (EUR -3.13 / -3.91).
   Only 7 non-priority SKUs reach EUR 10, and 5 of them have 1-2 units.
3. **Baltics carry the business.** 19 of 22 SKUs leave EUR 10 or more in LV and EE/LT.
4. **Paid traffic (when the owner approves any): P2 Dusty Pink and P3 Lambswool Crew, LV + EE/LT only.** Max CAC is
   EUR 15.83 / 14.83 for P2 and 13.00 / 12.00 for P3. P4 Hat & Scarf Set is 8.82 LV (thin). P1 and P5 are about EUR 3
   (organic only in practice). This matches the GM's ranking; no swap.
5. **Loses money even in Latvia: Long Wool Cardigan, Shawl Collar** (`69105a2ab0c4`, EUR -6.57) at 850 g / 300 min.
   Alt 2 Long Shawl Cardigan leaves EUR 2.61. Both need real minutes/grams or a price review before any promotion
   (price changes are owner proposals; product data is frozen).
6. **Best unit margins sit on SKUs with 1-2 units** (Distressed Raglan, Beige Raglan, both vests): they are good for
   organic sell-through, but stock is too low for a push.
7. **Labour is the biggest lever.** At A-PRD-01 EUR 12/h, each 30 minutes saved adds EUR 6.00 CM2 on every zone. Timing
   P1/P2/P3 (PRD-06) changes these numbers more than any carrier or fee choice.

## FIN-18: free shipping by region vs CM2 (decision 21/28), ASSUMPTION
Fulfilment cost we carry per order (shipping + packaging): LV 6.50, EE/LT 7.50, EU other 23.50, US/CA/AU 29.50 + duty
(A-OPS-02..06, -08, -10). Nov-Dec seasonal surcharge, if repeated (A-OPS-09, +7%): +0.35 / +0.42 / +1.54 / +1.96.

Shipping charge (incl. VAT) the customer would need to pay so CM2 reaches EUR 10. Each EUR charged adds about EUR 0.74
CM2 after VAT, payment fee and returns:
| SKU | LV | EE/LT | EU other | US/CA/AU |
|---|---|---|---|---|
| P1 Merino Raglan Cardigan | 0.00 | 0.00 | 17.81 | 57.96 |
| P2 Dusty Pink Merino Raglan | 0.00 | 0.00 | 1.59 | 40.78 |
| P3 Classic Lambswool Crew | 0.00 | 0.00 | 5.43 | 41.34 |
| P4 Hat & Scarf Set | 0.00 | 0.00 | 11.10 | 42.54 |
| P5 Rib-Knit Beanie | 0.00 | 0.00 | 18.87 (XS parcel EUR 14-19 instead of 22: about 8.00-14.80) | 39.05 |
| Alt 1 Turtleneck | 1.64 | 3.00 | 24.70 | 56.21 |
| Alt 2 Long Shawl Cardigan | 10.03 | 11.38 | 33.09 | 70.72 |

**Proposal for the owner (decision 21, final 2026-11-11 against real rates):**
- LV and EE/LT: keep free shipping. Every priority SKU clears EUR 10.
- EU other: keep free shipping only above a basket threshold (about EUR 150), or charge a flat fee of about EUR 12-15.
  At a EUR 12 flat fee, P2/P3/P4 clear EUR 10. P1 and the beanie need about EUR 18-19.
- US/CA/AU: charge shipping. Priority SKUs need EUR 39-58 to reach EUR 10. A EUR 40 flat fee covers P2, P3 and P5,
  almost P4 (42.54), but not P1 (57.96). Duty must be disclosed. Otherwise do not promote these zones in Q4 (aligns
  with A-GM-18).
- Rest of World: no free shipping, no promise (A-OPS-07).
These are settings proposals. The owner changes store settings; Finance changes nothing.

## W3-13 policy: CM2 by zone with the shipping charge (GM ruling 2026-10-21), ASSUMPTION
The table above (free shipping everywhere) is kept for comparison. This section applies the GM's assumed policy W3-13
(proposal; the owner changes store settings; final 2026-11-11 against real rates):
- LV, EE/LT: free shipping. No change to CM2.
- EU other: free from a EUR 150 basket; below that a flat **EUR 12.00** charged to the customer.
- US/CA/AU: flat **EUR 15.00** charged to the customer, not promoted, no paid traffic.
- Rest of World: no promise, not costed (A-OPS-07).

Method: same inputs as above, through the script's `economics()`. The charge is treated as revenue incl. VAT at 21%
(A-FIN-03 basis, not a VAT treatment). So the payment fee and the 5% returns allowance apply to price + charge. Carrier
cost is unchanged (EU 22.00, US 28.00). US duty stays 15% of the goods net + EUR 3.00, with no duty on the shipping
charge [VERIFY with Ops/accountant]. Effect of the charge on CM2: EUR 12 -> +8.84 (EEA fee); EUR 15 -> +11.01 (US fee).
Basket rule applied **per single-item order**: price >= EUR 150 ships free to EU other. Multi-item baskets are not
modelled (see note 3).

| # | SKU | Prio | Price | EU charge | CM2 EU old -> W3-13 | Max CAC EU | CM2 US/CA/AU old -> W3-13 (EUR 15) | Verdict EU / US |
|---|---|---|---|---|---|---|---|---|
| 1 | Merino Raglan Cardigan (Black) | P1 | 160.00 | 0.00 (>=150) | **-3.13** -> **-3.13** | **-13.13** | **-32.52** -> **-21.51** | loss / loss |
| 2 | Merino Raglan Sweater, Dusty Pink | P2 | 155.00 | 0.00 (>=150) | 8.83 -> 8.83 | **-1.17** | **-19.92** -> **-8.91** | thin / loss |
| 3 | Women's Classic Lambswool Crew | P3 | 136.00 | 12.00 | 6.00 -> 14.84 | 4.84 | **-20.33** -> **-9.34** | >=10 / loss |
| 4 | Merino Hat & Scarf Set | P4 | 110.00 | 12.00 | 1.82 -> 10.67 | 0.67 | **-21.21** -> **-10.20** | >=10 / loss |
| 5 | Rib-Knit Beanie | P5 | 45.00 | 12.00 | **-3.91** -> 4.93 | **-5.07** | **-18.65** -> **-7.64** | thin / loss |
| 6 | Merino Turtleneck, lightweight | Alt1 | 110.00 | 12.00 | **-8.21** -> 0.64 | **-9.36** | **-31.24** -> **-20.23** | thin / loss |
| 7 | 100% Wool Long Shawl Cardigan | Alt2 | 145.00 | 12.00 | **-14.39** -> **-5.55** | **-15.55** | **-41.88** -> **-30.87** | loss / loss |
| 8 | Distressed Wool Raglan Sweater | - | 155.00 | 0.00 (>=150) | 17.79 -> 17.79 | 7.79 | **-10.96** -> 0.05 | >=10 / thin |
| 9 | Lambswool Raglan Crew (A) | - | 136.00 | 12.00 | 6.00 -> 14.84 | 4.84 | **-20.33** -> **-9.34** | >=10 / loss |
| 10 | Lambswool Raglan Crew (B) | - | 136.00 | 12.00 | 6.00 -> 14.84 | 4.84 | **-20.33** -> **-9.34** | >=10 / loss |
| 11 | Long Wool Cardigan, Shawl Collar | - | 145.00 | 12.00 | **-23.57** -> **-14.73** | **-24.73** | **-51.06** -> **-40.05** | loss / loss |
| 12 | Merino Striped Oversized Sweater | - | 165.00 | 0.00 (>=150) | 6.95 -> 6.95 | **-3.05** | **-23.08** -> **-12.07** | thin / loss |
| 13 | Open-Front Wool Cardigan, Side-Slit | - | 155.00 | 0.00 (>=150) | 7.47 -> 7.47 | **-2.53** | **-21.28** -> **-10.27** | thin / loss |
| 14 | Oversized Merino Turtleneck, Dusty Pink | - | 155.00 | 0.00 (>=150) | 1.59 -> 1.59 | **-8.41** | **-27.16** -> **-16.15** | thin / loss |
| 15 | Oversized Merino V-Neck Vest | - | 126.00 | 12.00 | 17.64 -> 26.50 | 16.50 | **-7.42** -> 3.59 | >=10 / thin |
| 16 | Oversized Wool Raglan, Beige Melange | - | 155.00 | 0.00 (>=150) | 21.79 -> 21.79 | 11.79 | **-6.96** -> 4.05 | >=10 / thin |
| 17 | Wool V-Neck Vest, Beige (A) | - | 126.00 | 12.00 | 25.20 -> 34.06 | 24.06 | 0.14 -> 11.15 | >=10 / >=10 |
| 18 | Wool V-Neck Vest, Beige (B) | - | 126.00 | 12.00 | 25.20 -> 34.06 | 24.06 | 0.14 -> 11.15 | >=10 / >=10 |
| 19 | Pure Wool Side-Slit Sweater (A) | - | 136.00 | 12.00 | 11.94 -> 20.78 | 10.78 | **-14.39** -> **-3.40** | >=10 / loss |
| 20 | Pure Wool Side-Slit Sweater (B) | - | 136.00 | 12.00 | 11.94 -> 20.78 | 10.78 | **-14.39** -> **-3.40** | >=10 / loss |
| 21 | Pure Wool Stand-Collar Sweater | - | 136.00 | 12.00 | 7.78 -> 16.62 | 6.62 | **-18.55** -> **-7.56** | >=10 / loss |
| 22 | Women's wool stand collar sweater | - | 136.00 | 12.00 | 7.78 -> 16.62 | 6.62 | **-18.55** -> **-7.56** | >=10 / loss |

LV and EE/LT are unchanged (free shipping): CM2 >= EUR 10 on 19 of 22, 0-10 on 2, below 0 on 1 (row 11).

| Zone | Free-shipping basis: >=10 / 0-10 / <0 | W3-13 policy: >=10 / 0-10 / <0 |
|---|---|---|
| LV | 19 / 2 / 1 | 19 / 2 / 1 (no change) |
| EE/LT | 19 / 2 / 1 | 19 / 2 / 1 (no change) |
| EU other | 7 / 10 / 5 | **13 / 6 / 3** |
| US/CA/AU | 0 / 2 / 20 | **2 / 3 / 17** |

**What changes (on assumptions only):**
1. **EU other moves from thin to mostly viable.** 13 of 22 SKUs now leave EUR 10 or more (was 7). P3 Lambswool Crew
   (14.84) and P4 Hat & Scarf Set (10.67) cross EUR 10. The beanie moves from -3.91 to +4.93 (thin). Still losing
   money: P1 cardigan, Alt 2 Long Shawl Cardigan and row 11.
2. **The EUR 150 threshold exempts the thinnest high-price items.** Every SKU priced EUR 155-165 ships free and keeps
   its old CM2: P1 stays **-3.13** and P2 stays 8.83 (below EUR 10). 5 of the 9 EU-other SKUs still under EUR 10 are
   EUR 150+ items (P1, P2, Striped, Open-Front, Dusty Pink Turtleneck). Option for the owner (not a GM ruling): a EUR 200 threshold would charge EUR 12 on these single-item
   orders, so P1 would reach 5.71 and P2 17.67, but EU customers would see shipping on every single sweater.
3. **Multi-item baskets** (e.g. P3 + beanie = EUR 181) ship free under W3-13, so the beanie loses its EUR 12. One
   parcel carries both items, so the combined order still clears EUR 10 if the second item's own CM2 before shipping is
   positive. Real basket data does not exist yet (zero orders).
4. **US/CA/AU stays organic-only, as W3-13 says.** The EUR 15 charge cuts the loss by EUR 11.01 per order, but 17 of
   22 SKUs still lose money and every priority SKU loses EUR 7.64-21.51. Only the two beige vests clear EUR 10 (11.15),
   and they have 1 unit in one shared pool. Charges needed for EUR 10 on priority SKUs are unchanged (EUR 39-58, FIN-18
   table above). If exports are zero-rated for VAT (A-FIN-03), the US picture improves by about EUR 6-23 per order
   (accountant question).
5. **Paid-traffic shortlist does not change:** P2 + P3, LV + EE/LT only (Max CAC LV 15.83 / 13.00). EU other is still
   not a paid zone: P3's EU Max CAC is 4.84, P2's is -1.17.
6. **Gift-note perk (FIN-19) now crosses a line:** P4 Hat & Scarf Set to EU other at W3-13 = 10.67 -> **9.77** on gift
   orders (below EUR 10). It is a gift-order effect only and changes no promotion verdict.

Min contribution (W3-14): stays EUR 10 (Mid case). If the owner's fixed-cost list is EUR 200/month or more, it becomes
EUR 15. At EUR 15 the EU-other count falls from 13 to 9 SKUs (P3 and both Lambswool Crew listings at 14.84 and P4 at
10.67 drop out; no priority SKU stays), and US/CA/AU falls to 0. LV Max CAC at EUR 15: P2 10.83, P3 8.00. LV/EE-LT priority ranking and the "Baltics-only paid" verdict do not change.

## FIN-19: gift-season perks margin check (decision 31), ASSUMPTION
Perk set A-GM-22: gift note yes, no prices on the packing slip, no gift wrap, no extended exchange. Cost per gift order
**EUR 0.90** (A-FIN-05). Effect: CM2 and Max CAC fall by EUR 0.90 on gift orders only. **No SKU/zone crosses the EUR 10
line or zero** because of it. Nearest cases: P4 EU other 1.82 -> 0.92, Alt 1 LV 8.79 -> 7.89. If gift wrap were added
later (about EUR 1.50-3.00 + 5 minutes = EUR 1.00 labour; agent estimate), P5 beanie LV would fall below EUR 10,
so wrap should stay off for beanies (P5 LV would be about EUR 7.70-9.20). Verdict: **the A-GM-22 perk set changes no verdict: priority SKUs stay above EUR 10 in LV and
EE/LT and EU.** Owner confirms the card cost.

## Sensitivity (priority 5, CM2 LV, EUR)
| Change | P1 | P2 | P3 | P4 | P5 |
|---|---|---|---|---|---|
| Base | 13.87 | 25.83 | 23.00 | 18.82 | 13.09 |
| Minutes -25% (A-PRD-21 low) | 26.87 | 36.33 | 33.00 | 25.32 | 14.84 |
| Minutes +50% (A-PRD-21 high) | -12.13 | 4.83 | 3.00 | 5.82 | 9.59 |
| Stripe standard, Core plan (A-FIN-01 low) | 19.15 | 30.95 | 27.49 | 22.45 | 14.58 |
| Labour EUR 6/h (A-PRD-01 low) | 39.87 | 46.83 | 43.00 | 31.82 | 16.59 |

Computed from the inputs table, one change at a time. Minutes change labour by minutes x 0.20. The fee change is the
price x 3.3% saving (premium 2.8% + Squarespace 2% versus standard 1.5%).

## Cost data that turns this into DONE (owner, in order of EUR effect)
| What | Replaces | Who |
|---|---|---|
| Timed minutes for 3 units each of P1, P2, P3 | A-PRD-21 | Owner / Production (PRD-06) |
| Labour rate the owner wants costed | A-PRD-01 | Owner (decision 5b, 2026-10-28) |
| Carrier + one real label price LV, DE, US | A-OPS-02/05/06 | Owner + Operations (2026-10-28) |
| Squarespace plan (Billing screenshot) + one Stripe fee line | A-FIN-01/02, A-GM-05 | Owner (form rows 3-4) |
| VAT status, OSS, export zero-rating | A-FIN-03 | Accountant via owner (form row 18) |
| Owner writes confirmed values into `sku-economics.csv` (G1) | this whole file | Owner; Finance then re-runs `unit_economics.py` and pastes output as-is |

## Hand-off to GM / Growth (EUR impact)
- Break-even CAC (CM2) for the priority 5, LV / EE-LT: P1 13.87 / 12.87, P2 25.83 / 24.83, P3 23.00 / 22.00,
  P4 18.82 / 17.82, P5 13.09 / 12.09. Bid ceilings at EUR 10 minimum: P2 15.83, P3 13.00, P4 8.82, P1 3.87, P5 3.09 (LV).
- US/CA/AU free shipping costs EUR 18.65-32.52 per priority order on these assumptions. That is the single biggest
  margin leak, and fixing it needs a settings decision by 2026-10-31, not a cost input.
- Under the W3-13 policy (if the owner applies it): US/CA/AU loss per priority order falls to EUR 7.64-21.51 (still
  organic-only). EU other: 13 of 22 SKUs >= EUR 10 (was 7); P3 14.84 and P4 10.67 cross, P1 stays -3.13 and P2 8.83
  because the EUR 150 threshold exempts them.

DRAFT for owner. Assumptions, not facts. Not sent. Nothing applied.
