# AI Search Readiness and Agent Readiness: autumnandwool.com

Audit date: 2026-11-10. Scope: seo-geo + seo-agentic specialist pass over the shared crawl (`crawl/pages.tsv`, `crawl/html/`) plus live checks on `/`, `/robots.txt`, `/llms.txt`.

## Score: 64 / 100 (AI Search Readiness)

Analyst judgement, not a formula output. Breakdown:

| Area | Points | Max | Basis |
|---|---|---|---|
| AI crawler access | 20 | 20 | No AI bot or search bot blocked from content pages |
| llms.txt | 12 | 20 | Live, text/plain, all links 200, prices match; convention and wording issues, noindex header |
| Citability | 14 | 25 | Strong factual About/FAQ/shipping copy; contradictions across pages; thin product machine data; category pages weak |
| Entity clarity | 9 | 20 | Conflicting contact data in site-wide schema; Organization schema lacks name/url/logo; brand spelling mix |
| Agent readiness | 9 | 15 | Content server-rendered, real 404, agent UX heuristic 97; PSI link-name failures; unlabelled newsletter field; no alt on 4 home images |

## What works

- **Crawler access is fully open.** `robots.txt` has one group (`User-agent: *`) with the named AI bots (GPTBot, ClaudeBot, Google-Extended, CCBot, Applebot-Extended, cohere-ai, and others) inside the same group. That group only disallows `/config`, `/search`, `/account`, `/commerce/digital-download/`, `/api/` (except `/api/ui-extensions/`), `/static/`, and tracking/query-string patterns. No `Disallow: /` anywhere. Product, category, About and FAQ pages are allowed for every AI bot.
- **Server-rendered content.** `agentic_check.py` P0 `server-rendered`: pass, 326 words without JS on `/`, no JS shell marker.
- **Real 404.** `agentic_check.py` `http-404`: probe URL returns 404, no catch-all 200.
- **Agent UX heuristic.** `agent_ux_check.py` on `/`: score 97, status complete, 505 a11y nodes, 0 `div onclick` widgets, 18 semantic landmarks in the static DOM scan, 0 inputs without label in the HTML scan.
- **llms.txt accuracy on facts.** Every URL listed resolves to 200 in the crawl. Product prices in the file match the Product/AggregateOffer JSON-LD on all 22 product pages (for example vest EUR 126, cardigan EUR 145/155/160, beanie EUR 45, hat-and-scarf set EUR 110, digital gift card from EUR 25). Size chart (S-XL = EU 36-42 / UK 8-14 / US 6-12) matches `/size-guide`. Shipping and returns figures match `/shipping-returns` and `/faq`. Vest garment measurements (59 x 68 x 30 cm) and beanie fit (54-58 cm) match the product pages.
- **Imprint is dated and complete.** `/imprint`: "Last updated: 1 November 2026", legal name, registration number, address.
- **Product text is factual.** Product descriptions name the fibre (for example "100% pure new wool", "merino wool"), and care and fit blocks are present.

## Access policy (per bot, separate lines)

Source: `agentic_check.py` `data.robots.agents` (root-allowed for all 13 entries), plus manual read of the robots.txt group.

- **Training:** GPTBot (OpenAI), ClaudeBot/anthropic-ai (Anthropic), Google-Extended (control token, no crawler), Applebot-Extended (control token), CCBot (Common Crawl), cohere-ai, Meta-ExternalAgent, Bytespider and others are named in the group with no own Disallow, so they fall under the shared rules and are allowed to content pages. Blocking training bots is a policy choice, not a fix.
- **Search and citation:** OAI-SearchBot (not named, uses `*`, allowed), Claude-SearchBot (not named, allowed), PerplexityBot (not named, allowed), Bingbot (not named, allowed; powers Bing Copilot). Google-Extended governs Gemini/Vertex training and grounding only; Googlebot is unaffected.
- **User-triggered:** ChatGPT-User (`may not apply`), Claude-User (honours), Perplexity-User (generally ignores), Google user agent (generally ignores). Per vendor docs in the script; not an issue here.
- **Confirm the toggle.** The "AI crawlers" toggle under Settings > Crawlers is not visible from the file. The robots.txt state implies it is off (AI bots allowed). Verify in the Squarespace UI before any change.

## Findings

Layers: (a) Squarespace settings, (d) content edit, (g) llms.txt file replacement, (f) not fixable on this plan. No code injection proposed.

| ID | Severity | Finding | Evidence | Fix | Layer | Effort |
|---|---|---|---|---|---|---|
| G-01 | High | Site-wide Organization/LocalBusiness schema publishes a different contact (info@autumnandwool.com, +37129838090) from every visible contact (autumnandwool@gmail.com) | `crawl/html/*` JSON-LD on all 40+ HTML pages: `"email":"info@autumnandwool.com","telephone":"+37129838090"`; 43 files contain info@, 64 contain autumnandwool@gmail.com visibly (footer, imprint, FAQ, shipping) | Confirm which mailbox is monitored and which number is real. Make the Business Information email/phone match the visible one. If info@ is not a live mailbox, that is a lost-enquiry risk. | (a) | S |
| G-02 | Medium | Organization schema has no `name`, `url`, or `logo`; LocalBusiness `name` is the legal form "AUTUMN AND WOOL, SIA"; brand written three ways ("Autumn & Wool", "AUTUMN AND WOOL", lowercase "autumn and wool" logo text on About) | Org node keys: `legalName, address, email, telephone, sameAs, @type` only. About page footer block "autumn and wool" | Set Business Information name to "Autumn & Wool", upload logo, set site URL. Keep "AUTUMN AND WOOL, SIA" as legal name only. Pick one spelling for on-page text. | (a) | S |
| G-03 | Medium | `llms.txt` contains internal editing notes and non-convention prose, not only facts and links. Examples: "do not describe it as lambswool"; "Check the actual fibre on each listing"; "now includes hand-washing ... in its care FAQ"; "as checked on 1 November 2026"; "Fit outside this range is not guaranteed"; "No gift-wrap promise"; the section "Shopping, fit and care questions" is bullets of prose, not `[name](url): note` entries | `crawl/html/www-autumnandwool-com-llms-txt.html` lines in "Shopping, fit and care questions" | Replace the file with the corrected draft below (fact-only, link lists, no meta notes). | (g) | S |
| G-04 | Medium | `llms.txt` states "since 2011" for Mareshop, which the site never says (About says "15 years as Mareshop on Etsy") | `grep -l 2011 crawl/html/*` returns only the llms.txt file. Etsy shop search snippet (https://www.etsy.com/shop/mareshop) shows Riga, on Etsy since 2011 | Use "about 15 years on Etsy as Mareshop" in llms.txt; add the same statement to About if the date is wanted. | (g), (d) | S |
| G-05 | Medium | Unsourced headline claims on About: "8,000+ orders shipped worldwide", "4.9★ from 1,400+ reviews". AI systems may quote these. | `www-autumnandwool-com-about.html` visible text. Off-site snippet (Etsy shop page via WebSearch): about 8,100 sales, 4.9 from about 1,500 reviews. Roughly consistent but not linked | Add a source line that links to the Etsy shop (where the reviews live), or drop the numbers. Keep the figure date-stamped. | (d) | S |
| G-06 | Medium | Newsletter block: DOM contains Squarespace status text "This newsletter signup form needs a storage option..." (inside a class `newsletter-form-banner--hidden`, so likely not visible to people), placeholder-only input label ("Email Address", no `<label>`), and a captcha container on the signup form | `www-autumnandwool-com-about.html` and home; `<input ... placeholder="Email Address">` with no label; `.newsletter-form-banner--hidden`; `captcha-container` | Open the newsletter block in the editor, confirm storage is set and a test sign-up saves (use a test address, do not submit real data). If Sign Up fails, that is a revenue issue. Add a visible label. Note the captcha can block agents that try to sign up. | (a), (d) | S |
| G-07 | Medium | PSI (Lighthouse) reports "Links do not have a discernible name" on every run (6 of 6, mobile and desktop, home, /shop, product). The same run reports "Accessibility tree is not well-formed" failing in the Agentic Browsing category on every run. Not located in static HTML (0 unnamed anchors on home, /shop, vest page), so the source is rendered JS or icon links | `evidence/seo-audit-2026-11-10/pagespeed.md` lines 34-79 | Pull the failing node list from the PSI permalinks (in pagespeed.md) and name the links (aria-label or visible text) in the theme/block that produces them. Re-run PSI. | (a), (d), (f) if theme-locked | M |
| G-08 | Low | Home page has 4 `<img>` without `alt` (static HTML) | pages.tsv `img_no_alt`=4 on `/` and `/home`; agent_ux 1 unnamed interactive node | Add alt text to the 4 images (hero/logo) in the editor. | (d) | S |
| G-09 | Medium | Product machine data is thin: Product JSON-LD has `name, description, brand, offers, sku` only; no `material`, `color`, `size`, `gtin/mpn`, `brand.url`. Fibre appears only in prose (for example "100% pure new wool" in description, not as structured data). Some products carry `AggregateOffer` (price range) with no `url` | `prod.py` / `prod2.py` output on 22 product pages; JSON-LD dump of vest page | Put the fibre composition, colour and size in the product description/first line and in variant fields. Schema field additions are not editable on this plan. | (d) content, (f) schema | M |
| G-10 | Medium | Category pages have no H1 in static HTML (`/shop`, `/shop/cardigans`, `/shop/sweaters`, `/shop/vests`, `/shop/beanies--hats`, `/shop/sets`, `/shop/gift`, `/shop/winter-wool-gifts`). Meta descriptions missing on the same pages (desc_len 0) and on `/cart`. Titles are "Cardigans — Shop wool sweaters, cardigans & accessories | Autumn & Wool" (same suffix on all) | pages.tsv `h1_count` 0, `desc_len` 0 | Add a visible page title as H1 and a 120-160 character description per category. Use a plain factual sentence (material, fit, what is in the category) so an AI answer can quote it. | (a) for meta, (d) for H1 text | S-M |
| G-11 | Low | Return conditions differ between pages: shipping-returns says "Unworn, unused items"; FAQ says "unworn, unwashed items"; llms.txt says "original condition" | `www-autumnandwool-com-shipping-returns.html`; `www-autumnandwool-com-faq.html` | Pick one wording (the policy text) and reuse it on FAQ and llms.txt. | (d) | S |
| G-12 | Low | Duplicate content in sitemap: `/home` (sitemap lastmod 2026-01-28) has the same title and 326 words as `/`. The canonical of `/home` was not captured in the crawl, so it is unverified | `crawl/html/www-autumnandwool-com-sitemap-xml.html`; pages.tsv `/home` row | Check the `/home` canonical in the page SEO settings; if it is not `/`, point it there. Remove `/home` from the page list if it is an old duplicate. | (a) | S |
| G-13 | Low | llms.txt is served with `X-Robots-Tag: noindex` (platform header). Google ignores llms.txt, so impact is low; it can still stop some indexers from storing the file | `curl -sI https://www.autumnandwool.com/llms.txt` returns `x-robots-tag: noindex` | No setting visible on this plan. Track only. | (f) | - |
| G-14 | Low | llms.txt omits imprint and legal pages (`/imprint`, `/privacy-policy`, `/cookie-policy`) and the two gift category pages (`/shop/gift`, `/shop/winter-wool-gifts`), all 200 in the crawl | Sitemap vs llms link diff | Included in the corrected draft. | (g) | S |
| G-15 | Low | Product price list in llms.txt will go stale with every price change | llms.txt product section | Drop prices from llms.txt (the product pages carry the live price). Done in the draft. | (g) | S |
| G-16 | Medium | Brand presence off-site is thin and not linked to the new site: the Mareshop Etsy shop is the only result found for the brand history; no result for "Autumn & Wool" as a brand; the Organization `sameAs` points to legacy Mareshop profiles (Facebook "AccessoriesMareshop", Pinterest "mmareshop") and to Instagram, TikTok (current) | WebSearch "Autumn & Wool" Riga knitwear Mareshop Etsy (1 query; results: https://www.etsy.com/shop/mareshop, no separate "Autumn & Wool" brand listing) | Add the Etsy shop to sameAs (if the owner wants it recognised as the same maker) and keep the legacy Facebook/Pinterest profiles only if still active. Build a few third-party mentions (Etsy shop, Pinterest, Instagram bio) that say "Autumn & Wool, formerly Mareshop". | (a) sameAs, (d) profiles | M |
| G-17 | Info | `/.well-known` documents absent: api-catalog, oauth-protected-resource, oauth-authorization-server, agent-card.json, ai-catalog.json, UCP profile (404). WebMCP: 1 form, not annotated, no `registerTool`. Markdown negotiation not offered (no `index.md`, `Accept: text/markdown` returns HTML) | `agentic_check.py`, `ucp_check.py` (`profile_present: false`) | Opportunity only. Not fixable on this plan (no code injection, no file hosting at `/.well-known`). | (f) | - |
| G-18 | Info | Checkout agent reachability not tested live (no add-to-cart in an audit). Known from the project memory: beanie Add To Cart silently fails until a colour is picked, so an agent that does not choose the variant cannot buy | Project memory `autumnandwool-variant-add-to-cart-silent-fail.md` (not re-tested today) | Re-test on a test cart in the owner-approved window. Fix is the variant default (d) or product data. | (d) | M |

## Corrected llms.txt draft

Built only from URLs and titles in `crawl/pages.tsv` (status 200), plus facts already checked on the live pages. Prices removed (G-15). No internal notes (G-03). "since 2011" replaced (G-04).

```
# Autumn & Wool

> Autumn & Wool is a small knitwear studio in Riga, Latvia, run by designer and maker Kristine. It makes women's cardigans, sweaters, sweater vests, beanies and scarves from merino wool, lambswool and pure new wool. Pieces are knitted by hand or on a manually operated knitting machine in Latvia, then hand-sewn, washed and pressed before shipping. The studio was previously Mareshop on Etsy (about 15 years).

## Key facts
- Trading name: Autumn & Wool. Legal entity: AUTUMN AND WOOL, SIA, registration number 40203644965 (see https://www.autumnandwool.com/imprint).
- Studio: Braslas iela 22d, Rīga, LV-1035, Latvia.
- Contact: autumnandwool@gmail.com; Instagram @autumnandwool. Replies within 1-2 business days.
- Materials: merino wool, lambswool or pure new wool. The exact fibre is on each product page.
- Sizes: S-XL (EU 36-42, UK 8-14, US 6-12). Size chart: https://www.autumnandwool.com/size-guide
- Shipping: free to Latvia, the US and other destinations shown at checkout. In-stock items leave Riga in 2-5 working days. Estimated delivery 5-10 working days in Europe and 7-20 days to the USA, Canada and Australia. https://www.autumnandwool.com/shipping-returns
- Returns: unworn, unused items within 14 days of delivery; you pay return postage unless the item is faulty. Exchange = new order, then return the original. https://www.autumnandwool.com/shipping-returns
- Prices: EUR, including VAT for EU customers.
- Care: hand wash cold with a wool-safe detergent, do not tumble dry, lay flat to dry. Store folded with cedar or lavender.

## Pages
- [Handmade wool knitwear from Riga | Autumn & Wool](https://www.autumnandwool.com/)
- [Shop wool sweaters, cardigans & accessories | Autumn & Wool](https://www.autumnandwool.com/shop)
- [Cardigans — Shop wool sweaters, cardigans & accessories | Autumn & Wool](https://www.autumnandwool.com/shop/cardigans)
- [Sweaters — Shop wool sweaters, cardigans & accessories | Autumn & Wool](https://www.autumnandwool.com/shop/sweaters)
- [Vests — Shop wool sweaters, cardigans & accessories | Autumn & Wool](https://www.autumnandwool.com/shop/vests)
- [Beanies — Shop wool sweaters, cardigans & accessories | Autumn & Wool](https://www.autumnandwool.com/shop/beanies--hats)
- [Sets — Shop wool sweaters, cardigans & accessories | Autumn & Wool](https://www.autumnandwool.com/shop/sets)
- [Gift — Shop wool sweaters, cardigans & accessories | Autumn & Wool](https://www.autumnandwool.com/shop/gift)
- [Winter Wool Gifts — Shop wool sweaters, cardigans & accessories | Autumn & Wool](https://www.autumnandwool.com/shop/winter-wool-gifts)
- [Our story | Autumn & Wool](https://www.autumnandwool.com/about)
- [Size guide | Autumn & Wool](https://www.autumnandwool.com/size-guide)
- [Shipping & returns | Autumn & Wool](https://www.autumnandwool.com/shipping-returns)
- [FAQs | Autumn & Wool](https://www.autumnandwool.com/faq)
- [Contact | Autumn & Wool](https://www.autumnandwool.com/contact)

## Products
- [Digital Gift Card for Wool Knitwear | Autumn & Wool](https://www.autumnandwool.com/shop/p/autumn-and-wool-digital-gift-card)
- [Oversized Merino Wool Sweater Vest | Autumn & Wool](https://www.autumnandwool.com/shop/p/oversized-merino-wool-v-neck-sweater-vest)
- [Merino Wool Raglan Cardigan — Black, Brown or Blue | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/black-merino-wool-cardigan-100-merino-wool-raglan-sweater-minimalist-knitwear-sustainable-handmade-womens-cardigan-1)
- [Lambswool Raglan Crew Sweater, Brown | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/cozy-and-sustainable-hand-knitted-lambswool-sweater-for-women)
- [Distressed Oversized Wool Raglan Sweater | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/hand-knitted-distressed-wool-sweater-oversized-raglan-jumper-1)
- [Women's Classic Lambswool Crew Sweater | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper)
- [Lambswool Raglan Crew Sweater, Green | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/hand-knitted-lambswool-sweater-womens-winter-knitwear-1)
- [Merino Raglan Sweater, Dusty Pink | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/hand-knitted-merino-wool-raglan-sweater-dusty-pink-oversized-jumper)
- [Merino Striped Oversized Sweater | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/hand-knitted-merino-wool-striped-sweater-oversized-jumper)
- [Long Wool Shawl Cardigan, 100% Wool | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-cardigan-minimalist-open-front-sweater-1)
- [Open-Front Wool Cardigan with Side Slits | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-cardigan-open-front-winter-sweater-679428)
- [Pure Wool Stand-Collar Sweater, Blue | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-stand-collar-sweater-womens-knitwear-679510)
- [Pure Wool Side-Slit Sweater, Light Grey | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-sweater-organic-knitwear-asymmetrical-design-1)
- [Pure Wool Stand-Collar Sweater, Beige | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-sweater-stand-collar-knit-679503)
- [Pure Wool Side-Slit Sweater, Camel | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/hand-knitted-wool-sweater-womens-organic-knit-jumper-1)
- [Rib-Knit Beanie — Unisex | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1)
- [Merino Wool Hat & Scarf Set | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/merino-wool-hat-scarf-set-extra-fine-rib-knit-soft-on-skin-warm-not-bulky-unisex-gift)
- [Oversized Merino Turtleneck, Dusty Pink | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/merino-wool-sweater-oversize-sweater-knitted-wool-jumper-stand-up-collar-jumper-relaxed-fit-wool-pullover-warm-pink-jumper-679519)
- [Lightweight Merino Turtleneck, 12 Colours | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/merino-wool-turtleneck-sweater-womens-knit-pullover-soft-warm-lightweight-minimalist-sustainable-knitwear-sizes-sl-12-679428)
- [Long Wool Cardigan with Shawl Collar, 100% Wool | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/wool-cardigan-warm-cardigan-organic-wool-wrap-winter-sweater-cardigan-women-cardigan-sweater-minimalist-style-sweater)
- [Oversized Wool Raglan Sweater, Beige | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/wool-sweater-sweater-for-women-knit-cozy-pullover-sweater-sustainable-knitwear-oversized-wool-jumper-relaxed-fit-wool-pullover-1)
- [Oversized Wool V-Neck Vest, Beige Melange | Autumn & Wool](https://www.autumnandwool.com/shop/p/p/wool-sweater-vest-knitted-wool-vest-oversized-vest-womens-woolen-pullover-vest-top-sleeveless-wool-knit-vest-soft-v-neck-vest)

## Policies and company
- [Imprint | Autumn & Wool](https://www.autumnandwool.com/imprint)
- [Privacy policy | Autumn & Wool](https://www.autumnandwool.com/privacy-policy)
- [Cookie Policy | Autumn & Wool](https://www.autumnandwool.com/cookie-policy)
```

Draft notes: the Products list has 22 URLs from pages.tsv. The live sitemap (39 URLs) matches the crawl, so no product is missing from pages.tsv. The draft still needs a fact check against the contact email once G-01 is decided. If the owner confirms info@ is the right address, change the Key facts line.

## Not checked or limited

- **Lighthouse Agentic Browsing X/N: not obtained.** `lighthouse_agentic.py` returned HTTP 429 (PSI quota exceeded, no API key configured) for both mobile and desktop. The web-UI PSI run (pagespeed.md) recorded the agentic failure in words only, with no fraction.
- **Root HTML capture is empty.** `crawl/html/www-autumnandwool-com.html` and `autumnandwool-com.html` are 0 bytes, although pages.tsv lists `/` at 675,940 bytes. Home was analysed from `www-autumnandwool-com-home.html` (same title and word count) and from the live `/` via `agentic_check.py` and `agent_ux_check.py`.
- **Newsletter storage and sign-up not tested** (would submit a form; not done).
- **Checkout and add-to-cart not tested live** (would change a cart; not done). See G-18.
- **Brand mentions:** one WebSearch query only. No Wikipedia, Reddit, YouTube, LinkedIn or DataForSEO checks. No brand-mention numbers are given.
- **Squarespace AI-crawler toggle state** not read from the UI (inferred from robots.txt).
- **`info@autumnandwool.com` and `+37129838090`** not verified as live contacts.
- **Markdown negotiation** tested only with `Accept: text/markdown` on `/` (returned HTML); `--ua-matrix` not run (no authorisation from the orchestrator).
