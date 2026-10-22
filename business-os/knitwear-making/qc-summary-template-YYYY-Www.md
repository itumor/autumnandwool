# QC summary — week [YYYY]-[Www] (PRD-23)   Status: DRAFT for owner approval (AGENT-DOABLE skeleton)

File for the week `[YYYY]-[Www]`. Copy to `business-os/knitwear-making/qc-summary-YYYY-Www.md` once the first units have
been inspected. Definition: **defect rate = units failing first inspection / units inspected** (PRD-23). 100% inspection,
handmade volume small, no AQL sampling (`qc-checklist.md`). This summary starts only after PRD-13 closes: creation of
`business-os/knitwear-making/qc-log.csv` and the measurement tolerance set by the owner (proposal +/-2 cm = A-PRD-19).
Until then, the tables below are placeholders (FILL) and no defect is ever assumed (no QC log = no inspected units
assumed).

## 1. Week inputs (FILL)
Week: [YYYY]-[Www] (period [Mon DD] - [Sun DD Mon], e.g. 2026-W45)
Scope: units shipped in the week + any units inspected but not shipped (rework/scrap).
Source of record: `qc-log.csv` once created (schema in section 6). Until then: FILL manually from the owner's notes.
Owner / maker: Kristine (A-PRD-03).
Units inspected (100% of shipped, every unit): [FILL]
Units failing first inspection: [FILL]
Units reworked and shipped: [FILL]
Units scrapped ( Critical, do not ship ): [FILL]
Minutes lost to rework: [FILL] (compare against the 169 min/week reserve, A-PRD-17)
Repeat defect on the same SKU (2 fails in 4 weeks, puts the SKU on AMBER in the capacity file): [FILL SKU list or none]

## 2. Top line (FILL)
- Defect rate = fails / inspected = [FILL] %.
- Planning baseline (assumed, A-PRD-17): >= 95% first-QC pass = <= 5% fail.
- RAG: [GREEN <= 5% / AMBER 5-8% / RED > 8%] against the proposal baseline. **No measured baseline yet**; the planning
  value is an assumption and must not be quoted as an actual.
- SKUs on AMBER because of a repeated defect: [FILL or none].
- Consequence on the capacity file: SKUs in this AMBER list are not GREEN this week even if stock and photos would
  otherwise allow it.

## 3. Defects by grade (PRD-12 defect grades)
| Grade | Definition (from qc-checklist.md) | Count | % of inspected | SKUs affected | Action taken |
|---|---|---|---|---|---|
| Critical | wrong item, hole (except the designed holes on the Distressed Raglan), missing/wrong composition label | [FILL] | [FILL]% | [FILL] | do not ship |
| Major | measurement out of tolerance, shade mismatch, dropped/laddered stitch | [FILL] | [FILL]% | [FILL] | rework or do not ship |
| Minor | loose end, lint, drying crease, label not yet sewn in | [FILL] | [FILL]% | [FILL] | fix on the spot, then pass |

## 4. Defects by check number (1-11 from qc-checklist.md)
| # Check | Fails (FILL) | % of inspected (FILL) | SKUs affected (FILL) | Notes / root-cause candidate |
|---|---|---|---|---|
| 1 Right item (SKU, colour, size vs order + PDP photo) | [FILL] | [FILL]% | [FILL] | wrong size/colour vs the order |
| 2 Measurements (width, length, sleeve, hem vs PDP size table) | [FILL] | [FILL]% | [FILL] | tolerance = owner sets (A-PRD-19 +/-2 cm planning) |
| 3 Symmetry (sleeves equal, side seams, hem level, neckline) | [FILL] | [FILL]% | [FILL] | |
| 4 Knit surface (dropped/laddered stitches, holes, tight/loose rows, stripe misalignment) | [FILL] | [FILL]% | [FILL] | Distressed Raglan holes are designed, do not count |
| 5 Linking / seams (closed, no puckering; ends woven and trimmed) | [FILL] | [FILL]% | [FILL] | |
| 6 Finish (washed/blocked, no drying creases, lint, stains, odour) | [FILL] | [FILL]% | [FILL] | 24-48 h dry per batch (A-PRD-05) |
| 7 Shade (one dye lot body + sleeves, compare in daylight) | [FILL] | [FILL]% | [FILL] | whole-garment quantities per dye lot (A-PRD-15) |
| 8 Hand-feel / pilling (no visible pilling on a new garment) | [FILL] | [FILL]% | [FILL] | |
| 9 Trims (buttons pull test, buttonholes finished, cardigans only) | [FILL] | [FILL]% | [FILL] | P1 cardigan has buttons (+2.40 trim, A-PRD-10) |
| 10 Labels (fibre-composition label sewn in and matches the supplier spec sheet; care label separate) | [FILL] | [FILL]% | [FILL] | Critical if no spec sheet on file (PRD-18 BLOCKED: 22 of 22 have none) |
| 11 Paperwork (care card included; packing slip matches order) | [FILL] | [FILL]% | [FILL] | |

## 5. Defects by SKU (FILL) + root-cause review (agent, no assumed defects)
| # | SKU (visible list) | Units inspected | Fails | Defect rate for the SKU | Grade(s) | Check #(s) | Action (rework / scrap / shipped) | Re-inspection date |
|---|---|---|---|---|---|---|---|---|
| [FILL row per inspected SKU; include every SKU that passed through inspection this week, including 1-unit stock] | | | | | | | | |

Agent review of the risk surface (not a defect log; from existing files only):
- Fibre labels: 22 of 22 visible SKUs have no spec sheet on file (`label-check-2026-10-21.md`); a missing composition label is
  Critical (do not ship) once the adviser confirms the wording (PRD-19, PRD-18 BLOCKED). This is the single biggest
  preventable defect class until supplier evidence arrives.
- Measurements: no tolerance set yet (A-PRD-19 +/-2 cm planning; PRD-13 BLOCKED). Risk: units held for rework that would
  pass under a looser tolerance, or shipped under a tighter one.
- Colour / shade photos: 24 colour variants have no real photo (beanie 10, turtleneck 11, hat set 2, cardigan Blue 1); shade
  mismatch (check 7) cannot be validated visually on those.
- Buttons / trim on button cardigans (P1): pull test (check 9) before packing.
- Blocking / drying creases (check 6): 24-48 h flat dry per batch (A-PRD-05).

## 6. qc-log.csv schema (created only after owner approves PRD-13; the agent never creates it on its own)
```
date,order_no,sku,size,colour,check_no,grade,description,action(rework/scrap/shipped),minutes_lost
```
- `date`: ISO YYYY-MM-DD (local Riga).
- `order_no`: Squarespace order #, Etsy order id, or "STOCK" for a unit inspected ahead of sale (e.g. stall stock).
- `grade`: Critical / Major / Minor (PRD-12).
- `action`: rework / scrap / shipped.
- `minutes_lost`: effective minutes (A-PRD-01 EUR 0.20/min) spent on the rework.
- Rule: one row per failing unit and per failing check; a unit failing 2 checks has 2 rows. Partial pass after rework is logged
  twice (fail, then pass) so the first-fail count is not lost.
- Defect rate (PRD-23) counts **units failing first inspection / units inspected**; the rework count does not reduce it.

Care label default on the paperwork line (check 11 / QC): "hand wash cold or wool cycle, dry flat, no tumble dry" in ISO 3758
symbols only, per supplier care advice; never "machine washable" without supplier proof (`qc-checklist.md` section 4).

## 7. Defect prevention / blocker notes this week (FILL + agent)
- Open QC items carried from the monthly review (whatever applies this week): [FILL]
- Change to AMBER in the capacity file (repeated defect, 2 in 4 weeks): [FILL SKU list or none]
- Tolerance in use: [FILL: owner sets; planning value +/-2 cm, A-PRD-19]  (PRD-13 BLOCKED until owner sets it)
- Units held because no spec sheet exists for the yarn: [FILL] (PRD-18 BLOCKED; composition label = Critical once confirmed)
- Supplier/evidence needed before a GREEN label can be lifted: [FILL]

## 8. Weekly capacity impact (FILL)
Minutes lost to rework: [FILL] (reserve 169 min/week; A-PRD-17)
Effect on this week's plan: [FILL: e.g. 1 unit reworked = +N min lost, promo buffer cut by N; no paid impact this week]
Crossed 85% maker load because of rework? [yes/no -> mid-week re-issue]

## 9. Inputs still owed (do not advance these from this file)
- PRD-13: creation of `qc-log.csv` + tolerance set (owner).
- PRD-06: timed units (so minutes lost are real rather than assumed).
- PRD-18: supplier spec sheets (22 SKUs, priority 5 by 31 Oct).
- PRD-19: adviser answer on label wording/languages (adviser pack sent 3 Nov).
- PRD-11: physical stock count (so defect units can be mapped to real SKUs).

## 10. Assumed values cited
A-PRD-17 (first-QC pass >=95% planning baseline), A-PRD-19 (tolerance +/-2 cm planning), A-PRD-05 (drying 6 garments /
24-48 h), A-PRD-15 (whole-garment quantities per dye lot), A-PRD-10 (trims EUR 0.80 / buttons +2.40), A-PRD-01 (labour
EUR 12/h = EUR 0.20/min). CM2 of rework is charged against the same Finance file as the capacity file.

DRAFT. Assumptions, not facts. Nothing applied. Nothing sent.
