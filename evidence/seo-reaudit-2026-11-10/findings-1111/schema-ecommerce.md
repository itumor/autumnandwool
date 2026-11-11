# Schema and e-commerce structured data: re-audit 2026-11-11

Scope: 49 crawled pages in `crawl-1111` (22 product, 7 shop category, 4 guides, 16 other pages). Offline analysis only; no live requests.
Method: JSON-LD parsed from every page (0 parse errors, 0 placeholder strings). OG/Twitter meta read from the same HTML. Visible price read from the product page text.

Tags: `fixable` = owner can change in Squarespace settings or product data. `platform` = Squarespace emits it; not editable on this plan (no code injection); covered through Merchant Center feed. Platform items are scored at 50% weight.

## Score: 47 / 100

- Owner-fixable deductions: -27 (full weight).
- Platform deductions: -26 (50% of nominal -52).
- Without platform items the score would be 73.

## Findings

| ID | Severity | Tag | Finding | Evidence | Weight |
|---|---|---|---|---|---|
| S-01 | High | fixable | Product `sku` absent on 22/22 Product blocks | all `/shop/p/*` JSON-LD | -12 |
| E-01 | Medium | fixable | 7 shop category pages (`/shop`, `/shop/cardigans`, `/shop/beanies--hats`, `/shop/gift`, `/shop/sets`, `/shop/sweaters`, `/shop/vests`, `/shop/winter-wool-gifts`) have no meta description and no og:description | meta scan | -6 |
| S-02 | Low | fixable | Organization `sameAs` lists Instagram and TikTok only. The legacy Etsy shop `etsy.com/shop/mareshop` is linked visibly on `/`, `/home`, `/about` but not declared. Owner decision: declare it if the shop is still live | `sameAs`, link scan | -2 |
| S-03 | Medium | fixable | Organization/LocalBusiness `address` is one text string with a newline and blank region (`"22d Braslas iela\nRīga, , 1035\nLatvia"`), not a structured PostalAddress. Blank region is likely a Business Info field left empty (unverified) | JSON-LD on all 49 pages | -3 |
| S-04 | Low | fixable | `telephone` is `""` (empty string) and no `openingHours`. Imprint shows no phone, so no value to add unless owner publishes one | JSON-LD, imprint text | -2 |
| S-05 | Low | fixable | WebSite `description` is empty string | JSON-LD | -2 |
| S-06 | High | platform | Product `url` absent on 22/22 | JSON-LD | -3 |
| S-07 | High | platform | Product `offers.shippingDetails` absent on 22/22 | JSON-LD | -4 |
| S-08 | High | platform | `hasMerchantReturnPolicy` absent on 22/22 | JSON-LD | -4 |
| S-09 | Medium | platform | `gtin`/`mpn`, ProductGroup absent on 22/22 | JSON-LD | -3 |
| S-10 | Medium | platform | BreadcrumbList absent on all 49 pages | JSON-LD | -4 |
| S-11 | Low | platform | ItemList absent on 7 shop category pages | JSON-LD | -2 |
| S-12 | Low | platform | Article absent on 4 guides (`how-to-wash-a-wool-sweater`, `merino-vs-lambswool`, `oversized-fit-guide`, `how-to-choose-a-wool-cardigan`) | JSON-LD | -1 |
| S-13 | Low | platform | `@context` is `http://schema.org` in all blocks | JSON-LD | -1 |
| S-14 | Low | platform | `http://` scheme on Product `image`, og:image, twitter:image (all pages) | meta, JSON-LD | -1 |
| S-15 | Low | platform | WebSite `image` is protocol-relative (`//images.squarespace-cdn.com/...`) | JSON-LD | -1 |
| S-16 | Low | platform | `twitter:card` is `summary` on 49/49 (1200x630 social image shows as small thumbnail) | meta | -1 |
| S-17 | Low | platform | Organization has no `url` or `logo` | JSON-LD | -1 |
| S-18 | Info | n/a | No FAQPage on `/faq`. Do not add (Google FAQ rich results retired 2026-05-07) | faq.html | 0 |
| S-19 | Info | n/a | No HowTo present. Do not add | all pages | 0 |
| S-20 | Info | platform | LocalBusiness type emitted sitewide for an online shop with a registered studio address. Type is not editable | JSON-LD | 0 |

Platform total deduction: -26 (sum of half-weights for S-06 to S-17). Fixable total: -27 (S-01 to S-05). Score = 100 - 27 - 26 = 47.

## Product validation (22 products)

| Check | Result |
|---|---|
| `@type` Product, name, description, brand, image | Pass 22/22 (brand is a string, not a Brand object: minor, platform) |
| Offer type | Offer 9/22; AggregateOffer 13/22 (multi-variant; lowPrice = highPrice in all cases) |
| priceCurrency EUR | Pass 22/22 |
| Visible price = JSON-LD price | Pass 22/22 (gift card: visible "from €25.00" vs AggregateOffer 25-250, consistent) |
| og:product:price:amount = visible | Pass 22/22 |
| availability | InStock 22/22; no sold-out text visible; live stock not verified |
| url, sku, gtin | Fail 22/22 (S-01, S-06, S-09) |
| aggregateRating / review | Absent 22/22; no visible reviews on any product page (not an error; opportunity only if real reviews exist) |
| shippingDetails, hasMerchantReturnPolicy | Absent 22/22 (S-07, S-08) |

Full per-product row data: `scratchpad/schema/products.py` output (slug, offer type, price, sku, url, image scheme, og:image dims).

## Organization / LocalBusiness / WebSite

| Check | Result |
|---|---|
| name "Autumn & Wool" | Pass |
| legalName "AUTUMN AND WOOL, SIA" | Pass; matches imprint |
| email | Pass; matches contact page |
| url (WebSite) | Pass (`https://www.autumnandwool.com`) |
| url (Organization) | Absent (S-17) |
| logo | Absent (S-17) |
| telephone | Empty (S-04); not published on imprint |
| openingHours | Absent (S-04) |
| address | Present, unstructured (S-03); street/postcode match imprint |
| sameAs | Instagram, TikTok; Etsy legacy not declared (S-02) |

## Blocks

- BreadcrumbList: absent everywhere (S-10).
- ItemList: absent on category pages (S-11).
- Article: absent on guides (S-12).
- FAQPage: absent (S-18).

## Open Graph / Twitter

| Check | Result |
|---|---|
| og:title | Pass 49/49 |
| og:image 1200x630 on non-product pages | Pass 27/27 |
| og:image dimensions on products | Portrait 1500x2000 and similar; 1 gift card 1024x1024 (product photo, acceptable) |
| og:image scheme | http on 49/49 (S-14) |
| og:description | Absent on 7 category pages (E-01) |
| product:price:amount / currency / availability | Pass 22/22 (`instock`) |
| twitter:card | summary 49/49 (S-16) |

## Not verified

- Live rendering of JSON-LD (raw HTML only; SPA check not run).
- Whether `address` blank region and the empty `telephone` can be fixed in Business Info (unverified).
- Whether Squarespace exposes twitter:card type or Organization logo as settings (unverified).
- Whether guides would get Article if converted to blog posts (unverified).
- Live stock state and product `sku` availability in the Squarespace product editor.
- LocalBusiness `image` URL (folder-style path, no extension): not checked whether it resolves.
- H1 vs product name match.
