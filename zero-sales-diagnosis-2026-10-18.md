# Zero-sales diagnosis — autumnandwool.com

**Audited live with ego lite (ego-browser):** 18 October 2026, ~23:10–23:30 EET.
**Method:** real browsing session — home, shop, product, variant selection, add-to-cart, full checkout up to the payment step (no order placed, test email only), mobile emulation at 390px, robots.txt. Cross-checked against the Squarespace/GA4 baseline in `weekly-measurement-report-2026-10-17.md` and `QA-REPORT.md`.
**Browser space:** `autumnandwool-zero-sales-audit` (spaceId 4), finished. Test cart emptied where possibly; one cardigan line may persist in the audit browser profile only — customers are unaffected.

---

## 1. The headline finding: this is a TRAFFIC problem first, conversion second

| Baseline metric (19 Sep–18 Oct) | Value | Reading |
|---|---:|---|
| Visits / unique visitors | 64 / 64 | ~2 visits/day. Statistically nothing can convert at this volume. |
| Google as source | **2 visits** | The store is effectively invisible in search. |
| Instagram / Pinterest referrals | 0 | Social accounts produce no traffic yet. |
| Merchant Center products | 2 discovered, **0 approved, no shipping policy** | Not in Google Shopping at all. |
| Bounce rate / avg time on page | 95.95% / 27s | People who do arrive leave almost immediately. |
| Add-to-cart / checkout / purchase events | Not verified in GA4 | The funnel cannot even be measured today. |

Even a world-class store converts at ~1–3% of visits. At 64 visits/month, **zero orders is the expected outcome** — but the 96% bounce rate and the conversion-path defects below mean that when traffic arrives, it will still leak if these are not fixed.

## 2. Issues found live today (ego-browser evidence)

### A. Conversion killers (fix before buying any traffic)

| # | Severity | Issue | Evidence | Fix |
|---|---|---|---|---|
| 1 | **Critical** | **Variant deception bug confirmed.** Selecting "Brown" (or "Blue") on the cardigan leaves the H1 "Black Merino Wool Raglan Cardigan", the gallery unchanged, and the cart/checkout line reads "Black Merino Wool Raglan Cardigan — Primary color: Brown". A buyer cannot tell what they are getting. | [04-product-brown-selected.png](evidence/ego-2026-10-18/04-product-brown-selected.png); checkout summary in round 5 output | Assign per-variant images + variant names in the Squarespace variant UI, **or split Black/Brown/Blue into separate products**. Cleanest: separate products — also gives 3 indexable URLs instead of 1. |
| 2 | **Critical** | **No delivery-time information anywhere in checkout.** Only "Free shipping knitwear FREE". Squarespace shipping config has no delivery-time ranges. This also blocks Merchant Center approval. | Checkout rounds 5–8; measurement report 18 Oct | Add realistic ranges per zone (e.g. EU 3–7 days, US/UK 7–14 days) in Squarespace shipping settings; show "Ships from Riga in 2–5 working days · delivery in X–Y days" on every product page. Required for gift buyers (your core season is now). |
| 3 | **High** | **No PayPal.** Checkout offers Stripe (card + Google Pay iframes observed). No PayPal, no visible express checkout at the email step. | `js.stripe.com` iframes incl. `payment-request-inner-google-pay`; no PayPal signal | Connect PayPal in Squarespace Payments. For EU/US gift purchases PayPal is a meaningful share; absence reads as "small risky shop". |
| 4 | **High** | **No size selector on garments** (vest, cardigan) and measurements inconsistent (cm only vs cm+in). Knitwear × no size guidance = no purchase. | Product rounds 2–3; QA-REPORT §2 | Add size variants or, if 1–2 sizes, state it explicitly with flat measurements on every product in the same format. Design already specifies a size selector. |
| 5 | **High** | **"4.9 from 1,400+ reviews on Etsy (as Mareshop)"** is the only social proof, and it points to a *different shop name* with no link or evidence. Combined with legacy handles (Facebook "AccessoriesMareshop", Pinterest "mmareshop") it undermines the brand it tries to support. | Product page snapshot round 3; nav links round 1 | Either link the claim to the actual Etsy review page, or rebuild proof locally: 3–5 customer quotes/photos with first names + country. Update/remove legacy social accounts. |
| 6 | **High** | **Returns wording contradicts itself**: Shipping page "unworn, unused", FAQ "unworn, unwashed". | QA-REPORT §5 | One standard wording everywhere, e.g. "unworn, unwashed, in original condition, 14 days". |
| 7 | **Medium** | Checkout shows "Black Merino Wool Raglan Cardigan — Primary color: Brown" (product-name/variant mismatch continues into the order summary — same root cause as #1, confirmed at the payment step). | Round 8 order summary | Fixes with #1. |

### B. Search-visibility defects (why Google sends 2 visits)

| # | Severity | Issue | Evidence | Fix |
|---|---|---|---|---|
| 8 | **High** | **Merchant Center not live**: no shipping policy configured, 0 owner-provided products, 0 approved. The prepared feed `autumnandwool-google-feed.tsv` is not yet effective (0 owner-provided products). | Measurement report 18 Oct | Finish Merchant Center: shipping policy (free + delivery times), upload the TSV feed, resolve disapprovals. Free listings + Shopping tab for 20+ knitwear SKUs is the single biggest traffic lever this season. |
| 9 | **High** | **Shop page has no H1** (h1 count = 0). "The collection" heading exists as text but not as H1. | Round 3 DOM check: `h1count: 0` | Add one visible H1, e.g. "The collection — handmade wool knitwear from Riga". |
| 10 | **High** | **Image alt text is raw file names** ("IMG_3336.JPEG") across the catalog; shop tiles have empty alt. Zero image SEO; weak accessibility. Also: stored shop images carry "ChatGPT Image …" file names — verify provenance/licensing before ads; rename files descriptively (e.g. `merino-wool-raglan-cardigan-black.jpg`). | Round 2 `imgAlts`; QA-REPORT §4 | Write descriptive alts per gallery image (Squarespace image editor → filename/alt). Rename AI-generated assets honestly; confirm they are permissible for your listings. |
| 11 | **Medium** | **Legacy Etsy slugs**: ~35 products live under `/shop/p/p/…-679510` (double `/p/p/`, SEO-keyword-stuffed, numbered). Long ugly URLs depress CTR and look like a migrated marketplace listing. | Cardigan links round 3 | Where feasible, set clean slugs; add 301 redirects in Squarespace URL Mappings for any changed URL. Note sitemap still lists `/home` and `/shop/gift` — remove. |
| 12 | **Medium** | Title tags: duplicated brand suffix ("… \| Autumn & Wool — Autumn & Wool"), marketing filler ("Explore FAQs & Shop with Confidence"), cart title is generic "Autumn & Wool". | QA-REPORT §5; cart round 5 (`title: "Autumn & Wool"`) | Short, page-specific titles: "Your cart \| Autumn & Wool", drop duplicated suffix. |
| 13 | **Medium** | Home H1 renders as "**Wool knitwearfor cooler days**" (missing space at the line break) — the first words a visitor and Google read. | Round 1 `h1s` | Insert a space/soft line-break fix in the hero block. |
| 14 | **Low** | Product names are SEO strings ("Merino Wool Raglan Sweater — Dusty Pink Oversized Jumper"). | QA-REPORT §5 | Short display names + keywords in description, not the name. |

### C. Trust hygiene (smaller, quick)

| # | Severity | Issue | Fix |
|---|---|---|---|
| 15 | Medium | No announcement bar detected on home now (`announcementBar: null`). Free-shipping/14-day-returns/handmade-in-Riga claim should be persistently visible in exactly ONE place. | Re-enable announcement bar **or** the trust row — not both, not neither. |
| 16 | Medium | Privacy policy has no "Last updated" date; names Google Analytics while GA requests were not observed on first load. | Add the date; verify which analytics actually fire and align. |
| 17 | Low | Duplicate Instagram CTAs (custom grid + native block + header/footer icons). | Keep one. |
| 18 | Low | Footer links/social icons ~20–25px tap targets on phone (below the ~44px guidance). | Increase padding in footer CSS. |

### D. Verified working (do not spend time here)

- Checkout completes end-to-end to the payment step; totals/tax/shipping (FREE to US 10001) compute correctly. [08-checkout-payment.png](evidence/ego-2026-10-18/08-checkout-payment.png)
- Stripe live with card + Google Pay elements; multi-currency on; test mode OFF; SSL ok.
- Mobile 390px: no horizontal scroll on home/product; hero CTA "Shop the collection →" visible. [09-mobile-home.png](evidence/ego-2026-10-18/09-mobile-home.png) [10-mobile-product.png](evidence/ego-2026-10-18/10-mobile-product.png)
- Desktop load fast (DOM ready ~0.4s, load ~1.2s). robots.txt standard and correct, sitemap declared, canonical correct, Product JSON-LD with price/availability on product pages (good — ready for Shopping once Merchant Center is fixed).
- Previously reported "blank page after clicking Purchase on the beanie" **not reproducible** today (add-to-cart worked, stayed on page). Treat as transient; retest once weekly.
- Size Guide link now present in header nav (QA finding resolved).

## 3. Prioritized plan

**Week 1 — stop the leaks (all small, all in Squarespace admin):**
1. Fix the Brown/Blue cardigan variant (per-variant images or split products) — #1/#7.
2. Add delivery-time ranges per shipping zone + show delivery estimate on product pages — #2 (unblocks #8).
3. Finish Merchant Center (shipping policy → upload `autumnandwool-google-feed.tsv` → fix disapprovals) — #8.
4. Add size info to every garment — #4. Reconcile returns wording — #6. Fix the hero H1 space bug — #13.

**Week 2 — make the store buyable:** connect PayPal (#3), repair social proof: link the Etsy claim or replace it with named customer quotes (#5); update/retire legacy Mareshop FB/Pinterest handles (#5); one announcement/trust location (#15); one Instagram CTA (#17).

**Week 3 — SEO base:** Shop H1 (#9), image alts + file renames incl. the "ChatGPT Image" assets (#10), titles (#12), clean slugs + 301s and sitemap cleanup (#11), remove `/home` and `/shop/gift`.

**Week 4 — turn the tap on:** publish the already-drafted campaign posts with UTM links (`campaign-assets/campaign-drafts.md`); Pinterest first (knitwear's highest-intent organic channel; Product schema already qualifies rich pins); then consider a small Shopping/PMax test once Merchant Center is green.

**Measurement before traffic spend:** place one Squarespace **test-mode order** to verify GA4 `add_to_cart`/`begin_checkout`/`purchase` events actually fire (today they are unverified, so every future optimization decision would be blind), then revert to live mode. Re-run the weekly snapshot from `weekly-measurement-report-2026-10-17.md` with the same window definition.

## 4. Honest expectation setting

With ~2 visits/day, even a perfect store shows 0 orders most months. Realistic sequence: fix conversion killers + Merchant Center → organic/Shopping traffic climbs into the hundreds of visits/month → first orders become statistically possible, and GA4 ecommerce events will then tell you which remaining step leaks. Selling knitwear in October means the next 8–10 weeks are the season — weeks 1–2 items above are the ones to do *now*.
