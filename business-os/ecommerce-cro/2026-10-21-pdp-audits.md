# CRO audit: 5 provisional priority PDPs — 2026-10-21 — DRAFT

Owner: aw-ecommerce-cro. Tasks CRO-07, CRO-08, CRO-10 (audit half). Nothing applied; product data frozen.
KPI moved: conversion rate (orders / sessions), checkout completion. Traffic is 62-64 visits / 30 days, so this is a
fix-forward audit, not a test.

Scope / traffic source / primary action
- Pages: 5 PDPs below + their cart path. Traffic: direct, Instagram bio UTM, Google free listings (pending approval).
- Primary action: Add To Cart, then checkout.
- Evidence: WebFetch of live pages on 2026-10-21 (text only: cannot see JS, variant images, overlays, CSS `content`
  lines), `products_Oct-17_10-46-00PM.csv`, `build_google_feed.py` `D` list, `QA-REPORT.md`, `PROJECT-HANDBOOK.md`,
  `implementation-report.md`.

## 0. Provisional priority set (CRO proposal to GM; GM/owner decides 24 Oct, master plan decision 2)

The 5 priority SKUs are not chosen yet. To avoid idle work I audited a working set picked on readiness (photo,
stock in 17 Oct export, measurement facts, gift-season fit). If the GM picks differently, the method and the
site-wide findings carry over; only the per-SKU copy needs redoing.

| # | Product (id) | Price | Stock (17 Oct export, may be placeholder) | Why in the set |
|---|---|---|---|---|
| 1 | Merino Wool Raglan Cardigan (691050bcb0c4a7226c535650) | EUR 160 | 2 per colour (Black/Brown/Blue) | Plan default; home bestseller; most defects already known |
| 2 | Rib-Knit Beanie — Unisex (69105690dc1bc40ece1f4561) | EUR 45 | 20 per colour x 11 (looks like placeholder, master plan decision 4) | Plan default; gift price point; 11 feed rows |
| 3 | Merino Wool Hat & Scarf Set (69105624c6bfa9183a014d2a) | EUR 110 | 2 per colour x 3 | Gift season; already "gift-ready" packaging copy |
| 4 | Long Wool Cardigan — Women's Shawl Collar (69105a2ab0c4a7226c53591f) | EUR 145 | 3 per size S-XL | Single colour (no variant-photo risk), sized, model height on page |
| 5 | Merino Wool Raglan Sweater — Dusty Pink (69105bd9b0c4a7226c5359f0) | EUR 155 | 3 per size S/M, L/XL | Best measurement block on site; maps GSC query "oversized merino wool sweater" (pos 27) |

Left out on purpose: Oversized Merino V-Neck Vest (stock 1-2, restock open, master plan decision 20), Merino
Turtleneck (12 colours x 3 sizes with 0 own photos; colours may not physically exist, decision 4). None of the 5 is
costed yet (`sku-economics.csv` blank), so CM2 is unknown; GM re-confirms on 4 Nov (ruling C5).

## 1. Funnel checklist (README s5) — PASS / FAIL / UNVERIFIED

| Step | Check | 1 Raglan cardigan | 2 Beanie | 3 Hat & scarf set | 4 Long shawl cardigan | 5 Dusty pink raglan |
|---|---|---|---|---|---|---|
| 1 Arrives | What it is + price + photo + one action above the fold at 390px | UNVERIFIED (no screenshot) | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED |
| 1 Arrives | H1 = feed title = `<title>` intent | PASS (H1 "Merino Wool Raglan Cardigan" = feed) | FAIL: H1 "Rib-Knit Beanie — Unisex", feed "Rib-Knit Merino Beanie — Unisex" | PASS | PASS (H1 = feed); `<title>` 65 chars | PASS H1 = feed, but H1 is a 55-char keyword string (QA s5) |
| 2 Explores | Photo per colour | FAIL: Blue has no photo; Brown only in gallery (image_10), gallery does not switch (QA s2) | FAIL: 1 photo set for 11 colours (owner pack A) | FAIL: Gray, Brown no photo | PASS (single colour) | PASS (single colour) |
| 2 Explores | Fibre % stated | PASS "100% merino wool" | PASS "100% extra-fine merino wool, Italian-spun yarn" (CLAIM-CHECK) | PASS (same CLAIM-CHECK) | PASS "100% pure new wool" | FAIL: "merino wool" without % |
| 2 Explores | Fit stated | PASS "Relaxed, slightly oversized (one size)" | PASS one size, 54-58 cm | PASS | PASS "Straight, relaxed. Model 171 cm wears M" | PASS "Oversized; roomy" (no model info) |
| 2 Explores | Garment cm measurements | PASS (cm + in) | PARTIAL: head range only, no height/depth | PARTIAL: scarf 190 x 36 cm, beanie head range | FAIL: none on page | PASS per size, cm |
| 2 Explores | Size-guide link near selector | PASS "Size Guide" text present (position UNVERIFIED) | PASS | PASS | PASS | PASS |
| 3 Decides | Review proof (Etsy, labelled) | FAIL/UNVERIFIED: none in fetched text (QA 18 Oct saw an Etsy line; may be CSS/JS) | same | same | same | same |
| 3 Decides | Delivery cost + time | FAIL: no delivery line on this PDP | PASS "Free shipping. In-stock items ship from Riga within 2-5 working days. 14-day returns." | PASS | PASS | PASS |
| 3 Decides | Delivery time to customer (not only dispatch) | FAIL | FAIL: dispatch only, no 5-10 / 7-20 days | FAIL | FAIL | FAIL |
| 3 Decides | Stock / lead time | FAIL: "Brown and Blue are hand-knitted to order", no lead time; export shows stock 2 each (contradiction) | n/a in stock | n/a | n/a | n/a |
| 3 Decides | Returns consistent with policy | FAIL: made-to-order colours are excluded from returns on `/shipping-returns`, PDP does not say so | PASS line | PASS | PASS | PASS |
| 3 Decides | Claims within brand rules | FAIL: "hand-knitted in Riga" (banned: machine pieces are never "hand-knitted", aw-brand-voice s3) | CLAIM-CHECK "extra-fine", "Italian-spun" | CLAIM-CHECK same | CLAIM-CHECK "hand-sewn in Latvia" (origin evidence open, G8) | CLAIM-CHECK same |
| 4 Checks out | Variant selected before ATC | UNVERIFIED: overlay fix makes hint appear (handbook s4); retest needed | UNVERIFIED (Black default-selected 18 Oct) | UNVERIFIED | Size select required: UNVERIFIED | Size select required: UNVERIFIED |
| 4 Checks out | Payment options | FAIL: card/Google Pay only, PayPal not connected | same | same | same | same |
| 5 Receives | Order email / tracking promise | UNVERIFIED (test orders 18-19 Oct, email content not on file) | same | same | same | same |
| 6 Returns | Care advice | PASS | PASS | PASS | FAIL: no care block | PASS |
| 6 Returns | Related products ("Pairs well with") | PASS (3 cardigans, no accessory) | PASS heading | PASS | PASS | PASS |

## 2. Findings (impact order: value → facts/photos → CTA/variant → trust/delivery → objections → friction)

| # | Step | Finding | Evidence | Layer | ICE (I/C/E) | Proposed fix |
|---|---|---|---|---|---|---|
| F1 | 3 | Raglan cardigan says "hand-knitted in Riga" and "Brown and Blue are hand-knitted to order" | Live PDP 21 Oct (WebFetch) | COPY PROPOSAL | 5/5/5 | Replace with the feed wording (CLAIM-CHECK) and drop "hand-knitted"; see copy proposals |
| F2 | 3 | Brown/Blue made to order with no lead time; Shipping & Returns excludes "custom or made-to-order pieces" from returns | PDP + `/shipping-returns` 21 Oct; FAQ: made-to-order "ship within the time listed on each product page" (no time listed) | COPY PROPOSAL + OWNER DECISION | 5/4/3 | Owner confirms: are Brown/Blue in stock (export: 2 each) or made to order? If MTO: state lead time on PDP and confirm returns apply (standard items made after order are not "personalised" — adviser, G9) |
| F3 | 3 | Raglan cardigan has no delivery/returns line; the other 4 do | WebFetch 21 Oct | COPY PROPOSAL | 4/5/5 | Add the shared line (copy proposals s0) |
| F4 | 3 | Delivery line gives dispatch only (2-5 working days), not delivery time per zone | 4 PDPs | COPY PROPOSAL | 4/4/5 | Extend shared line with the published ranges already on `/shipping-returns` (ruling C8: no new range) |
| F5 | 2 | Variant colours without own photo: cardigan Blue, beanie 10, set 2 | owner-action-pack A; QA s2 | ASSET | 5/5/2 | Owner phone photos per colour (C7 dates); until then add "Photos show Black" line |
| F6 | 1 | Beanie H1 lacks "Merino"; feed title has it (title = H1 = feed rule) | WebFetch vs `autumnandwool-google-feed.tsv` | COPY PROPOSAL | 3/5/5 | H1 "Rib-Knit Merino Beanie — Unisex" |
| F7 | 2 | Long shawl cardigan: no garment measurements, no care block | WebFetch; feed `D` has none | COPY PROPOSAL + OWNER (measure) | 4/5/3 | Owner measures S-XL flat (width, length, sleeve); add care block |
| F8 | 2 | Dusty pink raglan: fibre % missing ("merino wool") | WebFetch | OWNER confirm label | 3/5/4 | `[OWNER: confirm % from label]` |
| F9 | 3 | No Etsy proof line visible to fetch on any PDP | WebFetch; QA 18 Oct saw one | OWNER DECISION 17 / UNVERIFIED | 3/3/4 | Screenshot to confirm; if absent, one line per ruling C1 "4.9 stars, 1,400+ reviews on Etsy (Mareshop)" |
| F10 | 4 | No PayPal | `implementation-report.md` l.272 | NATIVE SETTING (owner) | 4/4/4 | Connect PayPal (decision 14, 31 Oct) |
| F11 | 1 | Dusty pink H1 and `<title>` tags (cardigan 66, long cardigan 65 chars) over 60 chars | WebFetch | COPY PROPOSAL | 2/5/5 | Shorter SEO titles in copy proposals |
| F12 | 4 | ATC without a colour/size: behaviour after overlay fix not re-checked since 19 Oct | handbook s4, memory note | OWNER screenshot | 4/3/4 | Include in Nov test-order checklist step B2 |
| F13 | 6 | Cardigan "Pairs well with" shows 3 other cardigans, no accessory (AOV) | WebFetch | NATIVE SETTING (related products) — UNVERIFIED if configurable on plan | 2/3/3 | If Squarespace allows manual related items, show beanie/set on cardigans; else leave |

## 3. Quick wins (owner can apply in < 15 min each, after approval)
1. F3 + F4: paste the shared delivery line on the raglan cardigan (and extend on the other 4). COPY.
2. F1: replace "hand-knitted" wording on the raglan cardigan. COPY.
3. F6: beanie H1 add "Merino". COPY.
4. F10: PayPal connect. NATIVE.

## 4. Proposals needing approval
- Copy diffs for all 5: `2026-10-21-pdp-copy-proposals.md` / `.csv`.
- Measurement format for all garments: `2026-10-21-size-fit-standard.md`.
- Photos: Creative + owner (C7 dates). Scoped unfreeze request: copy proposals file s6.

## 5. Experiment log entry
| Field | Value |
|---|---|
| ID | EXP-01 (fix-forward, sequential) |
| Hypothesis | Because the raglan cardigan PDP has no delivery line, no lead time for 2 of 3 colours and a banned "hand-knitted" claim, adding the shared delivery line + lead time + corrected making line on that page for all traffic will increase cardigan add-to-carts and orders |
| Metric | Cardigan orders (Squarespace Orders) and abandoned carts containing the cardigan (owner screenshot); qualitative: sizing/delivery emails |
| Dates | Start = day owner applies; read after 14 days; one change on this page per 2 weeks |
| Layer / rollback | COPY; rollback = paste the "current" text from the CSV |
| Result / decision | TODO. At ~64 visits/month expect no readable number; record qualitative evidence only |

## 6. Unverified — needs screenshot or owner check
- 390px above-the-fold view of all 5 PDPs (phone screenshot, owner).
- Whether an Etsy proof line and the "Need sizing help?" line render (CSS `content`, invisible to WebFetch).
- ATC with no colour/size selected on cardigan, beanie, set: what the shopper sees.
- Which colour the beanie and set main images show (assumed Black from owner pack A).
- Physical stock: beanie 20/colour and the 17 Oct counts generally (decision 4).
