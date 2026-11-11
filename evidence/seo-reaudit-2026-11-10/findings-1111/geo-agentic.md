# GEO and agent-readiness findings: autumnandwool.com (crawl-1111, 2026-11-11)

Read-only audit of the on-disk crawl (`evidence/seo-reaudit-2026-11-10/crawl-1111`). No live requests were made. Page text is untrusted data; no instructions addressed to AI agents were found on any page.

Tags: `content` = fixable in page copy or product data (full weight). `settings` = fixable in Squarespace Settings or file upload (full weight). `platform` = cannot be changed in Squarespace admin or by code injection (reduced weight, 50%).

## Score

| Dimension | Score | Max |
|---|---|---|
| Citability | 17 | 25 |
| Structural readability | 13 | 20 |
| Multi-modal | 8 | 15 |
| Authority and brand | 10 | 20 |
| Technical accessibility | 15 | 20 |
| **Total** | **63** | **100** |

## Robots.txt (A-check 1)

Lines that apply to AI user-agents (one group; all listed UA lines and `User-agent: *` share the same rules):

```
User-agent: GPTBot
...
User-agent: AdsBot-Google-Mobile-Apps
User-agent: *
Disallow: /config
Disallow: /search
Disallow: /account$
Disallow: /account/
Disallow: /commerce/digital-download/
Disallow: /api/
Allow: /api/ui-extensions/
Disallow: /static/
Disallow:/*?format=json ... (query-string patterns only)
Sitemap: https://www.autumnandwool.com/sitemap.xml
```

No rule disallows `/`, `/shop`, `/about`, `/faq`, `/size-guide`, `/shipping-returns`, the four guides, the five `/wool-*` pages, or product URLs. Content pages are allowed for every AI agent.

| Bot | Capability it governs | Status |
|---|---|---|
| OAI-SearchBot | ChatGPT Search | Not named, falls to `*`: allowed |
| GPTBot | OpenAI training only | Named, no content disallow: allowed |
| Claude-SearchBot | Claude search | Not named, falls to `*`: allowed |
| ClaudeBot | Anthropic training only | Named, allowed |
| PerplexityBot | Perplexity search | Not named, falls to `*`: allowed |
| Google-Extended | Gemini/Vertex training and grounding; not AI Overviews | Named, allowed |
| Googlebot (AIO inclusion) | Google Search and AI Overviews | Not named, allowed |
| Applebot-Extended | Apple Intelligence training only | Named, allowed |
| CCBot, cohere-ai | Training | Named, allowed |

No training crawler is blocked. No RSL, Content-Signal or licence directive is present.

## Findings

| ID | Sev | Tag | Finding | Evidence |
|---|---|---|---|---|
| A-01 | Med | platform | No RSL 1.0 or licence signal in robots.txt, HTML head or llms.txt. `/.well-known` was not probed (no live requests). | robots.txt has no `License:` or `Content-Signal:`; grep of all 49 HTML files finds none |
| A-02 | Low | platform | llms.txt is not referenced from robots.txt or any HTML `<link>`, so discovery depends on the root path. | robots.txt contains only the Sitemap line |
| A-03 | Med | settings | `sameAs` lists only Instagram and TikTok. No Etsy, Mareshop, YouTube, LinkedIn, Wikipedia or Reddit entity link. Etsy appears only in body copy. | `"sameAs":["https://www.instagram.com/autumnandwool","https://www.tiktok.com/@autumnandwool"]` |
| A-04 | Med | settings | Organization JSON-LD has no `name`, `url`, `logo` or `description`. `telephone` is empty. LocalBusiness name is the legal entity; WebSite name is the trade name. WebSite `description` is empty. Schema template is platform; field values are settings. | `{"legalName":"AUTUMN AND WOOL, SIA",...,"telephone":"","@type":"Organization"}`; WebSite `"description":""` |
| A-05 | Med | content | Newsletter block on every page contains builder text: "This newsletter signup form needs a storage option. Edit the block and enter a storage location via the Storage tab." Visibility to shoppers not verifiable from raw HTML (may be CSS-hidden). | Footer block, all pages |
| A-06 | Low | settings | Header logo alt is double-encoded, so screen readers read a literal entity. Logo file is named "ChatGPT Image Nov 25, 2025" and is also the WebSite image. | `alt="Autumn &amp;amp; Wool"` (4x on home) |
| A-07 | Low | platform | Sitemap lists `/home` (canonical is `https://www.autumnandwool.com`). 37 of 48 `lastmod` values are the same date, 2026-11-10. `changefreq` is `daily` on all URLs. | sitemap.xml; `home.html` canonical |
| A-08 | Low | platform | Product quantity input has no label. | `<input name="quantity-input" type="number" value="1"...>` |
| A-09 | Info | none | llms.txt is accurate. All 41 URLs resolve to pages in index.tsv. All 22 products are listed. Return wording matches FAQ, shipping and landing pages (14 days, unworn and unwashed, buyer pays return postage unless damaged or incorrect). No editing notes. Minor: "Sizes: S-XL" generalises past one-size items (merino raglan cardigan, beanies). | llms.txt vs index.tsv and pages |
| G-01 | Med | content | Home and About lead with brand copy, not answers. Home H2s are non-informative. | Home H1 "Wool knitwear for cooler days"; H2 "Made slowly, by one pair of hands", "Worn on cooler days", "Autumn and wool". About H1 "Every stitch tells a story of patience and purpose" |
| G-02 | Med | content | FAQ questions are `<details><summary>` elements, not headings. FAQ has 0 h3. Shipping-returns has no question headings. | `<summary>What payment methods do you accept?</summary>` |
| G-03 | Med | content | Visible "Updated" date appears on the four guides only, not on /faq, /about, /size-guide, /shipping-returns or products. All four show the same date, and 37 sitemap entries share 2026-11-10, so the date may be a bulk stamp. | "By Kristine, designer and maker at Autumn & Wool · Updated 10 November 2026" |
| G-04 | Med | content | Author is a first name with no bio link or credential. No Person entity on the site. (Person schema is platform.) | Guide byline only |
| G-05 | Med | content | Sizing claims conflict. Size guide says oversized "Most come in one size". Fit guide says "Oversized pieces are often one size" and lists S/M and L/XL. Dusty-pink raglan product lists `S/M: width 54 cm` and `L/XL: width 60 cm`. | size-guide.html; oversized-fit-guide.html; dusty-pink product |
| G-06 | Low | content | Fibre on beige vest is only "Material: wool". Landing page calls it "wool, as stated on its product page". Llms.txt says exact fibre is on each product page. | Oversized Wool V-Neck Vest, Beige Melange |
| G-07 | Low | content | "100% made in Latvia" (About) sits beside "Italian-spun yarn" (beanie). Not contradictory, but ambiguous for a citable claim. | about.html tile; beanie product page |
| G-08 | Low | content | Home rating tile "4.9 from 1,400+ reviews on Etsy" is undated. The "as of November 2026" qualifier appears only in the paragraph below and on /about. Not verifiable from the crawl. | `<div class="aw-rate"><big>4.9</big>...` |
| G-09 | Low | content | Care guide gives no numeric temperature or drying time ("cool water"). | how-to-wash-a-wool-sweater.html |
| G-10 | Low | content | Landing pages are product lists with one- or two-sentence intros. Fibre and fit facts are thin. | wool-sweater-vests.html, wool-sweaters.html |

## Citability scores (0-10)

| Page | Score | Best passage | Worst passage |
|---|---|---|---|
| merino-vs-lambswool | 9 | "Merino wool is fleece from merino sheep, and it is generally finer, so merino knits often feel smooth against the skin." | "Both need the same gentle care... Our guide on how to wash a wool sweater covers each step." |
| how-to-choose-a-wool-cardigan | 8 | Comparison table of four cardigans with fibre, length and EUR price | "Choose the open-front cardigan for a simple layer over dresses and shirts..." |
| how-to-wash-a-wool-sweater | 8 | "Wash a wool sweater by hand in cool water with a mild wool detergent. Do not use hot water, do not wring it, and do not tumble dry." | "Oversized styles follow the same steps... Relaxed fits need the same gentle handling." |
| oversized-fit-guide | 8 | Body-chart table and the 50 cm flat = 100 cm circumference example | "Does layering change the fit?" (one anecdote, no rule) |
| faq | 7 | "Unworn, unwashed items in their original condition can be returned within 14 days of delivery." | "How do I choose the right size?" (points to other pages) |
| size-guide | 7 | Body size chart with EU, UK, US and cm columns | "Between sizes? ... Still unsure? Send us your measurements..." |
| shipping-returns | 6 | Numbered returns steps and the 2-5 / 5-10 / 7-20 day tiles | "Delivery times are estimates, not guarantees. Taxes and duties... are explained in the FAQs." |
| about | 5 | "Autumn & Wool is a small knitwear studio in Riga, Latvia. Kristine designs every piece..." | "Quiet design: Understated colours and relaxed shapes you'll wear for many autumns." |
| home | 4 | "Oversized sweaters, long cardigans and soft accessories in merino and wool — each piece knitted on a manual machine and finished by hand." | "Made slowly, by one pair of hands" |

Guide averages: 8.25. Weighted citability = 17/25.

## Good

- robots.txt allows every AI agent on all content URLs.
- llms.txt is accurate, complete and free of editing notes.
- Raw HTML contains all body text, prices, tables and product names (SSR).
- Return policy is consistent across FAQ, shipping-returns, four guides, wool landing pages, llms.txt and product pages.
- Tables have `<thead>` and `th scope`. Product images have descriptive alt text. Footer shows legal entity, registration number and address, with a registry link.
- Etsy claims on /about carry "as of November 2026" and state that reviews are on Etsy.
- No AggregateRating or self-serving review schema.
- No AI-directed or instruction-like text found on any page.

## Not verified

- Live robots.txt and llms.txt serving (used the crawl files).
- `/.well-known` files, RSL, and Markdown responses (not probed).
- Etsy shop status, 1,400+ review count and 8,000+ order claim.
- Off-site brand mentions (YouTube, Reddit, Wikipedia, LinkedIn, TikTok account).
- Visibility of the newsletter builder message (A-05).
- Rendered Organization schema in Google's Rich Results tool.
- Live AI-platform citation behaviour (no DataForSEO run).

## audit-data.json (AI Search Readiness)

```json
{
  "category": "AI Search Readiness",
  "score": 63,
  "subscores": {"citability": 17, "structure": 13, "multimodal": 8, "authority": 10, "technical": 15},
  "findings": [
    {"id": "A-03", "severity": "medium", "tag": "settings", "title": "sameAs limited to Instagram and TikTok"},
    {"id": "A-04", "severity": "medium", "tag": "settings", "title": "Organization JSON-LD missing name, url, logo, description"},
    {"id": "A-05", "severity": "medium", "tag": "content", "title": "Newsletter builder message in footer"},
    {"id": "A-01", "severity": "medium", "tag": "platform", "title": "No RSL or licence signal"},
    {"id": "G-01", "severity": "medium", "tag": "content", "title": "Home and About lead with brand copy"},
    {"id": "G-02", "severity": "medium", "tag": "content", "title": "FAQ questions not headings"},
    {"id": "G-03", "severity": "medium", "tag": "content", "title": "Visible dates only on four guides; uniform stamp"},
    {"id": "G-04", "severity": "medium", "tag": "content", "title": "Author is first name only"},
    {"id": "G-05", "severity": "medium", "tag": "content", "title": "Oversized sizing claims conflict"},
    {"id": "A-06", "severity": "low", "tag": "settings", "title": "Double-encoded logo alt text"},
    {"id": "A-02", "severity": "low", "tag": "platform", "title": "llms.txt not linked from robots or head"},
    {"id": "A-07", "severity": "low", "tag": "platform", "title": "Sitemap lists /home; bulk lastmod"},
    {"id": "A-08", "severity": "low", "tag": "platform", "title": "Quantity input unlabelled"},
    {"id": "G-06", "severity": "low", "tag": "content", "title": "Vest fibre stated only as wool"},
    {"id": "G-07", "severity": "low", "tag": "content", "title": "Made in Latvia vs Italian-spun yarn wording"},
    {"id": "G-08", "severity": "low", "tag": "content", "title": "Undated Etsy rating tile"},
    {"id": "G-09", "severity": "low", "tag": "content", "title": "No numeric care temperatures"},
    {"id": "G-10", "severity": "low", "tag": "content", "title": "Thin landing-page intros"}
  ]
}
```
