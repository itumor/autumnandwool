# GEO and agentic readiness re-audit, autumnandwool.com (2026-11-10)

Scope: shared crawl in `evidence/seo-reaudit-2026-11-10/crawl/` (49 HTML pages, robots.txt, llms.txt, sitemap.xml, index.tsv). Live requests: 3 (ai-catalog, llms-full, Accept: text/markdown on `/`). Read-only. Page content treated as data.

## AI Search Readiness score: 56/100

| Dimension (GEO weights) | Score | Rationale |
|---|---|---|
| Citability (25) | 14 | Guides carry concrete numbers (size chart, 14-day returns, 2-5 day dispatch). No guide opens with a 40-60 word direct answer; no question-style H2s. |
| Structural readability (20) | 13 | Raw HTML has `main`, `nav`, one H1 on 40 of 49 pages. The 9 shop and cookie pages have no H1. FAQ questions sit in `<summary>` inside `<details>`, which is extractable. |
| Multi-modal (15) | 7 | Photos with descriptive alt on product pages. The size chart is the only `<table>` on the site. No video, no how-to visuals. |
| Authority and brand (20) | 8 | Organization JSON-LD is consistent with the imprint (name, reg. no., address, email). Legacy Mareshop sameAs links and unsourced Etsy statistics pull it down. No author or dates on content pages. |
| Technical accessibility (20) | 14 | Full content in raw HTML (no JS needed). AI bots not blocked from content. llms.txt present. No RSL, no Content-Signal, no markdown negotiation. |

## AI crawler access (robots.txt, 62 lines)

- Lines 3-31: one group lists the AI user-agents (`CCBot` line 10, `ClaudeBot` line 11, `Google-Extended` line 16, `GPTBot` line 20, plus others). No `Disallow` follows them directly.
- Line 32 `User-agent: *` then rules at lines 33-61, which apply to that whole group: `Disallow: /config`, `Disallow: /search`, `Disallow: /account$`, `Disallow: /account/`, `Disallow: /commerce/digital-download/`, `Disallow: /api/`, `Allow: /api/ui-extensions/`, `Disallow: /static/`, plus query-string rules for author, tag, month, view, format=json and reversePaginate.
- Result: GPTBot, ClaudeBot, Google-Extended, CCBot and the others are not blocked from product, guide or FAQ pages. Only the paths above are closed.
- OAI-SearchBot, Claude-SearchBot, PerplexityBot and ChatGPT-User are not named. They fall under `*`, so they are allowed on content pages.
- No `Content-Signal:` line. No RSL or licence link found in any page or file.
- `Sitemap:` line 62 present.

## llms.txt

Present, H1, blockquote summary, link lists. Well-formed Markdown. Product prices match the product pages for all 22 products. Spot-checked product facts (vest 59/68/30 cm, beanie 54-58 cm, scarf 190 x 36 cm, set EUR 110, imprint reg. no.) all match the pages.

## Findings

| ID | Severity | Finding | Fixable? |
|---|---|---|---|
| G-01 | High | llms.txt contains internal editing notes and instruction-like text: "as checked on 1 November 2026"; "now includes hand-washing and flat-drying guidance"; "do not describe it as lambswool"; "Machine washing is conditional on the garment label"; "No gift-wrap promise". These are not buyer facts. | Fixable (file upload) |
| G-02 | Medium | llms.txt omits the 4 guides (`/how-to-wash-a-wool-sweater`, `/merino-vs-lambswool`, `/oversized-fit-guide`, `/how-to-choose-a-wool-cardigan`) and the 5 `/wool-*` landing pages. Grep for those paths in llms.txt returns 0. | Fixable (file upload) |
| G-03 | Medium | Return conditions differ by page. FAQ: "unworn, unwashed items". Shipping-returns: "Unworn, unused items". llms.txt: "original condition". Refund timing: FAQ "once the return arrives"; shipping-returns "Within 7 business days after we receive and approve it". | Fixable (content) |
| G-04 | High | Guides have no question-style H2s (for example "Wash it by hand", "Dry it flat"). No opening 40-60 word answer. The direct answer to "Merino or lambswool" only appears in the final H2 "Which one to choose". | Fixable (content) |
| G-05 | High | No author and no publication or update date on the 4 guides, size guide, shipping-returns, FAQ or about page. No datePublished or dateModified in JSON-LD. Only the imprint and privacy pages carry "Last updated". | Partly platform limit (Squarespace blog dates; pages have none). Author byline fixable (content). |
| G-06 | High | Organization JSON-LD `sameAs` (on all 49 pages) lists legacy profiles: `https://www.facebook.com/AccessoriesMareshop` and `https://www.pinterest.com/mmareshop/`. Instagram and TikTok point to @autumnandwool. | Fixable (settings: social links) |
| G-07 | Medium | About and home state "15 years as Mareshop on Etsy", "8,000+ orders on Etsy", "4.9★ from 1,400+ reviews on Etsy". No date or source; link to Etsy shop only. | Fixable (content: link to Etsy reviews) |
| G-08 | Low | Organization data: `LocalBusiness.name` is "AUTUMN AND WOOL, SIA" while `WebSite.name` and page titles use "Autumn & Wool". `telephone` is an empty string. Address string uses a newline. | Fixable (settings: business info) |
| G-09 | Low | `/home` returns 200 and is listed in sitemap.xml. Its canonical points to `https://www.autumnandwool.com`, so the duplicate is mitigated, but the sitemap carries a non-canonical URL. | Fixable (settings: delete page or drop from sitemap) |
| G-10 | Medium | Shop category pages (`/shop`, `/shop/cardigans`, `/shop/sweaters`, `/shop/vests`, `/shop/beanies--hats`, `/shop/sets`, `/shop/gift`, `/shop/winter-wool-gifts`) have no H1. The only heading is an H2 (for example "Cardigans"). `/shop/cardigans` has 78 words of main text. | Partly platform limit (template heading); content fix limited |
| G-11 | Low | Shop grid product images have `alt=""` (444 on category pages). Product names reach agents only through link text prefixed "Quick View". | Fixable (settings: image alt in product images) |
| G-12 | Medium | Multi-modal gap: no video, no care or fit visuals. Only photos. | Fixable (content / file upload) |
| G-13 | Low | Typography: stray space before full stops in several places ("Lightweight Merino Turtleneck .", "autumnandwool.com .", "Distressed Oversized Wool Raglan Sweater ,"). | Fixable (content) |
| G-14 | Info | No FAQPage schema. Not a gap to claim AI-citation benefit from. Product schema is present on all 22 products (cardigan uses AggregateOffer, lowPrice 160, offerCount 3). | n/a |
| A-01 | Info | `Accept: text/markdown` on `/` returns `text/html;charset=utf-8`. No markdown negotiation. | Platform limit |
| A-02 | Info | `/.well-known/ai-catalog.json` returns 404. `/llms-full.txt` returns 404. | Platform limit for .well-known; llms-full fixable (file upload) |
| A-03 | Pass | Raw HTML carries the full text of guides, FAQ, about, size guide, shipping, contact and product pages. Shop grids are present as links. No JS needed for content. | n/a |
| A-04 | Pass | All links and buttons across 49 pages have accessible names. Contact form fields have `<label for>` (Name, Email, Topic, Order number, Message). | n/a |

## Good

- Content in raw HTML, no CSR gap for content.
- Robots.txt does not block AI user-agents from content pages.
- llms.txt prices and product facts accurate on spot-check.
- Imprint, Organization JSON-LD and llms.txt agree on legal name, registration number 40203644965, address and email.
- Size chart in HTML table with EU/UK/US and cm. FAQ answers are short and self-contained.

## Could not verify

- Wikipedia, Reddit, YouTube and LinkedIn presence (no check run, not in the crawl).
- Live AI citation or retrieval behaviour (no DataForSEO run).
- Gift card values (EUR 25/50/100/150/250) are on the product page; not checked for stock or live checkout.
- Whether Squarespace serves `Content-Signal` or RSL on robots.txt. The file on disk has neither; the live file was not re-fetched.
- Whether the 15-year and Etsy review figures are accurate. Not checkable from the site.
- Live rendering with JS on, beyond the saved HTML.

## Platform limits vs fixable (summary)

- Platform limit: markdown negotiation (A-01), `.well-known` JSON (A-02), robots.txt content (no RSL/Content-Signal), page-level dates and author fields (G-05 partial), shop category H1 (G-10 partly).
- Fixable via content, settings or file upload: G-01, G-02, G-03, G-04, G-05 (byline), G-06, G-07, G-08, G-09, G-11, G-12, G-13, A-02 (llms-full only).
