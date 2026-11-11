# SEO re-audit — autumnandwool.com — 2026-11-10, 17:10 EET

Tool: claude-seo v2.5.0. Eight specialist passes (technical + sitemap, content + on-page, schema + e-commerce, performance, visual + images, AI search, search intent, backlinks) on one shared crawl of 49 URLs, then a manager spot-check of every disputed finding against the raw HTML.
Compared with: the morning audit, [2026-11-10-seo-audit-and-action-plan.md](2026-11-10-seo-audit-and-action-plan.md) (56 / 100), written in the `seo-audit-optimization-9ba6ac` worktree.
Nothing on the live site, Merchant Center or Etsy was changed by this run.

**SEO Health Score: 61 / 100** (morning: 56)

| Category | Weight | Morning | Now | Detail file |
|---|---|---|---|---|
| Technical SEO | 22% | 70 | 70 | [technical.md](../../evidence/seo-reaudit-2026-11-10/findings/technical.md) |
| Content quality | 23% | 55 | 55 | [content-onpage.md](../../evidence/seo-reaudit-2026-11-10/findings/content-onpage.md) |
| On-page SEO | 20% | 40 | 58 | same file, 49-row title / description / H1 table |
| Schema / structured data | 10% | 45 | 55 | [schema-ecommerce.md](../../evidence/seo-reaudit-2026-11-10/findings/schema-ecommerce.md) |
| Performance | 10% | 61 | 61 (carried over, see below) | [performance.md](../../evidence/seo-reaudit-2026-11-10/findings/performance.md) |
| AI search readiness | 10% | 64 | 56 | [geo-agentic.md](../../evidence/seo-reaudit-2026-11-10/findings/geo-agentic.md) |
| Images | 5% | 62 | 78 | [images-visual.md](../../evidence/seo-reaudit-2026-11-10/findings/images-visual.md) |

Also: [sxo-keywords.md](../../evidence/seo-reaudit-2026-11-10/findings/sxo-keywords.md), [backlinks.md](../../evidence/seo-reaudit-2026-11-10/findings/backlinks.md), screenshots in `evidence/seo-reaudit-2026-11-10/screenshots/`, raw crawl in `evidence/seo-reaudit-2026-11-10/crawl/`.

How to read the scores:

- They are specialists' judgement against the claude-seo rubric, not a Google number. A different specialist run scored each category, so a move of a few points is noise. The moves that rest on counted evidence are On-page (+18), Schema (+10) and Images (+16).
- Performance was not re-measured in a comparable way. The PageSpeed API was over its daily quota on all six runs. A local Lighthouse run gave mobile 64–66 and desktop 83–95, but it runs on a different machine with different throttling, so the morning score is carried over.
- AI search readiness dropped 8 points on paper. Nothing got worse on the site; this run's scorer weighted missing author, dates and off-site presence more heavily. The `llms.txt` it criticised was being replaced by another session at the time of the crawl.
- Backlinks: the domain is not in the Common Crawl link graph (too new, too few links). No score.

## What changed since the morning (verified in raw HTML)

| Morning finding | Now |
|---|---|
| No guides | 4 guides live and in the sitemap, 412–451 words each |
| Category pages cannot rank, no alternative | 5 landing pages live (`/wool-sweaters`, `/wool-cardigans`, `/wool-sweater-vests`, `/wool-hats-and-scarves`, `/wool-gifts`), each with its own canonical, H1 and description |
| 115 file-name alt texts, 84 over 125 characters | 0 and 0 across 1,462 image tags |
| Review claims without a source | Both now say "on Etsy" and link to the Etsy shop |
| Opening hours in structured data | Gone |
| Product names carried " \| Autumn & Wool" | Clean on 22 of 22 |
| Product pages linked to nothing | Related-products block and size-guide link present |
| Titles and descriptions weak | Titles unique (except `/home`); 42 pages have a description of 103–155 characters |

## Still open

| # | Severity | Finding | Evidence | Fixable here? |
|---|---|---|---|---|
| 1 | High | Two sets of pages now target the same searches. The 7 `/shop/<category>` pages (no H1, empty description, canonical to `/shop`) sit beside the 5 new `/wool-*` pages. Worst pair: `/wool-gifts` against `/shop/winter-wool-gifts` and `/shop/gift`. | T-01, O-01, O-03, X-02, C-20 | Yes: point every menu and in-page link at the `/wool-*` page; the `/shop/<category>` tag itself is a platform limit |
| 2 | High | The `/wool-*` pages list product names without prices or photos up front. On a phone the first screen is one long paragraph. Pages that rank for these searches are product grids with prices. | X-01, V-02, `wool-sweaters-mobile-fold.png` | Yes: product blocks with price, intro cut to two or three lines above them |
| 3 | High | `/wool-gifts` has no December delivery cut-off. | X-06 | Yes, needs owner dates (SEO-26) |
| 4 | High | Wording on how garments are made still conflicts: `/privacy-policy` says "handmade knitwear brand", other pages say machine-knitted and hand-finished, 12 product URLs contain "hand-knitted". | C-03, spot-checked | Page text yes; leave the URLs |
| 5 | High | Colour-twin products are 98–99% identical in text (three pairs), and two shawl cardigans are 94% identical. | C-05, C-06 | Yes, product text |
| 6 | High | Guides have no author and no date, and two of four do not answer the question in the first paragraph. `/oversized-fit-guide` has no size table; `/merino-vs-lambswool` has no comparison table. | C-11, C-12, G-04, G-05, X-04, X-05 | Yes, content |
| 7 | High | Cookie banner is about 150 px tall on a 390 px phone and covers the lower part of the product title on first visit. | V-01, `product-mobile-fold.png` | Yes, banner settings or Custom CSS; keep the overlay guard |
| 8 | Medium | Organisation data in structured data has only the legal name "AUTUMN AND WOOL, SIA": no brand name, URL or logo, empty phone, and two social links that point to Mareshop profiles (Facebook, Pinterest). | S-16, S-17, G-06, spot-checked | Yes, Business Information and Social Links; owner decides on the Mareshop profiles |
| 9 | Low | `/home` is still in the sitemap at top priority and duplicates `/`; `/` is not in the sitemap. Its canonical already points to `/`. | T-02, T-03 | No. `/home` is the homepage itself: hiding it from search would also hide `/`, and a URL mapping does not override a live page. Platform limit. |
| 10 | Retracted | "Old single-`/p/` product URL returns 404." Wrong: the probe URL (dusty-pink raglan) was made up by the manager session and never existed. The redirect the earlier session logged (`/shop/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper`) returns 301 to the right page, checked 20:33. | T-07 | Nothing to fix |
| 11 | Medium | `llms.txt` (as crawled) has internal editing notes ("as checked on 1 November 2026", "do not describe it as lambswool"), "since 2011", links to `/shop/<category>` pages, and none of the 9 new pages. | G-01, G-02, T-12 | Yes, file upload (in progress in the other session) |
| 12 | Medium | Return conditions are worded three ways ("unwashed", "unused", "original condition"). | G-03 | Yes, content |
| 13 | Medium | 15 products with variants publish a price range and no SKU in structured data; no shipping or returns data on any product. | S-01, S-03, S-04 | SKU field maybe; the rest is a platform limit, covered by the Merchant Center feed |
| 14 | Medium | Mobile speed: simulated LCP 10–14 s on all three pages tested. `/shop` loads 2.8 MB of images on mobile, and its largest painted element is the cookie banner text. | performance.md | Images yes; platform JavaScript no |
| 15 | Medium | Social preview image is still 1024 × 1536 portrait. | I-01 | Yes |
| 16 | Low | `/shop` and `/cookie-policy` have no H1; home H1 "Wool knitwear for cooler days" names no garment. | O-01, X-08, X-09 | Yes |
| 17 | Low | `/shop/gift` has no internal link. | T-04 | Yes |

Checked and fine: 49 of 49 URLs return 200; no `noindex` anywhere; apex and `http` redirect to `https://www` in one hop; content is in the raw HTML; AI crawlers are allowed on all content pages; price in structured data matches the visible price on 22 of 22 products; no missing alt attributes.

Not a problem: no FAQ markup on `/faq` (Google retired FAQ rich results on 2026-05-07, do not add it); no hreflang on a single-language site; security headers and IndexNow, which Squarespace does not expose.

## Action plan

Task IDs continue from SEO-50. Everything is a proposal until the owner approves; product text needs the same scoped unfreeze used for today's alt-text batch.

| ID | Action | Layer | Effort | Depends on | How we would know it failed | What to watch |
|---|---|---|---|---|---|---|
| SEO-51 | One URL per search. Check every menu, footer, home tile and guide link; each should go to the `/wool-*` page, none to `/shop/<category>`. Link `/wool-gifts` from the home hero. | Navigation, page links | S | none | Search Console still shows `/shop` for "wool cardigan" queries after 4 weeks | Pages report: impressions per `/wool-*` URL |
| SEO-52 | Put products with photo and price at the top of each `/wool-*` page; cut the intro to 2–3 lines above them, rest below. | Page editor | M | SEO-51 | Mobile first screen still shows no product (`wool-sweaters-mobile-fold.png` retake) | Clicks from `/wool-*` to product pages in Squarespace analytics |
| SEO-53 | Add delivery cut-off dates per region to `/wool-gifts` and the shipping page. | Content | S | Owner dates (SEO-26) | Dates missing on 1 December | Gift-page visits from search |
| SEO-54 | One wording for how garments are made, everywhere, including `/privacy-policy`. One wording for return conditions. | Content | S | Owner picks the wording | A site search for "handmade" still finds a page | none needed, one-off |
| SEO-55 | Colour twins: own first paragraph per colour and a link to the twin; decide whether the two shawl cardigans are one product. | Product text | M | Scoped unfreeze | Pair similarity still above 85% on the next crawl | Which twin Google shows per query |
| SEO-56 | Guides: answer in the first 2–3 sentences, add "By Kristine, updated <date>", add the size table and the merino-vs-lambswool table, link each guide to 3–4 products. | Content | M | none | First paragraph does not contain the answer | Impressions for the four guide URLs |
| SEO-57 | Cookie banner: compact layout or less padding on mobile, target under 100 px. Never hide it; keep `pointer-events:none !important` on the overlay selectors. | Banner settings / Custom CSS | S | none | Banner height on a 390 px retake | Mobile add-to-cart rate |
| SEO-58 | Business Information: brand name "Autumn & Wool", logo, phone or none; Social Links: decide on the two Mareshop profiles. | Squarespace settings | S | Owner decision | Home JSON-LD still lacks `name` and `logo` | none needed, one-off |
| SEO-59 | Link or remove `/shop/gift`. (`/home` and the old-URL redirect are dropped: see findings 9 and 10.) | Shop categories | S | none | `/shop/gift` still has no inbound link | none needed |
| SEO-60 | Replace `llms.txt` with the cleaned version: no notes, no "since 2011" unless it is on the site, `/wool-*` and guide URLs in, `/shop/<category>` out. | File upload | S | SEO-51 | `grep -i "as checked" llms.txt` still matches | none needed |
| SEO-61 | Speed: smaller grid thumbnails on `/shop`, re-export hero and product images at display size, landscape 1200 × 630 social image. Then re-run PageSpeed in the browser. | Image re-upload | M | none | PageSpeed mobile LCP on `/shop` still above 8 s | Weekly PageSpeed mobile run, three pages |
| SEO-62 | Re-run PageSpeed for the same three pages once the quota resets, so Performance has a like-for-like number. | Measurement | S | none | n/a | n/a |

Order: SEO-51 first (it decides which URLs the rest strengthens), then SEO-52, 53 and 57 before the Christmas search peak, then the rest.

## Limits of this audit

- Snapshot at 17:10 EET while another session was still making live changes (home images, `/shop` hover images, cookie bar, `llms.txt`). Findings 7, 11 and 14 may already be out of date.
- Performance is local Lighthouse only; no PageSpeed, no real-user data (traffic too low).
- Search-intent work used a web search proxy, not live Google results; ranking chances are estimates.
- The visual specialist stopped at its turn limit after taking screenshots; four mobile screenshots were reviewed by hand, desktop ones were not.
- No Search Console or analytics access in this run; indexing of the 9 new pages is not confirmed.
- Etsy order and review figures were not checked against Etsy.

## Update 21:40 EET — after the owner-approved live batches 7 to 11

**SEO Health Score: 65 / 100** (56 this morning, 61 at 17:10)

| Category | Weight | 17:10 | 21:40 | Basis |
|---|---|---|---|---|
| Technical SEO | 22% | 70 | 70 | not re-scored; nothing technical changed |
| Content quality | 23% | 55 | 58 | fresh specialist pass on a new crawl ([content-onpage.md](../../evidence/seo-reaudit-2026-11-10/findings-after/content-onpage.md)) |
| On-page SEO | 20% | 58 | 70 | same pass. Part of this gain is scoring, not site change: this pass was told to weight down the 7 `/shop/<category>` pages, because their H1, description and canonical cannot be edited on Squarespace (confirmed in the admin: no such fields) |
| Schema | 10% | 55 | 55 | not re-scored; Mareshop profiles are now out of `sameAs` |
| Performance | 10% | 61 | 61 | still not re-measured (PageSpeed quota) |
| AI search readiness | 10% | 56 | 64 | fresh specialist pass ([geo-agentic.md](../../evidence/seo-reaudit-2026-11-10/findings-after/geo-agentic.md)) |
| Images | 5% | 78 | 78 | not re-scored |

### What was changed live (logs in `evidence/seo-reaudit-2026-11-10/live-changes/`, backups in `…/backup/`)

| Batch | Change | Verified publicly |
|---|---|---|
| 7 | `/wool-sweaters`, `/wool-cardigans`, `/wool-sweater-vests`, `/wool-hats-and-scarves`: two-sentence lead, then the product grid with a price on every tile, rest of the text below. Prices are read from each product page by `live-2026-11-10-b/build_landing.py`; re-run it after any price change. | 13 / 4 / 2 / 2 priced tiles, one H1 each |
| 7 | `llms.txt`: the 7 `/shop/<category>` links removed (landing pages and guides were already listed) | 6,662 bytes |
| 7 | `/privacy-policy`: "is a handmade knitwear brand" → "is a knitwear brand" | 0 "handmade" on the page |
| 7 | Social Links: Facebook and Pinterest Mareshop profiles removed | `sameAs` = Instagram + TikTok |
| 8 | Four guides: answer in the first paragraph (52–59 words), "By Kristine … Updated 10 November 2026", question headings, one table each (size chart copied from `/size-guide`; cardigan table from the product pages) | byline and table on all four |
| 9 | Eight colour-twin products: one unique opening paragraph each, linking to its twin. Name, price, variants, images untouched. | paragraph, twin link, price and Add To Cart on all eight |
| 10 | Custom CSS: tighter cookie banner on phones. Overlay guard rules untouched. | banner 145 → 135 px, buttons 36 px |
| 11 | Footer: Facebook and Pinterest Mareshop lines removed | 0 on `/`, `/about`, `/shop` |

### Did not work or was not done

- Cookie banner: 10 px smaller, but on a 390 × 844 phone the price (y 710–741) and Add To Cart (y 757–805) are still under it on first visit. CSS alone does not fix this. It needs a shorter banner text or a different banner layout, which is an owner decision.
- Colour twins: the new paragraph lowers similarity from 0.98–0.99 to 0.77–0.86, still high, because the long description below is shared.
- Per-category SEO descriptions: Squarespace has no such field. Platform limit.
- Business name and logo in Business Information: not changed. The field holds the legal name "AUTUMN AND WOOL, SIA", which may also print on invoices and emails; changing it needs an owner check first.
- Landscape social image: no approved image.
- Christmas cut-off dates: skipped by owner choice.
- `/contact` still has one Facebook and one Pinterest Mareshop link inside the page's own block.
- `/shop/gift`: not linked, not removed.

### What would raise the score next (all need owner input or text approval)

| Lever | Category it moves | Needs |
|---|---|---|
| Home (173 words) and About (170 words): who knits, since when, how, with facts | Content, AI search | Owner facts |
| Proof for "4.9 from 1,400+ reviews, 8,000+ orders": a dated line ("as of November 2026, on Etsy") or reviews on the site | Content (trust) | Owner confirms numbers |
| Two listings with the same colour and price, 87% identical (dusty-pink raglan and dusty-pink oversized turtleneck); two near-identical shawl cardigans | Content, on-page | Owner: same product or not |
| 9 products under 300 words; shared template phrases | Content | Product text approval |
| Return wording in one form on `/faq`, `/shipping-returns`, `llms.txt`; who pays return postage | Content, AI search | Owner picks wording (policy text) |
| "Made to order" variants show as in stock in structured data | Schema, feed | Feed fix (SEO-03) |
| PageSpeed re-run, then image sizes on `/shop` | Performance | Quota reset, owner go-ahead |
| Shorter cookie banner text | Mobile conversion | Owner approves text |

## Update 2026-11-11, 09:50 EET — after live batches 12 and 13

**SEO Health Score this run: 63 / 100.** Previous runs: 56 (10 Nov morning), 61 (10 Nov 17:10), 65 (10 Nov 21:40).

The site did not get worse between 65 and 63. Every category was scored again by a fresh specialist pass on a new crawl, and two passes on the same site differ by up to 8 points per category. Read the score as "low to mid 60s" and judge progress by the counted changes below, not by the last digit.

| Category | Weight | 10 Nov 21:40 | 11 Nov 09:50 | Basis today |
|---|---|---|---|---|
| Technical SEO | 22% | 70 | 72 | fresh pass ([technical.md](../../evidence/seo-reaudit-2026-11-10/findings-1111/technical.md)); 13 of 16 findings are platform limits |
| Content quality | 23% | 58 | 55 | fresh pass ([content-onpage.md](../../evidence/seo-reaudit-2026-11-10/findings-1111/content-onpage.md)) |
| On-page SEO | 20% | 70 | 62 | same pass; stricter than yesterday's on the `/shop` pages |
| Schema | 10% | 55 | 55 | held. The fresh pass said 47, but it miscounted (it reported 0 products with a SKU and 13 price-range products; the raw data in both crawls shows 7 and 15, unchanged). Its number is not used. |
| Performance | 10% | 61 | 58 | PageSpeed web tool, one run each: mobile 48 / 64 / 48, desktop 90 / 49 / 66 ([pagespeed.md](../../evidence/seo-reaudit-2026-11-10/findings-after/pagespeed.md)). Single runs swing a lot: the product page went 72 → 48 on mobile with no change to it. |
| AI search readiness | 10% | 64 | 63 | fresh pass ([geo-agentic.md](../../evidence/seo-reaudit-2026-11-10/findings-1111/geo-agentic.md)) |
| Images | 5% | 78 | 82 | manager's count: social image now 1200 × 630 on all 27 non-product pages |

### Changed live on 11 Nov (logs: `live-changes/batch12-text.md`, `batch13-banner-image-contact.md`)

| Change | Verified publicly |
|---|---|
| One return wording on Home, `/faq`, `/shipping-returns`, 4 landing pages, `/wool-gifts`, `llms.txt`: "Unworn, unwashed items in their original condition can be returned within 14 days of delivery." | present on all, "unused items" gone |
| Home: Etsy line dated "as of November 2026"; one new paragraph (where made, fibres, size guide, returns). Home 173 → 227 words. | yes |
| About: process sentence in the lead; new paragraph with the Etsy history, dated and attributed to Etsy; links to shop and shipping | yes |
| `/contact`: Pinterest and Facebook Mareshop links removed | 0 left sitewide |
| Cookie banner text shortened to one sentence with Privacy Policy and Cookie Policy links. Buttons and consent settings unchanged. The Imprint link that was in the old text is no longer in the banner (Imprint stays in the footer). | banner 135 → 93 px on a 390 × 844 phone; price is now clear; Add To Cart is still overlapped by about 54 px |
| Site-wide social image: 1200 × 630 crop of the current home hero photo | `og:image` 1200 × 630 |
| Logo alt shows `Autumn &amp;amp; Wool`: site title is correct in settings, the double escape is Squarespace's. Not fixable. | n/a |

### Why the score will not move much further from page edits

1. Platform limits now make up most of what is left in Technical, Schema and On-page: the 7 `/shop/<category>` pages, `/home` in the sitemap, security headers, product schema fields, breadcrumbs, Article markup, platform JavaScript.
2. Performance on mobile is set by Squarespace's own JavaScript (about 950 KiB unused, 1.2–1.9 s render-blocking). The part that can change is images: `/shop` loads 2.4 MB of them on mobile.
3. Content is capped by facts only the owner has: fibre percentages on products that say only "wool", distinct text per colour, a longer maker story, product reviews on the site.

### What is left that can be done, with what it needs

| Item | Category | Needs |
|---|---|---|
| "Material: wool" with no fibre % on some products (the FAQ promises the exact fibre on every page) | Content | Owner: fibre per product |
| Merino Raglan Cardigan page has no returns line, and its made-to-order colours fall under "non-returnable" | Content | Owner: confirm rule, then one sentence |
| Six product pairs still 85–89% identical | Content | Owner: what differs per colour (photos, styling) |
| `/cookie-policy` has no H1 (its title is an H2) | Technical, On-page | Go-ahead; one heading change |
| `/shop/gift`: link it or remove the category | Technical | Owner choice |
| Brand name, logo and a structured address in Business Information | Schema, AI search | Owner check that the legal name on invoices is not affected |
| SKU on the 15 variant products | Schema | Owner SKUs |
| `/privacy-policy` says "sustainable garments" with no evidence | Content | Owner: keep with proof, or drop |
| Smaller grid images on `/shop` | Performance | Design choice (fewer products per page or smaller thumbnails) |
| Add To Cart still under the cookie banner on first phone visit | Conversion, not score | Banner layout choice, or a shorter product photo on phones |

## Update 2026-11-11, 11:50 EET: PageSpeed fixes on the home page (batch 14)

Asked for: fix Performance and Agentic browsing in PageSpeed Insights, mobile and desktop.

| Item | Before (10:45) | After | Status |
|---|---|---|---|
| Agentic browsing | 2/3 | 3/3 (mobile and desktop, 3 runs) | fixed |
| Accessibility | 96 | 100 | fixed (same cause) |
| Desktop Performance | 74 | 89, 72, 91 (3 runs) | better on 2 of 3 runs; home image bytes 601 KB to 289 KB |
| Mobile Performance | 59 | 54, 50, 47 (3 runs) | not improved; lab noise (48 at 08:22 before any change today) |

What changed: logo image is hidden visually instead of with `display:none`, so the logo link has a name; home images got `srcset` and `sizes`. Details and measurements: `evidence/seo-reaudit-2026-11-10/live-changes/batch14-pagespeed-logo-images.md`.

What is left for mobile: Squarespace's own CSS and scripts (not editable on this plan) and reCAPTCHA from the footer newsletter form. Moving that form to its own page is the one remaining lever and is the owner's call.

## Update 2026-11-11, 12:40 EET: PageSpeed round 2 (batches 15-17)

Owner approved three more steps. All live.

| Step | Change | Result |
|---|---|---|
| Newsletter form | Moved from the footer of every page to its own page `/newsletter`; footer has a "Join our newsletter" link | reCAPTCHA no longer loads on home or product pages (0 requests) |
| Font | Site Styles "Miscellaneous" font: Pragmatica Extended -> DM Sans bold | Adobe Typekit no longer loads (0 requests) |
| Hero image | Smaller file on lower-density phones | 102 KB -> 40 KB on those phones |

Home, PageSpeed Insights, three runs each:

| | Before (10:45, one run) | After (3 runs) | Median |
|---|---|---|---|
| Mobile Performance | 59 | 55, 78, 60 | 60 |
| Desktop Performance | 74 | 84, 91, 98 | 91 |
| Best Practices | 96 | 100 | 100 |
| Accessibility | 96 | 100 | 100 |
| Agentic browsing | 2/3 | 3/3 | 3/3 |

Mobile numbers swing run to run (55 to 78), so the mobile gain is not firm. What is left on mobile is Squarespace's own CSS and scripts, which cannot be changed on this plan.

Open cosmetic items: `/newsletter` says nearly the same sentence twice; the footer has an empty area where the form was; small uppercase labels now use DM Sans. Not tested: a real signup on `/newsletter`.

Details: `evidence/seo-reaudit-2026-11-10/live-changes/batch15-newsletter-page.md`, `batch16-hero-and-results.md`, `batch17-misc-font.md`.

## Update 2026-11-11, 13:25 EET: mobile 90 attempt (batches 18-19)

Asked for: mobile Performance 90. Not reached.

- Change made: on phones the hero text block fills the first screen so the heading, not the photo, is the largest element. PageSpeed confirms the heading is now the LCP element.
- Result: mobile 73, 76, 75, 70 then 60, 59, 78 across seven runs; before it was 55, 78, 60, 77. No measurable gain.
- Why 90 is out of reach: first paint is 2.6 s in every run, from Squarespace's own CSS; blocking time is Squarespace scripts plus Google Analytics. Best case with those fixed is about 89.
- Desktop: 84 to 96 across six runs.

Details: `evidence/seo-reaudit-2026-11-10/live-changes/batch18-19-phone-hero-lcp.md`.

## Update 2026-11-11, 14:10 EET: "mobile 71 to 90" plan, phases 0-3 (batches 20-21)

Not reached. No net live change in this round.

- Measured locally with Lighthouse (5 runs, median 76-82 depending on the hour).
- Cause of the late "largest paint": the heading really paints 20-160 ms after first paint; the test's simulator inflates that to 1-8 s, differently each run. The hero sits late in Squarespace's HTML, so the header paints first. Not controllable.
- Tried preloading the heading font: no measurable effect, reverted.
- Blocking time: customer-account scripts about 10 ms (skipped); Google Analytics about 2 points on PageSpeed (kept, owner decision).
- Final pagespeed.web.dev: mobile 56, 71, 61; desktop 92, 81, 85.
- 90 on mobile needs first paint under about 1.8 s; Squarespace's own CSS gives 2.6 s. Only a replatform changes that.

Details: `evidence/seo-reaudit-2026-11-10/live-changes/batch20-21-mobile-90-phases.md`.

