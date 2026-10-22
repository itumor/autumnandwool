# BE_CAC worksheet, priority SKUs   Status: DRAFT, BLOCKED (GRO-15)   prepared 2026-10-21 (wave 2)

aw-growth-marketing. Purpose: when costs are confirmed, GRO-15 is a copy-paste job, not new work.
Owner inputs: `owner-inputs-wave2.md` rows 5-7. Rule: no budget without a break-even CAC (hard rule 5).

## Formulas (same as `business-os/unit_economics.py` `economics()`)
- Net price ex VAT = price_eur / (1 + vat_rate)
- CM2 = BE_CAC = net - (materials_labour + shipping + payment + packaging + returns_allowance)
- Target CAC = `target_cac_eur` if set, else 0.6 x BE_CAC (skill `aw-paid-ads-testing` s1)
- Max CAC (FIN method) = CM2 - minimum contribution per order (decision 23). Paid-promotable only if Max CAC > 0.
  Use the **lower** of Target CAC and Max CAC as the CAC goal in briefs.
- Test budget per concept = 3 x BE_CAC. Kill: spend >= 2 x BE_CAC with 0 orders; spend >= 3 x BE_CAC with CAC > BE_CAC.
- Scale only after contribution after CAC > 0 on >= 3 orders.

## Table (SKUs from GM provisional pick `head-of-ecommerce/priority-5-sku-proposal-2026-10-21.md`, owner decides 24 Oct)
Price and VAT from `sku-economics.csv` (21 Oct). Net is arithmetic on those two columns. Every cost cell is TODO.

| # | SKU (product_id prefix) | Price EUR | Net ex VAT EUR | Variable costs EUR | BE_CAC (CM2) EUR | Target CAC EUR | Min contribution EUR | Max CAC EUR | Test budget/concept (3x) EUR | Kill 1 (2x, 0 orders) EUR | Paid-promotable? | GREEN + max units |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Merino Wool Raglan Cardigan (`691050bcb0c4`) | 160.00 | 132.23 | TODO (G1) | TODO | TODO | TODO (#23) | TODO | TODO | TODO | TODO | MISSING (G2) |
| 2 | Merino Raglan Sweater, Dusty Pink (`69105bd9b0c4`) | 155.00 | 128.10 | TODO (G1) | TODO | TODO | TODO (#23) | TODO | TODO | TODO | TODO | MISSING (G2) |
| 3 | Women's Classic Lambswool Crew (`691059dfdc1b`) | 136.00 | 112.40 | TODO (G1) | TODO | TODO | TODO (#23) | TODO | TODO | TODO | TODO | MISSING (G2) |
| 4 | Merino Wool Hat & Scarf Set (`69105624c6bf`) | 110.00 | 90.91 | TODO (G1) | TODO | TODO | TODO (#23) | TODO | TODO | TODO | TODO | MISSING (G2) |
| 5 | Rib-Knit Beanie (`69105690dc1b`) | 45.00 | 37.19 | TODO (G1) | TODO | TODO | TODO (#23) | TODO | TODO | TODO | TODO | MISSING (G2) |
| alt | Merino Turtleneck (`69105a8503d8`) | 110.00 | 90.91 | TODO (G1) | TODO | TODO | TODO (#23) | TODO | TODO | TODO | TODO | MISSING (G2) |
| alt | 100% Wool Long Shawl Cardigan (`69105a2903d8`) | 145.00 | 119.83 | TODO (G1) | TODO | TODO | TODO (#23) | TODO | TODO | TODO | TODO | MISSING (G2) |

Watch-out (no number implied): the beanie's net is EUR 37.19 **before** any cost, so its BE_CAC is below that.
A single paid order may not be affordable; as a gift add-on it may be organic-only. Decide on real costs, not this note.

## Steps when inputs land
1. Owner confirms costs in `sku-economics.csv` (G1). FIN runs `python3 business-os/unit_economics.py`; copy `contrib` into BE_CAC.
2. Owner sets minimum contribution (#23); fill Max CAC; mark Paid-promotable.
3. PRD capacity file: copy GREEN/AMBER and max units. AMBER = organic only.
4. Fill test-brief budget lines (`test-2026-10-21-dec-first-signal.md`) and `budget-proposal-2026-12.md`.
5. Move GRO-15 to DONE with a link here.

The README s9 EUR 33.10 example is illustrative and is not used anywhere in this table.
