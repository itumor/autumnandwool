# Content quality and on-page audit, re-audit 2026-11-11 (crawl-1111)

Scope: 49 pages from `crawl-1111/index.tsv`, raw HTML on disk, no live fetches. Visible main-content text via HTML parser; footer contact details checked separately. Word counts are approximate: the extractor's repeated-block cut removes duplicated product text, and FAQ/"Also see" blocks are still counted. Readability is a Flesch heuristic (syllable approximation).

## Scores

- **Content Quality: 55/100.** E-E-A-T on the skill model: Experience 60 (named maker, studio, dated Etsy history), Expertise 50 (guides are generic, no sources), Authoritativeness 30 (Etsy reviews only, no press or external citations), Trustworthiness 75 (full imprint, address, company number, returns and privacy pages). Weighted 20/25/25/30 = 55. Drags: home at 227 words, guides below the blog floor, six near-duplicate product pairs, one product with no returns line, two material lines with no fibre percentage.
- **On-Page: 62/100.** All 22 products have unique titles and descriptions of 128 to 155 characters; 41 of 49 pages have a meta description of 103 to 155 characters. Losses: /shop has no H1 and /home duplicates /. Platform-limited items (7 `/shop/<category>` pages: no H1, no description, canonical to /shop, templated titles over 60 characters) are scored at reduced weight. Internal linking is good.

Templated metadata (`metadata_template.py --pairs-file`, 49 pairs): site_risk **low**, templated_ratio **0.0**, shared_cta_phrases **none**, templated_count 0. Low-severity flags only: brand suffix in description (6 pages), missing metadata (7 category pages).

## Findings

| ID | Sev | Finding | URL | Evidence (quote) |
|---|---|---|---|---|
| C-01 | Medium | Homepage below 500-word homepage floor (227 unique words) | / | "Made slowly, by one pair of hands" section is the only story block; body is 227 words |
| C-02 | Medium | Five guides below 1,500-word blog floor (394 to 654 words) | /merino-vs-lambswool; /oversized-fit-guide; /how-to-choose-a-wool-cardigan; /how-to-wash-a-wool-sweater; /wool-gifts | merino-vs-lambswool 617 words; oversized-fit-guide 654 words |
| C-03 | Medium | Guide byline is a text line only: no author page, credentials, link, published date; no Article/Person markup | /how-to-wash-a-wool-sweater (x4 guides) | "By Kristine, designer and maker at Autumn & Wool · Updated 10 November 2026" |
| C-04 | Medium | /wool-gifts has no author, no date | /wool-gifts | "Wool gifts for her These ideas are arranged by budget." |
| C-05 | Medium | Fibre and fit claims in guides have no sources; zero external links in main content | /merino-vs-lambswool | "Merino fibres are generally finer than the wool of many other breeds" |
| C-06 | Medium | Near-duplicate product copy (colour twins and one same-colour duplicate). Full-text pairs >=0.85: six; description block >=0.85: three | /shop/p/p/hand-knitted-wool-stand-collar-sweater-womens-knitwear-679510 vs ...-679503; ...lambswool-sweater-womens-winter-knitwear-1 vs ...cozy-and-sustainable-...; ...wool-sweater-organic-knitwear-asymmetrical-design-1 vs ...womens-organic-knit-jumper-1; ...raglan-sweater-dusty-pink... vs ...merino-wool-sweater-oversize...turtleneck...679519 (desc 0.94) | Stand-collar: "The blue version is knitted from 100% pure new wool..." / beige: "Beige is the colour of this pure wool stand-collar sweater..." (0.89 full text). Dusty-pink raglan vs turtleneck: same "Oversized raglan sweater in dusty pink..." copy (0.94 description block) |
| C-07 | Medium | Product copy under 300 unique words (floor 300) | /shop/p/p/...679519 (270); ...-open-front-winter-sweater-679428 (261); ...striped-sweater-oversized-jumper (267); ...distressed-wool-sweater-oversized-raglan-jumper-1 (268); ...wool-sweater-sweater-for-women-...-1 (272); ...wool-sweater-vest-knitted-...soft-v-neck-vest (218); digital gift card (122) | Vest: "Oversized V-neck sweater vest in beige melange with a minimalist ribbed finish." (short description, no fit or care detail beyond the spec block) |
| C-08 | Medium | Material line lacks a fibre percentage on two products, contrary to the FAQ promise | /shop/p/p/hand-knitted-distressed-wool-sweater-oversized-raglan-jumper-1; /shop/p/p/wool-sweater-vest-knitted-wool-vest-...-soft-v-neck-vest | "Material: wool Fit: Oversized; designed to be roomy" / "Material: wool Fit: Oversized, relaxed." FAQ: "The exact fibre is listed on each product page." |
| C-09 | Medium | Returns wording conflict: merino raglan cardigan has no "DELIVERY & RETURNS" block and no 14-day line (20 of 22 products have it); its brown and blue colourways are made to order, which /shipping-returns lists as non-returnable | /shop/p/p/black-merino-wool-cardigan-100-merino-wool-raglan-sweater-minimalist-knitwear-sustainable-handmade-womens-cardigan-1; /shipping-returns | Product: "Brown and Blue are machine-knitted and hand-finished to order"; /shipping-returns: "Non-returnable items Custom or made-to-order pieces" |
| C-10 | Low | Process wording drift: one product and three site-wide strings use "machine-knitted and hand-finished in Riga" while most product pages say "Knitted on a manually operated knitting machine and hand-sewn in Latvia". No visible "handmade" or "hand-knitted" in body text (checked) | /shop/p/p/black-merino-...-cardigan-1; /; /shipping-returns; /shop/p/p/hand-knitted-wool-sweater-stand-collar-knit-679503 | Home: "Machine-knitted, hand-finished" / "Manual machine knit, hand-sewn in Riga"; cardigan: "machine-knitted and hand-finished in Riga" |
| C-11 | Medium | Sustainability claim with no evidence on site | /privacy-policy | "creating sustainable garments from 100% natural yarns" |
| C-12 | Low | Production-capacity claim that the crawl cannot verify | / | "Made slowly, by one pair of hands" |
| C-13 | Low | Only business email is a consumer Gmail address; no tel: link on the pages checked (home, category, product, guide, contact) | /contact; /imprint; /faq; /shipping-returns | "autumnandwool@gmail.com" (contact, imprint, FAQ, shipping); company SIA reg. 40203644965 is shown |
| C-14 | Low | Readability: home and wool landing pages have long sentences (FRE 27 home, 41 /wool-sweaters, 46 /wool-cardigans; 30 words per sentence on /wool-sweaters) | /; /wool-sweaters; /wool-cardigans | "Oversized sweaters, long cardigans and soft accessories in merino and wool..." |
| C-15 | Low | Landing pages are short (223 to 304 words); no defined floor, but they are the site's main category targets | /wool-sweaters (304); /wool-cardigans (239); /wool-hats-and-scarves (235); /wool-sweater-vests (227) | Sweater-vest landing text is 227 words |
| C-16 | Low | Thin landing text with the same return and shipping boilerplate repeated on each landing page | /wool-sweater-vests; /wool-hats-and-scarves | "Shipping is free to Latvia, the US and the destinations shown at checkout, and unworn, unwashed items..." |
| C-17 | Low | /shop/<category> grid pages carry 37 to 145 words (platform-limited, reduced weight) | /shop/beanies--hats (37); /shop/gift (39); /shop/sets (38); /shop/vests (48); /shop/cardigans (62); /shop/winter-wool-gifts (58); /shop/sweaters (145) | Grid text only: "Quick View ... €126.00" |
| C-18 | Medium | Cannibalisation: /shop/<category> vs /wool-* (platform, reduced weight). All seven /shop/<category> canonical to /shop. Site's own links go to /wool-*: home 4 tiles, guides 5 to 6 each, products 2 each. /shop/<category> gets in-site links only from /shop (6 tiles). Overlap pairs: sweaters, cardigans, vests, beanies--hats, gift + winter-wool-gifts, sets | /shop/sweaters vs /wool-sweaters; /shop/cardigans vs /wool-cardigans; /shop/gift vs /wool-gifts | Category canonical: "https://www.autumnandwool.com/shop"; home tile "Sweaters→" links /wool-sweaters |
| C-19 | Low | Structured data: Product schema on 22 product pages only; guides and FAQ have no Article, Person or FAQPage markup | /how-to-wash-a-wool-sweater; /faq | Only Organization, LocalBusiness and WebSite types found on these pages |
| O-01 | Medium | /shop has no H1 in raw HTML; the only heading is an H2 "The collection". Whether the H1 is editable on /shop is not confirmed | /shop | Title: "Shop wool sweaters, cardigans & accessories / Autumn & Wool" |
| O-02 | Low | /shop/<category> pages have no H1 (platform, reduced weight) | /shop/beanies--hats; /shop/cardigans; /shop/gift; /shop/sets; /shop/sweaters; /shop/vests; /shop/winter-wool-gifts | H2 only ("The collection") |
| O-03 | Medium | /shop/<category> pages have no meta description (platform, reduced weight; no editable field) | same 7 URLs | desc length 0 |
| O-04 | Low | /shop/<category> titles 66 to 79 characters with an identical suffix (templated); truncated in SERPs | same 7 URLs | "Winter Wool Gifts — Shop wool sweaters, cardigans & accessories / Autumn & Wool" (79) |
| O-05 | Medium | Duplicate: /home and / are identical in title, description, H1 and body; /home canonical points to root (canonical handles it, but the URL is still crawlable) | /home; / | Both: "Autumn & Wool / Wool sweaters and cardigans from Riga" |
| O-06 | Low | Brand name concatenated into description (metadata tool flag) | /about; /privacy-policy; /shipping-returns; /cookie-policy; /imprint; /shop | /shop: "Shop wool cardigans, sweaters, sweater vests, beanies and scarves at Autumn & Wool." |
| O-07 | Low | Weak H1s with no product or topic keyword | /faq ("Questions, answered"); /size-guide ("Find your fit"); /contact ("Let's talk wool"); /about ("Every stitch tells a story of patience and purpose") | H1 text as quoted |
| O-08 | Low | No H1 on legal page | /cookie-policy | H2 only |
| O-09 | Low | Brand spelling varies in meta text ("Autumn and Wool", "autumn and wool", "Autumn wool") vs "Autumn & Wool" elsewhere | /contact; /faq; /size-guide | "Find accurate size measurements for Autumn wool garments..." |
| O-10 | Info | All 22 product URLs carry a double /shop/p/p/ segment (platform artefact; observed, not scored) | all /shop/p/p/* products | URL path only |

Templated-metadata pass: `templated_count` 0. Duplicated product text is handled as C-06.

## Page table (49 rows)

Title and description lengths are character counts. Words are the unique main-content count after the repeated-block cut. Canonical "self" means the page points to itself.

| # | URL path | Title (len) | Meta description (len) | H1 | H2 | Words (approx.) | Canonical | Finding IDs |
|---|---|---|---|---|---|---|---|---|
| 1 | / | Autumn & Wool / Wool sweaters and cardigans from Riga (53) | 149 | 1: Wool knitwearfor cooler days | 4 | 227 | root (/) | C-01 C-15 O-05 |
| 2 | /about | About our Riga knitwear studio / Autumn & Wool (46) | 136 | 1: Every stitch tells a story of patience a | 3 | 255 | self | O-06 O-07 |
| 3 | /privacy-policy | Privacy policy / Autumn & Wool (30) | 103 | 1: Privacy policy | 9 | 370 | self | C-11 O-06 |
| 4 | /home | Autumn & Wool / Wool sweaters and cardigans from Riga (53) | 149 | 1: Wool knitwearfor cooler days | 4 | 227 | root (/) | O-05 |
| 5 | /shipping-returns | Shipping & returns / Autumn & Wool (34) | 143 | 1: Shipping & returns | 2 | 250 | self | O-06 |
| 6 | /contact | Contact our Riga studio / Autumn & Wool (39) | 135 | 1: Let's talk wool | 0 | 49 | self | C-13 O-09 |
| 7 | /size-guide | Knitwear Size Guide: Measurements and Fit (41) | 141 | 1: Find your fit | 5 | 387 | self | O-07 O-09 |
| 8 | /faq | Wool Knitwear FAQs: Sizing, Care and Returns (44) | 129 | 1: Questions, answered | 7 | 375 | self | C-13 O-07 O-09 |
| 9 | /cookie-policy | Cookie Policy / Autumn & Wool (29) | 128 | 0 (none) | 1 | 314 | self | O-06 O-08 |
| 10 | /imprint | Imprint / Autumn & Wool (23) | 108 | 1: Imprint | 0 | 78 | self | C-13 O-06 |
| 11 | /wool-sweaters | Wool Sweaters, Oversized and Relaxed / Autumn & Wool (52) | 125 | 1: Wool sweaters for layering and everyday  | 2 | 304 | self | C-15 C-16 |
| 12 | /wool-cardigans | Wool Cardigans, Long and Open-Front / Autumn & Wool (51) | 132 | 1: Wool cardigans for every day | 2 | 239 | self | C-15 C-16 |
| 13 | /wool-sweater-vests | Oversized Wool Sweater Vests / Autumn & Wool (44) | 150 | 1: Oversized sweater vests for layering | 2 | 227 | self | C-16 |
| 14 | /wool-hats-and-scarves | Merino Wool Beanies and Hat Sets / Autumn & Wool (48) | 136 | 1: Merino wool hats and scarves | 2 | 235 | self | C-16 |
| 15 | /wool-gifts | Wool Gifts for Her: A Christmas Guide / Autumn & Wool (53) | 122 | 1: Wool gifts for her | 8 | 394 | self | C-02 C-04 |
| 16 | /how-to-wash-a-wool-sweater | How to Wash a Wool Sweater at Home / Autumn & Wool (50) | 144 | 1: How to wash a wool sweater | 6 | 559 | self | C-02 C-03 C-05 C-19 |
| 17 | /merino-vs-lambswool | Merino or Lambswool: Which to Choose / Autumn & Wool (52) | 143 | 1: Merino or lambswool: which should you ch | 6 | 617 | self | C-02 C-03 C-05 C-19 |
| 18 | /oversized-fit-guide | Oversized Wool Sweater Fit Guide / Autumn & Wool (48) | 126 | 1: Oversized fit guide | 6 | 654 | self | C-02 C-03 C-05 C-19 |
| 19 | /how-to-choose-a-wool-cardigan | How to Choose a Wool Cardigan / Autumn & Wool (45) | 133 | 1: How to choose a wool cardigan | 6 | 581 | self | C-02 C-03 C-05 C-19 |
| 20 | /shop | Shop wool sweaters, cardigans & accessories / Autumn & Wool (59) | 152 | 0 (none) | 1 | 241 | /shop | O-01 O-06 C-18 |
| 21 | /shop/beanies--hats | Beanies — Shop wool sweaters, cardigans & accessories / Autumn & Wool (69) | 0 (missing) | 0 (none) | 1 | 37 | /shop | C-17 C-18 O-02 O-03 O-04 |
| 22 | /shop/cardigans | Cardigans — Shop wool sweaters, cardigans & accessories / Autumn & Woo (71) | 0 (missing) | 0 (none) | 1 | 62 | /shop | C-17 C-18 O-02 O-03 O-04 |
| 23 | /shop/gift | Gift — Shop wool sweaters, cardigans & accessories / Autumn & Wool (66) | 0 (missing) | 0 (none) | 1 | 39 | /shop | C-17 C-18 O-02 O-03 O-04 |
| 24 | /shop/sets | Sets — Shop wool sweaters, cardigans & accessories / Autumn & Wool (66) | 0 (missing) | 0 (none) | 1 | 38 | /shop | C-17 C-18 O-02 O-03 O-04 |
| 25 | /shop/sweaters | Sweaters — Shop wool sweaters, cardigans & accessories / Autumn & Wool (70) | 0 (missing) | 0 (none) | 1 | 145 | /shop | C-17 C-18 O-02 O-03 O-04 |
| 26 | /shop/vests | Vests — Shop wool sweaters, cardigans & accessories / Autumn & Wool (67) | 0 (missing) | 0 (none) | 1 | 48 | /shop | C-17 C-18 O-02 O-03 O-04 |
| 27 | /shop/winter-wool-gifts | Winter Wool Gifts — Shop wool sweaters, cardigans & accessories / Autu (79) | 0 (missing) | 0 (none) | 1 | 58 | /shop | C-17 C-18 O-02 O-03 O-04 |
| 28 | /shop/p/oversized-merino-wool-v-neck-sweater-vest | Oversized Merino Wool V-Neck Sweater Vest (41) | 150 | 1: Oversized Merino Wool V-Neck Sweater Ves | 0 | 467 | self | - |
| 29 | /shop/p/p/hand-knitted-merino-wool-raglan-sweater-dusty-pink-oversized-jumper | Merino Wool Raglan Sweater - Dusty Pink (39) | 134 | 1: Merino Wool Raglan Sweater - Dusty Pink | 1 | 345 | self | C-06 |
| 30 | /shop/p/p/merino-wool-sweater-oversize-sweater-knitted-wool-jumper-stand-up-collar-jumper-relaxed-fit-wool-pullover-warm-pink-jumper-679519 | Oversized Merino Turtleneck — Dusty Pink Raglan (47) | 147 | 1: Oversized Merino Turtleneck — Dusty Pink | 0 | 270 | self | C-06 C-07 |
| 31 | /shop/p/p/hand-knitted-wool-stand-collar-sweater-womens-knitwear-679510 | Pure Wool Stand-Collar Sweater - Blue (37) | 137 | 1: Pure Wool Stand-Collar Sweater - Blue | 0 | 594 | self | C-06 |
| 32 | /shop/p/p/hand-knitted-wool-sweater-stand-collar-knit-679503 | Pure Wool Stand-Collar Sweater - Beige (38) | 138 | 1: Pure Wool Stand-Collar Sweater - Beige | 0 | 614 | self | C-06 |
| 33 | /shop/p/p/merino-wool-turtleneck-sweater-womens-knit-pullover-soft-warm-lightweight-minimalist-sustainable-knitwear-sizes-sl-12-679428 | Lightweight Merino Turtleneck, 12 Colours (41) | 130 | 1: Lightweight Merino Turtleneck, 12 Colour | 0 | 384 | self | - |
| 34 | /shop/p/p/hand-knitted-wool-cardigan-open-front-winter-sweater-679428 | Open-Front Wool Cardigan with Side Slits (40) | 142 | 1: Open-Front Wool Cardigan with Side Slits | 0 | 261 | self | C-07 |
| 35 | /shop/p/p/wool-cardigan-warm-cardigan-organic-wool-wrap-winter-sweater-cardigan-women-cardigan-sweater-minimalist-style-sweater | Long Wool Cardigan with Shawl Collar (36) | 153 | 1: Long Wool Cardigan with Shawl Collar | 0 | 500 | self | C-06 |
| 36 | /shop/p/p/hand-knitted-wool-cardigan-minimalist-open-front-sweater-1 | 100% Wool Long Shawl Cardigan (29) | 150 | 1: 100% Wool Long Shawl Cardigan | 0 | 513 | self | C-06 |
| 37 | /shop/p/p/hand-knitted-merino-wool-striped-sweater-oversized-jumper | Merino Striped Oversized Sweater (32) | 146 | 1: Merino Striped Oversized Sweater | 0 | 267 | self | C-07 |
| 38 | /shop/p/p/hand-knitted-distressed-wool-sweater-oversized-raglan-jumper-1 | Distressed Oversized Wool Raglan Sweater (40) | 141 | 1: Distressed Oversized Wool Raglan Sweater | 0 | 268 | self | C-06 C-07 C-08 |
| 39 | /shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper | Women’s Classic Lambswool Crew Sweater (38) | 141 | 1: Women’s Classic Lambswool Crew Sweater | 0 | 413 | self | - |
| 40 | /shop/p/p/hand-knitted-lambswool-sweater-womens-winter-knitwear-1 | Lambswool Raglan Crew Sweater - Green (37) | 155 | 1: Lambswool Raglan Crew Sweater - Green | 0 | 622 | self | C-06 |
| 41 | /shop/p/p/cozy-and-sustainable-hand-knitted-lambswool-sweater-for-women | Lambswool Raglan Crew Sweater - Brown (37) | 155 | 1: Lambswool Raglan Crew Sweater - Brown | 0 | 636 | self | C-06 |
| 42 | /shop/p/p/hand-knitted-wool-sweater-organic-knitwear-asymmetrical-design-1 | Pure Wool Side-Slit Sweater - Light Grey (40) | 150 | 1: Pure Wool Side-Slit Sweater - Light Grey | 0 | 681 | self | C-06 |
| 43 | /shop/p/p/hand-knitted-wool-sweater-womens-organic-knit-jumper-1 | Pure Wool Side-Slit Sweater - Camel (35) | 145 | 1: Pure Wool Side-Slit Sweater - Camel | 0 | 674 | self | C-06 |
| 44 | /shop/p/p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1 | Merino Rib-Knit Beanie - Unisex (31) | 146 | 1: Merino Rib-Knit Beanie - Unisex | 0 | 495 | self | - |
| 45 | /shop/p/p/merino-wool-hat-scarf-set-extra-fine-rib-knit-soft-on-skin-warm-not-bulky-unisex-gift | Merino Wool Hat & Scarf Set (27) | 140 | 1: Merino Wool Hat & Scarf Set | 0 | 514 | self | - |
| 46 | /shop/p/p/wool-sweater-sweater-for-women-knit-cozy-pullover-sweater-sustainable-knitwear-oversized-wool-jumper-relaxed-fit-wool-pullover-1 | Oversized Wool Raglan Sweater — Beige Melange (45) | 155 | 1: Oversized Wool Raglan Sweater — Beige Me | 0 | 272 | self | C-06 C-07 |
| 47 | /shop/p/p/wool-sweater-vest-knitted-wool-vest-oversized-vest-womens-woolen-pullover-vest-top-sleeveless-wool-knit-vest-soft-v-neck-vest | Oversized Wool V-Neck Vest - Beige Melange (42) | 153 | 1: Oversized Wool V-Neck Vest - Beige Melan | 0 | 218 | self | C-07 C-08 |
| 48 | /shop/p/p/black-merino-wool-cardigan-100-merino-wool-raglan-sweater-minimalist-knitwear-sustainable-handmade-womens-cardigan-1 | Merino Wool Raglan Cardigan (27) | 149 | 1: Merino Wool Raglan Cardigan | 0 | 740 | self | C-09 C-10 |
| 49 | /shop/p/autumn-and-wool-digital-gift-card | Digital Gift Card for Wool Knitwear (35) | 128 | 1: Digital Gift Card for Wool Knitwear | 0 | 122 | self | C-07 |

## Internal links (summary)

- Products: 1 to 2 links to a /wool-* landing page each, 2 to 4 "Also see" links to related or colour-twin products, 0 links to /shop/<category>. Good.
- Guides link 3 to 7 products each and cross-link the other guides. Good.
- Home tiles link to /wool-* (4), not /shop/<category>.

## What is good

- Return and refund policy is consistent: 14 days, unworn and unwashed, buyer pays return postage unless damaged or incorrect, exchange = new order then return, across /, /about, /faq, /shipping-returns, the /wool-* landings, and /wool-gifts.
- Trust: imprint, cookie and privacy pages name the company (AUTUMN AND WOOL, SIA, reg. 40203644965) and street address in Riga; the footer shows the same email and address on every page checked (home, category, product, wool-gifts, contact).
- Etsy history is stated with a date ("as of November 2026") and the reviews are attributed to Etsy, not claimed on the site.
- Product copy shows fit, measurements, fibre and care on every product that has the spec block; prices match across home, /wool-* landings and product pages.
- Guides use answer-first questions and short direct answers, and four of five have a comparison or summary table.

## Could not verify

- Etsy figures (8,000+ orders, 4.9 from 1,400+ reviews, 15 years as Mareshop): not checked against Etsy; no live fetch was made.
- Actual production process (manual machine plus hand finishing) and "one pair of hands": not observable from HTML.
- Image alt text, photo originality, and rendered JavaScript content: not in the raw HTML extraction.
- Whether /shop H1 and category meta descriptions are editable: stated as platform facts in the brief; /shop H1 editability is unconfirmed.
- Word counts and readability are heuristics, and the repeated-block cut is approximate.
- Search Console and ranking data: not available to this audit.
