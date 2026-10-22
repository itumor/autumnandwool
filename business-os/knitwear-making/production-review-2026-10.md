# Production review — October 2026 (PRD-26)   Status: DRAFT for owner approval (AGENT-DOABLE skeleton; close by 05 Nov 2026)

aw-production, drafted 2026-10-22. Agent-only draft of the monthly production review PRD-26 (due 2026-11-05). Covers
October 2026 (week 1 Oct – week 31 Oct), with the only available in-month operating baseline running from the baseline
week 2026-10-19 (ruling C16) and the first capacity file issued Wed 21 Oct (W43). **No measured result is included
anywhere below.** Every figure is one of:
- **ASSUMPTION** — a value already registered in `business-os/knitwear-making/assumptions-wave3.md` (cite the A-ID) or in
  the department registers, used as a placeholder so the structure can be read;
- **FILL** — a thing an owner or Q4 log must supply (order exports, measurements, supplier facts, yarn count);
- **TODO / N/A** — not yet applicable or not available.

Nothing was written to `sku-economics.csv`, stock, product data or any shared CSV (HARD RULES 1–3). Fibre
content, certifications, "hand-knitted" and similar claims are never assumed (A-PRD-18, PRD-18 BLOCKED).

This draft does **not** advance any owner-blocked task. PRD-01, PRD-06, PRD-07, PRD-11, PRD-13, PRD-18 and PRD-19 stay
BLOCKED and are referenced only as inputs that are still owed.

## 1. One line (fill when October closes)

`October 2026: <fill orders shipped> shipped of <fill units available assumed>, sell-through <fill> %, first-QC failures
<fill> of <fill> inspected, W43-W44 bottleneck load <fill> % vs the 1,125 min/week assumed baseline (A-PRD-04).`

## 2. Scope, sources and how to read this file

- Period: 2026-10-01 to 2026-10-31 (review due 05 Nov; late-arriving data may be added until then).
- Sources used: `business-os/knitwear-making/capacity-2026-W43.md`; `sku-cost-proposals-2026-10-21.md`;
  `stock-duplicate-sheet.md`; `label-check-2026-10-21.md`; `qc-checklist.md`; `timing-sheet.md`; `cost-sheet-template.md`;
  `yarn-reorder-template.md`; `lead-time-wording-proposal.md`; `assumptions-wave3.md`;
  `business-os/finance/sku-margins-assumed-wave3.md` (single source for CM2); `plans/2026-2027/production.md` and
  `plans/2026-2027/status/production.md`.
- Sources **not** available: order exports (Squarespace/Etsy; Etsy shared pool status unknown), physical stock count
  (PRD-11 BLOCKED), timed minutes / yarn grams (PRD-06 BLOCKED), people + hours + labour rate + yarn on hand + supplier
  prices + lead times + MOQs (PRD-07 BLOCKED), `qc-log.csv` (PRD-13 BLOCKED), supplier spec sheets (PRD-18 BLOCKED),
  adviser answers on label wording/languages (PRD-19 BLOCKED).
- Assumed baselines relied on (do not quote as facts): A-PRD-01 EUR 12/h, A-PRD-02 efficiency 0.75, A-PRD-03 1 person x
  25 h/week, A-PRD-04 1,125 effective min/week, A-PRD-05 drying 6 garments / 24-48 h, A-PRD-12 stock rule
  (listed 1-8 = physical; 12/16 = 50%; 220/360 = 0, made to order), A-PRD-13 one pool per duplicate, A-PRD-16 yarn
  above reorder point for the 5 priority SKUs, A-PRD-17 first-QC pass 95% (5% fail) planning baseline, A-PRD-20/A-PRD-21
  yarn grams and labour minutes, A-PRD-06/07/08 yarn EUR/kg, A-PRD-10 trims, A-PRD-15 yarn supplier lead time 2 weeks.
- Units: finished garment units, ex VAT where a margin is shown. Externalities (packaging EUR 1.50 = A-OPS-10,
  shipping by zone = A-OPS-02..08, payment A-FIN-01/02, returns allowance 5% of net = A-GM-21) are Finance's per the GM
  rulings W3-2/W3-3 and already feed the CM2 columns cited below.

## 3. Capacity and output in October (planning vs actual)

### 3.1 Assumed baseline (used, not measured)

| Input | Value | Source |
|---|---|---|
| Maker step available | 1,125 effective min/week | A-PRD-04 |
| People making | 1 (Kristine) x 25 h/week | A-PRD-03 |
| Efficiency | 0.75 | A-PRD-02 |
| Drying rack | 6 garments at once, 24-48 h | A-PRD-05 |
| Rework reserve | 15% of available (169 min) | A-PRD-17 |

### 3.2 Actuals to fill (owner/Q4 log)

| Week | File | WIP finished garments | Orders dispatched | Minutes actually used (knit/link/finish/wash/QC/pack) | Load % on maker step | RAG | Notes |
|---|---|---|---|---|---|---|---|
| W43 (21-25 Oct) | `capacity-2026-W43.md` | FILL | FILL | FILL | FILL (plan = 71% on W44 buffer) | FILL | Assumed load only |
| W44 (26-30 Oct) | `capacity-2026-W44.md` (due Fri 30 Oct) | FILL | FILL | FILL | FILL | FILL | |
| (week of 1-? Nov belongs to the November review PRD-27) | | FILL | FILL | FILL | FILL | FILL | |

- Committed orders to date: **0 direct orders** as of 2026-10-22 (capacity file); Etsy status unknown (decision 9).
- Planned W44 buffer (ASSUMPTION, in `capacity-2026-W43.md`): Hat & Scarf Set Black x4 = 520 min, Beanie
  (photographed colour) x8 = 280 min, 0 rework of committed orders, plus 325 min rework/unplanned reserve. Load on the
  maker step with that plan = 71% GREEN (assumed). Adding one made-to-order sweater (about 200 min) brings load to 89%
  AMBER; two to 107% RED.
- One-person bottleneck: no step can exceed 85% load without a mid-week re-issue of the list. The drying rack is elapsed
  time, not labour, but 24-48 h per batch.

### 3.3 Capacity notes (agent review, not measured)

- Weekly capacity files: W43 issued; W44 due Fri 30 Oct; then every Friday to 25 Dec (PRD-22 TODO, not yet done). Missing
  W44-W48 must be closed before this review is signed off on 05 Nov.
- Market stall pre-build (PRD-16, ASSUMPTION): 26 Oct - 27 Nov = 5 weeks x 1,125 = 5,625 min; 50% or more kept for online
  + Christmas made-to-order leaves about 2,800 min for stall stock, e.g. 40 beanies + 6 hat sets + 3 sweaters.
  Every stall day costs a full production day (about 225 min). Stall stock is ring-fenced and not promotable online
  (PRD-24 TODO). Whether a stall happens at all is owner decision 27; no stall production starts without that decision.

## 4. Sell-through in October (units sold / units available)

Definition (aw-production KPI): units sold in the period divided by units available to sell in that channel (assumed
opening stock per A-PRD-12/13, plus any units made in the period). Baseline week 19 Oct (ruling C16). Test orders
#00003/#00004 excluded. Squarespace Orders is the source of truth; GA4 is sessions only (no summing platforms).

### 4.1 Monthly totals (FILL from order exports)

| Metric | October | Target / note |
|---|---|---|
| Orders (site) | FILL | n; exclude test orders |
| Orders (Etsy) | FILL | unknown whether Etsy shares the pool (decision 9) |
| Orders (market) | FILL (0 planned in Oct) | n |
| Units sold, total | FILL | |
| Unique new customers | FILL | |
| Sell-through, all visible SKUs combined | FILL % | only meaningfull with the available-units denominator below |
| On-time dispatch vs promised days | FILL n/N | target >= 95% (proposal) |
| Gift orders (gift note perk) | FILL | each lowers CM2 by EUR 0.90 (A-FIN-05, FIN-19) |
| Returns/refunds opened (see Ops returns review) | FILL | Operations owns the detail |

### 4.2 Sell-through by SKU (assumed available units; sold = FILL)

Available (A) = opening stock assumed under A-PRD-12/A-PRD-13, in the `stock-duplicate-sheet.md` pool logic. These are
**not** physical counts (PRD-11 BLOCKED for 24 Oct priority 5 and 31 Oct all 22). Duplicate pools are shown once where
rows share one pool; do not add the two listings together.

| # | SKU / listing | Dup pool | Available (A) | Sold in Oct (FILL) | Produced in Oct (FILL) | End-of-month stock (count + FILL) | Sell-through % (calc) | RAG / note |
|---|---|---|---|---|---|---|---|---|
| 1 | 100% Wool Long Shawl Cardigan | — | 8 | FILL | FILL | FILL | FILL | organic only; EUR 2.61 assumed LV (assumed) |
| 2 | Merino Raglan Cardigan (Black/Brown/Blue) | — | 6 (2/colour) | FILL | FILL | FILL | FILL | Brown/Blue are MTO promise (A-PRD-23); only 2 Black assumed in stock |
| 3 | Distressed Wool Raglan | — | 1 | FILL | FILL | FILL | FILL | one-off; 1-2 units |
| 4 | Merino Raglan, Dusty Pink | — | 6 (3 S/M, 3 L/XL) | FILL | FILL | FILL | FILL | 1 of the 4 safe-to-promote SKUs |
| 5 | Lambswool Raglan Crew (A) | D1 | 8 (pool total) | FILL | FILL | FILL | FILL | shares D1 with listing B |
| 6 | Lambswool Raglan Crew (B) | D1 | (in pool D1) | FILL | FILL | FILL | FILL | do not double-count |
| 7 | Long Wool Cardigan, Shawl Collar | (may share yarn with #1) | 6 | FILL | FILL | FILL | FILL | assumed LV loss (EUR -6.57) — verify with real minutes |
| 8 | Merino Striped Oversized | — | 1 | FILL | FILL | FILL | FILL | one-off |
| 9 | Merino Turtleneck, lightweight (12 colours x XS/S/M) | hidden copy | 0 (made to order; 360 listed is placeholder) | FILL | FILL | FILL | FILL | 24 colours unphotographed |
| 10 | Merino Hat & Scarf Set (Black/Brown/Gray) | — | 6 (2/colour) | FILL | FILL | FILL | FILL | Black only safe to promote |
| 11 | Open-Front Wool Cardigan, Side-Slit | hidden copy | 1 | FILL | FILL | FILL | FILL | one-off; duplicate listing not counted |
| 12 | Oversized Merino Turtleneck, Dusty Pink | hidden copy | 1 | FILL | FILL | FILL | FILL | one-off |
| 13 | Oversized Merino V-Neck Vest | — | 2 | FILL | FILL | FILL | FILL | |
| 14 | Oversized Wool Raglan, Beige Melange | — | 1 | FILL | FILL | FILL | FILL | one-off |
| 15 | Wool V-Neck Vest (A) | D2 | 1 (pool D2) | FILL | FILL | FILL | FILL | |
| 16 | Wool V-Neck Vest (B) | D2 | (in pool D2) | FILL | FILL | FILL | FILL | |
| 17 | Pure Wool Side-Slit (A) | D3 | 8 (pool total) | FILL | FILL | FILL | FILL | |
| 18 | Pure Wool Side-Slit (B) | D3 | (in pool D3) | FILL | FILL | FILL | FILL | |
| 19 | Pure Wool Stand-Collar | D4 | 8 (pool D4) | FILL | FILL | FILL | FILL | 1 image per listing (photo gap) |
| 20 | Rib-Knit Beanie (11 colours) | — | 0 (made to order; 220 listed is placeholder) | FILL | FILL | FILL | FILL | one colour only photographed; add-to-cart colour bug to fix (CRO) |
| 21 | Women's Classic Lambswool Crew (S-XL) | (close to D1? owner) | 8 (2/size) | FILL | FILL | FILL | FILL | may overlap duplicatelistings D1; owner decides |
| 22 | Women's wool stand collar | D4 | (in pool D4) | FILL | FILL | FILL | FILL | |
| Total (pools once) | 72 assumed physical + 2 SKUs made to order | | 72 (+ pool overlap adjustments) | FILL | FILL | FILL | FILL | 735 listed, of which 580 are placeholders |

- Sell-through formula used: `sold / (available A + produced in month)`. Where produced in month is blank, the column
  falls back to `sold / available A` and is marked FILL so the two bases are not confused.
- RAG rule basis (from `capacity-2026-W43.md`): stock >= 3 across promoted sizes/colours or made-to-order capacity
  >= 5 units this week; yarn above ROP (A-PRD-16, priority 5 only); no open QC defect; indicative CM2 > 0 at CAC 0 (EUR 10
  minimum contribution A-GM-20); a real photo per promoted colour.

### 4.3 What sold and what did not (FILL after exports)

- Top 3 SKUs by units sold (FILL SKU + units + channel): ______________________
- SKUs that received traffic but recorded no sales (FILL SKU + sessions source): ______________________
- SKUs that sold out of stock (FILL SKU + date + restock decision): ______________________
- SKUs with no traffic at all in October (FILL SKU): ______________________
- 8 visible SKUs at stock 1-2 (Distressed Raglan, Striped, Open-Front, Oversized Turtleneck, both Vests, both Beige):
  any unit sold removes the last one — store stock must be set to 0 by hand on sale (owner action).

### 4.4 Channel notes

- Site (Squarespace): FILL sessions, orders, conversion directionally.
- Etsy: FILL orders and live listing status; site and Etsy may share one physical pool (ruling C14) — the Etsy status is
  unknown and was not counted above as a separate pool.
- Google free listings: FILL whether they are indexing, orders with code.
- Creator / gift guides / press: FILL (Growth owns the per-code reports, plan #11).
- Paid: none this month (no owner-confirmed cost, no target CAC, no confirmed stock — `capacity-2026-W43.md`).

## 5. Defects (QC, inspection, rework)

Status: **no `qc-log.csv` exists yet.** PRD-13 is BLOCKED (owner agreement needed to create it; tolerance = owner's to
set, proposal value +/- 2 cm = A-PRD-19). The QC checklist itself is published (`qc-checklist.md`, 11 checks, 3 grades,
100% inspection) and its tolerance line is left at the planning value until the owner confirms. Effective inspection
cannot be reported retrospectively unless units pass through `qc-log.csv`, so the rows below are placeholders.

### 5.1 October QC totals (FILL)

| Metric | Value | Target / note |
|---|---|---|
| Units inspected (100% of shipped) | FILL | planning baseline pass rate >= 95% (A-PRD-17) |
| Units failing first inspection | FILL | |
| **Defect rate** = fails / inspected | FILL % | proposal <= 5% (A-PRD-17) |
| Units reworked and shipped | FILL | |
| Units scrapped | FILL | |
| Minutes lost to rework | FILL | capacity reserve 169 min/week (A-PRD-17) |
| Repeated defect on the same SKU (2 in 4 weeks) | FILL SKU list | a repeated defect puts the SKU on AMBER in the capacity file until it is fixed |

QC log schema (once created): `date,order_no,sku,size,colour,check_no,grade,description,action(rework/scrap/shipped),
minutes_lost`. Source: `qc-checklist.md` section 3.

### 5.2 Defects by grade and check (FILL)

| Grade | Example from checklist | Count (FILL) | % of inspected (FILL) | SKUs affected (FILL) |
|---|---|---|---|---|
| Critical | wrong item, hole, missing/wrong composition label | FILL | FILL % | FILL |
| Major | measurement out of tolerance, shade mismatch, dropped stitch | FILL | FILL | FILL |
| Minor | loose end, lint | FILL | FILL | FILL |

### 5.3 Defects by SKU (FILL), root-cause candidate review (agent)

No defective units are assumed. Agent review of the risk surface from existing files (not a defect log):
- Measurements: no tolerance set yet (A-PRD-19, +/- 2 cm planning); the PDP size table is the reference (check #2).
- Fibre labels: 22 of 22 SKUs have no spec sheet on file (`label-check-2026-10-21.md`); a missing/incorrect
  composition label is Critical (do not ship) once the adviser confirms the wording (PRD-19, PRD-18 BLOCKED).
- Colorway photos: 24 colour variants have no real photo (beanie 10, turtleneck 11, hat set 2, cardigan Blue 1); shade
  mismatch (check #7) cannot be validated visually for those.
- Buttons on button cardigans (P1 has buttons, +EUR 2.40 trims A-PRD-10): pull test (check #9) before packing.
- One dye lot across body and sleeves (check #7): affects multi-skein garments; dye-lot tracking lives with PRD-07 yarn
  data (BLOCKED).
- Drying creases / blocking (check #6): 24-48 h dry time per batch (A-PRD-05).

### 5.4 Label block (defect prevention until evidence exists)

Day-to-day rule from `qc-checklist.md`: no spec sheet for a yarn = Critical, do not ship, once the adviser confirms the
label rules. This is where the monthly review meets the legal track: see section 8.

## 6. Gross margin by SKU (assumed; costed only after owner confirms)

**Do not copy these into `sku-economics.csv`.** They remain production inputs and Finance remains the single owner of CM2
(GM rulings W3-2/W3-3, single source = `business-os/finance/sku-margins-assumed-wave3.md`). Compared with the
`sku-cost-proposals-2026-10-21.md` indicative CM2 columns (which still show Production's withdrawn EUR 3 / EUR 12
placeholders), cite **Finance's** per-zone CM2 only. Actual gross margin for October also needs the real channel mix by
order, returns and the actual shipping/packaging per parcel; all of those are FILL.

### 6.1 Assumed contribution, priority 5 (EUR per order, ASSUMPTION, A-PRD-01/-06/-07/-09/-10/-18/-20/-21; zone data from FIN)

| SKU | Price | Net | M+L (assumed) | CM1 % | CM2 LV | CM2 EE/LT | CM2 EU other (free) | CM2 EU other (W3-13 flat 12) | CM2 US/CA/AU (free) | CM2 US/CA/AU (W3-13 flat 15) | Max CAC LV | Flag |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 Merino Raglan Cardigan (Black) | 160.00 | 132.23 | 97.32 | 26.4 | 13.87 | 12.87 | -3.13 | -3.13 | -32.52 | -21.51 | 3.87 | thin for paid, EU loss |
| P2 Merino Raglan, Dusty Pink | 155.00 | 128.10 | 81.68 | 36.2 | 25.83 | 24.83 | 8.83 | 8.83 | -19.92 | -8.91 | 15.83 | paid-capable LV+EE/LT |
| P3 Classic Lambswool Crew | 136.00 | 112.40 | 70.50 | 37.3 | 23.00 | 22.00 | 6.00 | 14.84 | -20.33 | -9.34 | 13.00 | paid-capable LV+EE/LT; EU >= 10 only under W3-13 |
| P4 Hat & Scarf Set (Black only) | 110.00 | 90.91 | 55.51 | 38.9 | 18.82 | 17.82 | 1.82 | 10.67 | -21.21 | -10.20 | 8.82 | thin for paid; EU >= 10 only under W3-13 |
| P5 Rib-Knit Beanie (photo colour only) | 45.00 | 37.19 | 13.33 | 64.2 | 13.09 | 12.09 | -3.91 | 4.93 | -18.65 | -7.64 | 3.09 | best CM1 %, lowest EUR; organic/gift, not a paid hero |

### 6.2 Assumed margin map for all 22 visible SKUs (from FIN, values not to be copied as facts)

- 19 of 22 leave >= EUR 10 in LV and EE/LT; 2 are 0-10; 1 loses money even in LV (Long Wool Cardigan, Shawl Collar,
  EUR -6.57 assumed). Baltics carry the assumed profitability.
- US/CA/AU: **20 of 22 lose money** on free shipping (-6.96 to -51.06 per order assumed), 2 break even at EUR 0.14 (both
  beige V-Neck Vest units, one shared pool). Paid traffic in these zones is not realistic without a EUR 39-58 shipping
  charge per priority order.
- EU other (free shipping): 7 of 22 reach EUR 10; W3-13 (EUR 12 flat below EUR 150) raises that to 13 of 22, still
  excluding P1 and P2 because they sit above the free-shipping threshold.
- Minimum contribution (W3-14) stays EUR 10 (mid case). At EUR 15 the EU-other qualifying SKU count falls from 13 to 9
  and no priority SKU stays. LV Max CAC at EUR 15 becomes 10.83 (P2) and 8.00 (P3).
- Best unit margins sit on 1-2 unit SKUs (Distressed Raglan, Beige Raglan, both vests); those are organic sell-through
  candidates, not a promotion, because stock is too low and duplicate listings still need dedupe (decision 20a).

### 6.3 Gross margin for October (FILL, once the audit lands)

| Metric | Value | Source / note |
|---|---|---|
| Revenue ex VAT, month | FILL | Squarespace + Etsy, ex VAT |
| Cost of goods sold (actual M+L, once confirmed) | FILL / TODO-confirmed | SKU list + units; do not backfill assumed values |
| CM1 (actual) | FILL | actual net - actual M+L |
| CM2 (actual, all zones, actual shipping/packaging/returns) | FILL | Ops actuals per region |
| CM2 vs EUR 10 minimum contribution | FILL | flag any SKU/zone below |
| Gift-order effect (EUR 0.90 per gift order, A-FIN-05) | FILL | |

## 7. Yarn, reorder and material position

Status: no yarn stock count exists (PRD-07 BLOCKED). No physical stock count exists (PRD-11 BLOCKED). Reorder proposals
are therefore ASSUMED (none this week, see `yarn-reorder-template.md` s1-2).

- Assumed (A-PRD-16): yarn on hand covers >= 10 units per priority SKU in the promoted colour, from one dye lot — this
  is why the capacity file calls yarn "above ROP" for the priority 5. **Never use it to support paid spend.** Replaced
  by an owner yarn count (decision 4, 28 Oct).
- Yarn prices ASSUMED: merino EUR 60/kg (A-PRD-06), lambswool EUR 50/kg (A-PRD-07), plain wool EUR 40/kg (A-PRD-08);
  waste 8% (A-PRD-09); trims EUR 0.80 per garment, beanie 0.50, hat set 1.00, button cardigans +2.40 (A-PRD-10).
  Supplier invoices needed to close PRD-07/PRD-20.
- Supplier lead time assumed 2 weeks, safety stock 2 weeks of use, reorder whole-garment quantities per dye lot
  (A-PRD-15).
- December planning (W45-W50, in `yarn-reorder-template.md` s3): 3 hat sets + 10 beanies + 1 Dusty Pink per week comes to
  about 18.3 kg of merino-class yarn, reorder point 12.2 kg, ceiling about EUR 1,100 minus yarn on hand (unknown) — see
  PRD-20 December yarn reorder, an assumption, not a purchase authority.
- Owner (decision 32 after a finance cash check) is the only one who places any yarn order; the agent drafts requests
  only (HARD RULE 6).

## 8. Supplier notes (agent, draft only — no suppliers contacted)

### 8.1 Facts on file vs facts still needed (PRD-07, PRD-18 BLOCKED)

| Item | Assumed / on file | Still needed | Status |
|---|---|---|---|
| Merino yarn supplier + price/kg | A-PRD-06 EUR 60/kg (eBay listing range) | Invoice: supplier, price, MOQ, lead time, dye lot | BLOCKED |
| Lambswool yarn supplier + price/kg | A-PRD-07 EUR 50/kg | Same, plus Knoll Supersoft 11.5/2 confirmation | BLOCKED |
| Plain wool yarn supplier + price/kg | A-PRD-08 EUR 40/kg | Same | BLOCKED |
| Trims / buttons / labels | A-PRD-10 EUR 0.80 baseline | Supplier quote per component | BLOCKED |
| Supplier spec sheets / fibre evidence | none on file (PRD-18) | One spec sheet per yarn (priority 5 by 31 Oct, rest by 30 Nov) | BLOCKED |
| Packaging | OPS EUR 1.50 per order (A-OPS-10, W3-2) | supplier quote | OPS owns |
| Carrier / shipping rates, transit times | A-OPS-02..08 by zone (5 / 6 / 22 / 28 EUR) | one real label price LV / DE / US, carrier data (Operations) | in flight with Ops |
| 2-week yarn lead time / safety stock | A-PRD-15 | purchase orders + delivery experience | BLOCKED |
| Customer labour rate | A-PRD-01 EUR 12/h (CSB Latvia + minimum wage floor) | owner confirms (decision 5b, 28 Oct) | BLOCKED |

### 8.2 Fibre-composition and label position (PRD-17 DONE, PRD-18/19 BLOCKED)

From `label-check-2026-10-21.md`: **22 of 22 visible SKUs have no evidence on file**, and at least 4 make certification,
origin or "pure new wool" claims that need documents; the beanie shows **no composition at all** in the export. At least 4
SKUs (raglan cardigan, one crew listing, hat set, stand-collar) carry certification/origin/"pure new" wording in the export.
Rules applied (adviser to confirm): Annex I fibre names, "100%"/"pure"/"pure new wool" conditions, composition visible before
purchase (Art. 16), no certification claim without a certificate.

Open claims requiring documents or removal:
- "Hand-Knitted / Handmade" versus manual-machine production (brand claim gate — do not repeat "Hand-Knitted" from
  the P2 title; writer copy handled via brand-voice rules).
- "RWS-certified, mulesing-free, traceable, spun in Italy" on the Hat & Scarf Set — banned without certificate, and not
  safe to use anywhere while PRD-18 is open.
- "STANDARD 100 by OEKO-TEX®, REACH compliant, non-mulesed" on the Shawl Collar long cardigan.
- Language set for the sewn label (Latvian only vs more) — adviser question.
- Labelling is a legal/compliance interpretation: the agent proposes, the EU consumer-law adviser confirms; label
  wording never ships on an agent's word (HARD RULE 4).

### 8.3 Supplier action list (drafted for the owner; no orders placed)

1. Ask the owner for the yarn invoices for all 3 yarn classes and the trims card (PRD-07, decision 4), then (only after
   that) for spec sheets so `label-check` can close.
2. Decide whether to run the advisers pack for label languages on 03 Nov (`label-check` section TODO).
3. Re-run the cost proposal table once timed minutes + yarn grams exist (PRD-06): timing P1/P2/P3 changes the numbers
   more than any carrier or fee choice (EUR 6.00 CM2 per 30 minutes saved at EUR 12/h, A-PRD-01).
4. Consider removing or deferring "paid traffic candidates" until PRD-07 and PRD-11 close. Only P2 (Dusty Pink) and P3
   (Classic Lambswool Crew) are paid-capable on assumed figures, LV + EE/LT only.

## 9. Stock truth and risks (assumed, pending PRD-11)

- Assumed physical stock of the 22 visible SKUs: **72 units** (vs 735 listed), of which 580 are beanie 220 + turtleneck
  360 placeholder quantities with no physical stock assumed; 4 listings duplicate 8/8/1/1 pools (A-PRD-12, A-PRD-13).
- Physical count due 24 Oct for the priority 5 and 31 Oct for all 22 (decision 4, 20a). Until then the assumed quantities
  drive planning and **cannot** support ads spend.
- 8 visible SKUs at stock 1-2: one order sells them out (Distressed Raglan, Striped Oversized, Open-Front, Oversized
  Turtleneck Dusty Pink, both Vests, Oversized Wool Raglan Beige, one of the stand-collar pool).
- Hidden copies of 5 products exist in `sku-economics.csv`; they are not counted in the table above.
- Cardigan Brown/Blue: promised as made to order, 10 working days dispatch (A-PRD-23, W3-10), with the assumed 2 per
  colour as upside only until the 24 Oct count (decision 4). Black is in stock.
- Beanie (220) and turtleneck (360): **assume 0 on shelf, made to order**. Overselling risk; the Merchant Center feed
  hard-codes `in_stock`.
- 4 duplicate pairs still unresolved (lambswool raglan crew 16/8, side-slit 16/16, beige vest 1/1, stand-collar 12/16);
  close or double-count changes October sell-through; stock kept as one pool in this review so the numbers are not inflated.
- Etsy and the site may share one physical pool (ruling C14); the Etsy status is unknown and is not counted as a
  separate pool in section 4.

## 10. Weekly capacity files expected (October closeout)

| File | Period | Status |
|---|---|---|
| `business-os/knitwear-making/capacity-2026-W43.md` | 19-25 Oct, issued Wed 21 Oct, valid to Fri 30 Oct | DRAFT (ASSUMED), pending owner approval of PRD-01 |
| `business-os/knitwear-making/capacity-2026-W44.md` | 26 Oct - 1 Nov, due Fri 30 Oct | TODO |
| W45-W52 | weekly from 2 Nov | TODO (PRD-22) |
| Weekly `qc-summary-YYYY-Www.md` (PRD-23) | from first inspected unit | NOT STARTED (0 inspections to date) |
| `business-os/knitwear-making/capacity-2026-W44.md` monthly roll-up | W45-W48 partly belong to Nov review PRD-27 | FILL |

## 11. Blockers referenced, not advanced (PRD-01, 06, 07, 11, 13, 18, 19)

These are owner tasks and are recorded here as dependencies, not marked complete:
- PRD-01: approve production plan, Friday cadence, KPI targets (master decision 1, 24 Oct).
- PRD-06: owner times 3 units each of the priority SKUs, weighs yarn (25 Oct, 8 SKUs by 31 Oct) — turns PRD-09/15 from
  ASSUMED to DONE.
- PRD-07: people + hours, labour rate, yarn on hand by colour/lot, suppliers, prices, lead times, MOQs (28 Oct).
- PRD-11: physical stock count + MTO list + dedupe decision (24 Oct priority 5; 31 Oct all 22).
- PRD-13: create `qc-log.csv` and set measurement tolerance.
- PRD-18: supplier spec sheets per yarn (priority 5 by 31 Oct, rest by 30 Nov).
- PRD-19: label wording and languages via the EU consumer-law adviser (adviser pack sent 3 Nov).

Related but also pending, not touched: PRD-20 (December yarn reorder), PRD-21 (production lead time per SKU), PRD-22
(weekly capacity files W44-W52), PRD-23 (`qc-summary` weekly), PRD-24 (stall-stock ring-fence only if a stall is taken),
and PRD-25 (MTO gift-delivery stops: EU last MTO order 19 Nov garments / 26 Nov accessories; Baltic garments LV 4 Dec,
EE-LT 3 Dec; accessories LV 11 Dec, EE-LT 10 Dec — A-PRD-22, W3-11; OPS carrier dates still needed).

## 12. Decisions and questions for the owner (max 5, GM folds into the Monday batch per ruling C11)

1. Confirm that no orders or costs are recorded below the assumption layer: approve reading every FILL in section 4/6 as a
   manual entry by the owner; agent has recorded nothing (G1).
2. Confirm the available-stock table (section 4.2) is directionally acceptable as a planning baseline, or replace the
   assumed units and the pools before any promotion decision (PRD-11). Selling 0 actual units still counts as data once
   the stock is truthed.
3. Decide whether to keep production of the two loss SKUs (Long Wool Cardigan, Shawl Collar EUR -6.57 assumed; Alt 2 Long
   Shawl Cardigan EUR 2.61 assumed) in the December plan, or pause and use the minutes for P2/P3 — a decision on
   schedule, not on price (product data frozen, ruling applies).
4. Approve (or not) drafting December stall stock (PRD-16, any of the 2,800 assumed minutes) before decision 27 closes.
5. Give the adviser pack to the EU consumer-law adviser on 03 Nov so `label-check` can move from CLAIM-CHECK to CLOSED
   (PRD-19); this decides whether the 4 at-risk claims stay on the pages.

## 13. TODO / missing data at closeout (owner/Q4)

- All measured October numbers: orders, units sold by SKU, returns, dispatch times, minutes actually used, load %, yarn left.
- Physical stock counts + duplicate decisions (PRD-11).
- Timed units + yarn weights (PRD-06), labour rate + people + hours (PRD-07).
- Yarn on hand by colour/lot, supplier price/lead time/MOQ (PRD-07), spec sheets (PRD-18).
- QC log creation + tolerance + inspections (PRD-13).
- Adviser answers on labels (PRD-19).
- Late-arriving Etsy data and shared-pool status (decision 9).
- Beanie photographed colour and the add-to-cart-without-colour fix (CRO) — both gate the GREEN list in
  `capacity-2026-W43.md`.
- Ops carrier transit data (14 Nov) feeding the final Christmas order-by line.

## 14. Assumed values cited

The following A-IDs are used in this file; every other figure is FILL or a manual note. Assumptions register:
`business-os/knitwear-making/assumptions-wave3.md`. CM2 and zone values from `business-os/finance/sku-margins-assumed-wave3.md`.
A-PRD-01 (labour EUR 12/h), -02 (efficiency 0.75), -03 (1 person x 25 h), -04 (1,125 min), -05 (drying 6 / 24-48 h),
-06 (merino EUR 60/kg), -07 (lambswool EUR 50/kg), -08 (wool EUR 40/kg), -09 (waste 8%), -10 (trims), -12 (stock rule),
-13 (one pool per duplicate), -15 (2-week yarn lead time + 2-week safety stock), -16 (>= 10 units per priority SKU on hand,
priority 5 only), -17 (first-QC pass >= 95% planning baseline), -18 (cost class from title only), -19 (tolerance +/- 2 cm
planning), -20/-21 (yarn grams / labour minutes), -22 (Christmas made-to-order cutoffs), -23 (cardigan Brown/Blue made to
order, 10 wd). Shipping/packaging/returns/payments are A-OPS-02..10 and A-FIN-01/02/03, A-GM-20/21/22 as consolidated
in Finance's file.

DRAFT for owner. Assumptions, not facts. Nothing applied. Nothing sent.