# GEO-02: AI shopping feeds (ChatGPT, Perplexity, Google, Copilot)

Date: 2026-11-25. DRAFT. Research only. Nothing was submitted, no account created, no Merchant Center or site edit.
Rule used: a claim is "confirmed" only if I read it on an official page this session. Everything else says "unconfirmed".
Limits: OpenAI's docs pages did not list countries or merchant eligibility. Microsoft help pages did not load. Squarespace published nothing I could find.

## 1. Table

| Programme | Eligible for us? | Effort | What we reuse | Next step |
|---|---|---|---|---|
| ChatGPT shopping (OpenAI product feed, Business Hub) | UNCLEAR. A feed route exists for any merchant who verifies identity in Business Hub (OpenAI docs). Supported countries and merchant criteria: unconfirmed (not on the pages I read). Instant Checkout: unconfirmed for us (Etsy/Shopify launch; later reported as moved to merchant-site checkout, March 2026, secondary source). Squarespace connector: none found, unconfirmed | Medium (about 1 day: map columns, add 2 fields, upload) | Our TSV is nearly the right shape: id, title, description, link, image, price, brand, availability, colour, size, material, variants | Owner claims business in Business Hub, verifies identity, then we upload a test feed (section 2) |
| Perplexity Merchant Program | UNCLEAR, leaning no for now. Official post (18 Nov 2024) targets "a large retailer"; Buy with Pro is US Pro users only; countries for the merchant program not named. Anything newer: unconfirmed | Low (one web form) | Same feed (format unconfirmed) | Owner may fill the form on the Perplexity blog post; expect no reply. Do not count on it |
| Google Merchant Center free listings, then Shopping Graph / Gemini / AI Mode | YES for free listings (already set up). Google's page lists Search, Shopping tab, Images, Lens, YouTube, Maps, Gemini. It does not name AI Mode or list countries; Latvia availability itself: unconfirmed. Status: 98 items queued, 0 approved (repo, 19-21 Oct) | Low to medium (fix feed gaps, check diagnostics) | The whole feed (98 rows, `autumnandwool-google-feed.tsv`) | Check Diagnostics now; fix gaps in section 4; re-upload once |
| Microsoft Copilot / Bing shopping (Microsoft Merchant Center) | UNCLEAR, leaning no for Copilot. Microsoft's agentic-commerce page (via search, not opened): Copilot Checkout only English-language merchants selling to US buyers; needs UCP-compliant feed. Plain Bing Shopping ads: Google feed import supported (help page 51110, not opened) | Low for Bing import; high for Copilot Checkout | Google feed via Microsoft's Google Import tool | Park. Revisit only if we ship to the US and want Bing. Do not buy ads |

## 2. Step lists (drafts, owner executes)

### ChatGPT product feed
1. Owner signs in at OpenAI Business Hub and claims the business (docs: developers.openai.com/commerce/guides/get-started).
2. Verify identity in the product section. Owner does this, not us.
3. Choose countries and currencies at upload. Which countries are accepted: unconfirmed. Try Latvia as store country, EU and US as targets.
4. Build the feed from our TSV. Required by spec: item_id, title, description, url, brand, seller_name, image_url, availability, price, target_countries, store_country. Price format `136.00 EUR`. Availability only in_stock, out_of_stock, pre_order, backorder, unknown. Variants need group_id, listing_has_variations, variant_dict. TSV/CSV/JSONL, UTF-8, HTTPS URLs.
5. Upload by file, hosted HTTPS URL or SFTP. Feeds are full snapshots. Fix any errors shown.
6. Make sure our robots.txt does not block the ChatGPT browser agent (OpenAI "Agent Access" guide). Already allowed per CONTEXT.md.
7. Keep price and availability in the feed in step with the site. The feed does not update carts; OpenAI says the website must confirm the live offer.
Checkout/payments sections (ACP, Stripe) are out of scope: unconfirmed for Squarespace.

### Perplexity
1. Open the Typeform link in the 18 Nov 2024 blog post (perplexity.ai/hub/blog/shop-like-a-pro).
2. Give store URL and contact. Free per the post. Perplexity "will reach out".
3. If they reply, ask for the feed spec and country list. Until then: unconfirmed.

### Google (the main route)
1. Merchant Center, Products, Diagnostics: screenshot approved / pending / issues (owner). Free listings card under Marketing methods shows status.
2. Confirm returns and shipping settings exist (Google asks for a return policy).
3. Fix the gaps in section 4, regenerate, upload once (see `feed/2026-10-21-feed-qa.md` re-upload checklist).
4. Repeat Diagnostics check after 24-72 h.

### Microsoft
1. Park. If ever: Microsoft Merchant Center account, Google Import, feed label with country code, price in that country's currency.

## 3. Reality check
- Free listings and Gemini are the only surfaces with an official page behind them for us. Do those first.
- AI answers about knitwear still lean on Etsy (Mareshop) per CONTEXT.md. A feed alone will not fix brand mentions. It helps product matching.
- Shopify gets AI-catalogue syndication automatically (Shopify news, secondary). Squarespace has no equivalent that I could find. Third-party "xpay" lists Squarespace as "coming soon". Ignore.

## 4. Feed gaps (from `autumnandwool-google-feed.tsv`, 98 rows, 19 columns)

| Gap | Evidence | Fix (draft) | Needed by |
|---|---|---|---|
| `identifier_exists` = `no` on all 98 | TSV | Correct for handmade without GTIN. Keep. OpenAI: omit GTIN if unassigned, never invent MPN | Google, OpenAI |
| `availability` hard-coded `in_stock` | `build_google_feed.py`; QA F1 | **FIXED code-side 2026-11-25**: stock now read from the export `Stock` column, `0` → `out_of_stock`, missing/ambiguous SKU stops the run. The 17 Oct export shows stock ≥ 1 for all 98 rows, so the handbook's "85 in / 13 out" (QA F2) is not reproducible — the export wins until the owner counts. Generator patch committed (`800caec`) | all |
| Made-to-order turtleneck (36 rows) and beanie (11 rows) | `feed/2026-10-21-feed-availability-proposal-wave3.md` (assumed, not counted) | Keep `in_stock` only if lead time is true. Add handling time 5-10 days for turtleneck. OpenAI has no handling field I read; `backorder` or `pre_order` may fit, unconfirmed. Owner decides SEO-03 | Google, OpenAI |
| `color` empty on 12 rows | TSV count; QA F6 | Owner gives colour names as on the product page. Never guess | Google, OpenAI |
| `material` too thin | Values only "Merino wool" (58), "Wool" (28), "Lambswool" (12). No fibre % | `[FILL: fibre % per product]` from yarn spec. Do not write "100%" unless owner confirms | Google, OpenAI |
| Claims in descriptions | "hand-sewn in Latvia", "Italian-spun", "extra-fine" (QA F3) | Keep only what owner evidences; align with "machine-knitted, hand-finished" wording | all (policy) |
| Variant photos wrong or missing | about 48 rows (QA F4); SQ7601591 image check (F5) | Bind photos in Squarespace first, then re-upload | all |
| Missing OpenAI-only fields | not in the live TSV: `seller_name`, `target_countries`, `store_country`, `group_id`/`variant_dict`, `image_url` name | **DONE code-side 2026-11-25**: `--openai <out.tsv>` emits a 26-column feed (98 rows, 14 groups, `variant_dict` JSON). Draft at `feed/2026-11-25-openai-feed-DRAFT-do-not-upload.tsv`. `target_countries` is a guessed default — owner confirms before upload | OpenAI |
| `shipping`, returns | shipping column dropped on purpose; returns text only in description | **DONE for the OpenAI output**: `shipping_price` 0 EUR, `accepts_returns` true, `return_deadline_in_days` 14 (from our own feed text "Free shipping... 14-day returns"). Google keeps account-level shipping | OpenAI |
| No reviews | none on site | Leave empty. No fake ratings | OpenAI |
| Brand name | feed uses "Autumn & Wool" | Good. Keep, not "AUTUMN AND WOOL, SIA" | all |

## Owner actions
1. Send a Merchant Center Diagnostics screenshot (approved count, issues).
2. Give colour names for the 12 empty rows.
3. Give fibre % per product (or confirm "100%" lines) and the claims decision.
4. Decide made-to-order handling (turtleneck, beanie): lead time and how to show it.
5. Physical stock count per SKU.
6. Decide whether to claim the business in OpenAI Business Hub and verify identity (you do it, we do not).
7. Optional: submit the Perplexity form. Low odds.
8. Ignore Microsoft Copilot for now.

## Sources
- OpenAI, Commerce overview: https://developers.openai.com/commerce (read 2026-11-25, no date on page)
- OpenAI, Get started (Business Hub, upload methods): https://developers.openai.com/commerce/guides/get-started (read 2026-11-25)
- OpenAI, Product feed spec: https://developers.openai.com/commerce/specs/feed (read 2026-11-25)
- OpenAI, Buy it in ChatGPT, 29 Sep 2025 (Instant Checkout launch, secondary view only): https://openai.com/index/buy-it-in-chatgpt/ (not opened; seen in search)
- Digital Commerce 360, 17 Mar 2026, ChatGPT checkout change (secondary): https://www.digitalcommerce360.com/2026/03/17/shopify-integration-with-chatgpt-changes/
- Perplexity, Shop like a pro, 18 Nov 2024: https://perplexity.ai/hub/blog/shop-like-a-pro
- Google, Free listings for products: https://support.google.com/merchants/answer/13889434 (read 2026-11-25)
- Google, Merchant Center announcements: https://support.google.com/merchants/announcements/6192467 (not opened)
- Microsoft Advertising, Agentic commerce: https://about.ads.microsoft.com/en/solutions/technology/agentic-commerce (via search summary, unconfirmed)
- Microsoft help, Google import / Google feed: https://help.ads.microsoft.com/apex/index/3/en/56870 and /51110 (first page returned "no results" when fetched; unconfirmed)
- Repo: `autumnandwool-google-feed.tsv`, `build_google_feed.py`, `business-os/seo-marketplace/feed/README.md`, `business-os/seo-marketplace/feed/2026-10-21-feed-qa.md`, `feed/2026-10-21-feed-availability-proposal-wave3.md`, `PROJECT-HANDBOOK.md` §5 item 4
