# Yarn reorder template + reorder-point method (PRD-14) and December scenario (PRD-20)

DRAFT — for owner approval. aw-production, 2026-10-21. The owner buys; the agent proposes quantities only and contacts
no supplier. Section 3 is an **ASSUMPTION** scenario (register `assumptions-wave3.md`).

## 1. Method
- `ROP (kg) = average weekly yarn use (kg) x supplier lead time (weeks) + safety stock (kg)`
- Safety stock: 2 weeks of use until 8+ weeks of data exist; then `1.65 x sd(weekly use) x sqrt(lead time weeks)` (≈95% service).
- Weekly use = planned units x grams per garment x 1.08 (waste, A-PRD-09).
- **Dye lot:** reorder whole-garment quantities from one lot; never split a garment across lots.
- Order when `on hand − committed ≤ ROP`. Respect MOQ; check FIN cash buffer before any purchase (G3).

## 2. Template (one row per yarn x colour x lot)
| Yarn (supplier, name, Nm) | Colour | Dye lot | On hand kg | Committed kg | Weekly use kg | Lead time wk | Safety kg | ROP kg | Below ROP? | Proposed qty kg (whole garments) | EUR/kg | EUR | MOQ | Needed by | Owner OK |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | |

## 3. December scenario (PRD-20), ASSUMPTION
Plan per week, W45–W50 (2 Nov – 11 Dec), 950 of 1,125 min (84%): 3 hat & scarf sets Black (390 min) + 10 beanies (350) +
1 Dusty Pink raglan (210). Lambswool Crew sells from stock (A-PRD-12). Grams per A-PRD-20, waste 8%, lead time 2 weeks and
safety 2 weeks (A-PRD-15), merino EUR 60/kg (A-PRD-06).

| Yarn (cost class, not a fibre claim) | Colour | Weekly use kg | 6-week need kg | ROP kg (use x 2 + 2 wk safety) | EUR at 60/kg (6 weeks) |
|---|---|---|---|---|---|
| Merino class | Black (hat set) | 1.43 | 8.55 | 5.70 | 513 |
| Merino class | Beanie colour(s) with real photo | 0.97 | 5.83 | 3.89 | 350 |
| Merino class | Dusty Pink | 0.65 | 3.89 | 2.59 | 233 |
| **Total** | | **3.05** | **18.27** | **12.18** | **≈ 1,096** |

Proposal = 6-week need − yarn on hand (unknown, PRD-07). If on hand ≥ 18.3 kg in these colours, buy nothing. Ceiling
EUR ≈1,100 ex shipping (range EUR 550–1,370 at EUR 30–75/kg). Owner purchase decision 32 (16 Nov) after the FIN cash check.
This is a capacity-ceiling scenario, not a demand forecast: there are zero direct orders to date.

## TODO / missing data
Yarn on hand by colour/lot, supplier, price, MOQ, lead time (PRD-07); real grams (PRD-06); FIN cash buffer (decision 7).
