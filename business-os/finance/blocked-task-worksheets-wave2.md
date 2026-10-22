# Worksheets for blocked Finance tasks (FIN-03, FIN-17, FIN-18, FIN-19) — DRAFT, wave 2, 2026-10-21

Purpose: when the owner answers `owner-inputs-wave2.md`, each verdict is a fill-in, not new work.
Labels: **Actual** = from a file; **Computed** = arithmetic on Actual; **Proposed** = public list rate, owner confirms;
blank = TODO. Not accounting or tax advice.

`python3 business-os/unit_economics.py --selftest` -> `selftest ok`. Report: `0 costed, 82 TODO (22 of them visible on the store)`.

## 1. FIN-03 break-even CAC, GM's provisional 5 + 2 alternates
SKUs from `business-os/head-of-ecommerce/priority-5-sku-proposal-2026-10-21.md` (owner approves 2026-10-24).
Price, VAT rate, stock: Actual, `sku-economics.csv` (stock = 2026-10-17 export, may be stale).
Net = price / 1.21 (Computed). "Max materials+labour at 40% CM1" = net x 0.60 (Computed; 40% is a handmade-apparel
benchmark, not a rule). Payment proposal = Stripe EEA premium list rate + 2% Squarespace Basic fee
(`cost-collection-request-2026-10-21.md`, read 2026-10-21; Proposed, replace with account rates).

| # | SKU | product_id | Price | Net | Stock | Max M+L at 40% CM1 | materials_labour | shipping | payment (Proposed) | packaging | returns | CM2 = break-even CAC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Black Merino Wool Raglan Cardigan | 691050bcb0c4a7226c535650 | 160.00 | 132.23 | 6 | 79.34 | TODO PRD/owner | TODO OPS/owner | 7.93 | TODO OPS | TODO owner | TODO |
| 2 | Merino Raglan Sweater, Dusty Pink | 69105bd9b0c4a7226c5359f0 | 155.00 | 128.10 | 6 | 76.86 | TODO | TODO | 7.69 | TODO | TODO | TODO |
| 3 | Women's Classic Lambswool Crew Sweater | 691059dfdc1bc40ece1f4648 | 136.00 | 112.40 | 16 | 67.44 | TODO | TODO | 6.78 | TODO | TODO | TODO |
| 4 | Merino Wool Hat & Scarf Set | 69105624c6bfa9183a014d2a | 110.00 | 90.91 | 6 | 54.55 | TODO | TODO | 5.53 | TODO | TODO | TODO |
| 5 | Rib-Knit Beanie, unisex | 69105690dc1bc40ece1f4561 | 45.00 | 37.19 | 220 [VERIFY] | 22.31 | TODO | TODO | 2.41 | TODO | TODO | TODO |
| A1 | Merino Turtleneck, lightweight | 69105a8503d8727c4c7e8e1d | 110.00 | 90.91 | 360 [VERIFY] | 54.55 | TODO | TODO | 5.53 | TODO | TODO | TODO |
| A2 | 100% Wool Long Shawl Cardigan | 69105a2903d8727c4c7e8dfa | 145.00 | 119.83 | 16 | 71.90 | TODO | TODO | 7.21 | TODO | TODO | TODO |

Finance flag (no number invented): the beanie has EUR 37.19 net. With free shipping, its CM2 may be small or negative
once a real parcel price is known; check it first when OPS rates arrive. As a gift add-on it may still be worth selling,
but likely not with paid traffic.

Finish steps (once owner has written confirmed values into `sku-economics.csv`): run `--selftest`, run the report, paste
output as-is, then fill "Max CAC = CM2 - minimum contribution" (FIN-05) and hand to GM/Growth.

## 2. FIN-05 minimum contribution
Method: `min-contribution-method.md`. Inputs needed: owner rows 2, 9, 11 in `owner-inputs-wave2.md`. Nothing to pre-fill.

## 3. FIN-17 market stall verdicts
| Market | Fee EUR | Extras EUR (table, float, travel, card terminal) | Units brought (physical) | Cash before (week) | Cash after fee | Verdict |
|---|---|---|---|---|---|---|
| Baltic EXPO, 2026-12-11..13 (non-refundable) | TODO (5 levels, booking tool) | TODO | TODO | TODO | TODO | TODO |
| KuKu Tirgus, 2026-11-29, apply by 2026-11-10 | 50.00 (published) | TODO | TODO | TODO | TODO | TODO |
| White Xmas, 2026-12-18..20, apply by 2026-12-14 | TODO | TODO | TODO | TODO | TODO | TODO |
Rule: verdict = affordable now / after week N / no, with lowest Downside balance; Downside assumes zero stall sales
(fee is a sure cost, sales are not). Stall CM2 = net - materials_labour - packaging - card fee (no shipping) [VERIFY
receipt/cash-register rules with accountant].

## 4. FIN-18 free shipping by region vs CM2 (decision 21/28)
Regions from `business-os/operations/carrier-rates.md` s1 (all EUR 0 to the customer today, Actual).
| Region | Carrier + service (owner) | Price per sweater parcel EUR (OPS, with URL + date) | Lowest CM2 among the 5 before shipping | CM2 after shipping | Keep free? |
|---|---|---|---|---|---|
| LV | TODO | TODO | TODO | TODO | TODO owner |
| EU-18 | TODO | TODO | TODO | TODO | TODO owner |
| EE / LT | TODO | TODO | TODO | TODO | TODO owner |
| US / CA / AU | TODO | TODO | TODO | TODO | TODO owner |
| Other (UK, NO, CH, rest) | TODO | TODO | TODO | TODO | Finance proposal: restrict until priced (matches OPS gap 2 in `delivery-promise-reconciliation.md`) |

## 5. FIN-19 gift-season perks margin check (decision 31)
CRO and CX state no perk is offered yet and cost is unknown (`ecommerce-cro/2026-10-21-pdp-copy-proposals.md` l.111;
`customer-experience/support-macros.md` gift note = owner decision 31).
| Perk | Unit cost EUR (owner) | Minutes per order | CM2 of cheapest promoted SKU | CM2 after perk | Verdict |
|---|---|---|---|---|---|
| Handwritten gift note | TODO | TODO | TODO | TODO | TODO |
| Gift wrap / tissue + ribbon | TODO | TODO | TODO | TODO | TODO |
| Gift receipt (no price) | likely 0.00 materials [VERIFY] | TODO | TODO | TODO | TODO |
Rule: a perk is fine if CM2 after perk stays at or above the minimum contribution (FIN-05) on the beanie, the
cheapest gift item.
