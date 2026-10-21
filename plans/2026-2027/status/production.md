# Product & Production — status 2026-10-21
Summary: 0 done · 21 blocked · 12 todo
| ID | Task | Due | Status | Output / blocker |
|---|---|---|---|---|
| PRD-01 | Owner approves production plan, Friday capacity cadence, KPI targets (proposal values) | 2026-10-24 | BLOCKED | Owner (master decision 1) |
| PRD-02 | First weekly capacity + safe-to-promote list, `capacity-2026-W43.md` (all 22 visible SKUs AMBER at best: 0 costed, 0 stock-confirmed; no-photo colours RED) | 2026-10-23 | BLOCKED | Drafted, but the write to `business-os/production/` was refused by the `prod-guard` hook (pattern `**/production/**`). User must allow that path or name another folder |
| PRD-03 | Owner question list W43 (5 max: team/hours, physical count, timing, yarn stock + suppliers, labour rate) | 2026-10-23 | BLOCKED | Part of PRD-02 file; same `prod-guard` write block |
| PRD-04 | Lead-time wording proposal for made-to-order (production input to owner decision 3) | 2026-10-24 | BLOCKED | Part of PRD-02 file; same `prod-guard` write block. Final wording = owner |
| PRD-05 | Timing sheet (minutes per step, 3 units, median) + yarn-grams sheet for 8 priority SKUs | 2026-10-25 | BLOCKED | `prod-guard` write block on `business-os/production/` |
| PRD-06 | Owner times 3 units each of priority SKUs (beanie, hat set, 1 sweater, 1 cardigan, 1 vest first) and weighs yarn | 2026-10-25 (8 SKUs by 31 Oct) | BLOCKED | Owner (G0, master decision 5); GM/owner provisional 5 priority SKUs (decision 2, 24 Oct) |
| PRD-07 | Owner production facts: people + hours/day, labour rate, yarn on hand by colour/lot, suppliers, lead times, MOQs | 2026-10-28 | BLOCKED | Owner (G0, master decision 5) |
| PRD-08 | Per-SKU cost sheet template + 22-SKU cost-collection list (net price and 40% CM1 benchmark ceiling per SKU) | 2026-10-30 | BLOCKED | `prod-guard` write block on `business-os/production/` |
| PRD-09 | `sku-cost-proposals-2026-10-30.md`, first 8 SKUs (materials + labour) | 2026-10-30 | BLOCKED | Needs PRD-06 + PRD-07 from owner; output path also under `prod-guard` |
| PRD-10 | Stock-truth + dedupe sheet for 22 visible SKUs (listed stock, physical count, MTO flag, duplicate groups) | 2026-10-31 | BLOCKED | `prod-guard` write block on `business-os/production/` |
| PRD-11 | Owner confirms physical stock, made-to-order lead time, and the source of truth per duplicate listing | 2026-10-31 (5 priority 24 Oct) | BLOCKED | Owner (master decisions 4, 20) |
| PRD-12 | QC checklist: 11 checks, critical/major/minor grades, 100% inspection, `qc-log` template | 2026-10-31 | BLOCKED | `prod-guard` write block on `business-os/production/` |
| PRD-13 | Create `qc-log.csv` and set the measurement tolerance | 2026-10-31 | BLOCKED | Owner (master decision 20) |
| PRD-14 | Yarn reorder template + reorder-point method (ROP = weekly use x lead time + 2 weeks safety; whole-garment qty per dye lot) | 2026-11-16 | BLOCKED | `prod-guard` write block on `business-os/production/` |
| PRD-15 | Cost proposals for all 22 visible SKUs (owner confirms 11 Nov per ruling C4) | 2026-11-06 | BLOCKED | Needs PRD-06/07 for all SKUs; owner |
| PRD-16 | Market-stall production input (what can be made for stalls without starving online) | 2026-11-10 | BLOCKED | Owner market decision (master decision 27) + PRD-06/07 |
| PRD-17 | Label-check file, 22 visible SKUs (claims vs evidence: "Merino"/"Lambswool" not Annex I names, "Pure"/"100%"/"pure new wool" need single-fibre/virgin evidence, V07 page shows both "100% lambswool" and "100% wool"; adviser to confirm) | 2026-11-13 | BLOCKED | `prod-guard` write block on `business-os/production/`; evidence column also needs PRD-18 |
| PRD-18 | Supplier spec sheets / invoices per yarn (fibre evidence) for 22 visible SKUs | 2026-11-30 | BLOCKED | Owner (master decision 34); no spec sheet on file |
| PRD-19 | Label wording and label languages via EU consumer-law adviser | 2026-11-20 | BLOCKED | Owner sends adviser questions 3 Nov (master decision 22); adviser to confirm |
| PRD-20 | December yarn reorder proposals (owner buys) | 2026-11-16 | BLOCKED | Owner yarn stock + lead times (PRD-07); FIN cash check (G3); owner purchase decision 32 |
| PRD-21 | Production lead time per SKU for the Christmas order-by table | 2026-11-20 | BLOCKED | OPS carrier-backed dates (14 Nov) + PRD-06 timing |
| PRD-22 | Weekly capacity file W44-W52, every Friday 23 Oct - 25 Dec, mid-week re-issue on RED | Weekly Fri | TODO | First due Fri 23 Oct; needs the `prod-guard` path issue fixed |
| PRD-23 | Weekly `qc-summary-YYYY-Www.md` (defect rate = first-QC fails / inspected) | Weekly Fri from first inspected unit | TODO | Starts once units are inspected (0 orders to date) |
| PRD-24 | Stall-stock ring-fence line in the capacity file (not promotable online) | 2026-11-27 | TODO | Only if owner takes a stall (PRD-16) |
| PRD-25 | Stop made-to-order for gift delivery at the earliest regional cutoff (ruling C3: about 3 Dec EU, replaces plan's 11 Dec) | ~2026-12-03 | TODO | Date fixed by OPS table (PRD-21) |
| PRD-26 | `production-review-2026-10.md` (sell-through, defects, supplier notes) | 2026-11-05 | TODO | Future |
| PRD-27 | `production-review-2026-11.md` | 2026-12-05 | TODO | Future |
| PRD-28 | Q4 review: sell-through, defect rate, yarn left, what sold (feeds 2027 range) | 2026-12-28 | TODO | Future |
| PRD-29 | `production-review-2026-12.md` | 2026-12-31 | TODO | Future |
| PRD-30 | Q1 2027: confirmed cost + gross margin for 22 SKUs, live reorder points, range cull to core 10-12 (proposal), label evidence closed, crochet-glove decision | 2027-03-31 | TODO | Targets reset 15 Jan 2027 from Q4 actuals |
| PRD-31 | Q2 2027: spring drop of 2-4 lightweight pieces (gated), supplier review, bottleneck fix, quarterly label re-check | 2027-06-30 | TODO | Future |
| PRD-32 | Q3 2027: AW range locked 31 Jul, yarn pre-buy (owner, FIN cash check), pre-built stock, Production/Fulfilment hire trigger check | 2027-09-30 | TODO | Future |
| PRD-33 | Q4 2027: Christmas production calendar by 1 Oct, peak execution, gift-line focus, annual review | 2027-12-31 | TODO | Future |

## Blocked on owner

- Tooling: the `prod-guard` hook refuses every write under `business-os/production/` because it matches `**/production/**`. That blocks PRD-02, 03, 04, 05, 08, 10, 12, 14 and 17, all of which are drafted and ready to write. The user should allow the path or choose another folder. I did not work around the hook.
- Approve the production plan, Friday cadence and KPI targets (24 Oct).
- Provisional 5 priority SKUs (with GM, 24 Oct), so the timing study knows what to time.
- Time 3 units per priority SKU and weigh yarn per garment (25 Oct; 8 SKUs by 31 Oct).
- People + hours/day, labour rate, yarn on hand by colour/dye lot, supplier names, prices, lead times, MOQs (28 Oct).
- Physical stock count for the 22 visible SKUs, the made-to-order list, and the made-to-order lead time (turtleneck 360 and beanie 220 look like placeholders; repeated 16/12 values too) (31 Oct; 5 priority by 24 Oct).
- Dedupe: which listing is the source of truth for the lambswool crew, side-slit, beige vest and stand-collar listings, or confirm they are separate colours (31 Oct).
- Public dispatch promise and made-to-order lead time wording (24 Oct).
- Agree to create `qc-log.csv` and set the measurement tolerance (31 Oct).
- Market stall yes/no and how much stock to ring-fence (10 Nov).
- Yarn purchases for December (16 Nov; I propose quantities only).
- Supplier spec sheets for each yarn before any "100% / pure / pure new wool / merino" wording is kept (30 Nov).
- Send label wording and language questions to the EU adviser (3 Nov; adviser to confirm).
- Which existing product photos are real, not generated ("ChatGPT Image" assets), since a real photo per promoted colour is required for GREEN.
