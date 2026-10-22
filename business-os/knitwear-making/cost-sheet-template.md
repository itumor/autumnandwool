# Per-SKU cost sheet template + 22-SKU cost-collection list (PRD-08)

DRAFT — for owner approval. aw-production, 2026-10-21. Real data only (prices, VAT, product_ids from
`business-os/sku-economics.csv`). The assumption-based fill is in `sku-cost-proposals-2026-10-21.md` (ASSUMPTION).

## 1. One cost sheet per SKU (copy per SKU)

```
SKU: ____  product_id: ____  size(s) costed: ____  colour / dye lot: ____  date: ____  filled by: ____

MATERIALS
| Yarn (supplier, name, count Nm) | Colour/lot | Grams in finished garment | Waste % | Grams used | EUR/kg (invoice no.) | EUR |
| Trims: buttons | qty | EUR each | EUR |
| Labels: composition/care, brand | qty | EUR each | EUR |
| Thread / other | | | EUR |
Materials total EUR: ____

LABOUR (median of 3 timed units, from timing-sheet.md)
| Step | Minutes |
| Knitting (manual machine) | |
| Linking / seaming | |
| Hand finishing (ends, buttons, bands) | |
| Wash / block (active minutes only) | |
| QC + labelling | |
| Packing | |
Total minutes: ____  x labour rate EUR ____/h / 60 = labour EUR ____

materials_labour_eur = materials + labour = ____
Net price = price / 1.21 = ____   CM1 = net − materials_labour = ____ (__%)
Evidence attached: yarn invoice [ ]  timing notes [ ]  scale photo [ ]   Owner OK: ____ date ____
```

## 2. 22-SKU cost-collection list (real data)
40% CM1 ceiling = the most materials+labour can cost while CM1 stays at or above 40% of net (net x 0.60).
This is a benchmark from the unit-economics skill, not a rule.

| # | product_id | Title | Price EUR | Net ex VAT 21% | 40% CM1 ceiling EUR | Timing priority |
|---|---|---|---|---|---|---|
| 1 | 691050bcb0c4a7226c535650 | Black Merino Wool Raglan Cardigan | 160.00 | 132.23 | 79.34 | P1 (by 25 Oct) |
| 2 | 69105bd9b0c4a7226c5359f0 | Hand-Knitted Merino Wool Raglan Sweater - Dusty Pink | 155.00 | 128.10 | 76.86 | P2 (by 25 Oct) |
| 3 | 691059dfdc1bc40ece1f4648 | Women's Classic Lambswool Crew Sweater | 136.00 | 112.40 | 67.44 | P3 (by 25 Oct) |
| 4 | 69105624c6bfa9183a014d2a | Merino Wool Hat & Scarf Set | 110.00 | 90.91 | 54.55 | P4 (by 25 Oct) |
| 5 | 69105690dc1bc40ece1f4561 | Rib-Knit Beanie — Unisex | 45.00 | 37.19 | 22.31 | P5 (by 25 Oct) |
| 6 | 69105a8503d8727c4c7e8e1d | Merino Turtleneck — Lightweight | 110.00 | 90.91 | 54.55 | Alt 1 (by 31 Oct) |
| 7 | 69105a2903d8727c4c7e8dfa | 100% Wool Long Shawl Cardigan | 145.00 | 119.83 | 71.90 | Alt 2 (by 31 Oct) |
| 8 | 69105a2ab0c4a7226c53591f | Long Wool Cardigan — Shawl Collar | 145.00 | 119.83 | 71.90 | by 20 Nov |
| 9 | 691059de03d8727c4c7e8dd9 | Lambswool Raglan Crew (A) | 136.00 | 112.40 | 67.44 | by 20 Nov (dedupe) |
| 10 | 691059deb0c4a7226c535904 | Lambswool Raglan Crew (B) | 136.00 | 112.40 | 67.44 | by 20 Nov (dedupe) |
| 11 | 69105a20b0c4a7226c53591c | Distressed Wool Raglan Sweater | 155.00 | 128.10 | 76.86 | by 20 Nov |
| 12 | 69105a2694cd8c749255d65d | Merino Striped Oversized Sweater | 165.00 | 136.36 | 81.82 | by 20 Nov |
| 13 | 69105a8403d8727c4c7e8e1c | Open-Front Wool Cardigan — Side-Slit | 155.00 | 128.10 | 76.86 | by 20 Nov |
| 14 | 69105adfb0c4a7226c535976 | Oversized Merino Turtleneck — Dusty Pink | 155.00 | 128.10 | 76.86 | by 20 Nov |
| 15 | 6915d24b03d8727c4c8380ea | Oversized Merino Wool V-Neck Vest | 126.00 | 104.13 | 62.48 | by 20 Nov |
| 16 | 691055d8dc1bc40ece1f451a | Oversized Wool Raglan — Beige Melange | 155.00 | 128.10 | 76.86 | by 20 Nov |
| 17 | 6910544d03d8727c4c7e8c2e | Oversized Wool V-Neck Vest — Beige (A) | 126.00 | 104.13 | 62.48 | by 20 Nov (dedupe) |
| 18 | 69105a83b0c4a7226c535945 | Oversized Wool V-Neck Vest — Beige (B) | 126.00 | 104.13 | 62.48 | by 20 Nov (dedupe) |
| 19 | 691059dc03d8727c4c7e8dd6 | Pure Wool Side-Slit Sweater (A) | 136.00 | 112.40 | 67.44 | by 20 Nov (dedupe) |
| 20 | 691059dd03d8727c4c7e8dd8 | Pure Wool Side-Slit Sweater (B) | 136.00 | 112.40 | 67.44 | by 20 Nov (dedupe) |
| 21 | 69105ad603d8727c4c7e8e4e | Pure Wool Stand-Collar Sweater | 136.00 | 112.40 | 67.44 | by 20 Nov (dedupe) |
| 22 | 69105acfb0c4a7226c53596e | Women's wool stand collar sweater | 136.00 | 112.40 | 67.44 | by 20 Nov (dedupe) |

Missing for all 22: `materials_labour_eur` (Production), `packaging_eur` (Production/OPS). Shipping, payment and returns
columns: see `finance/cost-collection-request-2026-10-21.md`.

## TODO / missing data
- Owner fills one sheet per SKU from real timing and invoices; agent then replaces the ASSUMPTION values.
