# Priority 5 SKUs — provisional proposal (DRAFT for owner, decide 24 Oct, re-confirm 4 Nov)

Author: Head of E-commerce / GM (agent), 2026-10-21. Master plan decision 2, ruling C5. Nothing changed on the store.

**One line:** pick on readiness now (real photos, sizes, stock depth, one clean listing); CM2 is unknown for all 82
SKUs (`unit_economics.py`: 0 costed, 82 TODO, 22 visible TODO), so this list must be re-checked on 4 Nov once costs exist.

## Proposed 5

| # | SKU (product_id prefix) | Price incl. VAT | Stock (17 Oct export) | Why | Readiness gaps | Role |
|---|---|---|---|---|---|---|
| 1 | Merino Wool Raglan Cardigan (`691050bcb0c4`) | EUR 160 | 6 (2 per colour Black/Brown/Blue) | Most-worked PDP: title, colour copy, Brown feed image fixed 19 Oct; full cm measurements in description; highest price of the five | Blue colour has no real photo; no size selector (one size? `[VERIFY owner]`); "100% merino" claim needs supplier evidence (G8) | Hero sweater/cardigan |
| 2 | Hand-Knitted Merino Raglan Sweater, Dusty Pink (`69105bd9b0c4`) | EUR 155 | 6 (3 S/M, 3 L/XL) | One colour so every variant has a real photo; two sizes with cm measurements; matches GSC query "oversized merino wool sweater" (pos 27) | Title says "Hand-Knitted": claim evidence needed (G8); 6 units only | Search-led sweater |
| 3 | Women's Classic Lambswool Crew Sweater (`691059dfdc1b`) | EUR 136 | 16 (4 each S-XL) | Deepest real-looking stock among sweaters, 4 sizes, 8 images, single colour, single listing | Garment measurements in cm not found in description `[VERIFY CRO]`; "100% lambswool" evidence (G8) | Everyday core sweater |
| 4 | Merino Wool Hat & Scarf Set (`69105624c6bf`) | EUR 110 | 6 (2 per colour Black/Brown/Gray) | Gift item at mid price; sizes stated (54-58 cm, 190 x 36 cm); 17 images; PRD hero-gift candidate | Brown and Gray have no real photo -> promote Black only until photos; "RWS-certified, mulesing-free, spun in Italy" needs supplier proof (G8) | Gift, mid price |
| 5 | Rib-Knit Beanie, unisex (`69105690dc1b`) | EUR 45 | 220 (11 colours x 20) — looks like placeholder | Only gift entry price under EUR 100; one size stated | 11 colours, real photos missing per colour; stock 220 needs owner confirmation (decision 4); add-to-cart no-ops if no colour picked (known bug) | Gift entry, AOV add-on |

Alternates (timed by Production anyway, so ready to swap in on 4 Nov):
- **Merino Turtleneck, lightweight (`69105a8503d8`)**, EUR 110, 12 colours x XS/S/M, full size table. Swap in if the
  turtleneck photo shoot (C7, by 31 Oct) lands and the owner confirms the 360 stock figure. Biggest photo ask today.
- **100% Wool Long Shawl Cardigan (`69105a2903d8`)**, EUR 145, stock 16, S-XL. Swap in if the raglan cardigan's
  Blue photo or size question cannot be solved by 14 Nov.

Production times 8 SKUs (production.md: "GM's 5 plus beanie + hat set"). Since beanie and hat set are already in
the five, PRD's other 2 slots go to the two alternates above.

## Excluded and why
| SKU(s) | Reason |
|---|---|
| Distressed raglan, striped oversized, open-front side-slit cardigan, dusty-pink oversized turtleneck, beige raglan, both beige V-neck vests | Stock 1 each: a promotion sells out on the first order. Fine as one-offs, not as promoted SKUs |
| Merino V-neck sweater vest | Stock 2 |
| Lambswool Raglan Crew (2 listings), Pure Wool Side-Slit (2 listings) | Duplicate listings, dedupe first (decision 20) |
| Both stand-collar sweaters | 1 image each, and a duplicate pair |
| Long Wool Cardigan, shawl collar | Close to alternate #2; keep one cardigan of this type |

## Selection rule used (owner may change)
1. Real photo for every variant that will be promoted (or promote only the colours that have one).
2. Size information on the PDP (cm).
3. Stock of at least 6 units in the export (owner confirms physical stock by 24 Oct).
4. One clean listing (no duplicate).
5. Spread of price points: EUR 45 / 110 / 136 / 155 / 160 so gifts and core sweaters are both covered.
6. **Not yet used, because unknown:** CM2 (break-even CAC) per SKU. On 4 Nov any SKU whose CM2 is below the minimum
   contribution per order drops out of paid promotion (it can still be sold and promoted organically).

## Effect, cost, reversibility
- KPI effect: focuses PDP work (CRO), timing/costing (PRD), photos (CRE), pins and listings (SEO) on 5 pages instead
  of 22, so the first measured conversion and CM2 numbers arrive on the products we will promote.
- Cost: EUR 0. Time: owner photos for cardigan Blue, hat set Brown/Gray, beanie colours (already on the owner list).
- Reversible: yes, provisional until 4 Nov.

## Owner to answer by 24 Oct
- [ ] Approve the 5 (or swap with an alternate).
- [ ] Cardigan: one size or several? `TODO: owner`
- [ ] Physical stock of all five, especially beanie 220. `TODO: owner`
- [ ] Which beanie colours physically exist and can be photographed by 14 Nov. `TODO: owner`

Sources: `business-os/sku-economics.csv`, `products_Oct-17_10-46-00PM.csv` (descriptions, variants, image counts),
`PROJECT-HANDBOOK.md` s5, s7, s8, `plans/2026-2027/production.md` s2, `plans/2026-2027/master-plan.md` decisions 2, 4, 20 and C5, C7.
DRAFT: not sent, no store change.
