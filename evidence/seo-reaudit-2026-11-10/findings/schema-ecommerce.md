# Schema and E-commerce Re-audit: autumnandwool.com (2026-11-10)

Source: shared crawl, 49 pages (`evidence/seo-reaudit-2026-11-10/crawl/`). No live requests made.
Extraction: stdlib script `/private/tmp/claude-502/-Users-eramadan-autumnandwool--claude-worktrees-seo-audit-autumnandwool-eff2bf/8b31958e-8487-4d3c-99ed-c7f683f954e8/scratchpad/extract_schema.py` (output `extracted.json`, same folder).

Platform note: Squarespace 7.1 generates all JSON-LD. There is no code injection. "Fixable in Squarespace settings" means a field the merchant edits in Squarespace. Unless stated, the Squarespace-to-JSON-LD field mapping is **unverified** in this crawl.

## Detection summary

| Page type (count) | JSON-LD @types present | Microdata | Notes |
|---|---|---|---|
| Sitewide (all 49) | WebSite, Organization, LocalBusiness | `itemprop` meta only (name, url, description, image, thumbnailUrl) | Identical 3 blocks on every page |
| Product (22) | Product + Offer (7) or AggregateOffer (15) | itemprop meta only | Product JSON-LD is the only per-product block |
| Category `/shop/*` (7) | none beyond sitewide | none | No ItemList, no BreadcrumbList |
| Landing `/wool-*`, `/wool-gifts` (5) | none beyond sitewide | none | No ItemList |
| Guides (4) | none beyond sitewide | none | No Article/BlogPosting, no visible author or date |
| /faq (1) | none beyond sitewide | none | No FAQPage (correct, do not add) |
| Policy / about / contact / size-guide (~10) | none beyond sitewide | none | |

- 169 JSON-LD blocks across 49 pages. **All 169 parse as valid JSON.** No @type deprecated (no HowTo, SpecialAnnouncement, etc.).
- No BreadcrumbList, ItemList, Article, FAQPage, AggregateRating, Review, shippingDetails, or MerchantReturnPolicy on any page.

## Product validation (22 products)

Table columns: name suffix; image; description; brand; sku (Product/Offer); offer type; price matches visible; url; availability; aggregateRating; shippingDetails; hasMerchantReturnPolicy.

| # | Product (slug stem) | Offer type | name suffix | sku | url | price = visible | InStock | shipping / return |
|---|---|---|---|---|---|---|---|---|
| 1 | Oversized Merino Wool Sweater Vest | Offer | none | yes | yes | OK 126 | yes | none |
| 2 | Merino Raglan Sweater, Dusty Pink | AggregateOffer (2) | none | no | no | OK 155 | yes | none |
| 3 | Oversized Merino Turtleneck, Dusty Pink | Offer | none | yes | yes | OK 155 | yes | none |
| 4 | Pure Wool Stand-Collar Sweater, Blue | AggregateOffer (4) | none | no | no | OK 136 | yes | none |
| 5 | Pure Wool Stand-Collar Sweater, Beige | AggregateOffer (4) | none | no | no | OK 136 | yes | none |
| 6 | Lightweight Merino Turtleneck, 12 Colours | AggregateOffer (36) | none | no | no | OK 110 | yes | none |
| 7 | Open-Front Wool Cardigan with Side Slits | Offer | none | yes | yes | OK 155 | yes | none |
| 8 | Long Wool Shawl Collar Cardigan | AggregateOffer (4) | none | no | no | OK 145 | yes | none |
| 9 | Long Wool Shawl Cardigan, 100% Wool | AggregateOffer (4) | none | no | no | OK 145 | yes | none |
| 10 | Merino Striped Oversized Sweater | Offer | none | yes | yes | OK 165 | yes | none |
| 11 | Distressed Oversized Wool Raglan Sweater | Offer | none | yes | yes | OK 155 | yes | none |
| 12 | Women's Classic Lambswool Crew Sweater | AggregateOffer (4) | none | no | no | OK 136 | yes | none |
| 13 | Lambswool Raglan Crew Sweater, Green | AggregateOffer (4) | none | no | no | OK 136 | yes | none |
| 14 | Lambswool Raglan Crew Sweater, Brown | AggregateOffer (4) | none | no | no | OK 136 | yes | none |
| 15 | Pure Wool Side-Slit Sweater, Light Grey | AggregateOffer (4) | none | no | no | OK 136 | yes | none |
| 16 | Pure Wool Side-Slit Sweater, Camel | AggregateOffer (4) | none | no | no | OK 136 | yes | none |
| 17 | Merino Rib-Knit Beanie, Unisex | AggregateOffer (11) | none | no | no | OK 45 | yes | none |
| 18 | Merino Wool Hat & Scarf Set | AggregateOffer (3) | none | no | no | OK 110 | yes | none |
| 19 | Oversized Wool Raglan Sweater, Beige Melange | Offer | none | yes | yes | OK 155 | yes | none |
| 20 | Oversized Wool V-Neck Vest, Beige Melange | Offer | none | yes | yes | OK 126 | yes | none |
| 21 | Merino Wool Raglan Cardigan, Black/Brown/Blue | AggregateOffer (3) | none | no | no | OK 160 | yes | none |
| 22 | Digital Gift Card for Wool Knitwear | AggregateOffer (5, 25-250) | none | no | no | OK "from 25" | yes | none |

Common to all 22: `brand` is "Autumn & Wool" (string), `description` present (128-155 chars), `image` present (one URL, `http://static1...?format=1500w`), no `aggregateRating`, no `review`, no `gtin`/`mpn`, no `shippingDetails`, no `hasMerchantReturnPolicy`, no `color`/`size`/`material`, and **no Product-level `url`**.

Summary: 7 Offer, 15 AggregateOffer. 0 of 22 have aggregateRating/review. Visible price matches JSON-LD on 22/22.

## Findings

Severity: Critical / High / Medium / Low / Info. "Pass" = validated OK.

### Product

**S-01 (High). Product `sku` missing on 15 of 22 products (all AggregateOffer).**
Evidence: `shop__p__p__merino-wool-turtleneck-...-679428`: `"@type":"AggregateOffer","lowPrice":110.0,"highPrice":110.0,"offerCount":36` with no `sku`. The same page's variant JSON holds 36 SKUs (`"sku":"SQ..."`).
Fixable: Partly. Variant SKUs are editable in Squarespace product settings. Whether they reach AggregateOffer is unverified. The alternative is Merchant Center `id`/`gtin`.

**S-02 (High). Product `url` missing on all 22 products; `url` on Offer only (7).**
Evidence: `"offers":{"@type":"AggregateOffer", ...}` has no `url`. Product has no `url`.
Fixable: Platform limit (no injection). Merchant Center provides the product link in the feed.

**S-03 (High, merchant listings). No `shippingDetails` on any product.**
Evidence: no `shippingDetails` string in any of 49 pages. Visible copy says "Free shipping. In-stock items ship from Riga within 2–5 working days." (`llms.txt`: "free to Latvia, the United States and other destinations shown at checkout").
Fixable: Platform limit. Cover via Merchant Center shipping settings. Destination list needs owner confirmation before stating any destination.

**S-04 (High, merchant listings). No `hasMerchantReturnPolicy` on any product.**
Evidence: visible copy "14-day returns" (PDP "DELIVERY & RETURNS"; `shipping-returns` page).
Fixable: Platform limit. Cover via Merchant Center return policy.

**S-05 (Medium). No `gtin`/`mpn` on any product.**
Fixable: Platform limit. Merchant Center `gtin` field if GTINs exist (owner input needed; not verified).

**S-06 (Medium). Colour variants published as separate products with no ProductGroup grouping.**
Evidence: Stand-Collar Blue/Beige; Lambswool Raglan Green/Brown; Side-Slit Light Grey/Camel; Merino Raglan/Black cardigan variants. Each has its own URL and Product block.
Fixable: Platform limit. Merchant Center `item_group_id`.

**S-07 (Low). `color`, `size`, `material` not in Product JSON-LD.**
Evidence: variant JSON carries `"attributes":{"Size":"S"}` and `"Primary color"`; PDP text "Material: 100% pure new wool". Turtleneck: `Size=M,S,XS`, `Primary color` 12 values.
Fixable: Platform limit. Merchant Center attributes.

**S-08 (Low). One image per product in JSON-LD; gallery has 8 (Squarespace originalSize 2250x3000).**
Evidence: `"image":"http://static1.squarespace.com/.../image_1.jpg?format=1500w"` (one string).
Fixable: Platform limit. Merchant Center `additional_image_link`.

**S-09 (Medium). `http://` image URLs in all Product JSON-LD and all og:image tags (49/49 pages).**
Evidence: `"image":"http://static1.squarespace.com/static/6908755e..."`; `<meta property="og:image" content="http://static1.squarespace.com/...">` on all 49 pages.
Fixable: Platform limit (Squarespace emits http for static1). Not verified whether https variant exists.

**S-10 (Low). `@context` is `http://schema.org` in all 169 blocks.**
Evidence: `"@context":"http://schema.org"` in every block.
Fixable: Platform limit. Google parses http and https equivalently, so this is cosmetic against the house rule.

**S-11 (Low). Product name differs from H1 on 7 of 22 products.**
Evidence: JSON `"Long Wool Shawl Cardigan, 100% Wool"` vs H1 `"100% Wool Long Shawl Cardigan"`. `"Merino Raglan Sweater, Dusty Pink"` vs H1 `"Merino Wool Raglan Sweater - Dusty Pink"`. Others: Vest, Turtleneck, Cardigan (Long Wool), Hat & Scarf Set, Raglan Cardigan.
Fixable: Yes, Squarespace product title (name is the visible title; JSON name is generated from it). Unverified mapping.

**S-12 (Info). No name suffix on any product.** Pass. Names contain no " | Autumn & Wool". Page `<title>` also lacks suffix on products.

**S-13 (Low). AggregateOffer hides which variant carries which price.**
Evidence: Turtleneck AggregateOffer covers 36 variants at a single price. Not a defect, but no `offers` array, so no per-variant `availability` or `sku`.
Fixable: Platform limit.

**S-14 (Low). Product og:image dimensions below 1200 px on 2 products; og:twitter card is summary on all 49 pages.**
Evidence: Striped sweater `og:image:width 1024 / height 1536`; Gift card `1024 / 1024`. `twitter:card` = `summary` on 49/49.
Fixable: Image upload size is fixable (Squarespace product image). `twitter:card` is a template setting, platform limit.

**S-15 (Info). No `aggregateRating`/`review` on any product: correct.** `productReviewsEnabled: false` in page JSON. Home page text says "4.9 ★★★★★ from 1,400+ reviews on Etsy" (visible, off-site, not marked up). Do not mark up Etsy reviews on the site. Google review snippet policy forbids self-serving or off-site review markup. Pass.

### Sitewide (Organization / LocalBusiness / WebSite)

**S-16 (Medium). Organization has no `name`, `url`, or `logo`.**
Evidence: `"@type":"Organization","legalName":"AUTUMN AND WOOL, SIA","address":"22d Braslas iela\nRīga, , 1035\nLatvia","email":"autumnandwool@gmail.com","telephone":"","sameAs":[...]`. Keys: @type, address, email, legalName, sameAs, telephone.
Fixable: Yes, likely in Squarespace Site Settings (site title, logo) and Business Information. Mapping unverified.

**S-17 (Low). `telephone: ""` (empty string) on Organization.**
Fixable: Yes. Business Information phone, or remove. Empty values are invalid.

**S-18 (Low). Address is a plain string with embedded newline, empty locality, no PostalAddress type.**
Evidence: `"address":"22d Braslas iela\nRīga, , 1035\nLatvia"`.
Fixable: Yes, Business Information address fields. Mapping unverified.

**S-19 (Medium). LocalBusiness `image` is a folder URL with no file.**
Evidence: `"image":"https://static1.squarespace.com/static/6908755e4a17f81b7629f4bc/t/6925818ed87343383b55e7bc/1794322646867/"` (trailing slash, no file).
Fixable: Yes, upload a logo/site image in Squarespace. Mapping unverified.

**S-20 (Medium). LocalBusiness on an online-only shop with no storefront.**
Evidence: `"@type":"LocalBusiness","name":"AUTUMN AND WOOL, SIA","address":...`; no openingHours (correct, none present).
Note: LocalBusiness rich results require a customer-visited location. Studio address is not a shop floor. Consider leaving as entity markup only, or drop LocalBusiness and keep Organization.
Fixable: Platform limit on type; Business Information controls the content.

**S-21 (Low). Name inconsistency across entities.**
Evidence: Organization/LocalBusiness `"AUTUMN AND WOOL, SIA"` / `legalName`; WebSite `name` and Product `brand` `"Autumn & Wool"`; `og:site_name` `"Autumn &amp; Wool"`.
Fixable: Set brand name in Squarespace; legalName stays as company name.

**S-22 (Low). `sameAs` includes legacy Mareshop accounts.**
Evidence: `"https://www.facebook.com/AccessoriesMareshop"`, `"https://www.pinterest.com/mmareshop/"`.
Fixable: Confirm ownership and that accounts are still active. Owner check.

**S-23 (Low). WebSite `description` empty; WebSite `image` protocol-relative.**
Evidence: `"description":""`; `"image":"//images.squarespace-cdn.com/content/v1/..."`.
Fixable: Site description is editable in Squarespace SEO settings. Protocol-relative URL is platform.

**S-24 (Pass). WebSite `name` and `url` present and absolute (`https://www.autumnandwool.com`). No openingHours anywhere on site.**

### Breadcrumbs, lists, articles, FAQ

**S-25 (Low). No BreadcrumbList on any page, including product pages.**
Evidence: product pages have visible breadcrumb `Shop > <product>` (`product-nav-breadcrumb-link`), no category level.
Fixable: Platform limit (no injection, no feed equivalent). Accept or add category level via Squarespace collection structure.

**S-26 (Low). No ItemList on `/shop`, category pages, or `/wool-*` landing pages.**
Evidence: `/shop` has 22 product links; `/shop/sweaters` 13; `/wool-sweaters` 13; `/wool-gifts` 7.
Fixable: Platform limit.

**S-27 (Low). Four guides have no Article/BlogPosting, no datePublished, no visible author or date.**
Evidence: no `datePublished`, `dateModified`, `author` anywhere in crawl; no visible publish date on guides.
Fixable: Partly. Re-host as Squarespace Blog Posts, which typically emit BlogPosting (unverified in this crawl), and add a visible date and author. Do **not** recommend HowTo for the wash guide.

**S-28 (Info). /faq has no FAQPage. Correct. Do not add.** Google retired FAQ rich results 2026-05-07. Existing: none.

**S-29 (Info). No HowTo anywhere. Do not add.**

### Open Graph / Twitter

**S-30 (Pass). `og:type` is `product` on 22 product pages with `product:price:amount`, `product:price:currency` EUR, `product:availability` instock.** For AggregateOffer products, price is the low price.

**S-31 (Pass). `og:title`, `og:description`, `og:url`, `og:site_name` present on 49/49. Meta description present on 42/49** (missing on 7 category pages, see E-01).

## E-commerce checks (HTML)

**E-01 (Medium). Seven `/shop/*` category pages have no H1 and no meta description.**
Evidence: `/shop`, `beanies--hats`, `cardigans`, `gift`, `sets`, `sweaters`, `vests`, `winter-wool-gifts`: `<h1>` count 0 on all 8 pages. `description` meta absent on 7 of them (all except `/shop`).
Fixable: Yes, Squarespace collection page settings (title, description).

**E-02 (Pass). Price visible on 22/22 PDPs; matches JSON-LD.** Gift card shows "from €25.00".

**E-03 (Info). Variant selectors present on 14 PDPs (Size radio S–XL, Primary colour swatches). 7 single-variant PDPs; gift card has amount selector.** Variant JSON is in page source (`"variants":[...]`).

**E-04 (Low). No stock text on PDP.** Only "Add To Cart". Stock quantities exist in page JSON (`"stock":{"unlimited":false,"quantity":4}`, `qtyInStock:16`) but not shown. All variant quantities in the crawl are >0. JSON-LD `availability` is InStock on 22/22 with no OutOfStock evidence. Sold-out display not verifiable from this crawl.
Fixable: Yes, Squarespace commerce settings (show stock / sold-out state). Sold-out JSON-LD behaviour unverified.

**E-05 (Pass). Size and fit info on PDP.** `Fit: Straight, relaxed. The model is 171 cm tall.` Size guide link on PDP (6 `href="/size-guide"`). Shipping/returns link present.

**E-06 (Pass). Related products block on PDPs.** `related-products-section` present, "You Might Also Like". 3 product links in block.

**E-07 (Low). PDP to category link missing from breadcrumb.** Breadcrumb is `/shop` > product. Products also sit in `/shop/cardigans`, `/shop/sweaters`, etc., with no category-level crumb.
Fixable: Platform limit.

**E-08 (Info). Gift card product present.** `/shop/p/autumn-and-wool-digital-gift-card`, linked from `/shop/gift` and `/wool-gifts`. "Gift Now" CTA. AggregateOffer 25–250 EUR. Digital gift card eligibility for Merchant Center not verified.

## Validation summary

- Parse: 169/169 JSON-LD blocks valid JSON.
- Product core (name, image, description, brand, offers price/currency/availability): PASS on 22/22.
- Product recommended (sku, url, gtin, shippingDetails, returns): FAIL on 22/22 or 15/22 (see S-01 to S-05).
- Organization: name/url/logo missing; telephone empty; address unstructured.
- LocalBusiness: image invalid; type questionable for online-only shop.
- No deprecated types, no HowTo, no FAQPage, no SpecialAnnouncement. Pass.

## Score

**Schema score: 55/100.** Rationale: valid JSON and core Product fields are present on all 22 products, and prices match visible prices. Merchant-listing properties are absent (shipping, return policy, product URL, SKU on 15, GTIN). Sitewide Organization has empty and unstructured fields, and LocalBusiness has an invalid image. No BreadcrumbList or ItemList.

## Could not verify

- Whether Squarespace emits `sku`, `url`, or `shippingDetails` from settings; the crawl only shows current output.
- Sold-out JSON-LD behaviour (no zero-stock variant in crawl).
- Whether Business Information fields feed Organization/LocalBusiness JSON-LD.
- Whether blog-post template emits BlogPosting.
- Actual og:image rendering in Facebook, Twitter, or Pinterest.
- Shipping destination list and whether digital gift cards are eligible in Merchant Center.
- Ownership and activity of legacy Mareshop social accounts.
- Live rendering (no live requests were made).
