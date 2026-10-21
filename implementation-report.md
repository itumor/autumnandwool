# Autumn & Wool — Implementation Report

Checked: 18 October 2026. Live storefront: https://www.autumnandwool.com/

## Verified work and prior changes

| Item | Status | Evidence |
|---|---|---|
| Checkout path | Partial; desktop failed on recheck | Prior mobile run reached Stripe/Link for all four products in Latvia; no order. Current desktop beanie click produced a blank page; separate cart check found and removed the QA item. No payment submitted. See checkout matrix and follow-up. |
| Priority product copy | Published and verified | Public beanie, hat/scarf set, vest and cardigan pages now show shorter product-specific design, fit/measurement, care and contact details. Set and vest cross-recommend related accessories and clothing. Legacy URLs remain. |
| SEO metadata | Published and verified | Home title now “Wool Cardigans, Sweaters & Accessories | Autumn & Wool”; public page title confirmed after reload. Global description, Shop title/description, About title/description, and hat/scarf set and vest metadata saved. |
| Homepage sales copy | Published and rechecked | Live hero now says “Wool Knitwear for Cooler Days,” uses a real V-neck vest photo, has Shop and Size Guide buttons, and links three featured products: the vest, hat/scarf set and long cardigan. The beanie remains in the next section. Replaced the unsupported “high-quality manufacturing and design” heading with a factual brand introduction. |
| Shop labels | Checked | Shop categories already include All, Gift, Vests, Sweaters, Cardigans, Beanies and Sets. No-results message did not show without a filter. |
| Duplicates | Investigated | Repeated sweater, crew and vest names appear as separate listings. Left them intact because product identity/variant history is not confirmed. |
| Traffic baseline | Rechecked | Current Last 30 Days (19 Sep–18 Oct 2026): 64 visits, 64 unique visitors, 61 pageviews, 95.95% bounce; Direct 61, Google 2, Facebook 1. Earlier overlapping 62-visit baseline remains documented below. |
| Orders | Checked | Squarespace Orders shows “No orders yet.” Completed orders: 0. Commerce dashboard shows no revenue/AOV data. |
| About page | Published and verified | Fresh public page shows “Our Story,” factual Riga-based brand copy, and an Explore Our Collection button linked to /shop. |
| Catalog copy cleanup | Partial; public audit incomplete | First Squarespace CSV import updated 82 products; stock updates were unchecked. Public sweater check then found unsupported production/sustainability claims and malformed text. Second cleanup import updated 81 rows; one row failed with “Missing column: Add PRODUCT ID column.” A fresh public page still showed stale FAQ/care fragments, so the final cleanup is not verified. No more product data edits after the user asked to leave product data unchanged. Audit still needs supplier evidence; shipping/returns and legacy URLs retain claims. |

## Checkout matrix — mobile viewport (390×844)

| Product | Variant selected | Cart result | Shipping | Payment readiness | Result |
|---|---|---|---|---|---|
| Rib-Knit Beanie — €45 | Black default | Subtotal €45 | Latvia: free shipping shown | Secure payment UI loaded | Pass through payment screen; no order |
| Merino Wool Hat & Scarf Set — €110 | Black default | Subtotal €110 | Latvia: free shipping shown | Secure payment UI loaded | Pass through payment screen; no order |
| Oversized Merino Wool V-Neck Sweater Vest — €126 | No selector shown | Subtotal €126 | Latvia: free shipping shown | Secure payment UI loaded | Pass through payment screen; no order |
| Long Wool Cardigan — €145 | Size M selected | Subtotal €145 | Latvia: free shipping shown | Secure payment UI loaded | Pass through payment screen; no order |

All four products were added to one mobile QA cart (combined subtotal €426), then shipping details were entered for Latvia. Payment UI loaded. No other destination, payment submission or completed order was tested. All four QA products were removed; cart shows empty.

## SEO fields saved

- Site description: “Discover wool cardigans, sweaters, beanies and scarves from Autumn & Wool, based in Riga, Latvia. Explore the collection, fit details and care tips.”
- Home title: “Wool Cardigans, Sweaters & Accessories | Autumn & Wool”
- Shop title: “Shop Wool Knitwear & Accessories | Autumn & Wool”
- Shop description: “Shop wool cardigans, sweaters, sweater vests, beanies and scarves at Autumn & Wool. Browse the collection and explore sizes, materials and care details.”
- About title: “Our Story | Autumn & Wool Knitwear”
- About description: “Discover Autumn & Wool, a Riga-based knitwear brand inspired by a family connection to knitting, relaxed silhouettes and everyday style.”

## Blocked or incomplete

| Work | Status | Why / next action |
|---|---|---|
| Full purchase journey | Partly tested | Mobile path reached Stripe/Link after shipping on Latvia; no payment/order submitted, no other country tested. |
| Homepage structure | Partly improved | Hero, CTA, size-guide link and factual brand copy are live. Vest, set and cardigan appear in first product group; beanie appears later. Four-card grouping and direct Winter Wool Gifts homepage CTA remain incomplete. |
| Product-page priorities | Partly complete | Beanie, hat/scarf set, vest and cardigan copy updated and publicly checked. Set and vest have individual SEO metadata. Other product SEO, image quality and supplier evidence need review. |
| Catalog claim audit | Incomplete; product data now frozen | CSV imports changed product titles, descriptions and tags. The first import removed some unsupported claims, but a fresh public check still showed stale product FAQ/care fragments and old page-title/image-alt wording. A second cleanup CSV was generated and imported; one row failed, and a fresh public check did not show the corrected description. Do not edit product titles, descriptions, tags, prices, variants or stock further without new user approval. Product URLs were preserved. Shipping & Returns still says products are handmade/hand-finished and uses “sustainable fashion”; it also promises free shipping for the US and other destinations. Only Latvia was checkout-tested. Supplier evidence and qualified legal review are still needed. |
| Winter gifts collection | Created and live | Native “Winter Wool Gifts” category contains gift card, vest, hat/scarf set and beanie. Public category page: https://www.autumnandwool.com/shop/winter-wool-gifts. Homepage does not yet link directly to it. |
| Related products | Configured and live | Set and vest cross-recommend related accessories and clothing; public pages show “You might also like.” |
| Search Console connector | Mismatched property | The connected reporting tool exposes a different Squarespace property (`https://rhino-reindeer-zp9j.squarespace.com/`). Use the verified Autumn & Wool property in the browser; do not rely on this connector until its account is corrected. |
| Search Console | Existing Autumn & Wool property verified | Signed into the requested store profile. Overview shows 11 web search clicks, 11 indexed pages and 4 not indexed; visible period for the 11 clicks was not clear. One valid product snippet and one valid merchant listing. Full reports were loading. The reporting connector remains linked to another property. |
| Merchant Center | Existing Autumn & Wool account; feed needs work | Account has 2 auto-discovered products, 0 supplied products, both not approved, 0 clicks. Issue details: missing shipping information and pending initial review; last updated 6 Oct 2026. Only US listings surfaced. No ad campaign enabled. |
| GA4 | Connected; ecommerce events unverified | Squarespace External API Keys contains measurement ID `G-7TV8PK060Z`. The matching GA4 property stream is `https://www.autumnandwool.com/`, and GA4 reports active traffic in the past 48 hours. Recent events show `page_view`, `session_start`, `first_visit`, `user_engagement`, `scroll`, and `click`; no ecommerce events are listed. `purchase` is marked as a key event but has no stream data. No order exists to test the purchase event. No settings changed. |
| Newsletter / welcome automation | Copy drafted; configuration unverified | Footer signup exists. Consent destination, double opt-in, unsubscribe handling, and sender settings remain unverified. Welcome email draft: [welcome-email-draft.md](/Users/eramadan/autumnandwool/campaign-assets/welcome-email-draft.md). No welcome automation activated and no email sent. |
| Social posts | Six local drafts saved; platform drafts not created | Six captions, destination URLs, UTMs, and unaltered product photos are in [campaign-drafts.md](/Users/eramadan/autumnandwool/campaign-assets/campaign-drafts.md) with images under `campaign-assets/drafts/`. Public Instagram account mismatch remains; no posts published or scheduled. |
| Measurement | Snapshot saved; tracking gaps remain | See [weekly-measurement-report-2026-10-17.md](weekly-measurement-report-2026-10-17.md). Squarespace Sales/Purchase Funnel contains unrelated sample items and implausible event counts; those data are excluded. |
| Screenshots / evidence | Partial | Existing desktop/mobile homepage previews, live-page captures, and [empty-cart proof](/Users/eramadan/autumnandwool/evidence/cart-empty-2026-10-18.jpg) are saved under `evidence/`. Checkout and multiple mobile link checks remain incomplete. |

## Six organic campaign drafts

Use authentic existing product photographs. Add UTM parameters below. These are drafts only; confirm each social account belongs to Autumn & Wool before posting.

1. **Pinterest — Beanie**  
   Title: Rib-Knit Wool Beanie for Cooler Days  
   Copy: Looking for a simple winter accessory? Explore the rib-knit beanie from Autumn & Wool, including available colours, fit details and care information.  
   URL: https://www.autumnandwool.com/shop/p/p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1?utm_source=pinterest&utm_medium=organic_social&utm_campaign=winter_knitwear&utm_content=beanie
2. **Pinterest — Hat and scarf**  
   Title: Wool Hat and Scarf Set for Cooler Days  
   Copy: A coordinated hat-and-scarf set for cooler days. Discover the design, available colours and details at Autumn & Wool.  
   URL: https://www.autumnandwool.com/shop/p/p/merino-wool-hat-scarf-set-extra-fine-rib-knit-soft-on-skin-warm-not-bulky-unisex-gift?utm_source=pinterest&utm_medium=organic_social&utm_campaign=winter_knitwear&utm_content=hat_scarf
3. **Pinterest — Vest**  
   Title: Relaxed V-Neck Sweater Vest  
   Copy: A relaxed sweater vest for everyday layering. Explore outfit possibilities, garment measurements and the Autumn & Wool collection.  
   URL: https://www.autumnandwool.com/shop/p/oversized-merino-wool-v-neck-sweater-vest?utm_source=pinterest&utm_medium=organic_social&utm_campaign=winter_knitwear&utm_content=vest
4. **Instagram — Seasonal layers**  
   Cool days call for comfortable layers. Explore wool knitwear and accessories in simple, wearable designs. See the collection through the link in our profile.  
   #AutumnAndWool #WoolKnitwear #KnitwearStyle #SlowStyle
5. **Instagram — Accessories**  
   A little warmth for the season ahead. Explore our rib-knit beanie and coordinated hat-and-scarf set, with details on colours, fit and care on each product page. See the collection through the link in our profile.  
   #WinterAccessories #Knitwear #AutumnAndWool
6. **Instagram — Easy layers**  
   Easy layers for cooler days. Explore sweater vests and long cardigans, and find measurements and care details on each product page. Discover Autumn & Wool through the link in our profile.  
   #WoolCardigan #SweaterVest #KnitwearStyle #AutumnAndWool

## Return-policy review — proposal only, not legal advice

The live terms need a qualified Latvian/EU legal review before publication. EU and Latvian consumer guidance says online consumers generally have 14 days from delivery to withdraw; refunds include standard delivery charges, while consumers may pay return postage if informed before purchase. The personalized-goods exception is narrow; an ordinary standard product made after an order is not automatically custom. A sale price alone does not remove withdrawal rights. See [Latvia PTAC: right of withdrawal](https://www.ptac.gov.lv/en/right-withdrawal), [Latvia PTAC: electronic purchases](https://www.ptac.gov.lv/en/purchases-electronic-means), and [EU Your Europe: returns](https://europa.eu/youreurope/citizens/consumers/shopping/returns/index_en.htm).

Proposed redline direction: remove blanket exclusions for discounted items and made-to-order items; state the statutory exception only for goods made to the consumer’s specifications or clearly personalized; clarify that refunds include standard outbound delivery where applicable; specify return-postage responsibility only if disclosed before purchase; replace short defect-reporting cutoff with wording that preserves statutory remedies. Do not publish before legal review.

## Next three actions

1. Resolve the Squarespace blank editor and checkout/payment frame; then recheck mobile and desktop purchase steps without submitting an order.
2. Confirm actual delivery-time ranges, social-account ownership, newsletter consent settings, and obtain Latvian legal review for the return-policy redline.
3. After those blockers clear, finish the homepage gift CTA and verify ecommerce events; keep product data unchanged.

## Revalidation — 18 October 2026

**Product-data freeze honored:** this pass changed no product title, description, metadata, category, tag, price, variant, stock, SKU, ID, or URL. Product pages and records remain untouched.

### Done and verified this pass

| Item | Evidence / result |
|---|---|
| Desktop checkout journey | Long Wool Cardigan, size M, €145. Added to cart; synthetic `qa@example.com` checkout progressed through Latvia shipping and displayed the payment step. Free shipping option shown; €145 total. Stopped before payment. Removed item; public cart confirmed empty. No order placed. |
| Shop browse state | Fresh public `/shop` showed categories All, Winter Wool Gifts, Gift, Vests, Sweaters, Cardigans, Beanies, Sets and product links. “No results found” was not visible without a filter. |
| Search Console property | Store Google profile can access URL-prefix property `https://www.autumnandwool.com/`. The domain property `sc-domain:autumnandwool.com` is not accessible in that profile. Last 3 months (15 Jul–14 Oct): 11 clicks, 372 impressions, 3% CTR, average position 14.2. Top queries include “timeless knitwear” (1 click / 19 impressions) and “oversized merino wool sweater” (1 / 4). |
| Indexing | Last updated 12 Oct: 11 indexed, 4 not indexed. Reasons: 3 “Crawled – currently not indexed” and 1 “Alternate page with proper canonical tag.” The three examples include two old product URLs and `/shop/vests`. No 404s shown. No URL changes made. |
| Merchant Center | Store account 5687087698 has 2 auto-found products, 0 supplied products, 0 approved, 2 not approved, 0 clicks. Exact blocker: missing shipping information for both products. Merchant Center has no shipping policy. Squarespace shipping settings currently offer free shipping for Latvia, the US, and Rest of world; delivery-time ranges were not present in the inspected settings, so no Merchant Center policy was invented. No ads enabled. |
| Duplicate investigation | Read-only export comparison: Side-Slit sweaters have separate product IDs, SKUs, URLs and image sets; Raglan Crew listings also have separate IDs, SKUs, URLs and image sets. Beige Melange vest listings share SKU `SQ7004700` but have separate product IDs, URLs and image sets. No listing was edited, merged, deleted or redirected. |
| About page | Fresh public page shows the Riga-based factual story and `/shop` CTA. Decorative “Every stitch tells a story of patience and purpose” remains. |

### Still open

| Task | Status / reason |
|---|---|
| Homepage exact four-product layout and Winter Wool Gifts CTA | Not done. Public homepage still shows vest, set and cardigan first; beanie appears after the brand intro. Editor preview is blank, blocking page edits. |
| Shop introduction copy | Not verified/changed. Public page has category navigation and product listings; editor preview blank. |
| Site-wide product claims audit | Not complete. Product fields are frozen at the owner’s instruction. Public Shipping & Returns still includes “handmade or hand-finished,” “handmade,” and “sustainable fashion.” No product data changed. |
| Shipping & Returns legal review | Not published. Existing clauses about refunds, sale/custom items and defect reporting need qualified review. The editor preview is blank. |
| Product-page copy or metadata revisions | Not done in this pass to honor the product-data freeze. Earlier report records the prior imports and their incomplete public verification. |
| Merchant Center feed approval | Blocked by missing shipping info. Current shipping settings show free shipping across three regions but not delivery times; no accurate Merchant policy can be completed without verified delivery ranges. |
| Newsletter consent and welcome automation | Not verified. Campaigns admin content is unavailable; the Automations page works. No signup was submitted, no welcome flow was activated, and no email was sent. |
| Abandoned-checkout recovery | Live and verified. Squarespace confirms “Recover abandoned carts” is Live: sends one reminder after 1 day if no order, with an unsubscribe link. |
| Analytics purchase events | Not verified. Current evidence still supports traffic only; no reliable purchase funnel/purchase-event setup confirmed. No tracking code or account permission changed. |
| Instagram/Pinterest assets | Existing report contains six text drafts and tracked product links. No external drafts were saved or posts published; account ownership differs between header and footer. |
| Mobile re-test | Earlier mobile check passed through payment UI for four products, Latvia only. This pass added a desktop check; no mobile test was repeated. |

### Current conversion diagnosis

The shop has low qualified organic visibility: 372 Search Console impressions and 11 clicks for 15 July–14 October 2026, average position 14.2. Squarespace currently shows 64 visits, 95.95% bounce, and 0 orders for 19 September–18 October; Direct 61, Google 2, Facebook 1. This is too little traffic to isolate one conversion cause. GA4 is connected but has no listed ecommerce events. The homepage still separates the €45 beanie from the first featured-product group.

### Admin limitation

Fresh `/config/pages` editor check on 18 Oct shows the page list and toolbar, but page previews remain `about:blank`; clicking Edit did not load the editor. A fresh public request to `/redesign-preview` returns the site’s 404 page. The Campaigns admin route renders no usable content, while the Automations route works. No page content was saved or published in this pass.

### Revalidation — Analytics and orders, 18 October 2026

| Metric | Result | Source |
|---|---:|---|
| Visits | 64 | Squarespace Analytics → Traffic, Sep 19–Oct 18 |
| Unique visitors | 64 | Squarespace Analytics → Traffic, Sep 19–Oct 18 |
| Pageviews | 61 | Squarespace Analytics → Traffic, Sep 19–Oct 18 |
| Bounce rate | 95.95% | Squarespace Analytics → Traffic, Sep 19–Oct 18 |
| Orders | 0 | Products & Services → Orders: “No orders yet” |
| Cart/checkout/purchase events | Not verified | Funnel showed no values in its accessible view |
| Sales by product | Unreliable / mismatched | It listed unrelated furniture products despite the verified Autumn & Wool knitwear catalog. Excluded from sales reporting. |

The actual Orders page is the source of truth here: it confirms zero orders. The Analytics sales panel conflicts with the store catalog, so its listed revenue and units sold were not attributed to Autumn & Wool. The Sales screen also labels this as a premium feature. Report this mismatch to Squarespace support before using those metrics.

**Product-data freeze:** no product record or field was edited in this pass. No checkout payment or order was submitted.

## Live-site audit — 18 October 2026

### Homepage and Shop

Fresh public rendering verified at `https://www.autumnandwool.com/` and `/shop`.

- Homepage hero is factual and has “Explore the Collection” and “Find Your Size” links.
- Three product cards appear before the brand introduction: vest €126, hat/scarf set €110, cardigan €145. Beanie €45 appears after the story. Exact four-product group is not live.
- No final shopping CTA appears before the footer. Newsletter signup is in the footer; consent destination and processing remain unverified.
- Header/social destinations conflict with footer: Instagram `@autumnandwool` vs `@mare.knitwear`; Facebook and Pinterest point to `AccessoriesMareshop` / `mmareshop`.
- Shop has 23 visible product links and categories All, Winter Wool Gifts, Gift, Vests, Sweaters, Cardigans, Beanies, Sets. No Shop introduction is visible. “No results found” is absent from the unfiltered live page and DOM snapshot.
- Repeated visible product names remain: Pure Wool Side-Slit Sweater, Lambswool Raglan Crew, and Oversized Wool V-Neck Vest — Beige Melange. Prior read-only export showed distinct IDs/URLs for the repeated entries; no merge, rename, delete, or redirect was made.

### Claims audit — read-only

Checked the live homepage, Shop, About, FAQ, Size Guide, Shipping & Returns, Contact, Privacy Policy, and all 23 product URLs linked from Shop. Search covered the requested sustainability/certification/production claims in visible copy, page title, SEO description, and product-image alt text. Supplier proof was not available.

Residual public claims / stale metadata:

- **Gift Card:** SEO description calls it a gift for “sustainable knitwear lovers.”
- **Black Merino Wool Raglan Cardigan:** product-image alt text still says “Sustainable Handmade Women’s Cardigan.”
- **Long cardigan listing:** page title metadata still includes “Handmade.”
- **Dusty Pink Merino Raglan Sweater:** SEO title and image alt say “Hand-Knitted”; SEO description says “Handcrafted with natural warmth and breathability.”
- **FAQ:** says handmade or made-to-order knitwear may need up to five business days before dispatch; asks whether products are sustainable, then directs shoppers to item-specific material/production details.
- **Shipping & Returns:** says every item is handmade or hand-finished, repeats handmade variation wording, excludes shipping costs from refunds, excludes all made-to-order and discounted goods from returns, sets a five-day defect-reporting window, and ends with “handmade, sustainable fashion.”
- **Privacy Policy:** describes the business as making “sustainable garments from 100% natural yarns.”
- About page and homepage body did not return these flagged terms in this scan. Material percentages and supplier claims remain unverified.

No product titles, descriptions, metadata, tags, categories, prices, images, variants, stock, SKUs, IDs, or URLs were changed. The account owner’s product-data freeze blocks edits to the flagged product metadata and image alt text. Non-product page edits also remain blocked: Squarespace’s page editor shows `sqs-site-frame` as `about:blank`; the product list remains on “Loading.” No save occurred.

### Return-policy redline — prepared, not published

Live policy currently says “unworn, unused” and “original condition and packaging,” excludes shipping from refunds, excludes made-to-order and discounted items, and asks shoppers to report defects within five days. These limits need Latvian legal review before publication.

Proposed replacement for legal counsel/owner review:

> **Right to withdraw**  
> For most online purchases, you may withdraw from the contract within 14 days after delivery without giving a reason. To exercise this right, contact us at autumnandwool@gmail.com within that period. Please return the goods without undue delay and no later than 14 days after notifying us. You may examine the goods as you would in a shop. You may be responsible for any reduction in value caused by handling beyond what is necessary to inspect them.
>
> **Refunds**  
> We will reimburse payments received, including the cost of standard delivery, within 14 days after you notify us that you are withdrawing. We may withhold reimbursement until we receive the returned goods or evidence that you have sent them. If you selected a more expensive delivery option, we reimburse only the standard delivery cost.
>
> **Return postage**  
> You are responsible for the direct cost of returning goods where this was disclosed before purchase. Contact us first for goods that arrive faulty or damaged; statutory remedies remain unaffected.
>
> **Exceptions and faulty goods**  
> The right of withdrawal does not apply only where a statutory exception applies, such as goods made to your specifications or clearly personalized. A standard item made after an order is not excluded for that reason alone. Sale prices do not remove statutory rights. Nothing in this policy limits your rights for faulty or non-conforming goods.

This is a drafting proposal, not legal advice. Have Latvian counsel confirm the wording and the applicable withdrawal form, deadlines, and consumer-guarantee language. Sources: [Latvian PTAC — Right of withdrawal](https://www.ptac.gov.lv/en/right-withdrawal) (updated 2 Feb 2025); [EU Your Europe — e-commerce withdrawal and trader obligations](https://europa.eu/youreurope/business/selling-in-eu/selling-goods-services/ecommerce-distance-selling/index_en.htm); [EU Your Europe — returns](https://europa.eu/youreurope/citizens/consumers/shopping/returns/index_en.htm) (checked 28 Apr 2026).

### Search Console — fresh account verification

Switched from the wrong signed-in Google account to the previously authorized Autumn and wool profile. Verified that it can open `https://www.autumnandwool.com/`. The latest available Performance data remains 15 July–14 October 2026: 11 clicks, 372 impressions, 3% CTR, average position 14.2. Overview shows 11 indexed, 4 not indexed; product snippets 1 valid / 0 invalid; merchant listings 1 valid / 0 invalid. No property setting was changed.

### Squarespace UI preview — 18 October 2026

- Saved native text and button edits on **Redesign Preview (Hidden)**: “Warmth in every detail.” hero, approved subtitle, “Shop Knitwear” → `/shop`, “Our Story” → `/about`, and “Behind every stitch.” with factual copy and “Meet Autumn & Wool →” → `/about`.
- Added a native “Shop by category” row with Cardigans → `/shop/cardigans`, Sweaters → `/shop/sweaters`, and Beanies & Hats → `/shop/beanies--hats`. These targets match existing Squarespace categories; Accessories was represented by the closest existing category, Beanies & Hats.
- Page remains under **Not Linked** and **Disabled**. Save is clean. Publish was not clicked; the public Home page and commerce data are unchanged.
- Visual preview captures: [desktop hero](/Users/eramadan/autumnandwool/evidence/redesign-preview-after-desktop.png), [mobile hero](/Users/eramadan/autumnandwool/evidence/redesign-preview-after-mobile.png), [desktop story](/Users/eramadan/autumnandwool/evidence/redesign-preview-after-story.png), [desktop category row](/Users/eramadan/autumnandwool/evidence/redesign-preview-final-category.jpg), [mobile category stack](/Users/eramadan/autumnandwool/evidence/redesign-preview-final-mobile-category.jpg). Category heading now precedes all three buttons on mobile.
- Not implemented: eyebrow, image-based category tiles, trust strip, and requested featured-product substitutions. Existing native product blocks remain unchanged: vest €126, hat/scarf set €110, cardigan €145 first; beanie €45 later. No product records, prices, stock, variants, checkout, policies, or newsletter were changed.
- Mobile/desktop were inspected visually only. No viewport suite, purchase flow, shipping, newsletter, or stock test was run.

### Checkout follow-up — 18 October 2026

| Product / check | Result | Evidence |
|---|---|---|
| Rib-Knit Beanie — desktop | Blocked before payment | Black selected by default; Purchase opened checkout; cart subtotal €45; Latvia delivery offered with free shipping. Synthetic QA details reached the Payment section, but Continue returned “Enter the required information.” The payment/address frame exposed no usable payment fields and remained blank. Stopped before payment. |
| QA cart cleanup | Complete | Removed the beanie. Public `/cart` shows “You have nothing in your shopping cart” and header shows 0 items. |
| Product data | Unchanged | No product title, description, metadata, category, tag, price, image, variant, stock, SKU, ID, or URL was edited or imported in this pass. |

This desktop failure differs from the earlier mobile checkout runs that reached the payment UI. It needs a fresh payment-settings/platform diagnosis before claiming desktop purchase readiness. No real payment or order was submitted. The task sheet’s full checkout success condition remains unverified.

### Search Console sitemap refresh — 18 October 2026

- Submitted the live `https://www.autumnandwool.com/sitemap.xml` under the verified URL-prefix property.
- Search Console confirmed “Sitemap submitted successfully”; the table updated to submitted/read 18 Oct 2026, Success, 37 discovered pages, 0 videos.
- Existing `/sitemap.txt` remains Success but last read 25 Dec 2025 (42 pages). No removal or URL change was made.
- Current Page indexing report (last update 12 Oct): 11 indexed, 4 not indexed. Reasons: 3 crawled-currently-not-indexed; 1 alternate page with proper canonical. Zero 404s. Three unindexed examples include two older product URLs and `/shop/vests`; no product URLs or product records were changed.


### Analytics tracking verification — 18 October 2026

- Squarespace Settings → Developer Tools → External API Keys contains GA4 measurement ID `G-7TV8PK060Z`. The ID matches the GA4 web stream for `https://www.autumnandwool.com/` (stream ID 13239857437).
- GA4 says collection is active in the past 48 hours. Enhanced Measurement is enabled. Recent events in the last 28 days: `click`, `first_visit`, `page_view`, `scroll`, `session_start`, and `user_engagement`. No ecommerce events appeared. `purchase` is configured as a key event but shows no stream data.
- Squarespace's built-in GA integration documents visitor, traffic-source, and sales tracking and says order data is sent for every order ([Squarespace help](https://support.squarespace.com/hc/en-us/articles/205815608-Connect-Google-Analytics-to-your-site)). The store has zero completed orders, so purchase-event delivery cannot be proven without an actual test order. No test order was submitted. No GA4 or Squarespace settings changed.
- The Squarespace Traffic view currently shows 64 visits, 64 unique visitors, 61 pageviews, and **95.95% bounce** for Sep 19–Oct 18. Earlier report text said 94.55%; that was a transcription error.
- Dashboard internal consistency issue: the same Traffic view reports device totals of 106 and browser subtotal counts that exceed 64 visits (Chrome 62, Chrome Mobile 17, Mobile Safari 10, Safari 5, Others 7). Treat those breakdowns as unreliable pending Squarespace support; top sources (Direct 61, Google 2, Facebook 1) sum to 64.


### Cart analytics smoke test — 18 October 2026

- Opened the public Rib-Knit Beanie page and clicked Purchase once. The browser page then rendered blank, so checkout navigation and GA4 `add_to_cart` were not confirmed.
- A separate cart check showed one QA beanie (€45); removed it. Fresh cart view confirms “You have nothing in your shopping cart” and 0 items. No checkout or payment was submitted.
- Screenshot: [empty cart after cleanup](/Users/eramadan/autumnandwool/evidence/cart-empty-2026-10-18.jpg). Product data unchanged.


### Abandoned-checkout recovery — rechecked 18 October 2026

- Squarespace Automations was available. “Recover abandoned carts” was inactive and the menu offered “Go Live.” Enabled it. Squarespace then showed the automation as **Live** and confirmed “Automation activated.” It triggers at checkout abandonment, waits one day, then sends one reminder if no order was placed. The message includes an unsubscribe link. No test reminder or order was sent.


### Organic campaign assets — 18 October 2026

- Prepared six local, unpublished drafts: three Pinterest pins and three Instagram posts. Each has a caption, canonical destination with UTMs, and a portrait image copied unaltered from the live product page. Files and source references are listed in [campaign-drafts.md](/Users/eramadan/autumnandwool/campaign-assets/campaign-drafts.md).
- Social ownership is not confirmed: the public header links Instagram `@autumnandwool` while the footer links `@mare.knitwear`; Facebook and Pinterest also use Mareshop accounts. No platform upload, scheduling, or publication.
- Source photos are 3:4 portrait. Platform-specific crops were not applied, preserving the exact product photos. Confirm account ownership and crop format before posting.
- No product fields changed.


### Newsletter follow-up — 18 October 2026

- Saved the requested welcome email copy locally at [welcome-email-draft.md](/Users/eramadan/autumnandwool/campaign-assets/welcome-email-draft.md).
- No welcome email was uploaded or sent. Footer form consent, subscriber destination, double opt-in, unsubscribe handling, and sender configuration remain unverified. Campaigns settings show no usable controls; the Automations page works and cart recovery is Live.

### Shipping and payment settings recheck — 18 October 2026

- Merchant Center was checked under the Autumn & Wool Google profile. Products & store → Shipping and returns has no shipping policy. Opened the policy wizard to inspect requirements, then left without saving; delivery-time values were not available from verified store settings.
- Squarespace has three €0 shipping options: Latvia, United States (54/54 states and territories), and Rest of world. The inspected rate setup contains no delivery-time range. Google shipping setup remains incomplete until actual delivery estimates are confirmed.
- Squarespace Payments shows Stripe Connected, Test Mode Off, EUR currency, and multi-currency checkout On. PayPal is not connected. This confirms a Stripe connection, not payout/account readiness. No payment or shipping setting changed.
- Product data freeze remains active. No product field or catalog record was edited.


### Fresh public-site and automation verification — 18 October 2026

- Public homepage rechecked in a fresh browser tab. Hero reads “Wool Knitwear for Cooler Days,” with Shop and Size Guide buttons. Four product blocks are present, but order is vest (€126), hat/scarf set (€110), cardigan (€145); beanie (€45) appears after the brand introduction. The direct Winter Wool Gifts CTA and shopping-assistance strip are absent.
- `/redesign-preview` returns the public site’s not-found page, though Squarespace still lists “Redesign Preview (Hidden)” in Not Linked. The editing preview iframe is `about:blank`; homepage changes cannot be made or republished through this editor state.
- Squarespace Automations is available. “Recover abandoned carts” is now **Live**. Trigger: customer leaves cart at checkout; wait: 1 day; sends one reminder if no order; email footer includes unsubscribe. Squarespace confirmed “Automation activated.”
- Welcome/new-subscriber email remains inactive. The campaign settings page renders no usable controls; consent, audience, and sender settings are unverified. No newsletter signup was submitted and no welcome email was sent.
- Fresh public FAQ recheck shows unverified dispatch and delivery ranges (1–2 business days processing; 2–4 days Europe, 3–5 days UK/Ireland, 5–10 days worldwide), plus “handmade or made-to-order” wording. These remain visible and need factual confirmation or editing access.
- No product records or product fields changed.

## Consolidated status against the source mission — 18 October 2026

This matrix reflects current browser evidence and the user’s product-data freeze. “Partial” means a deliverable exists but its stated success condition is not met.

| Mission item | Status | Current evidence / remaining work |
|---|---|---|
| 1. Checkout verification | Partial; not passed | Mobile Latvia checks reached Stripe/Link, but no payment/order. Desktop beanie flow showed a blank payment/address frame. Test mode and real-order submission were not used. |
| 2. Homepage structure | Partial | Live home has factual hero and four product links, but beanie is separated after the brand section; no Winter Wool Gifts CTA or shopping-assistance strip. Editor iframe is blank; `/redesign-preview` is 404. |
| 3. Unsupported claims | Incomplete | Fresh FAQ still has unverified manufacturing and delivery-time claims. Shipping/Returns and Privacy also contain flagged claims. Product metadata/alt-text claims remain frozen. |
| 4. Four priority product pages | Prior edits only; frozen | Earlier copy changes and metadata are recorded above. Do not edit product titles, copy, metadata, tags, categories, prices, images, variants, stock, SKUs, IDs, or URLs. |
| 5. Labels and duplicate listings | Partial | Shop categories are present; unfiltered “No results found” was not visible. Duplicate-looking listings have separate IDs/URLs/images; no records changed. |
| 6. Winter gifts | Partial | “Winter Wool Gifts” category is live with existing products. Direct homepage promotion is absent. |
| 7. Search Console / Merchant Center | Partial | URL-prefix property verified and sitemap submission succeeded (37 discovered pages); 11 indexed, 4 not indexed. Merchant Center has 2 auto-discovered, 0 owner-provided, 0 approved; shipping policy missing. Delivery estimates unavailable, so shipping was not invented. |
| 8. Newsletter / welcome email | Prepared, not verified | Welcome email is drafted locally. Consent, destination, double opt-in, unsubscribe, and sender configuration are unknown; no subscriber signup or welcome flow activation. |
| 9. Six organic campaigns | Prepared, unpublished | Six local copy/photo drafts with UTMs exist. Account ownership is inconsistent between site header and footer; no social posts were uploaded or published. |
| 10. Measurement | Partial | Weekly snapshot/report exists. Current 30-day data: 64 visits, 64 unique visitors, 61 pageviews, 95.95% bounce, 0 orders. Ecommerce event funnel and interactive dashboard are unavailable/unverified. |
| 11. Return-policy review | Prepared for legal review | Redline exists; not published pending Latvian legal/owner review. |
| 12. Analytics | Partial | GA4 stream is connected and collecting page/engagement events. No ecommerce events or purchase event verified; no order exists. |
| 13. Final QA and evidence | Partial | Public-page checks, mobile/desktop checkout attempts, empty-cart proof, and preview images are recorded. Checkout is not passed; fresh page-editor preview is blank. |
| Abandoned checkout recovery | Done; live | Squarespace shows “Recover abandoned carts” Live: one reminder after 1 day if no order, unsubscribe included. No recovered sale is evidenced yet. |

Product data remains untouched during this pass. No sales result is claimed from impressions, draft assets, or automation activation.

## Fixes applied — 18 October 2026 (evening), data taken from Etsy shop mareshop

Owner approved product-data edits using public Etsy listing data. Certification/eco claims (RWS, mulesing-free, organic, sustainable) were deliberately NOT copied. Contact email kept as autumnandwool@gmail.com. Long cardigan material set to Etsy wording (100% pure new wool). Instagram links unified to @autumnandwool.

| Area | Change | Status |
| --- | --- | --- |
| Cart | Settings → Selling → Cart: "Skip cart page" turned OFF; add-to-cart confirmation = button + cart; Continue Shopping → Shop. Product pages now show "Add To Cart". | Live, verified |
| FAQ | Payment answer no longer promises PayPal; dispatch 2–5 working days; delivery Europe ~5–10 working days, USA/Canada/Australia 7–20 days; materials answer; "sustainable" Q replaced by "How are your pieces made?" (Kristine, hand/manual machine knitting, hand-sewn); size answer = garment measurements; Instagram → @autumnandwool. | Live, verified |
| Shipping & Returns | International paragraph now lists dispatch and delivery estimates; closing "sustainable fashion" line replaced. Legal return terms unchanged (still need legal review). | Live |
| Contact | Added company details (AUTUMN AND WOOL, SIA, reg. 40203644965, Braslas iela 22d, Rīga, LV-1035) and Mareshop/Etsy line linked to Etsy reviews. | Live, verified |
| About | Added Kristine + 15 years as Mareshop on Etsy (8,000+ orders, 4.9★ from 1,400+ reviews) and how pieces are made. | Live, verified (desktop + mobile) |
| Homepage | Hero subtitle: "Handmade in Riga by Kristine. Formerly Mareshop on Etsy, rated 4.9★ by 1,400+ customers" (link to Etsy reviews). Brand section text: made in Latvia, free shipping, 14-day returns, measurements on every garment page. | Live, verified |
| Footer (global) | Tagline: handmade by Kristine, formerly Mareshop; copyright line now © 2026 + company name, reg. no., address, email; footer Instagram → @autumnandwool. | Live, verified |
| Products | Descriptions rewritten from Etsy for 20 public products (material, fit, per-size garment measurements, model size, care, delivery & returns line). Removed stale fragments ("Layering options extend…", "How do I care…", orphan merino paragraph). Stand-collar sweaters renamed "— Blue" / "— Beige". Long Wool Cardigan SEO title/description fixed (no more "Machine-washable"). Black Merino Raglan Cardigan left as is (already complete). | Saved; spot-checked live |
| Google Merchant Center (acct 5687087698) | Business address added; shipping policies: Latvia free, 2–5 handling + 2–5 transit; 18 EU countries free, 2–5 + 5–10; USA/Canada/Australia free, 2–5 + 7–20. Return policy (Latvia): 14 days, new items, by mail, customer pays return postage, no restocking fee, refund 7 days, URL /shipping-returns. Setup shows "completed". | Saved; Google review pending (up to 10 days for returns) |

### Not done / needs owner
- Etsy review import into Squarespace (Settings → Selling → Product Reviews → Etsy Reviews → Import) needs Etsy sign-in by the owner.
- Real test order on desktop + phone, then refund. Check tax settings (checkout shows Tax €0.00). Connect PayPal only if wanted (FAQ no longer mentions it).
- Facebook and Pinterest links still point to Mareshop accounts (only Instagram was changed, per owner).
- Merchant Center still only has 2 auto-found products: connect Squarespace's Google product feed so all products are submitted.
- Checkout default country is United States; consider Latvia.
- Return-policy legal review (redline above) still pending.
- Other product SEO titles/descriptions beyond the long cardigan still contain old Etsy-style wording.

### Note
During this session other edits appeared on the site that were not made in this session: an announcement bar ("Free shipping · 14-day returns · Handmade in Riga"), an "Autumn Picks" homepage section, new hero button labels, colour names on Side-Slit and Lambswool Raglan Crew listings, and one beige vest listing set to Hidden. Check whether another session or person is editing.

## Traffic actions — 18 October 2026 (late evening)

| # | Action | Status |
|---|---|---|
| 1 | Google Merchant Center: uploaded `autumnandwool-google-feed.tsv` as a primary product source (feed label EU, English). All 21 physical products / 98 variants, with SKUs, prices, images, colour, size, gender, category. | Done. Merchant Center reports 98 products added, all attributes recognised, no file issues. Products are now in Google review (usually 3–5 days). |
| 1a | Shipping in Merchant Center covers Latvia, 18 EU countries, US, CA and AU (set up earlier). The source also lists other countries with no shipping set, so products just won't show there. | No action needed unless you start shipping elsewhere. |
| 1b | The upload is manual. When prices, stock or products change, regenerate the feed (`build_google_feed.py`) and click "Update" on the source. Squarespace's automatic Google sync needs a plan upgrade. | Note |
| 3 | Pinterest and Instagram posts | Not posted: neither account is signed in on Chrome, and I can't enter passwords. Sign in to Pinterest (and Instagram), then I can post the six drafts in `campaign-assets/campaign-drafts.md`. |
| 4 | 10%-off sign-up pop-up | Blocked: Squarespace Discounts and Promotional Pop-Up are locked on the current plan. Needs a plan upgrade (owner's decision). |
| 6 | Riga Christmas markets and gift-guide media | Research done: `markets-and-gift-guides.md` (dates, deadlines, contacts, pitch drafts in EN/LV — not sent). |

## Free traffic actions — 18 October 2026 (night)

| Action | Result |
|---|---|
| Google Search Console | Already connected; sitemap.xml read today (37 URLs). Only 11 pages were indexed, including just 2 product pages. Requested indexing for 12 product pages (beanie, hat & scarf set, turtleneck, black cardigan, both long cardigans, open-front cardigan, camel side-slit, lambswool brown, classic lambswool, merino vest, beige vest). Google's daily limit was reached. |
| Still to request (tomorrow, quota resets daily) | Beige raglan, lambswool green, distressed raglan, stand-collar beige and blue, dusty pink turtleneck, dusty pink raglan. |
| Bing / Microsoft Merchant Center | Not done: needs a new Microsoft account sign-up, which only the owner can create. After sign-up, Bing Webmaster Tools can import from Search Console and Microsoft Merchant Center can import from Google Merchant Center. |
| Product SEO titles & descriptions | 17 products got new titles and descriptions (material, colour, made in Latvia, free shipping / 14-day returns). This removed false "machine-washable" claims, cut-off titles ("Natural Fib…") and "sustainable" wording on the gift card. On 4 more products the doubled "| Autumn & Wool" title ending was removed. All 22 checked live; other product fields verified unchanged. |
| Newsletter sign-up | Footer sign-up (every page) already stores to Squarespace Contacts. Text changed to "Get new knits, restocks and gift ideas from Riga. A few emails a season, no spam." No discount promised. |
| Note | Another edit to the Stand-Collar Blue product's SEO happened in parallel during this session (someone else changed it); my version was saved last. |

## Follow-up — 18 October 2026, 00:30 UTC

| Check | Result |
|---|---|
| Google indexing, last 7 product pages | Not sent yet: Google's daily limit is still used up (it resets around 10:00 Riga time). A reminder in this conversation retries at 10:00 Riga time on 19 Oct. |
| Merchant Center status | 98 products "Available soon" (still in Google's review). No account-level setup or policy issues. All 98 were flagged "not approved" for 3 reasons, all caused by the feed targeting ~95 countries: South Korea needs a Korean business number; ~80 countries have no shipping set; prices in EUR are not accepted in non-euro countries. |
| Fix applied | Feed countries changed to the 13 euro countries that have free shipping set up: Latvia, Austria, Belgium, Finland, France, Germany, Greece, Ireland, Italy, Netherlands, Portugal, Slovakia, Spain. Google needs time to re-check the products. |
| Trade-off | Shipping is also set for Czechia, Denmark, Hungary, Poland, Romania, Sweden, the US, Canada and Australia, but those countries don't use EUR, so they are left out for now. To add them later, add a second feed with prices in each local currency. |
