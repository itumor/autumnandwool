# On-page SEO proposals, 2026-10-21 (DRAFT for owner approval)

Author: aw-seo-marketplace. Tasks SEO-12 (category copy), SEO-14 (H1s and alt text), SEO-15 (SEO titles and metas),
SEO-16 (colour-twin openings). Bulk-paste file: [2026-10-21-onpage-proposals.csv](2026-10-21-onpage-proposals.csv).

Rules applied: product data is frozen, so everything here is a proposal the owner pastes into Squarespace. Titles
≤ 60 characters, metas ≤ 155 (character counts include spaces). Facts come from `llms.txt`, the feed `D` list and the
17 Oct export. No "handmade", "made in Latvia", "sustainable", "extra-fine" or "Italian-spun" (gate G8). Returns
wording is left out of metas until the adviser answers (ruling C12). The dispatch time "2–5 working days" is the live
`llms.txt` wording; it changes everywhere at once if the owner's decision 3 changes it.
**Lane:** PDP body copy belongs to E-commerce/CRO. SEO title, meta, alt text, category intros and site H1s are mine.
The colour-twin opening lines (section E) are input for CRO to merge into its PDP copy, not a separate edit.
Current values marked `[VERIFY]` come from the 18 Oct QA report; GROWTH-PLAN S9 says some titles were fixed on
18–19 Oct, so the owner checks the current value before pasting.

## A. Site H1s (native block settings)

| Page | Issue (evidence) | Proposal | Layer |
|---|---|---|---|
| `/shop` | No H1; only H2 "Shop" (QA-REPORT §4, zero-sales #9) | Set the page header text block to Heading 1: **"The wool knitwear collection"** (keeps the design's "The collection" wording, adds the topic) | Native block |
| `/` | Second H1 "Autumn and wool" in a footer HTML block (QA-REPORT §2) | Change that block's text from Heading 1 to Paragraph (or Heading 4 for the look). Keep the hero H1 "Wool knitwear for cooler days" (the missing-space finding was a false positive, incident log round 2) | Native block |
| `/shop/sweaters`, `/cardigans`, `/vests` | No H1, no intro (fetch 21 Oct of `/shop/sweaters`: breadcrumb "All / Sweaters", no intro text) | Category description field with the intros in section D; H1 = category name if the template allows | Native category settings `[VERIFY the template shows a category description]` |

## B. SEO titles and meta descriptions

| Page | Current | Proposed SEO title (chars) | Proposed meta description (chars) |
|---|---|---|---|
| Home `/` | TODO `[VERIFY]` | Wool Knitwear for Women from Riga \| Autumn & Wool (49) | Autumn & Wool: women's wool and merino knitwear from a studio in Riga, by Kristine, formerly Mareshop on Etsy. Free shipping to eligible destinations. (150) |
| Shop `/shop` | "… \| Autumn & Wool — Autumn & Wool" (duplicate suffix, QA) `[VERIFY]` | Women's Wool Sweaters, Cardigans & Vests \| Autumn & Wool (56) | Wool sweaters, cardigans, sweater vests, merino beanies and hat-and-scarf sets for women, from a small knitwear studio in Riga. (127) |
| `/shop/sweaters` | "Sweaters — Shop wool sweaters, cardigans & accessories \| Autumn & Wool" (fetched 21 Oct, 72 chars, mentions cardigans on the sweaters page) | Wool Sweaters for Women: Merino & Lambswool \| Autumn & Wool (59) | Women's wool sweaters in merino, lambswool and pure new wool: oversized raglans, turtlenecks and crew necks from EUR 110. Ships from Riga. (138) |
| `/shop/cardigans` | TODO | Merino & Wool Cardigans for Women \| Autumn & Wool (49) | Women's wool cardigans: long shawl-collar and open-front styles in pure new wool, and a merino raglan cardigan in three colours. Ships from Riga. (145) |
| `/shop/vests` | TODO | Oversized Wool Sweater Vests for Women \| Autumn & Wool (54) | Oversized V-neck sweater vests in wool and merino wool, cut to layer over shirts and dresses. Garment measurements on every page. Ships from Riga. (146) |
| `/size-guide` | "Find Your Perfect Fit – Shop Now" (QA) `[VERIFY]` | Wool Size Chart & Knitwear Size Guide \| Autumn & Wool (53) | Wool size chart for women's knitwear: S–XL in cm and inches (EU 36–42, UK 8–14, US 6–12), fit types and how to measure. (119) |
| `/cart` | "Autumn & Wool" (generic, QA) | Your cart \| Autumn & Wool (25) | n/a (keep cart out of search; Squarespace already does not list it in the sitemap) |
| Vest PDP | "Oversized Merino Wool Sweater Vest" ≠ H1 (QA) | Oversized Merino Wool V-Neck Sweater Vest \| Autumn & Wool (57) | Oversized V-neck sweater vest in merino wool [CLAIM-CHECK] that layers over shirts and dresses. Width 59 cm, length 68 cm. Free shipping to eligible destinations. (148) |
| Merino Raglan Cardigan PDP | "Merino Wool Raglan Cardigan — Black, Brown or Blue \| Autumn & Wool" (handbook §5, 66 chars, cut in results) | Merino Raglan Cardigan, Black, Brown or Blue \| Autumn & Wool (60) | Relaxed raglan cardigan in merino wool [CLAIM-CHECK], in black, brown or blue. Width 61 cm, front length 67 cm. Free shipping to eligible destinations. (137) |
| Striped PDP | TODO | Oversized Merino Wool Sweater, Striped \| Autumn & Wool (54) | Oversized striped sweater in merino wool [CLAIM-CHECK] with Japanese-style shoulder shaping. Width 59 cm, front length 67 cm. Ships from Riga in 2–5 working days. (148) |
| Beanie PDP | TODO | Rib-Knit Merino Wool Beanie, Unisex \| Autumn & Wool (51) | Unisex rib-knit beanie in merino wool [CLAIM-CHECK] with a fold-over cuff. One size, fits 54–58 cm heads. 11 colours. Free shipping to eligible destinations. (143) |
| Hat & Scarf Set PDP | TODO | Merino Wool Hat and Scarf Set, Gift Idea \| Autumn & Wool (56) | Matching rib-knit beanie and scarf in merino wool [CLAIM-CHECK]. Beanie fits 54–58 cm heads, scarf about 190 × 36 cm. Black, gray or brown. Add a handwritten gift note. (154) |
| Oversized Wool Raglan Beige PDP | TODO | Oversized Wool Raglan Sweater, Beige Melange \| Autumn & Wool (60) | Oversized raglan sweater in beige melange, pure wool [CLAIM-CHECK], ribbed neck and cuffs. Width 59 cm, back length 69 cm. Free shipping to eligible destinations. (148) |

Checks: fibre wording copied from the feed `D` list; owner confirms it matches the live PDP (`aw-brand-voice` §3: copy
the PDP wording exactly). "Free shipping to eligible destinations" is the brand-voice approved line. The vest and set
metas drop "extra-fine" (CLAIM-CHECK). Prices left out of PDP metas so a price change cannot make them wrong.
Wave 3 (GM rulings W3-7, W3-8; A-GM-10, A-GM-22): fibre % removed from every meta ("merino wool", "pure wool", no
"100%", no "extra-fine") until a spec sheet/invoice clears G8; `[CLAIM-CHECK]` is a marker, delete it before pasting
(counts exclude it). Set meta: "Ships in gift packaging" replaced by "Add a handwritten gift note" (no gift wrap).

## C. Alt text, 5 working-set PDPs (Squarespace image editor → Alt text / filename)
The working set is provisional until decision 2 (24 Oct). I could not view the photos (no image access in this
session), so each line names the product and colour, and the owner fills the view in brackets after looking.
Pattern: `<Product> in <colour>, <view: front worn / back / detail of rib / flat lay>`. Keep under ~125 characters, no
"image of", no keyword lists.

| PDP | Image (file) | Proposed alt text |
|---|---|---|
| Vest | IMG_3336.JPEG | Oversized merino wool V-neck sweater vest, [VERIFY colour], [VERIFY view, e.g. worn over a white shirt, front] |
| Vest | IMG_3328 / 3333 / 3331.JPEG | Same pattern, one view each: back, side, rib detail `[VERIFY]` |
| Merino Raglan Cardigan | image_1.jpg | Black merino wool raglan cardigan, [VERIFY view, e.g. worn open, front] |
| Merino Raglan Cardigan | image_10.jpg | Brown merino wool raglan cardigan, [VERIFY view] (confirm this file is the brown one: feed QA F5) |
| Merino Raglan Cardigan | images 2–9, 11–14 | Black or brown (as shown), one view each `[VERIFY]` |
| Striped sweater | image_1–4.jpg | Oversized striped merino wool sweater, [VERIFY stripe colours], [VERIFY view] |
| Beanie | image_1–4.jpg | Rib-knit merino wool beanie in [VERIFY colour], [VERIFY: folded cuff, worn / flat] |
| Hat & Scarf Set | image_1–4.jpg | Merino wool rib-knit hat and scarf set in [VERIFY colour], [VERIFY view] |
| Shop grid tiles | `alt=""` on ~200 images (QA) | Squarespace fills product tile alt from the product image alt; fixing the PDP images fixes the grid `[VERIFY after first PDP]` |

"ChatGPT Image …" files on the shop page (QA §4): do not write alt text that describes them as product photos until
the owner confirms what they show and that we have the rights (decision 16).

## D. Category intros (60–120 words, category description field)

**Sweaters (≈ 95 words)**
> Sweaters in three fibres, each named on its product page: merino wool, lambswool and pure new wool. Choose an
> oversized raglan, a relaxed crew neck with side slits or a curved hem, a stand collar, or a lightweight merino
> turtleneck that sits closer to the body for layering. Sizes run S–XL (EU 36–42, UK 8–14, US 6–12), and several
> oversized styles are one size. Compare the measurements on each product page with a sweater you already own, or
> read the size guide. In-stock pieces leave Riga in 2–5 working days.

**Cardigans (≈ 85 words)**
> Four wool cardigans. Two long, open-front styles in pure new wool with a draped collar, a shorter open-front
> cardigan with ribbed side slits, and a relaxed merino raglan cardigan in black, brown or blue that you can wear open
> or buttoned. The long cardigans come in S–XL; the merino raglan has a relaxed, slightly oversized fit. Wear one over
> a turtleneck or a sweater vest. Fibre and garment measurements are on each product page, and the size guide explains
> each fit.

**Sweater vests (≈ 70 words)**
> Two oversized V-neck sweater vests for layering over shirts, dresses and long sleeves. One is merino wool [CLAIM-CHECK] with
> Japanese-style shoulder shaping, 59 cm wide and 68 cm long. The other is a wool vest in beige melange with a ribbed
> finish, 57 cm wide and 69 cm long. Both are cut loose and roomy. See the size guide for how our oversized pieces fit.

CLAIM-CHECK: none of the three uses origin or "handmade" claims. `[VERIFY]` that the vest fibre lines match the live
PDPs, and that the 13 sweaters still include all three fibres after the dedupe (decision 20).

**Beanies, Sets (1 product each):** no intro proposed. Options for decision 29: (a) hide both categories from the
Shop filter and keep the products in "Winter Wool Gifts"; (b) merge into one "Hats & scarves" category (beanie +
set = 2 products), which also fixes the home tile label mismatch (QA §2). I recommend (b), because the home tile already
says "Hats & scarves". Category URL changes need the redirect list rule: if the merged category gets a new slug,
301 the old one.

## E. Colour twins: distinct first lines (input for CRO PDP copy)
Shared specs stay identical. Only the first line changes, so Google sees two different pages.

| Product | Proposed opening line |
|---|---|
| Pure Wool Side-Slit Sweater — Camel | A round-neck sweater in warm camel, with side slits and a hem cut shorter at the front than at the back. |
| Pure Wool Side-Slit Sweater — Light Grey | The side-slit sweater in light grey: a quiet neutral with the same short-front, longer-back hem. |
| Pure Wool Stand-Collar Sweater — Beige | A beige sweater with a stand collar, for a warm neckline without a full turtleneck. |
| Pure Wool Stand-Collar Sweater — Blue | The stand-collar sweater in blue, the same clean shape with a raised neckline. |
| Lambswool Raglan Crew — Brown | A brown lambswool crew with raglan sleeves, ribbed cuffs and a gently curved hem. |
| Lambswool Raglan Crew — Green | The lambswool raglan crew in green, with the same ribbed cuffs and curved hem as the brown. |
| Women's Classic Lambswool Crew Sweater (grey) | The classic grey lambswool crew: raglan sleeves, ribbed cuffs, a gently curved hem. |

## F. Not proposed (and why)
- URL slugs: no change without an owner-approved redirect list (`aw-ecommerce-seo` guardrail; decision 35, Jan 2027).
- Rating or review schema: no real on-site reviews exist.
- robots.txt, sitemap, canonical on PDPs: verified correct on 19 Oct; no new evidence.
