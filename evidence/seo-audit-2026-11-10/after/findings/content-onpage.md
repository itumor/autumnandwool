# Content Quality and On-Page SEO re-audit: autumnandwool.com (2026-11-10, after the new pages)

Scope: the fresh crawl at `after/crawl/` (`pages.tsv`, 59 rows; `html/*.html`). Same rubric as the first audit (`../findings/content-onpage.md` in the parent folder). No live fetch. Nothing edited except this file.

Path shorthand: `H/` = `after/crawl/html/https-www-autumnandwool-com-`. Before-state = `evidence/seo-audit-2026-11-10/crawl/` (first crawl, used only for diffs).

Method notes:
- Product descriptions are de-duplicated (the DOM repeats each description twice). Word counts are from the unique description blocks, measured the same way for before and after.
- Similarity is 5-gram containment and Jaccard on those description blocks.
- The repo's `metadata_template.py` (42 metas) and `content_quality.py` were run. `content_quality.py` still gives 96 on `wool-gifts`, `wool-sweater-vests` and `how-to-wash-a-wool-sweater`, so it does not separate pages.
- The first audit's rewrite table is a proposal, not a record of what was published. Its text is compared only where the live HTML matches it.

## Scores

| Category | First audit | Now | Change |
|---|---|---|---|
| Content Quality | 55 | **61** | +6 |
| On-Page SEO | 40 | **56** | +16 |

Content Quality, point by point (55 to 61):
- +6 guides published and accurate. `how-to-wash-a-wool-sweater`, `merino-vs-lambswool`, `oversized-fit-guide` and `how-to-choose-a-wool-cardigan` (370 to 410 words each) state fibre, fit, price and care facts that match the product pages, the size-guide chart and the FAQ. I checked each against the source.
- +3 claim wording partly aligned (C-04). "handmade" is gone from the home title and meta. About and product copy now say "knitted on a manual knitting machine". Visible "made in Latvia" and "handmade" remain (see C-04).
- +1 Etsy source linked from home and about (C-05). The figures themselves are still unverified.
- +1 colour twins now differ by one colour sentence (C-03). Otherwise the bodies are still near-identical.
- -3 new factual or claim errors in the new copy: the hat page's "manual machine ... finished by hand" claim (N-02), the gift page's "packed by hand ... sent with tracking" line for digital cards (N-03), and the unsupported "Christmas" title (N-04).
- -2 new boilerplate across the nine pages, an orphaned guide cluster, and two thin landing pages (N-07, N-10, N-11).
- Not credited: product descriptions (median 174.5 to 184.5 words, still 21 of 22 under 300), category intro copy (none), the about page's thin maker section, dates, and FAQ depth.

On-Page SEO, point by point (40 to 56):
- +8 product pages now link to related products and their category page (O-04). Each product has two or three related-product links and a "More sweaters: ..." link to a landing page.
- +2 product titles are now 53 characters or fewer (O-06).
- +2 privacy, about, contact and FAQ titles and the privacy meta are rewritten (O-11).
- +1 the "Explore..." meta openers are gone and the gift card H1 is specific (O-12).
- +1 every image tag has an alt attribute (O-15).
- +1 the old product URL now 301s instead of 404 (O-18).
- +6 nine new landing pages. Each has a unique title (44 to 53 characters), a meta of 122 to 150 characters, one H1 and a self-referencing canonical, and is listed in the sitemap.
- -2 the new landing pages duplicate the intent of the category URLs (N-01).
- -1 brand name written three ways in metas, and product titles lost the brand suffix (N-08).
- -1 "Free shipping, 14-day returns." now in 11 metas, up from 8 (O-10).
- Not credited: O-01 (the seven category canonicals still point to /shop, still critical), O-02, O-03, and the category titles (O-05). These pages are still the weakest on-page URLs, and the new landing pages do not change that.

## First-audit findings: status

Status values: FIXED, PARTLY FIXED, OPEN, NOT FIXABLE ON PLATFORM. Counts: FIXED 6, PARTLY FIXED 5, NOT FIXABLE 1, OPEN 17 (29 total).

### Content Quality

| ID | Status | Fresh evidence |
|---|---|---|
| C-01 | PARTLY FIXED | Four guides exist, and a gift guide: `H/how-to-wash-a-wool-sweater.html` (422 words), `H/merino-vs-lambswool.html` (460), `H/oversized-fit-guide.html` (444), `H/how-to-choose-a-wool-cardigan.html` (444). `/blog` is still a 404 in `pages.tsv`. Linking is partial: the guides link to categories and products, but nothing in the home page, the product pages, the FAQ or the size guide links to them (N-10). |
| C-02 | OPEN | The seven category pages still have only a list and filter text. Main text: `/shop/sweaters` 161 words, `/shop/cardigans` 78, `/shop/vests` 64, `/shop/gift` 55, `/shop/beanies--hats` 53, `/shop/sets` 54, `/shop/winter-wool-gifts` 74. Intro copy exists only on the new landing pages, which are separate URLs (N-01). |
| C-03 | PARTLY FIXED | Each twin gets one colour sentence. Beige: "This beige version of the pure wool stand-collar sweater..." and Blue: "This blue version..." (`H/...679503.html`, `H/...679510.html`). Brown and Green lambswool differ the same way. Everything else is identical. Containment after: stand-collar 0.97, side-slit Camel vs Light Grey 0.99, lambswool Brown vs Green 0.99, Women's Classic vs Green 0.96, shawl cardigans 0.93. Before, same method: 1.00, 1.00, 1.00, 0.96, 0.93. |
| C-04 | PARTLY FIXED | Fixed: home title is "Autumn & Wool \| Wool sweaters and cardigans from Riga" (was "Handmade wool knitwear from Riga"). About now says "Knitted on a manual knitting machine" (was "Knitted by hand or on a manually operated machine"). Still open: privacy "Autumn & Wool is a handmade knitwear brand ... creating sustainable garments from 100% natural yarns"; about "100% made in Latvia" and "Every garment is made in Latvia from merino, lambswool or pure new wool"; shipping "Each piece is machine-knitted and hand-finished". Product wording also differs by product (N-09). |
| C-05 | PARTLY FIXED | Etsy is now linked: home and about read "4.9 ... from 1,400+ reviews on Etsy" and "8,000+ orders on Etsy" with links to `etsy.com/shop/mareshop` (5 Etsy links). The figures are unverified. No review text appears on any product page. |
| C-06 | OPEN | About main text is 179 words (was 180). The only changes are the Etsy links and the process sentence. "Kristine designs every piece, inspired by a family tradition of knitting." is still the only maker sentence. No bio, years of practice, or maker photo appears in the text. |
| C-07 | OPEN | Unique description words, same method: median 174.5 (before) to 184.5 (after); under 300 words: 21 of 22 before and after. Shortest: gift card 34, beige V-neck vest 83. |
| C-08 | OPEN | "In-stock items ship from Riga within 2–5 working days. 14-day returns." is in 20 of 22 product descriptions (unchanged). "Knitted on a manually operated knitting machine and hand-sewn in Latvia" is in 16 of 22. |
| C-09 | OPEN | Not re-scored. The sentence splitter cannot separate headings from body copy on these pages, so there is no reliable figure. Home and shipping body wording is unchanged apart from title and meta edits. |
| C-10 | OPEN | "Last updated: 1 November 2026" appears only on `H/imprint.html` and `H/cookie-policy.html`. The nine new pages have no date, although they quote prices and shipping terms. |
| C-11 | NOT FIXABLE ON PLATFORM | No page has FAQPage JSON-LD. JSON-LD types across the site are LocalBusiness, Organization, WebSite, Product, Offer and AggregateOffer. This is the plan limit the first audit recorded. |

### On-Page SEO

| ID | Status | Fresh evidence |
|---|---|---|
| O-01 (critical) | OPEN | `H/shop-cardigans.html` still has `<link rel="canonical" href="https://www.autumnandwool.com/shop"/>`. The same holds for all seven category pages, and the sitemap still lists them. Whether Squarespace lets you change this was not checked. |
| O-02 | OPEN | All seven category pages still have no meta description. |
| O-03 | OPEN | No H1 on `/shop`, the seven category pages, or `/cookie-policy` (nine pages). Category pages have only an H2 ("Cardigans"). |
| O-04 | FIXED | Every product page now has two or three related-product links ("Also see: Pure Wool Side-Slit Sweater - Camel") and a category landing link ("More sweaters: wool sweaters"). Link counts checked on all 22 product pages; the "Also see" pattern was read in full on the stand-collar Beige page. |
| O-05 | OPEN | The seven category titles are unchanged and still 66 to 79 characters, for example "Winter Wool Gifts — Shop wool sweaters, cardigans & accessories \| Autumn & Wool" (79). |
| O-06 | FIXED | No product title is over 60 characters now (longest 53). Note: the brand suffix was dropped from product titles (N-08). |
| O-07 | OPEN | `/` and `/home` still share the title "Autumn & Wool \| Wool sweaters and cardigans from Riga" and the same meta. `/home` canonicals to the root, and `/home` is still in the sitemap. |
| O-08 | OPEN | 7 of 22 live product URLs still contain "sustainable", "organic" or "handmade" (for example `...merino-wool-turtleneck-...-sustainable-knitwear-sizes-sl-12-679428`). The new pages use clean slugs. No product slug was changed. |
| O-09 | PARTLY FIXED | Titles and metas are unique by colour. Bodies differ by one colour sentence only (see C-03). |
| O-10 | OPEN (worse) | "Knitted and hand-sewn in Latvia." is in 15 metas (unchanged). "Free shipping, 14-day returns." is in 11 metas (was 8). `metadata_template.py` reports site_risk low and templated_ratio 0.0 over 42 metas, but it checks only closing CTAs, so it does not catch mid-meta repeats. |
| O-11 | FIXED | `H/privacy-policy.html` meta: "How Autumn & Wool collects, uses and protects your personal data when you shop with us or get in touch." (103). About title "About our Riga knitwear studio \| Autumn & Wool" (46). Contact title "Contact our Riga studio \| Autumn & Wool" (39). FAQ title "Wool Knitwear FAQs: Sizing, Care and Returns" (44, no brand suffix). |
| O-12 | FIXED | No meta starts with "Explore". Gift card H1 is now "Digital Gift Card for Wool Knitwear" (was "Gift Card"). |
| O-13 | OPEN | `H/about.html`: H2 then H4 (footer). `H/imprint.html`: H1 then H3. `/shop` and all category pages: H2 then H4 (filters). |
| O-14 | OPEN | Four links per page have no text and no aria-label (header and footer). This is my count. The first audit's 11 used a different method, so the two are not comparable. |
| O-15 | FIXED | 0 of 1,474 `<img>` tags in the raw HTML lack an alt attribute (first audit: 8 of 1,409). Alt text quality was not reviewed. |
| O-16 | OPEN | `H/faq.html` and `H/size-guide.html`: 0 product links and 0 category links in the main content. `H/about.html`: 1 category link. |
| O-17 | OPEN | `lang="en-US"` on all 49 content pages. |
| O-18 | FIXED | `/shop/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper` now returns 301 (was 404). The target is `http://` (N-14). The `/this-page-does-not-exist-404-test` URL returns 404 as it should. |

## New findings

Severity: High, Medium, Low.

- **N-01 (High). Two URL sets now compete for the same queries.** Landing pages: `/wool-sweaters`, `/wool-cardigans`, `/wool-sweater-vests`, `/wool-hats-and-scarves`, `/wool-gifts`. Category pages: `/shop/sweaters`, `/shop/cardigans`, `/shop/vests`, `/shop/beanies--hats` and `/shop/sets`, `/shop/winter-wool-gifts` and `/shop/gift`. All of these are in the sitemap. The category set is canonicalised to `/shop`. Owner decision: keep one set per category, and either remove the other from the sitemap or fix the canonical. Not decided here.
- **N-02 (Medium). Claim goes beyond product copy.** `H/wool-hats-and-scarves.html`: "Each piece is designed by Kristine in Riga, Latvia, and knitted on a manual knitting machine and finished by hand." The beanie and hat-set copy have no "manual" and no "hand-finished". Their only care wording is "use a machine wool cycle".
- **N-03 (Medium). Shipping line wrong for digital gift cards.** `H/wool-gifts.html`, Delivery: "Every order is packed by hand in our Riga studio and sent with tracking." The same page says "Gift cards are sent by email".
- **N-04 (Medium-Low). Title promises content the body lacks.** `H/wool-gifts.html` title "Wool Gifts for Her: A Christmas Guide". "Christmas" does not appear in the page body. The H1 is "Wool gifts for her". The title is also the link text in the "More from" block on eight other new pages.
- **N-05 (Medium). Prices will go stale.** `H/wool-gifts.html` hard-codes €25, €45, €110, €136 and €145. The hat-set product FAQ says: "Is this a matching merino hat and scarf gift under €120? Yes. At the current price of €110". The H2 "Sweaters and cardigans, €110 to €145" reads as a range, but the catalogue has €155 (Oversized Wool Raglan, Open-Front cardigan), €160 (Merino Raglan Cardigan) and €165 (Merino Striped Oversized). The four pieces listed are correct.
- **N-06 (Medium). "Free shipping" without the qualifier.** Product pages: "Free shipping. In-stock items ship from Riga..." (20 of 22). Metas: "Size guide and free shipping." (wool-sweaters, wool-cardigans, wool-sweater-vests), "Free shipping." (hats). Shipping page: "Free Latvia, the US & destinations shown at checkout". Category pages: "Free shipping to eligible destinations".
- **N-07 (Medium). Shared boilerplate on the nine new pages.** "Shipping is free to Latvia, the US and the destinations shown at checkout" on 5 pages. "Unworn, unused items can be returned within 14 days of delivery" on 5. "Shop the full collection" on 9. The same 8-link "More from Autumn & Wool" block on each page. Body text is not duplicated between the new pages (maximum 5-gram containment 0.23, wool-sweaters vs wool-hats-and-scarves). This is templating, not duplication.
- **N-08 (Medium). Brand name is inconsistent.** Product title tags have no brand suffix (raw `<title>`: "Pure Wool Stand-Collar Sweater, Beige"), while every other title has "| Autumn & Wool". Metas spell the name three ways: `size-guide` "Find accurate size measurements for Autumn wool garments", `faq` "...about autumn and wool products", `contact` "Contact Autumn and Wool...". The metadata script also flags a brand suffix concatenated into the description on /about, /cookie-policy, /imprint, /privacy-policy, /shipping-returns and /shop.
- **N-09 (Low-Medium). Production wording varies by product.** Most product copy: "Knitted on a manually operated knitting machine and hand-sewn in Latvia." The black merino cardigan: "machine-knitted and hand-finished in Riga." The turtleneck and others use "Knitted and hand-sewn in Latvia." Harmonise once the owner confirms the process.
- **N-10 (Medium). Guide cluster is orphaned.** `how-to-wash-a-wool-sweater`, `merino-vs-lambswool`, `oversized-fit-guide` and `how-to-choose-a-wool-cardigan` are linked only from the other new pages (8 source pages each). Home, product pages, FAQ and size guide do not link to them. The product care lines do not point to the wash guide.
- **N-11 (Medium-Low). Thin landing pages.** Body text excluding the "More from" block: `wool-sweater-vests` 168 words, `wool-hats-and-scarves` 180, `wool-sweaters` 249, `wool-cardigans` 187, `wool-gifts` 345. The first audit's 300-word floor applies to the vests and hats pages.
- **N-12 (Low). Two near-identical dusty-pink merino raglans with confusing names.** "Merino Wool Raglan Sweater - Dusty Pink" and "Oversized Merino Turtleneck, Dusty Pink" (H1 "Oversized Merino Turtleneck — Dusty Pink Raglan"), 5-gram containment 0.76. The turtleneck's H1 calls it a raglan.
- **N-13 (Low). Size-guide one-size wording.** `H/size-guide.html`: Oversized "Most come in one size". The Oversized Merino Raglan (Dusty Pink) lists S/M and L/XL. Owner to confirm the size facts.
- **N-14 (Low). Redirect chain.** The old product URL 301s to `http://www.autumnandwool.com/shop/p/p/...`, then to https.
- **N-15 (Low, verify in a browser).** Static HTML on the category pages I checked (cardigans, winter gifts) contains "No results found. No results match your search." This may be a hidden JavaScript filter state. Not checked in a browser.
- **N-16 (Low, verify).** `/shop/gift` has no internal HTML link in the crawl. Navigation may be JavaScript-rendered.
- **N-17 (Low).** Hat landing page: H1 "Merino wool hats and scarves" against title "Merino Wool Beanies and Hat Sets".

Verified as accurate (no action): gift card prices €25 to €250; beanie €45; set €110; turtleneck €110 (12 colours, 12 listed); beanie 11 colours (11 listed); side-slit S width 50 cm; size-guide chart S chest 84 to 90 and M 90 to 96 (in the table markup); fit notes ("Relaxed", "Oversized; roomy and easy to layer", "Comfortable, close to the body"); fibre statements; gift cards not returnable (shipping page); cedar/lavender storage and "do not tumble dry" match between FAQ and wash guide.

## Not checked

- No live fetch and no browser render. JavaScript filters, navigation and template-generated H1s were not seen as rendered.
- Squarespace settings (category canonical, SEO fields, H1 template, sitemap control, site language) were not checked.
- No Search Console, analytics or rank data.
- Etsy review and order figures were not verified.
- Alt text quality was not reviewed. Images were checked only for the presence of an alt attribute.
- C-09 readability was not re-scored reliably.
- Before-state similarity figures were computed by me with the same method. The first audit's own 0.92 figure used a different measure.
- The crawl has 49 content pages with status 200 and a real title. The first audit listed 39 indexable pages plus 9 new, which is 48. I did not reconcile the one-page difference.
