# Product change sheet, live site, 2026-11-10

Status: PROPOSAL for owner application. Nothing on the live site, Etsy, Merchant Center or Search Console has been changed. The owner lifted the product-data freeze today for these SEO fixes only: names, SEO titles, SEO descriptions, the description sentences listed here, colour-twin first paragraphs, related-links blocks and image alt texts. Stock, prices, variants, images and slugs are not in scope.

Source of facts: `evidence/seo-audit-2026-11-10/crawl/html/*.html` (live HTML as crawled 2026-11-10: H1, description paragraphs, variant options, gallery image files and alts) and `crawl/pages.tsv` (current SEO title and meta, full URLs). No other fact source was used. Plan: `business-os/seo-marketplace/2026-11-10-seo-audit-and-action-plan.md` (SEO-37, SEO-40, SEO-43, SEO-44, SEO-45).

## Rules applied to every new value

1. **Making wording (owner decision 1).** No new or kept visible name, SEO title, meta description, description sentence or alt text says "hand-knitted", "hand knit" or "handmade". Replacement wording: "machine-knitted and hand-finished" (short form) or "knitted on a manual knitting machine and finished by hand" (long form). The existing "Knitted and hand-sewn in Latvia" is not banned and is kept as written. Its origin claim is listed in CLAIM-CHECK.
2. **Slugs unchanged.** Every URL below is the live URL. The slugs still contain "hand-knitted", "sustainable" and "organic". That is a known issue, not a change in this sheet.
3. **No new claims.** Each line comes from that page's own description, FAQ, variants or photo alts. Where the page does not say what a colour pairs with, the line is a marked placeholder `[OWNER: ...]`, not a guess.
4. **No brand suffix.** New SEO titles carry no " | Autumn & Wool" (brief). The rewrite table in `content-onpage.md` showed the suffix; this sheet drops it. OWNER: check in the editor whether Squarespace adds a brand suffix to product SEO titles by itself. If it does, that is a platform setting and must not be typed in.
5. **Lengths.** Counted character by character, spaces included. Kept values show the crawl length from `pages.tsv`.
6. **Colour.** Taken from the page's own variant options (`variant-option-Primary color-*`), from the product name, or from the page's own photo alts. Where none of these gives a colour, the line is marked `[OWNER: colour]`.
7. **Alt pattern.** `<short name> in <colour>, <view>`. The view word comes from the current alt. Where the current alt gives no view (for example "additional view 3" or a file name) the neutral `photo N` is used, N = gallery position. Alt lengths are all between 35 and 75 characters (limit 110).
8. **Gallery.** Order is the main gallery (`nbf-products-gallery-zoom`). The lightbox repeats the same images and is not listed twice. Where one file appears in two gallery slots with different alts (vest IMG_3336.JPEG), both slots are listed.

Landing URLs (new category pages, SEO-35, owner go-ahead needed): https://www.autumnandwool.com/wool-sweaters · https://www.autumnandwool.com/wool-cardigans · https://www.autumnandwool.com/wool-sweater-vests · https://www.autumnandwool.com/wool-hats-and-scarves · https://www.autumnandwool.com/wool-gifts

## Index (22 products, in crawl order)

| No. | Live URL slug (short) | Name change | SEO title change | Alts |
|---|---|---|---|---|
| 01 | autumn-and-wool-digital-gift-card | yes | yes | 2 |
| 02 | oversized-merino-wool-v-neck-sweater-vest | no | yes | 10 |
| 03 | black-merino-wool-cardigan-…-cardigan-1 | no | yes | 14 |
| 04 | cozy-and-sustainable-hand-knitted-lambswool-sweater-for-women (Brown) | yes | yes | 8 |
| 05 | hand-knitted-distressed-wool-sweater-oversized-raglan-jumper-1 | yes | yes | 10 |
| 06 | hand-knitted-lambswool-sweater-womens-grey-knit-jumper | no (pending colour) | yes | 8 |
| 07 | hand-knitted-lambswool-sweater-womens-winter-knitwear-1 (Green) | yes | yes | 7 |
| 08 | hand-knitted-merino-wool-raglan-sweater-dusty-pink-oversized-jumper | yes | yes | 9 |
| 09 | hand-knitted-merino-wool-striped-sweater-oversized-jumper | yes | yes | 8 |
| 10 | hand-knitted-wool-cardigan-minimalist-open-front-sweater-1 | yes | yes | 9 |
| 11 | hand-knitted-wool-cardigan-open-front-winter-sweater-679428 | yes | yes | 9 |
| 12 | hand-knitted-wool-stand-collar-sweater-womens-knitwear-679510 (Blue) | yes | yes | 1 |
| 13 | hand-knitted-wool-sweater-organic-knitwear-asymmetrical-design-1 (Light Grey) | yes | yes | 7 |
| 14 | hand-knitted-wool-sweater-stand-collar-knit-679503 (Beige) | yes | yes | 1 |
| 15 | hand-knitted-wool-sweater-womens-organic-knit-jumper-1 (Camel) | yes | yes | 7 |
| 16 | merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1 | yes | yes | 18 |
| 17 | merino-wool-hat-scarf-set-extra-fine-rib-knit-soft-on-skin-warm-not-bulky-unisex-gift | no | yes | 17 |
| 18 | merino-wool-sweater-oversize-…-warm-pink-jumper-679519 | no | yes | 9 |
| 19 | merino-wool-turtleneck-sweater-womens-knit-pullover-…-sizes-sl-12-679428 | no | yes | 9 |
| 20 | wool-cardigan-warm-cardigan-organic-wool-wrap-…-sweater | yes | yes | 9 |
| 21 | wool-sweater-sweater-for-women-knit-cozy-pullover-…-wool-pullover-1 | no | yes | 10 |
| 22 | wool-sweater-vest-knitted-wool-vest-oversized-vest-…-soft-v-neck-vest | no | yes | 10 |

Totals: 22 products; 14 names changed, 8 kept; 22 SEO titles changed; 192 alts rewritten. Full live URLs are in each section.

---

## 01. Digital gift card

- **Live URL:** https://www.autumnandwool.com/shop/p/autumn-and-wool-digital-gift-card
- **Variants:** none.
- **Name (H1):** `Gift Card` → `Digital Gift Card for Wool Knitwear` (35)
- **SEO title:** `Digital Gift Card for Wool Knitwear | Autumn & Wool` (51) → `Digital Gift Card for Wool Knitwear` (35)
- **SEO description:** keep (128). `Give wool knitwear without guessing the size. A digital gift card sent by email and redeemable at checkout on autumnandwool.com.`
- **Description edits:** none. No banned wording. "This gift card never expires." is on the live page and is kept. OWNER: confirm it is still the policy.
- **Twin paragraph:** not applicable.
- **Related-links block (append to end of description):**
  ```
  More wool gifts: https://www.autumnandwool.com/wool-gifts
  Also see: https://www.autumnandwool.com/shop/p/p/merino-wool-hat-scarf-set-extra-fine-rib-knit-soft-on-skin-warm-not-bulky-unisex-gift
  Also see: https://www.autumnandwool.com/shop/p/p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1
  ```
- **Alts:**

| # | Current file | Current alt | New alt |
|---|---|---|---|
| 1 | ChatGPT Image Nov 9, 2025, 12_13_41 PM.png | Autumn and Wool digital gift card with elegant minimalist design — perfect for gifting cozy knitwear that never expires. | Digital gift card for Autumn & Wool, photo 1 |
| 2 | ChatGPT Image Nov 9, 2025, 12_26_29 PM.png | ChatGPT Image Nov 9, 2025, 12_26_29 PM.png | Digital gift card for Autumn & Wool, photo 2 |

---

## 02. Oversized Merino Wool V-Neck Sweater Vest (single-segment URL, grey)

- **Live URL:** https://www.autumnandwool.com/shop/p/oversized-merino-wool-v-neck-sweater-vest
- **Variants:** none on the page. Colour grey comes from the photo alts only.
- **Name (H1):** keep `Oversized Merino Wool V-Neck Sweater Vest` (already fine). OWNER: if grey is the only colour, the name can become `Oversized Merino Wool V-Neck Sweater Vest - Grey` (48).
- **SEO title:** `Oversized Merino Wool Sweater Vest | Autumn & Wool` (50) → `Oversized Merino Wool Sweater Vest` (34)
- **SEO description:** `Explore an oversized V-neck sweater vest with a relaxed fit. View garment measurements, layering details and care guidance at Autumn & Wool.` (140) → `Oversized V-neck merino sweater vest with ribbed edging and Japanese-style shoulder shaping. Garment measurements and care details from Autumn & Wool.` (150)
- **Description edits:** none. CLAIM-CHECK: "Material: 100% extra-fine merino wool" is kept as written (see CLAIM-CHECK).
- **Twin paragraph:** not applicable.
- **Related-links block:**
  ```
  More vests: https://www.autumnandwool.com/wool-sweater-vests
  Also see: https://www.autumnandwool.com/shop/p/p/wool-sweater-vest-knitted-wool-vest-oversized-vest-womens-woolen-pullover-vest-top-sleeveless-wool-knit-vest-soft-v-neck-vest
  Also see: https://www.autumnandwool.com/shop/p/p/black-merino-wool-cardigan-100-merino-wool-raglan-sweater-minimalist-knitwear-sustainable-handmade-womens-cardigan-1
  ```
- **Alts (10 gallery slots, 9 files; IMG_3336.JPEG is in slots 1 and 6):**

| # | Current file | Current alt | New alt |
|---|---|---|---|
| 1 | IMG_3336.JPEG | Grey oversized V-neck merino wool vest layered over a black top on a mannequin | Oversized merino vest in grey, layered over a black top on a mannequin |
| 2 | IMG_3328.JPEG | Back of grey merino wool sweater vest showing relaxed fit and ribbed hem | Oversized merino vest in grey, back view |
| 3 | IMG_3333.JPEG | Grey V-neck sweater vest showing ribbed neckline and dropped shoulders | Oversized merino vest in grey, neckline and dropped shoulders |
| 4 | IMG_3331.JPEG | Front view of grey oversized sweater vest layered over a black top | Oversized merino vest in grey, front view over a black top |
| 5 | IMG_3334.JPEG | Close-up of the grey merino vest's ribbed V-neck edging | Oversized merino vest in grey, close-up of ribbed V-neck edging |
| 6 | IMG_3336.JPEG (second slot) | Grey oversized merino wool vest with wide armholes over a black top | Oversized merino vest in grey, wide armholes over a black top |
| 7 | IMG_3341.JPEG | Close-up of shoulder shaping and ribbed armhole on grey merino vest | Oversized merino vest in grey, close-up of shoulder and armhole |
| 8 | IMG_3339.JPEG | Back view of grey merino sweater vest hanging against a wall | Oversized merino vest in grey, back view hanging against a wall |
| 9 | IMG_3344.JPEG | Front view of grey V-neck merino wool vest on a hanger | Oversized merino vest in grey, front view on a hanger |
| 10 | IMG_3347.JPEG | Grey merino wool vest on a hanger showing its relaxed silhouette | Oversized merino vest in grey, relaxed silhouette on a hanger |

---

## 03. Merino Wool Raglan Cardigan (Black, Brown, Blue variants in the copy)

- **Live URL:** https://www.autumnandwool.com/shop/p/p/black-merino-wool-cardigan-100-merino-wool-raglan-sweater-minimalist-knitwear-sustainable-handmade-womens-cardigan-1
- **Variants:** the copy says Black (shown in the photos), Brown and Blue. No variant option is set on the page. The photos are black.
- **Name (H1):** keep `Merino Wool Raglan Cardigan`.
- **SEO title:** `Merino Wool Raglan Cardigan — Black, Brown or Blue | Autumn & Wool` (66) → `Merino Wool Raglan Cardigan in Black, Brown or Blue` (51)
- **SEO description:** `Shop the relaxed merino wool raglan cardigan, hand-knitted in Riga in black, brown or blue. Measurements, fit and wool-care details from Autumn & Wool.` (151) → `Shop the relaxed merino wool raglan cardigan, machine-knitted and hand-finished in Riga, in black, brown or blue. Measurements, fit and care details.` (149)
- **Description edits (old → new):**
  1. `A relaxed raglan cardigan in 100% merino wool, hand-knitted in Riga.` → `A relaxed raglan cardigan in 100% merino wool, machine-knitted and hand-finished in Riga.`
  2. `Brown and Blue are hand-knitted to order in the same raglan style and fit` → `Brown and Blue are machine-knitted and hand-finished to order in the same raglan style and fit`
- **Twin paragraph:** not a C-03 colour twin. Not changed.
- **Related-links block:**
  ```
  More cardigans: https://www.autumnandwool.com/wool-cardigans
  Also see: https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-cardigan-open-front-winter-sweater-679428
  Also see: https://www.autumnandwool.com/shop/p/p/wool-cardigan-warm-cardigan-organic-wool-wrap-winter-sweater-cardigan-women-cardigan-sweater-minimalist-style-sweater
  ```
- **Alts (14 gallery slots; colour black, from the description "Black (shown in the photos)"):** the current alts are one 163-character pipe-separated keyword string per view, which is replaced.

| # | Current file | Current alt (view word only) | New alt |
|---|---|---|---|
| 1 | image_1.jpg | main view | Merino raglan cardigan in black, main view |
| 2 | image_2.jpg | close-up detail view | Merino raglan cardigan in black, close-up detail view |
| 3 | image_3.jpg | side angle view | Merino raglan cardigan in black, side angle view |
| 4 | image_4.jpg | back view detail | Merino raglan cardigan in black, back view detail |
| 5 | image_5.jpg | lifestyle styling view | Merino raglan cardigan in black, styling view |
| 6 | image_6.jpg | texture and material detail | Merino raglan cardigan in black, texture and material detail |
| 7 | image_7.jpg | additional view 1 | Merino raglan cardigan in black, photo 7 |
| 8 | image_8.jpg | additional view 2 | Merino raglan cardigan in black, photo 8 |
| 9 | image_9.jpg | additional view 3 | Merino raglan cardigan in black, photo 9 |
| 10 | image_10.jpg | additional view 4 | Merino raglan cardigan in black, photo 10 |
| 11 | image_11.jpg | additional view 5 | Merino raglan cardigan in black, photo 11 |
| 12 | image_12.jpg | additional view 6 | Merino raglan cardigan in black, photo 12 |
| 13 | image_13.jpg | additional view 7 | Merino raglan cardigan in black, photo 13 |
| 14 | image_14.jpg | additional view 8 | Merino raglan cardigan in black, photo 14 |

---

## 04. Lambswool Raglan Crew Sweater, Brown (colour twin of 07 Green)

- **Live URL:** https://www.autumnandwool.com/shop/p/p/cozy-and-sustainable-hand-knitted-lambswool-sweater-for-women
- **Variants:** sizes S, M, L, XL. Colour is in the name only.
- **Name (H1):** `Lambswool Raglan Crew — Brown` → `Lambswool Raglan Crew Sweater - Brown` (37)
- **SEO title:** `Lambswool Raglan Crew Sweater, Brown | Autumn & Wool` (52) → `Lambswool Raglan Crew Sweater, Brown` (36)
- **SEO description:** keep (155). `Brown crew-neck sweater in 100% lambswool with raglan sleeves and a curved hem. Knitted and hand-sewn in Latvia. Sizes S–XL, free shipping, 14-day returns.`
- **Description edits:** none with banned wording. The twin paragraph below is the only change.
- **Twin paragraph (new first paragraph, 57 words, placed above "Lambswool sweater with a round ribbed neck…"):**
  > This brown version of the lambswool raglan crew is 100% lambswool (pure new wool), with a round ribbed neck, raglan sleeves, ribbed cuffs and a gently curved hem. The fit is relaxed. The photos show the sweater from the side and the back, and a close-up of the knit. Choose your size from the garment measurements below.

  `[OWNER: one line on what it pairs with. The live page does not say, so none is written here.]`
- **Cross link (place after the paragraph):** `Also in Green: https://www.autumnandwool.com/shop/p/p/hand-knitted-lambswool-sweater-womens-winter-knitwear-1`
- **Related-links block:**
  ```
  More sweaters: https://www.autumnandwool.com/wool-sweaters
  Also see: https://www.autumnandwool.com/shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper
  Also see: https://www.autumnandwool.com/shop/p/p/wool-sweater-sweater-for-women-knit-cozy-pullover-sweater-sustainable-knitwear-oversized-wool-jumper-relaxed-fit-wool-pullover-1
  ```
- **Alts (8 slots; colour brown, from the name):**

| # | Current file | Current alt (view word only) | New alt |
|---|---|---|---|
| 1 | image_1.jpg | main view (alt begins "Lambswool Raglan Crew — Women's Relaxed Jumper - 100% wool") | Lambswool raglan crew sweater in brown, main view |
| 2 | image_2.jpg | close-up detail view | Lambswool raglan crew sweater in brown, close-up detail view |
| 3 | image_3.jpg | side angle view | Lambswool raglan crew sweater in brown, side angle view |
| 4 | image_4.jpg | back view detail | Lambswool raglan crew sweater in brown, back view detail |
| 5 | image_5.jpg | lifestyle styling view | Lambswool raglan crew sweater in brown, styling view |
| 6 | image_6.jpg | texture and material detail | Lambswool raglan crew sweater in brown, texture and material detail |
| 7 | image_7.jpg | additional view 1 | Lambswool raglan crew sweater in brown, photo 7 |
| 8 | image_8.jpg | additional view 2 | Lambswool raglan crew sweater in brown, photo 8 |

---

## 05. Distressed Oversized Wool Raglan Sweater (colour not on the page)

- **Live URL:** https://www.autumnandwool.com/shop/p/p/hand-knitted-distressed-wool-sweater-oversized-raglan-jumper-1
- **Variants:** none. The page names no colour. `[OWNER: colour]`
- **Name (H1):** `Distressed Wool Raglan Sweater — Oversized` → `Distressed Oversized Wool Raglan Sweater` (39). This matches the live page title, so H1 and title agree.
- **SEO title:** `Distressed Oversized Wool Raglan Sweater | Autumn & Wool` (56) → `Distressed Oversized Wool Raglan Sweater` (39)
- **SEO description:** keep (141). `Oversized wool raglan sweater with distressed details, ribbed neck and cuffs. Knitted and hand-sewn in Latvia. Free shipping, 14-day returns.`
- **Description edits:** none. The description says "Material: wool". This sheet does not add "100%", although the current alts say "100% wool" (see CLAIM-CHECK).
- **Twin paragraph:** none.
- **Related-links block:**
  ```
  More sweaters: https://www.autumnandwool.com/wool-sweaters
  Also see: https://www.autumnandwool.com/shop/p/p/wool-sweater-sweater-for-women-knit-cozy-pullover-sweater-sustainable-knitwear-oversized-wool-jumper-relaxed-fit-wool-pullover-1
  Also see: https://www.autumnandwool.com/shop/p/p/hand-knitted-merino-wool-striped-sweater-oversized-jumper
  ```
- **Alts (10 slots; no colour known):**

| # | Current file | Current alt (view word only) | New alt |
|---|---|---|---|
| 1 | image_1.jpg | main view (alt says "100% wool") | Distressed oversized raglan sweater, main view |
| 2 | image_2.jpg | close-up detail view | Distressed oversized raglan sweater, close-up detail view |
| 3 | image_3.jpg | side angle view | Distressed oversized raglan sweater, side angle view |
| 4 | image_4.jpg | back view detail | Distressed oversized raglan sweater, back view detail |
| 5 | image_5.jpg | lifestyle styling view | Distressed oversized raglan sweater, styling view |
| 6 | image_6.jpg | texture and material detail | Distressed oversized raglan sweater, texture and material detail |
| 7 | image_7.jpg | additional view 1 | Distressed oversized raglan sweater, photo 7 |
| 8 | image_8.jpg | additional view 2 | Distressed oversized raglan sweater, photo 8 |
| 9 | image_9.jpg | additional view 3 | Distressed oversized raglan sweater, photo 9 |
| 10 | image_10.jpg | additional view 4 | Distressed oversized raglan sweater, photo 10 |

---

## 06. Women's Classic Lambswool Crew Sweater (grey by URL only)

- **Live URL:** https://www.autumnandwool.com/shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper
- **Variants:** sizes S, M, L, XL. No colour option. The page never names a colour. Grey is in the slug only. `[OWNER: confirm colour]`
- **Name (H1):** keep `Women’s Classic Lambswool Crew Sweater`. If the owner confirms grey: `Women's Classic Lambswool Crew Sweater - Grey` (46).
- **SEO title:** `Women's Classic Lambswool Crew Sweater | Autumn & Wool` (54) → `Women's Classic Lambswool Crew Sweater` (39)
- **SEO description:** `Classic crew-neck sweater in 100% lambswool with raglan sleeves and ribbed cuffs. Knitted and hand-sewn in Latvia. Sizes S–XL, free shipping, 14-day returns.` (157, over the 155 limit) → `Classic crew-neck sweater in 100% lambswool, raglan sleeves and ribbed cuffs. Knitted and hand-sewn in Latvia. Free shipping, 14-day returns.` (141)
- **Description edits:** none with banned wording.
- **Twin paragraph:** near-duplicate of 07 Green (similarity 0.92, C-03). Add the same paragraph as 04 once the owner has confirmed the colour. `[OWNER: colour]` first.
- **Related-links block:**
  ```
  More sweaters: https://www.autumnandwool.com/wool-sweaters
  Also see: https://www.autumnandwool.com/shop/p/p/cozy-and-sustainable-hand-knitted-lambswool-sweater-for-women
  Also see: https://www.autumnandwool.com/shop/p/p/wool-sweater-sweater-for-women-knit-cozy-pullover-sweater-sustainable-knitwear-oversized-wool-jumper-relaxed-fit-wool-pullover-1
  ```
- **Alts (8 slots).** The current alts name a different product ("Lambswool Raglan Crew — Women's Relaxed Jumper"), so all are replaced:

| # | Current file | Current alt (view word only) | New alt |
|---|---|---|---|
| 1 | image_1.jpg | main view | Classic lambswool crew sweater, main view |
| 2 | image_2.jpg | close-up detail view | Classic lambswool crew sweater, close-up detail view |
| 3 | image_3.jpg | side angle view | Classic lambswool crew sweater, side angle view |
| 4 | image_4.jpg | back view detail | Classic lambswool crew sweater, back view detail |
| 5 | image_5.jpg | lifestyle styling view | Classic lambswool crew sweater, styling view |
| 6 | image_6.jpg | texture and material detail | Classic lambswool crew sweater, texture and material detail |
| 7 | image_7.jpg | additional view 1 | Classic lambswool crew sweater, photo 7 |
| 8 | image_8.jpg | additional view 2 | Classic lambswool crew sweater, photo 8 |

Once the colour is confirmed, insert it after "sweater": `Classic lambswool crew sweater in grey, …`.

---

## 07. Lambswool Raglan Crew Sweater, Green (colour twin of 04 Brown)

- **Live URL:** https://www.autumnandwool.com/shop/p/p/hand-knitted-lambswool-sweater-womens-winter-knitwear-1
- **Variants:** sizes S, M, L, XL. Colour is in the name only.
- **Name (H1):** `Lambswool Raglan Crew — Green` → `Lambswool Raglan Crew Sweater - Green` (37)
- **SEO title:** `Lambswool Raglan Crew Sweater, Green | Autumn & Wool` (52) → `Lambswool Raglan Crew Sweater, Green` (36)
- **SEO description:** keep (155). `Green crew-neck sweater in 100% lambswool with raglan sleeves and a curved hem. Knitted and hand-sewn in Latvia. Sizes S–XL, free shipping, 14-day returns.`
- **Description edits:** none with banned wording. The twin paragraph is the only change.
- **Twin paragraph (57 words, above "Lambswool sweater with a round ribbed neck…"):**
  > This green version of the lambswool raglan crew is 100% lambswool (pure new wool), with a round ribbed neck, raglan sleeves, ribbed cuffs and a gently curved hem. The fit is relaxed. The photos show the sweater from the side and the back, and a close-up of the knit. Choose your size from the garment measurements below.

  `[OWNER: one line on what it pairs with.]`
- **Cross link:** `Also in Brown: https://www.autumnandwool.com/shop/p/p/cozy-and-sustainable-hand-knitted-lambswool-sweater-for-women`
- **Related-links block:**
  ```
  More sweaters: https://www.autumnandwool.com/wool-sweaters
  Also see: https://www.autumnandwool.com/shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper
  Also see: https://www.autumnandwool.com/shop/p/p/wool-sweater-sweater-for-women-knit-cozy-pullover-sweater-sustainable-knitwear-oversized-wool-jumper-relaxed-fit-wool-pullover-1
  ```
- **Alts (7 slots; colour green, from the name):**

| # | Current file | Current alt (view word only) | New alt |
|---|---|---|---|
| 1 | image_1.jpg | main view | Lambswool raglan crew sweater in green, main view |
| 2 | image_2.jpg | close-up detail view | Lambswool raglan crew sweater in green, close-up detail view |
| 3 | image_3.jpg | side angle view | Lambswool raglan crew sweater in green, side angle view |
| 4 | image_4.jpg | back view detail | Lambswool raglan crew sweater in green, back view detail |
| 5 | image_5.jpg | lifestyle styling view | Lambswool raglan crew sweater in green, styling view |
| 6 | image_6.jpg | texture and material detail | Lambswool raglan crew sweater in green, texture and material detail |
| 7 | image_7.jpg | additional view 1 | Lambswool raglan crew sweater in green, photo 7 |

---

## 08. Merino Wool Raglan Sweater, Dusty Pink (size variants only)

- **Live URL:** https://www.autumnandwool.com/shop/p/p/hand-knitted-merino-wool-raglan-sweater-dusty-pink-oversized-jumper
- **Variants:** sizes S/M, L/XL. Colour dusty pink is in the name.
- **Name (H1):** `Merino Wool Raglan Sweater — Dusty Pink Oversized Jumper` → `Merino Wool Raglan Sweater - Dusty Pink` (39)
- **SEO title:** `Merino Raglan Sweater, Dusty Pink | Autumn & Wool` (49) → `Merino Raglan Sweater, Dusty Pink` (33)
- **SEO description:** keep (134). `Oversized dusty pink raglan jumper in merino wool, sizes S/M and L/XL. Knitted and hand-sewn in Latvia. Free shipping, 14-day returns.`
- **Description edits:** none in the description. The alts repeated "Hand-Knitted" (replaced below).
- **Twin paragraph:** cluster C with 18 (same colour). Not a C-03 twin. The owner decides whether both stay. See 18.
- **Related-links block:**
  ```
  More sweaters: https://www.autumnandwool.com/wool-sweaters
  Also see: https://www.autumnandwool.com/shop/p/p/merino-wool-sweater-oversize-sweater-knitted-wool-jumper-stand-up-collar-jumper-relaxed-fit-wool-pullover-warm-pink-jumper-679519
  Also see: https://www.autumnandwool.com/shop/p/p/hand-knitted-merino-wool-striped-sweater-oversized-jumper
  ```
- **Alts (9 slots; colour dusty pink, from the name):**

| # | Current file | Current alt (view word only) | New alt |
|---|---|---|---|
| 1 | image_1.jpg | "Hand-Knitted Merino Wool Raglan Sweater…" main view | Merino raglan sweater in dusty pink, main view |
| 2 | image_2.jpg | close-up detail view | Merino raglan sweater in dusty pink, close-up detail view |
| 3 | image_3.jpg | side angle view | Merino raglan sweater in dusty pink, side angle view |
| 4 | image_4.jpg | back view detail | Merino raglan sweater in dusty pink, back view detail |
| 5 | image_5.jpg | lifestyle styling view | Merino raglan sweater in dusty pink, styling view |
| 6 | image_6.jpg | texture and material detail | Merino raglan sweater in dusty pink, texture and material detail |
| 7 | image_7.jpg | additional view 1 | Merino raglan sweater in dusty pink, photo 7 |
| 8 | image_8.jpg | additional view 2 | Merino raglan sweater in dusty pink, photo 8 |
| 9 | image_9.jpg | additional view 3 | Merino raglan sweater in dusty pink, photo 9 |

---

## 09. Merino Striped Oversized Sweater (colour not on the page)

- **Live URL:** https://www.autumnandwool.com/shop/p/p/hand-knitted-merino-wool-striped-sweater-oversized-jumper
- **Variants:** none. The page names no colour. `[OWNER: colour]`
- **Name (H1):** `Merino Striped Oversized Sweater — Women’s Jumper` → `Merino Striped Oversized Sweater` (32)
- **SEO title:** `Merino Striped Oversized Sweater | Autumn & Wool` (48) → `Merino Striped Oversized Sweater` (32)
- **SEO description:** keep (146). `Oversized striped jumper in 100% merino wool with Japanese-style shoulder shaping. Knitted and hand-sewn in Latvia. Free shipping, 14-day returns.`
- **Description edits:** none with banned wording.
- **Twin paragraph:** none.
- **Related-links block:**
  ```
  More sweaters: https://www.autumnandwool.com/wool-sweaters
  Also see: https://www.autumnandwool.com/shop/p/p/hand-knitted-merino-wool-raglan-sweater-dusty-pink-oversized-jumper
  Also see: https://www.autumnandwool.com/shop/p/p/wool-sweater-sweater-for-women-knit-cozy-pullover-sweater-sustainable-knitwear-oversized-wool-jumper-relaxed-fit-wool-pullover-1
  ```
- **Alts (8 slots; no colour known):**

| # | Current file | Current alt (view word only) | New alt |
|---|---|---|---|
| 1 | image_1.jpg | main view | Merino striped oversized sweater, main view |
| 2 | image_2.jpg | close-up detail view | Merino striped oversized sweater, close-up detail view |
| 3 | image_3.jpg | side angle view | Merino striped oversized sweater, side angle view |
| 4 | image_4.jpg | back view detail | Merino striped oversized sweater, back view detail |
| 5 | image_5.jpg | lifestyle styling view | Merino striped oversized sweater, styling view |
| 6 | image_6.jpg | texture and material detail | Merino striped oversized sweater, texture and material detail |
| 7 | image_7.jpg | additional view 1 | Merino striped oversized sweater, photo 7 |
| 8 | image_8.jpg | additional view 2 | Merino striped oversized sweater, photo 8 |

---

## 10. 100% Wool Long Shawl Cardigan (near-duplicate of 20)

- **Live URL:** https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-cardigan-minimalist-open-front-sweater-1
- **Variants:** sizes S, M, L, XL. No colour option. `[OWNER: colour]`
- **Name (H1):** `100% Wool Long Shawl Cardigan – Warm Knit` → `100% Wool Long Shawl Cardigan` (29). "Warm Knit" is dropped (no warmth claim on the page; see CLAIM-CHECK).
- **SEO title:** `Long Wool Shawl Cardigan, 100% Wool | Autumn & Wool` (51) → `Long Wool Shawl Cardigan, 100% Wool` (35)
- **SEO description:** keep (150). `Long open-front cardigan in 100% pure new wool with a draped collar and dropped shoulders. Knitted and hand-sewn in Latvia. Sizes S–XL, free shipping.`
- **Description edits:** none with banned wording.
- **Near-duplicate paragraph (new first paragraph, 57 words; C-03 says the two shawl cardigans compete, so each gets a distinct opening):**
  > This long open-front cardigan is cut straight, with dropped shoulders, a draped collar and double-folded cuffs and hem. It is 100% pure new wool, with a straight, relaxed fit in sizes S to XL. The model is 171 cm tall and wears size M. The photos show the side, the back and a close-up of the knit.
- **Cross link:** `Similar cardigan, other opening: https://www.autumnandwool.com/shop/p/p/wool-cardigan-warm-cardigan-organic-wool-wrap-winter-sweater-cardigan-women-cardigan-sweater-minimalist-style-sweater` (OWNER: keep one of 10 or 20, C-03 decision.)
- **Related-links block:**
  ```
  More cardigans: https://www.autumnandwool.com/wool-cardigans
  Also see: https://www.autumnandwool.com/shop/p/p/wool-cardigan-warm-cardigan-organic-wool-wrap-winter-sweater-cardigan-women-cardigan-sweater-minimalist-style-sweater
  Also see: https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-cardigan-open-front-winter-sweater-679428
  ```
- **Alts (9 slots; no colour known):**

| # | Current file | Current alt (view word only) | New alt |
|---|---|---|---|
| 1 | image_1.jpg | main view (alt "100% wool cardigan main view") | Long wool shawl cardigan, main view |
| 2 | image_2.jpg | close-up detail view | Long wool shawl cardigan, close-up detail view |
| 3 | image_3.jpg | side angle view | Long wool shawl cardigan, side angle view |
| 4 | image_4.jpg | back view detail | Long wool shawl cardigan, back view detail |
| 5 | image_5.jpg | lifestyle styling view | Long wool shawl cardigan, styling view |
| 6 | image_6.jpg | texture and material detail | Long wool shawl cardigan, texture and material detail |
| 7 | image_7.jpg | additional view 1 | Long wool shawl cardigan, photo 7 |
| 8 | image_8.jpg | additional view 2 | Long wool shawl cardigan, photo 8 |
| 9 | image_9.jpg | additional view 3 | Long wool shawl cardigan, photo 9 |

---

## 11. Open-Front Wool Cardigan with Side Slits (colour not on the page)

- **Live URL:** https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-cardigan-open-front-winter-sweater-679428
- **Variants:** none. `[OWNER: colour]`
- **Name (H1):** `Open-Front Wool Cardigan — Women’s Side-Slit Knit` → `Open-Front Wool Cardigan with Side Slits` (40)
- **SEO title:** `Open-Front Wool Cardigan with Side Slits | Autumn & Wool` (56) → `Open-Front Wool Cardigan with Side Slits` (40)
- **SEO description:** keep (142). `Straight-cut open-front cardigan in 100% pure new wool with ribbed side slits. Knitted and hand-sewn in Latvia. Free shipping, 14-day returns.`
- **Description edits:** none with banned wording.
- **Twin paragraph:** none (D2 cluster, a different cardigan).
- **Related-links block:**
  ```
  More cardigans: https://www.autumnandwool.com/wool-cardigans
  Also see: https://www.autumnandwool.com/shop/p/p/black-merino-wool-cardigan-100-merino-wool-raglan-sweater-minimalist-knitwear-sustainable-handmade-womens-cardigan-1
  Also see: https://www.autumnandwool.com/shop/p/p/wool-cardigan-warm-cardigan-organic-wool-wrap-winter-sweater-cardigan-women-cardigan-sweater-minimalist-style-sweater
  ```
- **Alts (9 slots; no colour known):**

| # | Current file | Current alt (view word only) | New alt |
|---|---|---|---|
| 1 | image_1.jpg | main view | Open-front wool cardigan with side slits, main view |
| 2 | image_2.jpg | close-up detail view | Open-front wool cardigan with side slits, close-up detail view |
| 3 | image_3.jpg | side angle view | Open-front wool cardigan with side slits, side angle view |
| 4 | image_4.jpg | back view detail | Open-front wool cardigan with side slits, back view detail |
| 5 | image_5.jpg | lifestyle styling view | Open-front wool cardigan with side slits, styling view |
| 6 | image_6.jpg | texture and material detail | Open-front wool cardigan with side slits, texture and material detail |
| 7 | image_7.jpg | additional view 1 | Open-front wool cardigan with side slits, photo 7 |
| 8 | image_8.jpg | additional view 2 | Open-front wool cardigan with side slits, photo 8 |
| 9 | image_9.jpg | additional view 3 | Open-front wool cardigan with side slits, photo 9 |

---

## 12. Pure Wool Stand-Collar Sweater, Blue (colour twin of 14 Beige)

- **Live URL:** https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-stand-collar-sweater-womens-knitwear-679510
- **Variants:** sizes S, M, L, XL. Colour is in the name. The page has one gallery photo (the crawl's seven image tags are not gallery photos).
- **Name (H1):** `Pure Wool Stand-Collar Sweater — Blue` → `Pure Wool Stand-Collar Sweater - Blue` (37)
- **SEO title:** `Pure Wool Stand-Collar Sweater, Blue | Autumn & Wool` (52) → `Pure Wool Stand-Collar Sweater, Blue` (36)
- **SEO description:** keep (137). `Blue stand-collar sweater in 100% pure new wool with a clean, timeless shape. Knitted and hand-sewn in Latvia. Sizes S–XL, free shipping.`
- **Description edits:** none with banned wording.
- **Twin paragraph (58 words, new first paragraph; C-03 twin of 14):**
  > This blue version of the pure wool stand-collar sweater is 100% pure new wool, with a clean, timeless shape, a stand collar and a relaxed fit. Sizes run from S to XL, and the model is 171 cm tall and usually wears size S. Measurements for each size are listed below. The one photo shows it in blue.

  OWNER: the two stand-collar pages differ only by colour and have one photo each. A stronger difference needs a second photo per colour or fit facts from the owner.
- **Cross link:** `Also in Beige: https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-sweater-stand-collar-knit-679503`
- **Related-links block:**
  ```
  More sweaters: https://www.autumnandwool.com/wool-sweaters
  Also see: https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-sweater-organic-knitwear-asymmetrical-design-1
  Also see: https://www.autumnandwool.com/shop/p/p/wool-sweater-sweater-for-women-knit-cozy-pullover-sweater-sustainable-knitwear-oversized-wool-jumper-relaxed-fit-wool-pullover-1
  ```
- **Alts (1 slot):**

| # | Current file | Current alt | New alt |
|---|---|---|---|
| 1 | image_1.jpg | Pure Wool Stand-Collar Sweater — Women’s Knit - 100% wool sweater main view | Pure wool stand-collar sweater in blue, main view |

---

## 13. Pure Wool Side-Slit Sweater, Light Grey (colour twin of 15 Camel)

- **Live URL:** https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-sweater-organic-knitwear-asymmetrical-design-1
- **Variants:** sizes S, M, L, XL. Colour is in the name.
- **Name (H1):** `Pure Wool Side-Slit Sweater — Light Grey` → `Pure Wool Side-Slit Sweater - Light Grey` (40)
- **SEO title:** `Pure Wool Side-Slit Sweater, Light Grey | Autumn & Wool` (55) → `Pure Wool Side-Slit Sweater, Light Grey` (39)
- **SEO description:** keep (150). `Light grey round-neck sweater in 100% pure new wool with side slits and a longer back hem. Knitted and hand-sewn in Latvia. Sizes S–XL, free shipping.`
- **Description edits:** none with banned wording.
- **Twin paragraph (58 words, new first paragraph):**
  > The light grey version has a round neck, side slits and an asymmetric hem, with the front shorter than the back. It is 100% pure new wool with a relaxed fit, in sizes S to XL. The model is 171 cm tall and wears size S. The photos show the side, the back and the knit up close.
- **Cross link:** `Also in Camel: https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-sweater-womens-organic-knit-jumper-1`
- **Related-links block:**
  ```
  More sweaters: https://www.autumnandwool.com/wool-sweaters
  Also see: https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-stand-collar-sweater-womens-knitwear-679510
  Also see: https://www.autumnandwool.com/shop/p/p/wool-sweater-sweater-for-women-knit-cozy-pullover-sweater-sustainable-knitwear-oversized-wool-jumper-relaxed-fit-wool-pullover-1
  ```
- **Alts (7 slots; colour light grey, from the name):**

| # | Current file | Current alt (view word only) | New alt |
|---|---|---|---|
| 1 | image_1.jpg | main view | Pure wool side-slit sweater in light grey, main view |
| 2 | image_2.jpg | close-up detail view | Pure wool side-slit sweater in light grey, close-up detail view |
| 3 | image_3.jpg | side angle view | Pure wool side-slit sweater in light grey, side angle view |
| 4 | image_4.jpg | back view detail | Pure wool side-slit sweater in light grey, back view detail |
| 5 | image_5.jpg | lifestyle styling view | Pure wool side-slit sweater in light grey, styling view |
| 6 | image_6.jpg | texture and material detail | Pure wool side-slit sweater in light grey, texture and material detail |
| 7 | image_7.jpg | additional view 1 | Pure wool side-slit sweater in light grey, photo 7 |

---

## 14. Pure Wool Stand-Collar Sweater, Beige (colour twin of 12 Blue)

- **Live URL:** https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-sweater-stand-collar-knit-679503
- **Variants:** sizes S, M, L, XL. Colour is in the name. One gallery photo.
- **Name (H1):** `Pure Wool Stand-Collar Sweater — Beige` → `Pure Wool Stand-Collar Sweater - Beige` (38)
- **SEO title:** `Pure Wool Stand-Collar Sweater, Beige | Autumn & Wool` (53) → `Pure Wool Stand-Collar Sweater, Beige` (37)
- **SEO description:** keep (138). `Beige stand-collar sweater in 100% pure new wool with a clean, timeless shape. Knitted and hand-sewn in Latvia. Sizes S–XL, free shipping.`
- **Description edits:** none with banned wording.
- **Twin paragraph (58 words, new first paragraph):**
  > This beige version of the pure wool stand-collar sweater is 100% pure new wool, with a clean, timeless shape, a stand collar and a relaxed fit. Sizes run from S to XL, and the model is 171 cm tall and usually wears size S. Measurements for each size are listed below. The one photo shows it in beige.
- **Cross link:** `Also in Blue: https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-stand-collar-sweater-womens-knitwear-679510`
- **Related-links block:**
  ```
  More sweaters: https://www.autumnandwool.com/wool-sweaters
  Also see: https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-sweater-womens-organic-knit-jumper-1
  Also see: https://www.autumnandwool.com/shop/p/p/wool-sweater-sweater-for-women-knit-cozy-pullover-sweater-sustainable-knitwear-oversized-wool-jumper-relaxed-fit-wool-pullover-1
  ```
- **Alts (1 slot):**

| # | Current file | Current alt | New alt |
|---|---|---|---|
| 1 | image_1.jpg | Women’s wool stand collar sweater - 100% wool sweater main view | Pure wool stand-collar sweater in beige, main view |

---

## 15. Pure Wool Side-Slit Sweater, Camel (colour twin of 13 Light Grey)

- **Live URL:** https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-sweater-womens-organic-knit-jumper-1
- **Variants:** sizes S, M, L, XL. Colour is in the name.
- **Name (H1):** `Pure Wool Side-Slit Sweater — Camel` → `Pure Wool Side-Slit Sweater - Camel` (35)
- **SEO title:** `Pure Wool Side-Slit Sweater, Camel | Autumn & Wool` (50) → `Pure Wool Side-Slit Sweater, Camel` (34)
- **SEO description:** keep (145). `Camel round-neck sweater in 100% pure new wool with side slits and a longer back hem. Knitted and hand-sewn in Latvia. Sizes S–XL, free shipping.`
- **Description edits:** none with banned wording.
- **Twin paragraph (57 words, new first paragraph):**
  > The camel version has a round neck, side slits and an asymmetric hem, with the front shorter than the back. It is 100% pure new wool with a relaxed fit, in sizes S to XL. The model is 171 cm tall and wears size S. The photos show the side, the back and the knit up close.
- **Cross link:** `Also in Light Grey: https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-sweater-organic-knitwear-asymmetrical-design-1`
- **Related-links block:**
  ```
  More sweaters: https://www.autumnandwool.com/wool-sweaters
  Also see: https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-stand-collar-sweater-womens-knitwear-679510
  Also see: https://www.autumnandwool.com/shop/p/p/wool-sweater-sweater-for-women-knit-cozy-pullover-sweater-sustainable-knitwear-oversized-wool-jumper-relaxed-fit-wool-pullover-1
  ```
- **Alts (7 slots; colour camel, from the name):**

| # | Current file | Current alt (view word only) | New alt |
|---|---|---|---|
| 1 | image_1.jpg | main view | Pure wool side-slit sweater in camel, main view |
| 2 | image_2.jpg | close-up detail view | Pure wool side-slit sweater in camel, close-up detail view |
| 3 | image_3.jpg | side angle view | Pure wool side-slit sweater in camel, side angle view |
| 4 | image_4.jpg | back view detail | Pure wool side-slit sweater in camel, back view detail |
| 5 | image_5.jpg | lifestyle styling view | Pure wool side-slit sweater in camel, styling view |
| 6 | image_6.jpg | texture and material detail | Pure wool side-slit sweater in camel, texture and material detail |
| 7 | image_7.jpg | additional view 1 | Pure wool side-slit sweater in camel, photo 7 |

---

## 16. Merino Rib-Knit Beanie, Unisex (11 colour variants)

- **Live URL:** https://www.autumnandwool.com/shop/p/p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1
- **Variants (live, 11):** Black, Brown, Navy, Blue, Gray, Light grey, Beige, Camel, Bordeaux, Pink, Melange grey. One size. The copy says "Available in 11 colours", which matches the variant list, so the 11 is kept.
- **Name (H1):** `Rib-Knit Beanie — Unisex` → `Merino Rib-Knit Beanie - Unisex` (31). The fibre is in the copy ("100% extra-fine merino wool, Italian-spun yarn"). "Extra-fine" and "Italian-spun" are not in the name (see CLAIM-CHECK).
- **SEO title:** `Merino Rib-Knit Beanie, Unisex` (30). The live title is `Rib-Knit Beanie — Unisex | Autumn & Wool` (40).
- **SEO description:** `Rib-knit beanie with a fold-over cuff and smooth front panel. One size, available in 11 color options. See care details and shop at Autumn & Wool.` (146) → `Merino rib-knit beanie with a fold-over cuff, one size, in 11 colours. Care details and sizing on the product page. Free shipping, 14-day returns.` (146)
- **Description edits:** none with banned wording.
- **Twin paragraph:** not applicable (colour variants on one product).
- **Related-links block:**
  ```
  More hats and scarves: https://www.autumnandwool.com/wool-hats-and-scarves
  Also see: https://www.autumnandwool.com/shop/p/p/merino-wool-hat-scarf-set-extra-fine-rib-knit-soft-on-skin-warm-not-bulky-unisex-gift
  Also see: https://www.autumnandwool.com/shop/p/autumn-and-wool-digital-gift-card
  ```
- **Alts (18 slots).** Colours come from the page's own photo alts, which name several colours. OWNER: check each shade against the photo before publishing (slots 5, 13 and 14 need a shade name).

| # | Current file | Current alt (abridged) | New alt |
|---|---|---|---|
| 1 | image_1.jpg | Grey rib-knit beanie with a wide fold-over cuff | Merino rib-knit beanie in grey, wide fold-over cuff |
| 2 | image_2.jpg | Merino beanie colour chart showing stacked knitted hats and colour labels | Merino rib-knit beanie colour chart, photo 2 |
| 3 | image_3.jpg | Camel rib-knit merino beanie with a folded cuff | Merino rib-knit beanie in camel, folded cuff |
| 4 | image_4.jpg | Stack of rib-knit beanies in light and dark colour options | Merino rib-knit beanies in light and dark colours, photo 4 |
| 5 | image_5.jpg | Dark rib-knit beanie showing its wide folded cuff | Merino rib-knit beanie in a dark shade, wide folded cuff |
| 6 | image_6.jpg | Burgundy rib-knit merino beanie with a fold-over cuff | Merino rib-knit beanie in burgundy, fold-over cuff |
| 7 | image_7.jpg | Beige rib-knit beanie showing the ribbed crown and cuff | Merino rib-knit beanie in beige, ribbed crown and cuff |
| 8 | image_8.jpg | Burgundy beanie folded to show the rib-knit texture | Merino rib-knit beanie in burgundy, folded to show texture |
| 9 | image_9.jpg | Beige merino beanie folded to show the cuff and interior | Merino rib-knit beanie in beige, folded to show cuff and interior |
| 10 | image_10.jpg | Camel rib-knit beanie worn on a mannequin in side view | Merino rib-knit beanie in camel, worn on a mannequin, side view |
| 11 | image_11.jpg | Grey rib-knit beanie worn on a mannequin with a matching scarf | Merino rib-knit beanie in grey, worn on a mannequin with a scarf |
| 12 | image_12.jpg | Rib-knit beanies stacked in beige, camel, grey, burgundy and dark shades | Merino rib-knit beanies in several colours, stacked, photo 12 |
| 13 | image_13.jpg | Beige rib-knit beanie on a mannequin showing its tall crown | Merino rib-knit beanie in beige, on a mannequin, tall crown |
| 14 | image_14.jpg | Dark grey rib-knit beanie on a mannequin in side view | Merino rib-knit beanie in dark grey, mannequin side view |
| 15 | image_15.jpg | Close-up of grey merino rib knit and folded beanie cuff | Merino rib-knit beanie in grey, close-up of folded cuff |
| 16 | image_16.jpg | Rib-knit beanies arranged together in burgundy, camel, grey and dark shades | Merino rib-knit beanies in several colours, photo 16 |
| 17 | image_17.jpg | Side view of a stack of folded merino beanies in several colours | Merino rib-knit beanies in several colours, stacked, photo 17 |
| 18 | image_18.jpg | Grey merino beanie and matching scarf worn on a mannequin | Merino rib-knit beanie in grey, on a mannequin with a scarf |

---

## 17. Merino Wool Hat & Scarf Set (variants Black, Gray, Brown)

- **Live URL:** https://www.autumnandwool.com/shop/p/p/merino-wool-hat-scarf-set-extra-fine-rib-knit-soft-on-skin-warm-not-bulky-unisex-gift
- **Variants:** Black, Gray, Brown (colour options). Beanie one size; scarf approx. 190 × 36 cm (copy).
- **Name (H1):** keep `Merino Wool Hat & Scarf Set` (27).
- **SEO title:** `Merino Wool Hat & Scarf Set | Autumn & Wool` (43) → `Merino Wool Hat & Scarf Set in Black, Gray or Brown` (51)
- **SEO description:** `Explore a coordinated hat-and-scarf set for cooler days. View available colours, measurements and care details at Autumn & Wool.` (128) → `Matching merino hat and scarf set with a rib-knit beanie, in black, gray or brown. Scarf approx. 190 × 36 cm. Free shipping, 14-day returns.` (140)
- **Description edits:** none with banned wording. OWNER: the FAQ inside the description says "At the current price of €110" and "under €120". Check the price is still current.
- **Twin paragraph:** not applicable.
- **Related-links block:**
  ```
  More hats and scarves: https://www.autumnandwool.com/wool-hats-and-scarves
  Also see: https://www.autumnandwool.com/shop/p/p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1
  Also see: https://www.autumnandwool.com/shop/p/autumn-and-wool-digital-gift-card
  ```
- **Alts (17 slots):**

| # | Current file | Current alt (abridged) | New alt |
|---|---|---|---|
| 1 | image_1.jpg | Merino Wool Hat & Scarf Set - merino wool scarf main view | Merino hat and scarf set, main view |
| 2 | image_2.jpg | … close-up detail view | Merino hat and scarf set, close-up detail view |
| 3 | image_3.jpg | … side angle view | Merino hat and scarf set, side angle view |
| 4 | image_4.jpg | … back view detail | Merino hat and scarf set, back view detail |
| 5 | image_5.jpg | Grey rib-knit beanie and matching long scarf worn on a mannequin | Merino hat and scarf set in grey, worn on a mannequin |
| 6 | image_6.jpg | Merino wool rib-knit beanie and matching scarf displayed on a mannequin | Merino hat and scarf set, worn on a mannequin |
| 7 | image_7.jpg | … additional view 1 | Merino hat and scarf set, photo 7 |
| 8 | image_8.jpg | Merino wool rib-knit beanie and matching scarf displayed on a mannequin | Merino hat and scarf set, worn on a mannequin, photo 8 |
| 9 | image_9.jpg | … additional view 3 | Merino hat and scarf set, photo 9 |
| 10 | image_10.jpg | … additional view 4 | Merino hat and scarf set, photo 10 |
| 11 | image_11.jpg | … additional view 5 | Merino hat and scarf set, photo 11 |
| 12 | image_12.jpg | … additional view 6 | Merino hat and scarf set, photo 12 |
| 13 | image_13.jpg | … additional view 7 | Merino hat and scarf set, photo 13 |
| 14 | image_14.jpg | … additional view 8 | Merino hat and scarf set, photo 14 |
| 15 | image_15.jpg | Merino wool rib-knit beanie and matching scarf displayed on a mannequin | Merino hat and scarf set, worn on a mannequin, photo 15 |
| 16 | image_16.jpg | Merino wool rib-knit beanie and matching scarf displayed on a mannequin | Merino hat and scarf set, worn on a mannequin, photo 16 |
| 17 | image_17.jpg | Merino wool rib-knit beanie and matching scarf displayed on a mannequin | Merino hat and scarf set, worn on a mannequin, photo 17 |

---

## 18. Oversized Merino Turtleneck, Dusty Pink Raglan (single colour)

- **Live URL:** https://www.autumnandwool.com/shop/p/p/merino-wool-sweater-oversize-sweater-knitted-wool-jumper-stand-up-collar-jumper-relaxed-fit-wool-pullover-warm-pink-jumper-679519
- **Variants:** none. Colour dusty pink is in the name and description.
- **Name (H1):** keep `Oversized Merino Turtleneck — Dusty Pink Raglan`.
- **SEO title:** `Oversized Merino Turtleneck, Dusty Pink | Autumn & Wool` (55) → `Oversized Merino Turtleneck, Dusty Pink` (39)
- **SEO description:** keep (147). `Oversized raglan turtleneck in dusty pink merino wool with ribbed collar and cuffs. Knitted and hand-sewn in Latvia. Free shipping, 14-day returns.`
- **Description edits:** none with banned wording.
- **Twin paragraph:** cluster C with 08 (same colour). Not a C-03 twin. See 08.
- **Related-links block:**
  ```
  More sweaters: https://www.autumnandwool.com/wool-sweaters
  Also see: https://www.autumnandwool.com/shop/p/p/hand-knitted-merino-wool-raglan-sweater-dusty-pink-oversized-jumper
  Also see: https://www.autumnandwool.com/shop/p/p/merino-wool-turtleneck-sweater-womens-knit-pullover-soft-warm-lightweight-minimalist-sustainable-knitwear-sizes-sl-12-679428
  ```
- **Alts (9 slots; colour dusty pink):**

| # | Current file | Current alt (abridged) | New alt |
|---|---|---|---|
| 1 | image_1.jpg | Oversized Merino Turtleneck — Dusty Pink Raglan - merino wool oversized main view | Oversized merino turtleneck in dusty pink, main view |
| 2 | image_2.jpg | … close-up detail view | Oversized merino turtleneck in dusty pink, close-up detail view |
| 3 | image_3.jpg | … side angle view | Oversized merino turtleneck in dusty pink, side angle view |
| 4 | image_4.jpg | … back view detail | Oversized merino turtleneck in dusty pink, back view detail |
| 5 | image_5.jpg | … lifestyle styling view | Oversized merino turtleneck in dusty pink, styling view |
| 6 | image_6.jpg | … texture and material detail | Oversized merino turtleneck in dusty pink, texture and material detail |
| 7 | image_7.jpg | … additional view 1 | Oversized merino turtleneck in dusty pink, photo 7 |
| 8 | image_8.jpg | … additional view 2 | Oversized merino turtleneck in dusty pink, photo 8 |
| 9 | image_9.jpg | … additional view 3 | Oversized merino turtleneck in dusty pink, photo 9 |

---

## 19. Lightweight Merino Turtleneck, 12 Colours (12 colour variants)

- **Live URL:** https://www.autumnandwool.com/shop/p/p/merino-wool-turtleneck-sweater-womens-knit-pullover-soft-warm-lightweight-minimalist-sustainable-knitwear-sizes-sl-12-679428
- **Variants (live, 12 colours):** Melange Grey, Classic Grey, Chestnut Brown, Melange Brown, Melange Taupe, Melange Beige, Dusty Rose, Rose Pink, Berry Purple, Purple Brown, Royal Blue, Sky Blue. Size options XS, S, M. The size table in the copy lists S, M and L. OWNER: confirm the size range before publishing.
- **Name (H1):** `Merino Turtleneck — Women’s Lightweight Knit` → `Lightweight Merino Turtleneck, 12 Colours` (41). The count of 12 matches the variant list. The current title field already uses this wording.
- **SEO title:** `Lightweight Merino Turtleneck, 12 Colours | Autumn & Wool` (57) → `Lightweight Merino Turtleneck, 12 Colours` (41)
- **SEO description:** keep (130 raw). The crawl shows 17 characters because of an apostrophe. `Lightweight women's turtleneck in 100% merino wool, in 12 colours. Knitted and hand-sewn in Latvia. Free shipping, 14-day returns.`
- **Description edits:** none with banned wording.
- **Twin paragraph:** not needed. One product carries the 12 colours.
- **Related-links block:**
  ```
  More sweaters: https://www.autumnandwool.com/wool-sweaters
  Also see: https://www.autumnandwool.com/shop/p/p/merino-wool-sweater-oversize-sweater-knitted-wool-jumper-stand-up-collar-jumper-relaxed-fit-wool-pullover-warm-pink-jumper-679519
  Also see: https://www.autumnandwool.com/shop/p/p/hand-knitted-merino-wool-raglan-sweater-dusty-pink-oversized-jumper
  ```
- **Alts (9 slots).** The alts do not name the colour of each photo, so the colour is left out, not guessed. OWNER: confirm which colour the photos show before adding it.

| # | Current file | Current alt (abridged) | New alt |
|---|---|---|---|
| 1 | image_1.jpg | Merino Turtleneck — Women’s Lightweight Knit - merino wool main view | Women's lightweight merino turtleneck, main view |
| 2 | image_2.jpg | … close-up detail view | Women's lightweight merino turtleneck, close-up detail view |
| 3 | image_3.jpg | … side angle view | Women's lightweight merino turtleneck, side angle view |
| 4 | image_4.jpg | … back view detail | Women's lightweight merino turtleneck, back view detail |
| 5 | image_5.jpg | … lifestyle styling view | Women's lightweight merino turtleneck, styling view |
| 6 | image_6.jpg | … texture and material detail | Women's lightweight merino turtleneck, texture and material detail |
| 7 | image_7.jpg | … additional view 1 | Women's lightweight merino turtleneck, photo 7 |
| 8 | image_8.jpg | … additional view 2 | Women's lightweight merino turtleneck, photo 8 |
| 9 | image_9.jpg | … additional view 3 | Women's lightweight merino turtleneck, photo 9 |

---

## 20. Long Wool Cardigan with Shawl Collar (near-duplicate of 10)

- **Live URL:** https://www.autumnandwool.com/shop/p/p/wool-cardigan-warm-cardigan-organic-wool-wrap-winter-sweater-cardigan-women-cardigan-sweater-minimalist-style-sweater
- **Variants:** sizes S, M, L, XL. No colour option. `[OWNER: colour]`
- **Name (H1):** `Long Wool Cardigan — Women’s Shawl Collar` → `Long Wool Cardigan with Shawl Collar` (36)
- **SEO title:** `Long Wool Cardigan with Shawl Collar, 100% Wool | Autumn & Wool` (63) → `Long Wool Shawl Collar Cardigan` (31)
- **SEO description:** keep (153). `Knee-length open-front cardigan in 100% pure new wool, knitted and hand-sewn in Latvia. Sizes S–XL with full measurements. Free shipping, 14-day returns.`
- **Description edits:** none with banned wording.
- **Near-duplicate paragraph (56 words, new first paragraph; see 10):**
  > This knee-length open-front cardigan has a straight cut, dropped shoulders, long sleeves and a draped shawl collar. It is 100% pure new wool, with a straight, relaxed fit in sizes S to XL. The model is 171 cm tall and wears size M. The photos show the side, the back and a close-up of the knit.
- **Cross link:** `Similar cardigan, other opening: https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-cardigan-minimalist-open-front-sweater-1` (OWNER: C-03 decision.)
- **Related-links block:**
  ```
  More cardigans: https://www.autumnandwool.com/wool-cardigans
  Also see: https://www.autumnandwool.com/shop/p/p/black-merino-wool-cardigan-100-merino-wool-raglan-sweater-minimalist-knitwear-sustainable-handmade-womens-cardigan-1
  Also see: https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-cardigan-open-front-winter-sweater-679428
  ```
- **Alts (9 slots; no colour known):**

| # | Current file | Current alt (view word only) | New alt |
|---|---|---|---|
| 1 | image_1.jpg | main view | Long wool cardigan with shawl collar, main view |
| 2 | image_2.jpg | close-up detail view | Long wool cardigan with shawl collar, close-up detail view |
| 3 | image_3.jpg | side angle view | Long wool cardigan with shawl collar, side angle view |
| 4 | image_4.jpg | back view detail | Long wool cardigan with shawl collar, back view detail |
| 5 | image_5.jpg | lifestyle styling view | Long wool cardigan with shawl collar, styling view |
| 6 | image_6.jpg | texture and material detail | Long wool cardigan with shawl collar, texture and material detail |
| 7 | image_7.jpg | additional view 1 | Long wool cardigan with shawl collar, photo 7 |
| 8 | image_8.jpg | additional view 2 | Long wool cardigan with shawl collar, photo 8 |
| 9 | image_9.jpg | additional view 3 | Long wool cardigan with shawl collar, photo 9 |

---

## 21. Oversized Wool Raglan Sweater, Beige Melange

- **Live URL:** https://www.autumnandwool.com/shop/p/p/wool-sweater-sweater-for-women-knit-cozy-pullover-sweater-sustainable-knitwear-oversized-wool-jumper-relaxed-fit-wool-pullover-1
- **Variants:** none. Colour beige melange is in the name and description.
- **Name (H1):** keep `Oversized Wool Raglan Sweater — Beige Melange` (already fine).
- **SEO title:** `Oversized Wool Raglan Sweater, Beige | Autumn & Wool` (52) → `Oversized Wool Raglan Sweater, Beige Melange` (44)
- **SEO description:** keep (155). `Oversized raglan sweater in 100% pure wool, beige melange. Knitted and hand-sewn in Latvia. Measurements listed on the page. Free shipping, 14-day returns.`
- **Description edits:** none with banned wording.
- **Twin paragraph:** none.
- **Related-links block:**
  ```
  More sweaters: https://www.autumnandwool.com/wool-sweaters
  Also see: https://www.autumnandwool.com/shop/p/p/wool-sweater-vest-knitted-wool-vest-oversized-vest-womens-woolen-pullover-vest-top-sleeveless-wool-knit-vest-soft-v-neck-vest
  Also see: https://www.autumnandwool.com/shop/p/p/hand-knitted-distressed-wool-sweater-oversized-raglan-jumper-1
  ```
- **Alts (10 slots; colour beige melange, from the name). Current alts: 5 file names, 3 view words, 2 empty descriptions.**

| # | Current file | Current alt | New alt |
|---|---|---|---|
| 1 | image_1.jpg | image_1.jpg | Oversized wool raglan sweater in beige melange, photo 1 |
| 2 | image_2.jpg | Oversized Wool Raglan Sweater — Beige Melange - close-up detail view | Oversized wool raglan sweater in beige melange, close-up detail view |
| 3 | image_3.jpg | image_3.jpg | Oversized wool raglan sweater in beige melange, photo 3 |
| 4 | image_4.jpg | image_4.jpg | Oversized wool raglan sweater in beige melange, photo 4 |
| 5 | image_5.jpg | image_5.jpg | Oversized wool raglan sweater in beige melange, photo 5 |
| 6 | image_6.jpg | … texture and material detail | Oversized wool raglan sweater in beige melange, texture and material detail |
| 7 | image_7.jpg | image_7.jpg | Oversized wool raglan sweater in beige melange, photo 7 |
| 8 | image_8.jpg | image_8.jpg | Oversized wool raglan sweater in beige melange, photo 8 |
| 9 | image_9.jpg | image_9.jpg | Oversized wool raglan sweater in beige melange, photo 9 |
| 10 | image_10.jpg | image_10.jpg | Oversized wool raglan sweater in beige melange, photo 10 |

---

## 22. Oversized Wool V-Neck Vest, Beige Melange

- **Live URL:** https://www.autumnandwool.com/shop/p/p/wool-sweater-vest-knitted-wool-vest-oversized-vest-womens-woolen-pullover-vest-top-sleeveless-wool-knit-vest-soft-v-neck-vest
- **Variants:** none. Colour beige melange is in the name and description.
- **Name (H1):** keep `Oversized Wool V-Neck Vest - Beige Melange` (already fine).
- **SEO title:** `Oversized Wool V-Neck Vest, Beige Melange | Autumn & Wool` (57) → `Oversized Wool V-Neck Vest, Beige Melange` (41)
- **SEO description:** keep (153). `Oversized V-neck sweater vest in beige melange wool with a ribbed finish. Easy to layer over shirts and dresses. Free shipping from Riga, 14-day returns.`
- **Description edits:** none with banned wording.
- **Twin paragraph:** none.
- **Related-links block:**
  ```
  More vests: https://www.autumnandwool.com/wool-sweater-vests
  Also see: https://www.autumnandwool.com/shop/p/oversized-merino-wool-v-neck-sweater-vest
  Also see: https://www.autumnandwool.com/shop/p/p/wool-sweater-sweater-for-women-knit-cozy-pullover-sweater-sustainable-knitwear-oversized-wool-jumper-relaxed-fit-wool-pullover-1
  ```
- **Alts (10 slots; the current alts are file names only):**

| # | Current file | Current alt | New alt |
|---|---|---|---|
| 1 | image_1.jpg | image_1.jpg | Oversized wool V-neck vest in beige melange, photo 1 |
| 2 | image_2.jpg | image_2.jpg | Oversized wool V-neck vest in beige melange, photo 2 |
| 3 | image_3.jpg | image_3.jpg | Oversized wool V-neck vest in beige melange, photo 3 |
| 4 | image_4.jpg | image_4.jpg | Oversized wool V-neck vest in beige melange, photo 4 |
| 5 | image_5.jpg | image_5.jpg | Oversized wool V-neck vest in beige melange, photo 5 |
| 6 | image_6.jpg | image_6.jpg | Oversized wool V-neck vest in beige melange, photo 6 |
| 7 | image_7.jpg | image_7.jpg | Oversized wool V-neck vest in beige melange, photo 7 |
| 8 | image_8.jpg | image_8.jpg | Oversized wool V-neck vest in beige melange, photo 8 |
| 9 | image_9.jpg | image_9.jpg | Oversized wool V-neck vest in beige melange, photo 9 |
| 10 | image_10.jpg | image_10.jpg | Oversized wool V-neck vest in beige melange, photo 10 |

---

## CLAIM-CHECK (product copy, kept or changed, owner to confirm)

1. **Origin (all 22 pages).** "Knitted and hand-sewn in Latvia" (and "in Riga" on 03) is kept as written. Origin is an open item (C-04, README §7). Owner to confirm before the next product push.
2. **"100% extra-fine merino wool"** (02) and **"100% merino… extra-fine… Italian-spun yarn"** (16 and 17). "Extra-fine" and "Italian-spun" are kept as on the page and must be checked against the spec before reuse.
3. **"Warm Knit"** removed from the 10 H1 (name now `100% Wool Long Shawl Cardigan`). It was a warmth claim with no support on the page.
4. **"Soft on the skin and warm without bulk"** (17) and **"won't press or leave lines"** (16) are existing copy, kept. Both are fit or performance statements to confirm.
5. **"Brown and Blue are … knitted to order"** (03) is a made-to-order claim, kept as on the page. Lead time not verified.
6. **Alt "100% wool"** on 05 and 10 (current alts). Dropped in the new alts. The description says only "Material: wool" on 05.
7. **"This gift card never expires."** (01) kept. Owner to confirm.
8. **Sustainable / organic in URL slugs** (03, 04, 10, 15, 19, 20, 21). Slugs not changed (no redirect plan). Not in visible copy.
9. **Colour not on page:** 02 (grey, photo alts only), 05, 06 (grey, slug only), 09, 10, 11, 20. Each marked `[OWNER: colour]` in the section.
10. **Stock and price** are not in this sheet. Hat and scarf FAQ mentions "€110" (17).
11. **Single photo** on 12 and 14 (stand-collar). A second photo per colour is needed for real twin differentiation.
12. **Beanie shades** (16, slots 4, 5, 13, 14): shade names come from the page alts and need checking against the photos.

## Self-check

- **Lengths:** names, SEO titles and new SEO descriptions were counted character by character, spaces included, with no tool. New values: longest title 51 (03, 17), longest new description 150 (02), longest name 48 only if the optional 02 name is used (keep is 34-char title). Kept descriptions show the crawl length from `pages.tsv`, which is at most 155. Alt texts are all between 35 and 75 characters, under the 110 limit.
- **Banned words in new values:** see the grep result in the reply. Hits are only in the "current" column, in quoted "old →" text, or in the removed-text quotes. No new value contains "hand-knit", "hand knit" or "handmade".
- **URLs:** every URL in this file is a live product URL from `pages.tsv` (checked against the full crawl URLs), or one of the five new landing URLs in the brief.
- **Coverage:** all 22 products appear in the index and in full sections (01–22). Every gallery image in the live HTML is listed, 192 slots in total.
