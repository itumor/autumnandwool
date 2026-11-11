# End-to-end QA, live store, 2026-11-10

Target: https://www.autumnandwool.com (live, public). Read-only except one add-to-cart of the Oversized Merino Wool V-Neck Sweater Vest, removed again.
Browser: ego-browser task space `aw-e2e-qa-2026-11-10-a` (space 14), closed at the end.
Scratch scripts: `scratchpad/e2e/`. Link results: `scratchpad/e2e/link_results.txt`, image results: `scratchpad/e2e/img_results.txt`, wording hits: `scratchpad/e2e/t7_hits.json`.

Screenshots (this run): `after/screenshots/<slug>-desktop.png` and `<slug>-mobile.png` for the 9 new pages (T2); `after/screenshots/reg-<slug>-<desktop|mobile>.png` for the T3 pages; `after/screenshots/t4-checkout-desktop.png` (T4). Files named `audit-*.png` were there before this run and were not produced by it.

## Summary

| Test | Result |
|---|---|
| T1 Link integrity and new-page images | FAIL (21 of 22 image URLs on the new pages return 404) |
| T2 Rendering of 9 new pages | FAIL (product grids broken and overflowing; text pages PASS) |
| T3 Regression of edited pages | PASS with notes (selector check partial) |
| T4 Buying path | PASS |
| T5 Overlay guard | PASS |
| T6 Technical spot checks | PASS |
| T7 Banned wording sweep | FAIL (1 hit, privacy policy) |

Cart count: before 0 (cart empty), after 0 (cart empty). Item added and removed twice (desktop and mobile); final `/cart` shows "You have nothing in your shopping cart."

## T1 Link integrity: FAIL

- Internal hrefs: 52 unique URLs collected from all crawled HTML (`after/crawl/html`). Each requested once at 1 req/s with `curl -A "Mozilla/5.0"`.
- Result: 52 of 52 returned 200 on the recorded run, except `https://www.autumnandwool.com/` which returned one `301` to `http://www.autumnandwool.com` on its first request. Six immediate retries all returned 200. Treated as a transient edge response, not reproduced.
- All nine new pages return 200 and are in the sitemap.
- Images on the nine new pages: 22 unique `<img src>` URLs.
  - 1 returns 200 (header logo, `images.squarespace-cdn.com`).
  - 21 return 404. Source pattern: `http://static1.squarespace.com/static/6908755e4a17f81b7629f4bc/6908755f4a17f81b7629f4db/<id>/<ts>/image_N.jpg?format=1500w?format=500w`. The query string is doubled (`?format=1500w?format=500w`) and the host is http, not the CDN.
  - Pages affected: wool-sweaters (14 image tags), wool-cardigans (5), wool-sweater-vests (3), wool-hats-and-scarves (3). The 5 guide/gift pages had one image each or none; `wool-gifts` has no product images. Not confirmed for the guide pages, which have no product tiles.
  - Browser probe confirms the same: broken images on those four pages at desktop and mobile.

## T2 Rendering of the 9 new pages: FAIL

Checked at 1440x900 and 390x844 (full-page screenshots, probed in browser). All nine: H1 visible and styled (dark on beige), body text readable, header and footer present, no raw HTML/CSS text, no horizontal page scroll (scrollWidth equals viewport width).

Defects:

1. **wool-sweaters, wool-cardigans, wool-sweater-vests, wool-hats-and-scarves: product images broken.** Every product tile shows a grey box with alt text (`wool-sweaters-desktop.png`, `wool-sweaters-mobile.png`, `wool-cardigans-desktop.png`, `wool-sweater-vests-desktop.png`, `wool-hats-and-scarves-desktop.png`). Cause: the malformed src in T1.
2. **Product grid overflows the viewport.** Tiles are rendered at a fixed 500 px width (`width="500" height="667"` with no responsive CSS).
   - Desktop, wool-sweaters: 4 tiles at x=180 to 2229 on a 1440 px viewport. The third and fourth columns are clipped, and no horizontal scrollbar appears because the wrapper clips. `wool-sweaters-desktop.png` shows the right-hand column cut off.
   - Mobile, wool-sweaters: the second column starts at x=532 on a 390 px viewport, so the page shows one column only. `wool-sweaters-mobile.png`, `wool-cardigans-mobile.png`.
   - Vests and hats pages (2 tiles) fit on desktop but the tiles are still 500 px and the mobile second column is clipped.
   - The brief asked for a tidy 4-column desktop and 2-column mobile grid. Not met.
3. Guide and gift pages (`wool-gifts`, `how-to-wash-a-wool-sweater`, `merino-vs-lambswool`, `oversized-fit-guide`, `how-to-choose-a-wool-cardigan`): no defects found in the screenshots at either size. Headings, body text, link lists and footer all render.

## T3 Regression of edited pages: PASS with notes

| Page | Desktop / mobile | Checked | Result |
|---|---|---|---|
| Home (`reg-home-*.png`) | both | hero, trust strip "Machine-knitted, hand-finished" (present), "reviews on Etsy" link to https://www.etsy.com/shop/mareshop (present, correct), 4 category tiles to /wool-sweaters, /wool-cardigans, /wool-sweater-vests, /wool-hats-and-scarves | PASS. Note: 3 Instagram images at the bottom are lazy-loaded and were not loaded when probed (not confirmed as broken or working). |
| About (`reg-about-*.png`) | both | stats tiles "15 years as Mareshop on Etsy", "8,000+ orders on Etsy", "4.9 ... reviews on Etsy", "100% made in Riga"; "on Etsy" text (present) | PASS |
| FAQ (`reg-faq-*.png`) | both | renders, headings, questions | PASS |
| Shipping & returns (`reg-shipping-returns-*.png`) | both | renders, delivery tiles, returns steps | PASS |
| Footer sentence | all pages | "Machine-knitted, hand-finished knitwear by Kristine in Riga, Latvia. Formerly Mareshop on Etsy." | PASS |
| Header trust bar | all pages | "Free shipping · 14-day returns · Made in Riga, Latvia" visible in screenshots | PASS |
| /shop (`reg-shop-*.png`) | both | 22 product links, names updated, 2-column grid on mobile | PASS. Desktop full-page capture shows some tall empty tiles in the lower rows (lazy images not loaded at capture time). Not confirmed as broken. |
| /shop/p/oversized-merino-wool-v-neck-sweater-vest | both | H1 "Oversized Merino Wool V-Neck Sweater Vest", price €126.00, Add To Cart, gallery 1/10 loads, description ends with "More vests: wool sweater vests" and two "Also see" links | PASS. Gallery off-screen slides have empty src (alt text only); visible slide loads. |
| Pure Wool Stand-Collar Sweater - Blue (`/shop/p/p/hand-knitted-wool-stand-collar-sweater-womens-knitwear-679510`) | both | H1 correct, €136.00, description first paragraph is the stand-collar text, ends "More sweaters: wool sweaters" plus "Also see" links, all links 200 (T1). Size radios S/M/L/XL. | PASS. Size M selected by a DOM label click (checked = true). A real pointer click on the visible "M" was not accepted by ego (locator matched a hidden element). Pointer-level selector test: not conclusive. |
| Merino Rib-Knit Beanie - Unisex (`/shop/p/p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1`) | both | H1 correct, €45.00, description ends "More hats and scarves: wool hats and scarves" plus "Also see" links, gallery loads | PASS. Colour swatch selection: NOT TESTED (could not locate the swatch elements reliably). |

Layout checks on the product and listing pages: no horizontal scroll at either size (scrollWidth equals viewport).

## T4 Buying path: PASS

Desktop (1440):
1. Cart count before: 0 (`.sqs-cart-quantity` = "0", cart empty).
2. Vest page: no size or colour options exist for this product. Add To Cart clicked. Mini-cart reported "Added to cart! Oversized Merino Wool V-Neck Sweater Vest €126.00 1x". Count = 1.
3. /cart: item name "Oversized Merino Wool V-Neck Sweater Vest", price €126.00, quantity 1, subtotal €126.00. Count = 1.
4. Checkout: first click loaded a blank page at 4 s (body empty). Reloaded from the cart at 9 s: URL `/checkout?cartToken=…`, title "Autumn & Wool | Secure Checkout", headings "Your Email", "Delivery", "Payment", "Review & Purchase", order summary shows the vest. No field was filled and no form submitted. Screenshot `t4-checkout-desktop.png` taken during the blank first attempt.
5. Back to /cart, Remove clicked, /cart shows empty. Count = 0.

Mobile (390): Add To Cart on the vest page, count = 1, /cart shows the item, horizontal scroll 0. Removed, count = 0.

## T5 Overlay guard: PASS

- `https://www.autumnandwool.com/site.css` (linked from the homepage) contains `.sqs-widgets-confirmation-overlay{pointer-events:none !important}` and `.sqs-widgets-confirmation{pointer-events:none !important}`.
- After Add To Cart (desktop and mobile), the mini-cart, cart and remove buttons were all clickable and responded.

## T6 Technical spot checks: PASS

- Sitemap: 48 `<loc>` entries. All nine new URLs present (wool-sweaters, wool-cardigans, wool-sweater-vests, wool-hats-and-scarves, wool-gifts, how-to-wash-a-wool-sweater, merino-vs-lambswool, oversized-fit-guide, how-to-choose-a-wool-cardigan).
- robots.txt: no `Disallow: /` line. Groups for AI crawlers and `User-agent: *` with the usual Squarespace disallows. Not compared to a pre-change copy; "unchanged in substance" is not verified against a baseline.
- llms.txt: HTTP 200, contains "wool-gifts" (2 hits).
- Homepage JSON-LD: contains autumnandwool@gmail.com (in the Organization block); no `openingHours`.
- Product JSON-LD name (vest): "Oversized Merino Wool Sweater Vest". No " | Autumn & Wool" suffix. Note: this differs from the H1 "Oversized Merino Wool V-Neck Sweater Vest".
- Redirects, one hop each: `http://www.autumnandwool.com/` to `https://www.autumnandwool.com/`; `https://autumnandwool.com/` to `https://www.autumnandwool.com/`; `http://autumnandwool.com/` to `https://www.autumnandwool.com/`.
- Old URL `/shop/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper`: one redirect to `/shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper`, final HTTP 200.

## T7 Banned wording sweep: FAIL

Visible text only (scripts, styles, tags, URLs stripped), all crawled HTML files:
- "handmade": 1 hit. `after/crawl/html/https-www-autumnandwool-com-privacy-policy.html`: "...Autumn & Wool is a handmade knitwear brand based in Riga, Latvia, creating sustainable..."
- "hand-knit": 0 hits. "hand knit": 0 hits.

## Not tested / limits

- Colour swatch selection on the beanie (not located reliably).
- Pointer-level size selection on the stand-collar (ego could not click the visible "M" label; DOM click used instead).
- Lazy-loaded images on the homepage (Instagram block) and the shop grid's lower rows were not confirmed as loaded.
- Checkout was loaded but not gone past; no payment or address data was entered by design.
- "robots.txt unchanged" was not compared to a pre-change copy.
- Mobile was not repeated for the T4 remove step beyond the cart-state check (removed and confirmed at 0).

## Defects to fix (ordered)

1. Malformed product image URLs on wool-sweaters, wool-cardigans, wool-sweater-vests, wool-hats-and-scarves (21 of 22 URLs 404). Replace the `static1` http URLs and the doubled `?format=` with working image URLs. Source for these is `business-os/seo-marketplace/live-2026-11-10/html/`.
2. Product tiles fixed at 500 px width: remove the fixed width/height attributes or add responsive CSS so the 4-column desktop and 2-column mobile grids fit the viewport.
3. Privacy policy wording: "handmade knitwear brand" (banned wording).
4. Checkout first load was blank for at least 4 s (loaded at about 9 s). Observed once; monitor.
