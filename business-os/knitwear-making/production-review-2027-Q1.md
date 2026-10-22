# Production review — Q1 2027 (PRD-30)   Status: DRAFT skeleton for owner approval (AGENT-DOABLE; close by 31 Mar 2027)

aw-production, drafted 2026-10-22. Covers Q1 baseline: confirmed cost + gross margin for 22 SKUs, live reorder points,
range cull to a proposed core 10-12, closed label evidence, and the crochet-glove decision. **No data yet; all values are
ASSUMPTION / FILL / TODO and are reset after 15 Jan 2027 from Q4 actuals** (`plans/2026-2027/production.md`). Nothing
written to `sku-economics.csv`, stock, product data or any shared CSV.

## 1. One line (fill when Q1 closes)

`Q1 2027: cost/margin confirmed on <FILL> of 22 SKUs in `sku-economics.csv`, first reorder point breached <FILL> times on
promoted SKUs, defect rate <FILL> %, range cull proposal delivered (core <FILL> SKUs), fibre-label evidence closed on
<FILL> of 22. `

## 2. Period, sources and reset
- Period: 2027-01-01 to 2027-03-31; close date 31 Mar 2027. (Targets reset 15 Jan 2027 from Q4 actuals.)
- Sources: Q4 roll-up (`production-review-2026-Q4.md`), monthly reviews, all capacity files W43-... (carried into 2027),
  qc logs (once PRD-13 closes), timed minutes and yarn weight (PRD-06), production facts (PRD-07), spec sheets (PRD-18),
  adviser answers (PRD-19), Finance CM2 file.
- Values that may change on 15 Jan 2027: all targets, yarn reorder point parameters, hero SKU list, spring drop scope.

## 3. Confirmed costs and gross margin (22 SKUs)
- Cost sheet (`cost-sheet-template.md`) filled for each of the 22 visible SKUs with confirmed M+L; the assumptions values
  (A-PRD-20/21) are replaced by owner-timed figures where available, else remain ASSUMPTION with an open TODO.
- Columns confirmed: materials by yarn class (merino 60 EUR/kg, lambswool 50, wool 40 ASSUMED, A-PRD-06/07/08), trims
  (A-PRD-10), labour (EUR 0.20/min, A-PRD-01), waste (8%, A-PRD-09), packaging/shipping/payment per Finance file.
- `sku-economics.csv`: no write here. First write happens only after owner confirmation and GM/Finance review of the cost
  proposal (ruling: production drafts, owner confirms before any CSV write, HARD RULE 1).
- SKUs below the first margin floor (owner sets on 15 Jan 2027): FILL list.
- Crochet glove (hidden) cost position if it is ever unhidden: FILL.

## 4. Live reorder points
- ROP = avg weekly use x lead time + 2 weeks safety stock (A-PRD-15); move to z-score once >= 8 weeks of data exist (~March).
- ROP table per colour/lot: FILL owner data; target zero yarn stockouts on GREEN SKUs.
- Reorder events triggered this quarter: FILL (SKU, colour, date, qty, owner-buy).
- Stockouts avoided (if any) recorded here: FILL.
- `yarn-reorder-template.md` updated with real numbers (December assumed scenario replaced).

## 5. Range cull to a core 10-12 (proposal only, product data frozen)
- Method (proposal): ABC by contribution x sell-through (matches `plans/2026-2027/production.md`, Q1 initiative 3).
- Keep list (proposed): FILL SKUs + rationale (contribution, photos, colour evidence).
- Cull / merge candidates (proposal): FILL SKUs + rationale (duplicate pools, thin margin, no photo, 1-2 unit stock).
- Crochet glove decision (owner, decision 12): revive (needs cost/minutes/yarn) or stay hidden; FILL.
- No SKU deleted without owner; product data remains frozen except for an explicit scoped unfreeze.

## 6. Label evidence closed
- Spec sheet progress from 28 Dec: FILL count (target 22 of 22 by 30 Nov 2026; carry-over into Q1).
- Adviser answers received and changes applied: FILL.
- SKUs with revised sewn labels ( Annex I fibre names, %, languages): FILL.
- Beanie composition gap closed (currently shows none in the export): FILL.
- Language set per garment (Latvian vs more) confirmed by the adviser: FILL.

## 7. Defect rate and QC
- Defect rate <= 5% (proposal) carried into Q1; target after Q4 data: FILL.
- `qc-log.csv` created (once PRD-13 closes) and month-over-month comparison: FILL.
- Repeated defects resolved and SKUs lifted from AMBER: FILL.
- Tolerance set by the owner (A-PRD-19 +/-2 cm planning) or other: FILL.

## 8. Capacity and one-person bottleneck
- Load on the maker step averaged FILL %; threshold 85%.
- Bottleneck analysis (knit / finish / drying) with one proposed fix and cost TODO.
- Holiday/absence subtraction for Q1 planning: FILL (summer style calendar).
- Hire decision triggered by data? FILL.

## 9. What is done / what stays TODO
- Done items (confirmed numbers only): FILL list.
- Items still TODO and why (data, budget, owner): FILL list.
- Decisions owed by owner on 15 Jan 2027 (decision 12): FILL.

## 10. Inputs owed at quarter close (FILL / do not advance)
All items from PRD-30 (confirmed cost + gross margin for 22 SKUs, live reorder points, range cull proposal, label evidence
closed, crochet-glove decision), plus the measured Q4 actuals as baseline.

## 11. Assumed values cited
A-PRD-01..23 (and their quarter rules from production.md s3); A-OPS-02..10; A-FIN-01/02/03; A-GM-20/21/22;
A-CRO-01/07. CM2 single source: Finance file. DRAFT, nothing applied.
DRAFT. Assumptions, not facts. Nothing applied. Nothing sent.
