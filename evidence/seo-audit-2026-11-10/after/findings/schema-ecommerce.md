# Schema and e-commerce re-audit: autumnandwool.com (after-state, 2026-11-10)

Scope: `after/crawl/pages.tsv` (59 rows) and `after/crawl/html/` (55 non-empty files; 4 are 0 bytes: `http-*`, the apex 301, and the old single-`p` grey lambswool URL). Feed: `autumnandwool-google-feed.tsv` (98 rows) and `build_google_feed.py`, both unchanged (last commit 2026-10-21, no working-tree changes). No live fetching. Validator: `schema_ecommerce_validate.py` run on all 22 Product blocks.

Method: all JSON-LD re-extracted from the 55 files; embedded Squarespace product JSON parsed for every PDP (price, stock, SKU); feed rows compared to that JSON, to each page's canonical, and to the page's image IDs; visible text checked for prices, shipping/returns, cross-links, H1s.

## Scores

| Score | First audit | Re-audit | Like-for-like (same formula, see caveat) |
|---|---|---|---|
| Schema / Structured Data | 45/100 | **46/100** | 43 to 46 (+3) |
| E-commerce readiness | 60/100 | **51/100** | 59 to 51 (-8) |

Rubric caveat: the first audit did not record point weights. I re-scored with a severity deduction rubric: start at 100; each open finding costs High 7, Medium 4, Low 1, Info 0; PARTLY FIXED costs half; FIXED and no-action cost 0; NOT FIXABLE ON PLATFORM costs full (platform limits keep costing points). Applied to the first-audit statuses, the same formula gives 43 (schema) and 59 (e-commerce) against the recorded 45 and 60. So the reliable comparison is the like-for-like column.

Schema point by point (deductions 57 to 54):
- Relief -16: S-02 site suffix removed from all 22 Product names and titles (-7); S-03 unsourced 4.9 claim reworded to an Etsy attribution (-3.5); S-04 opening hours removed from LocalBusiness (-3.5); S-05 email aligned to the visible address (-2).
- Added +13: N-01 Organization `telephone` left as empty string (-4); N-02 Product name differs from H1 on 7 PDPs (-4); N-03 availability contradicts the PDP copy (-4); N-08 no top-level Product `url`/`sku` on 15 AggregateOffer PDPs (-1).

E-commerce point by point (deductions 41 to 49):
- Added +10: N-03 availability contradiction (-4); N-05 black cardigan PDP has no shipping/returns text (-4); N-04 feed titles diverge from live names (-1); N-06 PDP `<title>` no longer carries the brand (-1).
- Relief -2: E-07 partly (manual "Also see" links now on all 22 PDPs; native related block still off).
- Unchanged: E-01 to E-06, E-08 to E-11 (feed generator, reviews, category metadata, stock test, gift card policy, taxonomy IDs, URL pattern).

## Status of first-audit findings

Counts: FIXED 1 (S-02). PARTLY FIXED 4 (S-03, S-04, S-05, E-07). NOT FIXABLE ON PLATFORM 7 (S-01, S-08, S-09, S-11, S-12, S-13, S-18). OPEN 14 (S-06, S-07, S-10, S-14, E-01 to E-06, E-08 to E-11). No action / still correct 4 (S-15, S-16, S-17, E-12).

| ID | Sev | Status | Fresh evidence |
|---|---|---|---|
| S-01 | High | NOT FIXABLE ON PLATFORM | 15 of 22 Product blocks still `"@type": "AggregateOffer"` (e.g. turtleneck `"lowPrice": 110.0, "highPrice": 110.0, "offerCount": 36`). The 7 single-variant PDPs emit `"@type": "Offer"` with price, sku and url, so the cause is variant count, which is a product-structure decision. Note for the validator: its High rule is written against Merchant listings. Google's Product snippet accepts AggregateOffer with a price range. |
| S-02 | High | FIXED | Names and titles no longer carry the suffix on any PDP, e.g. `"name": "Open-Front Wool Cardigan with Side Slits"` (no `\|`). `<title>` on the same page: "Open-Front Wool Cardigan with Side Slits". Residual punctuation mismatch with H1 is tracked as N-02. |
| S-03 | High | PARTLY FIXED | Claim reworded on home and About: "4.9 ★ from 1,400+ reviews on Etsy", "8,000+ orders on Etsy". The source is now named, but the figures cannot be checked from the crawl. No review or rating markup anywhere (`aggregateRating`, `review`, `ratingValue`: 0 hits). |
| S-04 | High | PARTLY FIXED | `openingHours` gone (0 hits). LocalBusiness is still emitted on all 52 pages with `"name": "AUTUMN AND WOOL, SIA"`, `"address": "22d Braslas iela\nRīga, , 1035\nLatvia"`. The address is now visible in the contact page and footer ("Braslas iela 22d, Rīga, LV-1035, Latvia"), but the site calls it a "Studio" and gives no visit information. Whether LocalBusiness applies to an online shop is an owner decision. |
| S-05 | Med | PARTLY FIXED | Email now matches the visible address: `"email": "autumnandwool@gmail.com"` (footer: "autumnandwool@gmail.com"). `info@autumnandwool.com` is gone. The phone was removed but left as `"telephone": ""` (see N-01). |
| S-06 | Med | OPEN | Organization keys are still `legalName, address, email, telephone, sameAs, @context, @type`. No `name`, `url` or `logo`, on all 52 pages. |
| S-07 | Med | OPEN | `address` still a plain string with a blank region (`"Rīga, , 1035"`). `image` still `https://static1.squarespace.com/static/6908755e4a17f81b7629f4bc/t/6925818ed87343383b55e7bc/1794322646867/` (folder path, trailing slash; not fetched). |
| S-08 | Med | NOT FIXABLE ON PLATFORM (page part) | 0 of 22 Product blocks have `shippingDetails` or `hasMerchantReturnPolicy` (validator: 22 and 22). Feed header still has no shipping column; `build_google_feed.py` still writes `cols[:-1]`. Merchant Center shipping and returns settings not checked. |
| S-09 | Med | NOT FIXABLE ON PLATFORM | `"@context": "http://schema.org"` on all blocks; Product `image` is `http://static1.squarespace.com/...` on 22/22; WebSite `image` is protocol-relative. |
| S-10 | Med | OPEN | WebSite still `"description": ""` on all 52 pages. WebSite now has `"url": "https://www.autumnandwool.com"` (not in the first audit; a positive change). |
| S-11 | Low | NOT FIXABLE ON PLATFORM | No BreadcrumbList. Visible breadcrumb is one level: "The collection › Oversized Merino Wool V-Neck Sweater Vest" (product-nav-breadcrumb). |
| S-12 | Low | NOT FIXABLE ON PLATFORM | No `gtin`, `mpn`, `itemCondition` on any Product. Feed keeps `identifier_exists=no`. Handmade goods: acceptable. |
| S-13 | Low | NOT FIXABLE ON PLATFORM | No ProductGroup. Turtleneck (36 offers) and beanie (11 offers) are single AggregateOffer Products with no color or size. |
| S-14 | Low | OPEN | Organization and LocalBusiness both declare `AUTUMN AND WOOL, SIA`. Duplicate entity signal remains because LocalBusiness is still emitted. |
| S-15 | Low | NO ACTION (still correct) | No FAQPage, QAPage or HowTo markup on any page (0 hits). Do not add FAQPage. |
| S-16 | Info | NO ACTION | No SearchAction (0 hits). |
| S-17 | Info | NO ACTION | Validator `missing-member-program` still fires on 22/22; not applicable to this shop. |
| S-18 | Low | NOT FIXABLE ON PLATFORM | 404 test page still emits WebSite, Organization and LocalBusiness. |
| E-01 | High | OPEN | Feed still `in_stock` on all 98 rows (`'in_stock'` in `build_google_feed.py`). Live stock unchanged from the first audit: 0 SKUs at zero, 17 SKUs at 1 or 2 (e.g. `SQ2078364` qty 1, `SQ9088173` qty 2). The feed is not regenerated from stock. |
| E-02 | High | OPEN | Generator unchanged: product data still literal lists in `build_google_feed.py`; output still `/mnt/user-data/outputs/autumnandwool-google-feed.tsv`. |
| E-03 | Med | OPEN | Feed still 98 product rows (99 lines with header) against the owner's 99 approved. Not reconciled; needs the Merchant Center list. |
| E-04 | Med | OPEN | Wording still differs: gift page "Free shipping to eligible destinations"; FAQ "Shipping is free to Latvia, the US and other destinations offered at checkout"; PDPs unconditional "Free shipping."; returns FAQ "unworn, unwashed items in original condition" vs shipping page "Unworn, unused items can be returned within 14". |
| E-05 | Med | OPEN | `/shop/cardigans`, `/shop/sweaters`, `/shop/vests`, `/shop/sets`, `/shop/beanies--hats`, `/shop/gift`, `/shop/winter-wool-gifts`: h1 count 0, meta description length 0, titles 66 to 79 chars with the repeated suffix. Only `/shop` (root) has a meta description now (152 chars). The `/wool-*` landing pages do have an H1 and meta descriptions (122 to 150 chars). |
| E-06 | Med | OPEN | No review UI or review count on any PDP. Embedded store settings still `"productReviewsEnabled":false` on all 52 pages. Whether this plan can enable native reviews is unverified. |
| E-07 | Med | PARTLY FIXED | Native related block still off: `"relatedProductsEnabled":false`, section title "Pairs well with" configured but not shown. Manual "Also see:" block now on all 22 PDPs with exactly 2 product links each (e.g. vest page: "Also see: Oversized Wool V-Neck Vest - Beige Melange", "Also see: Merino Wool Raglan Cardigan"). All 44 link instances (22 PDPs x 2) resolve to status 200 in the crawl. Origin date of these links unknown. |
| E-08 | Med | OPEN | No SKU is sold out, so the sold-out state is still not observed. No product data changed. |
| E-09 | Low | OPEN | Gift card still `"@type": "AggregateOffer"`, `"lowPrice": 25.0, "highPrice": 250.0, "offerCount": 5`; not in feed. Merchant Center digital-goods policy not checked. |
| E-10 | Low | OPEN | Category IDs (`212`, `173`) unchanged in the script; not checked against the current Google taxonomy. |
| E-11 | Low | OPEN (changed) | Old single-`p` grey lambswool URL was 404 in the first audit. It is now a 301 to `http://www.autumnandwool.com/shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper`, which adds a hop through http. The pattern is still undocumented. See N-07. |
| E-12 | Info | STILL TRUE | 98/98 feed image IDs found on their PDP. |

## New findings

| ID | Sev | Area | Finding | Evidence |
|---|---|---|---|---|
| N-01 | Med | Schema | Organization `telephone` is an empty string on every page (52). Invalid value; the phone was removed but the key was kept. | `"telephone": ""` in the Organization block on all pages. |
| N-02 | Med | Schema | Product JSON-LD `name` differs from the visible H1 on 7 of 22 PDPs (10 more differ only by punctuation). | JSON-LD "Merino Wool Raglan Cardigan in Black, Brown or Blue" vs H1 "Merino Wool Raglan Cardigan"; "Oversized Merino Turtleneck, Dusty Pink" vs H1 "Oversized Merino Turtleneck — Dusty Pink Raglan"; "Oversized Merino Wool Sweater Vest" vs H1 "Oversized Merino Wool V-Neck Sweater Vest"; "Long Wool Shawl Collar Cardigan" vs H1 "Long Wool Cardigan with Shawl Collar"; plus three word-order cases. |
| N-03 | Med | Schema and E-com | Availability contradicts the copy. Black raglan cardigan PDP says "Brown and Blue are machine-knitted and hand-finished to order", but JSON-LD is `"availability": "InStock"` on the AggregateOffer (offerCount 3) and the feed lists Brown (`SQ7601591`) and Blue (`SQ1988154`) as `in_stock` with qty 2. Owner must confirm what "to order" means for stock. |
| N-04 | Low | E-com | Feed titles not synced to live names. 14 of 21 feed products (76 of 98 rows) differ from the live Product name. Turtleneck example: feed "Merino Turtleneck — Women’s Lightweight Knit (Berry Purple, M)" vs live "Lightweight Merino Turtleneck, 12 Colours" (the first audit quotes the same old H1). Seven products match after punctuation normalisation. Title is not in the must-match list (price, availability, link, image), so this is a consistency issue; Merchant Center diagnostics not checked. |
| N-05 | Med | E-com | Black raglan cardigan PDP has no shipping or returns text at all (no "Free shipping", no "14-day returns", no DELIVERY & RETURNS block). The other 20 physical PDPs have it. Gift card also has none; acceptable for a digital card if the owner agrees. Not mentioned in the first audit, which may mean it predates today. |
| N-06 | Low | E-com | PDP `<title>` no longer carries "Autumn & Wool" (e.g. "Oversized Merino Wool Sweater Vest", 34 chars). Brand recall in search results may drop. Not measured. |
| N-07 | Low | E-com | Old single-`p` grey lambswool URL now 301s to an `http://` location (2 hops to https). Folded into E-11 deduction, not counted twice. |
| N-08 | Low | Schema | No top-level `url` or `sku` on any Product. `sku` and `offers.url` appear only on the 7 single-offer PDPs. |
| N-09 | Info | Schema | WebSite `image` is `https://images.squarespace-cdn.com/...ChatGPT+Image+Nov+25%2C+2025...png`. Filename suggests a generated image. Owner to confirm it is the intended brand image. |

## Schema validation (fresh, 22 Product blocks + site blocks)

- Product: keys present on all 22 are name, image, description, brand, offers, @context, @type. Offer type: Offer 7, AggregateOffer 15 (incl. gift card). Validator ok: 7/22, same as first audit. Findings: High merchant-listing-offer-type 15; Medium recommended-offer-price 15, missing-return-policy 22, missing-shipping-details 22, missing-member-program 22 (not applicable); Info no-product-group 22.
- Product snippet view: name, image and offers with price are present on all 22 in the JSON-LD. No review or rating markup, so no stars are being claimed (correct).
- Organization: no name, url or logo. Google's logo eligibility needs logo. `telephone` empty string (N-01).
- WebSite: name and url valid; description empty; no SearchAction (correct, not needed).
- LocalBusiness: physical-location markup for a studio whose visit status is not stated; address is a string, not PostalAddress (S-07).
- Contextual: absolute URLs for canonicals and links; image and @context over http (S-09); no HowTo, FAQPage, QAPage, AggregateRating or Review types anywhere.

## PDP completeness, links, reviews, related products, categories, gift card

- Price: visible price on the page matches JSON-LD on 22/22 (€126.00, €155.00, €136.00 etc.). "€120" on the hat and scarf page is FAQ text, not a price.
- H1: present on 22/22 PDPs and matches the Product name in 15 of 22 cases after punctuation normalisation (N-02).
- Canonical equals og:url on all PDPs. `product:availability` "instock" and `product:price:amount` on all.
- Internal links from PDPs: site navigation plus two manual "Also see" product links each (E-07). Breadcrumb is single-level.
- Reviews: none, and the store setting is off (E-06).
- Related products: none automated (E-07).
- Categories: `/shop/*` store categories have no H1 and mostly no meta description (E-05). `/wool-*` landing pages are fine on H1 and meta. Two parallel category sets (`/shop/sweaters` and `/wool-sweaters`, etc.) target similar terms; both self-canonical; no change recommended here.
- Gift card: present as Product (AggregateOffer 25 to 250, 5 options), excluded from feed. Policy check still open (E-09).

## Feed alignment (98 rows vs live)

- 98/98 SKUs found in live product JSON; 98/98 prices equal the live variant price; 98/98 `link` equals the live canonical; 98/98 image IDs on the PDP.
- Stock: 0 SKUs at zero; 17 SKUs at qty 1 or 2 (same 17 as first audit). All 98 still `in_stock` (E-01).
- Titles: see N-04. Gift card not in feed.
- Row count 98 vs 99 approved (E-03, OPEN).

## Not checked

- Merchant Center console (diagnostics, approved count, shipping and returns settings, digital gift card policy, title warnings).
- Squarespace admin (Business Information fields, SEO title override, plan features for reviews and related products).
- Live rendering and Google Rich Results Test (saved HTML only; no JS run).
- Image URL reachability (not fetched).
- No pre-change crawl exists in `after/`, so I cannot date which of today's changes produced each delta; deltas are against the first-audit quotes.
- Which 15 products were renamed today (14 feed groups now diverge; the 15th is either the gift card or one of the 7 that still match).
- Origin of the "Also see" links and the missing shipping block on the black cardigan.
- Etsy review and order figures (4.9, 1,400+, 8,000+): the claim is now attributed, not verified.
- Sold-out display (E-08); DataForSEO data (not in scope).
