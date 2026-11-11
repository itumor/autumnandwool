# Images and visual audit: www.autumnandwool.com (2026-11-10)

Scope: 50 crawled HTML files in `crawl/html/` (image tags, alt, lazy loading, srcset, og:image, sitemap); 10 HEAD and 5 byte-range requests to image URLs (15 total, 1 per second); 8 viewport screenshots (1440x900 desktop, 390x844 mobile) of home, /shop, /shop/sweaters and /shop/p/oversized-merino-wool-v-neck-sweater-vest, with DOM measurements on each.

Platform: Squarespace 7.1, no code injection, no scripts. Layer codes: (a) Squarespace image/page/product settings, (c) Custom CSS, (d) content or layout edit in the editor, (h) re-upload a better file (owner task), (f) not fixable on this plan.

## Scores

- **Images: 62 / 100.** Delivery is mostly sound (lazy loading, srcset, WebP hero, no broken images). Deductions come from filename alt text on product images, over-long keyword alt text, one site-wide portrait social image, and a poorly targeted fetch priority.
- **Visual / mobile verdict: usable and on-brand, with one blocker.** No horizontal overflow and no broken images in any of the 8 views. H1 and the primary CTA are above the fold on home at both sizes. On a 390px first visit, the cookie bar covers the product price and Add To Cart (see V-01).

## What works

- Descriptive alt on the product gallery and home images, e.g. `alt="Grey oversized V-neck merino wool vest layered over a black top on a mannequin"` (product vest page) and `alt="Model wearing an oversized Autumn & Wool knit sweater"` (home).
- Below-fold images are lazy: home 15 of 20 tags, /shop 199 of 203. The hero (`WhatsApp%2BImage...webp?format=1500w`, `loading` unset) is not lazy, which is correct.
- Responsive delivery: grid and gallery tags carry `srcset` with `?format=100w` through `?format=2500w` (7 candidates on /shop).
- Hero is WebP: `image/webp`, 217,950 B. Logo is WebP: 22,650 B. Home slide variant: WebP, 88,942 B.
- Rendered sizes match the slot on desktop: shop grid tile 432 CSS px at natural 432 px; product gallery 744 CSS px at natural 750 px. Mobile grid tile 166 CSS px at natural 343 px (about 2x).
- No broken images: 0 across 8 views.
- No horizontal overflow: `scrollWidth` equals viewport width in all 8 views.
- Sitemap carries image entries: 192 `image:image` entries across 39 URLs.
- Cookie bar has "Decline all" at the same visual weight as "Accept all".
- Trust signals on desktop: home hero "4.9 from 1,400+ customers"; product block "4.9 from 1,400+ reviews on Etsy (as Mareshop)", free shipping, dispatch time, 14-day returns.

## Notes on the crawl's alt numbers (not defects)

- `pages.tsv` reports 4 missing alts on home. These are `alt=""` (empty), not missing. Three of the four share a file URL with labelled slides (`image_1.jpg` matches the "Oversized Wool Raglan Sweater" slide; `IMG_3336.JPEG` matches the vest slide). They are duplicate decorative clones. Low priority.
- On /shop and the category pages, every grid `<img>` carries two `alt` attributes: the descriptive one first, then `alt=""`. Browsers use the first, so the effective alt is correct. A parser that keeps the last attribute (the crawler does) will read the alt as empty. See I-10.

## Images findings

| ID | Sev | Finding | Evidence | Fix | Layer | Effort |
|---|---|---|---|---|---|---|
| I-01 | High | Filename used as alt text on product and grid images: 115 tags across the crawl. Three product pages are affected, and the category grids carry the same names. | `crawl/html/www-autumnandwool-com-shop-p-p-wool-sweater-vest-knitted-wool-vest-...html`: `alt="image_1.jpg"` through `image_10.jpg`, each 4 times (40 tags). `...-shop-p-p-wool-sweater-sweater-for-women-...html`: `alt="image_1.jpg"` (36 tags across 9 files). `...-shop-p-autumn-and-wool-digital-gift-card.html`: `alt="ChatGPT Image Nov 9, 2025, 12_26_29 PM.png"` x4. `www-autumnandwool-com-shop.html`: `image_1.jpg` through `image_10.jpg` (2 each). | Replace each filename alt with a product description: the product image's Alt text field in the product editor, or the image block's alt field on the category page. Reference the existing good alts (vest page) for wording. | (a) | M |
| I-02 | Medium | Over-long, pipe-separated keyword alt on the black merino cardigan family: 84 tags across the crawl exceed 125 characters. | `www-autumnandwool-com-shop-cardigans.html`: `alt="Black Merino Wool Cardigan \| 100% Merino Wool Raglan Sweater \| Minimalist Knitwear \| Sustainable Handmade Women's Cardigan - close-up detail view"` (163 chars), and the same string with "additional view 1" through "additional view 8" (one tag each). Same pattern on the black cardigan product page. | Shorten each to one descriptive phrase per view, e.g. "Black merino wool raglan cardigan, close-up of knit detail". | (a) | S |
| I-03 | Low | Five different Instagram photos on home carry the same alt. | `www-autumnandwool-com-home.html`: `alt="Autumn &amp; Wool on Instagram"` on 5 tags (`IMG_2369`, `IMG_3022`, `IMG_2929`, `IMG_2166`, `IMG_2373`). | Describe each photo (e.g. "Knitted sweater in a Riga studio, hand-finishing detail") or make purely decorative tiles `alt=""` in the block settings. | (a) | S |
| I-04 | Medium | og:image is one site-wide portrait PNG on every non-product page; twitter card is `summary` (small thumbnail). | `www-autumnandwool-com-home.html`: `og:image` = `static1.squarespace.com/.../a2ce269e-e44f-494d-81c1-2821f25a6e26.png?format=1500w`, `og:image:width` 1024, `og:image:height` 1536, `twitter:card` = `summary`. The same og:image appears on /shop, /about and /size-guide. Product pages use their own image (`IMG_3334.JPEG`, 1500x2000). | Set a per-page Social image (Page settings > SEO, or Social sharing) at 1200x630 for the main pages. Consider `summary_large_image`, which Squarespace may not allow (then (f)). | (a) | S per page |
| I-05 | Medium | /shop has 203 `<img>` tags: 22 product cards each render cover, hover and all gallery images. Page bytes 954,626 vs 675,940 on the homepage. | `www-autumnandwool-com-shop.html`: `grid-item-additional-image` x156, `grid-image-cover` x22, `grid-image-hover` x20; 199 of 203 are `loading="lazy"`. Only in-view tiles download on first load; the grid original is 456,916 B (range check) and is not fetched unless its tile comes into view. Page weight is therefore mainly HTML/DOM, not image bytes. Not measured: total images fetched on scroll. | Reduce gallery images per product that show in the grid, or the number of additional images shown in the category view. Check the product block's image settings first. | (a)/(d) | M |
| I-06 | Medium | Fetch priority is aimed at the wrong images. Four logo copies per page carry `fetchpriority="high"` and `loading="eager"`; the hero has no `fetchpriority`. | `www-autumnandwool-com-home.html`: first four `<img>` (logo, alt "Autumn & Wool") have `fetchpriority="high"`; hero `<img>` (`WhatsApp%2BImage%2B2025-11-07...webp?format=1500w`) has no `fetchpriority`. Same logo pattern on every page. Impact is small: logo is 22 KB. LCP was not captured in the headless run (LCP entries empty), so the hero's LCP role is unconfirmed. | Cannot set attributes in the Squarespace editor and Custom CSS cannot set priority. Note for the owner and re-check after any theme change. | (f) | - |
| I-07 | Medium | Camera, ChatGPT and generic file names in the CDN URLs (search engines and file managers see them). Examples: logo and og base file `ChatGPT Image Nov 25, 2025, 12_10_55 PM.png`, camera files `IMG_3336.JPEG`, `IMG_2369.JPEG`, generic `image_1.jpg`. | `www-autumnandwool-com-home.html`: logo `src` ends `ChatGPT+Image+Nov+25%2C+2025%2C+12_10_55+PM.png`; hero `WhatsApp%2BImage%2B2025-11-07%2Bat%2B08.48.42...`. Product grid: `IMG_3336.JPEG`. File names are only a weak ranking signal; alt and page context matter more. | Re-upload the logo and the key product photos under descriptive file names (e.g. `autumn-and-wool-logo.png`, `oversized-merino-wool-vest-grey-front.jpg`) before they are attached in the editor. Renaming an existing image in place does not change the CDN path. | (h) | M |
| I-08 | Low | `width` and `height` absent on most content images, so CLS is possible if the wrapper does not reserve space. CLS was not measured. | Home: 20 of 20 `<img>` without width/height. Product vest page: 44 of 44. Product black cardigan: 60 of 60. `/shop` grid: width/height present on 199 of 203. | Verify with a real CLS run (PageSpeed) on the home and product pages. If it is a real shift, check the image block's aspect-ratio setting (a). | (a) verify / (f) | S |
| I-09 | Low | Product gallery original is a large JPEG (IMG_3336.JPEG, 456,916 B at 1536x2048). Variants exist and srcset-capable browsers pick them; the fallback `src` is the original. Product photos are JPEG at the source, and no AVIF is served. | HEAD/range checks: `IMG_3336.JPEG` (no format) 456,916 B; `?format=2500w` 456,916 B (same file, returned unchanged); `?format=100w` 4,171 B JPEG. Note: CDN content-type varied with the request (home variants WebP, grid variants JPEG) under a plain curl request; browser negotiation not verified. | Upload smaller source files (about 2000 px long edge, quality 80) for future product photos. | (h) | M |
| I-10 | Low | Duplicate `alt` attributes in the Squarespace grid markup (`alt="<descriptive>" ... alt=""`). The browser uses the first (correct); parsers that keep the last see an empty alt. | `www-autumnandwool-com-shop.html`: 200 duplicate attributes; first `alt` is `Grey oversized V-neck merino wool vest layered over a black top on a mannequin`, second `alt=""`. | Template markup; not fixable on this plan. Note so the crawler's "missing alt" count is not treated as a real defect. | (f) | - |
| I-11 | Low | Sitemap image entries use generic titles for many views. | `www-autumnandwool-com-sitemap-xml.html`: 192 `image:image` entries across 39 `<url>`, titles such as "... - additional view 1" and "... - additional view 2". | Retitle the views once the product photos are renamed (I-07). | (h)/(d) | S |

## Visual findings

| ID | Sev | Finding | Evidence | Fix | Layer | Effort |
|---|---|---|---|---|---|---|
| V-01 | High | On a 390px first visit, the cookie bar covers the product price and Add To Cart. The bar is fixed at the bottom and is 178 px tall on mobile. | `measure.json` product-vest-mobile-390: bar rect y=666 to 844 (`gdpr-cookie-banner BOTTOM bar`, z 300000); price y=710; Add To Cart y=757 to 805, `in_fold` true only because it is inside 844. Screenshot `product-vest-mobile-390.png` shows the H1 cut by the bar and no price or button visible. Once the visitor chooses, the bar goes and the controls are visible. | Keep the consent bar (required). Shorten its copy and reduce its padding with Custom CSS so it is compact on small screens (c). Check Squarespace's cookie banner settings for a compact/position option (a). Do not hide the bar or set it to `display:none`. | (c) / (a) | S |
| V-02 | Medium | Category pages have no H1, and on desktop no category title is visible above the fold. | Crawl: `/shop` h1_count 0, `/shop/sweaters` h1_count 0. Screenshot `shop-sweaters-desktop-1440.png`: only the breadcrumb "All /" is visible, no title. Mobile `shop-sweaters-mobile-390.png` shows "Sweaters" in large type but it is not an H1. | Set the collection title in the collection page's settings so it renders as the page heading (d). If the theme does not expose a heading level, it is (f). | (d) / (f) | S |
| V-03 | Medium | On mobile the product gallery takes about 60% of the first screen, pushing the title, price and CTA down. | `product-vest-mobile-390.png`: gallery occupies y=139 to 597 of 844. H1 at y=619, price y=710, Add To Cart y=757. | Reduce the product image height on mobile (product page image ratio in the product page settings) or cap the gallery height with Custom CSS (c). | (a) / (c) | S |
| V-04 | Low | Tap targets are small: footer legal links are 12 to 14 px tall; desktop header text links are 23 px; the cookie buttons are 42 px. 9 to 23 elements per view are under 44 px. | `measure.json` `tap_small_sample`: "Privacy Policy" 60x12 (desktop), 69x14 (mobile); "Cookie Policy" 59x12; "Imprint" 32x12. Cookie buttons 95 to 133 x 42. | Add vertical padding to footer links and header text links with Custom CSS (c). Keep the cookie buttons; 42 px is close to the 44 px target. | (c) | S |
| V-05 | Low | Small text: cookie-bar copy and footer links render at about 9.5 px (desktop) and 11 px (mobile). 5 to 7 text nodes per view are under 12 px. | `measure.json` `font_min` 9.544 (desktop), 10.97 (mobile); `font_below_12px` 5 to 7. | Raise the cookie-bar and footer font size with Custom CSS (c). Body copy is fine. | (c) | S |
| V-06 | Low | Home trust signal is not in the mobile first screen. The "4.9 from 1,400+ customers" badge appears only on desktop above the fold. | `home-desktop-1440.png` shows the badge over the hero image; `home-mobile-390.png` shows hero, H1, paragraph and CTAs only. | Optional: move the rating line under the mobile CTAs (d). | (d) | S |

Checked and fine: H1 and primary CTA above the fold on home at both sizes (`Shop the collection` at y=609 desktop, y=521 mobile). Product H1, price and Add To Cart above the fold on desktop (`product-vest-desktop-1440.png`: Add To Cart y=351 to 406).

## Limits and not checked

- Headless Chromium on macOS, not a real iPhone or Android device. Mobile screenshots at device pixel ratio 1, not 2.
- Fresh browser profile: the cookie bar is shown on first visit. Returning visitors with stored consent will not see it.
- No LCP or CLS values captured (LCP entries empty in the headless run). I-06 and I-08 are unconfirmed.
- `capture_screenshot.py` uses fixed presets (desktop 1920x1080, mobile 375x812 at 2x). I used a Chrome DevTools Protocol script instead, to get the 1440 and 390 widths requested. Script: scratchpad `shot.mjs`; raw measurements: scratchpad `measure.json`.
- Not verified: browser format negotiation (WebP vs JPEG per request); total image bytes fetched on /shop scroll; the desktop 1920 and 1366 and tablet views (not requested).
- `og:image` HEAD for the site-wide PNG returned a content-length of 1 and was not re-measured; dimensions taken from the meta tags.
- Image-request budget: 15 used (10 HEAD, 3 range GET, 2 HEAD following redirects).

## Evidence index

Screenshots in `screenshots/`:
- `home-desktop-1440.png`, `home-mobile-390.png`
- `shop-desktop-1440.png`, `shop-mobile-390.png`
- `shop-sweaters-desktop-1440.png`, `shop-sweaters-mobile-390.png`
- `product-vest-desktop-1440.png`, `product-vest-mobile-390.png`

Crawl HTML cited: `crawl/html/` (file names as quoted in the table).
