# Partnerships & Influencers plan, Q4 2026 and 2027

Status: DRAFT for owner approval. Written 2026-10-21 by `aw-partnerships`. Nothing here is sent, bought, shipped or
created. All targets are proposals, not forecasts. Unknowns are TODO / [VERIFY].

Success metric (`business-os/hiring-plan.md`): **profitable creator-attributed sales**, not reach or followers.

## 1. Starting point (facts from the repo)

| Fact | Source |
|---|---|
| Zero real direct-store orders to date. About 2 visits/day (64 visits in 30 days), Google 2 visits, Instagram/Pinterest referrals 0 | `zero-sales-diagnosis-2026-10-18.md` s1, `business-os/README.md` s2 |
| Click-trap overlay fixed 19 Oct. Stripe proven with test orders only. **PayPal not connected** | `business-os/README.md` s2 |
| GA4 `G-7TV8PK060Z` has pageviews only, no purchase events. Orders are counted from Squarespace Orders (and Etsy) | `business-os/README.md` s2, `aw-utm-attribution` s1 |
| So a **discount code per creator is the primary attribution key**, UTM is secondary | `aw-utm-attribution` s1, s3 |
| Per-code usage limits and per-code order reports on the current Squarespace plan: UNVERIFIED | `aw-utm-attribution` s3 |
| Proof asset: Mareshop/Etsy, about 8.2k sales, about 1.5k reviews, 4.9 stars, 15 years. Marketplace history, not direct-store sales. Must be attributed to Mareshop on Etsy | `business-os/README.md` s2, `zero-sales-diagnosis-2026-10-18.md` #5 |
| Product costs in `sku-economics.csv` are **all empty** (82 rows, 22 visible). So gift cost and break-even CAC are unknown, and every paid brief is BLOCKED | `business-os/sku-economics.csv`, `business-os/ai-team.md` decision 1 |
| Prices: beanie EUR 45, hat and scarf set EUR 110, turtleneck EUR 110, sweaters EUR 126-165 (incl. 21% VAT). Ex-VAT beanie is about EUR 37.19 (45 / 1.21). Contribution after costs: TODO | `business-os/sku-economics.csv` |
| Stock: turtleneck 360 and beanie 220 look like made-to-order placeholders. Most sweaters are stock 1-16. Physical stock unconfirmed | `business-os/ai-team.md` decision 2, `sku-economics.csv` |
| No `capacity-YYYY-Www.md` exists yet. Gift only GREEN/AMBER SKUs, so the SKU list is **MISSING** | `ai-team.md` hand-offs, `aw-production-capacity` |
| No `business-os/partnerships/` folder, tracker, shortlist or utm-links.csv exists yet | repo glob 2026-10-21 |
| Claims "handmade", "sustainable", "made in Latvia" unverified. The Doma laukums market asks for proof of Latvian production | `business-os/README.md` s7, `markets-and-gift-guides.md` header |
| Variant photos missing for beanie, turtleneck, hat set, blue cardigan. Variant bug on the cardigan (Brown/Blue shows Black) | `owner-action-pack-2026-10-19.md` A, `zero-sales-diagnosis-2026-10-18.md` #1 |
| No delivery-time info in checkout. Gift buyers need it, and creators' followers will bounce without it | `zero-sales-diagnosis-2026-10-18.md` #2 |
| Idea backlog: 66 (micro-influencers LV/DE/Nordics, gift for an honest post), 65 (UGC from past Etsy buyers), 71 (Riga cafe/bakery shoot and giveaway) | `GROWTH-PLAN-100-IDEAS.md` |
| Press and gift-guide pitches (neighborhood.lv, TVNET Egoiste, Santa.lv, etc.) are already drafted. That is PR, not creators, and sits with Growth/Brand | `markets-and-gift-guides.md` s3-4 |
| Wave 4 hire (Partnerships Specialist) only "when creator tests show profitable orders". Until then this agent drafts, the owner sends | `business-os/hiring-plan.md` |

Honest read: with about 2 visits/day, creator traffic is one of the few ways to get buyers to a store that has no
search presence. But a creator who sends 200 followers to a page with no delivery times, no PayPal and unclear
sizing will produce clicks and no orders. Fixes in s4 gate the programme.

## 2. Q4 2026 (21 Oct - 31 Dec)

### Goal
Run a small, honest gifting test (5-10 creators, per README days 31-60) and learn whether creator gifts acquire
buyers below break-even CAC. Do not expect scale. Peak season is short: **creator content must be live by about
mid-Dec** to help gift orders. Last-order and delivery dates: TODO from Operations.

### KPIs and targets (baseline for all: 0)

| KPI | Target by 31 Dec | Note |
|---|---|---|
| Creators scored and shortlisted (>= 9/14, no red flags) | 20 | Research only, public data |
| Creators contacted (owner sends) | 10-15 by 14 Nov | Per `hiring-plan.md` 10-20 |
| Reply rate | Track, no target. Expect low | Report honestly |
| Gifts shipped (owner approves each) | 5-8 by 30 Nov | Cap pending owner decision D2 |
| Post rate of gifted creators | >= 50% of shipped | Gift is no-obligation, so low is normal |
| Disclosure compliance on posted content | 100% | Hard rule 5. Fix or ask creator to edit |
| Orders with a creator code | >= 3 | Target, not a forecast. Zero is a valid reported result |
| Creator cost per attributed order vs break-even CAC | <= break-even CAC | Break-even CAC = TODO until costs are filled |
| Reusable assets with written usage rights | >= 5 images/clips | Ask separately, in writing |
| Gifting spend | <= owner-approved cap (TODO EUR) | = gifts x cost per gift |

### Weekly actions (agent drafts, owner approves and sends)
- Shortlist update, scored per `aw-creator-outreach` s2. Markets: Latvia first, then DE and Nordics.
- 3-5 personalised DM drafts in `business-os/partnerships/`, each citing a specific post. One follow-up max, after 7 days.
- Update `creator-tracker.csv` (statuses shortlisted to closed).
- Disclosure check on any posted content (`#reklama`, `#apmaksats`, `#sponsorets` or the paid-partnership label).
- Per agreed creator: brief, proposed `HANDLE10` code, UTM link (`creator-<handle>`, `affiliate`, `gifting-2026-11`), gift spec (SKU/size/colour/cost).
- Attribution readout: "platforms claim N, we can verify M" from Squarespace Orders by code.

### Calendar

| When | Action |
|---|---|
| Wk of 21 Oct | Needs from owner: costs for the gift SKUs, capacity list, decisions D1-D4. Agent builds tracker, scoring sheet, first 20 candidates |
| By 28 Oct | First 5 DM drafts ready. Brief and code scheme drafted. Tracking ready before any outreach |
| 28 Oct - 14 Nov | Owner sends in batches of 3-5. Agreed creators get gift spec |
| By 30 Nov | Last gifts shipped so creators can post by mid-Dec. Date depends on carrier time: TODO |
| Mid-Dec | First monthly creator report (Nov data). Disclosure audit |
| 31 Dec | Q4 readout: contacted, replied, shipped, posted, orders, cost per order, assets gained |

### Cheap extras (owner-approved only)
- Idea 65: ask past Etsy buyers for photos with a small thank-you. Needs consent wording and an Etsy-compliant route [VERIFY Etsy rules on moving buyers off-platform]. Coordinate with CX.
- Idea 71: one Riga cafe/bakery shoot. Only if Creative has capacity. Low priority in Q4.

## 3. 2027 by quarter

All 2027 targets depend on Q4 results. If gifting fails the break-even test, Q1 changes the deal or stops. Budget
numbers are TODO until `sku-economics.csv` is costed.

### Q1 2027 (Jan-Mar): verdict and cleanup
- Goal: day-90 programme verdict (does gifting or affiliate acquire below break-even CAC?) and wave 2 terms.
- KPIs: verdict delivered by 31 Jan. Every Q4 creator closed, repeat or ambassador with reasons. >= 80% of Q4 usage rights documented. Tracker 100% complete.
- Initiatives: Q4 post-mortem. Thank-you and feedback note to every gifted creator (owner sends). Standard usage-rights template (3-6 months, written) [legal review: D5]. Pause or light-touch gifting in Jan (post-season, stock low).
- Budget ask: TODO (gifts x cost, only if verdict is positive). Default: EUR 0 new spend in Jan.

### Q2 2027 (Apr-Jun): wave 2, spring/early-autumn content
- Goal: replicate whatever worked. 10-15 creators on an updated deal (gift + code, optional commission if owner approves and `aw-unit-economics` shows headroom).
- KPIs (proposed): >= 10 creators contacted per month. Net revenue ex VAT per creator reported monthly. Creator-attributed orders per month: TODO set after Q4 baseline. Cost per attributed order <= break-even CAC. Disclosure 100%.
- Initiatives: affiliate pilot with 2-3 best creators (up to about 50k followers per skill). Add DE and Nordic creators, with national disclosure rules checked by an adviser [VERIFY]. Hand best assets to Growth/Creative as ad creative, **only** with written rights.
- Budget ask: gifts + commission pool, TODO EUR.

### Q3 2027 (Jul-Sep): autumn pre-season
- Goal: be booked early. Creator content for autumn knitwear lands in Sep, ahead of the gift season.
- KPIs: >= 5 repeat or ambassador creators signed by 31 Aug. Ship autumn gifts by mid-Aug so content is live from early Sep. Creator-attributed share of orders: TODO.
- Initiatives: ambassador programme (2-5 creators, longer term, a clear per-creator contribution case). Seasonal creator brief. Decide on the hire of a Partnerships Specialist only if Q1/Q2 show profitable orders (`hiring-plan.md` wave 4).
- Budget ask: TODO. Cash fees only if owner decides and unit economics support them.

### Q4 2027 (Oct-Dec): peak
- Goal: first full-season run with data. Creator codes live for gift season. Content ready by mid-Nov (earlier than 2026).
- KPIs: creator-attributed orders and net revenue ex VAT vs 2026 Q4 (target TODO). Cost per order <= break-even CAC. Post rate >= 60% of shipped. Disclosure 100%. Assets with rights >= 15 for the year.
- Initiatives: gift-guide creator roundups. Giveaways only with disclosure and clear rules, owner approved. Year-end report and 2028 terms.
- Budget ask: TODO (gifts, commission, any approved fee), set from 2027 Q2-Q3 results.

## 4. Dependencies on other departments

| Needs | From | Why / blocker |
|---|---|---|
| Costed `sku-economics.csv` (gift SKUs first) and capacity file with GREEN/AMBER SKUs | Production, Finance | No gift cost, break-even CAC or safe SKU list today |
| Confirm physical stock for beanie/turtleneck | Production | 360/220 look like placeholders. Don't gift what can't ship |
| Delivery times in checkout, PayPal connected, size info, variant photos and the cardigan variant fix | E-commerce/CRO, Owner | Creator traffic will leak on these (`zero-sales-diagnosis-2026-10-18.md`) |
| Squarespace discount feature check (per-code limits, order report by code) | E-commerce/CRO | Primary attribution key. Without it, per-creator reporting is manual from Orders |
| Plan upgrade for Code Injection (GA4 purchase events) | Owner, GM | Without it, creator sessions can't be tied to purchases |
| Verified claims wording (fibre, "Riga", handmade) | Owner, Production | Used in every DM and brief. Until then: "knitted on manual machines and finished by hand in Riga" per `ai-team.md` |
| `aw-brand-voice` review on drafts | Creative | Every customer-facing draft |
| Gift packaging and parcel handling, shipping labels | Operations | Owner ships parcels. Needs carrier cost and dates |
| Creator content reuse as ads | Growth | Only with written usage rights, and by `aw-paid-ads-testing` rules |
| Monthly creator cost into `kpi-weekly.csv` (`creator_cost_eur`) | GM, Finance | Sheet is empty today |
| Newsletter capture and welcome email for creator visitors | CX/CRM | Non-buying visitors from creators should have somewhere to go (`campaign-assets/welcome-email-draft.md`) |

## 5. Risks and owner decisions

### Risks

| Risk | Mitigation |
|---|---|
| Traffic goes to a leaky store, so a good creator test looks like a failure | Gate shipping gifts on delivery times and PayPal (D1). Don't judge channel from GA4 alone |
| Gift cost exceeds break-even CAC | Fill costs first. Gift lower-cost SKUs (e.g. beanie, hat and scarf set) once costed. Stop or change the deal if over budget within 60 days |
| Season too short: content late | Hard date for last parcel (about 30 Nov, TODO). After that, Q4 ends in a readout, not more gifting |
| Undisclosed or vague posts (EU/PTAC) | Brief requires disclosure. Weekly check. Never hide the relationship |
| "Made in Latvia" or "handmade" appearing in drafts or creator posts | Banned until verified. Brief lists words to avoid |
| Fake engagement or wrong audience | Scoring sheet, no scraping, no bought data. Red flags exclude |
| Low reply rate, zero attributed orders | Report honestly. Switch to cheaper gifts or the UGC route (idea 65) |
| Overlap with PR gift-guide pitches | One owner per outlet. Partnerships does creators, Growth/Brand does media |
| Squarespace can't report by code | Manual count from Orders by code each week. Add a "how did you hear" question [VERIFY plan support] |

### Owner decisions needed

| # | Decision | Needed by |
|---|---|---|
| D1 | Do creator gifts wait for PayPal + delivery times + size info, or start earlier at your risk? | 28 Oct |
| D2 | Q4 gifting cap: number of gifts and max EUR per gift (agent proposes after costs are filled) | 28 Oct |
| D3 | Which SKUs to gift (after capacity file). Confirm beanie/turtleneck stock | 28 Oct |
| D4 | Approve the shortlist, each DM, and every gift. Who sends from which account | Weekly |
| D5 | Discount size for `HANDLE10` codes, any commission, usage-rights terms and length. Legal check of the terms | Before first agreement |
| D6 | Verify "handmade" / "Riga" / "made in Latvia" wording | Before first DM |
| D7 | Squarespace upgrade (Code Injection) for purchase tracking | Q4 if possible, else Q1 |
| D8 | Q1-Q4 2027 budget (TODO) and whether to hire the Partnerships Specialist after the day-90 verdict | 31 Jan 2027 |

MISSING today: gift cost per SKU, break-even CAC, capacity file, tracker/shortlist files, creator names (none
researched yet, none invented), discount code feature check.
