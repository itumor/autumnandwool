DRAFT — for owner approval

# Operations / Fulfilment plan: Q4 2026 and 2027 (agent `aw-operations`)

Written 2026-10-21. Drafts only: I do not touch orders, labels, stock, store settings or customers. Every carrier,
rate, cost and date I cannot source is marked TODO or [VERIFY]. No carrier has been chosen; none is named here.

Sources: `business-os/README.md` (s6, s9, s11), `business-os/hiring-plan.md`, `business-os/ai-team.md`,
`business-os/kpi-weekly.csv`, `zero-sales-diagnosis-2026-10-18.md`, `markets-and-gift-guides.md`,
`owner-action-pack-2026-10-19.md`, `GROWTH-PLAN-100-IDEAS.md`, `implementation-report.md`.

## 1. Starting point (facts)

| Fact | Source |
|---|---|
| Zero real direct orders to date. 64 visits in 30 days (~2/day), 2 from Google. Zero orders is the expected result at this traffic. | `zero-sales-diagnosis-2026-10-18.md` s1 |
| Stripe proven with test orders #00003/#00004 (refunded). PayPal not connected. No GA4 ecommerce events: orders must be counted from Squarespace Orders + Etsy. | `README.md` s2 |
| `kpi-weekly.csv` is header only: no baseline week, so on-time dispatch has no history. | `kpi-weekly.csv` |
| Squarespace shipping = three EUR 0 options (Latvia, US, Rest of World). Only Latvia checkout-tested. No delivery-time range in the settings, and none shown in checkout. | `implementation-report.md` (shipping recheck 18 Oct); diagnosis issue #2 |
| Merchant Center shipping policy saved (pending Google review): Latvia free, 2-5 handling + 2-5 transit; 18 EU countries free, 2-5 + 5-10; USA/Canada/Australia free, 2-5 + 7-20. These are the public promises. They are not carrier-verified. | `implementation-report.md` (Merchant Center row) |
| Merchant Center return policy (Latvia): 14 days, customer pays return postage, refund in 7 days. This conflicts with the live page (refunds exclude shipping, 5-day defect window, no sale or made-to-order returns). Legal review is not done. | `implementation-report.md`; `README.md` s11 |
| Stock figures (turtleneck 360, beanie 220) look like placeholders for made-to-order. 13 items are out of stock while the feed says in_stock. Vest stock = 1. | `ai-team.md` owner decisions 2-3; `owner-action-pack` B2 |
| Variant photos are missing for beanie (10 colours), turtleneck (11), hat set (2), cardigan blue (1). This is a likely source of wrong-item and returns risk. | `owner-action-pack` A |
| Missing ops data: carriers, return address, HS codes, minutes per garment, supplier lead times, size table, reply-time rule (24 h vs 1-2 days). | `ai-team.md` owner decisions 5, 8 |
| Existing assets: SOP skill (`.claude/skills/aw-fulfilment-sop`), returns skill, QC checklist. No SOP, packaging spec, carrier table or returns log exists in `business-os/` yet. | `.claude/skills/`; `business-os/` listing |
| Christmas markets (27 Nov - 3 Jan, plus 11-13 Dec, 18-20 Dec) would add hand-sold stock and take production time. None is booked. | `markets-and-gift-guides.md` s1 |
| Idea list: delivery times and Christmas deadlines per country (#10), tracked shipping by default (#98), December stock and production calendar (#97), one-size exchange (#8). | `GROWTH-PLAN-100-IDEAS.md` |

Volume assumption: direct orders are 0 now. All targets below are conditional. Q4 targets are process-readiness
targets, not volume targets. I will not set order-count targets until a real baseline exists (README s10).

## 2. Q4 2026 (21 Oct - 31 Dec)

### Goals

1. Be able to ship the first real order correctly with no improvisation: SOP, packaging, one carrier per region
   chosen, return address and returns log in place by **6 Nov**.
2. Publish honest, carrier-backed delivery times and Christmas order-by dates before gift buyers arrive (unblocks
   Merchant Center and gift conversion).
3. Run every Q4 order by hand through the SOP and log it. Capture real shipping and packaging cost per order.
4. Close the policy gap: returns wording legally reviewed and consistent before the peak (target 20 Nov).

### KPIs and targets

| KPI | Q4 target | Note |
|---|---|---|
| On-time dispatch (dispatched within the promised 2-5 working days / orders) | >= 95% | Measured from the first real order. 100% of exceptions get a customer-notice draft the same day |
| Fulfilment errors (wrong / missing / damaged per order) | <= 2% (target 0 for wrong item) | Small sample: report counts, not just %, until 30+ orders |
| Fulfilment cost per order (shipping + packaging) | Real figure logged for 100% of orders; compare with `sku-economics.csv` assumptions (illustrative EUR 12 + 3 in README s9) | Target value after the first 10 orders. TODO |
| Tracking sent to customer | 100% of orders, same day as dispatch | Verify the Squarespace fulfilment email setting |
| Tracking exceptions acted on | Before the customer asks, 100% | Sweep every 2 business days |
| Returns / withdrawals logged | 100% in `returns-log.csv` with deadline dates | Refund-due date = notice + 14 days. Owner decides every outcome |
| Support-case hand-off to CX | Same working day | Reply-time rule still to be picked by the owner |

### Actions

| When | Action | Output |
|---|---|---|
| By 24 Oct | Owner gives answers to the TODO list in section 5 (carriers used today, return address, who packs, handling time). I draft the SOP from the skill and README s6 | `business-os/sop-order-to-delivery.md` |
| By 28 Oct | Carrier research per region from public price lists only, each price with a source and date. Compare with the free-shipping promise | `business-os/carrier-rates.md` |
| By 30 Oct | Packaging spec and supplies list (mailer, tissue, care card, label); quote cost per pack | `business-os/packaging-spec.md` |
| By 30 Oct | Returns log format, withdrawal and faulty-item draft replies, hand-off format to CX | `business-os/returns-log.csv` (proposed header), drafts |
| By 31 Oct | Provisional Christmas cutoff table (see below), then replace with carrier-stated dates. Owner approves publication | Table in the SOP |
| 6 Nov | Dry run: one internal test parcel to a Latvian address, one to an EU address, packed, weighed and tracked. Records real weight, cost and transit | Dispatch log first rows |
| From first order | Daily dispatch checklist (only when orders exist), 2-day tracking sweep | `business-os/dispatch-YYYY-MM-DD.md`, `dispatch-log.csv` (proposed rows) |
| Weekly (Mon) | Ops KPI file: on-time %, errors, cost/order, returns by reason and SKU, open cases with deadlines. Feeds `kpi-weekly.csv` via owner | `business-os/ops-weekly-YYYY-Www.md` |
| 20 Nov | Freeze check: policy wording status, carrier last-posting dates confirmed, stock/production calendar agreed with Production | Go/no-go note to owner |
| 26 Dec - 31 Dec | Post-peak review: all Q4 cases, cost per order, carrier performance, return reasons. Propose 2027 changes | `business-os/returns-review-2026-12.md` |

### Christmas cutoffs: provisional, worst-case arithmetic only

Method: Thursday 24 Dec 2026 delivery, working back from the promised ranges in Merchant Center
(handling 2-5 + transit by region) in business days, ignoring weekends. This uses the public promise, not carrier
data.

| Region | Worst-case dispatch-to-door | Provisional "order by" for delivery by 24 Dec | Status |
|---|---|---|---|
| Latvia | 5 + 5 = 10 business days | about 10 Dec | [VERIFY] Latvian public holidays and carrier calendar |
| EU (18 countries) | 5 + 10 = 15 business days | about 3 Dec | [VERIFY] |
| US / Canada / Australia | 5 + 20 = 25 business days | about 18-19 Nov (18 Nov is a Latvian holiday) | [VERIFY]. Likely too late already for non-express. Owner decides: say "not guaranteed for Christmas" or offer paid express (needs rates, TODO) |

Rules: the published deadline must be later than nothing I cannot support. If a carrier states a later last-posting
date, use the carrier's date minus my handling buffer. Stock items dispatch faster than made-to-order: the order-by
date for in-stock items can be later only if Production confirms physical stock (never assume the placeholder
stock figures). Gift cards (digital) carry no shipping risk and are the fallback message after each cutoff
(idea #85).

## 3. 2027 by quarter

Targets stay conditional on real order volume (TODO baseline after Q4). Budget figures are unknown until quotes
exist; I will not estimate them.

### Q1 2027 (Jan - Mar): learn from peak, fix the base

| Goals | Key initiatives | KPIs |
|---|---|---|
| Turn Q4 data into real costs and a stable process | Update `sku-economics.csv` shipping/packaging columns with actuals (proposal to owner, not edited by me). Monthly returns review. Size-guide and PDP proposals from SIZE_* clusters | On-time dispatch >= 95%; errors <= 2%; cost/order within +/-15% of Q4 actuals TODO |
| Returns done within statute | Publish adviser-reviewed returns terms (owner action). Returns log live and reviewed monthly | 100% refunds issued within 14 days of notice once owner approves; zero missed deadlines |
| Post-Christmas returns wave handled | Returns inspection per QC checklist, condition notes, deduction proposals with justification | Median days from received to owner decision <= 2 working days |
| Customs clarity for non-EU | Check with accountant and carrier what is shown at checkout for duties and VAT (UK, US, CA, AU, NO, CH). No statements without adviser | HS codes and invoice process documented. TODO |

Budget ask: packaging restock [TODO quote]; carrier contract or account fee [TODO]; adviser one-off (owner already
planned, README s3). Hours for returns handling [TODO].

### Q2 2027 (Apr - Jun): reduce cost and risk

| Goals | Key initiatives | KPIs |
|---|---|---|
| Lower fulfilment cost per order without worse service | Carrier comparison refresh (quarterly), lockers or pick-up points for Baltics where cheaper [VERIFY options]. Packaging weight and size review | Cost/order target set from Q1 actuals (TODO value); no rise in damage rate |
| Tracking and delivery promise based on data | Replace the Merchant Center ranges with observed 80th-percentile transit per region from the log | Promised vs actual: >= 90% of deliveries inside the stated range |
| Fewer errors | Pre-pack checklist with photo of packed item; label check per SKU (Production owns evidence) | Errors <= 1.5%; damaged-in-transit claims filed within carrier deadline: 100% |
| Spring market or pop-up logistics (if the owner books any) | Separate stock count and cash-up sheet; keep online stock reserved | No oversell: 0 |

Budget ask: new packaging variant tests [TODO]; label printer or supplies [TODO]; optional tracking-notification
tool only if Squarespace email proves insufficient [TODO, check plan]. 

### Q3 2027 (Jul - Sep): prepare for peak

| Goals | Key initiatives | KPIs |
|---|---|---|
| Peak-season readiness by 30 Sep | Forecast with Production: made-to-order backlog limit and the date after which "Christmas delivery" is no longer promised. Pre-buy packaging for peak (owner approves) | Packaging on hand >= 6 weeks of forecast [TODO method]; capacity limit agreed in writing |
| Hiring decision | If monthly orders exceed what one person can pack and answer in the time promised, recruit Fulfilment Coordinator (hiring-plan wave 3). Trigger value TODO | Trigger agreed (orders/week), not a calendar date |
| Second region test | Only if owner approves a new free-shipping region: rate table, customs notes, checkout test per region (only Latvia is checkout-tested today) | Each active region has a tested checkout and a sourced rate |
| Carrier SLA review | Review incidents (lost, late), claim outcomes | Lost parcels per 100 orders: track; target TODO |

Budget ask: peak packaging pre-buy [TODO]; temporary packing help for Nov-Dec [TODO]; second carrier account if
chosen [TODO].

### Q4 2027 (Oct - Dec): peak season, second edition

| Goals | Key initiatives | KPIs |
|---|---|---|
| Carrier-backed Christmas cutoffs published by 1 Oct | Table per region using carrier-stated last posting dates (dated sources). Banner and per-country dates on site (owner/e-commerce publish) | 100% of regions with a sourced cutoff; on-time dispatch >= 97% |
| Peak operations | Daily dispatch file, exception sweep every business day in Dec, same-day customer notice drafts | Errors <= 1.5%; no order older than the promised dispatch time |
| Returns | Pre-agreed December return handling, clear return address and instructions on the packing slip | 100% in log; refunds within statute |
| Annual review | 2028 plan input: cost/order trend, carrier performance, return rates by SKU | Review delivered by 15 Jan 2028 |

Budget ask: seasonal packing support [TODO]; express shipping rates for late gift orders [TODO, only if offered].

## 4. Dependencies on other departments

| Department (agent) | What I need | What I give |
|---|---|---|
| Production (`aw-production`) | Weekly `capacity-YYYY-Www.md` with made-to-order due dates; confirmed physical stock; supplier fibre evidence for labels; QC log | Defect and return-reason clusters (QUALITY, SIZE_*); errors per SKU |
| E-commerce / CRO | Publish delivery ranges, cutoff banner and returns text once owner approves; fix variant photos and sizes; PayPal; fulfilment email check | Verified transit data; wording proposals; return-reason feedback for PDPs |
| CX | Customer case hand-offs with order number; reply-time rule | Dates, status, draft replies for owner; return deadlines |
| Finance | Stripe/PayPal fee schedule (actual); accountant view on VAT/OSS and customs | Actual shipping and packaging cost per order; cost per region |
| Growth / Partnerships / Content | Campaign calendar early; no promotion of non-GREEN SKUs | Delivery cutoffs, shipping facts for ads and gift guides; "last order date" messaging |
| GM (`aw-head-of-ecommerce`) | Weekly review slot; decisions from section 5 | Weekly ops KPI file; exceptions list |
| Gift guides and markets (owner) | Dates and stall plan | Pack/stock logistics for markets (a stall competes with online orders for the same stock) |

Note: `markets-and-gift-guides.md` pitch drafts promise "free shipping" and "returns within 14 days". They should
not go out before the delivery times and returns wording above are settled.

## 5. Risks and owner decisions

### Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Free shipping in US/Rest of World with no rates known and only Latvia tested | Margin loss; untested checkout | Source rates first; test checkout for US and one EU country. Owner decides regions |
| Published ranges not backed by carriers (2-5 + 7-20) | Late deliveries, disputes, wrong Christmas promise | Real test parcels; carrier-stated times; adjust ranges |
| Returns terms conflict with statute and with Merchant Center policy | Legal exposure; inconsistent refunds | Adviser review; until then replies follow the statutory floor per case, owner approves each |
| Stock placeholders (360 / 220) | Oversell, missed dates | Owner confirms physical stock; Production's capacity file gates promotion |
| Missing variant photos | Wrong colour received, returns | Photos before promoting those SKUs |
| Customs/duties unclear for non-EU | Surprise charges, refusals | Adviser/carrier confirm; no customs statements until then |
| One person doing packing, support and production at peak | Missed dispatch | Capacity cap in the production file; temporary help budget; fall back to gift cards |
| Cash tied up in returns during Q1 | Cash strain | Monthly returns review with Finance |

### Owner decisions needed (I cannot decide any of these)

| # | Decision | Needed by |
|---|---|---|
| 1 | Which carrier(s) and services per region (carrier choice and contract are yours) | 28 Oct |
| 2 | Promised dispatch time to show publicly (FAQ says up to 5 business days for made-to-order; Merchant Center says 2-5) | 24 Oct |
| 3 | Keep free shipping for Latvia, US and Rest of World? Offer paid express for late Christmas orders? | 31 Oct |
| 4 | Return address, and who pays return postage (Merchant Center says customer; live page unclear) | 30 Oct |
| 5 | Send returns terms to the EU consumer-law adviser (README s11); approve wording | 3 Nov to adviser |
| 6 | Physical stock truth and made-to-order lead time per SKU | 24 Oct |
| 7 | Approve publishing the Christmas cutoff table and the per-country banner | after carrier dates confirmed |
| 8 | Packaging style and spend (branded supplies are your approval) | 30 Oct |
| 9 | Book a Christmas market? (consumes stock and your time) | by market deadlines in `markets-and-gift-guides.md` |
| 10 | Hiring trigger for a Fulfilment Coordinator (orders per week) | Q3 2027 |

## TODO / missing data

- Carriers used today and any account numbers; public price lists per region with date (`carrier-rates.md`)
- Parcel weights and sizes per SKU; packaging cost per pack
- Return address; return postage rule; customs/HS codes; duties wording per country
- Handling minutes per garment, yarn, supplier lead times (Production owns)
- Carrier last-posting dates for Christmas 2026 and 2027; Latvian public holidays for the cutoff table
- Whether Squarespace fulfilment email sends tracking; whether a parcel-locker option is wanted
- Baseline week in `kpi-weekly.csv`; real order volume to replace the conditional targets
- All 2027 budget figures (every "TODO" above)
