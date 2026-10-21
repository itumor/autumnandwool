# Product & Production plan, Q4 2026 and 2027

DRAFT — for owner approval. Written 2026-10-21 by aw-production. Nothing here changes stock, costs, product data
or `sku-economics.csv`. Targets marked (proposal) are my suggestions; the owner sets final values.
Unknown = `TODO` / `[VERIFY]`. No stock, cost, minutes, yarn or fibre figure below is invented.

Sources: `business-os/README.md` s6/s9/s11, `business-os/hiring-plan.md`, `business-os/ai-team.md`,
`business-os/sku-economics.csv`, `products_Oct-17_10-46-00PM.csv`, `zero-sales-diagnosis-2026-10-18.md`,
`GROWTH-PLAN-100-IDEAS.md`, `owner-action-pack-2026-10-19.md`, `markets-and-gift-guides.md`,
`implementation-report.md`.

---

## 1. Starting point (facts from repo)

| Area | Fact | Source |
|---|---|---|
| Catalog | 82 products, 22 visible, 60 hidden (mostly crochet fingerless gloves at EUR 39-83, plus hidden duplicates) | `sku-economics.csv` |
| Visible range | Sweaters/jumpers EUR 136-165, cardigans 145-160, vests 126, turtlenecks 110-155, hat+scarf set 110, beanie 45 | `sku-economics.csv` |
| Costs | All five cost columns and `target_cac_eur` are empty for all 82 rows. Gross margin per SKU is unknown. Only the illustrative EUR 155 sweater exists (not real) | `sku-economics.csv`, README s9 |
| Stock numbers | Turtleneck 360, beanie 220 look like made-to-order placeholders. Most visible garments show stock 1-16. 7 visible SKUs show stock 1 | `sku-economics.csv`, `ai-team.md` item 2 |
| Duplicates | Same title listed more than once among visible items (lambswool crew x2 plus a "Classic Lambswool Crew", pure wool side-slit x2, beige vest x2, stand-collar sweaters x3). Owner must pick one source of truth | `sku-economics.csv`, action pack B.2 |
| Work content | Minutes per step, yarn grams per garment, yarn stock by colour/lot, supplier lead times, MOQs, labour rate: none on file | `ai-team.md` item 8 |
| Process | Manual knitting machines, hand finishing, Riga. Dispatch promise 2-5 working days (brand-voice rule); Merchant Center lists 4-10 business days. No delivery-time ranges in Squarespace shipping yet | brand-voice skill, diagnosis #2 |
| Photos | Colour photos missing: beanie (10 colours), turtleneck (11 colours x S-XL, 36 feed rows), hat set (2), cardigan Blue (1) | action pack A |
| Demand | Zero direct orders to date. 64 visits in 30 days. First real orders are now possible only once traffic starts | diagnosis s1, README s2 |
| Fibre claims | Titles say "100% Wool", "Pure Wool", "Merino", "Lambswool", "100% pure new wool". No supplier spec sheet on file for any of them. Catalog claims cleanup only partly verified; some catalog items may be blends/acrylic | `implementation-report.md`, README s7 |
| Labels | Reg. (EU) 1007/2011 label on every garment is a QC requirement in the plan, no label-check file exists yet. Language question (Latvian, others) open: adviser to confirm | README s6/s11 |
| Sales calendar | Season is now. Riga markets: Doma laukums 27 Nov-3 Jan, Kalnciema Saturdays 28 Nov-26 Dec, Baltic EXPO 11-13 Dec, White Xmas 18-20 Dec, KuKu 29 Nov (apply by 10 Nov) | `markets-and-gift-guides.md` |
| Agent outputs | No `capacity-YYYY-Www.md`, `sku-cost-proposals`, `qc-checklist.md` or `label-check` exist yet | repo glob |
| Marketing gate | Marketing may promote only SKUs on my GREEN list. With costs unknown every SKU is AMBER at best ("cost unknown") | skill rule 7 |

Net: the single biggest blocker is owner-supplied production data. Without it I can only publish AMBER lists, and
paid ads stay blocked (`ai-team.md` item 1).

---

## 2. Q4 2026 (21 Oct - 31 Dec): goals, KPIs, actions

### Goals
1. Get production facts out of Kristine's head into 5 numbers per SKU, fast and cheaply (timing real units, not a project).
2. Publish a weekly capacity + safe-to-promote list so no gift order is accepted that cannot ship before Christmas.
3. Cost the 22 visible SKUs (proposal file, owner confirms) so GM/Finance can set minimum contribution and ad caps.
4. QC checklist live on 100% of units shipped; fibre-label evidence collected for the visible range.
5. Yarn covered for the December peak without over-buying (owner buys; I propose quantities).

### KPIs (numeric targets; baselines are TODO until week 1 data exists)

| KPI | Target | By | Note |
|---|---|---|---|
| Visible SKUs with cost sheet proposal (materials + labour) | 22 of 22 | 6 Nov | Owner confirms values before they go in the CSV |
| Visible SKUs with timed minutes per step (3 units, median) | 8 priority SKUs by 31 Oct, 22 of 22 by 20 Nov | | Priority = GM's 5 plus beanie + hat set |
| Capacity file issued | Every Friday from 23 Oct (10 files to 25 Dec) | | `business-os/capacity-YYYY-Www.md` |
| Visible SKUs with a documented yarn spec sheet (fibre evidence) | 22 of 22 | 30 Nov | Missing = label-check issue, SKU stays AMBER |
| First-QC pass rate (100% inspected) | >= 95% (proposal); baseline set in first 2 weeks | Dec | Defect rate = fails / inspected |
| On-time dispatch vs promised days | >= 95% of orders | Dec | Needs owner's promised days confirmed |
| Orders accepted beyond capacity (red step) | 0 | Dec | Re-issue list mid-week if a step goes red |
| Stock truth confirmed for 22 visible SKUs | 22 of 22 | 31 Oct | Fixes the 360/220 placeholder risk |
| Yarn below reorder point with no open proposal | 0 | from 16 Nov | Needs yarn stock + lead times |
| Label wording check per visible SKU (adviser to confirm) | 22 of 22 drafted | 20 Nov | |

### Weekly actions (every week)

| Day | Action |
|---|---|
| Mon | Read order exports (Squarespace/Etsy). Log defects in `qc-log.csv` if owner agrees to create it |
| Thu | Ask owner 5 questions max (open data gaps), merge answers |
| Fri | Publish `capacity-YYYY-Www.md`: load by step, GREEN/AMBER/RED per visible SKU, max units to promote, stock risks, reorder proposals. Hand GREEN list to growth, ads, content |
| Fri | `qc-summary-YYYY-Www.md`: defect rate, repeat defects (SKU goes AMBER until fixed) |
| Any | Re-issue mid-week if a step turns red or a SKU hits stock 0 |

### Dated actions

| Date | Action | Who |
|---|---|---|
| Wk 43 (by 23 Oct) | First capacity file, mostly TODO + AMBER; owner question list (below) | Agent |
| By 25 Oct | Owner times 3 units each of beanie, hat set, one sweater, one cardigan, one vest (steps: knit, link, finish, wash/block/dry, QC+label, pack) and weighs yarn per garment | Owner |
| By 28 Oct | Owner gives: people + hours/day, labour rate, yarn on hand by colour/lot, supplier names + lead times + MOQs | Owner |
| 30 Oct | `sku-cost-proposals-2026-10-30.md` (first 8 SKUs) with TODO list. Default efficiency 0.75 shown as assumption | Agent |
| 31 Oct | Owner confirms physical stock for 22 visible SKUs; dedupe decision for duplicate listings | Owner |
| 31 Oct | `qc-checklist.md` (11-line checklist, defect grades, tolerance TODO owner sets) | Agent |
| 6 Nov | Cost proposals for all 22 visible SKUs. Owner confirms, then GM/Finance run `unit_economics.py` | Agent / Owner |
| 10 Nov | Market decision deadline: KuKu fee window closes. Production input = what can be made for stalls without starving online orders | Owner |
| 13 Nov | `label-check-2026-11-13.md`: per-SKU table with spec-sheet evidence, claims vs evidence. "Likely issue, adviser to confirm" only | Agent |
| 16 Nov | Yarn reorder proposals for December demand. Owner buys. Whole-garment quantities per dye lot | Agent / Owner |
| 20 Nov | Last-order-date table per country/zone for Christmas (needs carrier times from Operations). Feeds growth idea 10 | Agent + Ops |
| 27 Nov-3 Jan | If owner takes a market stall: capacity file adds a "stall stock" line; stock held for markets is not promotable online | Owner decides |
| 11 Dec | Stop accepting made-to-order for gift delivery unless the table says it ships in time (dates TODO until lead times known) | Owner |
| 28 Dec | Q4 review: sell-through, defect rate, yarn left, what sold. Feeds 2027 range plan | Agent |
| 31 Dec | `production-review-2026-12.md` (monthly file; also Nov review by 5 Dec, Oct by 5 Nov) | Agent |

### Q4 range rule
No new styles this quarter. Priority is making the existing 22 visible SKUs producible and promotable. Candidate
hero gift SKUs (for owner to confirm against costs and capacity): beanie EUR 45 (gift entry price), hat+scarf set
EUR 110, one cardigan, one sweater. Beanie/turtleneck variants stay AMBER until a real photo exists per promoted
colour. Hidden crochet glove listings stay hidden; reviving them is a 2027 decision (crochet process, different
skills, own timing needed).

---

## 3. 2027 by quarter

Targets for 2027 are conditional on Q4 data (real orders, minutes, margins). Numbers below are placeholders to
be reset on 15 Jan 2027 using Q4 actuals; "TODO" means no basis exists today.

### Q1 2027 (Jan-Mar): baseline and cost discipline
- **Goals:** every visible SKU has confirmed cost and a gross-margin figure; reorder points live; label evidence closed out; decide the 2027 range.
- **KPIs:** gross margin per SKU known for 22 of 22 (target: first margin floor set by owner, TODO value); CM1 below 40% of net flagged on every SKU (benchmark in unit-economics skill, not a rule); defect rate <= 5% (proposal); yarn stockouts on promoted SKUs: 0; stock-risk report weekly.
- **Initiatives:**
  1. Fill `sku-economics.csv` columns (owner-approved) and publish first `production-review-2027-01.md`.
  2. Yarn reorder points per colour/lot: `ROP = avg weekly use x lead time + 2 weeks safety stock`. Switch to z-score once 8+ weeks of data exist (~March).
  3. Cull the range: merge duplicate listings, propose a core of 10-12 SKUs (ABC by contribution x sell-through). Proposal only, product data frozen.
  4. Fibre labels: sewn label plan per yarn (supplier name, Annex I fibre name, %). Adviser confirms wording and languages.
  5. Post-season review: January sale stock, returns causes (with Operations), defect log patterns.
  6. Decide whether crochet gloves return (needs cost, minutes, yarn data first).
- **Budget ask:** TODO. Items to price: yarn restock for spring, label printing (supplier quote TODO), measuring/timing aids (minor), adviser fee for label wording (one-off, TODO).

### Q2 2027 (Apr-Jun): spring/summer drop and capacity
- **Goals:** one lighter-weight spring drop; first real capacity expansion decision based on measured load; supplier review.
- **KPIs:** drop SKUs each with cost sheet + timing + photo before launch (100%); load on bottleneck step <= 85% at launch week; on-time dispatch >= 95%; sell-through of the drop at 8 weeks (target TODO until first sell-through data); gross margin per drop SKU >= owner floor.
- **Initiatives:**
  1. Spring drop: 2-4 lightweight styles (e.g. extra colours of the existing lightweight turtleneck, a vest or short-sleeve knit). Which fibres is `[VERIFY]` with supplier availability. Owner picks; no yarn commitment without owner.
  2. Pre-launch checklist: sample timed, costed, labelled, photographed, then GREEN.
  3. Supplier review: 2-3 yarn suppliers compared on price, MOQ, lead time, spec-sheet quality (research facts + links only, owner contacts them).
  4. Bottleneck analysis: is it knitting, finishing or drying? Propose one fix (second machine, helper hours, drying racks). Cost TODO.
  5. First quarterly label check re-run (`label-check-2027-04-*.md`).
- **Budget ask:** TODO. Drop yarn, sample yarn, extra finishing hours or helper (hiring-plan wave 3: hire only when orders exceed one person's capacity).

### Q3 2027 (Jul-Sep): autumn/winter collection build
- **Goals:** build and de-risk the autumn/winter range before the season, since knitwear sells from September. Pre-build stock for best sellers.
- **KPIs:** AW collection locked by 31 Jul (SKU list, costs, yarn orders placed by owner by mid-Aug, TODO lead times); safe-to-promote list ready for the first September campaign; pre-built stock of top SKUs = 2 units per size/colour (fixed minimum, to be replaced by weekly sales x lead time once data exists); yarn dye-lot match on 100% of garments; first-QC pass >= 95%.
- **Initiatives:**
  1. AW drop planning from Q2 sell-through and creator/market feedback: 3-5 new styles or colourways, with Creative/E-commerce briefed for photos.
  2. Pre-season yarn order: forecast from 2026 Q4 actuals and Q2 sales, owner approves each purchase; MOQs checked first.
  3. Production schedule: orders, restock, promo buffer, in the weekly capacity file; summer weeks used for pre-building (holiday absences subtracted).
  4. QC: sample garment wash/shrink test and measurements recorded before each new style goes live (tolerance set by owner).
  5. Decide if a Production/Fulfilment hire is justified by load numbers (not by feel).
- **Budget ask:** TODO. Largest line: AW yarn pre-buy. Needs Finance cash-flow check (`aw-cash-flow`) before commitment.

### Q4 2027 (Oct-Dec): peak season execution
- **Goals:** run peak without overselling; apply the 2026 lessons; ship every order inside the promise.
- **KPIs:** on-time dispatch >= 97% (proposal); defect rate <= 4% (proposal); orders accepted beyond capacity: 0; yarn stockouts on GREEN SKUs: 0; sell-through of AW drop at 10 weeks (target TODO); gross margin held at or above floor.
- **Initiatives:**
  1. Christmas production calendar published by 1 Oct (idea 97 in growth plan): last-order dates per country, cut-off for made-to-order.
  2. Weekly capacity file, mid-week re-issue on red.
  3. Gift-line focus: entry price items (beanie, sets), which are quickest to make; gift-wrap and card stock (Ops).
  4. Market stock plan if markets are used again, ring-fenced from online stock.
  5. Annual review: SKU cull/keep, supplier scorecard, label re-check, 2028 range draft.
- **Budget ask:** TODO. Peak-season finishing help (hours, rate TODO), packaging, extra yarn buffer.

### Collection drops summary (2027, all subject to owner approval)

| Drop | Timing | Content | Gate to launch |
|---|---|---|---|
| Core refresh | Feb | Existing best sellers in 1-2 new colours, culled range | Costs confirmed, photos per colour |
| Spring | Apr-May | 2-4 lightweight pieces | Cost sheet, timing, label evidence, photo |
| Autumn/Winter | Sep | 3-5 new styles or colourways | Yarn bought by owner, schedule load < 85% |
| Christmas gift edit | Oct-Nov | Bundles/sets, beanie colours, optional numbered edition (growth idea 86) | Real scarcity only if stock is real |

---

## 4. Dependencies on other departments

| Department | I need | I give |
|---|---|---|
| Owner / founder (production lead) | Timing of real units, yarn weights, yarn stock, supplier terms, labour rate, stock confirmation, dedupe decision | Cost proposals, schedules, reorder proposals to approve |
| Finance (`aw-finance`, accountant) | Payment fee schedule, shipping, packaging costs for CM2; cash-flow check before yarn buys; labour treatment | Materials + labour per SKU, yarn purchase forecast |
| Head of E-commerce / GM | Minimum contribution per order, 5 priority SKUs, promo plan 1 week ahead | GREEN/AMBER/RED list, max units to promote |
| Growth / Ads / Partnerships | Which SKUs they want to push, expected volume, creator gifting quantities | Max units to promote; gifted units come out of capacity |
| Creative / Content | Photos per colour (beanie, turtleneck, hat set, cardigan blue first), making-of content (needs studio time, counts as an absence) | Process facts for scripts, hands-on schedule |
| E-commerce / CRO | Product page fibre/size/lead-time wording changes (owner approves), delivery ranges in Squarespace | Verified composition and care lines, measurement tables |
| Operations / CX | Carrier times per zone, returns reasons, packing time per order | Last-order-date table, defect and returns feedback loop |
| Legal / EU consumer-law adviser | Label wording, language rules, "Pure/100%" use, Shipping & Returns review | Label-check table to review |
| SEO / Marketplace | Etsy sell-through (Etsy stock and listings must match real capacity, one shared stock pool) | Safe-to-sell units across both channels |

---

## 5. Risks and owner decisions needed

### Risks

| # | Risk | Effect | Mitigation |
|---|---|---|---|
| 1 | Production data stays missing | Everything stays AMBER, paid ads blocked, no honest lead-time promise | Smallest possible ask first: 8 SKUs timed by 25 Oct |
| 2 | Capacity is one person on manual machines | December demand spike could exceed it; late gift deliveries cause returns and reviews damage | Weekly load check, last-order table, cut-off for made-to-order, no scarcity claims |
| 3 | Stock numbers are placeholders (360 / 220) | Overselling, wrong Merchant Center availability (feed hard-codes `in_stock`, `ai-team.md` item 3) | Confirm physical stock; treat as made-to-order until confirmed |
| 4 | Fibre claims lack supplier evidence | Possible label/consumer-law issue (adviser to confirm); trust damage | Collect spec sheets; label-check file; no composition change without evidence |
| 5 | Marketplace and site share stock | Double-sale between Etsy and Squarespace | One stock list in the capacity file; owner confirms Etsy status |
| 6 | Yarn dye-lot variance | Shade mismatch between body and sleeves | Whole-garment quantities from one lot, daylight shade check |
| 7 | Yarn supply lead times unknown | Stockouts in peak | Reorder points once lead times known; owner contacts suppliers (I never do) |
| 8 | New drops overload a one-person studio | Delays, defects | Gate: bottleneck load < 85% before launch; hire only when load data supports it |
| 9 | Hidden crochet range (60 listings) distracts | Wasted effort, unknown cost basis | Keep hidden until costed; owner decides keep/cull in Q1 |
| 10 | Efficiency 0.75 is an assumption | Capacity over- or under-stated | Replace with measured data after 4 weeks |

### Owner decisions needed

| # | Decision | By |
|---|---|---|
| 1 | Approve this plan, the weekly Friday capacity cadence and the KPI targets (all "proposal" values) | 24 Oct |
| 2 | Provide or schedule: timing of real units, yarn grams per garment, yarn stock by colour/lot, people + hours, labour rate | 28 Oct |
| 3 | Confirm real physical stock for the 22 visible SKUs; say which stock is made-to-order | 31 Oct |
| 4 | Dedupe: which listing is the source of truth for each duplicate (lambswool crew, pure wool side-slit, beige vest, stand-collar sweaters) | 31 Oct |
| 5 | Confirm the promised dispatch days and the made-to-order lead time (propose wording; I do not change the site) | 31 Oct |
| 6 | Minimum contribution per order and gross-margin floor (with GM/Finance) | 10 Nov |
| 7 | Whether to take a market stall this season (Doma laukums, Kalnciema, Baltic EXPO) and how much stock to ring-fence. Proof of Latvian production may be required; fact must come from owner | 10 Nov |
| 8 | Supplier spec sheets or invoices for each yarn (fibre evidence), before any "100% / pure / merino" wording is kept | 30 Nov |
| 9 | Yarn purchases for December and for 2027 AW (I propose quantities only) | 16 Nov / Jul 2027 |
| 10 | Label languages (Latvian only vs more) and wording, via the EU adviser (adviser to confirm) | 20 Nov |
| 11 | Whether to create `business-os/qc-log.csv` and the QC tolerance (e.g. +/-1-2 cm, owner sets) | 31 Oct |
| 12 | 2027 range direction: core cull, spring drop scope, crochet gloves keep/cut, men's/kids line (growth ideas 88/89 are not scheduled) | 15 Jan 2027 |
| 13 | Budget lines for 2027 (yarn, labels, finishing help): all TODO until Q4 data | 31 Jan 2027 |

---

## TODO / missing data

- Minutes per step per SKU; yarn grams per garment; yarn stock, colour, dye lot; supplier names, price lists, lead times, MOQs; labour rate; efficiency; absences, people and hours.
- Confirmed physical stock; real current Etsy status and stock.
- Supplier spec sheets for fibre composition on every visible SKU.
- Carrier delivery times per zone; promised dispatch days confirmation.
- QC tolerances; defect baseline; label languages.
- All 2027 budget figures and sell-through targets (no data yet).
