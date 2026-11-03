# Merchant Center report: first sale push, 2026-11-02

Account 5687087698 (autumnandwool). Data window: Merchant Center "Last 28 days" view. The product table shows "Last updated Oct 21, 2026", so figures may lag about 12 days.

## 1. Numbers

| Metric | Value | Source |
|---|---|---|
| Products total | 99 | Overview / Products |
| Approved | 99 | Overview |
| Limited / Not approved / Under review | 0 / 0 / 0 | Overview |
| Online store clicks (organic, website) | 10 (+150%) | Analytics > Summary. This is the "Total clicks" card on Overview. It is NOT product clicks. |
| Product clicks on Google | 0 | Analytics > Summary, "Product clicks" |
| Product page impressions (on Google) | 52 | Analytics > Products header card |
| Product CTR | 0.0% | Analytics > Products header card |
| Ad campaigns | none (Shopping ads: "Setup required") | Marketing |
| Products with any impression | 20 of 99 (each under 20 impressions, 0 clicks) | Analytics > Products report |
| Products with zero impressions | 79 of 99 | Derived by matching Products list to Analytics report |
| Countries with impressions | 20 (Australia, Austria, Canada, Dominican Republic, Finland, France, Germany, Greece, India, Ireland, Italy, Malaysia, Netherlands, Other, Portugal, Slovakia, Spain, Switzerland, United Kingdom, United States). All show 0 clicks. | Analytics > Products > Countries |

Reading: Google showed the store about 2 times a day (52 impressions in 28 days) but nobody clicks a product. The 10 website clicks came from organic traffic, not from Shopping listings.

## 2. Changes made (before → after)

| # | Setting | Before | After |
|---|---|---|---|
| 1 | Overview card "Turn on automatic image improvements" (Automations > Image improvements) | Off ("Turn on now" card showing) | On (check mark shown on Automations > Product data optimizations > Image improvements). Clicked "Turn on now" on the card. No Terms dialog appeared. |
| 2 | Business info > Customer service contact (Overview card "Build trust with your customer service") | Website URL blank; Email info@autumnandwool.com (prefilled); Phone +371 29838090 (prefilled); live chat and chat-bot boxes unchecked | Website URL https://www.autumnandwool.com/contact; Email autumnandwool@gmail.com (the public address on /contact); Phone unchanged; live chat and chat-bot still unchecked. Saved. Business info now shows the new values. |

Verified not changed: Free listings marketing method stays ON (Marketing > Marketing methods). It is one switch. No separate YouTube, Google Images or Discover toggles exist in this UI, so there was nothing else to set.

Verified not changed: Shipping and returns. See section 4.

## 3. Skipped and why

| Item | Why |
|---|---|
| Overview card "Add checkout to your listings" | Setup needs a per-product checkout_link_template attribute in the data source. Entering a plain cart URL (https://www.autumnandwool.com/cart) in Business info > Checkout made Save disabled with "Missing required parameter: {id}". Fixing it means product-data edits (frozen). Edit cancelled; nothing saved. Owner decision needed. |
| Automations > Shipping not updated: "Turn on" | Google would rewrite each product's shipping info automatically. That is a product-data change, and product data is frozen. Needs owner OK first. |
| Overview card "Increase conversions by showing your promotions on Google" (Promotions add-on) | Not in the requested list. Add-on setup not done. |
| Shopping ads (Marketing > Set up) | Would start paid ads. Spending money is out of scope. Not touched. |
| Overview card "Update descriptions for Women's Sweaters" | Product data frozen. Missing-attribute list recorded in section 5 instead. |
| Customer service phone +371 29838090 | Prefilled in Merchant Center. Not found on any public page of autumnandwool.com (checked /, /contact, /imprint, /shipping-returns). Left as-is. Owner should confirm it is correct, or clear it. |
| Customer service live chat / chat bot boxes | No public evidence. Left unchecked. |
| Shipping policy timing | Merchant Center delivery times do not match the public shipping page. Owner decision. See section 4. |

## 4. Shipping and returns check

Returns policy: present. "Standard for Latvia", status Verified, 14 days, customer pays return shipping. Matches public page https://www.autumnandwool.com/shipping-returns ("within 14 days", "You cover return postage"). Covers 98 products. Gap: 1 product is not on this policy. Not identified; check Shipping and returns > Return policies.

Shipping policies: present. Latvia default: free, 4-10 days. Other policies: Austria/Belgium etc (Europe), Australia/Canada (US/CA/AU), Estonia (Latvia, Finland +17), UK/Norway (+1). All free. Mismatches with public page (not changed, owner decision):

| Region | Public page says | Merchant Center says |
|---|---|---|
| Latvia | dispatch from Riga in 2-5 working days (in stock); no separate Latvia delivery time published | 4-10 days delivery |
| Europe | 5-10 working days | 7-15 days |
| USA, Canada, Australia | 7-20 days | 9-25 days |

Policy names are messy: "Shipping Policy 2 11Europe free shipping", "Shipping Policy 0 19", "Estonia". Ship-from location is set.

## 5. Missing attributes for "Update descriptions for Women's Sweaters" (47 products)

Source: Products > Update product descriptions, category Women's Sweaters, 47 rows. The UI has two columns and does not define them (hover shows no tooltip). Both are reported verbatim.
- "Key details" column: Size 40, Material 43, Pattern 3.
- "Add to description" column: Pattern 44, Size 7, Material 4.

| Product | Key details (missing) | Add to description |
|---|---|---|
| Women’s Classic Lambswool Crew Sweater (S) | Size, Material | Pattern |
| Pure Wool Side-Slit Sweater — Camel (S) | Size, Material | Pattern |
| Pure Wool Stand-Collar Sweater — Beige (L) | Size, Material | Pattern |
| Pure Wool Side-Slit Sweater — Light Grey (S) | Size, Material | Pattern |
| Pure Wool Stand-Collar Sweater — Beige (XL) | Size, Material | Pattern |
| Merino Wool Raglan Cardigan (Blue) | Material | Size, Pattern |
| Lambswool Raglan Crew — Brown (M) | Size, Material | Pattern |
| Pure Wool Stand-Collar Sweater — Blue (S) | Size, Material | Pattern |
| Pure Wool Side-Slit Sweater — Light Grey (L) | Size, Material | Pattern |
| Oversized Wool Raglan Sweater — Beige Melange | Material | Size, Pattern |
| Women’s Classic Lambswool Crew Sweater (XL) | Size, Material | Pattern |
| Merino Striped Oversized Sweater — Women’s Jumper | Pattern, Material | Size |
| Oversized Merino Wool V-Neck Sweater Vest | Material | Size, Pattern |
| Lambswool Raglan Crew — Green (M) | Size, Material | Pattern |
| Pure Wool Side-Slit Sweater — Camel (XL) | Size, Material | Pattern |
| Long Wool Cardigan — Women’s Shawl Collar (S) | Size | Pattern, Material |
| Long Wool Cardigan — Women’s Shawl Collar (M) | Size | Pattern, Material |
| Pure Wool Side-Slit Sweater — Camel (M) | Size, Material | Pattern |
| Lambswool Raglan Crew — Green (XL) | Size, Material | Pattern |
| 100% Wool Long Shawl Cardigan – Warm Knit (L) | Size, Material | Pattern |
| Pure Wool Stand-Collar Sweater — Blue (M) | Size, Material | Pattern |
| Lambswool Raglan Crew — Brown (L) | Size, Material | Pattern |
| Lambswool Raglan Crew — Brown (XL) | Size, Material | Pattern |
| Women’s Classic Lambswool Crew Sweater (M) | Size, Material | Pattern |
| Open-Front Wool Cardigan — Women’s Side-Slit Knit | Size, Pattern, Material | - |
| Lambswool Raglan Crew — Green (L) | Size, Material | Pattern |
| Women’s Classic Lambswool Crew Sweater (L) | Size, Material | Pattern |
| Long Wool Cardigan — Women’s Shawl Collar (XL) | Size | Pattern, Material |
| 100% Wool Long Shawl Cardigan – Warm Knit (S) | Size, Material | Pattern |
| Oversized Merino Turtleneck — Dusty Pink Raglan | Material | Size, Pattern |
| Pure Wool Stand-Collar Sweater — Blue (L) | Size, Material | Pattern |
| 100% Wool Long Shawl Cardigan – Warm Knit (M) | Size, Material | Pattern |
| Long Wool Cardigan — Women’s Shawl Collar (L) | Size | Pattern, Material |
| Lambswool Raglan Crew — Brown (S) | Size, Material | Pattern |
| Merino Wool Raglan Cardigan (Brown) | Material | Size, Pattern |
| Pure Wool Side-Slit Sweater — Light Grey (M) | Size, Material | Pattern |
| 100% Wool Long Shawl Cardigan – Warm Knit (XL) | Size, Material | Pattern |
| Merino Wool Raglan Sweater — Dusty Pink Oversized Jumper (L/XL) | Size, Material | Pattern |
| Pure Wool Side-Slit Sweater — Light Grey (XL) | Size, Material | Pattern |
| Merino Wool Raglan Sweater — Dusty Pink Oversized Jumper (S/M) | Size, Material | Pattern |
| Pure Wool Stand-Collar Sweater — Blue (XL) | Size, Material | Pattern |
| Merino Wool Raglan Cardigan (Black) | Material | Size, Pattern |
| Lambswool Raglan Crew — Green (S) | Size, Material | Pattern |
| Pure Wool Stand-Collar Sweater — Beige (S) | Size, Material | Pattern |
| Distressed Wool Raglan Sweater — Oversized | Size, Pattern, Material | - |
| Pure Wool Stand-Collar Sweater — Beige (M) | Size, Material | Pattern |
| Pure Wool Side-Slit Sweater — Camel (L) | Size, Material | Pattern |

## 6. Per-product performance (Last 28 days)

Products with impressions (20). Impressions are shown as "<20" per product. Clicks are 0 for all 20.

| ID | Title | Price | Impr. | Clicks | CTR |
|---|---|---|---|---|---|
| SQ9956956 | Merino Wool Raglan Sweater — Dusty Pink Oversized Jumper (S/M) | €155.00 | <20 | 0 | 0.0% |
| SQ9790760 | Merino Turtleneck — Women’s Lightweight Knit (Melange Taupe, XS) | €110.00 | <20 | 0 | 0.0% |
| SQ9379546 | Merino Wool Hat & Scarf Set (Black) | €110.00 | <20 | 0 | 0.0% |
| SQ9326369 | Oversized Wool Raglan Sweater — Beige Melange | €155.00 | <20 | 0 | 0.0% |
| SQ8708276 | Merino Turtleneck — Women’s Lightweight Knit (Melange Beige, S) | €110.00 | <20 | 0 | 0.0% |
| SQ8666979 | Pure Wool Stand-Collar Sweater — Blue (L) | €136.00 | <20 | 0 | 0.0% |
| SQ8362078 | Long Wool Cardigan — Women’s Shawl Collar (L) | €145.00 | <20 | 0 | 0.0% |
| SQ7476378 | Merino Wool Hat & Scarf Set (Brown) | €110.00 | <20 | 0 | 0.0% |
| SQ7145776 | 100% Wool Long Shawl Cardigan – Warm Knit (S) | €145.00 | <20 | 0 | 0.0% |
| SQ7004700 | Oversized Wool V-Neck Vest - Beige Melange | €126.00 | <20 | 0 | 0.0% |
| SQ6945548 | Merino Wool Raglan Sweater — Dusty Pink Oversized Jumper (L/XL) | €155.00 | <20 | 0 | 0.0% |
| SQ4155762 | Merino Turtleneck — Women’s Lightweight Knit (Royal Blue, M) | €110.00 | <20 | 0 | 0.0% |
| SQ3898906 | Pure Wool Stand-Collar Sweater — Beige (XL) | €136.00 | <20 | 0 | 0.0% |
| SQ3776585 | Open-Front Wool Cardigan — Women’s Side-Slit Knit | €155.00 | <20 | 0 | 0.0% |
| SQ3600486 | Oversized Merino Turtleneck — Dusty Pink Raglan | €155.00 | <20 | 0 | 0.0% |
| SQ3433178 | Merino Turtleneck — Women’s Lightweight Knit (Melange Grey, XS) | €110.00 | <20 | 0 | 0.0% |
| SQ2914675 | Merino Turtleneck — Women’s Lightweight Knit (Melange Beige, XS) | €110.00 | <20 | 0 | 0.0% |
| SQ2239941 | Merino Wool Hat & Scarf Set (Gray) | €110.00 | <20 | 0 | 0.0% |
| SQ2037965 | 100% Wool Long Shawl Cardigan – Warm Knit (XL) | €145.00 | <20 | 0 | 0.0% |
| SQ1599152 | Rib-Knit Merino Beanie — Unisex (Melange grey) | €45.00 | <20 | 0 | 0.0% |

Products with zero impressions and zero clicks (79):

| ID | Title | Price | Impr. | Clicks | CTR |
|---|---|---|---|---|---|
| 6137320240575994227 | Digital Gift Card for Wool Knitwear | Autumn & Wool | €25.00 | 0 | 0 | 0.0% |
| SQ9891810 | Rib-Knit Merino Beanie — Unisex (Light grey) | €45.00 | 0 | 0 | 0.0% |
| SQ9502706 | Merino Striped Oversized Sweater — Women’s Jumper | €165.00 | 0 | 0 | 0.0% |
| SQ9486312 | Merino Turtleneck — Women’s Lightweight Knit (Dusty Rose, M) | €110.00 | 0 | 0 | 0.0% |
| SQ9265885 | Lambswool Raglan Crew — Brown (M) | €136.00 | 0 | 0 | 0.0% |
| SQ9088173 | Merino Wool Raglan Cardigan (Black) | €160.00 | 0 | 0 | 0.0% |
| SQ9044699 | Merino Turtleneck — Women’s Lightweight Knit (Rose Pink, XS) | €110.00 | 0 | 0 | 0.0% |
| SQ9035687 | Merino Turtleneck — Women’s Lightweight Knit (Classic Grey, XS) | €110.00 | 0 | 0 | 0.0% |
| SQ8973335 | Women’s Classic Lambswool Crew Sweater (S) | €136.00 | 0 | 0 | 0.0% |
| SQ8867279 | Pure Wool Stand-Collar Sweater — Blue (S) | €136.00 | 0 | 0 | 0.0% |
| SQ8772441 | Pure Wool Side-Slit Sweater — Light Grey (M) | €136.00 | 0 | 0 | 0.0% |
| SQ8421560 | Merino Turtleneck — Women’s Lightweight Knit (Melange Brown, S) | €110.00 | 0 | 0 | 0.0% |
| SQ8241965 | Long Wool Cardigan — Women’s Shawl Collar (XL) | €145.00 | 0 | 0 | 0.0% |
| SQ8111036 | Merino Turtleneck — Women’s Lightweight Knit (Melange Beige, M) | €110.00 | 0 | 0 | 0.0% |
| SQ8096733 | Merino Turtleneck — Women’s Lightweight Knit (Dusty Rose, XS) | €110.00 | 0 | 0 | 0.0% |
| SQ8005265 | Merino Turtleneck — Women’s Lightweight Knit (Melange Brown, XS) | €110.00 | 0 | 0 | 0.0% |
| SQ7867996 | Lambswool Raglan Crew — Brown (XL) | €136.00 | 0 | 0 | 0.0% |
| SQ7845957 | 100% Wool Long Shawl Cardigan – Warm Knit (L) | €145.00 | 0 | 0 | 0.0% |
| SQ7776260 | 100% Wool Long Shawl Cardigan – Warm Knit (M) | €145.00 | 0 | 0 | 0.0% |
| SQ7638948 | Merino Turtleneck — Women’s Lightweight Knit (Melange Taupe, S) | €110.00 | 0 | 0 | 0.0% |
| SQ7601591 | Merino Wool Raglan Cardigan (Brown) | €160.00 | 0 | 0 | 0.0% |
| SQ7358699 | Merino Turtleneck — Women’s Lightweight Knit (Rose Pink, S) | €110.00 | 0 | 0 | 0.0% |
| SQ6830651 | Rib-Knit Merino Beanie — Unisex (Navy) | €45.00 | 0 | 0 | 0.0% |
| SQ6735209 | Rib-Knit Merino Beanie — Unisex (Brown) | €45.00 | 0 | 0 | 0.0% |
| SQ6566202 | Pure Wool Stand-Collar Sweater — Blue (XL) | €136.00 | 0 | 0 | 0.0% |
| SQ6470056 | Merino Turtleneck — Women’s Lightweight Knit (Classic Grey, S) | €110.00 | 0 | 0 | 0.0% |
| SQ6384123 | Merino Turtleneck — Women’s Lightweight Knit (Berry Purple, XS) | €110.00 | 0 | 0 | 0.0% |
| SQ6240622 | Rib-Knit Merino Beanie — Unisex (Beige) | €45.00 | 0 | 0 | 0.0% |
| SQ6061536 | Lambswool Raglan Crew — Brown (S) | €136.00 | 0 | 0 | 0.0% |
| SQ5989399 | Merino Turtleneck — Women’s Lightweight Knit (Royal Blue, XS) | €110.00 | 0 | 0 | 0.0% |
| SQ5958509 | Merino Turtleneck — Women’s Lightweight Knit (Chestnut Brown, XS) | €110.00 | 0 | 0 | 0.0% |
| SQ5891265 | Lambswool Raglan Crew — Green (L) | €136.00 | 0 | 0 | 0.0% |
| SQ5869324 | Merino Turtleneck — Women’s Lightweight Knit (Purple Brown, XS) | €110.00 | 0 | 0 | 0.0% |
| SQ5766994 | Rib-Knit Merino Beanie — Unisex (Blue) | €45.00 | 0 | 0 | 0.0% |
| SQ5713917 | Women’s Classic Lambswool Crew Sweater (L) | €136.00 | 0 | 0 | 0.0% |
| SQ5710264 | Pure Wool Side-Slit Sweater — Light Grey (L) | €136.00 | 0 | 0 | 0.0% |
| SQ5350409 | Merino Turtleneck — Women’s Lightweight Knit (Melange Grey, M) | €110.00 | 0 | 0 | 0.0% |
| SQ5327787 | Pure Wool Side-Slit Sweater — Light Grey (XL) | €136.00 | 0 | 0 | 0.0% |
| SQ5264360 | Merino Turtleneck — Women’s Lightweight Knit (Dusty Rose, S) | €110.00 | 0 | 0 | 0.0% |
| SQ5142555 | Long Wool Cardigan — Women’s Shawl Collar (S) | €145.00 | 0 | 0 | 0.0% |
| SQ4975266 | Pure Wool Side-Slit Sweater — Camel (XL) | €136.00 | 0 | 0 | 0.0% |
| SQ4863473 | Pure Wool Stand-Collar Sweater — Beige (S) | €136.00 | 0 | 0 | 0.0% |
| SQ4784604 | Merino Turtleneck — Women’s Lightweight Knit (Purple Brown, M) | €110.00 | 0 | 0 | 0.0% |
| SQ4628527 | Women’s Classic Lambswool Crew Sweater (M) | €136.00 | 0 | 0 | 0.0% |
| SQ4599687 | Merino Turtleneck — Women’s Lightweight Knit (Berry Purple, M) | €110.00 | 0 | 0 | 0.0% |
| SQ4591024 | Pure Wool Stand-Collar Sweater — Beige (M) | €136.00 | 0 | 0 | 0.0% |
| SQ4565277 | Pure Wool Side-Slit Sweater — Camel (S) | €136.00 | 0 | 0 | 0.0% |
| SQ4483570 | Merino Turtleneck — Women’s Lightweight Knit (Melange Grey, S) | €110.00 | 0 | 0 | 0.0% |
| SQ3934346 | Pure Wool Side-Slit Sweater — Camel (L) | €136.00 | 0 | 0 | 0.0% |
| SQ3869977 | Women’s Classic Lambswool Crew Sweater (XL) | €136.00 | 0 | 0 | 0.0% |
| SQ3845006 | Rib-Knit Merino Beanie — Unisex (Bordeaux) | €45.00 | 0 | 0 | 0.0% |
| SQ3807672 | Distressed Wool Raglan Sweater — Oversized | €155.00 | 0 | 0 | 0.0% |
| SQ3434719 | Pure Wool Stand-Collar Sweater — Blue (M) | €136.00 | 0 | 0 | 0.0% |
| SQ3314835 | Rib-Knit Merino Beanie — Unisex (Pink) | €45.00 | 0 | 0 | 0.0% |
| SQ2898392 | Merino Turtleneck — Women’s Lightweight Knit (Rose Pink, M) | €110.00 | 0 | 0 | 0.0% |
| SQ2462373 | Lambswool Raglan Crew — Green (M) | €136.00 | 0 | 0 | 0.0% |
| SQ2323221 | Lambswool Raglan Crew — Green (XL) | €136.00 | 0 | 0 | 0.0% |
| SQ2272298 | Merino Turtleneck — Women’s Lightweight Knit (Sky Blue, M) | €110.00 | 0 | 0 | 0.0% |
| SQ2134916 | Merino Turtleneck — Women’s Lightweight Knit (Melange Brown, M) | €110.00 | 0 | 0 | 0.0% |
| SQ2122502 | Rib-Knit Merino Beanie — Unisex (Camel) | €45.00 | 0 | 0 | 0.0% |
| SQ2078364 | Oversized Merino Wool V-Neck Sweater Vest | €126.00 | 0 | 0 | 0.0% |
| SQ1988154 | Merino Wool Raglan Cardigan (Blue) | €160.00 | 0 | 0 | 0.0% |
| SQ1919240 | Merino Turtleneck — Women’s Lightweight Knit (Royal Blue, S) | €110.00 | 0 | 0 | 0.0% |
| SQ1844551 | Pure Wool Stand-Collar Sweater — Beige (L) | €136.00 | 0 | 0 | 0.0% |
| SQ1652750 | Merino Turtleneck — Women’s Lightweight Knit (Sky Blue, S) | €110.00 | 0 | 0 | 0.0% |
| SQ1526199 | Merino Turtleneck — Women’s Lightweight Knit (Sky Blue, XS) | €110.00 | 0 | 0 | 0.0% |
| SQ1481398 | Merino Turtleneck — Women’s Lightweight Knit (Chestnut Brown, S) | €110.00 | 0 | 0 | 0.0% |
| SQ1480313 | Merino Turtleneck — Women’s Lightweight Knit (Berry Purple, S) | €110.00 | 0 | 0 | 0.0% |
| SQ1398008 | Rib-Knit Merino Beanie — Unisex (Gray) | €45.00 | 0 | 0 | 0.0% |
| SQ1183187 | Lambswool Raglan Crew — Green (S) | €136.00 | 0 | 0 | 0.0% |
| SQ0851295 | Lambswool Raglan Crew — Brown (L) | €136.00 | 0 | 0 | 0.0% |
| SQ0850514 | Pure Wool Side-Slit Sweater — Camel (M) | €136.00 | 0 | 0 | 0.0% |
| SQ0831840 | Merino Turtleneck — Women’s Lightweight Knit (Melange Taupe, M) | €110.00 | 0 | 0 | 0.0% |
| SQ0742548 | Long Wool Cardigan — Women’s Shawl Collar (M) | €145.00 | 0 | 0 | 0.0% |
| SQ0554332 | Pure Wool Side-Slit Sweater — Light Grey (S) | €136.00 | 0 | 0 | 0.0% |
| SQ0376525 | Merino Turtleneck — Women’s Lightweight Knit (Classic Grey, M) | €110.00 | 0 | 0 | 0.0% |
| SQ0199503 | Merino Turtleneck — Women’s Lightweight Knit (Chestnut Brown, M) | €110.00 | 0 | 0 | 0.0% |
| SQ0189633 | Rib-Knit Merino Beanie — Unisex (Black) | €45.00 | 0 | 0 | 0.0% |
| SQ0111040 | Merino Turtleneck — Women’s Lightweight Knit (Purple Brown, S) | €110.00 | 0 | 0 | 0.0% |

All 99 products: "Click potential" = Low for every product. Availability = In stock for every product. Data sources: autumnandwool-google-feed.tsv (98 products) and www.autumnandwool.com (1 product, the digital gift card).

## 7. Notes for owner

1. Product clicks are 0 across the whole catalogue. The fix is not in Merchant Center settings. Likely causes: few impressions, and product data quality (see section 5). Both are owner-gated.
2. Decide on the checkout link (needs per-product template in the feed) and on Shipping updates automation.
3. Confirm the phone number in Customer service.
4. Align shipping delivery times with the public shipping page.
