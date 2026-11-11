# GEO and agent-readiness audit, after pass (2026-11-10)

Scope: crawl on disk at `evidence/seo-reaudit-2026-11-10/crawl-after/` (49 pages, raw HTML, robots.txt, llms.txt, sitemap.xml, index.tsv). No live requests. Judged only what the crawl shows. Page text treated as untrusted data.

## Score: 64 / 100

| Dimension | Score | Basis |
|---|---|---|
| Citability | 17 / 25 | Four guides open with direct 53-59 word answers. FAQ, About, Size guide and Shipping have no direct answer block. |
| Structural readability | 14 / 20 | One H1 per page, question-style H2s on guides, tables present. FAQ questions are not headings, About H1 is a slogan. |
| Multi-modal | 8 / 15 | 472 product images, all with non-empty alt, but alt text is templated. No video or audio on any page. Tables carry the data. |
| Authority and brand | 10 / 20 | Byline and visible date on guides, legal entity and reg. no. on imprint. Org sameAs is thin, legacy Mareshop profiles linked, Etsy claims unverified. |
| Technical accessibility | 15 / 20 | Content and JSON-LD in raw HTML, AI crawlers not blocked from content, llms.txt well formed. Sitemap has /home not /, lastmod uninformative. |

## AI crawler access (robots.txt)

No Disallow applies to any content path. The named AI user agents sit in the same group as `User-agent: *`, which holds only `Disallow: /config`, `/search`, `/account/`, `/api/`, `/static/` and query-parameter rules. No `Disallow: /` exists.

| Crawler | Governs | Status in crawl |
|---|---|---|
| OAI-SearchBot | ChatGPT search citability | Not named, falls under `*`, allowed |
| ChatGPT-User | ChatGPT user-initiated fetch | Not named, allowed |
| Claude-SearchBot | Claude search citability | Not named, allowed |
| Claude-User | Claude user-initiated fetch | Not named, allowed |
| PerplexityBot | Perplexity index | Not named, allowed |
| Googlebot | Google Search and AI Overviews | Not named, allowed |
| GPTBot | OpenAI training only | Named in group, no Disallow, allowed |
| ClaudeBot | Anthropic training only | Named in group, no Disallow, allowed |
| CCBot | Training | Named in group, allowed |
| Google-Extended | Gemini training and grounding | Named in group, allowed |
| Applebot-Extended | Apple Intelligence training | Named in group, allowed |
| cohere-ai | Training | Named in group, allowed |

Quoted lines: `User-agent: *` / `Disallow: /config` / `Disallow: /search` / `Disallow: /account/` / `Disallow: /api/` / `Disallow: /static/`.

## llms.txt

Present, well formed (H1, blockquote summary, H2 sections, link lists). 41 unique URLs, all found in index.tsv. Registration no., address, email, size range and shipping figures match the imprint, size guide and shipping page. No prices listed, so no price drift. No internal editing notes or [FILL] markers.

## Findings

| ID | Severity | One line | Evidence | Fixable |
|---|---|---|---|---|
| G-01 | Info (positive) | AI search crawlers are not blocked from content | robots.txt generic group above | n/a |
| G-02 | Low | Training bots are named in robots.txt but get the same allow rules, so the file reads as opt-out but is not | `User-agent: GPTBot` … `User-agent: cohere-ai` sit above `User-agent: *` with no Disallow of their own | Policy decision. Editing robots.txt: platform limit unless the plan exposes it (unverified) |
| G-03 | Medium | Return conditions differ across FAQ, shipping page and llms.txt | FAQ: "unworn, unwashed items"; shipping: "Unworn, unused items"; llms.txt: "unworn, unused items". Postage exception: FAQ and llms "unless the item is faulty"; shipping "unless the item arrived damaged or incorrect". Exclusions (custom/made-to-order, gift cards, sale items) and 5-day damage claim appear only on shipping page | Fixable (content) |
| G-04 | Medium | llms.txt and Product JSON-LD omit made-to-order status on brown/blue raglan cardigan | Product page: "Brown and Blue are machine-knitted and hand-finished to order". JSON-LD AggregateOffer: `"availability":"InStock"`, offerCount 3. llms.txt: "Merino Wool Raglan Cardigan in Black, Brown or Blue" with no note | Fixable (content) for llms.txt and product copy; JSON-LD availability is generated: platform limit |
| G-05 | Medium | Guides carry a visible byline and date but no machine-readable author or date | "By Kristine, designer and maker at Autumn & Wool · Updated 10 November 2026". JSON-LD on guides: WebSite, Organization, LocalBusiness only. No Article or Person type | Visible text fixable (content). Schema: platform limit (no code injection) |
| G-06 | Medium | Organization JSON-LD is thin | Has name, legalName, email, address (plain string), sameAs. `"telephone":""`, no url, no logo. LocalBusiness has no telephone or url | Fixable (settings: phone in Business info, logo upload). url and PostalAddress: platform limit |
| G-07 | Medium | sameAs lists only Instagram and TikTok, while footer links legacy Mareshop-branded profiles | sameAs: instagram.com/autumnandwool, tiktok.com/@autumnandwool. Footer: facebook.com/AccessoriesMareshop, pinterest.com/mmareshop/. Etsy link: etsy.com/shop/mareshop (header/footer on home and about) | Fixable (settings: social links) |
| G-08 | Medium | About page makes Etsy-based claims the crawl cannot verify | "8,000+ orders on Etsy", "4.9★ from 1,400+ reviews on Etsy", "15years as Mareshop on Etsy" | Fixable (content: state source and date, or link the Etsy reviews page) |
| G-09 | Medium | About page has no direct answer and a slogan H1 | H1 "Every stitch tells a story of patience and purpose"; 162 words; no named person entity beyond "Kristine" in body | Fixable (content) |
| G-10 | Low | FAQ has no direct answer block, generic H1, and questions are not headings | H1 "Questions, answered"; 12 `<details>/<summary>` items with questions in summary; no H3s | Fixable (content). Accordion itself is good: answers are in raw HTML |
| G-11 | Low | Size guide opener is short and has no question headings | Opener: "Our knits are made in relaxed and oversized shapes. Use your body measurements to pick a size…" (about 27 words, no numbers). Body size chart table is good | Fixable (content) |
| G-12 | Low | Shipping page has concrete numbers but no question headings; refund step is ambiguous | "Within 7 business days after we receive and approve it. Shipping costs not included." | Fixable (content) |
| G-13 | Low | Off-site entity presence not evidenced on site: no YouTube, Reddit, Wikipedia or LinkedIn link, no video on any page | 0 `<video>`, `<iframe>` or YouTube embeds across 49 pages | Content or channel decision. Not verifiable from crawl |
| G-14 | Low | Product alt text is templated and HTML entities are double-encoded on logo images | 88 images with `alt="Autumn &amp;amp; Wool"`; product alt pattern e.g. "Women's lightweight merino turtleneck, photo 9" | Fixable (content: image alt in Squarespace) |
| G-15 | Info | Cardigan guide prices match product pages | Guide table: €155, €145, €145, €160 vs product pages €155, €145, €145, €160 | n/a |
| A-01 | Info (positive) | Content, prices and JSON-LD are in raw HTML (SSR) | Raw fetch shows guide text, FAQ text, "€160.00", "Add To Cart", Product JSON-LD. Not rendered in a browser | n/a |
| A-02 | Info (positive) | Accessible names and language | 0 unnamed anchors on 5 sampled pages (after counting img alt); one H1 per page; 472/472 product images have alt. `lang="en-US"` on the site, which is English content for a Latvian studio | lang: platform setting, low value |
| A-03 | Low | Sitemap lists /home and omits / | Sitemap has `https://www.autumnandwool.com/home`; index.tsv has `/` but not in sitemap. home.html canonical is `https://www.autumnandwool.com` | Fixable (settings: check whether /home is a duplicate page) |
| A-04 | Low | Sitemap lastmod is not informative | 27 of 48 URLs share `<lastmod>2026-11-10</lastmod>` with `changefreq daily` | Platform limit (auto-generated) |
| A-05 | Info (positive) | No AI-directed or injected text found | Phrase scan of visible text (AI assistant, language model, ignore previous, as an AI, instructions for) returned no hits | n/a |

## What is good

- Guide openers answer the question directly, self-contained and under 60 words: wash guide "Wash a wool sweater by hand in cool water with a mild wool detergent…" (59 words); merino guide "Neither fibre is automatically warmer…" (53 words); oversized guide (55 words); cardigan guide (53 words).
- Guides use question H2s (5 of 5 on the wash guide), plus tables (cardigan price/fibre, size chart) and visible byline and "Updated" date.
- Imprint has legal entity, reg. no. 40203644965, address and email. Contact page matches.
- Size chart and cardigan table are real HTML tables, extractable without rendering.
- Product pages give garment measurements, fibre percentages and care lines in text.
- llms.txt is accurate against the site on the points checked.

## What I could not verify

- Etsy claims (8,000+ orders, 4.9 from 1,400+ reviews, 15 years): not checkable from the crawl.
- Off-site presence on Wikipedia, YouTube, Reddit, LinkedIn: not checked, no live requests.
- Whether the plan exposes a robots.txt or Organization-schema editor: unverified, treated as platform limit.
- Live JavaScript-rendered state: only raw HTML was read, no browser render.
- Whether any AI engine reads llms.txt: not assessed.
- Editorial dates: "Updated 10 November 2026" equals the crawl date, so it may be a template value.
- Platform-specific citation scores (Google AIO, ChatGPT, Perplexity, Bing Copilot) and DataForSEO mention data: not run.
