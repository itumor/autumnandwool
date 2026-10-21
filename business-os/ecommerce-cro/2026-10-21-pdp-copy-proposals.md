# PDP copy proposals — 2026-10-21 — DRAFT for owner approval

Owner: aw-ecommerce-cro. Tasks CRO-06 (shared delivery line), CRO-09, CRO-10 (copy half), CRO-21 (unfreeze request).
Product data is frozen: nothing here is applied. Bulk-paste version: `2026-10-21-pdp-copy-proposals.csv`.
Facts only from the live PDP (WebFetch 21 Oct), `products_Oct-17_10-46-00PM.csv`, `build_google_feed.py` `D`,
`llms.txt`, `/shipping-returns`. Unknown = `[OWNER: confirm]`. `CLAIM-CHECK` = keep only with evidence (G8, 31 Oct).
Voice: aw-brand-voice (calm, specific, no hype, no exclamation marks).

## 0. Shared lines (same wording on every visible PDP)

### Delivery + returns line (CRO-06)
- Free shipping. In-stock items ship from Riga within 2–5 working days. 14-day returns.   (current: on 5 of 6 PDPs fetched 21 Oct, missing on the raglan cardigan; other 16 not checked)
+ Free shipping to eligible destinations. In-stock items leave Riga in 2–5 working days; delivery takes about
+ 5–10 working days in Europe and 7–20 days to the US, Canada and Australia. 14-day returns, see Shipping & Returns.

Why: shoppers (gift buyers especially) need the arrival time, not only dispatch. The ranges are the ones already
published on `/shipping-returns` and in `llms.txt`, so this adds no new promise (ruling C8). OPS must reconcile with
the Merchant Center service ("4–10 business days", handbook s5.4) before the line goes live.
Made-to-order variant (only on PDPs with made-to-order colours/sizes):
+ Made to order: ships from Riga within [OWNER/PRD: confirm working days], then the delivery times above.

### Colour-selection line (every PDP with a colour selector; ATC no-ops without a selection)
+ Choose your colour below before adding to cart.

### Photo honesty line (only until each colour has its own photo)
+ Photos show [colour]. Other colours are the same knit and shape. [OWNER: confirm true for every colour]

### Etsy proof (only if owner approves placement, decision 17; wording per ruling C1)
+ 4.9 stars, 1,400+ reviews on Etsy (Mareshop). Reviews are of the Etsy shop, not this product page.

---

## 1. Merino Wool Raglan Cardigan (691050bcb0c4a7226c535650, /shop/p/p/black-merino-wool-cardigan-100-merino-wool-raglan-sweater-minimalist-knitwear-sustainable-handmade-womens-cardigan-1)
Fact sheet: fibre 100% merino wool | fit relaxed, slightly oversized, one size | width 61, front length 67, sleeve
from neck 82, sleeve from armpit 49, collar 4 cm | colours Black, Brown, Blue | price EUR 160 | images: Black
gallery, Brown = image_10, Blue none | gaps: Brown/Blue stock vs made-to-order (export: stock 2 each; PDP: "to
order"), lead time, model height/size, Blue photo, returns rule for made-to-order.

### Title
No change: "Merino Wool Raglan Cardigan" (= H1 = feed title).

### Description (diff)
- A relaxed raglan cardigan in 100% merino wool, hand-knitted in Riga.
- Available in three colours: Black (shown in the photos), Brown and Blue.
- Brown and Blue are hand-knitted to order in the same raglan style and fit — your cardigan follows the same knit
- pattern and measurements, in the colour you choose.
+ A relaxed raglan cardigan in 100% merino wool. Slightly oversized, so it sits easily over a shirt or a fine knit,
+ and it can be worn open or buttoned.
+ Colours: Black, Brown and Blue. Choose your colour below before adding to cart. Photos show Black [update once
+ Brown and Blue photos are added]; Brown and Blue are the same pattern and measurements.
+ [IF made to order — OWNER: confirm] Brown and Blue are made to order and ship within [OWNER/PRD: X] working days.
+ Knitted on a manually operated knitting machine and hand-sewn in Latvia.   CLAIM-CHECK
(DETAILS, MEASUREMENTS and CARE blocks: keep as live; add the model line when known.)
+ Fit: relaxed, slightly oversized, one size. Model is [OWNER: confirm height] cm.
+ [shared delivery line]

### SEO title / meta description
- Merino Wool Raglan Cardigan — Black, Brown or Blue | Autumn & Wool   (66 chars)
+ Merino Raglan Cardigan, Black, Brown or Blue | Autumn & Wool   (60)
+ Meta (152): Relaxed raglan cardigan in 100% merino wool, one size, slightly oversized. Black, Brown or Blue. Free
+ shipping to eligible destinations, 14-day returns.

CLAIM-CHECK: "hand-sewn in Latvia" (origin evidence, G8). Removed: "hand-knitted" (banned for machine pieces).
OWNER: Brown/Blue in stock or made to order? Lead time? Do made-to-order colours keep the 14-day return (Shipping &
Returns currently excludes them; adviser G9)? Model height?

---

## 2. Rib-Knit Beanie — Unisex (69105690dc1bc40ece1f4561, /shop/p/p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1)
Fact sheet: fibre 100% extra-fine merino, Italian-spun (CLAIM-CHECK both qualifiers) | one size, medium-thick rib,
gentle stretch, fits 54–58 cm heads | fold-over cuff, smooth forehead band | colours Black, Brown, Navy, Blue,
Gray, Light grey, Beige, Camel, Bordeaux, Pink, Melange grey | EUR 45 | kraft gift packaging | gaps: photo per
colour (10 missing), beanie height in cm (folded/unfolded), real stock (20 per colour looks like a placeholder).

### Title
- Rib-Knit Beanie — Unisex
+ Rib-Knit Merino Beanie — Unisex   (matches feed title and llms.txt; adds the fibre shoppers search for)

### Description (diff)
- Unisex rib-knit beanie with a fold-over cuff. A smooth, straight knit at the forehead means it won't press or
- leave lines. Suits short or long hair. Available in 11 colours.
+ A unisex merino beanie in a medium-thick rib with a fold-over cuff. The forehead band is knitted smooth and
+ straight, so it does not press or leave a line. Suits short or long hair.
+ Colours (11): Black, Brown, Navy, Blue, Gray, Light grey, Beige, Camel, Bordeaux, Pink, Melange grey. Choose your
+ colour below before adding to cart. [Photo honesty line until per-colour photos exist]
+ Size: one size with gentle stretch, fits 54–58 cm heads. Height [OWNER: confirm cm, unfolded / folded].
(Material, packaging, care: keep live wording; material line stays CLAIM-CHECK.)

### SEO title / meta description
+ Rib-Knit Merino Beanie, Unisex, 11 Colours | Autumn & Wool   (59)
+ Meta (148): Unisex rib-knit beanie in 100% merino wool with a fold-over cuff. One size, fits 54–58 cm heads. 11
+ colours. Free shipping to eligible destinations.

CLAIM-CHECK: "extra-fine", "Italian-spun yarn" (supplier spec sheet, decision 34). OWNER: height in cm; which
colours physically exist today.

---

## 3. Merino Wool Hat & Scarf Set (69105624c6bfa9183a014d2a, /shop/p/p/merino-wool-hat-scarf-set-extra-fine-rib-knit-soft-on-skin-warm-not-bulky-unisex-gift)
Fact sheet: fibre as beanie (CLAIM-CHECK) | beanie one size 54–58 cm; scarf approx. 190 x 36 cm | colours Black,
Gray, Brown | EUR 110 | kraft gift packaging | care incl. store folded | gaps: Gray and Brown photos; whether hat and
scarf are always the same colour.

### Title
No change: "Merino Wool Hat & Scarf Set".

### Description (diff, point edits)
+ (insert after first paragraph) Colours: Black, Gray or Brown; the hat and scarf come in the same colour
+ [OWNER: confirm]. Choose your colour below before adding to cart. [Photo honesty line]
+ (insert before care) A practical gift: it ships in kraft packaging, so it can go straight under the tree.
(Keep the rest as live. Do not add "free gift wrap" or a gift note: not offered, cost unknown, CRO-20.)

### SEO title / meta description
+ Merino Wool Hat & Scarf Set, 3 Colours | Autumn & Wool   (53)
+ Meta (141): Matching rib-knit beanie and scarf in 100% merino wool. Beanie fits 54–58 cm heads, scarf approx.
+ 190 × 36 cm. Ships in kraft gift packaging.

CLAIM-CHECK: "extra-fine", "Italian-spun". OWNER: same-colour pair? Gray/Brown photos.

---

## 4. Long Wool Cardigan — Women's Shawl Collar (69105a2ab0c4a7226c53591f, /shop/p/p/wool-cardigan-warm-cardigan-organic-wool-wrap-winter-sweater-cardigan-women-cardigan-sweater-minimalist-style-sweater)
Fact sheet: fibre 100% pure new wool | fit straight, relaxed; model 171 cm wears M | sizes S, M, L, XL | knee
length, open front, dropped shoulders, draped shawl collar | EUR 145 | gaps: garment measurements per size, care
block, difference vs the twin "100% Wool Long Shawl Cardigan – Warm Knit" (also EUR 145, also S–XL).

### Title
No change (H1 = feed). Note for SEO/owner: two near-identical shawl cardigans confuse shoppers; distinct opening lines
below; merge/hide is an owner decision (decision 20).

### Description (diff)
+ (new opening line) Our longest cardigan: knee length, open front and a soft shawl collar that drapes rather than
+ folds. Wear it as a light coat indoors or over a dress. [OWNER: confirm this is the knee-length one of the two]
(Keep the live structure lines and model line.)
+ MEASUREMENTS (garment laid flat, cm) — see Size Guide
+ S: width [OWNER] · length [OWNER] · sleeve from neck [OWNER]
+ M: width [OWNER] · length [OWNER] · sleeve from neck [OWNER]
+ L: width [OWNER] · length [OWNER] · sleeve from neck [OWNER]
+ XL: width [OWNER] · length [OWNER] · sleeve from neck [OWNER]
+ CARE: Hand wash cold with a wool-safe detergent. Do not tumble dry. Lay flat to dry.   (llms.txt care section)

### SEO title / meta description
- Long Wool Cardigan with Shawl Collar, 100% Wool | Autumn & Wool   (65)
+ Long Wool Shawl-Collar Cardigan, Knee Length | Autumn & Wool   (60)
+ Meta (155): Knee-length open-front cardigan in 100% pure new wool with a draped shawl collar. Sizes S–XL, relaxed
+ straight fit. Free shipping to eligible destinations.

CLAIM-CHECK: "hand-sewn in Latvia" (live). OWNER: measure one of each size (4 numbers x 4 sizes).

---

## 5. Merino Wool Raglan Sweater — Dusty Pink (69105bd9b0c4a7226c5359f0, /shop/p/p/hand-knitted-merino-wool-raglan-sweater-dusty-pink-oversized-jumper)
Fact sheet: fibre "merino wool" (% missing) | oversized, roomy | S/M: width 54, front 62, back 66, sleeve from neck
75 cm; L/XL: 60 / 63 / 69 / 80 cm | dusty pink only | EUR 155 | gaps: fibre %, model height/size, how S/M and L/XL
map to the size guide (EU 36–42).

### Title
- Merino Wool Raglan Sweater — Dusty Pink Oversized Jumper   (55, keyword string, QA s5)
+ Oversized Merino Wool Raglan Sweater — Dusty Pink   (49; leads with the GSC query "oversized merino wool sweater")
Feed title must change in the same upload (feed fix list row F-07); keep the URL slug (no redirect plan).

### Description (diff, point edits)
- Material: merino wool
+ Material: [OWNER: confirm % from label] merino wool
+ Fit: oversized and roomy, easy to layer. S/M fits about EU [OWNER: confirm] and L/XL about EU [OWNER: confirm].
+ Model is [OWNER: confirm] cm and wears [OWNER: confirm].
(Keep the measurement and care blocks as live: they are the site's best example.)

### SEO title / meta description
- Merino Raglan Sweater, Dusty Pink | Autumn & Wool
+ Oversized Merino Wool Sweater, Dusty Pink | Autumn & Wool   (57)
+ Meta (141): Oversized merino wool sweater in dusty pink with raglan sleeves and a curved hem. Sizes S/M and L/XL.
+ Free shipping to eligible destinations.

CLAIM-CHECK: "hand-sewn in Latvia". OWNER: fibre %, size mapping, model.

---

## 6. Scoped unfreeze request (CRO-21, master plan decision 19, due 31 Oct)

Ask: allow these 5 PDPs (or the GM's final 5) to change in one batch, applied by the owner from the CSV:
title (beanie, dusty pink), description, SEO title, meta description, and variant images when photos arrive. Not
requested: prices, variants, stock, slugs. Alternative: keep proposals-only; then every item above stays a diff
and the 5 Dec "applied" target in the CRO plan cannot be met.

## 7. Self-check
- Every factual line traces to the live PDP, the export, the feed script or llms.txt. Unknowns are `[OWNER]`.
- Title = H1 = feed title after change: beanie and dusty pink need the feed title edited in the same pass.
- No banned claim added; "hand-knitted" removed; "handmade" not used; Etsy proof only as ruling C1.
- Lengths: SEO titles ≤ 60, metas ≤ 155 (counted by hand; recount in Squarespace field counter).
- Colour names copied exactly from the variant selectors.
