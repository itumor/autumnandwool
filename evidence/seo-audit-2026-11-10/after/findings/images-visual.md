# Images and visual re-audit (after): www.autumnandwool.com (2026-11-10, fresh crawl)

Scope: 59 crawled files in `after/crawl/html/` (all `<img>` tags, alt, lazy, fetchpriority, og:image, twitter:card, sitemap titles). Image requests: 11 HEAD requests plus one redirect follow (12 max, cap 15, 1 per second). Browser: headless Chromium (Chrome 157), fresh profile, 1440x900 and 390x844, DOM measurements from `scratchpad/measure.js`, 10 screenshots. Raw measurements: `findings/images-visual-measure.json`.

Platform: Squarespace 7.1. Layer codes: (a) Squarespace settings, (c) Custom CSS, (d) content or layout edit in the editor, (h) re-upload a file, (f) not fixable on this plan.

Site changes since the first audit (from `live-changes/`, read for context only, not used as evidence of fixes): batch 4 rewrote product titles, SEO and image alts on 22 products; batch 2 built the 9 new pages as Code blocks from `business-os/seo-marketplace/live-2026-11-10/html/`. Batch 5 changed the cookie bar and LLMs text. The status below comes from the fresh HTML and browser, not from those logs.

## Scores

- **Images: 66 / 100 (first audit 62).** Up 4, from the alt-text fixes (I-01, I-02, I-03). Partly offset by a new broken-image defect on the new landing pages (N-01, High). Method and per-item weights in the Scoring section.
- **Visual / mobile verdict: usable and on-brand on home and /shop at both sizes, but the one blocker is unchanged.** On a 390px first visit, the cookie bar still covers the product price and Add To Cart (V-01 OPEN). The new /wool-sweaters landing page shows broken image tiles on desktop and mobile (N-01). /wool-gifts has no images at all (N-03).

## Status summary

| Group | FIXED | PARTLY FIXED | OPEN | NOT FIXABLE ON PLATFORM |
|---|---|---|---|---|
| Images I-01..I-11 | 3 | 3 | 4 | 1 |
| Visual V-01..V-06 | 0 | 0 | 6 | 0 |
| **Total (17)** | **3** | **3** | **10** | **1** |

New findings: N-01 (High), N-02 (Medium), N-03 (Low).

## Status of first-audit findings

| ID | First-audit sev | Status now | Fresh evidence |
|---|---|---|---|
| I-01 | High | **FIXED** | Filename alts as the effective (first) alt: 0 across 59 files. Product pages: 854 tags, all descriptive (e.g. "Oversized merino vest in grey, front view over a black top"). /shop and category grids: first alt descriptive on 435 tags. Residual: 9 tags have `alt=""` first and a filename in a second, ignored alt attribute (`IMG_3057.JPEG` on 8 pages, `IMG_0976.JPEG` on /about). Same markup defect as I-10. |
| I-02 | Medium | **FIXED** | Alts over 125 chars: 0 (was 84 tags). Pipe-separated alts: 0. Cardigan pages now carry short descriptive alts. |
| I-03 | Low | **FIXED** | Home Instagram tiles now have distinct alts: "Autumn &amp; Wool knitwear, Instagram photo 1" to "photo 5" (5 different files). Duplicate alt across different image files on any page: 0. |
| I-04 | Medium | **PARTLY FIXED** | Product pages (22 files) now carry their own og:image (`image_1.jpg?format=1500` and similar). 27 files still carry the site-wide portrait PNG `a2ce269e-...png` (home x2, /shop, 7 category, 9 new landing pages, about, contact, etc.). twitter:card is `summary` on all files that have one; no `summary_large_image`. |
| I-05 | Medium | **OPEN** | /shop: 203 `<img>` tags (unchanged). 199 `loading="lazy"`. HTML size now 888,441 B (pages.tsv). The first-audit figure (954,626 B) has no recorded basis, so the two are not comparable. |
| I-06 | Medium | **PARTLY FIXED** | Home hero (`WhatsApp...(2)(1).webp?format=1000w`) now has `fetchpriority="high"` and no `loading` attribute (correct for LCP). Still wrong: the 4 header-logo tags on every page keep `fetchpriority="high"` and `loading="eager"` (88 tags on 22 product pages, 28 on categories). Logo is 22,650 B WebP, so the impact is small. Full fix needs a theme change (f). |
| I-07 | Medium | **OPEN** | Camera and generic names remain: logo `ChatGPT+Image+Nov+25...PM.png`; hero `WhatsApp+Image...`; product og and grid files `image_1.jpg`, `IMG_3336.JPEG`, `IMG_3334.JPEG`. New pages use `image_1.jpg` / `image_2.jpg` and `IMG_3334.JPEG`. Not renamed in place (h). |
| I-08 | Low | **OPEN** | No width/height on 40 of 40 home tags, 854 of 854 product tags, 36 of 57 new-page tags. Grid tags on /shop and categories carry them (244 of 272 category, 199 of 203 /shop). CLS not measured in this run; the PageSpeed lab values in `after/../pagespeed.md` are CLS 0 (home), 0.001 (product desktop), 0.011 (product mobile). That lowers the risk, but markup still lacks the dimensions. |
| I-09 | Low | **OPEN** | Originals still large. `IMG_3336.JPEG` (no format param) now returns `image/webp` 364,916 B; the first audit recorded JPEG 456,916 B for the same URL, so the served file changed, but no re-upload is logged, so the cause is not known. Grid original `image_1.jpg` (no format param) is 1,039,468 B. Product photos are still uploaded at full size (h). |
| I-10 | Low | **NOT FIXABLE ON PLATFORM** | Duplicate `alt` attributes on the Squarespace grid: 444 `<img>` tags carry two alt attributes (first descriptive or empty, last `alt=""`). Browsers use the first, so the effective alt is fine. Parsers that keep the last see an empty alt, and 9 tags show a filename there. Template markup (f). |
| I-11 | Low | **PARTLY FIXED** | Sitemap has 192 `image:image` entries. 174 now have descriptive titles; 18 still end in "- additional view 1..3" (e.g. "Oversized Merino Turtleneck - Dusty Pink Raglan - additional view 1"). |
| V-01 | High | **OPEN** | Cookie bar is still fixed at the bottom. On 390px it is now 145 px tall, top y=699 (was 178 px, y=666). On the product page, price (y=710) and Add To Cart (y=757 to 805) are still inside the bar (y=699 to 844). Screenshot `audit-product-vest-mobile-390.png` shows the H1 and gallery, with no price or button visible. The bar is 33 px shorter, which does not clear the controls. Home mobile is also covered: bar y=699 to 844 over the hero's lower half. |
| V-02 | Medium | **OPEN** | /shop and /shop/sweaters: h1_count 0 in the crawl. /shop mobile shows "The collection" as large text, not an H1. Desktop /shop shows only the category tabs, no visible title. New landing pages all have an H1 (9 of 9), which is an improvement. |
| V-03 | Medium | **OPEN** | Product mobile: H1 y=619, price y=710, Add To Cart y=757. Gallery fills y=115 to 495 on the scaled screenshot (about 60% of the first screen). Same as the first audit. |
| V-04 | Low | **OPEN** | Small tap targets in the first viewport: 9 (home mobile), 9 (/shop mobile), 9 (product mobile), 10 (wool-sweaters mobile), 17 (wool-sweaters desktop), 18 (product desktop), 23 (/shop desktop). Footer link sizes not re-measured separately. |
| V-05 | Low | **OPEN** | Smallest text: 9.5 px (desktop) and 11 px (mobile). 5 to 7 text nodes per view are under 12 px. Same as the first audit. |
| V-06 | Low | **OPEN** | Home mobile (`audit-home-mobile-390.png`) still has no rating line in the first screen; the "4.9 from 1,400+ reviews on Etsy" badge is desktop only (`audit-home-desktop-1440.png`). |

Checked and fine: H1 and primary CTA visible above the fold on home at both sizes (H1 y=251 desktop, y=219 mobile). Product H1, price and Add To Cart above the fold on desktop (H1 y=180, price y=303, Add To Cart y=351 to 406). Horizontal overflow: none (scrollWidth equals viewport width at 1440 and 390 on all 10 views). No broken images on home, /shop, /wool-gifts or the product page.

## New findings

| ID | Sev | Finding | Evidence | Fix | Layer | Effort |
|---|---|---|---|---|---|---|
| N-01 | High | **Broken images on the new landing pages.** 21 `<img>` tags have a malformed `src` with two query strings, `...image_1.jpg?format=1500w?format=500w` (or `IMG_3334.JPEG?format=1500w?format=500w`). These tags carry no `srcset`, so the browser requests the malformed URL. /wool-sweaters: 13 tags. /wool-cardigans: 4. /wool-sweater-vests: 2. /wool-hats-and-scarves: 2. HEAD on the /wool-sweaters, /wool-cardigans and /wool-sweater-vests variants returned **404**. Browser: 12 broken images at 1440 and 4 at 390 on /wool-sweaters (script count, `img_broken_count`). Screenshot `audit-wool-sweaters-desktop-1440.png` shows grey empty tiles with broken-image icons and alt text ("Oversized Wool Raglan Sweater, Beige", "Distressed Oversized Wool Raglan Sweater"). The /wool-hats-and-scarves variant was not requested. Cause: the same string is in the source HTML at `business-os/seo-marketplace/live-2026-11-10/html/` (4 files), which was pasted into Code blocks (live-changes batch 2). | Fix the source HTML so each `src` has one `?format=` (e.g. `...image_1.jpg?format=1500w`), or re-insert the images with Squarespace's image block. Then re-paste the 4 Code blocks and re-run the broken-image check. Do not hide the tiles with CSS. | (d) | S |
| N-02 | Medium | **Logo alt text is double-escaped on every page.** The header logo tags (4 per page) have `alt="Autumn &amp;amp; Wool"`, which is read as the literal text "Autumn &amp; Wool" by screen readers. Found on 52 of 59 crawled files, 208 tags. Also on the new landing pages. | `grep 'Autumn &amp;amp; Wool'` across the crawl; the other alts with "&" (e.g. "Model wearing an oversized Autumn &amp; Wool knit sweater") are correct. | Set the site logo's image alt text to plain "Autumn and Wool" (or "Autumn & Wool") in the Site Header logo settings; check that the value is not re-escaped on save. | (a) | S |
| N-03 | Low | **/wool-gifts has no product or content images.** The page has 4 `<img>` tags, all header logos. Screenshots `audit-wool-gifts-desktop-1440.png` and `audit-wool-gifts-mobile-390.png` show text only, with links to products that have images. | crawl img=4; browser img_visible=0 for content images. | Add the gift product images (or a hero image) as image blocks with descriptive alts. Keep the existing text. | (d) | S |

## Screenshots (new, in `after/screenshots/`)

Requested set (1440 and 390 each):
- `audit-home-desktop-1440.png`, `audit-home-mobile-390.png`
- `audit-shop-desktop-1440.png`, `audit-shop-mobile-390.png`
- `audit-wool-sweaters-desktop-1440.png`, `audit-wool-sweaters-mobile-390.png` (new page; broken tiles visible)
- `audit-wool-gifts-desktop-1440.png`, `audit-wool-gifts-mobile-390.png` (text only)
- `audit-product-vest-desktop-1440.png`, `audit-product-vest-mobile-390.png`

Other files in `after/screenshots/` (e.g. `wool-sweaters-desktop.png`, `wool-cardigans-mobile.png`, `how-to-wash-a-wool-sweater-desktop.png`) were not created by this run and were not reviewed.

## Scoring

The first audit's 62 has no per-item weights in its file. For a transparent comparison I used the weights that reproduce 62 exactly: High I-01 = 12; Medium I-02, I-04, I-05, I-06, I-07 = 4 each; Low I-03, I-08, I-09, I-11 = 1 each; I-10 = 2. PARTLY FIXED deducts half of the weight, rounded up (so Low PARTLY = 1). New findings use the same scale (N-01 High = 12, N-02 Medium = 4, N-03 Low = 1).

Current deductions: I-04 2, I-05 4, I-06 2, I-07 4, I-08 1, I-09 1, I-10 2, I-11 1, N-01 12, N-02 4, N-03 1. Total 34. **Score: 66 / 100.**

What changed from 62:
- +12 I-01 fixed (filename alts gone from effective alts).
- +4 I-02 fixed (no alts over 125 chars or with pipes).
- +1 I-03 fixed (distinct Instagram alts).
- +2 I-04 partly (product og images fixed; 27 pages still share one portrait PNG).
- +2 I-06 partly (hero now has fetchpriority high; logos still high).
- No change for I-05, I-07, I-08, I-09, I-10 (still open or not fixable), and I-11 stays at 1 (PARTLY, Low).
- -12 N-01 (broken images on new pages), -4 N-02 (double-escaped logo alt), -1 N-03 (no images on /wool-gifts).

Net: +21 from fixes and partial fixes, minus 17 from new defects, so +4. The new broken-image defect is High and is the first thing to fix; without it the score would be 78.

## Limits and not checked

- Headless Chromium on macOS, not a real iPhone or Android device; DPR 1. Fresh profile, so the cookie bar is shown.
- LCP not captured (`lcp` empty in this run). CLS not measured here; PageSpeed lab values are in `after/../pagespeed.md`.
- Only /wool-sweaters, /wool-cardigans and /wool-sweater-vests malformed URLs were HEAD-checked (3 of the 4 page patterns, 404 each). /wool-hats-and-scarves was not checked separately; browser evidence is for /wool-sweaters only. Other 3 pages were not screenshotted or measured in the browser.
- Image file formats: the CDN now returns WebP for some URLs that the first audit recorded as JPEG. I did not establish whether this is content negotiation or a re-upload.
- Product pages: 0 tags with `loading="lazy"`. Squarespace appears to lazy-load with its own attributes (`data-load`); not verified in the browser beyond 2 visible images at 390.
- The malformed tiles on /wool-cardigans, /wool-sweater-vests and /wool-hats-and-scarves were not seen in screenshots; their defect is from HTML and HEAD only.
- Image-request budget: 11 HEAD plus one redirect follow (12 of 15).
- Screenshot review: images were downscaled copies (JPEG, max 700 px) in the scratchpad to read them; the originals in `after/screenshots/` are full size. No other files were changed.

## Evidence index

- Crawl HTML: `after/crawl/html/` (file names as crawled). Pages: 59 files, incl. 22 product, 7 category, 9 new landing, 1 /shop grid, 2 home (http/https duplicates).
- Measurements: `findings/images-visual-measure.json` (per view: cookie bar rect, H1 and price/CTA y, tap-target counts, broken-image count, font sizes).
- HEAD results (11 requests): home hero WebP 184,908 B; logo WebP 22,650 B; /shop-grid `image_1.jpg` 1,039,468 B; IG `IMG_2369.JPEG` 166,986 B; product original `IMG_3336.JPEG` 364,916 B (WebP); site og PNG 301 redirect; malformed URLs 404 (wool-sweaters, wool-cardigans, wool-sweater-vests); valid `?format=500w` variant 301 to CDN.
- Screenshots: `after/screenshots/audit-*.png` (10 files, listed above).
