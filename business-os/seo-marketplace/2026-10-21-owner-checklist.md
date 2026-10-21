# Owner checklist: SEO, Merchant Center, Pinterest, Etsy (week of 21 Oct)

DRAFT from aw-seo-marketplace. Tasks SEO-02, 05, 06, 07, 09. All steps are owner-only (logins). Each is under 15
minutes (ruling C11). Send me screenshots or exports; I turn them into the next deliverables.

## 1. Merchant Center (today, 21 Oct checkpoint): about 5 min
- [ ] Products → Diagnostics: screenshot of the item-issues table and the counts (approved / limited / disapproved / pending).
- [ ] Products → All products: filter "Disapproved", screenshot the first page.
- [ ] Open both URLs side by side and tell me which shows the **brown** cardigan (feed QA F5):
  - `https://images.squarespace-cdn.com/content/v1/6908755e4a17f81b7629f4bc/1762677080229-61UOLLY9NEB98MTXF359/image_10.jpg?format=1500w` (in the live feed now)
  - `https://images.squarespace-cdn.com/content/v1/6908755e4a17f81b7629f4bc/1762677181680-ROINLJPXW23F9IBWGYYN/image_10.jpg?format=1500w`
- [ ] No re-upload yet (wait for photos, ruling C7).

## 2. Google Search Console: about 10 min
Already done (incident log round 6): URL-prefix property `https://www.autumnandwool.com/` verified; sitemap submitted 18 Oct, status Success, 37 URLs.
- [ ] Performance → Search results → last 3 months → Export (Google Sheets or CSV): Queries and Pages tabs. This is the only way I can fill positions and find the 8–20 quick wins.
- [ ] Pages (indexing) report: screenshot of "Why pages aren't indexed" with the reasons.
- [ ] URL Inspection → "Request indexing" for these 10 URLs (one by one; Google limits daily requests):
  1. `/shop/p/p/black-merino-wool-cardigan-100-merino-wool-raglan-sweater-minimalist-knitwear-sustainable-handmade-womens-cardigan-1`
  2. `/shop/p/p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1`
  3. `/shop/p/p/hand-knitted-merino-wool-striped-sweater-oversized-jumper`
  4. `/shop/p/oversized-merino-wool-v-neck-sweater-vest`
  5. `/shop/p/p/merino-wool-hat-scarf-set-extra-fine-rib-knit-soft-on-skin-warm-not-bulky-unisex-gift`
  6. `/shop` 7. `/shop/sweaters` 8. `/shop/cardigans` 9. `/shop/vests` 10. `/size-guide`
  (PDPs 1–5 are a provisional working set; swap in the GM's 5 once decision 2 is made.)
- [ ] Optional: add a Domain property (DNS TXT) so `http://` and non-`www` variants are covered too.

## 3. Bing Webmaster Tools: about 5 min
- [ ] bing.com/webmasters → "Import from Google Search Console" (no DNS work), then submit `https://www.autumnandwool.com/sitemap.xml`. Bing feeds ChatGPT search (GROWTH-PLAN S1).

## 4. Site clean-up in Squarespace: about 10 min
- [x] `/redesign-preview`: returns 404 on 21 Oct (checked). Nothing to do.
- [ ] Settings → Advanced → URL Mappings: add `/home -> / 301` (`/home` is still in the sitemap, last modified 28 Jan).
- [ ] `/shop/gift`: hide, or merge into `/shop/winter-wool-gifts` (see gift guide proposal).

## 5. Rich Results Test: about 5 min
- [ ] At https://search.google.com/test/rich-results, test the 5 PDPs from step 2 (1–5) and screenshot each result (detected items + warnings).
  Why: a page fetch cannot see JSON-LD that scripts inject, so only Google's test can confirm Product schema with name, image,
  offers (price, priceCurrency, availability). GROWTH-PLAN S6 found the cardigan has no `price` because of its variants;
  this test confirms or clears that.

## 6. Pinterest: about 10 min (after decisions 10/18)
- [ ] Decide: rename `mmareshop` (keep followers) or new account.
- [ ] Convert to a business account; claim `autumnandwool.com`.
- [ ] Profile website: `https://www.autumnandwool.com/shop?utm_source=pinterest&utm_medium=social&utm_campaign=bio-link`.
- [ ] Name and About text: see [Pinterest plan](2026-10-21-pinterest-plan.md). Do not post pins yet.

## 7. Etsy (only after decision 9: is Mareshop still selling?): about 10 min
- [ ] Tell me: active or not, and whether both channels stay open this season.
- [ ] If active: Shop Manager → Settings → Options → Download data → Listings CSV, plus Stats → last 30 days (screenshot of the listing table). I then score and rewrite 5 listings.

## 8. Stock truth (decision 4, 24 Oct)
- [ ] For each SKU in the feed: physical stock today, or "made to order". The 17 Oct export shows 10 per turtleneck variant and 20 per beanie colour, which look like placeholders. The feed `availability` follows your answer.
