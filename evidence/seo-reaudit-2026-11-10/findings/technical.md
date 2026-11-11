# Technical SEO re-audit: autumnandwool.com (2026-11-10)

Scope: 49 pages from the shared crawl (`evidence/seo-reaudit-2026-11-10/crawl/`), sitemap, robots.txt, llms.txt, probes.txt, plus 9 live curl requests (browser UA, 1s apart). Read-only. Platform: Squarespace 7.1.

Technical score: **70 / 100**. Rationale: no noindex, no broken internal links, HTTPS and redirects clean, SSR content and Product schema present. Deductions for canonical/sitemap conflicts on 8 URLs, the /home duplicate, missing H1s and meta descriptions on category pages, and a 404 with no redirect for the old single-/p/ product URL.

## Findings

| ID | Severity | Scope | Finding | Evidence |
|---|---|---|---|---|
| T-01 | High | Platform-limited? (see note) | 7 category pages canonicalise to `/shop`, so they drop out of the index as separate landing pages. | `https://www.autumnandwool.com/shop/cardigans`, `/shop/beanies--hats`, `/shop/gift`, `/shop/sets`, `/shop/sweaters`, `/shop/vests`, `/shop/winter-wool-gifts`: `<link rel="canonical" href="https://www.autumnandwool.com/shop"/>` |
| T-02 | High | Fixable in Squarespace | `/home` is in the sitemap (priority 1.0, lastmod 2026-01-28) but canonicalises to `/`. Sitemap sends a conflicting signal. | `https://www.autumnandwool.com/home`: `<link rel="canonical" href="https://www.autumnandwool.com"/>`; sitemap `<loc>https://www.autumnandwool.com/home</loc>` |
| T-03 | High | Fixable in Squarespace | `/` is missing from the sitemap, and `/home` is a full duplicate of `/` (same title, same body, 0 internal inbound links). Fix by a 301 `/home` -> `/` in URL Mappings, which also clears T-02. | `https://www.autumnandwool.com/`: title `Autumn &amp; Wool \| Wool sweaters and cardigans from Riga`; `/home` returns the same title, 200 live. Root absent from sitemap.xml |
| T-04 | Medium | Fixable in Squarespace | Orphan pages: `/shop/gift` has 0 internal inbound links from the 49 crawled pages (only self-link), and `/home` has 0. | `https://www.autumnandwool.com/shop/gift` (only referenced inside its own HTML) |
| T-05 | Medium | Fixable (content) | 8 pages have no H1: `/shop`, the 7 category pages, and `/cookie-policy`. Category pages use `h2.nested-category-title` only. | `https://www.autumnandwool.com/shop`: no `<h1>` in raw HTML; `https://www.autumnandwool.com/cookie-policy`: no `<h1>` |
| T-06 | Medium | Fixable in Squarespace | 7 category pages have a `<meta name="description">` with empty content. | `https://www.autumnandwool.com/shop/cardigans`: `<meta name="description" content="">` (length 0; same for beanies--hats, gift, sets, sweaters, vests, winter-wool-gifts) |
| T-07 | Medium | Fixable (redirect) | Old single-/p/ product URL returns 404 with no redirect to the live /shop/p/p/ URL. Indexing history unverified (no GSC access). | `https://www.autumnandwool.com/shop/p/hand-knitted-merino-wool-raglan-sweater-dusty-pink-oversized-jumper`: `HTTP/2 404`. Live target `/shop/p/p/...dusty-pink-oversized-jumper` returns 200 with self canonical |
| T-08 | Medium | Platform, partly fixable | Product URL structure is inconsistent: 20 products under `/shop/p/p/`, 2 under `/shop/p/` (`oversized-merino-wool-v-neck-sweater-vest`, `autumn-and-wool-digital-gift-card`). Several slugs carry duplicate-style suffixes (`-1`) and keyword-stuffed tails (e.g. `...sizes-sl-12-679428`). | `https://www.autumnandwool.com/shop/p/p/merino-wool-turtleneck-sweater-womens-knit-pullover-soft-warm-lightweight-minimalist-sustainable-knitwear-sizes-sl-12-679428` |
| T-09 | Medium | Platform, not fixable | Sitemap lastmod is not a usable freshness signal: 27 of 48 entries are stamped `2026-11-10` (today, the crawl date). Changefreq `daily` and priority values are ignored by Google. | `https://www.autumnandwool.com/sitemap.xml`: `<lastmod>2026-11-10</lastmod>` x27; `/home` `<lastmod>2026-01-28</lastmod>` |
| T-10 | Medium | Platform, not fixable | Security headers: HSTS is `max-age=15552000` with no `includeSubDomains` or `preload`. No `Content-Security-Policy`, `Referrer-Policy`, or `Permissions-Policy` on any of the 49 responses. `X-Frame-Options: SAMEORIGIN` and `nosniff` are present. | All `*.headers` files, e.g. `https://www.autumnandwool.com/`: `strict-transport-security: max-age=15552000` |
| T-11 | Medium | Platform, not fixable (verify) | Possible CWV risk from source only (no field data; PSI keyless quota exhausted). Product pages: 60 `<img>`, 0 with `loading="lazy"`, 32 without `width` attribute. `/shop`: 971 KB raw HTML, 203 images, 39 scripts. Homepage: 20 images, none with `width`. | `https://www.autumnandwool.com/shop/p/p/black-merino-wool-cardigan-...-cardigan-1` (60 img, lazy=0); `/shop` (971,449 bytes) |
| T-12 | Medium | Fixable in Squarespace | Llms.txt and sitemap disagree with canonicals: llms.txt lists `/shop/cardigans`, `/shop/sets`, `/shop/sweaters`, `/shop/vests`, `/shop/beanies--hats` as key pages, yet those canonicalise to `/shop`. | `https://www.autumnandwool.com/llms.txt` "Pages" section |
| T-13 | Low | Platform | Titles over 60 characters on category pages (80-93 chars, the store suffix is repeated). Likely truncated in SERPs. | `https://www.autumnandwool.com/shop/winter-wool-gifts`: `Winter Wool Gifts &mdash; Shop wool sweaters, cardigans &amp; accessories \| Autumn &amp; Wool` (93 chars) |
| T-14 | Low | Fixable (content) | Mixed content: 4 pages have `src="http://static1.squarespace.com/..."` image sources. `/imprint` links to `http://www.autumnandwool.com` (single 301 hop). | `https://www.autumnandwool.com/wool-cardigans`, `/wool-sweaters`, `/wool-sweater-vests`, `/wool-hats-and-scarves`; `https://www.autumnandwool.com/imprint` |
| T-15 | Low | Platform | Slug/title mismatch on some products: `hand-knitted-lambswool-sweater-womens-winter-knitwear-1` is titled "Lambswool Raglan Crew Sweater, Green", and `cozy-and-sustainable-...-for-women` is titled "...Brown". | Product `<title>` tags on the two pages above |
| T-16 | Info | Platform | No `hreflang` on any page (single-language site, `lang="en-US"`). Not a defect, but the store is Riga-based with EUR pricing. Hreflang checks deferred to seo-hreflang. | `<html lang="en-US">` on 49/49 |

### Verified OK (no finding)
- Status: 49/49 pages return 200 (crawl). `/this-is-404-probe` returns 404. `/blog` returns 404 (no page). `/cart` returns 200 with `<meta name="ROBOTS" content="NOINDEX">` (intentional).
- Canonicals: 41 pages self-canonical (`/` counts as self). Only T-01 / T-02 deviate. Root canonical is `https://www.autumnandwool.com` (no trailing slash, consistent).
- Indexability: no `meta robots` noindex and no `X-Robots-Tag` on any of the 49 pages.
- Redirects: `http://autumnandwool.com/`, `https://autumnandwool.com/`, `http://www.autumnandwool.com/` each 301 directly to `https://www.autumnandwool.com/` (single hop). HSTS on every page.
- Titles: present and unique on all pages except `/` and `/home` (T-03). Meta descriptions have content on 42 of 49 pages (the 7 empty ones are in T-06). One is short, 17 chars, on `/shop/p/p/merino-wool-turtleneck...-679428` (`Lightweight women...`).
- Viewport: `width=device-width, initial-scale=1` on 49/49.
- Internal links: no broken internal hrefs in crawled HTML apart from `/cart` (200, noindex). 212 anchor/empty hrefs are fragment links.
- Sitemap: well-formed XML, 48 URLs, all URLs resolve in crawl set. Missing from sitemap: `/` only. Extra: `/home` (T-02) and 7 canonicalised category pages (T-01).
- Robots: 200, declares `Sitemap: https://www.autumnandwool.com/sitemap.xml` (live sitemap 200, text/xml). Disallows only `/config`, `/search`, `/account`, `/api/`, `/static/`, and query-param variants. No disallow on any product or content URL. AI crawlers (GPTBot, ClaudeBot, etc.) are not blocked from public pages.
- llms.txt: 200 live, no `/home` reference.
- JS rendering: SSR. Raw HTML word counts 198-949. EUR prices present in raw HTML on 22/22 product pages. No JS-only content identified.
- Structured data (raw HTML): WebSite, Organization, LocalBusiness on 49/49 pages; Product on 22 product pages; AggregateOffer on 15, Offer on 7.
- Mixed content beyond T-14: none for scripts or stylesheets.

### Not verified
- Google Search Console / index coverage: cannot confirm whether the 8 non-canonical URLs or the old single-/p/ URL are indexed or linked externally.
- Field CWV (LCP, INP, CLS): PSI keyless quota exhausted, no CrUX access. T-11 is source-inspection only.
- Touch target sizes, tap spacing, and rendered layout: not measurable from HTML alone.
- IndexNow: not checked in this pass (out of scope for this crawl).
- Whether Squarespace's page SEO panel can override category canonicals (T-01) and hide `/home` from the sitemap (T-02/T-03): needs a check in the admin UI. Recommended first step for T-03 is a 301 URL mapping `/home` -> `/`.
- Whether `/shop/gift` is reachable from the nav menu or footer drop-down rendered client-side (crawl found no inbound link in static HTML).

Live requests used: 9 of ~10 budget (4 header probes, 404 body, sitemap, robots, canonical on /shop/p/p dusty-pink, /home canonical, /cart HTML).
