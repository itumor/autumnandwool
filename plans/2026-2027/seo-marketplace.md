# SEO / Pinterest / Etsy (Mareshop) / Merchant Center — plan Q4 2026 + 2027

DRAFT for owner approval. Author: aw-seo-marketplace, 21 Oct 2026. Nothing here is applied: product data is frozen,
every live change (site, Etsy, Merchant Center, Pinterest, GSC) is an owner action. Targets are PROPOSALS set against
the baselines below; `business-os/kpi-weekly.csv` is still empty (header only), so there is no weekly history yet.
Where a number is unknown it says TODO. No target below is a forecast of revenue.

## 1. Starting point (facts, with source)

| Area | Fact | Source |
|---|---|---|
| Organic baseline | GSC 90 d to 19 Oct: 11 clicks / 388 impressions / 2.8% CTR / avg pos 14.1; 11 of 37 known URLs indexed | agent brief, `PROJECT-HANDBOOK.md` §7 (as quoted in skill `aw-ecommerce-seo`) |
| Traffic | 64 visits / 30 d, 2 from Google, 0 from Instagram or Pinterest, bounce ~96% | `zero-sales-diagnosis-2026-10-18.md` §1 |
| Orders | Zero real direct orders; orders come from Squarespace Orders, GA4 has no ecommerce events (Code Injection plan-gated) | `business-os/README.md` §2, §8 |
| Query headroom | "oversized merino wool sweater" pos 27, "timeless knitwear" 5.9, "wool size chart" 44 | skill `aw-ecommerce-seo` (GSC 19 Oct) |
| On-page defects | Shop page no H1; home 2 H1s (and "knitwearfor" space bug); category pages no meta/H1 and canonical to `/shop`; alt text = file names; `/redesign-preview` and `/home` in sitemap; thin categories (Beanies 1, Sets 1) | `zero-sales-diagnosis` #9,#10,#13; `GROWTH-PLAN-100-IDEAS.md` S2–S4; `QA-REPORT.md` |
| Slugs | ~35 legacy Etsy-style `/shop/p/p/...` slugs; no slug change without owner-approved redirect list | `llms.txt` product URLs; `GROWTH-PLAN` S5/idea 20 |
| Schema | Product JSON-LD present with price/availability; no `aggregateRating`, `shippingDetails`, return policy; cardigan shows no price (variants) | `GROWTH-PLAN` S6, `zero-sales-diagnosis` §2D |
| llms.txt | Repo copy now lists 22 products with prices, shipping and returns. Growth plan (19 Oct) called the live file stale: TODO confirm what is live | `llms.txt`, `GROWTH-PLAN` §3 |
| Merchant Center | Feed `autumnandwool-google-feed.tsv`, 98 rows, uploaded 19 Oct; approval expected from 21 Oct. ~48 rows share one image (beanie 11, turtleneck 36, set 3, cardigan blue 1). `build_google_feed.py` line 108 hard-codes `in_stock`; 13 items are out of stock | `business-os/README.md` §2, `owner-action-pack-2026-10-19.md` A, `ai-team.md` decisions 3 |
| Pinterest | Legacy handle "mmareshop"; zero referrals; Product schema should qualify rich pins; bio UTM link defined | `zero-sales-diagnosis` #5, `owner-action-pack` C |
| Etsy | Mareshop: ~8.2k sales, ~1.5k reviews, 4.9 stars, 15 years (site says 1,400+; owner pack proposes 1,500+). Whether it is still actively selling is unconfirmed | `business-os/README.md` §2, `owner-action-pack` D, `GROWTH-PLAN` §6 |
| Claims | "handmade", "made in Latvia/Riga", "sustainable", "organic" lack evidence; markets ask for proof of Latvian production | `markets-and-gift-guides.md` header, `aw-brand-voice` §3 |
| Unit economics | `sku-economics.csv` cost columns blank; paid spend blocked until filled | `ai-team.md` decisions 1 |
| Team | SEO/Pinterest and Marketplace Manager are "Later" hires; E-commerce Specialist (AI agents until hired) owns the channels | `hiring-plan.md` |

Principle: organic and free channels (GSC, Merchant Center free listings, Pinterest, Etsy) cost no ad spend. Judge them on
contribution (`aw-unit-economics`), not traffic alone.

## 2. Q4 2026 (21 Oct – 31 Dec): gift season

### 2.1 Goals
1. Be indexed and measurable: GSC and Bing verified, sitemap clean, priority pages indexed.
2. Free Google listings live for every row with a correct image and correct stock status.
3. Pinterest and Etsy producing the first attributable visits to the 5 priority SKUs (SKU list from GM/Production).
4. Etsy kept as a live sales channel for the season (owner confirms it is active).

### 2.2 KPIs and targets (proposed; re-baseline at end of week 4)

| KPI | Baseline | Target 31 Dec | Source of truth |
|---|---|---|---|
| Indexed pages (GSC Pages report) | 11 of 37 | 25+ of the sitemap URLs after cleanup (denominator will drop once `/home`, `/redesign-preview` go) | GSC |
| GSC clicks, 28 d | 11 per 90 d (~4 per 28 d) | At least 5x baseline run-rate (~20 per 28 d) | GSC |
| GSC impressions, 28 d | 388 per 90 d (~130 per 28 d) | At least 3x baseline (~400 per 28 d) | GSC |
| Queries in top 10 | TODO (export needed) | At least 3 non-brand queries | GSC export |
| Merchant Center approved items | 0 approved on 18 Oct; 98 submitted | At least 90 of 98 approved, 0 account-level issues | MC Diagnostics |
| MC disapprovals unresolved > 7 days | n/a | 0 | MC Diagnostics |
| Pinterest outbound clicks / GA4 sessions (source=pinterest) | 0 | Any non-zero by week 4; 50 sessions in Dec is a stretch goal, set after 4 weeks of data | GA4 |
| Etsy listing visits, conversion, orders | TODO (owner Etsy Stats export) | Per-listing baseline recorded in week 1; 5 listings rewritten; review rating held at or above 4.9 | Etsy Stats |
| Direct-store orders from organic/free channels | 0 | Count only; no target (traffic too low for statistical claims, per `zero-sales-diagnosis` §4) | Squarespace Orders |

### 2.3 Actions

Week 1 (21–27 Oct)
- Diagnostics check on Merchant Center (owner checkpoint 21 Oct, `owner-action-pack` E); I summarise screenshots into
  `business-os/feed/2026-10-2x-feed-qa.md` with a proposal TSV: stock fix for the 13 out-of-stock rows (needs owner
  inventory evidence) and variant-image flags.
- Owner: verify GSC + Bing Webmaster, submit sitemap, request indexing for the 5 priority PDPs + 5 categories; delete or
  noindex `/redesign-preview`; 301 `/home` to `/`.
- Owner: Pinterest bio link with UTM (`owner-action-pack` C); switch to business account, claim the website.
- Owner: Etsy Stats and listing export so I can baseline and score (`aw-etsy-listing` inventory step).
- Me: query to page map from the GSC export; Rich Results Test request for the 5 priority PDPs.

Weekly (every Monday, `business-os/seo/<date>-weekly.md`)
- GSC movers, query-to-page map updates, 5–10 pin briefs, 3 proposals. Log in `kpi-weekly.csv` notes the date of each
  owner-applied change (one change per page per 2 weeks).

Weeks 2–4 (28 Oct – 17 Nov)
- Category copy proposals (60–120 words, H1, meta) for sweaters, cardigans, vests; owner decides on hiding or merging
  Beanies and Sets (each has 1 product).
- Shop H1, home H1 space bug, alt text proposals for the 5 priority PDPs (descriptive, not file names).
- Pinterest: 5 boards by search theme (oversized wool sweaters, merino cardigans, sweater vest outfits, wool beanie gifts,
  wool gifts for her), 10 pin briefs per week, real product photos only, 1000x1500, UTM per board.
- Etsy batch 1: 5 listings scored and rewritten (title, 13 tags, attributes, description, photo order) to
  `business-os/etsy/`; price parity checked against `aw-unit-economics` before any parity proposal.
- Gift guide page on site (proposal in `business-os/proposals/`): "Wool gifts under EUR 50 / 120 / special"; uses real
  prices from `llms.txt`; no origin or "handmade" claim without owner OK.

Monthly (Nov, Dec; `business-os/seo/<date>-seo-review.md`)
- Indexation review, on-page check, schema request, `llms.txt` diff against the live site, Etsy batch of 5, feed QA after
  any photo upload.
- Seasonal keyword plan Oct–Dec: first version by 28 Oct (gift, winter, "merino cardigan", "oversized wool sweater").

Variant photos (blocks Pinterest catalog and clean MC approval)
- Owner uploads photos (`owner-action-pack` A). After that: I bind-check, regenerate-proposal, QA; owner re-uploads feed in
  one pass; check Diagnostics 24–72 h later. Do not re-upload before photos exist.

Christmas cut-offs
- Last-order dates per zone come from Operations. I do not post gift-delivery claims until they exist.
  Pin and feed content stops pushing out-of-stock or AMBER SKUs.

## 3. 2027 by quarter

Budget convention: monthly figures exclude salaries and ads unless stated. TODO = needs owner or Finance. No figure below
is a quote. The README tool cap (EUR 100–250/month, illustrative, `business-os/README.md` §8) is the only budget fact on file.

### Q1 2027 (Jan–Mar): fix foundations, win the long tail
- Goals: indexation complete; category landing pages ranking for their own terms; Merchant Center clean; Etsy listings
  all optimised once.
- KPIs (proposed, re-set after Q4 actuals): indexed share of sitemap at least 90%; non-brand top-10 queries at least 10;
  MC approved share at least 95%; Pinterest sessions month over month growth three months running; Etsy conversion above
  own Q4 baseline.
- Initiatives:
  - Winter sale-season content: "how to wash merino", "merino vs lambswool vs pure new wool", "oversized fit guide"
    (each links to 2–3 PDPs); FAQ phrased as real questions.
  - Category landing pages with real copy if Squarespace keeps canonical to `/shop` (`GROWTH-PLAN` S4).
  - Slug clean-up ONLY if owner approves a full redirect list; feed links and Pinterest pins must update in the same pass.
  - Etsy: remaining listings rewritten in batches of 5 per month (22 visible SKUs, so about 4 months); shop-level checks
    (About, policies, sections) aligned with `llms.txt`.
  - On-site reviews: only real ones collected after real orders; enable rating schema only when they exist.
  - Latvian pages (home, about, shipping, 5 bestsellers) as proposal, native speaker review required.
- Budget ask: EUR 0 paid. TODO: SEO tool (e.g. rank tracker) is optional; free GSC/Bing/Pinterest Trends suffice.
  TODO: native-speaker proofreading for Latvian (hours and rate unknown).

### Q2 2027 (Apr–Jun): spring/Mother's Day, scale what works
- Goals: seasonal pivot (lighter knits, gifts); first measured contribution per channel; Pinterest catalog live.
- KPIs: contribution per organic order (needs `sku-economics.csv` filled); Pinterest outbound clicks and sessions vs Q1;
  Merchant Center free-listing clicks vs Q1; GSC clicks at least 2x Q1 run-rate (proposal).
- Initiatives:
  - Pinterest catalog (feed upload) once variant photos are verified; shoppable pins for safe-to-promote SKUs only.
  - Mother's Day gift page and pins (Latvian and EU dates: TODO confirm).
  - Merchant Center: add free-listing extras (return policy, shipping details) if account settings allow; review
    Performance Max only as a Growth Marketing decision, not mine.
  - Monthly AI-visibility test, 10 fixed prompts x 4 assistants (`GROWTH-PLAN` idea 49).
  - Google Business Profile check against the studio address in `llms.txt` (owner action).
- Budget ask: EUR 0 paid. TODO: Pinterest promoted pins test budget is a Growth/GM decision, only after the Q1 data
  and CM2 per SKU exist.

### Q3 2027 (Jul–Sep): pre-season build
- Goals: autumn keyword and content ready by mid-Aug; Etsy and site listings refreshed with Q2 learnings.
- KPIs: autumn landing pages indexed by 31 Aug; seasonal queries in top 10 before 1 Oct; Etsy listing visits per listing
  vs same-month baseline; MC disapprovals 0.
- Initiatives:
  - Seasonal keyword plan v2 built from a year of GSC and Pinterest Trends data.
  - Content refresh of top guides; new styling guides tied to new products from Production.
  - Etsy second pass on listings (one change batch per listing per month, 30-day windows).
  - Hire decision point: SEO/Pinterest specialist or freelancer if order volume justifies it (`hiring-plan.md`, "Later").
- Budget ask: TODO. Part-time freelancer or hire cost unknown; decide at GM review with real contribution data.

### Q4 2027 (Oct–Dec): second gift season
- Goals: run the Q4 2026 playbook from week 1 of October, not week 5; compare against 2026 actuals.
- KPIs: year-on-year GSC clicks and impressions; MC approved items; Pinterest sessions; Etsy orders and revenue per listing;
  all judged against contribution after channel costs.
- Initiatives: gift guides live by 1 Oct; Christmas cut-off banner and pins per zone from Operations; PR and gift-guide
  outreach is Partnerships/Creative, I supply keyword and URL support.
- Budget ask: TODO. Any promoted Etsy listings or Pinterest ads require `aw-unit-economics` approval and owner sign-off.

## 4. Dependencies on other departments

| Need | From | By when |
|---|---|---|
| Variant photos per colour (beanie, turtleneck, set, cardigan blue) | Owner / Creative Content | Before MC re-upload and Pinterest catalog; ASAP |
| Safe-to-promote list, weekly capacity (GREEN/AMBER) | Production | Weekly; gates which SKUs I push |
| Physical stock truth (turtleneck 360 / beanie 220 look like placeholders; 13 out of stock) | Production / Owner | Week 1, for feed availability |
| SKU costs, minimum contribution per order | Production, Finance | Before any paid or promoted spend |
| Last-order dates per zone, delivery ranges per zone | Operations | Before gift content, mid Nov at latest |
| PDP copy, size info, measurements, delivery line | E-commerce / CRO | Rolling; SEO fields proposed jointly, one owner per page |
| GA4 ecommerce events, Clarity (plan upgrade decision) | GM / Owner | Without it, channel contribution cannot be measured past visits |
| Content for pins (real photos, video stills, captions in brand voice) | Creative Content | 5–10 per week from Nov |
| Creator and press links (backlinks, gift guides) | Partnerships | Nov; no bought links |
| Return policy wording, claim evidence | EU adviser / Owner | Before schema, feed or Etsy text uses it |
| Reviews for rating schema | CX | Real on-site reviews only |

I provide: query-to-page map, keyword sheet, pin briefs, feed QA, Etsy proposals, `llms.txt` diffs to all of the above.

## 5. Risks and owner decisions

### Risks
| Risk | Effect | Mitigation |
|---|---|---|
| Feed images do not match variants | Disapprovals or warnings, weak free-listing reach | Hold re-upload until photos; flag rows in QA |
| Feed says `in_stock` for 13 sold-out items | Account suspension risk, wasted clicks | Proposal TSV with stock from owner evidence; fix generator logic in a proposal, not a run |
| Claims on Etsy, feed, site (handmade, made in Latvia, sustainable, organic; legacy slugs and titles contain "sustainable", "organic") | Etsy handmade policy, Google misrepresentation, consumer-law exposure | Flag as CLAIM-CHECK; use "knitted on manual machines and finished by hand in Riga" only after owner confirms |
| Etsy price or policy mismatch with site; Etsy rules on off-platform links | Account risk, margin loss | No parity proposal without CM2 check; owner reads Etsy rules before any "move to site" wording |
| Low traffic makes data noisy (about 2 visits/day) | False conclusions | Sequential before/after, one change per page per 2 weeks, no split tests |
| Plan blocks Code Injection | No GA4 ecommerce events; no new scripts | Count orders from Squarespace Orders; keep upgrade decision visible |
| Slug changes break feed, pins, and links | Lost indexing | No change without owner-approved redirect list, done in one pass |
| Squarespace trial ends 1 Nov (duplicate site backup) | Loss of backup copy | Owner decision per `GROWTH-PLAN` idea 99 |
| Brand entity split (Mareshop vs Autumn & Wool, legacy FB/Pinterest handles) | Weak recognition in search and AI answers | Same name string everywhere after owner decision |
| AI-generated "ChatGPT Image" assets on store | Rights/provenance, Pinterest and Etsy policy | Real product photos only for pins and Etsy; owner confirms rights |

### Owner decisions needed (this week unless noted)
1. Verify GSC and Bing; delete or noindex `/redesign-preview`; 301 `/home`.
2. Pinterest: rename "mmareshop" to Autumn & Wool and keep followers, or open a new account (and update footer link).
3. Is Etsy/Mareshop still actively selling? Keep both channels open through the season?
4. Etsy review count wording: 1,400+ or 1,500+ on the site (owner pack D).
5. Evidence for "handmade", "made in Latvia/Riga" (also needed for Riga markets, `markets-and-gift-guides.md`).
6. Approve a slug clean-up and redirect list, or keep legacy slugs through 2027.
7. Hide or merge categories with a single product (Beanies, Sets).
8. Approve photo upload date and a single feed re-upload pass.
9. Plan upgrade (Code Injection) decision, or accept visit-only measurement.
10. Any promoted listing or Pinterest ad spend: not requested for 2026; revisit Q2 2027 with CM2 data.

### Unverified
- Live status of `llms.txt`, current GSC query list and top-10 count, Merchant Center approval counts after 21 Oct,
  Etsy Stats, Pinterest account state, Rich Results Test on PDPs. All need owner exports or screenshots.
