# Content quality (E-E-A-T) and on-page findings: autumnandwool.com, re-audit 2026-11-10

Scope: 49 pages from `evidence/seo-reaudit-2026-11-10/crawl-after` (raw HTML, read-only, no live fetches). Page text treated as untrusted data.

Method:
- Title, meta description, H1/H2, canonical: parsed from raw HTML (`<title>`, `meta[name=description]`, `link[rel=canonical]`, `<h1>`, `<h2>`).
- Word count: visible text inside `<main>` only (nav, header, footer, script, style, forms removed). Squarespace repeats product description blocks in the DOM, so a "de-dup" count also removes repeated sentences. The de-dup number is the one used for thresholds.
- Product similarity: visible description sentences only (price, "Image n of n", size lines and the spec block after "MEASUREMENTS/Material/CARE" removed). Ratio = difflib SequenceMatcher on the cleaned text.
- Metadata templating: `claude-seo run metadata_template.py --pairs-file` on all 49 {url,title,description} pairs.
- Readability: Flesch Reading Ease, heuristic syllable counter (indicative only).
- Extraction script: the earlier `extract.py` pointed at `crawl/` and hard-coded 9 files, so it was not reused. Replacement: `scratchpad/ea/extract2.py` (run with `python3 -I`).

## Scores (claude-seo rubric; E-E-A-T weights 20/25/25/30)

**Content Quality: 58/100.** Experience 70, Expertise 60, Authoritativeness 45, Trust 75 gives a weighted 63. Minus about 5 for templated product copy (identical spec and care blocks on 16 to 20 products) and 9 products under 300 words. Strengths: named maker, legal entity and address, consistent process wording, answer-first guides with tables. Weak point: Authoritativeness rests on Etsy claims that cannot be checked from the crawl.

**On-Page: 70/100.** Titles are unique on every page except the `/` and `/home` duplicate (product, landing and guide titles 27 to 53 chars). Meta descriptions run 103 to 155 chars. Exactly one H1 on 40 of 49 pages. Platform-limited items are weighted at reduced weight: 7 `/shop/<category>` pages have no H1 and no meta description and canonicalise to `/shop`, and their title suffix is shared. Main deductions: thin homepage and landing pages, one duplicated garment listing, and 9 thin products.

## Findings

Severity: high / medium / low / ok. Platform limit = not editable on Squarespace 7.1 here; weighted down.

### On-page (O-)
- **O-01 (medium)** Homepage `/` has 173 words against a 500-word homepage floor. Copy is mostly hero text, nav and CTAs. Evidence: "Wool knitwear for cooler days ... Shop the collection".
- **O-02 (high)** Duplicate garment. `/shop/p/p/hand-knitted-merino-wool-raglan-sweater-dusty-pink-oversized-jumper` ("Merino Wool Raglan Sweater - Dusty Pink", €155) and `/shop/p/p/merino-wool-sweater-oversize-...-warm-pink-jumper-679519` ("Oversized Merino Turtleneck — Dusty Pink Raglan", €155) have the same colour, price and copy ("Oversized raglan sweater in dusty pink ... Knitted on a manually operated knitting machine and hand-sewn in Latvia"). Description similarity 0.87. Owner decision: merge, or make the turtleneck and ribbed-neck differences explicit.
- **O-03 (medium)** Colour twins with templated copy. Green/brown lambswool (`...womens-winter-knitwear-1` vs `...for-women`): 0.86. Light grey/camel side-slit: 0.79. Blue/beige stand-collar: 0.77. Four product pairs clear 85% in total: dusty pink with turtleneck 0.87, dusty pink with distressed 0.86, green with brown 0.86, dusty pink with beige melange 0.85. Cross-links "Also made in beige / brown / camel" exist (positive). Fix: per-colour fit, feel or styling notes.
- **O-04 (medium-low)** Boilerplate spec blocks. "Knitted on a manually operated knitting machine and hand-sewn in Latvia." appears on 16 of 21 products. "CARE Hand wash gently in cool water with a mild wool detergent." on 18. "In-stock items ship from Riga within 2–5 working days." on 20.
- **O-05 (medium)** Thin products below the 300-word floor (de-dup): dusty pink raglan 267; turtleneck 679519 212; "Lightweight Merino Turtleneck, 12 Colours" 280; "Open-Front Wool Cardigan with Side Slits" 207; "Merino Striped Oversized Sweater" 208; "Distressed Oversized Wool Raglan Sweater" 212; "Women's Classic Lambswool Crew Sweater" 279; "Oversized Wool Raglan Sweater — Beige Melange" 214; "Oversized Wool V-Neck Vest - Beige Melange" 187. 19 of 21 physical products are under the 400-word bar for complex products.
- **O-06 (low-medium)** Raglan family reads as one template. Dusty pink, distressed and beige-melange raglans share an opener ("Oversized raglan sweater ... ribbed cuffs and a curved hem"). Pairwise 0.83 to 0.86. Titles for the distressed and grey lambswool omit colour.
- **O-07 (medium, platform limit, reduced weight)** `/shop/beanies--hats`, `/shop/cardigans`, `/shop/gift`, `/shop/sets`, `/shop/sweaters`, `/shop/vests`, `/shop/winter-wool-gifts`: no H1, no meta description, canonical to `https://www.autumnandwool.com/shop`. Titles 66 to 79 chars with shared suffix "— Shop wool sweaters, cardigans & accessories | Autumn & Wool" (truncation risk at 79). Not editable on this platform as stated in the brief.
- **O-08 (low)** `/shop` has no H1 (platform-template, probably with O-07). `/cookie-policy` has no H1 and is editable: add one.
- **O-09 (low, platform limit)** Intent overlap between `/wool-*` landings and `/shop/<category>`: sweaters, cardigans, vests, hats (beanies/sets), gifts (gift/winter-wool-gifts). Site-internal links point to `/wool-*` (for example, product breadcrumbs "More sweaters: wool sweaters" and every guide), and `/shop/<category>` is linked only from `/shop`. Canonicals to `/shop` remove the conflict. Verdict: no live cannibalisation, but duplicate intent exists in the sitemap-level structure. The `/shop/<category>` H1/meta cannot be changed here.
- **O-10 (medium)** Landing pages are thin: `/wool-sweaters` 300, `/wool-cardigans` 239, `/wool-sweater-vests` 223, `/wool-hats-and-scarves` 231 words. The 800-word service-page floor is a reference only, not a rule for these pages. Each has one H1 and two H2s.
- **O-11 (low)** Internal linking works. Products link to the twin and the category (5 to 7 product links each on sweaters). Guides link to 3 to 6 products each (for example `/merino-vs-lambswool` 6). Category-to-guide links present. Positive.
- **O-12 (low)** `/size-guide` (387 words, one table) and `/oversized-fit-guide` (654 words) overlap on fit and measurement intent. Cross-links exist (`oversized-fit-guide` links to `/size-guide`). Keep both; make the size guide the reference table and the fit guide the how-to.
- **O-13 (low)** Guides are 559 to 654 words (`how-to-wash-a-wool-sweater` 559, `merino-vs-lambswool` 617, `oversized-fit-guide` 654, `how-to-choose-a-wool-cardigan` 581). They are below the 1,500 blog-post floor if classed as blog posts. They are focused guides, not blog posts, so this is a classification note, not a defect.
- **O-14 (low)** `/wool-hats-and-scarves`: title "Merino Wool Beanies and Hat Sets" does not match H1 "Merino wool hats and scarves". Align the title with the H1 and the scarf content.
- **O-15 (low)** `/home` and `/` are both crawlable with identical title and description. The canonical on `/home` points to `/` (correct). A 301 from `/home` to `/` is cleaner.
- **O-16 (low, tool heuristic)** `metadata_template.py` flags the brand name in descriptions on 10 pages (`/about`, `/privacy-policy`, `/shipping-returns`, `/cookie-policy`, `/imprint`, `/shop`, and 4 products). In most it is a real sentence subject ("Discover Autumn & Wool, a Riga-based knitwear brand..."), not a concatenation artefact. Low; optional edit.
- **O-17 (info)** Site-wide templating check: `templated_ratio` 0.0 (0 of 49), `site_risk` low, `shared_cta_phrases` none. The only shared template is the `/shop/<category>` title suffix (O-07). Method is heuristic.

### Content, E-E-A-T and AI-citation (C-)
- **C-01 (medium)** Maker identity is clear: Kristine (designer and maker), Riga studio, "family tradition of knitting" (`/about`). The About page is 170 words and has no portrait, credentials or process photos described in text. Experience and Expertise are asserted more than shown. Photos cannot be verified from HTML.
- **C-02 (ok)** Process wording is consistent. Home: "each piece knitted on a manual machine and finished by hand". Shipping: "machine-knitted and hand-finished". Products: "Knitted on a manually operated knitting machine and hand-sewn in Latvia". Black cardigan: "machine-knitted and hand-finished in Riga". The words "handmade" and "hand-knitted" appear only in URL slugs (checked visible text). Minor: Riga and Latvia are used interchangeably.
- **C-03 (medium)** Review and sales claims: "4.9 from 1,400+ reviews on Etsy" and "8,000+ orders on Etsy" on `/` and `/about`. The only outbound link is `https://www.etsy.com/shop/mareshop` (2 links on `/`, 1 on `/about`). Counts cannot be verified from the crawl. No third-party press, awards or certifications on site.
- **C-04 (low)** Returns: "Unworn, unused items can be returned within 14 days" is clear. Refund step says "Within 7 business days after we receive and approve it. Shipping costs not included." Who pays return postage is not stated.
- **C-05 (medium-low)** Guides carry "By Kristine, designer and maker at Autumn & Wool · Updated 10 November 2026". There is no author bio link and no original publish date. All four guides show the identical "Updated" date, which can look like a bulk stamp. Legal pages show "Last updated: 1 November 2026".
- **C-06 (ok)** Guide quality is good. Each guide answers in the first paragraph ("Merino wool is fleece from merino sheep, and it is generally finer..."). Each has one table, H2 questions and product links. Fibre facts check out (lambswool from young sheep at first shearing; neither fibre automatically warmer).
- **C-07 (low)** Readability (Flesch, heuristic): guides 62 to 76, product copy about 74, `/about` about 49, `/wool-sweaters` about 42 (average sentence about 30 words). Acceptable for consumer copy; the landing page is the hardest read.
- **C-08 (medium)** AI-template risk (QRG: repetitive structure across pages, generic phrasing). Product bodies repeat a fixed skeleton (spec, care, delivery) with stock phrases ("clean, timeless shape", "relaxed fit", "ready to wear"). Counter-evidence (positive): model height and size worn, garment measurements per size, and the twin cross-links are specific and first-hand.
- **C-09 (low)** Structured data: Organization, LocalBusiness and WebSite on every page checked. Product with AggregateOffer on product pages (price, InStock). No AggregateRating or Review despite the review claims. No FAQPage on `/faq`. Guides have no Article or author markup.
- **C-10 (ok)** Prices agree across pages: beanie €45, hat-and-scarf set €110, stand-collar €136, cardigan €145, raglan €155, striped €165, black cardigan €160.
- **C-11 (ok)** AI-citation readiness is good. `llms.txt` exists and states the legal entity, address and making process. Guides and FAQ use question headings and answer-first paragraphs. Gaps: product facts sit in prose, not in a spec table, and there is no FAQPage markup.
- **C-12 (low)** Contact: email `autumnandwool@gmail.com`, Instagram DM, studio address and legal entity (AUTUMN AND WOOL, SIA, reg. 40203644965) on `/contact`, `/imprint` and `/cookie-policy`. No phone number. Reply time stated as 1 to 2 business days.

## What is good
- Named maker, legal entity, registration number and street address on `/imprint`, `/contact` and `/cookie-policy`.
- Consistent making claims across pages (C-02). Shipping and returns terms are concrete (free to Latvia, US and listed destinations; 2 to 5 working days in stock; 14-day returns).
- Unique titles and descriptions on all non-platform pages. No templated CTA across descriptions (tool: 0 of 49).
- Answer-first guides with specific, accurate fibre and fit advice, one table each, and links into products.
- Twin products cross-link ("Also made in beige"). Category links from products and guides are present.
- `/size-guide` with a table and per-size measurements; garment measurements on every product.

## What I could not verify
- Etsy review count (1,400+), order count (8,000+), 4.9 rating and the 15 years on Etsy. Only the link exists.
- Photo quality, whether product photos are first-hand, alt text quality, and studio imagery (HTML only).
- Whether `/shop/<category>` product grids render. Raw HTML shows "No results found" on `/shop/beanies--hats` (grid likely JavaScript-loaded). Live rendering was not done (read-only, crawl only).
- Pixel-based SERP truncation (character counts only).
- Who pays return postage (not stated in the crawl).
- Whether the 10 November "Updated" stamp reflects a real edit (no revision history in the crawl).
- Stock status, variant availability and whether colour twins have separate stock.
- Flesch scores are heuristic, not a validated tool.
- The homepage H1 renders as "Wool knitwear / for cooler days" from a `<br>`. The concatenated text in the extract is an extraction artefact, not a finding.

## Page table (49 rows)
Canonical "self" means it points to itself. "Words raw / de-dup" is main-content words before and after removing repeated sentences. Finding IDs refer to the list above.

| # | URL (path) | Title (len) | Meta desc (len) | H1 | H2 | Words raw / de-dup | Canonical | Severity | Finding IDs | Evidence (quoted) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `/` | Autumn & Wool / Wool sweaters and cardigans from Riga (53) | 149 | 1 | 4 | 173 / 173 | self | medium | O-01, C-03, O-15 | "Wool knitwear for cooler days"; 173 words; "from 1,400+ reviews on Etsy" |
| 2 | `/about` | About our Riga knitwear studio / Autumn & Wool (46) | 136 | 1 | 3 | 170 / 170 | self | medium | C-01, C-03, C-12 | 170 words; "Kristine designs every piece, inspired by a family tradition of knitting"; "8,000+ orders on Etsy" |
| 3 | `/privacy-policy` | Privacy policy / Autumn & Wool (30) | 103 | 1 | 9 | 370 / 370 | self | ok | O-16 | 370 words; contact autumnandwool@gmail.com |
| 4 | `/home` | Autumn & Wool / Wool sweaters and cardigans from Riga (53) | 149 | 1 | 4 | 173 / 173 | -> / | low | O-15 | Same title/description as /; canonical -> / |
| 5 | `/shipping-returns` | Shipping & returns / Autumn & Wool (34) | 143 | 1 | 2 | 246 / 246 | self | low | C-04 | "Unworn, unused items can be returned within 14 days"; "Shipping costs not included" |
| 6 | `/contact` | Contact our Riga studio / Autumn & Wool (39) | 135 | 1 | 0 | 49 / 49 | self | low | C-12 | 49 words; email, Instagram DM, Braslas iela 22d; no phone |
| 7 | `/size-guide` | Knitwear Size Guide: Measurements and Fit (41) | 141 | 1 | 5 | 387 / 387 | self | ok | O-12 | 387 words, one table; "Find your fit" |
| 8 | `/faq` | Wool Knitwear FAQs: Sizing, Care and Returns (44) | 129 | 1 | 7 | 376 / 376 | self | ok | C-09 | 376 words; "Made-to-order items ship within the time shown on the product page" |
| 9 | `/cookie-policy` | Cookie Policy / Autumn & Wool (29) | 128 | 0 | 1 | 314 / 314 | self | low | O-08 | No H1; "Last updated: 1 November 2026" |
| 10 | `/imprint` | Imprint / Autumn & Wool (23) | 108 | 1 | 0 | 78 / 78 | self | ok | C-12 | AUTUMN AND WOOL, SIA, reg. 40203644965 |
| 11 | `/wool-sweaters` | Wool Sweaters, Oversized and Relaxed / Autumn & Wool (52) | 125 | 1 | 2 | 300 / 300 | self | medium | O-10, C-07 | 300 words; H1 "Wool sweaters for layering and everyday wear"; FRE ~42 |
| 12 | `/wool-cardigans` | Wool Cardigans, Long and Open-Front / Autumn & Wool (51) | 132 | 1 | 2 | 239 / 239 | self | medium | O-10, O-09 | 239 words; H1 "Wool cardigans for every day" |
| 13 | `/wool-sweater-vests` | Oversized Wool Sweater Vests / Autumn & Wool (44) | 150 | 1 | 2 | 223 / 223 | self | medium | O-10 | 223 words; H1 "Oversized sweater vests for layering" |
| 14 | `/wool-hats-and-scarves` | Merino Wool Beanies and Hat Sets / Autumn & Wool (48) | 136 | 1 | 2 | 231 / 231 | self | medium | O-10, O-14 | 231 words; title "Merino Wool Beanies and Hat Sets" vs H1 "Merino wool hats and scarves" |
| 15 | `/wool-gifts` | Wool Gifts for Her: A Christmas Guide / Autumn & Wool (53) | 122 | 1 | 8 | 390 / 390 | self | low | O-09 | 390 words; prices match product pages (€45, €110, €25+) |
| 16 | `/how-to-wash-a-wool-sweater` | How to Wash a Wool Sweater at Home / Autumn & Wool (50) | 144 | 1 | 6 | 559 / 559 | self | low | O-13, C-05, C-06 | 559 words; "Updated 10 November 2026"; answer in first paragraph; one table |
| 17 | `/merino-vs-lambswool` | Merino or Lambswool: Which to Choose / Autumn & Wool (52) | 143 | 1 | 6 | 617 / 617 | self | low | O-13, C-05, C-06 | 617 words; "Merino ... generally finer ... Lambswool ... usually taken at their first shearing" |
| 18 | `/oversized-fit-guide` | Oversized Wool Sweater Fit Guide / Autumn & Wool (48) | 126 | 1 | 6 | 654 / 654 | self | low | O-12, O-13, C-05 | 654 words; answer first; one table |
| 19 | `/how-to-choose-a-wool-cardigan` | How to Choose a Wool Cardigan / Autumn & Wool (45) | 133 | 1 | 6 | 581 / 581 | self | low | O-13, C-05, C-06 | 581 words; answer first; one table |
| 20 | `/shop` | Shop wool sweaters, cardigans & accessories / Autumn & Wool (59) | 152 | 0 | 1 | 241 / 241 | self | medium | O-08, O-07 | 241 words; no H1; 7 links to /shop/<category> only |
| 21 | `/shop/beanies--hats` | Beanies — Shop wool sweaters, cardigans & accessories / Autumn & Wool (69) | MISSING | 0 | 1 | 37 / 37 | -> /shop | medium | O-07, O-09 | PLATFORM: no H1, no meta, canonical -> /shop; title 69 chars; raw HTML "No results found" (grid likely JS, unverified) |
| 22 | `/shop/cardigans` | Cardigans — Shop wool sweaters, cardigans & accessories / Autumn & Wool (71) | MISSING | 0 | 1 | 62 / 62 | -> /shop | medium | O-07, O-09 | PLATFORM: no H1/meta, canonical -> /shop; title 71 chars; competes with /wool-cardigans |
| 23 | `/shop/gift` | Gift — Shop wool sweaters, cardigans & accessories / Autumn & Wool (66) | MISSING | 0 | 1 | 39 / 39 | -> /shop | medium | O-07, O-09 | PLATFORM: no H1/meta, canonical -> /shop; title 66 chars; competes with /wool-gifts |
| 24 | `/shop/sets` | Sets — Shop wool sweaters, cardigans & accessories / Autumn & Wool (66) | MISSING | 0 | 1 | 38 / 38 | -> /shop | medium | O-07 | PLATFORM: no H1/meta, canonical -> /shop; 38 words raw |
| 25 | `/shop/sweaters` | Sweaters — Shop wool sweaters, cardigans & accessories / Autumn & Wool (70) | MISSING | 0 | 1 | 145 / 145 | -> /shop | medium | O-07, O-09 | PLATFORM: no H1/meta, canonical -> /shop; title 70 chars; competes with /wool-sweaters |
| 26 | `/shop/vests` | Vests — Shop wool sweaters, cardigans & accessories / Autumn & Wool (67) | MISSING | 0 | 1 | 48 / 48 | -> /shop | medium | O-07, O-09 | PLATFORM: no H1/meta, canonical -> /shop; title 67 chars; competes with /wool-sweater-vests |
| 27 | `/shop/winter-wool-gifts` | Winter Wool Gifts — Shop wool sweaters, cardigans & accessories / Autumn & Wool (79) | MISSING | 0 | 1 | 58 / 58 | -> /shop | medium | O-07, O-09 | PLATFORM: no H1/meta, canonical -> /shop; title 79 chars (SERP truncation); competes with /wool-gifts |
| 28 | `/shop/p/oversized-merino-wool-v-neck-sweater-vest` | Oversized Merino Wool V-Neck Sweater Vest (41) | 150 | 1 | 0 | 507 / 316 | self | low | O-05 | 316 words de-dup; "Oversized Merino Wool V-Neck Vest" title 41 chars |
| 29 | `/shop/p/p/hand-knitted-merino-wool-raglan-sweater-dusty-pink-oversized-jumper` | Merino Wool Raglan Sweater - Dusty Pink (39) | 134 | 1 | 1 | 381 / 267 | self | high | O-02, O-05, O-06 | "Merino Wool Raglan Sweater - Dusty Pink" €155, 267 words; same colour and price as warm-pink-jumper-679519; description similarity 0.87 |
| 30 | `/shop/p/p/merino-wool-sweater-oversize-sweater-knitted-wool-jumper-stand-up-collar-jumper-relaxed-fit-wool-pullover-warm-pink-jumper-679519` | Oversized Merino Turtleneck — Dusty Pink Raglan (47) | 147 | 1 | 0 | 306 / 212 | self | high | O-02, O-05 | "Oversized Merino Turtleneck — Dusty Pink Raglan" €155, 212 words; "Oversized raglan sweater in dusty pink" |
| 31 | `/shop/p/p/hand-knitted-wool-stand-collar-sweater-womens-knitwear-679510` | Pure Wool Stand-Collar Sweater - Blue (37) | 137 | 1 | 0 | 598 / 336 | self | medium | O-03, O-04 | "Pure Wool Stand-Collar Sweater - Blue" €136; "Also made in beige"; similarity to beige 0.77 |
| 32 | `/shop/p/p/hand-knitted-wool-sweater-stand-collar-knit-679503` | Pure Wool Stand-Collar Sweater - Beige (38) | 138 | 1 | 0 | 618 / 357 | self | medium | O-03, O-04 | "Pure Wool Stand-Collar Sweater - Beige" €136; "Also made in blue" |
| 33 | `/shop/p/p/merino-wool-turtleneck-sweater-womens-knit-pullover-soft-warm-lightweight-minimalist-sustainable-knitwear-sizes-sl-12-679428` | Lightweight Merino Turtleneck, 12 Colours (41) | 130 | 1 | 0 | 420 / 280 | self | medium | O-05 | "Lightweight Merino Turtleneck, 12 Colours" €110, 280 words |
| 34 | `/shop/p/p/hand-knitted-wool-cardigan-open-front-winter-sweater-679428` | Open-Front Wool Cardigan with Side Slits (40) | 142 | 1 | 0 | 297 / 207 | self | medium | O-05 | "Open-Front Wool Cardigan with Side Slits" €155, 207 words |
| 35 | `/shop/p/p/wool-cardigan-warm-cardigan-organic-wool-wrap-winter-sweater-cardigan-women-cardigan-sweater-minimalist-style-sweater` | Long Wool Cardigan with Shawl Collar (36) | 153 | 1 | 0 | 536 / 331 | self | low | O-06 | "Long Wool Cardigan with Shawl Collar" €145, 331 words; similar to 100% Wool Long Shawl Cardigan (0.72) |
| 36 | `/shop/p/p/hand-knitted-wool-cardigan-minimalist-open-front-sweater-1` | 100% Wool Long Shawl Cardigan (29) | 150 | 1 | 0 | 549 / 337 | self | low | O-06 | "100% Wool Long Shawl Cardigan" €145, 337 words; "A similar long cardigan is listed" cross-link |
| 37 | `/shop/p/p/hand-knitted-merino-wool-striped-sweater-oversized-jumper` | Merino Striped Oversized Sweater (32) | 146 | 1 | 0 | 299 / 208 | self | medium | O-05 | "Merino Striped Oversized Sweater" €165, 208 words |
| 38 | `/shop/p/p/hand-knitted-distressed-wool-sweater-oversized-raglan-jumper-1` | Distressed Oversized Wool Raglan Sweater (40) | 141 | 1 | 0 | 308 / 212 | self | medium | O-05, O-06 | "Distressed Oversized Wool Raglan Sweater" €155, 212 words; similar to dusty pink raglan (0.86) |
| 39 | `/shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper` | Women’s Classic Lambswool Crew Sweater (38) | 141 | 1 | 0 | 445 / 279 | self | medium | O-05 | "Women’s Classic Lambswool Crew Sweater" €136, 279 words; no colour in title |
| 40 | `/shop/p/p/hand-knitted-lambswool-sweater-womens-winter-knitwear-1` | Lambswool Raglan Crew Sweater - Green (37) | 155 | 1 | 0 | 650 / 376 | self | medium | O-03, O-04 | "Lambswool Raglan Crew Sweater - Green" €136; "Also made in brown"; similarity to brown 0.86 (highest twin pair) |
| 41 | `/shop/p/p/cozy-and-sustainable-hand-knitted-lambswool-sweater-for-women` | Lambswool Raglan Crew Sweater - Brown (37) | 155 | 1 | 0 | 668 / 385 | self | medium | O-03, O-04 | "Lambswool Raglan Crew Sweater - Brown" €136; "See the green version too"; similarity to green 0.86 |
| 42 | `/shop/p/p/hand-knitted-wool-sweater-organic-knitwear-asymmetrical-design-1` | Pure Wool Side-Slit Sweater - Light Grey (40) | 150 | 1 | 0 | 709 / 396 | self | low | O-03 | "Pure Wool Side-Slit Sweater - Light Grey" €136, 396 words; "Also made in camel" |
| 43 | `/shop/p/p/hand-knitted-wool-sweater-womens-organic-knit-jumper-1` | Pure Wool Side-Slit Sweater - Camel (35) | 145 | 1 | 0 | 702 / 407 | self | low | O-03 | "Pure Wool Side-Slit Sweater - Camel" €136, 407 words; "See the light grey version" |
| 44 | `/shop/p/p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1` | Merino Rib-Knit Beanie - Unisex (31) | 146 | 1 | 0 | 567 / 361 | self | ok | C-09 | "Merino Rib-Knit Beanie - Unisex" €45, 361 words; "fits 54–58 cm heads" |
| 45 | `/shop/p/p/merino-wool-hat-scarf-set-extra-fine-rib-knit-soft-on-skin-warm-not-bulky-unisex-gift` | Merino Wool Hat & Scarf Set (27) | 140 | 1 | 0 | 582 / 359 | self | low | O-05 | "Merino Wool Hat & Scarf Set" €110, 359 words; FAQ "At the current price of €110" |
| 46 | `/shop/p/p/wool-sweater-sweater-for-women-knit-cozy-pullover-sweater-sustainable-knitwear-oversized-wool-jumper-relaxed-fit-wool-pullover-1` | Oversized Wool Raglan Sweater — Beige Melange (45) | 155 | 1 | 0 | 312 / 214 | self | medium | O-05, O-06 | "Oversized Wool Raglan Sweater — Beige Melange" €155, 214 words |
| 47 | `/shop/p/p/wool-sweater-vest-knitted-wool-vest-oversized-vest-womens-woolen-pullover-vest-top-sleeveless-wool-knit-vest-soft-v-neck-vest` | Oversized Wool V-Neck Vest - Beige Melange (42) | 153 | 1 | 0 | 258 / 187 | self | medium | O-05 | "Oversized Wool V-Neck Vest - Beige Melange" €126, 187 words; thinnest product |
| 48 | `/shop/p/p/black-merino-wool-cardigan-100-merino-wool-raglan-sweater-minimalist-knitwear-sustainable-handmade-womens-cardigan-1` | Merino Wool Raglan Cardigan (27) | 149 | 1 | 0 | 796 / 464 | self | ok | C-02 | "machine-knitted and hand-finished in Riga"; "handmade" only in URL slug; €160, 464 words |
| 49 | `/shop/p/autumn-and-wool-digital-gift-card` | Digital Gift Card for Wool Knitwear (35) | 128 | 1 | 0 | 130 / 105 | self | low | C-09 | Gift card, 105 words; €25–€250 values |
