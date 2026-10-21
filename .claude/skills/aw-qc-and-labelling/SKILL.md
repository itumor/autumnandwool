---
name: aw-qc-and-labelling
description: Use when checking an Autumn & Wool garment before dispatch, writing or updating the QC checklist, logging defects, or checking EU textile fibre-composition and care labels (Regulation (EU) 1007/2011) on garments or product pages, including whether "100%", "pure wool", "merino" or "virgin wool" wording is allowed.
---

# Garment QC and EU fibre-composition labelling

Purpose: every garment that leaves the studio matches its product page, is free of defects, and carries a
compliant fibre-composition label. Output = a QC checklist, a defect log, and a label-compliance list.
Not legal advice: anything unclear goes to the EU consumer-law adviser (README s.11).

## 1. Per-garment QC checklist (final inspection, every unit, before packing)

Handmade volume is small, so inspect 100% of units, not an AQL sample. Record pass/fail per line.

| # | Check | Pass rule |
|---|---|---|
| 1 | Right item | SKU, colour, size match the order and the product page photo |
| 2 | Measurements | Chest/width, length, sleeve (shoulder-to-cuff or raglan), hem width vs size guide; tolerance TODO (owner sets, e.g. +/-1-2 cm) |
| 3 | Symmetry | Sleeves equal length, side seams straight, hem level, neckline centred |
| 4 | Knit surface | No dropped/laddered stitches, holes, tight/loose rows, stripe misalignment |
| 5 | Linking / seams | Seams closed, no gaps or puckering, yarn ends woven in and trimmed |
| 6 | Finish | Washed/blocked to shape, no creases from drying, no lint, no stains, no odour |
| 7 | Shade | Same dye lot across body and sleeves; compare under daylight |
| 8 | Hand-feel / pilling | No visible pilling or fuzz balls on new garment |
| 9 | Trims | Buttons secure (pull test), buttonholes finished, no loose threads |
| 10 | Labels | Fibre-composition label sewn in, correct for this yarn (section 2); care label present (section 3) |
| 11 | Paperwork | Care card included; order slip matches |

Defect grading: **Critical** (wrong item, hole, missing/wrong composition label) = do not ship. **Major**
(visible flaw a customer would return for: measurement out of tolerance, shade mismatch, dropped stitch) = rework
or do not ship. **Minor** (fixable on the spot: loose end, lint) = fix, then pass.

Defect log row (`business-os/qc-log.csv`, propose; create only if the owner agrees):
`date,order_no,sku,size,colour,check_no,grade,description,action(rework/scrap/shipped),minutes_lost`
Weekly: defect rate = units failing first inspection / units inspected. Repeated defect on a SKU = flag to
aw-production-capacity (SKU goes AMBER until fixed).

## 2. Fibre-composition label rules (Regulation (EU) 1007/2011, summary)

- Applies to products with >= 80% textile fibres by weight sold to consumers in the EU. Label must be durable,
  legible, visible and firmly attached (sewn in).
- List every fibre by its official Annex I name (e.g. "wool"; "merino" is not an Annex I name, see below)
  with weight percentage, in decreasing order.
- **"100%", "pure", "all"** only if the product is made of one fibre only. Up to 2% unavoidable foreign fibres
  tolerated (5% for carded products) if not added systematically.
- **"Virgin wool" / "fleece wool"** only for wool never previously incorporated in a finished product and not
  previously processed beyond spinning/felting; extraneous fibres max 0.3%; in blends wool must be >= 25%.
- Fibres up to 5% each (15% together) may be grouped as "other fibres" only if hard to state at manufacture.
- Manufacturing tolerance between stated and tested percentages: 3%.
- Composition text: uniform font/size/style, separate from other info (care, brand). Trade names may sit next
  to it.
- Language: official language(s) of each EU country where sold to consumers (Your Europe). For Latvia = Latvian.
  Selling to other EU states raises a translation question: flag to adviser (TODO decide label languages).
- **Online:** composition must be clearly visible to the consumer before purchase, including e-commerce (Art. 16).
  So each product page must state composition matching the sewn label.
- "Merino", "lambswool" are descriptive; the composition line itself must use the Annex I name ("wool"), e.g.
  "100% wool" with "merino wool" elsewhere in the description. Exact compliant wording = adviser check (TODO).

Label-compliance check output (`business-os/label-check-YYYY-MM-DD.md`):
```
| SKU | Yarn supplier + spec sheet (evidence) | Composition on sewn label | Composition on product page | Uses 100%/pure/virgin? Allowed? | Languages | Issue | Action (owner) |
```
Evidence rule: composition comes from the yarn supplier spec/invoice, never from the current product title.
Several titles say "100% Wool", "Pure Wool", "Merino": each needs supplier evidence; no evidence = issue.

## 3. Care labels

EU law does not make care labelling mandatory (Latvian rules: adviser to confirm), but the care info must be
separate from composition. Use ISO 3758/GINETEX symbols only per supplier care advice. Wool default (verify per
yarn): hand wash cold or wool cycle, dry flat, no tumble dry. Never claim "machine washable" without supplier
proof.

## Guardrails

- Never state or change a fibre percentage without supplier documentation. Never edit product pages (frozen);
  propose corrections to the owner.
- Never ship a Critical defect. Never decide legal compliance: write "likely issue, adviser to confirm".
- No sustainability/organic/certification wording without certificates (see aw-brand-voice).

## Sources

- Your Europe, "Textile labelling" https://europa.eu/youreurope/business/product-requirements/labels-markings/textile-label/index_en.htm
  — EU site; page shows no licence (Commission reuse policy Decision 2011/833/EU normally allows reuse with
  attribution, unverified for this page); summarized: scope, 100%/pure,
  order, language, separation from care info.
- Regulation (EU) No 1007/2011, Arts. 7, 8, 9, 14, 16, 20 — text read via legislation.gov.uk copy
  https://www.legislation.gov.uk/eur/2011/1007/data.htm?view=plain (Open Government Licence); EU original
  https://eur-lex.europa.eu/eli/reg/2011/1007/oj/eng . Own-words summary. Note: UK copy's language article is
  UK-modified; EU language rule taken from Your Europe.
- Garment inspection practice (key dimensions, seam checks, critical/major/minor grading, shade under daylight,
  AQL 2.5 for bulk): racklify seam-inspection guide https://racklify.com/encyclopedia/seam-inspection-checklist-how-to-inspect-garment-seams-step-by-step/
  and Kanchan Cashmere QA page https://kanchancashmere.com/pages/kci-quality-assurance — all rights reserved;
  ideas only. Winner: own checklist, because sources are mass-production/AQL oriented and A&W inspects every unit.
