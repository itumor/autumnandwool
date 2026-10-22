# Production review — November 2026 (PRD-27)   Status: DRAFT skeleton for owner approval (AGENT-DOABLE; close by 05 Dec 2026)

aw-production, drafted 2026-10-22. **No measured result is included anywhere below.** Every figure is one of:
- **ASSUMPTION** — value in `assumptions-wave3.md` (cite the A-ID) or in the W43-W48 capacity files;
- **FILL** — an owner log, order export, supplier fact, or weekly capacity/qc file must supply it;
- **TODO / N/A** — not yet applicable or not available.

Nothing was written to `sku-economics.csv`, stock, product data or any shared CSV (HARD RULES 1–3). Fibre
content, certifications, "hand-knitted" and similar claims are never assumed (PRD-18 BLOCKED).

## 1. One line (fill when November closes)

`November 2026: <FILL orders shipped> shipped of <FILL units available, assumed>, sell-through <FILL> %, first-QC
failures <FILL> of <FILL> inspected, Christmas MTO stops executed on EU 19/26 Nov and Baltic 3-4/10-11 Dec,
maker load [FILL]% against the 1,125 min/week assumed baseline (A-PRD-04).`

## 2. Scope, sources and gaps
- Period: 2026-11-01 to 2026-11-30 (close by 05 Dec).
- Sources available to fill: capacity files W44-W48 (PRD-22), qc summaries W44-W48 (PRD-23), `stock-duplicate-sheet.md`,
  `sku-cost-proposals-2026-10-21.md`, Finance CM2 file, `christmas-orderby-production-table-2026.md`,
  `lead-time-wording-proposal.md`, W43 file.
- Sources not available: order exports, `qc-log.csv` unless PRD-13 closes, timed minutes (PRD-06), people/hours/labour rate
  /yarn (PRD-07), physical stock count (PRD-11), supplier spec sheets (PRD-18), adviser answers (PRD-19), OPS carrier
  dates unless the 14 Nov publication lands before closeout. Re-run December if late data arrives.
- Assumed baseline (do not quote as facts): A-PRD-01..23, A-PRD-22 Christmas cutoffs (assumed), A-OPS/A-FIN as
  consolidated in Finance's file.

## 3. Capacity and output in November (planning vs actual)
### 3.1 Assumed baseline
Same as October: 1 person x 25 h x 0.75 = 1,125 effective min/week (A-PRD-02/03/04); drying 6 garments/24-48 h (A-PRD-05).

### 3.2 Weekly actuals to fill (FILL)
| Week | File | WIP finished (units) | Orders dispatched | Minutes actually used | Load % (maker) | RAG | Notes (absences, stall days, MTO stops) |
|---|---|---|---|---|---|---|---|
| W44 (26 Oct - 1 Nov) | capacity-2026-W44.md | FILL | FILL | FILL | FILL (plan 71%) | FILL | holiday W44 |
| W45 (2-8 Nov) | capacity-2026-W45.md | FILL | FILL | FILL | FILL | FILL | lateness/cutoff prep |
| W46 (9-15 Nov) | capacity-2026-W46.md | FILL | FILL | FILL | FILL | FILL | PDP order-by line deadline 9 Nov (owner applies, CRO A-CRO-07) |
| W47 (16-22 Nov) | capacity-2026-W47.md | FILL | FILL | FILL | FILL | FILL | EU garments MTO stop 19 Nov; accessories 26 Nov |
| W48 (23-29 Nov) | capacity-2026-W48.md | FILL | FILL | FILL | FILL | FILL | Baltic garment stop LV 4 Dec / EE-LT 3 Dec; stall prep if owner proceeds |
| W49 (30 Nov - 6 Dec) | capacity-2026-W49.md (part; belongs to Dec review) | FILL | FILL | FILL | FILL | FILL | carry-forward into the December review |

- Christmas transition: from 19 Nov the promo buffer is Baltic-only (per `christmas-orderby-production-table-2026.md`).
- Re-issue mid-week if a maker load crosses 85%.

### 3.3 November capacity notes (agent, not measured)
- Weekly capacity files W44-W48 must be closed before this review is signed off (PRD-22).
- Market decision deadline 10 Nov (Doma laukums / Kalnciema / Baltic EXPO); production input = what can be made for stalls without
  starving online/Christmas orders (PRD-16). If a stall is taken, ring-fenced stock per PRD-24 sits in the capacity file and is not
  promotable online.
- On-time dispatch vs promised days: FILL n/N; target >=95% assumed.

## 4. Sell-through in November (FILL from order exports)
### 4.1 Monthly totals
| Metric | Value (FILL) | Target / note |
|---|---|---|
| Orders (site) | FILL | exclude test orders |
| Orders (Etsy) | FILL | status of the shared pool (decision 9) |
| Orders (market) | FILL | 0 if no stall |
| Units sold, total | FILL | |
| Sell-through, all visible SKUs combined | FILL % | denominator = available units (assumed pools) |
| On-time dispatch vs promised days | FILL n/N | >=95% proposal |
| Gift orders (gift note perk) | FILL | lowers CM2 by EUR 0.90 each (A-FIN-05, FIN-19) |
| Returns/refunds opened | FILL | Ops owns detail |

### 4.2 Sell-through by SKU (assumed available pools; sold = FILL)
Use the same 22-row table structure as the October review section 4.2, carry forward produced-in-month and end-of-month stock as FILL
from W44-W48 files. Pools (lambswool raglan crew, side-slit, beige vest, stand-collar) counted once (A-PRD-13). Do not add extra rows
or duplicate-listing double counts. Flag any SKU that sold out mid-month and had restock.

### 4.3 What sold and what did not (FILL)
- Top 3 SKUs by units sold (FILL SKU + units + channel): ______
- Gift-line entries that sold (beanie / hat & scarf set) vs capacity consumed: ______
- SKUs at stock 1-2 that sold out (FILL SKU + date + restock decision): ______
- Stock that arrived too late to ship before Christmas (if any): ______

### 4.4 Channel notes
- Site (Squarespace), Etsy, Google free listings, creator gifting (plan #11), paid (none unless owner-confirmed cost + stock): FILL.

## 5. Defects (FILL unless PRD-13 stays BLOCKED)
### 5.1 November QC totals (FILL)
| Metric | Value | Note |
|---|---|---|
| Units inspected | FILL | 100% of shipped |
| Units failing first inspection | FILL | |
| Defect rate | FILL % | proposal <=5% (A-PRD-17) |
| Units reworked and shipped | FILL | |
| Units scrapped | FILL | |
| Minutes lost to rework | FILL | vs 169 min/week reserve |
| Repeated defect -> SKU on AMBER | FILL or none | |

### 5.2 Defects by grade and check
Use the PRD-23 template structure (grades Critical/Major/Minor, checks 1-11, qc-checklist.md). Fill from qc-log.csv if it exists,
otherwise from weekly qc summaries and manual notes (and flag this as a data caveat).

### 5.3 Labels (defect prevention, PRD-18/19 still BLOCKED)
- No spec sheet on file for any of the 22 visible SKUs; composition label remains Critical until the adviser confirms wording
  (qc-checklist.md check 10). Any shipped stock labelled anyway must be recorded here as a variance for the adviser.
- Fibre claims on the pages are frozen unless the owner + adviser agree (choice lock on claims).

## 6. Gross margin by SKU (assumed; do not copy into sku-economics.csv)
Reuse the structure of the October review section 6, with the per-zone Finance CM2 unchanged. Actual November values need: real channel mix
by order, returns, and the actual shipping/packaging per parcel (FILL or carry forward planned externalities A-OPS-02..10, A-FIN-01/02/03).
- Gift-order effect at EUR 0.90 per gift order (A-FIN-05): FILL orders * EUR 0.90.
- Closure of any SKU below the EUR 10 minimum contribution (A-GM-20) in any zone: FILL SKU/zone list.

## 7. Yarn, reorder and material position
- ROP = avg weekly use x lead time + 2 weeks safety stock (A-PRD-15); with Nov on schedule, December yarn reorder proposals are due 16 Nov
  (PRD-20) and the owner buys (decision 32, after a finance cash check). Proposal quantity: 3 hat sets + 10 beanies + 1 Dusty Pink per week,
  ~18.3 kg merino-class, ROP 12.2 kg, ceiling ~EUR 1,100 minus yarn on hand (unknown) (ASSUMPTION, `yarn-reorder-template.md` s3).
- Yarn below ROP with no open proposal: FILL count (target 0 from 16 Nov).
- Supplier prices (merino EUR 60/kg, A-PRD-06; lambswool EUR 50/kg, A-PRD-07; wool EUR 40/kg, A-PRD-08; waste 8%, A-PRD-09;
  trims A-PRD-10) still assumed; supplier invoices needed to close PRD-07/PRD-20.
- Spec sheet progress (PRD-18): priority 5 by 31 Oct, rest by 30 Nov -> FILL count at month end.

## 8. Supplier notes (draft only; no suppliers contacted)
Reuse the October section 8 structure. Add November deltas:
- adviser pack sent 3 Nov to the EU consumer-law adviser (PRD-19); report any answers that change label wording or languages.
- Package supplier/label quote progress: FILL.
- Packaging (OPS A-OPS-10 EUR 1.50/order) and carrier rates (A-OPS-02..08) confirmed or still assumed: FILL.
- Light-touch supplier review pre-work for 2027 Q2 (cost vs MOQ vs lead time) may start now by gathering the facts only (owner never the agent contacts suppliers).

## 9. Stock truth and risks
- Assumed physical stock of the 22 visible SKUs (72 units, 580 assumed placeholders, 4 duplicate pools) stands until PRD-11.
- Cardigan Brown/Blue: promised MTO 10 wd (A-PRD-23); reassess only after the 24 Oct physical count decision.
- Beanie 220 / turtleneck 360 treated as placeholders (MTO) until counted; Merchant Center still hard-codes `in_stock`.
- Market stock, if any, is ring-fenced and not promotable online (PRD-24).
- December sell-through of a pre-built stock position on the safest SKUs: FILL units held for gift peak.

## 10. Weekly capacity file roll-up (November closeout)
| File | Period | Status |
|---|---|---|
| `capacity-2026-W43.md` | 21-25 Oct issues | DRAFT assumed, Sept-Oct baseline |
| `capacity-2026-W44.md` ... `W48.md` | Nov | FILL status closeout |
| (cross-month) W49-W52 | late Nov-Dec | belong to the December review, list them here as issued |

## 11. Blockers referenced, not advanced (PRD-01, 06, 07, 11, 13, 18, 19)
Take over the blocker list from the October review section 11 and add November progress only (FILL). Nothing is marked complete
unless owner evidence exists. Add any PRD-21/22/23/24/25 follow-ups resolved on either page.

## 12. Decisions and questions for the owner (max 5, merged into the Monday/Thursday batch, ruling C11)
1. FILL (must be about data, not priority lists)
2. FILL
3. FILL
4. FILL
5. FILL

## 13. TODO / missing data
Carry over and extend the October list: all measured November numbers; capacity files; qc logs; stock counts; timed units;
yarn count; spec sheets; carrier dates; paid spend approval (decision 28a). Late-arriving data (Etsy) added until 05 Dec.

## 14. Assumed values cited
A-PRD-01..23 incl A-PRD-22 (Christmas cutoffs, assumed) and A-PRD-23 (cardigan MTO); A-OPS-02..08/10; A-FIN-01/02/03;
A-GM-20/21/22, A-CRO-01/07. CM2 and zone values from Finance's file. DRAFT for owner, assumptions not facts.
Nothing applied, nothing sent.
DRAFT. Assumptions, not facts. Nothing applied. Nothing sent.
