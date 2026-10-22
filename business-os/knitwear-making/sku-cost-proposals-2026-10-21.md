# SKU cost proposals, 22 visible SKUs (PRD-09, PRD-15): ASSUMPTION-BASED

DRAFT — for owner approval. aw-production, 2026-10-21, assumption mode.
**Every cost below is an ASSUMPTION** (register: `business-os/knitwear-making/assumptions-wave3.md`). Do not copy any
of it into `sku-economics.csv` or `finance/sku-cost-proposals-staging.csv` as a confirmed value. Owner replaces it with
timed/weighed/invoiced figures (PRD-06, PRD-07) and then confirms (decision 28a, 4 Nov; 28b, 11 Nov).

## Formula (all inputs shown)
`materials_labour_eur = grams x 1.08 (A-PRD-09 waste) x EUR/kg / 1000 + trims (A-PRD-10) + minutes x EUR 0.20 (A-PRD-01 EUR 12/h)`
Net = price / 1.21. CM1 = net − materials_labour. 40% CM1 benchmark ceiling = net x 0.60 (unit-economics skill).
**CM2 / margins: single source = `business-os/finance/sku-margins-assumed-wave3.md`** (GM rulings W3-2/W3-3). The
Pkg / Pay / Ship / Ret / Indic. CM2 columns below used Production's withdrawn placeholders (packaging EUR 3 / 2, shipping
EUR 12 / 7 flat) and are **superseded; do not cite them**. Use Finance's per-zone CM2 (OPS packaging EUR 1.50, shipping by
zone). The materials+labour and CM1 columns here remain Production's input to that file.
I could not run `unit_economics.py` (no shell in this session), so this is a hand calculation. Finance must run the script after the owner confirms values.

## Per SKU (ASSUMPTION)

| # | SKU | Price | Net | Yarn EUR | Trims | Labour EUR | **Materials+labour** | 40% ceiling | CM1 EUR | CM1 % | Pkg | Pay | Ship | Ret | **Indic. CM2** | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Merino Raglan Cardigan (P1) | 160 | 132.23 | 42.12 | 3.20 | 52.00 | **97.32** | 79.34 | 34.91 | 26.4% | 3.00 | 7.93 | 12 | 6.61 | **5.37** | CM1 < 40%; CM2 thin |
| 2 | Merino Raglan, Dusty Pink (P2) | 155 | 128.10 | 38.88 | 0.80 | 42.00 | **81.68** | 76.86 | 46.42 | 36.2% | 3.00 | 7.69 | 12 | 6.41 | **17.32** | CM1 < 40% |
| 3 | Classic Lambswool Crew (P3) | 136 | 112.40 | 29.70 | 0.80 | 40.00 | **70.50** | 67.44 | 41.90 | 37.3% | 3.00 | 6.78 | 12 | 5.62 | **14.50** | CM1 < 40% |
| 4 | Hat & Scarf Set (P4) | 110 | 90.91 | 28.51 | 1.00 | 26.00 | **55.51** | 54.55 | 35.40 | 38.9% | 3.00 | 5.53 | 12 | 4.55 | **10.32** | CM1 < 40% |
| 5 | Rib-Knit Beanie (P5) | 45 | 37.19 | 5.83 | 0.50 | 7.00 | **13.33** | 22.31 | 23.86 | 64.2% | 2.00 | 2.41 | 7 | 1.86 | **10.59** | ok |
| 6 | Merino Turtleneck light (Alt 1) | 110 | 90.91 | 20.74 | 0.80 | 44.00 | **65.54** | 54.55 | 25.37 | 27.9% | 3.00 | 5.53 | 12 | 4.55 | **0.29** | break-even; check price/minutes |
| 7 | 100% Wool Long Shawl Cardigan (Alt 2) | 145 | 119.83 | 36.72 | 0.80 | 60.00 | **97.52** | 71.90 | 22.31 | 18.6% | 3.00 | 7.21 | 12 | 5.99 | **−5.89** | loses money (assumed) |
| 8 | Distressed Wool Raglan | 155 | 128.10 | 25.92 | 0.80 | 46.00 | **72.72** | 76.86 | 55.38 | 43.2% | 3.00 | 7.69 | 12 | 6.41 | **26.28** | ok |
| 9 | Lambswool Raglan Crew (A) | 136 | 112.40 | 29.70 | 0.80 | 40.00 | **70.50** | 67.44 | 41.90 | 37.3% | 3.00 | 6.78 | 12 | 5.62 | **14.50** | CM1 < 40%; dup |
| 10 | Lambswool Raglan Crew (B) | 136 | 112.40 | 29.70 | 0.80 | 40.00 | **70.50** | 67.44 | 41.90 | 37.3% | 3.00 | 6.78 | 12 | 5.62 | **14.50** | CM1 < 40%; dup |
| 11 | Long Wool Cardigan, Shawl Collar | 145 | 119.83 | 45.90 | 0.80 | 60.00 | **106.70** | 71.90 | 13.13 | 11.0% | 3.00 | 7.21 | 12 | 5.99 | **−15.07** | loses money (assumed) |
| 12 | Merino Striped Oversized | 165 | 136.36 | 42.12 | 0.80 | 48.00 | **90.92** | 81.82 | 45.44 | 33.3% | 3.00 | 8.17 | 12 | 6.82 | **15.45** | CM1 < 40% |
| 13 | Open-Front Side-Slit Cardigan | 155 | 128.10 | 30.24 | 0.80 | 52.00 | **83.04** | 76.86 | 45.06 | 35.2% | 3.00 | 7.69 | 12 | 6.41 | **15.96** | CM1 < 40% |
| 14 | Oversized Merino Turtleneck, Dusty Pink | 155 | 128.10 | 42.12 | 0.80 | 46.00 | **88.92** | 76.86 | 39.18 | 30.6% | 3.00 | 7.69 | 12 | 6.41 | **10.08** | CM1 < 40% |
| 15 | Oversized Merino V-Neck Vest | 126 | 104.13 | 22.68 | 0.80 | 28.00 | **51.48** | 62.48 | 52.65 | 50.6% | 3.00 | 6.30 | 12 | 5.21 | **26.14** | ok |
| 16 | Oversized Wool Raglan, Beige | 155 | 128.10 | 25.92 | 0.80 | 42.00 | **68.72** | 76.86 | 59.38 | 46.4% | 3.00 | 7.69 | 12 | 6.41 | **30.28** | ok |
| 17 | Wool V-Neck Vest, Beige (A) | 126 | 104.13 | 15.12 | 0.80 | 28.00 | **43.92** | 62.48 | 60.21 | 57.8% | 3.00 | 6.30 | 12 | 5.21 | **33.70** | ok; dup |
| 18 | Wool V-Neck Vest, Beige (B) | 126 | 104.13 | 15.12 | 0.80 | 28.00 | **43.92** | 62.48 | 60.21 | 57.8% | 3.00 | 6.30 | 12 | 5.21 | **33.70** | ok; dup |
| 19 | Pure Wool Side-Slit (A) | 136 | 112.40 | 23.76 | 0.80 | 40.00 | **64.56** | 67.44 | 47.84 | 42.6% | 3.00 | 6.78 | 12 | 5.62 | **20.44** | ok; dup |
| 20 | Pure Wool Side-Slit (B) | 136 | 112.40 | 23.76 | 0.80 | 40.00 | **64.56** | 67.44 | 47.84 | 42.6% | 3.00 | 6.78 | 12 | 5.62 | **20.44** | ok; dup |
| 21 | Pure Wool Stand-Collar | 136 | 112.40 | 25.92 | 0.80 | 42.00 | **68.72** | 67.44 | 43.68 | 38.9% | 3.00 | 6.78 | 12 | 5.62 | **16.28** | CM1 < 40%; dup |
| 22 | Women's wool stand collar | 136 | 112.40 | 25.92 | 0.80 | 42.00 | **68.72** | 67.44 | 43.68 | 38.9% | 3.00 | 6.78 | 12 | 5.62 | **16.28** | CM1 < 40%; dup |

## What this says (under the assumptions only)
Points 2–5 below refer to the superseded indicative CM2. Finance's current reading (LV): Long Wool Cardigan Shawl Collar
−6.57 (loses money even in LV), Alt 2 +2.61, Turtleneck 8.79, P1 13.87 but Max CAC 3.87; P2/P3 are the only paid-capable
priority SKUs (LV + EE/LT). See the FIN file for all zones.

1. **Labour is the biggest cost:** 55–65% of materials+labour on every garment. A-PRD-01 (EUR 12/h) and A-PRD-21
   (minutes) move the results more than yarn price does. Timing real units (PRD-06) matters more than chasing yarn invoices.
2. **The two long shawl cardigans lose money** at EUR 145 under these assumptions (850 g, 300 min). If the owner's real
   minutes are near 180, they break even. Owner check before any promotion: real minutes, grams, or price.
3. **Turtleneck (Alt 1) is at break-even** (CM2 EUR 0.29). Do not swap it into the priority 5 for paid traffic until it has been timed.
4. **Beanie has the best margin** (64% CM1) but the lowest CM2 in EUR (10.59), which is under any likely paid CAC.
   Use it as an organic gift or add-on, not as a paid-ads hero.
5. **Priority-5 indicative CM2:** Dusty Pink 17.32 > Lambswool Crew 14.50 > Beanie 10.59 ≈ Hat set 10.32 > Raglan
   Cardigan 5.37. The GM's "hero" cardigan has the thinnest CM2. GM/FIN to re-check on 4 Nov with confirmed costs.
6. 13 of 22 SKUs are below the 40% CM1 benchmark (a benchmark, not a rule).

## Sensitivity (priority 5, materials+labour EUR)
Low = EUR 6/h, minutes −25%, grams −20%, low yarn price. High = EUR 18/h, minutes +50%, grams +20%, high yarn price.
Trims held at base.

| SKU | Low: labour + yarn + trims | Low total | Base | High: labour + yarn + trims | High total | Net price |
|---|---|---|---|---|---|---|
| Raglan Cardigan | 19.50 + 16.85 + 3.20 | **39.55** | 97.32 | 117.00 + 63.18 + 3.20 | **183.38** | 132.23 |
| Dusty Pink | 15.75 + 15.55 + 0.80 | **32.10** | 81.68 | 94.50 + 58.32 + 0.80 | **153.62** | 128.10 |
| Lambswool Crew | 15.00 + 16.63 + 0.80 | **32.43** | 70.50 | 90.00 + 49.90 + 0.80 | **140.70** | 112.40 |
| Hat & Scarf Set | 9.75 + 11.40 + 1.00 | **22.15** | 55.51 | 58.50 + 42.77 + 1.00 | **102.27** | 90.91 |
| Beanie | 2.63 + 2.33 + 0.50 | **5.46** | 13.33 | 15.75 + 8.75 + 0.50 | **25.00** | 37.19 |

Low: labour = EUR 0.10/min x 0.75 x minutes; yarn = 0.8 x grams x 1.08 x (merino EUR 30 / lambswool EUR 35 per kg).
High: labour = EUR 0.30/min x 1.5 x minutes; yarn = 1.2 x grams x 1.08 x (merino EUR 75 / lambswool EUR 70 per kg).
In the high case, four of the five priority SKUs cost more than their net price. The range is too wide for pricing decisions,
which is why PRD-06 timing is rank 2 in the owner unblock pack.

## TODO / missing data
- Real minutes (PRD-06), grams, labour rate, yarn invoices (PRD-07). Shipping, packaging, payment, returns: taken over by OPS/FIN (see FIN margins file).
- Duplicate pairs costed identically on purpose (A-PRD-13). If the owner says they are different yarns or colours, cost them separately.
- Finance runs `unit_economics.py` after owner-confirmed values are in the CSV (owner writes it, not agents).
