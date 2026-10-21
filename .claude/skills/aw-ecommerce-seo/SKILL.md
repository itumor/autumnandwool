---
name: aw-ecommerce-seo
description: Use when doing SEO for autumnandwool.com or Pinterest — keyword research, Search Console review, title/meta/H1 fixes, product or category page SEO, schema/structured data checks, llms.txt, image alt text, Pinterest boards, pins and rich pins.
---

# aw-ecommerce-seo — site SEO + Pinterest for Autumn & Wool

Owner of output: SEO/Pinterest specialist agent (`aw-seo-marketplace`); the CRO agent uses it for PDP SEO fields.

## Known state (handbook, 19 Oct)
- robots.txt, sitemap.xml, canonical and Product schema verified correct. Do not "fix" them without new evidence.
- GSC 90 days: 11 clicks / 388 impressions / 2.8% CTR / avg pos 14.1. 37 known, 11 indexed.
- Query clusters with headroom: "oversized merino wool sweater" (pos 27), "timeless knitwear" (5.9),
  "wool size chart" (44).
- QA issues: Shop page has no H1; home has 2 H1s; vest `<title>` ≠ H1; size guide title ends "– Shop Now";
  thin categories (Beanies 1, Sets 1). Long legacy Etsy-style URL slugs (`/shop/p/p/...`) — do **not** propose
  slug changes without a redirect plan the owner approves (lost links, feed links break).
- Product data frozen → titles, descriptions, SEO fields, alt text are proposals.

## Procedure — site
1. **Indexation first.** From the owner's GSC export (or her screenshot): pages not indexed and why. Squarespace
   handles sitemap; your fixes are content/linking (thin pages, duplicate descriptions across colour twins).
2. **Quick wins = positions 8–20.** List queries in that band, map each to one target page (no two pages for
   one query), propose title/meta/H1/first-paragraph changes.
3. **On-page per target page:** one H1; title ≤ 60 chars with the query + brand; meta ≤ 155 chars; query in
   first 100 words naturally; descriptive alt text per image ("Black merino raglan cardigan, front, worn open");
   internal links from home/category/size guide.
4. **Duplicate copy across colour products** (e.g. Side-Slit Camel vs Light Grey, Stand-Collar Beige vs Blue):
   propose a distinct opening line per colour; keep shared specs.
5. **Category pages:** propose 60–120 word intro (what, fibres, fit range) for sweaters/cardigans/vests; merge or
   hide categories with ≤ 1 product (owner decision).
6. **Schema:** WebFetch cannot see JS-injected JSON-LD — never report "no schema" from a fetch. Ask for a Google
   Rich Results Test result (search.google.com/test/rich-results) on the 5 priority PDPs. Product needs name,
   image, offers(price, priceCurrency, availability). Review/aggregateRating markup only for real on-site reviews.
7. **llms.txt:** keep product list, prices and policy lines in sync with the live site; propose diffs.
8. **Content ideas** tied to clusters: wool size chart guide, how to wash merino, oversized vs regular fit.
   Drafts follow `aw-brand-voice` and go to `business-os/proposals/`.

## Procedure — Pinterest (intent discovery channel, README §4)
- Keyword research: Pinterest search-bar suggestions and Pinterest Trends for seeds (merino cardigan, oversized
  wool sweater, sweater vest outfit, minimalist knitwear, wool beanie). Record in a keyword sheet.
- Profile: business account; display name with a keyword ("Autumn & Wool | Wool Knitwear"); claim the website.
  Footer link still points to legacy `mmareshop` — owner decision to switch.
- Boards: one board per real search theme (e.g. "Oversized wool sweaters", "Sweater vest outfits",
  "Merino cardigans"), keyword in title + 1–2 sentence description.
- Pins: 2:3 vertical (1000×1500), real product photos only (no AI-altered garments); title ≤ 100 chars,
  description ≤ 500 chars, keyword first, link to the exact PDP with UTM
  `?utm_source=pinterest&utm_medium=social&utm_campaign=<board>`.
- Product rich pins read the PDP's Open Graph/schema.org Product + Offer markup; Squarespace emits it. Catalog
  (feed upload) is the route to shoppable product pins — reuse the Merchant Center feed only after variant
  photos are fixed (`aw-merchant-feed-qa`). Owner applies; you prepare.
- Cadence suggestion: 5–10 fresh pins/week from the content batch; review monthly on outbound clicks and
  sessions in GA4 (source = pinterest), not impressions.

## Output
`business-os/seo/<YYYY-MM-DD>-seo-review.md`:
```
## Executive summary (top 3 issues, quick wins)
## Findings: Issue | Impact | Evidence | Fix | Layer (copy/native/asset/owner) | Priority
## Query → page map (query, pos, impressions, target URL, proposed title/meta)
## Proposals (diffs) ## Pinterest plan (boards, 10 pin briefs, keyword sheet)
## Unverified
```

## Guardrails
- No live edits, no account logins, no posting pins. No link schemes, no bought links, no doorway pages.
- No fake reviews or rating markup; no claims beyond `aw-product-page-copy` fact sources.
- Do not change URL slugs, navigation or redirects without an owner-approved redirect list.

## Sources
- coreyhaines31/marketingskills `skills/seo-audit/SKILL.md`, `skills/schema/SKILL.md` —
  https://github.com/coreyhaines31/marketingskills — MIT. Taken: priority order (crawl → technical → on-page →
  content → authority), pos 8–20 quick wins, Issue/Impact/Evidence/Fix/Priority format, ecommerce checks
  (thin categories, duplicate descriptions), "fetch can't see JS schema" caveat, Product schema minimum.
- finsilabs/awesome-ecommerce-skills `ecommerce-seo` — https://github.com/finsilabs/awesome-ecommerce-skills —
  MIT. Compared; platform-implementation focused (Shopify/Woo code), not adopted.
- nexscope-ai/ecommerce-skills `product-page-seo` — https://github.com/nexscope-ai/ecommerce-skills — MIT per
  repo; compared, beta, overlapped with above.
- Pinterest Help, Rich Pins — https://help.pinterest.com/en/business/article/rich-pins — cited (metadata, catalogs).
- Shopify blog, Pinterest SEO — https://www.shopify.com/blog/pinterest-seo — cited (title/description limits,
  2:3 ratio, Trends, board naming). Own words.
