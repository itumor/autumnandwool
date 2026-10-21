# E-commerce & CRO plan, Q4 2026 and 2027 — DRAFT

Owner of plan: `aw-ecommerce-cro`. Written 2026-10-21. Status: DRAFT for owner/GM approval. Nothing here is applied.
Hard rules in force: product data frozen (proposals as CSV/markdown diff only), no live edits, no Code Injection or
`<script>` unless labelled `NEEDS PLAN UPGRADE`, overlay fix CSS kept, no split tests at current traffic, no
invented numbers (unknown = `TODO` or `[OWNER: confirm]`).

KPI moved by this plan: conversion rate (orders / sessions), checkout completion, AOV, plus product-page quality
and feed approval (enablers of revenue).

---

## 1. Starting point (facts, 21 Oct 2026)

| Area | Fact | Source |
|---|---|---|
| Orders | Zero real direct orders to date. 2 test orders (#00003 desktop, #00004 mobile) placed and refunded 18-19 Oct; Stripe card chain proven | `business-os/README.md` s2; `weekly-measurement-report-2026-10-19.md` |
| Traffic | 62 visits / 30 days (17 Oct), bounce 94.34%; 2 visits from Google, 0 from Instagram/Pinterest | `weekly-measurement-report-2026-10-19.md`; `zero-sales-diagnosis-2026-10-18.md` s1 |
| Search | GSC 90 d: 11 clicks, 388 impressions, CTR 2.8%, avg pos 14.1; 37 URLs discovered, 11 indexed | `incident-veil-blocker-2026-10-19.md` round 6 |
| Root-cause fix | Invisible overlay click-trap fixed 19 Oct via Custom CSS (`.sqs-widgets-confirmation-overlay`, `.sqs-widgets-confirmation` `pointer-events:none`). Must never be removed | `incident-veil-blocker-2026-10-19.md` |
| Measurement | GA4 `G-7TV8PK060Z` pageviews only. No add_to_cart / begin_checkout / purchase events (Code Injection plan-gated). Orders counted from Squarespace Orders. `kpi-weekly.csv` has a header row and no data yet | `weekly-measurement-report-2026-10-19.md`; `business-os/kpi-weekly.csv` |
| Payments | Stripe connected (card + Google Pay seen), test mode off. PayPal NOT connected (owner credentials) | `owner-action-pack-2026-10-19.md` B1; `implementation-report.md` |
| Merchant Center | 98 rows uploaded 19 Oct 01:31 EET; 0 not approved, 98 under review; checkpoint 21 Oct. Shipping set: Latvia + EU-19 + UK/NO/CH free 4-10 d | `incident-veil-blocker-2026-10-19.md` |
| Feed risk | 48 of 98 rows share one image across colours (beanie 11, turtleneck 36, hat and scarf 3, cardigan blue 1). Generator hard-codes `availability=in_stock`; 13 items were out of stock per handbook | `weekly-measurement-report-2026-10-19.md`; `owner-action-pack-2026-10-19.md` A; `business-os/ai-team.md` owner decision 3 |
| Variant photos | Not one variant has its own image (`variant.imageIds=[]`); owner photography pending (about 51 photos in the pack) | `incident-veil-blocker-2026-10-19.md` round 8 |
| PDP gaps | No size selector on garments checked; measurements format inconsistent (vest cm only, cardigan cm + in); vest title vs H1 mismatch; image alt = file names; delivery time not shown on PDP | `QA-REPORT.md` s2, s4; `zero-sales-diagnosis-2026-10-18.md` A4 |
| Copy conflicts | Returns wording "unused" vs "unwashed"; "handmade"/"sustainable" claims on Shipping & Returns without supplier evidence; reply time 24 h (Contact) vs 1-2 business days (welcome email) | `QA-REPORT.md` s5; `business-os/README.md` s7; `business-os/ai-team.md` decision 5 |
| Plan limits | No Code Injection; Discounts and promotional pop-up locked; Google sync of feed manual | `implementation-report.md` (feed note 1b, row 4) |
| Shop page | H1 missing, "No results found" message shown with products, heavy page (872 KB, 203 img), category pages have no meta/H1 | `QA-REPORT.md`; `squarespace-implementation-proposal.md` SHOP; `GROWTH-PLAN-100-IDEAS.md` S4, S7 |
| Economics | `sku-economics.csv` cost columns blank; no minimum contribution per order agreed. Prices seen: cardigan EUR 145 / 160, beanie EUR 45, vest EUR 126, set EUR 110 | `business-os/sku-economics.csv`; `squarespace-implementation-proposal.md` |
| Priority PDPs | The 5 priority products are not yet chosen (GM decision, README s12) | `business-os/README.md` s12 |

Honest reading: this is a traffic problem first, conversion second (`zero-sales-diagnosis-2026-10-18.md` s1). My job
in Q4 is to make sure every visitor who arrives can find, understand, and pay, and to make the funnel measurable
without a script.

---

## 2. Q4 2026 (21 Oct - 31 Dec): peak gift season

### Goals
1. Store is buyable end to end on phone and desktop with two payment routes, and a real (non-test) order completes without a soft-lock.
2. 5 priority PDPs perfected (audit + copy proposal each) and applied by owner, from the GM's list.
3. Merchant Center free listings live for SKUs with correct variant images.
4. Weekly before/after log running, so every change is attributable.
5. Gift-buyer path complete: delivery estimate and last-order dates visible before checkout.

### KPIs and targets
Traffic is 62 visits/30 d, so conversion-rate targets are not meaningful yet. Targets below are process/quality
gates (checkable) plus provisional outcome targets that unlock only once traffic exists.

| KPI | Baseline (source) | Target by 31 Dec | Measured from |
|---|---|---|---|
| Merchant Center approved items | 0 approved, 98 under review | Approved > 0 by 28 Oct; approved count for all rows with a correct variant image = 100% of those rows (target set after 21 Oct diagnostics) | MC Diagnostics screenshot (owner) |
| Feed rows with image-mismatch risk | 48 of 98 | 0 (via owner photos, or trimmed rows if photos not supplied by 14 Nov, owner decision) | feed QA report |
| Priority PDPs perfected | 0 of 5 | 5 of 5 audited and proposals delivered by 14 Nov; applied by 5 Dec (owner-dependent) | `business-os/cro/`, `business-os/proposals/` |
| PayPal live | Not connected | Connected and one PayPal test order + refund passed by 7 Nov (owner-dependent) | test-order checklist |
| Real test-order checklist runs | 2 (Stripe, 18-19 Oct) | 2 more: November (card + PayPal, desktop + phone), December (card, phone), each with refund | `business-os/cro/<date>-test-order-checklist.md` |
| Delivery time visible on all visible PDPs | 0 of 22 | 22 of 22 (one shared line) | PDP audit |
| Size/fit + cm measurements on priority PDPs | inconsistent | 5 of 5 same format, cm (inches optional) | PDP audit |
| Add-to-cart dead clicks (overlay) | fixed 19 Oct | 0 reproduced in weekly 390px smoke | weekly note |
| Orders (site) | 0 real | First real order: TODO target, depends on traffic from Marketing; log every week | Squarespace Orders |
| Conversion rate | n/a (0 orders) | Provisional: report weekly; set a numeric target after 4 weeks with enough sessions [OWNER/GM: confirm threshold]. Diagnosis benchmark for a good store is 1-3% of visits (`zero-sales-diagnosis-2026-10-18.md` s1, benchmark not our data) | `kpi-weekly.csv` |
| Checkout completion (cart to order) | unknown | Baseline only: owner shares Squarespace abandoned-cart count weekly | owner screenshot |
| AOV | unknown | Baseline only until 5+ real orders; no target | Squarespace Orders |

### Weekly actions (every Friday, before Monday review)
- Write `business-os/cro/<date>-weekly.md`: changes owner applied, before/after numbers, next 3 proposals, experiment log rows.
- Fill `kpi-weekly.csv` conversion/AOV columns from Squarespace Orders + GA4 sessions; propose `notes` text with change dates.
- 390px smoke check of home, shop, one PDP, cart via WebFetch plus owner screenshot (WebFetch cannot see JS/overlays: mark UNVERIFIED).
- Retest the beanie and cardigan "Add To Cart without colour" path after any CSS change (owner screenshot).
- One change per page per 2 weeks (sequential before/after, no split tests).

### Monthly actions
- Nov and Dec: test-order and refund checklist for owner (desktop + phone; card; PayPal once live).
- After any feed change: feed QA report + proposal TSV in `business-os/feed/` (never run the generator, never overwrite the live TSV).
- Re-verify the overlay CSS is still in Custom CSS (screenshot request).

### Dated plan
| When | Action | Layer | Owner applies |
|---|---|---|---|
| 21-23 Oct | Read MC diagnostics (owner screenshot); feed QA report incl. availability vs stock check | feed TSV / account | yes |
| 21-28 Oct | PayPal connect; one PayPal + card test order, refund | native setting | yes |
| 24 Oct | First data row in `kpi-weekly.csv` (week start 19 Oct baseline, 2 test orders excluded) | sheet | yes |
| By 28 Oct | Delivery-time line per zone in shipping settings + one shared PDP line proposal | native setting + copy | yes |
| By 31 Oct | Priority PDP 1-2 audits and copy diffs (cardigan, beanie unless GM picks otherwise) | copy proposal | yes |
| By 7 Nov | PDP 3-5 audits; size/fit and measurement format proposal (one table for all) | copy proposal | yes |
| By 7 Nov | November test-order checklist run | owner task | yes |
| By 14 Nov | Variant photos bound, then regenerated feed QA and re-upload checklist; else trim decision | asset / feed | yes |
| By 14 Nov | Christmas last-order-date banner proposal per country; carrier cut-offs `[OWNER: confirm]` | copy / native | yes |
| By 21 Nov | Cart reassurance line once near Checkout (CSS or native text); shop page H1 and "No results found" fix proposals | CSS / native | yes |
| By 5 Dec | Apply all approved PDP changes; freeze site changes from 12 Dec except defects, so Christmas results are readable | all | yes |
| 12-24 Dec | Defect-watch only: daily owner glance at Orders and cart; weekly smoke | monitoring | no |
| 28-31 Dec | Q4 retrospective with before/after table; December test order | note | yes |

Gift items proposed (copy / native, owner decides, `aw-unit-economics` check before any cost): gift-wrap and
handwritten-note option (cost TODO), "no prices" gift receipt wording. Discounts and sign-up pop-up are plan-locked, so
no discount-based tactic this quarter.

---

## 3. 2027 by quarter

All targets after Q4 are TODO until Q4 produces a real conversion baseline (README s10 rule: set revenue targets only
after conversion, margin and CAC are measured). Budget lines are asks, not approved; Squarespace and tool prices must be
verified on current pricing pages before any decision.

### Q1 2027 (Jan-Mar): measure and fix
- Goals: funnel measurable past pageviews; all 22 visible PDPs on one template; Merchant Center steady-state.
- KPIs: share of visible PDPs passing the 6-step funnel checklist (baseline: 0 of 22 audited; target 100% of visible PDPs); feed rows in disapproval = 0 `[target TODO after MC history]`; monthly test order passed 3 of 3; conversion rate and AOV recorded for every week.
- Initiatives:
  1. Plan upgrade decision, evaluated against the cost of blind spend (`business-os/README.md` s8): unlocks GA4 ecommerce events, Clarity, Discounts, pop-up, auto Google sync. `NEEDS PLAN UPGRADE`.
  2. Roll out the perfected PDP template to the remaining visible PDPs, 2 weeks per batch.
  3. Category landing pages (80-150 words, own meta, H1) with `aw-ecommerce-seo`; thin categories merge/hide decision.
  4. Colour twin duplicate copy (side-slit, stand-collar) given distinct opening lines.
  5. Replace the contact form `mailto:` workaround with a native Squarespace Form block (`incident-veil-blocker-2026-10-19.md`).
  6. Returns/legal wording adopted after EU adviser review (README s11).
- Budget ask: Squarespace plan difference TODO (verify pricing); photography per colour (TODO, owner/Creative); test-order refund float TODO (small, order value returned).

### Q2 2027 (Apr-Jun): conversion under real traffic
- Goals: first reliable conversion read; PDP and cart improvements driven by data instead of audit alone.
- KPIs: conversion rate (target TODO after Q1 baseline); checkout completion from abandoned-cart counts (target TODO); AOV (target TODO, after 10+ real orders); cart-to-order drop-off step identified.
- Initiatives:
  1. If upgraded: GA4 ecommerce events live, funnel report per step; Clarity mobile recordings for one-week reviews. If not upgraded: continue sequential before/after with owner-supplied Squarespace screenshots.
  2. Bundles ("Pairs well with", sweater + beanie) and free-shipping threshold test, each only after `aw-unit-economics` (sku-economics.csv costed) and, for discounts, the plan feature. Prices unchanged unless owner approves.
  3. Spring/summer lightweight range PDPs (turtleneck lightweight, beanie transition) prepared with safe-to-promote list from Production.
  4. Feed refresh monthly; Pinterest catalog reuse only after variant photos verified.
- Budget ask: Clarity free; analytics setup time TODO; any bundle discount cost from `sku-economics.csv` (TODO).

### Q3 2027 (Jul-Sep): pre-season readiness
- Goals: site ready for autumn demand before the traffic arrives; reviews on site.
- KPIs: PDP pass rate stays 100%; on-site reviews collected: count TODO (target set with CX after first orders); mobile checkout completion vs desktop gap (target TODO); load time of Shop page (baseline 872 KB HTML, 203 img; target: paginate/limit, number TODO).
- Initiatives:
  1. Collect real on-site reviews (post-purchase email from CX) and consider rating markup only for genuine on-site reviews (`aw-ecommerce-seo`; review widget script = `NEEDS PLAN UPGRADE`).
  2. Shop page restructure (limit products per page, category entry points).
  3. Enable A/B only if a page reaches about 1,000 sessions/week (`aw-cro-audit`); otherwise stay sequential.
  4. Latvian/German key pages feasibility (native review required), only if EU traffic data supports it.
  5. Seasonal gift landing page and last-order-date logic prepared by end Sep.
- Budget ask: review tooling TODO; translation review TODO (native reviewer).

### Q4 2027 (Oct-Dec): peak season, run and measure
- Goals: repeat of Q4 2026 playbook with data; change freeze before peak.
- KPIs: conversion rate vs Q3 baseline (target TODO); AOV vs Q3 (TODO); cart abandonment (TODO); checkout defects in peak = 0; test orders monthly 3 of 3.
- Initiatives:
  1. Site-change freeze from mid-Nov except defects; December defect-watch.
  2. Gift flow (wrap, note, receipt, last-order dates) templated and reused.
  3. Post-peak retrospective with year-on-year before/after table.
  4. 2028 plan input: replatform question only if measured limits of Squarespace are blocking revenue (README s2: do not re-platform first).
- Budget ask: TODO after Q3 results.

Standing every quarter: 12 monthly test-order checklists across 2027, quarterly full funnel audit of all visible PDPs,
weekly note, monthly feed QA.

---

## 4. Dependencies on other departments

| Need | From | Why / when |
|---|---|---|
| 5 priority SKUs chosen | GM (`aw-head-of-ecommerce`) | Blocks PDP work order; needed 24 Oct |
| Costs for 22 visible SKUs, minimum contribution per order | Finance + Production + owner | Needed before any bundle, threshold, gift-wrap cost or discount (`aw-unit-economics`); BLOCKED until filled |
| Weekly capacity and safe-to-promote list; real stock truth (turtleneck 360, beanie 220 look like placeholders); lead times | Production | Stock, `availability` in feed, PDP lead-time line |
| Fibre %, garment measurements, colour list, care per priority SKU; claim evidence (handmade, made in Latvia/Riga) | Production + owner | PDP copy cannot be finished without; unknowns stay `[OWNER: confirm]` |
| Per-colour photos, photo briefs | Creative (`aw-product-photo-briefs`) + owner | Feed approval, variant images, PDP step 2 |
| Dispatch/carrier cut-offs, return address, packaging | Operations | Christmas last-order dates, delivery line |
| Reply-time standard, order email, review request, abandoned-cart email, newsletter | CX | PDP/Contact promise consistency; funnel steps 5-6 |
| UTM-tagged links in all profiles; traffic volume | Growth, SEO/Pinterest | Without sessions no conversion read; I do not raise ad spend (GM decides) |
| Query-to-page map, category copy, llms.txt sync | SEO (`aw-seo-marketplace`) | Shared PDP SEO fields; one target page per query |
| Returns/shipping legal wording | EU consumer-law adviser via owner | Cart/PDP delivery and returns lines, README s11 |
| Weekly KPI summary rows | Head of E-commerce / Finance | `kpi-weekly.csv` ownership split (orders, revenue) |

What others get from me: weekly note, PDP fact-gap lists (for Production), photo needs per colour (Creative), feed QA
(SEO), funnel-defect list (Ops/CX).

---

## 5. Risks and owner decisions

### Risks
| # | Risk | Likelihood / impact | Mitigation |
|---|---|---|---|
| 1 | Traffic stays near 62 visits/month, so no CRO result is readable | High / High | Report process gates; push traffic asks to Growth/SEO; never claim conversion lifts from fewer than a handful of orders |
| 2 | MC image-mismatch disapprovals on 48 rows | Medium / High | Owner photos by 14 Nov; fallback trim (accept lower reach) |
| 3 | Feed lists out-of-stock items as in_stock (generator hard-code) | Medium / High | Stock-vs-feed check each upload; proposal TSV with `out_of_stock`; owner uploads |
| 4 | Soft-lock regression if CSS is overwritten | Low / Critical | Check CSS present monthly; every CSS proposal repeats the two rules |
| 5 | Funnel stays blind without Code Injection | High / Medium | Upgrade decision in Q1; until then orders + abandoned-cart + owner screenshots |
| 6 | Unproven claims (handmade, sustainable, made in Latvia) on pages | Medium / High | Flag as `CLAIM-CHECK`, never add; owner evidence |
| 7 | Frozen product data blocks fixes (size selector, per-colour images, titles) | High / Medium | Ship as diffs; ask for a scoped unfreeze for the 5 priority PDPs |
| 8 | Peak-season change during December causes a defect | Medium / High | Freeze from 12 Dec (2026) |
| 9 | Owner is the single applier of every change; bottleneck | High / Medium | Batches of at most 15-minute tasks, ordered by ICE |
| 10 | Real phone check limited to 390px iframe (QA-REPORT s6) | Medium / Medium | Owner phone screenshots in each checklist |

### Decisions needed from owner
1. Connect PayPal now (credentials) and run the first PayPal test order. Needed by 7 Nov.
2. Scoped unfreeze of product data for the 5 priority PDPs (size selector/variants, per-colour images, titles, descriptions), or keep proposals-only. Needed by 31 Oct.
3. Photos: supply per-colour photos by 14 Nov, or approve trimming the 48 at-risk rows from the feed.
4. Squarespace plan upgrade yes/no (unlocks events, Discounts, pop-up, auto feed sync). Decide by end Nov with price verified; apply Q1 at latest.
5. One returns wording and one reply-time promise (24 h vs 1-2 business days); adviser review of Shipping & Returns.
6. Which Etsy review claim to show (1,400+ vs 1,500+) and whether verbatim Etsy quotes may appear on PDPs (labelled "Etsy review").
7. Vest: restock or hide; duplicate Beige Melange listing, one source of truth.
8. Christmas order deadlines per country and gift-wrap offer (needs Operations facts and cost).
9. Provenance and rights of the "ChatGPT Image" assets before ads or PDP use.
10. Confirm whether Etsy/Mareshop and the site both stay open this season (affects "move to site" messaging).

### Open questions
- Which 5 SKUs are priority (GM)? Do any have more than one colour (affects the photo ask)?
- Is the minimum acceptable contribution per order decided? (blocks threshold/bundle work)
- Weekly abandoned-cart count: can the owner share it from Squarespace each Friday?
