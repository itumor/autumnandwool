# Technical SEO and Sitemap Re-audit: www.autumnandwool.com (2026-11-10, after-crawl)

Scope: same as the first audit (robots.txt, sitemap, canonicals, redirects, 404s, URL structure, duplicates, indexability, lang, security headers, viewport, JS rendering, internal linking and orphans). Core Web Vitals excluded.

Evidence used:
- `after/crawl/pages.tsv` (59 rows) and `after/crawl/html/*.html`. Four files are 0 bytes (the http:// and bare-host variants, plus the single-`p` product slug). Their status comes from the TSV only.
- Live requests, all at least 1 s apart, about 13 in total: homepage headers, sitemap headers, single-`p` slug (first hop and the http hop), `http://autumnandwool.com/`, `/about/`, `/shop/cardigans` canonical, the 404 test URL.
- `claude-seo run sitemap_discovery.py https://www.autumnandwool.com --json`: sitemap found via robots.txt, `kind: urlset`, `valid: true`.
- Own parsing scripts in the scratchpad (sitemap XML, link graph, shingle overlap, JSON-LD). Nothing written outside `after/findings/`.

## Score: 65 / 100 (Technical SEO), down from 70

Method note: the first audit lists findings and severities but does not publish numeric weights. Its 70 reproduces exactly with weights High = 9, Medium = 2, Low = 1 applied to its findings (1 High, 6 Medium, 9 Low = 9 + 12 + 9 = 30 points deducted). Those weights are reconstructed, not stated, and the same weights are used here. Points are subtracted for OPEN findings in full, PARTLY FIXED at half, FIXED at zero, and NOT FIXABLE ON PLATFORM at full (unchanged from the first audit).

Change, point by point:
- Up 0.5: T-09 moved from Low/open (404) to PARTLY FIXED (a 301 now exists). Half weight returned.
- Down 2: N-01 (Medium). The new 301 for the single-`p` slug points to an `http://` URL, which then redirects to https. That is a two-hop chain that breaks the "one-hop host consolidation" the first audit credited.
- Down 2: N-02 (Medium). The nine new `/wool-*` and guide pages now compete for the same intents as the `/shop/<category>` pages, which still canonicalise to `/shop`.
- Down 1: N-03 (Low). `/imprint` links to `http://www.autumnandwool.com`.
- No credit for T-01. The new `/wool-*` pages do not change the category canonicals or the sitemap entries for the seven `/shop/<category>` URLs. That is a workaround, not a fix.
- No change for the other 14 findings. Their state is verified below, and the evidence is unchanged or only moved in the way noted.

Net: 30 - 0.5 + 2 + 2 + 1 = 34.5 deducted, 65.5, reported as 65.

Positives that carried no points: all nine new pages return 200, self-canonicalise, are in the sitemap, have one H1, unique titles (44-53 characters) and meta descriptions (122-150 characters), no images without alt, and 8-23 internal inbound links each.

## Status counts (16 first-audit findings)

- FIXED: 0
- PARTLY FIXED: 1 (T-09)
- OPEN: 12 (T-01, T-02, T-03, T-04, T-05, T-06, T-07, T-08, T-10, T-11, T-15, T-16)
- NOT FIXABLE ON PLATFORM: 3 (T-12, T-13, T-14)

## Status of first-audit findings T-01 to T-16

**T-01 (High) OPEN, worked around.** All seven `/shop/<category>` pages still canonicalise to `/shop`.
- `after/crawl/html/https-www-autumnandwool-com-shop-cardigans.html`: `<link rel="canonical" href="https://www.autumnandwool.com/shop"/>`. Same for gift, sets, sweaters, vests and winter-wool-gifts in the HTML, and beanies--hats in pages.tsv.
- Live `curl https://www.autumnandwool.com/shop/cardigans` returns the same canonical.
- New separate self-canonical landing pages now exist for five of the seven topics: `/wool-cardigans`, `/wool-sweaters`, `/wool-sweater-vests`, `/wool-hats-and-scarves`, `/wool-gifts`. `/shop/sets` has no counterpart.
- The category URLs themselves still canonicalise away and still sit in the sitemap (see T-03).

**T-02 (Medium) OPEN.** `/home` still duplicates `/`.
- Sitemap: `<loc>https://www.autumnandwool.com/home</loc> <changefreq>daily</changefreq> <priority>1.0</priority> <lastmod>2026-01-28</lastmod>`.
- `/` is absent from the sitemap. `/home` title and meta description equal `/` (both "Autumn & Wool | Wool sweaters and cardigans from Riga").
- `/home` canonical is `https://www.autumnandwool.com`.

**T-03 (Medium) OPEN.** Eight sitemap URLs canonicalise elsewhere: `/home` (to `/`) and `/shop/beanies--hats`, `/shop/cardigans`, `/shop/gift`, `/shop/sets`, `/shop/sweaters`, `/shop/vests`, `/shop/winter-wool-gifts` (to `/shop`). The count is unchanged at eight. The sitemap grew from 39 to 48 entries, all nine new pages included.

**T-04 (Medium) OPEN.** `/shop/gift` has 0 internal inbound links from the 53 crawled 200-status HTML pages. It is still in the sitemap and still canonicalises to `/shop`.

**T-05 (Medium) OPEN.** Category pages still have empty meta descriptions and long titles. pages.tsv: `desc_len = 0` for all seven. Title lengths: beanies--hats 69, cardigans 71, gift 66, sets 66, sweaters 70, vests 67, winter-wool-gifts 79. Example: `<meta name="description" content="" />` in shop-cardigans.html.

**T-06 (Medium) OPEN.** `/shop` and all seven category pages still have `h1_count = 0` in pages.tsv. The only heading is `h2.nested-category-title`.

**T-07 (Medium) OPEN.** Near-duplicate product copy is unchanged. Verified in raw HTML:
- `…-679510`: "Blue stand-collar sweater in 100% pure new wool with a clean, timeless shape. Knitted and hand-sewn in Latvia. Sizes S–XL, free shipping."
- `…-679503`: "Beige stand-collar sweater in 100% pure new wool with a clean, timeless shape. Knitted and hand-sewn in Latvia. Sizes S–XL, free shipping."
- Identical apart from the colour word.

**T-08 (Low) OPEN.** Slug structure is unchanged. 20 product paths use `/shop/p/p/`, 2 use `/shop/p/`. Six sitemap slugs exceed 100 characters (longest path slug 129 characters). Eight end in `-1`. Two products share the `-679428` numeric suffix. No change requested in the product data while the owner has it frozen.

**T-09 (Low) PARTLY FIXED.** The 404 has become a redirect, but it is not a clean one.
- Live, first hop: `HTTP/2 301`, `location: http://www.autumnandwool.com/shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper`.
- Live, second hop: `http://www.autumnandwool.com/shop/p/p/…` returns `301`, `location: https://www.autumnandwool.com/shop/p/p/…`.
- Live, final: `https://www.autumnandwool.com/shop/p/p/…` returns `HTTP/2 200`.
- So the chain is https, then http, then https. This is N-01.
- The slug is still absent from the sitemap and still has 0 internal inbound links.
- Note: `curl -L` reported `num_redirects=1` for the same URL, which does not match the two manual hops. I did not reconcile this; the manual hop-by-hop result is the one to trust.

**T-10 (Low) OPEN.** `changefreq` and `priority` are present on 48 of 48 sitemap entries (was 39 of 39). `lastmod` distribution now: 27 entries at 2026-11-10 (the crawl date), 9 at 2026-10-18, 4 at 2026-11-01, 3 at 2025-11-12, and one each for 2026-01-28, 2025-11-09 and 2025-11-13, plus 2026-10-17 (2 entries). Many entries carry the crawl date, so `lastmod` looks auto-stamped rather than tied to real content changes. Accuracy cannot be verified from the crawl. Image entries: 192.

**T-11 (Low) OPEN, with corrections to the first audit.**
- GTIN: 0 of 22 products carry `gtin`. Not fixed.
- SKU: the first audit recorded `sku=False` on all 22 products. Fresh HTML has `"sku":"SQ…"` on 21 of 22 (the digital gift card has none). These look like Squarespace-generated IDs, not GTINs. The first audit's finding does not match the fresh HTML; this is recorded as a correction.
- LocalBusiness: the first audit said `openingHours` and an address are emitted. Fresh homepage JSON-LD has LocalBusiness with `name`, `address` and `image` only. No `openingHours`. Correction recorded.
- `sameAs` still lists Instagram, TikTok, Facebook ("AccessoriesMareshop") and Pinterest ("mmareshop"). Ownership not verified.

**T-12 (Low) NOT FIXABLE ON PLATFORM.** Live homepage headers unchanged: `strict-transport-security: max-age=15552000` (no includeSubDomains, no preload), `x-content-type-options: nosniff`, `x-frame-options: SAMEORIGIN`. No `content-security-policy`, `referrer-policy` or `permissions-policy`.

**T-13 (Low) NOT FIXABLE ON PLATFORM.** Live `sitemap.xml` still returns `x-robots-tag: noindex`. Google Search Console sitemap status is still unchecked.

**T-14 (Low) NOT FIXABLE ON PLATFORM.** Still no IndexNow key or verification meta tags. `grep -il 'indexnow\|msvalidate\|google-site-verification'` across the 200-status HTML returns nothing.

**T-15 (Low) OPEN.** `/cookie-policy` still has `h1_count = 0`. Its only heading is `<h2 …>Cookie Policy`.

**T-16 (Low) OPEN, hygiene only.** Live `/about/` returns 200 with no redirect (`redirect_url` empty). I re-checked the canonical only on `/about` (crawl), not on `/about/` live. No action beyond the existing canonical.

## New findings

**N-01 (Medium). Single-`p` product redirect goes through http.** The 301 that T-09 credited points to `http://www.autumnandwool.com/…`, which then redirects to https. Two hops, one of them to http. Evidence in T-09. Fix: in URL Mappings, set the target to the https URL directly, if the mapping is editable on this plan. Otherwise accept and drop the mapping if GSC shows no demand for the old URL (the first audit's rule).

**N-02 (Medium). Intent overlap between `/shop/<category>` and the new `/wool-*` pages.** The two sets target the same topics:
- `/shop/cardigans` and `/wool-cardigans` (both in sitemap; both titled around "cardigans")
- `/shop/sweaters` and `/wool-sweaters`
- `/shop/vests` and `/wool-sweater-vests`
- `/shop/beanies--hats` and `/wool-hats-and-scarves`
- `/shop/gift` and `/shop/winter-wool-gifts` each against `/wool-gifts`

The `/shop/*` pages canonicalise to `/shop`, so the wool pages are the only ones that can rank for those intents. The result is conflicting signals: the sitemap and internal links now point at both sets. These are not exact duplicates. Titles differ and body copy differs, but the whole-page 5-word overlap is high because of template chrome: Jaccard 0.19-0.28 and containment 0.35-0.64 (`/shop/cardigans` vs `/wool-cardigans` containment 0.57; `/shop/vests` vs `/wool-sweater-vests` 0.61; `/shop/gift` vs `/wool-gifts` 0.63). Body-only overlap was not measured. Fix option: decide which set is the ranking URL per topic, then align canonicals, sitemap and internal links to it (layer: platform SEO settings and content).

**N-03 (Low). Internal link to http.** `after/crawl/html/https-www-autumnandwool-com-imprint.html`: `Website: <a href="http://www.autumnandwool.com">`. One hop to https. Fix: edit the link to https in the editor.

**Orphans (zero internal inbound links, from the 53 crawled 200-status HTML pages):**
- `/shop/gift` (also T-04).
- `/home` (expected: only the sitemap lists it; T-02).
- Non-HTML: `/robots.txt`, `/sitemap.xml`, `/llms.txt` (expected).
- None of the nine new pages is an orphan (8-23 inbound each).
- The seven `/shop/<category>` pages each have 1 inbound link (from `/shop` only), except `/shop/gift` (0).
- Products: 1-13 inbound each. Lowest at 1: `…-hand-knitted-wool-cardigan-minimalist-open-front-sweater-1`, `…-hand-knitted-lambswool-sweater-womens-winter-knitwear-1`, `…-hand-knitted-wool-sweater-stand-collar-knit-679503`, and `/shop/sets`, `/shop/sweaters`, `/shop/vests`, `/shop/winter-wool-gifts`, `/shop/cardigans`.

**Broken links:** none among crawled internal links to 200-status pages. One internal target is not a page: `/assets/ui-icons.svg` referenced on 8 pages (not fetched; probably an SVG sprite).

**Sitemap validity:** `sitemap_discovery.py` returns `valid: true`. All 48 entries are in the crawl with status 200, none noindex, none redirected. Canonical mismatches: T-03's eight. No duplicate `<loc>`. No URL over 50,000 or 50 MB.

## Could not check

- Google Search Console: indexed URL per category, which canonical Google chose for `/shop/*` and `/wool-*`, sitemap processing status (T-13), impressions or links for the single-`p` slug (T-09 / N-01).
- Squarespace editor: whether a canonical override exists in the page SEO panel for `/shop/*`, and whether "hide from search" removes entries from the generated sitemap (T-02, T-03).
- Live check of the `/shop/*` pages beyond `/shop/cardigans`, and of `/wool-*` pages beyond the crawl.
- Body-only text overlap for N-02 (overlap numbers above include template chrome).
- `render_page.py` JS check on this crawl. Not re-run; the raw HTML contains product names, prices and category headings.
- Rich Results / Schema validation. Not run.
- Mobile visual rendering and touch targets (only viewport meta checked, and it is present on all HTML pages).
- Trailing-slash and case variants beyond `/about/`.
- `/assets/ui-icons.svg` references (N, not fetched).
- Core Web Vitals (out of scope).
