# QC checklist: final inspection, every unit (PRD-12)

DRAFT — for owner approval. aw-production, 2026-10-21. Method: aw-qc-and-labelling skill. Handmade volume is small,
so 100% of units are inspected (no AQL sampling). Not legal advice: label wording and languages are for the adviser to confirm.

## 1. Checks (pass/fail per line, before packing)
| # | Check | Pass rule |
|---|---|---|
| 1 | Right item | SKU, colour, size match the order and the product page photo |
| 2 | Measurements | Width, length, sleeve, hem vs the PDP size table. Tolerance: owner sets (PRD-13). Planning value ±2 cm = ASSUMPTION A-PRD-19 |
| 3 | Symmetry | Sleeves equal, side seams straight, hem level, neckline centred |
| 4 | Knit surface | No dropped/laddered stitches, holes (except the designed holes on the Distressed Raglan), tight/loose rows, stripe misalignment |
| 5 | Linking / seams | Closed, no gaps or puckering; yarn ends woven in and trimmed |
| 6 | Finish | Washed/blocked to shape, no drying creases, lint, stains or odour |
| 7 | Shade | One dye lot across body and sleeves; compare in daylight |
| 8 | Hand-feel / pilling | No visible pilling on a new garment |
| 9 | Trims | Buttons secure (pull test), buttonholes finished (cardigans) |
| 10 | Labels | Fibre-composition label sewn in and matching the supplier spec sheet for this yarn; care label present and separate. No spec sheet = Critical (do not ship) once label rules are confirmed by the adviser |
| 11 | Paperwork | Care card included; packing slip matches the order |

## 2. Defect grades
| Grade | Examples | Action |
|---|---|---|
| Critical | Wrong item, hole, missing or wrong composition label | Do not ship |
| Major | Measurement out of tolerance, shade mismatch, dropped stitch | Rework, or do not ship |
| Minor | Loose end, lint | Fix on the spot, then pass |

A repeated defect on one SKU (2 in 4 weeks) puts the SKU on AMBER in the capacity file until it is fixed.

## 3. Defect log (proposed `business-os/knitwear-making/qc-log.csv`, created only after the owner agrees, PRD-13)
```
date,order_no,sku,size,colour,check_no,grade,description,action(rework/scrap/shipped),minutes_lost
```
Weekly KPI: defect rate = units failing first inspection / units inspected. Planning baseline 5% (ASSUMPTION A-PRD-17).

## 4. Care label default (verify per yarn)
Wool: hand wash cold or wool cycle, dry flat, no tumble dry. ISO 3758 symbols only per supplier care advice.
Never "machine washable" without supplier proof.

## TODO / missing data
Tolerance (owner), qc-log creation (owner), label wording + languages (adviser to confirm, PRD-19), spec sheets (PRD-18).
