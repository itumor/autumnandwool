# Production assumptions register, wave 3 (SHARED BASELINE)

DRAFT — for owner approval. Author: aw-production, 2026-10-21. Mode: ASSUMPTION MODE (owner-approved 2026-10-21).

**Every number here is an ASSUMPTION, not a fact.** Each one stands in for an owner-supplied number. Once the owner
gives the real number, it replaces the assumption and the dependent tasks move from ASSUMED to DONE. Other departments must cite the
A-ID when they use a value (e.g. "materials+labour EUR 70.50, ASSUMPTION A-PRD-20/21").
Nothing here was written to `sku-economics.csv`, the store or any shared CSV.

Not assumed, ever: fibre content, certifications (RWS, OEKO-TEX, mulesing-free), "hand-knitted" claims, physical
stock counts. Those stay CLAIM-CHECK / BLOCKED (see `label-check-2026-10-21.md`, `stock-duplicate-sheet.md`).

## A. Global assumptions

| A-ID | Assumed value | Basis | Low–high | Conf. | Used by | Owner confirms by |
|---|---|---|---|---|---|---|
| A-PRD-01 | Labour rate **EUR 12.00 / hour** (EUR 0.20/min), all making steps, owner-maker | CSB Latvia Q1 2026 average hourly earnings EUR 11.87 gross (https://stat.gov.lv/en/statistics-themes/labour-market/wages-and-salaries/press-releases/27579-wages-and-salaries-1st); floor = 2026 minimum wage EUR 780/month ≈ EUR 4.6/h (https://www.lm.gov.lv/en/article/minimum-wage-latvia-will-be-780-euros) | 6–18 | L | PRD-09, PRD-15, FIN-03, FIN-05, GRO-15, GM-05 | 28 Oct (decision 5b) |
| A-PRD-02 | Efficiency **0.75** for hand processes | aw-production-capacity skill default (garment SAM practice: observed time x rating + allowances) | 0.60–0.85 | M | PRD-02, PRD-16, PRD-22 | Replace with measured after 4 weeks |
| A-PRD-03 | **1 person** (Kristine) making, **25 production hours/week** (5 h/day x 5 days); rest of the week goes to admin, packing, photos, support (ruling C11) | Repo: one founder/production lead (README, hiring-plan); hours = agent estimate | 15–35 h | L | PRD-02, PRD-16, PRD-21, OPS-09, GRO, CRE-16 | 28 Oct (decision 5b) |
| A-PRD-04 | Weekly capacity = 25 h x 60 x 0.75 = **1,125 effective minutes/week** | Derived A-PRD-02 x A-PRD-03 | 540–1,785 | L | PRD-02, PRD-16, PRD-22, GRO, PAR, CRE | With A-PRD-03 |
| A-PRD-05 | Bottleneck = the maker's own time (one person does every step). Drying is elapsed time, not labour: **6 garments drying at once, 24–48 h** | Agent estimate; wool dried flat (care text on PDPs) | rack 4–10 | L | PRD-02, PRD-21 | 31 Oct |
| A-PRD-06 | Merino yarn on cone **EUR 60/kg** ex VAT, delivered | eBay merino cone listings EUR ~55–75/kg (e.g. https://www.ebay.de/itm/406767424142 ~EUR 72/kg; https://www.ebay.de/itm/388319726210 ~EUR 75/kg); aggregator shows merino 28/2 at EUR 29.50–32.50/kg (https://www.ebay.de/str/strickmaschinengarn) | 30–75 | L | PRD-09, PRD-15, PRD-20 | 28 Oct (yarn invoices) |
| A-PRD-07 | Lambswool yarn **EUR 50/kg** | Knoll Supersoft 11.5/2 listing headline EUR 69.50/kg (https://www.ebay.de/str/strickmaschinengarn, unverified); Handweavers UK skein pricing (https://www.handweavers.co.uk/yarns-wool-lambswool.irc) | 35–70 | L | PRD-09, PRD-15, PRD-20 | 28 Oct |
| A-PRD-08 | Plain wool yarn (titles "Wool", "Pure Wool", "100% Wool") **EUR 40/kg** | Agent estimate below merino/lambswool, eBay pure-wool cone listings (https://www.ebay.de/itm/403426344127) | 25–55 | L | PRD-09, PRD-15, PRD-20 | 28 Oct |
| A-PRD-09 | Yarn waste allowance **8%** (swatch, cast-on, ends, linking) | Skill: 5–10% | 5–10% | M | PRD-09, PRD-15, PRD-20 | 31 Oct (weigh garment vs cone) |
| A-PRD-10 | Trims + labels: **EUR 0.80** per garment (composition/care label, brand label, thread); beanie **EUR 0.50**; hat+scarf set **EUR 1.00**; button cardigans **+EUR 2.40** buttons | Agent estimate, no supplier quote on file | garment 0.40–1.50; buttons 1.00–6.00 | L | PRD-09, PRD-15 | 31 Oct |
| A-PRD-11 | **Superseded (GM W3-2).** Packaging is owned by OPS: EUR 1.50 per order (A-OPS-10). Production's old placeholder EUR 3.00 / 2.00 is withdrawn. Margins: see `business-os/finance/sku-margins-assumed-wave3.md` (single source) | OPS register | n/a | — | FIN-03 | 30 Oct (decision 13, OPS) |
| A-PRD-12 | **Physical stock rule:** listed stock 1–8 = real finished units as listed; listed 12 or 16 (repeated across 11 listings, suspect) = **50% physical**, rounded down; 220 (beanie) and 360 (turtleneck) = **0 on shelf, made-to-order** | Repo: `sku-economics.csv` 17 Oct export; placeholder pattern noted in plan and FIN anomaly list | low = 1/3 of listed, high = listed | L | PRD-02, PRD-10, OPS-09, CRO-23, SEO-04, FIN-17, PAR-11 | 24 Oct (5 priority) / 31 Oct (22) |
| A-PRD-13 | **Duplicate listings share one stock pool**; use the larger listed number, never the sum (lambswool raglan crew 16/8, side-slit 16/16, beige vest 1/1, stand-collar 12/16) | FIN anomaly 1; plan s1 | sum (if separate colours) | L | PRD-10, FIN-17, SEO-04 | 31 Oct (decision 20a) |
| A-PRD-14 | **Lead time:** in stock = dispatch in 2–5 working days (live promise); made-to-order garments = **dispatch within 10 working days**; made-to-order beanie / hat set = **5 working days** | Live FAQ 2–5 wd (brand-voice skill); MTO derived from A-PRD-04/05/21 (one sweater ≈ 1 working day of effort + 1–2 days drying + queue) | garments 7–15 wd; accessories 3–7 wd | L | PRD-04, PRD-21, PRD-25, OPS-02, OPS-08, OPS-09, CX FAQ, CRO-26 | 24 Oct (decision 3) |
| A-PRD-15 | Yarn supplier lead time **2 weeks**; safety stock **2 weeks of use**; reorder whole-garment quantities per dye lot | Skill rule 5; EU cone suppliers ship 1–2 weeks (agent estimate) | 1–4 weeks | L | PRD-14, PRD-20 | 28 Oct |
| A-PRD-16 | Yarn on hand covers **≥ 10 units per priority SKU in the promoted colour**, from one dye lot (so "yarn above ROP" is assumed true for the 5 priority SKUs only) | No data. Agent assumption so a planning list can exist. **Never use it to support paid spend** | 0–30 units | L | PRD-02 GREEN gate, GRO, PAR gifts | 28 Oct (decision 5b) |
| A-PRD-17 | First-QC pass rate **95%** (5% rework; capacity keeps a 15% unallocated buffer) | Plan KPI proposal >= 95% | 90–98% | L | PRD-02, PRD-23 | After first 20 inspected units |
| A-PRD-18 | Cost class per SKU (merino / lambswool / wool) taken from the **title only, for costing**. This is **not** a fibre claim and must not be used on labels or pages | Titles in `sku-economics.csv` | n/a | L | PRD-09, PRD-15 | With PRD-18 spec sheets |
| A-PRD-19 | QC measurement tolerance **±2 cm** on width/length/sleeve (planning only; PRD-13 stays with owner) | Skill example "+/-1-2 cm" | ±1–3 cm | L | PRD-12, CX-08 | 31 Oct (decision 20a) |
| A-PRD-22 | **Christmas made-to-order stops (GM W3-1/W3-11):** **EU** (non-Baltic addresses) last MTO order = **19 Nov garments**, **26 Nov beanie/hat set** (10 / 5 wd back from 3 Dec, ruling C3). **Baltic second stop** (Baltic delivery addresses only): garments **LV 4 Dec / EE-LT 3 Dec**, accessories **LV 11 Dec / EE-LT 10 Dec**. US/CA/AU "not guaranteed". Order-by line on cardigan, beanie, hat set PDPs + FAQ by 9 Nov (owner applies) | Derived A-PRD-14 + master ruling C3 + GM W3-11 | ±1 week | L | PRD-21, PRD-25, OPS cutoff table, CRE-22, CX-25, SEO-26, CRO-25 | 4 Nov (W3-11), 14 Nov (OPS carrier dates G5) |
| A-PRD-23 | **Cardigan Brown/Blue = made to order, dispatch within 10 wd** (customer promise, GM W3-10, A-CRO-01). The assumed 2 units per colour on the shelf (A-PRD-12) are upside only, never promised. Black = in stock | GM W3-10 (less risky promise wins) | n/a | M | PRD-02, PRD-04, CRO, SEO | 24 Oct (physical count, decision 4) |

## B. Per-SKU assumptions (all 22 visible SKUs): A-PRD-20 yarn grams, A-PRD-21 labour minutes

Minutes = total effective minutes per unit (knit + link/seam + hand finish + wash/block active time + QC/label + pack).
Benchmarks are agent estimates for manual flat-machine knitwear. **No unit has been timed or weighed.**
Low–high: grams ±20%, minutes −25% / +50%. Confidence L for all. Owner confirms by 25 Oct (priority 5), 31 Oct (8),
20 Nov (22) via `timing-sheet.md`.

Packaging column below is the withdrawn Production placeholder (A-PRD-11), kept for history only; use FIN's margins file.

| # | product_id | SKU | Priority | Cost class (A-PRD-18) | A-PRD-20 grams | Yarn EUR/kg | A-PRD-21 minutes | Trims EUR | Packaging EUR (withdrawn) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 691050bcb0c4a7226c535650 | Merino Wool Raglan Cardigan | P1 | merino | 650 | 60 | 260 | 3.20 (incl. buttons) | 3.00 |
| 2 | 69105bd9b0c4a7226c5359f0 | Merino Raglan Sweater, Dusty Pink | P2 | merino | 600 | 60 | 210 | 0.80 | 3.00 |
| 3 | 691059dfdc1bc40ece1f4648 | Women's Classic Lambswool Crew | P3 | lambswool | 550 | 50 | 200 | 0.80 | 3.00 |
| 4 | 69105624c6bfa9183a014d2a | Merino Wool Hat & Scarf Set | P4 | merino | 440 (beanie 90 + scarf 350) | 60 | 130 | 1.00 | 3.00 |
| 5 | 69105690dc1bc40ece1f4561 | Rib-Knit Beanie | P5 | merino (conservative) | 90 | 60 | 35 | 0.50 | 2.00 |
| 6 | 69105a8503d8727c4c7e8e1d | Merino Turtleneck, lightweight | Alt 1 | merino | 320 | 60 | 220 | 0.80 | 3.00 |
| 7 | 69105a2903d8727c4c7e8dfa | 100% Wool Long Shawl Cardigan | Alt 2 | wool | 850 | 40 | 300 | 0.80 | 3.00 |
| 8 | 69105a20b0c4a7226c53591c | Distressed Wool Raglan Sweater | | wool | 600 | 40 | 230 | 0.80 | 3.00 |
| 9 | 691059de03d8727c4c7e8dd9 | Lambswool Raglan Crew (listing A) | | lambswool | 550 | 50 | 200 | 0.80 | 3.00 |
| 10 | 691059deb0c4a7226c535904 | Lambswool Raglan Crew (listing B) | | lambswool | 550 | 50 | 200 | 0.80 | 3.00 |
| 11 | 69105a2ab0c4a7226c53591f | Long Wool Cardigan, Shawl Collar | | lambswool | 850 | 50 | 300 | 0.80 | 3.00 |
| 12 | 69105a2694cd8c749255d65d | Merino Striped Oversized Sweater | | merino | 650 | 60 | 240 | 0.80 | 3.00 |
| 13 | 69105a8403d8727c4c7e8e1c | Open-Front Wool Cardigan, Side-Slit | | wool | 700 | 40 | 260 | 0.80 | 3.00 |
| 14 | 69105adfb0c4a7226c535976 | Oversized Merino Turtleneck, Dusty Pink | | merino | 650 | 60 | 230 | 0.80 | 3.00 |
| 15 | 6915d24b03d8727c4c8380ea | Oversized Merino V-Neck Vest | | merino | 350 | 60 | 140 | 0.80 | 3.00 |
| 16 | 691055d8dc1bc40ece1f451a | Oversized Wool Raglan, Beige Melange | | wool | 600 | 40 | 210 | 0.80 | 3.00 |
| 17 | 6910544d03d8727c4c7e8c2e | Wool V-Neck Vest, Beige (listing A) | | wool | 350 | 40 | 140 | 0.80 | 3.00 |
| 18 | 69105a83b0c4a7226c535945 | Wool V-Neck Vest, Beige (listing B) | | wool | 350 | 40 | 140 | 0.80 | 3.00 |
| 19 | 691059dc03d8727c4c7e8dd6 | Pure Wool Side-Slit Sweater (A) | | wool | 550 | 40 | 200 | 0.80 | 3.00 |
| 20 | 691059dd03d8727c4c7e8dd8 | Pure Wool Side-Slit Sweater (B) | | wool | 550 | 40 | 200 | 0.80 | 3.00 |
| 21 | 69105ad603d8727c4c7e8e4e | Pure Wool Stand-Collar Sweater | | wool | 600 | 40 | 210 | 0.80 | 3.00 |
| 22 | 69105acfb0c4a7226c53596e | Women's wool stand collar sweater | | wool | 600 | 40 | 210 | 0.80 | 3.00 |

Resulting per-SKU materials+labour (ASSUMPTION) and indicative CM1/CM2 values: `sku-cost-proposals-2026-10-21.md`.

## C. Values borrowed from other departments (not A-PRD; their register wins)

**Single source for packaging, shipping, payment, returns and CM2: `business-os/finance/sku-margins-assumed-wave3.md`**
(GM rulings W3-2/W3-3/W3-4). Production no longer carries its own placeholders (old EUR 3 packaging / EUR 12 shipping
withdrawn). The capacity file's CM2 column copies Finance's CM2 LV figure.

| Value | Now taken from | Owner of the number |
|---|---|---|
| Packaging per order | EUR 1.50 (A-OPS-10, W3-2) via FIN margins file | OPS |
| Shipping per order | by zone: LV 5 / EE-LT 6 / EU-other 22 / US-CA-AU 28 + duty (A-OPS-02..08, W3-3) via FIN margins file | OPS (carrier rates) |
| Payment per order | A-FIN-01/02 via FIN margins file | FIN / owner account rates |
| Returns allowance | 5% of net (A-GM-21, W3-4) | GM / FIN / owner |
| Target CAC | none set; CM2 checked at CAC 0 (organic); min contribution EUR 10 (A-GM-20, W3-14) | GM / GRO |

## TODO / missing data (replaces assumptions when received)

- Timing of 3 real units per priority SKU (PRD-06), yarn grams per garment, labour rate, people + hours (PRD-07).
- Yarn invoices (price/kg, supplier, lead time, MOQ, dye lots on hand).
- Physical stock count, MTO list, dedupe decision (PRD-11).
- Supplier spec sheets for fibre composition (PRD-18): **never assumed**.
