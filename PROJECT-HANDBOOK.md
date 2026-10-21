# 🧶 Autumn & Wool — Project Handbook
**Store:** https://www.autumnandwool.com/ (Squarespace 7.1, EUR base)
**Admin:** https://rose-tarpon-ld9w.squarespace.com/config/
**Owner brand context:** Formerly Etsy shop "Mareshop" (etsy.com/shop/Mareshop — 4.9★, 1.5k reviews, 8.2k sales, 15 years).
**This document is the memory of every investigation, fix, decision, and open item.** Update this file after every
pass. Companion detail files are listed at the end.

---

## 1. The one-line history
On 2026-10-18 an ego Lite audit diagnosed visible blockers (no PayPal, no delivery times, variant bug, etc.)
and hypothesized "traffic first, conversion second." Overnight 2026-10-19 a deeper investigation found the
**real root cause of zero sales: an invisible full-screen overlay (`.sqs-widgets-confirmation-overlay`) that
Squarespace mounts after a failed Add-To-Cart attempt and never removes**, swallowing all subsequent clicks.
Everything else was downstream noise. Overnight rounds 1–19 fixed the defect classes end-to-end and re-queued
the traffic flywheel. Goal marked complete with all verifiable layers green at 02:0X EET 2026-10-19.

---

## 2. Environment & access memory (so next pass starts fast)
- **Squarespace admin**: `rose-tarpon-ld9w.squarespace.com/config/…` — logged in (dsn patched into ego session).
- **ego-browser TaskSpaces used**:
  - `autumnandwool-admin-fix` — id **17**, admin-ready page `p1` (login automation included).
  - `autumnandwool-zero-sales-audit` — id **14**, storefront page `p----------------------------------------------------------------------1` (click/buy flow testing).
- Both remain persistent on disk; ego reuses them by name. One Squarespace editing session at a time (always via space 17/p1).
- Page budget: safe ops ≈ 6–8 pages per task space per run.

## 3. Plan-gated features on this site** (learned hard, don't attempt again)**
- **Custom Code Injection**: 403 — plan gate.
- **Inline `<script>` inside a page code block**: hard gate ("premium blocks") — dismiss with Escape without saving to avoid persistence.
- **Waitlists** and some marketing blocks: gated as well.
- **Working layers**: Custom CSS panel (no latent validation), product metadata editors (Fields/Inventory/Organization/Taxes tabs), the commerce list UI itself, checkout iframe locators (labels + auto-submit behavior), Merchant Center + Search Console surfaces.
- The Squarespace page (visual) editor works but is fragile: **the CM6 inline code-block editor loads the doc lazily (3 windows × ~1.5k chars); a paste/ctrl+a inside it only sees the visible window. Pasting to an about-block corrupted the AW About page to "+!$…)#.${%s2*P' like garbage" — recovered by walking the CM6 doc: window sweeps 0→1409→2764→4096 and re-typed the doc **window by window** (CM [first] tab in custom CSS panel accepts setValue but on Custom CSS; use product metadata editors first).

## 4. THE ROOT-CAUSE DETAIL (carry this identity into every future investigation)
- Failed ADD'd `product-space-form` submit leaves `<div class="sqs-widgets-confirmation-overlay">`
  + a `.yui3-widget.sqs-widgets-confirmation` element in DOM with **opacity:0, z-index:999999, pointer-events:auto**.
- Neither class is a pointer-events exception from Squarespace. The overlay is a 100vh/100vw barrier — therefore
  ALL later clicks on the page (and on STATE click-delay) are swallowed. User-visible symptoms: "unclickable",
  "blank page at Purchase step", "radio buttons not clickable".
- **Fix (live)**: Custom CSS panel appended:
  ```css
  .sqs-widgets-confirmation-overlay{pointer-events:none !important;}
  .sqs-widgets-confirmation{pointer-events:none !important;}
  ```
  Verified live: after fail-click → the overlay remains but pointer crosses it; radio buttons are clickable;
  add works; hint text appears instead of nothing. Full passes on cardigan + beanie.

## 5. Fixes shipped overnight 2026-10-19 (verified live)
1. Overlay click-trap CSS (above).
2. **Cardigan truth**: product title "Black Merino Wool Raglan Cardigan 100% Merino Wool — Raglan Sweater,
   Minimalist Knitwear, Sustainable Handmade Womens Cardigan" → **"Merino Wool Raglan Cardigan"**; description now
   states "available in Black, Brown, and Blue — select your colour below" and per-swatch "swatch = colour" hint
   at the top. SEO title "Merino Wool Raglan Cardigan — Black, Brown or Blue | Autumn & Wool". Brown-variant feed
   image re-pointed to `image_10.jpg` (actual brown photo already in gallery; feed re-uploaded 2026-10-19 01:31 EET).
3. **Buying-detail consistency**:
   - `/shipping-returns`: exchange copy now says "place a new order for the right item and return the original"
     (matches FAQ).
   - `/faq`: identical exchange flow + returns condition wording hit both "unused" and "unwashed" language.
   - Every PDP with a `/size-guide` mappable product: a small line **"📏 Need sizing help? View our size guide"**
     placed via Custom CSS 20px under the Add-To-Cart button (CSS-only because plan-gated HTML/script is out).
4. **Merchant Center rebuild**:
   - Prior: 2 auto items, 45 auto-targeted countries, zero shipping services — approval blocked.
   - Now: 98 primary rows (85 in-stock, 13 out → auto-excluded later); business-info countries trimmed to
     **Latvia + 18 EU + US/CA/AU/UK/NO/CH**; custom shipping services (free, 4–10 business days) per region.
   - Diagnostics clean after the 01:31 re-upload. Approved>0 due by **2026-10-21** (24–72h window).
5. **Contact form safety**: the mailto: form used `method=post` → Chrome security interstitial. CTA hidden via CSS,
   guidance text rendered instead: "Email us at autumnandwool@gmail.com — we reply within 24 hours." (CSS-only).
6. **Vest restock** from 0→1 (Own pair ordering OK; Public + live).
7. **Homepage "Shop by Category" cards relinked** from /shop category pages to real PDPs (customers keep context).
8. Verified **third-party "Website Speedy" scripts are absent** from live HTML.
9. Verified GA4 tag G-7TV8PK060Z loads + one `collect` beacon per page after cookie accept (consent chain healthy);
   ecommerce events (`view_item`, `add_to_cart`, `purchase`) NOT emitted — hard plan gate (no Code Injection).

## 6. Verified WHAT'S HEALTHY (don't touch)
- Homepage → Shop → PDP → Cart → Checkout (Squarespace Secure Checkout) all HTTP 200.
- Cart math correct, shipping €0 + tax €0 shown. Cookie banner behaves.
- Mobile 390px: no horizontal scroll. Page speed ~1.2s.
- robots.txt + sitemap.xml + canonical + Product schema all correct.
- Newsletter + Contact + Account Registration flows work.
- Store catalog: 22 live shop cards; no sold-out live items after vest restock.

## 7. Measurement baselines (don't lose these numbers)
| Metric | Value |
|---|---|
| Squarespace 30-day visits (10/17) | 62 (94.34% bounce, 27s mean dwell) |
| GSC 90d (10/19) | 11 clicks / 388 imp / 2.8% CTR / vec pos 14.1 |
| GSC indexing (10/19) | 37 known, 11 indexed, 4 not-indexed |
| MC state (10/19) | 98 upload, 0 rejected, 0 approved (== 98 issue-free) |
| Orders placed | 2 (orders #00003 desktop + #00004 phone—both test&refunded) |
| GA4 function | page_view OK; ecommerce events absent (plan-gated) |
| Etsy Mareshop (for trust copy) | 4.9 (1.5k), 8.2k sales, 15 years |

Query clusters visible in GSC: "oversized merino wool sweater" pos 27, "timeless knitwear" pos 5.9,
"wool size chart" pos 44 — fastest organic growth paths.

## 8. Open items the OWNER must do (none are codable without owner assets)
1. **Photography** (51 photos): Beanie ×11 colours, Turtleneck ×12 colours (each size too if possible),
   Hat&Scarf ×2 (Brown, Gray), Cardigan Blue ×1. Attach at Inventory → Variants → EDIT ALL → tap variant →
   Upload variant image. Straight after, the assistant binds them to variants + re-uploads the feed in one pass.
2. **PayPal connect** (Selling Tools → Payments).
3. **UTM-logo-bio links** (IG/TikTok/FB/Pinterest/Etsy) — URLs pre-baked in owner-action-pack file.
4. **Trust copy bumps**: both "1,400+" strips in home to **"1,500+"**.
5. **Decide duplicate beige vest** (publish second Public product or delete hidden duplicate).
6. Google Feed re-upload *only after* variant photos are bound (else the mismatch-risk surface persists).

## 9. Scheduled checkpoints (2026-10)
- **21 Oct**: MC Diagnostics — Approved ramps; if the 48 "same-image-multi-color" rows get flagged
  individually → trim exact rows and re-upload.
- **24 Oct**: weekly measurement delta — window anchored 20 Sep–19 Oct + trailing 7 days.

## 10. Companion artifacts (in `/Users/eramadan/autumnandwool/`)
- `incident-veil-blocker-2026-10-19.md` — master incident/engineering log, round-by-round tables.
- `weekly-measurement-report-2026-10-19.md` — measurement baseline + funnel instrumentation state.
- `owner-action-pack-2026-10-19.md` — every owner-facing action copy-pasteable.
- `autumnandwool-google-feed.tsv` — the live uploaded feed (98 rows).
- `evidence/ego-2026-10-18/SESSION-NOTES.md` — technical ego-session learnings (selectors, workflows, traps).
- `zero-sales-diagnosis-2026-10-18.md` (earlier day audit).
- `implementation-report.md` (earlier implementation+QA report).

---

## 11. Status snapshot (as of 2026-10-19 02:0X EET)
| Indicator | State |
|---|---|
| Storefront | ✅ fully sellable; every blocker on the order path is lifted |
| Stripe chain | ✅ proven (orders #00003 & #00004 placed + refunded) |
| Google Merchant Center | ⏳ 98 items queued, diagnostics clean, approved=0 until review lands |
| Google Search Console | 🟡 indexed/recovering; baseline captured |
| Variant color↔image risk surface | 🟡 48 rows remain (await owner's photography) |
| PayPal | ⏳ pending connect (owner) |
| Social UTM coverage | ⏳ pending pasting into bios (owner) |
| Overall | 🟢 **ready for traffic**; only calendar + owner-side feeds the next lift |

**Next concrete action**: once the owner uploads variant photos, run one binding + feed re-upload pass;
the assistant has the CM6/admin script recipe + product selectors ready to deploy.
