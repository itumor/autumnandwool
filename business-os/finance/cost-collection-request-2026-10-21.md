# Cost-collection request, 22 visible SKUs (FIN-01, FIN-02) — DRAFT for owner

Ask: fill 5 cost columns per visible SKU in `business-os/finance/sku-cost-proposals-staging.csv`. Owner confirms, then
owner copies confirmed values into `business-os/sku-economics.csv`. Finance never writes the CSV.
Schedule (master-plan ruling C4): PRD proposals 2026-10-30 (8 SKUs) and 2026-11-06 (all 22); owner confirms 5 priority
SKUs + sets min contribution 2026-11-04 (fallback 2026-11-11); all 22 confirmed 2026-11-11; GRO gets break-even CAC for
priority SKUs 2026-11-15.
Not accounting or tax advice. Owner sends this; Finance sends nothing.

## Coverage today (Actual)
`python3 business-os/unit_economics.py --selftest` -> `selftest ok` (run 2026-10-21).
`python3 business-os/unit_economics.py` -> `0 costed, 82 TODO (22 of them visible on the store)`.
Break-even CAC unknown for every SKU. All 22 visible rows below have all five cost columns blank.

## Who supplies which column
| Column | Meaning (per order, EUR) | Supplier | Evidence wanted |
|---|---|---|---|
| `materials_labour_eur` | Yarn grams x yarn price per gram + make time x labour rate | Founder / Production (G0: 3 timed units per priority SKU, yarn grams, labour rate) | Yarn invoice, timing notes |
| `shipping_eur` | Our carrier cost per parcel (site advertises free shipping) | Operations, carrier rates per region (owner decision 8, 2026-10-28) | Carrier price list, date |
| `payment_eur` | Card/PayPal fee per order + Squarespace transaction fee if on Basic | Owner: rates shown on the actual Stripe/PayPal account and Squarespace billing page | Screenshot or statement line |
| `packaging_eur` | Box/bag, tissue, care card, label, tape | Production / Operations | Supplier invoice |
| `returns_allowance_eur` | Expected return/refund cost per order | Owner assumption, labelled as assumption until returns data exists | Owner said on DATE |

## The 22 visible SKUs (from `business-os/sku-economics.csv`, stock = 2026-10-17 export, may be stale)
| # | product_id | Title | Price EUR | Net ex VAT 21% | Stock | Missing |
|---|---|---|---|---|---|---|
| 1 | 69105a2903d8727c4c7e8dfa | 100% Wool Long Shawl Cardigan – Handmade Warm Knit | 145.00 | 119.83 | 16 | all 5 |
| 2 | 691050bcb0c4a7226c535650 | Black Merino Wool Raglan Cardigan | 160.00 | 132.23 | 6 | all 5 |
| 3 | 69105a20b0c4a7226c53591c | Distressed Wool Raglan Sweater — Oversized | 155.00 | 128.10 | 1 | all 5 |
| 4 | 69105bd9b0c4a7226c5359f0 | Hand-Knitted Merino Wool Raglan Sweater - Dusty Pink Oversized Jumper | 155.00 | 128.10 | 6 | all 5 |
| 5 | 691059de03d8727c4c7e8dd9 | Lambswool Raglan Crew — Women's Relaxed Jumper | 136.00 | 112.40 | 16 | all 5 |
| 6 | 691059deb0c4a7226c535904 | Lambswool Raglan Crew — Women's Relaxed Jumper | 136.00 | 112.40 | 8 | all 5 |
| 7 | 69105a2ab0c4a7226c53591f | Long Wool Cardigan — Women's Shawl Collar | 145.00 | 119.83 | 12 | all 5 |
| 8 | 69105a2694cd8c749255d65d | Merino Striped Oversized Sweater — Women's Jumper | 165.00 | 136.36 | 1 | all 5 |
| 9 | 69105a8503d8727c4c7e8e1d | Merino Turtleneck — Women's Lightweight Knit | 110.00 | 90.91 | 360 [VERIFY] | all 5 |
| 10 | 69105624c6bfa9183a014d2a | Merino Wool Hat & Scarf Set | 110.00 | 90.91 | 6 | all 5 |
| 11 | 69105a8403d8727c4c7e8e1c | Open-Front Wool Cardigan — Women's Side-Slit Knit | 155.00 | 128.10 | 1 | all 5 |
| 12 | 69105adfb0c4a7226c535976 | Oversized Merino Turtleneck — Dusty Pink Raglan | 155.00 | 128.10 | 1 | all 5 |
| 13 | 6915d24b03d8727c4c8380ea | Oversized Merino Wool V-Neck Sweater Vest | 126.00 | 104.13 | 2 | all 5 |
| 14 | 691055d8dc1bc40ece1f451a | Oversized Wool Raglan Sweater — Beige Melange | 155.00 | 128.10 | 1 | all 5 |
| 15 | 6910544d03d8727c4c7e8c2e | Oversized Wool V-Neck Vest - Beige Melange | 126.00 | 104.13 | 1 | all 5 |
| 16 | 69105a83b0c4a7226c535945 | Oversized Wool V-Neck Vest - Beige Melange | 126.00 | 104.13 | 1 | all 5 |
| 17 | 691059dc03d8727c4c7e8dd6 | Pure Wool Side-Slit Sweater | 136.00 | 112.40 | 16 | all 5 |
| 18 | 691059dd03d8727c4c7e8dd8 | Pure Wool Side-Slit Sweater | 136.00 | 112.40 | 16 | all 5 |
| 19 | 69105ad603d8727c4c7e8e4e | Pure Wool Stand-Collar Sweater — Women's Knit | 136.00 | 112.40 | 12 | all 5 |
| 20 | 69105690dc1bc40ece1f4561 | Rib-Knit Beanie — Unisex | 45.00 | 37.19 | 220 [VERIFY] | all 5 |
| 21 | 691059dfdc1bc40ece1f4648 | Women's Classic Lambswool Crew Sweater | 136.00 | 112.40 | 16 | all 5 |
| 22 | 69105acfb0c4a7226c53596e | Women's wool stand collar sweater | 136.00 | 112.40 | 16 | all 5 |

Net ex VAT = price / 1.21 (sheet assumes LV 21% for every sale; destination VAT/OSS = accountant question Q1).

## Data anomalies found (flag only, nothing changed)
1. **Duplicate titles, different product_ids:** rows 5/6 (Lambswool Raglan Crew), 15/16 (V-Neck Vest Beige Melange),
   17/18 (Pure Wool Side-Slit Sweater). Owner: same product listed twice, or different colours/yarns? If duplicates,
   stock may be double counted (16+8, 1+1, 16+16 units).
2. **Placeholder-looking stock:** turtleneck 360, beanie 220 (master-plan decision 4). Do not plan cash or ads on them.
3. **Eight visible SKUs show stock 1-2** (rows 3, 8, 11, 12, 13, 14, 15, 16). One sale each sells out; a paid push on them is not worth it.

## Public fee schedules (research, read-only, 2026-10-21) — PROPOSED input for `payment_eur`, owner to confirm
Sources: https://stripe.com/en-lv/pricing and https://www.squarespace.com/pricing, both read 2026-10-21. These are
**public list rates**, not the account's actual rates. Squarespace may process cards through its own Stripe
integration with different rates [VERIFY on the account's payout/fee lines].
- Stripe standard EEA card 1.5% + EUR 0.25; premium EEA 2.8% + EUR 0.25; UK 2.5% + EUR 0.25; international 3.15% +
  EUR 0.25 (+2% if currency conversion). Standard payouts free; schedule rolling/weekly/monthly (account setting, TODO owner).
- Squarespace (prices shown in EUR on 2026-10-21): Basic EUR 11/mo annual or EUR 15/mo monthly, **2% transaction fee on
  online store sales**, no Code Injection; Core EUR 17/24, 0% store fee, Code Injection included; Advanced EUR 29/42.
- **Finding:** the site has no Code Injection (PROJECT-HANDBOOK s3: 403 plan gate), which matches Basic. If so,
  every order also pays 2% to Squarespace. [VERIFY current plan on the Squarespace billing page.] Fee base (incl. or
  excl. VAT) [VERIFY].

| Price EUR | Net ex VAT | Stripe EEA std | Stripe EEA premium | Stripe UK | Stripe intl | Squarespace 2% (if Basic) | EEA std + 2% | EEA premium + 2% |
|---|---|---|---|---|---|---|---|---|
| 45.00 | 37.19 | 0.92 | 1.51 | 1.38 | 1.67 | 0.90 | 1.82 | 2.41 |
| 110.00 | 90.91 | 1.90 | 3.33 | 3.00 | 3.71 | 2.20 | 4.10 | 5.53 |
| 126.00 | 104.13 | 2.14 | 3.78 | 3.40 | 4.22 | 2.52 | 4.66 | 6.30 |
| 136.00 | 112.40 | 2.29 | 4.06 | 3.65 | 4.53 | 2.72 | 5.01 | 6.78 |
| 145.00 | 119.83 | 2.42 | 4.31 | 3.88 | 4.82 | 2.90 | 5.32 | 7.21 |
| 155.00 | 128.10 | 2.57 | 4.59 | 4.12 | 5.13 | 3.10 | 5.67 | 7.69 |
| 160.00 | 132.23 | 2.65 | 4.73 | 4.25 | 5.29 | 3.20 | 5.85 | 7.93 |
| 165.00 | 136.36 | 2.73 | 4.87 | 4.38 | 5.45 | 3.30 | 6.03 | 8.17 |

Computed from list rates on price incl. VAT. Conservative proposal for `payment_eur` until account rates are known:
the "EEA premium + 2%" column. Owner to confirm or replace with account rates. PayPal rates: TODO once connected.

## Review checklist for each PRD cost proposal (FIN-02)
- [ ] Each value has a source (invoice, timing note, carrier list, account rate, or "owner said on DATE").
- [ ] Materials+labour uses timed units (3 per priority SKU), not a guess; labour rate stated.
- [ ] Shipping is the worst-case region we offer free shipping to, or one row per region in a note.
- [ ] Returns allowance labelled "owner assumption".
- [ ] Duplicate-title rows resolved (same cost or explained difference).
- [ ] Owner initials + date in `owner_confirmed_date` before anything goes into `sku-economics.csv`.
- [ ] After the owner writes the CSV: Finance runs `unit_economics.py --selftest` then `unit_economics.py`, pastes output
      as-is into the unit-economics review, and sends break-even CAC (`contrib`) per priority SKU to GM and Growth.

## Owner message draft (owner sends, to Production/self)
Need 5 cost numbers per visible SKU, 8 SKUs by 30 Oct, all 22 by 6 Nov. Sheet: `business-os/finance/sku-cost-proposals-staging.csv`.
Per SKU: yarn+labour, our shipping cost, card/plan fees, packaging, returns allowance. Source per number.
Also: confirm turtleneck 360 / beanie 220 stock; say if rows 5/6, 15/16, 17/18 are duplicates.
