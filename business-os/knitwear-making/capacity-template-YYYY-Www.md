# Capacity + safe-to-promote — week [YYYY]-[Www] (issued [DAY DD Mon], valid to [Fri DD Mon])   Status: DRAFT for owner approval (AGENT-DOABLE skeleton)

Template for the weekly capacity file PRD-22. Copy to `business-os/knitwear-making/capacity-YYYY-Www.md` for each Friday run
(W44-W52 and beyond). Fill every FILL; keep ASSUMED values cited by A-ID from `assumptions-wave3.md`; change no numbers
on the assumption layer without updating the register. No measured or supplier fact is invented here. Manager:
aw-production, mode ASSUMPTION.
Status line conventions (from `capacity-2026-W43.md`): ASSUMED (on assumed inputs), GREEN AMBER RED per SKU, FILL for
owner/data inputs not yet available.

## 0. How to use this template
1. Set week + dates in the header; cite the previous week file.
2. Update section 1 with any owner answers received this week (people, hours, efficiency, absences, committed orders).
3. Re-run the load table (section 2) and the RAG column; re-issue mid-week if any step crosses 85%.
4. Roll forward stock from the prior week + produced - sold (section 4); with no physical count use the assumed pools
   (A-PRD-12/13) and mark every row ASSUMED.
5. Re-compute "max units to promote" per visible SKU using the GREEN gate in section 5.
6. Compare yarn against ROP (reorder point) using the yarn on hand from PRD-07 data when it exists.
7. Run section 11b (stall-stock ring-fence) **only if the owner has taken a market stall** this season (see PRD-24,
   section 10 below); otherwise mark N/A and delete that line from the published file.

## 1. Week inputs (FILL / ASSUMPTION)
People making: [FILL: owner PRD-07]  (ASSUMED baseline 1 person, Kristine, A-PRD-03)
Production hours/week: [FILL]  (ASSUMED 25 h, A-PRD-03)
Efficiency: [FILL / 0.75 assumed, A-PRD-02]
Committed / paid orders in the queue this week (units): [FILL]  (Etsy unknown unless owner confirms, decision 9)
Absences (illness, photo shoot, filming, travel, stall day): [FILL]  (each full stall day = ~225 min, A-PRD-03/04, PRD-24)
Effective minutes/week available (maker step): [FILL]  (ASSUMED 25 h x 60 x 0.75 = 1,125, A-PRD-04)
Drying rack: [FILL garments/batch] drying 24-48 h per batch (ASSUMED 6 at once, A-PRD-05)
Reserve for rework (15% of available): [FILL] (ASSUMED 169 min/week, A-PRD-17 first-QC pass baseline 95%)

## 2. Load by step (key bottlenecks, A-PRD-05 single maker)
| Step | Available min | Required min (this week) | Load % | RAG | Notes |
|---|---|---|---|---|---|
| Maker (knit, link, finish, wash/block, QC, pack) | [FILL] | [FILL] | [FILL]% | [GREEN/AMBER/RED] | single person bottleneck |
| Drying rack (elapsed, 24-48 h/batch) | [FILL] garments/batch | [FILL] units | [FILL]% | [FILL] | elapsed time, not labour |
| Reserve for rework (15%) | [FILL] | held | n/a | [FILL] | |
Committed split (minutes): [FILL]: committed orders [FILL], restock [FILL], promo buffer [FILL].
Rule: no step above 85% without a mid-week re-issue of this file.

## 3. Per visible SKU (22 visible SKUs; fill from the prior file + this week's production/sales)
Stock = listed 17 Oct -> assumed physical (A-PRD-12/13) until PRD-11 confirms; duplicate pools shown once.
CM2 = Finance's CM2 per zone (single source: `business-os/finance/sku-margins-assumed-wave3.md`, GM W3-2/W3-3); never
recomputed in this file. Yarn vs ROP = owner yarn count once PRD-07 closes; until then mark assumed/unknown.
Photo flag = one real photo per promoted colour (claim gate G8: no reuse of "Hand-Knitted"; certification only with a document).

| SKU | Stock listed -> assumed (confirmed? no/yes) | Produced this week (units) | Sold this week (units) | End of week stock (units) | Makeable/wk (1,125 / min, A-PRD-20/21) | Yarn vs ROP | CM2 LV EUR (assumed, FIN) | Photo per colour | Status | Max units to promote this week | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 Merino Raglan Cardigan (Black/Brown/Blue) | [FILL] | [FILL] | [FILL] | [FILL] | 4 | [FILL] | 13.87 | Black/Brown yes; Blue no | [FILL] | [FILL] | Brown/Blue promised MTO 10 wd (A-PRD-23) |
| P2 Merino Raglan, Dusty Pink | [FILL] | [FILL] | [FILL] | [FILL] | 5 | [FILL] | 25.83 | yes (1 colour) | [FILL] | [FILL] | |
| P3 Classic Lambswool Crew | [FILL] | [FILL] | [FILL] | [FILL] | 5 | [FILL] | 23.00 | yes | [FILL] | [FILL] | |
| P4 Hat & Scarf Set (Black only) | [FILL] | [FILL] | [FILL] | [FILL] | 8 | [FILL] | 18.82 | Black yes; Brown, Gray no | [FILL] | [FILL] | |
| P5 Rib-Knit Beanie (photographed colour only) | [FILL] | [FILL] | [FILL] | [FILL] | 32 | [FILL] | 13.09 | 1 of 11 colours [VERIFY which] | [FILL] | [FILL] | add-to-cart colour bug (CRO) |
| Alt 1 Merino Turtleneck light | [FILL] | [FILL] | [FILL] | [FILL] | 5 (uses 98% of week) | [FILL] | 8.79 | 1 of 12 colours | [FILL] | [FILL] | |
| Alt 2 Long Shawl Cardigan (100% wool) | [FILL] | [FILL] | [FILL] | [FILL] | 3 | [FILL] | 2.61 | yes | [FILL] | [FILL] | thin margin |
| Long Wool Cardigan, Shawl Collar | [FILL] | [FILL] | [FILL] | [FILL] | 3 | [FILL] | -6.57 | yes | [FILL] | [FILL] | loss even in LV (assumed) |
| Lambswool Raglan Crew A+B (dup, one pool) | [FILL] | [FILL] | [FILL] | [FILL] | 5 | [FILL] | 23.00 | yes | [FILL] | [FILL] | dedupe decision pending (20a) |
| Pure Wool Side-Slit A+B (dup) | [FILL] | [FILL] | [FILL] | [FILL] | 5 | [FILL] | 28.94 | yes | [FILL] | [FILL] | dedupe pending |
| Stand-collar sweaters (2 listings, dup) | [FILL] | [FILL] | [FILL] | [FILL] | 5 | [FILL] | 24.78 | 1 image each | [FILL] | [FILL] | dedupe + photos |
| Distressed Wool Raglan | [FILL] | [FILL] | [FILL] | [FILL] | 4 | [FILL] | 34.79 | yes | [FILL] | [FILL] | stock 1-2 |
| Merino Striped Oversized | [FILL] | [FILL] | [FILL] | [FILL] | 4 | [FILL] | 23.95 | yes | [FILL] | [FILL] | stock 1-2 |
| Open-Front Side-Slit Cardigan | [FILL] | [FILL] | [FILL] | [FILL] | 4 | [FILL] | 24.47 | yes | [FILL] | [FILL] | stock 1-2 |
| Oversized Merino Turtleneck, Dusty Pink | [FILL] | [FILL] | [FILL] | [FILL] | 4 | [FILL] | 18.59 | yes | [FILL] | [FILL] | stock 1-2 |
| Oversized Merino V-Neck Vest | [FILL] | [FILL] | [FILL] | [FILL] | 8 | [FILL] | 34.64 | yes | [FILL] | [FILL] | stock 2 |
| Oversized Wool Raglan, Beige | [FILL] | [FILL] | [FILL] | [FILL] | 5 | [FILL] | 38.79 | yes | [FILL] | [FILL] | stock 1-2 |
| Wool V-Neck Vest, Beige A+B (dup) | [FILL] | [FILL] | [FILL] | [FILL] | 8 | [FILL] | 42.20 | yes | [FILL] | [FILL] | pool 1 unit |
| (repeat for any remaining visible SKUs under the visible list; do not add a row that is not in `stock-duplicate-sheet.md`) | | | | | | | | | | | |

GREEN gate (assumed inputs, skill rule 7): visible; stock >= 3 across the promoted sizes/colours OR MTO capacity >= 5
units this week; yarn above ROP (priority 5 assumed, others [FILL/unknown]); no open QC defect; indicative CM2 > 0 at
CAC 0 (Finance's LV CM2); one real photo per promoted colour.
Paid ads: **none** until owner confirms cost (decision 28a) and stock (decision 4). Safe to promote (GREEN) only:
organic posts, PDP work, pins, emails, gifting plans.

## 4. Production plan this week (minutes)
| Priority | Work | Minutes |
|---|---|---|
| 1 | Committed orders (made-to-order backlog) | [FILL] |
| 2 | Restock of GREEN SKUs within max units above | [FILL] |
| 3 | Promo buffer (planned made-to-order for the Green list) | [FILL] |
| 4 | QC rework / reserve (15%) | [FILL] |
| 5 | Other (filming, photo shoot counts as absence, timing study) | [FILL] |

## 5. Safe to promote / do not promote (hand the GREEN list to GRO / CRE / PAR / CRO / SEO)
- SAFE (GREEN, ASSUMED): [FILL SKU, max units, lead time]
- ORGANIC ONLY (AMBER) + why: [FILL SKU, reason]
- DO NOT PROMOTE (RED) + why: [FILL SKU, reason]
- Paid: **[FILL: none this week unless owner-confirmed cost + stock]**.

## 6. Lead-time and Christmas made-to-order stops (assumed, A-PRD-14/22; see christmas-orderby-production-table-2026.md)
- In stock: dispatch 2–5 working days. MTO garments: 10 wd. MTO beanie/hat set: 5 wd.
- Last MTO order for Christmas delivery, **EU**: garments 19 Nov, accessories 26 Nov. **Baltic second stop**: garments LV 4 Dec / EE-LT 3 Dec; accessories LV 11 Dec / EE-LT 10 Dec. US/CA/AU "not guaranteed."
- From each stop date, MTO for that zone stops and the buffer shifts; re-issue mid-week if the queue pushes maker load past 85%.

## 7. Stock risks (fill)
- 8 visible SKUs at stock 1-2: one order sells them out; set store stock to 0 by hand on sale (owner).
- Beanie 220 / turtleneck 360 assumed placeholders (MTO) -> overselling risk; Merchant Center feed hard-codes `in_stock`.
- Duplicate pools (4): do not add listings together (A-PRD-13).
- Etsy and site may share one physical pool (ruling C14): Etsy status [FILL].
- Unphotographed colour variants: do not promote (G8 / CRO) until photos exist.
- Cardigan Brown/Blue: promised MTO 10 wd (A-PRD-23) until the physical count changes it.

## 8. Reorder proposals (owner buys)
None this week / [FILL]: yarn on hand [FILL] vs ROP [FILL] -> ceiling EUR [FILL].
December planning: `yarn-reorder-template.md` (ASSUMED quantities; owner buys, PRD-20). Whole-garment quantities per
dye lot (A-PRD-15). Agent never places orders (HARD RULE 6).

## 9. TODO / missing data (carry forward)
Physical count (PRD-11), timed minutes (PRD-06), production facts (PRD-07), yarn count, spec sheets (PRD-18), real vs
generated photos, beanie photographed colour, Etsy status, absences. Weekly `qc-summary-YYYY-Www.md` (PRD-23) follows.

## 10. PRD-24 — stall-stock ring-fence note (OPTIONAL, include ONLY if the owner takes a market stall)
Scope: only if PRD-16 market stall = yes (owner decision 27, 10 Nov). If no stall, delete this section and say "N/A (no
stall this week)".

### 10a. Rule
Stock made or held for the market is **ring-fenced and is not promotable online** (PRD-24). It never sits on the GREEN
list and is not offered in paid ads, gifting, or creator outreach. Track it in its own line here and in the capacity
file's section 4 "stall stock" minutes line.

### 10b. This week's stall-stock position (FILL, only if a stall is taken)
| Item | Ring-fenced units | Ring-fenced minutes invested | Allowed sourcing rule |
|---|---|---|---|
| Stall beanies | [FILL] | [FILL] | from the stall pre-build window, not from online GREEN stock |
| Stall hat & scarf sets | [FILL] | [FILL] | as above |
| Stall sweaters | [FILL] | [FILL] | as above |
| **Total stall minutes this week** | | [FILL] | Pre-build window 26 Oct - 27 Nov = 5 weeks x 1,125 = 5,625 min; 50%+ kept for online + Christmas MTO -> ~2,800 min for stall stock, per `capacity-2026-W43.md` (ASSUMPTION) |
Every stall day costs a full production day (~225 min). A multi-week market (Doma laukums 27 Nov - 3 Jan) would take
most of December capacity from online orders; take one short market at most (owner decision 27). Stall stock is moved
only by a written owner decision, never by an agent edit to the storefront.

## 11. Assumed values cited in this file
A-PRD-01..23 (assumptions register); A-PRD-22 (Christmas cutoffs); A-PRD-23 (cardigan Brown/Blue MTO 10 wd);
A-OPS-02..08/10 (shipping/packaging); A-FIN-01/02/03, A-GM-20/21/22; A-CRO-01, A-CRO-07. CM2 from the Finance file.
PRD-24 optional note lives in section 10 above. PRD-25 handled by the MTO stop lines in section 6 / christmas table.

DRAFT. Assumptions, not facts. Nothing applied. Nothing sent.
