# Autumn & Wool: SEO, AI visibility and 100 growth ideas

Written 19 October 2026, from the shop manager's point of view. It builds on `zero-sales-diagnosis-2026-10-18.md`, `QA-REPORT.md`, `markets-and-gift-guides.md` and today's checks of the live site.

**How to read the ideas:** Impact H/M/L · Effort S (under a day) / M (a few days) / L (weeks) · 💶 = costs money. ⚠️ = needs your decision or a fact only you have. ✅ = already prepared in an earlier report, only needs doing.

---

## 1. The situation in five lines

1. **Traffic is the problem.** 64 visits in 30 days, 2 of them from Google, 0 from Instagram or Pinterest. At 1–3% conversion, zero orders is the expected result.
2. **The brand is invisible online, but the maker is not.** A web search for "Autumn & Wool" finds nothing, and `site:autumnandwool.com` returns no pages. **Mareshop on Etsy** is well indexed: about 8,100 sales, 4.9 from about 1,450 reviews, on Etsy since 2011. It already appears in "best Baltic knitwear" answers.
3. **The new site is ready to convert.** The redesign is live, checkout works and abandoned-cart email is on. The known conversion leaks still need fixing: variant photos, delivery times, sizes and PayPal.
4. **The next 8–10 weeks are the season.** Christmas markets, gift guides and gift buying all happen now.
5. **Measurement is not yet trustworthy.** GA4 ecommerce events have not been verified, so every idea below must be measured before money is spent on it.

---

## 2. SEO review (checked 19 Oct 2026)

| # | Finding | Evidence | Severity | Fix |
|---|---|---|---|---|
| S1 | Domain not visible in the search index tested. | `site:autumnandwool.com` returns nothing. A brand-name search finds nothing. | **High** | Verify in **Google Search Console** and **Bing Webmaster Tools** (ChatGPT search draws on Bing), submit the sitemap, request indexing for the top 15 URLs. |
| S2 | Hidden page `/redesign-preview` is public (HTTP 200) and listed in the sitemap. | `curl` and `sitemap.xml` | **High** | Delete the page, or disable it and set it to noindex. |
| S3 | Sitemap lists `/home`, a duplicate of `/`, and `/shop/gift`, a thin page. | `sitemap.xml` (38 URLs) | Med | Delete or redirect `/home` → `/` with a 301 in URL Mappings. Hide or fill `/shop/gift`. |
| S4 | Category pages (`/shop/sweaters` etc.) have **no meta description, no H1**, and a canonical pointing to `/shop`, so Google won't rank them on their own. | Page HTML | **High** | Give every category its own SEO title and description and a short 80–150-word intro. If Squarespace keeps the canonical on `/shop`, build real landing pages instead ("Merino wool cardigans", "Wool sweaters for women"…) with a product block. |
| S5 | Product URLs are long Etsy-style slugs, e.g. `/shop/p/p/black-merino-wool-cardigan-100-merino-wool-raglan-…-1`. | Sitemap | Med | Short slugs (`/shop/merino-raglan-cardigan`) plus 301 redirects from the old ones. ⚠️ Product data is frozen; this is a proposal. |
| S6 | Product schema lacks `aggregateRating`/`review`, `sku`, `shippingDetails` and `hasMerchantReturnPolicy`. The cardigan has no `price` because of its variants. | JSON-LD on 2 products | Med | Add delivery times and a return policy in Squarespace/Merchant Center. Collect on-site reviews so ratings can be marked up. |
| S7 | Shop page is heavy: 872 KB HTML and 203 `<img>` tags in one page. | `curl` | Med | Paginate or limit to 24 products. Use category landing pages. |
| S8 | English only (`en-US`), with no Latvian or German version, though the shop is in Riga and ships to the EU. | `lang`, no `hreflang` | Med | A Latvian version of the key pages (home, about, shipping, 5 bestsellers), at least for local Christmas buyers. |
| S9 | Meta descriptions are present and the right length on the main pages. Titles fixed on 18–19 Oct. | `seo_check.py` | ✅ Done | — |
| S10 | No blog or guides, so nothing ranks for questions people actually search ("how to wash merino", "lambswool vs merino", "wool sweater gift for her"). | Sitemap: no blog | **High** | Five evergreen guides (see ideas 21–30). |
| S11 | Organization and LocalBusiness schema are present. Good base for a Google Business Profile. | JSON-LD | ✅ | Create or verify the **Google Business Profile** with the same name, address and hours. |

## 3. AI visibility (ChatGPT, Claude, Gemini, Perplexity)

**How AI assistants choose a shop to recommend:** they repeat what the open web already says. That means pages they can crawl, plus third-party mentions (lists, gift guides, Reddit, marketplaces, press), plus clear, consistent facts about the brand.

| Check | Status | What it means |
|---|---|---|
| AI crawlers allowed in `robots.txt` (GPTBot, ClaudeBot, Google-Extended, PerplexityBot via `*`) | ✅ Allowed. They share the `*` rules: only admin and API paths are blocked. | Keep it. Don't switch on Squarespace's "block AI crawlers". |
| `llms.txt` | ⚠️ **Stale.** It's a static file uploaded in Nov 2025 with old titles ("Shop Now…"), it links `/home`, and it lists **no products**. | Rewrite it (draft in idea 33): brand facts, maker, materials, sizes, shipping, returns, top products with prices. |
| Brand entity | ❌ "Autumn & Wool" isn't known anywhere online. "Mareshop" is. | Connect the two names everywhere you control them: "Autumn & Wool, by Kristine (formerly Mareshop on Etsy, since 2011)". |
| Third-party mentions | ❌ None found for Autumn & Wool. Competitors (Woolture, PappusStore, Mattilde, Smukilini) do appear in directory and list results. | Gift guides, Riga shopping guides, directories, Reddit and press (ideas 36–48). |
| Facts an AI can quote | ⚠️ Partly. The FAQ, size guide and shipping pages exist, but delivery times, materials per product and reviews are missing or inconsistent. | One "Facts" block: who, where, since when, what yarn, shipping times, return rule. |
| Test it | Not done. I can't log into ChatGPT or Perplexity as a customer. | Once a month, ask 10 fixed questions in ChatGPT, Claude, Gemini and Perplexity and record whether we're named (idea 49). |

---

## 4. The 100 ideas

### A. Fix the leaks first (conversion): 1–15
| # | Idea | Impact | Effort |
|---|---|---|---|
| 1 | Fix the Brown/Blue cardigan: a photo per colour, or split it into 3 products (3 extra indexable pages). ⚠️ product freeze | H | S |
| 2 | Show delivery times per zone at checkout and on every product page ("Ships from Riga in 2–5 working days · EU 5–10 days"). ✅ | H | S |
| 3 | Connect **PayPal**, plus Apple Pay and Google Pay express buttons. | H | S |
| 4 | Size selector or a clear "one size, fits EU 36–42" line, plus flat measurements, on every garment in the same format. ⚠️ | H | M |
| 5 | Put a "Size guide" link and a "Not sure? Email Kristine your measurements" box next to Add to cart. | M | S |
| 6 | Real social proof on the site: import or quote 10–20 Etsy reviews with first name and country, or link the Etsy review page. ⚠️ | H | S |
| 7 | One consistent returns rule everywhere ("unworn, unwashed, original condition, 14 days"). ⚠️ | M | S |
| 8 | Free returns, or one free exchange of size, for EU orders in December. 💶 | M | S |
| 9 | Gift options: gift wrap, a handwritten note and a "gift receipt / no prices" checkbox. 💶 small | H | S |
| 10 | A "Christmas delivery deadline" banner per country (last order dates). | H | S |
| 11 | Cart reassurance: "Free shipping · 14-day returns · Handmade in Riga", once, near the Checkout button. | M | S |
| 12 | Verify GA4 ecommerce events with one test-mode order (add_to_cart, begin_checkout, purchase). ✅ | H | S |
| 13 | Exit-intent or second-visit offer: a free gift-wrap code for an email address (no pop-up on the first visit). | M | S |
| 14 | Product pages: add "Pairs well with" bundles (sweater + beanie = 10% off the set). | M | S |
| 15 | Make product photos consistent: same background, flat-lay and on-body shots, and a 10-second video per bestseller. | H | M |

### B. Search engine optimisation (Google and Bing): 16–32
| # | Idea | Impact | Effort |
|---|---|---|---|
| 16 | Verify Google Search Console and **Bing Webmaster Tools**, submit the sitemap, request indexing. | H | S |
| 17 | Delete `/redesign-preview`, redirect `/home` → `/`, clean the sitemap. | M | S |
| 18 | Write SEO titles and descriptions for every category page. | M | S |
| 19 | Category landing pages with real copy: "Merino wool cardigans", "Lambswool sweaters", "Wool gifts for her", "Wool beanies". | H | M |
| 20 | Short product slugs plus 301 redirects. ⚠️ freeze | M | M |
| 21 | Guide: "Merino vs lambswool vs pure new wool: which to choose". | H | M |
| 22 | Guide: "How to wash and store a wool sweater" (care pages earn links and AI citations). | H | S |
| 23 | Guide: "Wool sweater sizing: how oversized fits work". | M | S |
| 24 | Gift guide on our own site: "Wool gifts under €50 / under €120 / special". | H | S |
| 25 | Story: "From Mareshop on Etsy to Autumn & Wool: 15 years of knitting in Riga". | H | S |
| 26 | "Made in Riga" page: studio photos, the knitting machine, the process. Strong for trust and press. | M | M |
| 27 | Image SEO: rename files (no more "ChatGPT Image…", "IMG_3336"), write descriptive alt text. ⚠️ photo rights | M | M |
| 28 | Add `shippingDetails` and a return policy so Google shows "free delivery / returns" in results. | M | S |
| 29 | **Google Merchant Center**: shipping policy → upload the prepared feed → free product listings. ✅ | H | M |
| 30 | Google Business Profile for the studio (Riga map pack: "knitwear Riga", "wool sweater Riga"). | H | S |
| 31 | Latvian versions of the key pages for local Christmas buyers. | M | L |
| 32 | Internal links: every guide links to 2–3 products and every product links to the guide. | M | S |

### C. AI assistant visibility (GEO): 33–50
| # | Idea | Impact | Effort |
|---|---|---|---|
| 33 | Rewrite **llms.txt**: brand summary, maker, since 2011, materials, sizes, shipping times, returns, top 15 products with price and URL. | H | S |
| 34 | A short "Facts" block on About (who, where, since when, materials, delivery, returns), written in plain sentences that AI can quote. | H | S |
| 35 | Use the same name string everywhere: "Autumn & Wool by Kristine (formerly Mareshop on Etsy)". | H | S |
| 36 | Keep the Etsy shop alive and consistent: same photos and story. Etsy is the source AI already trusts. ⚠️ Etsy rules limit off-platform links | H | S |
| 37 | Get listed in "best Latvian knitwear / Baltic gifts" articles (neighborhood.lv, LIVE RĪGA, In Your Pocket Riga, Deep Baltic). ✅ pitch drafted | H | M |
| 38 | List in Latvian business directories (zl.lv, 1188.lv, LIVE RĪGA shop list) with the same name, address and phone. | M | S |
| 39 | Reddit: answer honestly in r/knitting, r/BuyItForLife, r/latvia, r/femalefashionadvice (as the maker, disclosed, no spam). | M | M |
| 40 | Pinterest: rich pins plus boards like "Merino cardigans", "Wool gift ideas". Pinterest is crawled and quoted. | H | M |
| 41 | YouTube or Shorts: "How a sweater is made on a manual knitting machine in Riga". Video transcripts feed AI answers. | M | M |
| 42 | FAQ answers phrased as real questions ("Is merino itchy?", "Does lambswool pill?"). They are easy for AI to lift. | M | S |
| 43 | Comparison page: "Machine-knitted by hand vs factory knitwear: what's the difference". | M | S |
| 44 | Press release on Latvian news wires about the 15-year maker launching her own brand. | M | S |
| 45 | Wikidata or Crunchbase-style entries only where the brand qualifies (no fake notability). | L | S |
| 46 | Ask happy customers to review us on Google Business Profile and Trustpilot. Third-party ratings get quoted. | H | M |
| 47 | Product feeds to ChatGPT Shopping or Perplexity shopping when open to small merchants (via the Merchant Center feed). | M | M |
| 48 | Guest article on a knitting blog or in Ravelry forums about yarn choice. | M | M |
| 49 | Monthly AI visibility test: 10 fixed prompts × 4 assistants, logged in a sheet. | M | S |
| 50 | Use Squarespace's own "AI Visibility" panel (prompts tracker) and track the trend weekly. | L | S |

### D. Channels and marketplaces: 51–60
| # | Idea | Impact | Effort |
|---|---|---|---|
| 51 | Keep **Etsy (Mareshop)** as a sales channel for the season, not only as history. It already has the reviews. | H | S |
| 52 | Free Google Shopping listings (Merchant Center), then a small Performance Max test (€5–10/day) once events are verified. 💶 | H | M |
| 53 | Pinterest ads for 2–3 bestsellers in the gift season. 💶 | M | M |
| 54 | Instagram and Facebook Shops catalogue from Squarespace. | M | S |
| 55 | Wholesale or consignment: 2–3 Riga concept stores and museum shops (Art Nouveau Museum, design shops). | M | M |
| 56 | FromMe.lv "Made in Latvia" gift card partner. ✅ researched | M | S |
| 57 | Curated EU platforms for slow fashion (e.g. Wolf & Badger-type marketplaces). Check fees first. 💶 | M | M |
| 58 | Hotel or airport shops in Riga for tourists. | L | M |
| 59 | Corporate gifting: wool beanie or scarf sets with a logo card for Riga companies at Christmas. | M | M |
| 60 | Pre-order or made-to-order for sold-out colours (2–3 week lead time stated). | M | S |

### E. Social and content: 61–72
| # | Idea | Impact | Effort |
|---|---|---|---|
| 61 | Retire or rename the legacy Facebook (AccessoriesMareshop) and Pinterest (mmareshop) accounts to Autumn & Wool, keeping the followers. ⚠️ | H | S |
| 62 | Three posts a week on Instagram with UTM links. Drafts exist in `campaign-assets/`. ✅ | H | M |
| 63 | Reels: "Riga studio, one sweater from yarn to parcel" (process content performs best for handmade). | H | M |
| 64 | Behind-the-scenes "knit along" story series in Kristine's own voice. | M | S |
| 65 | UGC: ask past Etsy buyers for photos wearing their sweater, with a small thank-you. | H | M |
| 66 | Micro-influencers in Latvia, Germany and Scandinavia (2–10k followers, slow fashion): gift a piece and ask for an honest post. 💶 | H | M |
| 67 | TikTok "soft life / slow fashion" knit content (low effort, reuse the Reels). | M | S |
| 68 | Monthly "colour of the month" drop (e.g. December: bordeaux). | M | S |
| 69 | Styling content: "3 ways to wear the long cardigan". | M | S |
| 70 | Care content: "Fixing a pill on wool" (useful, shareable). | M | S |
| 71 | Collaboration with a Riga café or bakery: photo shoot plus a joint giveaway. | M | S |
| 72 | Seasonal lookbook PDF to share with press and stores. | M | M |

### F. Email and customers: 73–82
| # | Idea | Impact | Effort |
|---|---|---|---|
| 73 | Newsletter sign-up with a reason to join ("first to know about new colours + gift wrap code"). | H | S |
| 74 | Welcome email series (3 emails: story, care, bestsellers). Draft exists. ✅ | H | S |
| 75 | Abandoned-cart email: already live. Add a second reminder after 3 days. | M | S |
| 76 | Post-purchase email: care guide, a review request after 10 days, a referral code. | H | S |
| 77 | Referral: "Give €15, get €15". | M | S |
| 78 | Win back past Etsy customers where Etsy rules allow (e.g. a package insert for future Etsy orders). ⚠️ Etsy rules | M | S |
| 79 | Back-in-stock alerts for sold-out colours. | M | S |
| 80 | Birthday or "one year with your sweater" email with a care tip. | L | S |
| 81 | Segment by country and send Christmas deadline emails per zone. | M | S |
| 82 | Loyalty card: 5th purchase = free beanie. | L | S |

### G. Product, price and offer: 83–92
| # | Idea | Impact | Effort |
|---|---|---|---|
| 83 | Gift entry price point: beanie + scarf set and gloves under €60 (gift buyers start low). | H | M |
| 84 | Bundles: "Matching set" sweater + beanie, "Couple beanies". | M | S |
| 85 | Gift card visible in the header in December (no shipping risk, last-minute gifts). | H | S |
| 86 | Limited "Riga Christmas edition" colour, numbered, with small quantity and real scarcity. | M | M |
| 87 | Repair or re-knit service (sustainability story, earns press). | L | M |
| 88 | Men's line: start with beanie, scarf and one crew sweater (QA saw mostly women's). | M | L |
| 89 | Kids' or mini-me beanie to match the adult set. | L | M |
| 90 | Price test: free shipping threshold vs flat price. Keep free shipping on garments. | M | S |
| 91 | Show "price per wear" or "a sweater for 10 winters": quality justification on product pages. | L | S |
| 92 | Yarn transparency: name the supplier and the fibre % per product (also kills "is it itchy" doubt). ⚠️ | M | S |

### H. Riga and offline: 93–96
| # | Idea | Impact | Effort |
|---|---|---|---|
| 93 | Christmas markets: Kalnciema Saturdays, Baltic EXPO (20 spots left), MyExpo White Xmas. ✅ researched | H | M |
| 94 | QR card at the stall → site with a "market visitor" code, to see offline-to-online sales. | M | S |
| 95 | Studio open day or pre-Christmas "try-on evening" in Riga. | M | S |
| 96 | Tourist angle: LIVE RĪGA "What to buy in Riga" knitwear section. ✅ researched | M | S |

### I. Operations and trust: 97–100
| # | Idea | Impact | Effort |
|---|---|---|---|
| 97 | Stock and production calendar for December so nothing sells that can't ship before Christmas. | H | S |
| 98 | Tracked shipping by default, plus "where's my order" auto-emails. | M | S |
| 99 | Back up the Squarespace site before 1 Nov: the duplicate is a trial. Upgrade or export it. | M | S |
| 100 | Weekly 30-minute dashboard: visits by source, add-to-carts, orders, email sign-ups, AI-prompt test. Decide using numbers only. | H | S |

---

## 5. My top 10 for the next 30 days (season first)

| Rank | Idea # | Why now |
|---|---|---|
| 1 | 16, 17 Search Console + Bing, clean the sitemap | Nothing else works if the site isn't indexed. |
| 2 | 29 Merchant Center free listings | Free Google Shopping traffic for gift season. Feed already prepared. |
| 3 | 2, 10 Delivery times + Christmas deadlines | Gift buyers won't buy without them, and Merchant Center needs them. |
| 4 | 3 PayPal + express pay | Removes the "small risky shop" feeling at checkout. |
| 5 | 6, 35, 36 Bring the Mareshop reviews and name to the new brand | The reputation already exists; the new site doesn't use it yet. |
| 6 | 33, 34 llms.txt + Facts block | One hour of work; makes the shop quotable by AI. |
| 7 | 1, 4 Variant photos and sizes ⚠️ | The biggest remaining reason a visitor leaves a product page. |
| 8 | 93 One Christmas market | Cash, contacts, emails and photos in one go. |
| 9 | 62, 63, 40 Instagram + Pinterest with UTM | The only traffic you control today. Drafts exist. |
| 10 | 12, 100 Verify GA4 events + weekly dashboard | So we know which of the above actually sells. |

## 6. Decisions only you can make

- Is Mareshop on Etsy still selling? Should Etsy and the site both stay open this season?
- Is "made in Latvia" correct for every product? Markets ask for proof.
- Rights to the "ChatGPT Image" photos, and whether we can quote Etsy reviews on the site.
- Budget for paid tests (Shopping, Pinterest, influencers): suggested €200–300 for December, only after GA4 events are verified.
- Unfreeze product data for ideas 1, 4, 20 and 92, or keep proposing only.
