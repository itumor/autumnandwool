# INCIDENT REPORT — Invisible Overlay Soft-Lock on the Store (Resolved 2026-10-19)

## Severity: Critical (directly tied to zero-sales)
A failed **Add To Cart** click (variant not pre-selected) left an **invisible full-screen overlay**
(`div.sqs-widgets-confirmation-overlay` + its `div.yui3-widget.sqs-widgets-confirmation` dialog)
that swallowed **every subsequent click** on the page until reload. A visitor who tapped
"Add To Cart" before picking a colour could never recover: colour radios, cart, navigation—all dead.

## Root cause (deterministic evidence)
1. Cardigan shows `Please select the Primary color option.` only as a small inline hint; no default variant.
2. On the failed click, Squarespace's confirmation machinery shows the overlay at `opacity:0` with
   `pointer-events:auto; z-index:999999`, covering the WHOLE viewport.
3. `elementsFromPoint` at the Black radio centre: topmost layers = `.sqs-widgets-confirmation-content` + veil.
4. Radio click while veiled never registers (`checked` never flips); the veil never auto-clears (12s+ sample window).
5. Selecting Black explicitly and clicking Add To Cart works fine (qty increments).

## Fix shipped (Custom CSS — plan has no Code Injection)
`Website → Pages → Custom CSS` (accessible under this plan; Code Injection API is 403-gated):
```css
/* A&W Critical Fix (19-Oct-2026) */
.sqs-widgets-confirmation-overlay{pointer-events:none !important;}
.sqs-widgets-confirmation{pointer-events:none !important;}
```

## E2E verification after fix (2026-10-19 Europe/Riga)
- Failed Add To Cart → hint shown → **Black radio clickable post-fail** (checked=true) → Add To Cart → cart = 1 ✓
- Success-path confirmation ("Added!") still renders (inside the button wrapper, unaffected by the overlay rule).
- "Website Speedy" third-party scripts (3 files from `websitespeedycdn5.b-cdn.net/speedyscripts/ecmrx_11679_*`)
  are **absent from live page HTML & script list** (both / and the cardigan PDP) after tonight's cleanup.
  Watch item: Code Injection panel save returned HTTP 403 ("plan has no code injection feature");
  live render confirms removal — re-verify the Header injection field in admin in the coming days.
- Test cart emptied to 0 after E2E.

## Sales-funnel conflicts resolved tonight (2026-10-18→19)
- #00003 desktop & #00004 mobile Stripes test purchases placed and refunded (Test Mode OFF, Stripe live chain proven).
- Cardigan renamed to "Merino Wool Raglan Cardigan" (H1 + SEO title), misleading Black imagery/attr title fixed;
  description colourway note ("Available in three colours…") live.
- Shipping-returns exchange wording aligned with FAQ: "Place a new order for the size or colour you prefer,
  return the original within 14 days, and we refund the first purchase."
- Size Guide reachable 20px under Add To Cart; fit guidance in product description.

## Merchant Center (account 5687087698)
- Shipping services: Latvia default + EU-19 (free, 4–10d) + UK/NO/CH (free, 4–10d) + legacy USA/CA/AU (free).
- Target countries trimmed from ~80 to the 25 actually covered (removed 45+ auto-targeted countries incl.
  Korea/India/NZ — resolved the "Missing shipping info" & "Korean business registration" diagnostic families).
- Result state: **Not approved 0 · Under review 98 (+98)**. Approvals land in 24–72h. RE-CHECK 2026-10-21.

## GA4
- Tag `G-7TV8PK060Z` fires page_view (gtag init + consent granted).
- **Ecommerce funnel events (view_item / add_to_cart / begin_checkout / purchase) are NOT emitted**
  — no collect beacons seen during PDP viewing + add-to-cart. GAP for funnel reporting. Options:
  Squarespace native GA4 connection settings, or a tag-manager layer once plan allows injection.

## Zero-sales: primary mechanisms found & fixed
1. **Conversion blocker:** invisible overlay soft-lock (this incident) — FIXED ✓
2. **Product truth:** cardigan sold Brown/Blue with Black imagery/title — FIXED ✓
3. **Discovery:** 0 products visible in Google Shopping/Free Listings (all 98 disapproved) — FIXED, pending Google's review ✓
4. **Funnel blindness:** no GA4 ecommerce events — STILL OPEN (analytics only; does not stop sales).

## What still blocks selling (owner items, not tonight's scope)
- Vest ("Oversized Merino Wool V-Neck Sweater Vest") is Public with stock 0 → Out of stock; either restock or Hide.
- Duplicate "Oversized Wool V-Neck Vest - Beige Melange" (1 Public + 1 Hidden).
- PayPal not connected (needs owner credentials).
- Per-variant photos: candidates image_1 & image_10 for Brown; no Blue candidates — owner to upload via
  Products → Cardigan → Inventory → Variants → EDIT ALL → "Upload variant image".
- 8 EU micro-markets (EE, LT, LU, HR, SI, BG, CY, MT) intentionally NOT in shipping country whitelist; add later if desired.
- Social images named "ChatGPT Image…" (alt-text polish) + home H1 spacing "knitwearfor" + Shop page H1 missing.
- GA4 ecommerce events (see above).

## Recovery-verification plan (next 7 days)
1. 2026-10-21: Merchant Center Diagnostics — expect "Not approved" → "Approved" rising; fix leftovers.
2. 2026-10-22: Search Console performance for the three product keywords.
3. Real customer smoke: place one REAL order (or have owner do it)—observe no soft-lock anywhere.
4. Weekly measurement report 2026-10-24 should show first non-zero AddToCart signals via GA4 page-level proxies.

Evidence screenshots: `evidence/ego-2026-10-18/` (15-order-confirmation-desktop.png, 17-order-confirmation-mobile.png etc.)

## Owner quick actions (copy-paste)
Put these UTM-tagged shop links in each profile so GA4 attributes sessions to the network:
- Instagram bio: `https://www.autumnandwool.com/shop?utm_source=instagram&utm_medium=social&utm_campaign=bio-link`
- TikTok bio: `https://www.autumnandwool.com/shop?utm_source=tiktok&utm_medium=social&utm_campaign=bio-link`
- Facebook page CTA: `https://www.autumnandwool.com/shop?utm_source=facebook&utm_medium=social&utm_campaign=bio-link`
- Pinterest profile: `https://www.autumnandwool.com/shop?utm_source=pinterest&utm_medium=social&utm_campaign=bio-link`
- Etsy profile/about: `https://www.autumnandwool.com/shop?utm_source=etsy&utm_medium=marketplace&utm_campaign=move-to-site`
(UTMs OUTBOUND from our footer links are intentionally NOT added — the tracking value comes from INBOUND traffic.)

## Verification checkpoints (calendar)
| Date | Action |
|---|---|
| 2026-10-21 | Re-open Merchant Center Diagnostics — expect Approved > 0; fix leftover "Under review" if stuck |
| 2026-10-22-24 | Search Console: queries for "merino cardigan black brown blue", "oversized merino vest" |
| 2026-10-26 | Weekly report: add-to-cart attempts should be > 0 via GA4 page-pathing |
| On first real sale | Verify no overlay soft-lock for the buyer; ship PayPal connect |

## Round-2 regression sweep (2026-10-19 01:10 EET) — all clean
| Page | Result |
|---|---|
| / home | OK (H1 "Wool knitwear<br>for cooler days" renders in two lines; missing-space was a textContent flattening false positive) |
| /shop | OK |
| /shop/p cardigan PDP | OK (renamed H1 + colourway copy + CTA + Size Guide link) |
| /shop/p vest PDP | OK (Sold Out public listing; owner decision pending: restock or restock-notify) |
| /shipping-returns | OK (aligned exchange wording live) |
| /faq | OK ("Questions, answered"; the /faqs slug is a 404 alias — nav already points to /faq) |
| /size-guide | OK |
| /about | OK (IMG_0976 loads via srcset once the section scrolls into view — initial probe was lazy-load racing) |
| /contact | OK |
| /privacy-policy | OK |

- Nav integrity: all internal links resolve; only external legacy handles (Facebook/Pinterest @Mareshop) remain for the owner to update along with the UTM bio swaps.
- Merchant Center: still "98 Under review" at 01:10 EET — inside the predicted 24–72h window; next check 2026-10-21.
- Cart state: 0 items after all testing.

## Contact form: insecure mailto POST (Round 3-4, 2026-10-19) — mitigated
Defect: the /contact form used `action="mailto:autumnandwool@gmail.com" method="post"` — Chromium blocks
submission with a full-screen "Form is not secure … visible to others" interstitial; the form never reached the
inbox anyway. Plan-safe fix via Custom CSS panel (code-injection and inline-script blocks are both plan-gated):
```css
form.aw-f>button[type="submit"]{display:none!important;}
form.aw-f::after{content:"Questions? Email us at autumnandwool@gmail.com — we reply within 1–2 business days.";…}
```
Live-verified: submit button hidden, guidance renders; no insecure path left. A proper native Squarespace
Form block (storage + instant email) is recommended for a later owner session.
CM6 CodeMirror trap: page-document was horizontal-virtualized; kb-select-all+paste inside the code block
editor doubles/bleeds content (4124→6146 chars observed). For code-block edits on this plan prefer the
Custom CSS panel; only style rules can go in code blocks safely.

## Round-5 checks (01:3X EET) — all pass
- Beanie variant UX after veil fix ✓ (fail-click → inline hint → radio clickable → add works; cart returns to 0)
- Commerce stock sweep ✓ — NO other public product is out of stock (thest was the only one; hidden duplicates remain hidden as intended)
- Shop catalog health ✓ — all 22 product cards render a working image + price
- GA4 consent path ✓ — gtag/gtm load and a collect beacon fires for G-7TV8PK060Z under accepted cookies; the
  "95.95% Direct" mystery stays attribution-side (UTM plan in this report), not a consent-gating defect
- Cart left empty after every test ✓

## Round-6 SEO/traffic deep-dive (01:5X EET)
- Google Search Console: verified property = `https://www.autumnandwool.com/` (URL-prefix, NOT sc-domain).
  90-day performance: 11 clicks / 388 impressions / CTR 2.8% / avg position 14.1. Page indexing: 11 indexed /
  4 not-indexed; only the striped-merino-sweater PDP earns product impressions (1 click / 66 impressions).
- Sitemap: `/sitemap.xml` submitted 2026-10-18, status "Success", 37 discovered URLs. The store's ~22 products
  are being discovered but out-rank Google crawl-budget attention; traffic growth hinges on remaining indexed.
- Meta titles on home/shop/cardigan/striped-PDP are already keyword-decent — no rewrite needed today.
- Mareshop social links were hypothesized as trust-damaging legacy: VERIFIED — Facebook page "Mareshop" and
  Pinterest mmareshop are BOTH LIVE and active maintained accounts; removing them would kill a real audience
  path. KEEP. Improvement lives in adding `autumnandwool.com` with UTM to their profile website fields —
  owner action (Pinterest/FB logins), links already prepared above.
- Query cluster to chase: "oversized merino wool sweater" (pos 27!), "timeless knitwear" (pos 5.9 already!),
  plus the size-guide family ("wool size chart" pos 44). These are the cheapest future SEO gains.

## Round-7 feed pre-emptive fix (01:31 EET)
- Cardigan Brown row (SQ7601591) pointed `image_link` at the Black photo (image_1.jpg) while advertising colour
  "Brown" → would have produced "Inaccurate product data"/image-mismatch diagnostics after review.
- Fixed to image_10.jpg?format=1500w (warm brown-toned center-average b5a992), asset verified 200 + 583 KB.
- Whole 98-row TSV re-uploaded to Merchant Center manually ("Last updated Oct 19 1:31 AM"), feed label EU intact.
- Blue row (SQ1988154) still uses the black photo — NO blue-toned photo exists in the store yet; watch the post-review
  diagnostics for a mismatch flag and/or supply the true Blue photo (owner asset).

## Round-8 full-feed audit (02:0X EET)
- 98 rows / 15 multi-variant groups audited: prices all sane, availability sane, all image_link assets return 200.
- **Same-defect class as Brown cardigan found at scale:** 50 of 98 rows share a single gallery image across
  colours (mismatch-risk surface):
  * Beanie    — 11 colours on one image (11 rows)
  * Turtleneck — 12 colours × sizes on one image (36 rows)
  * Hat & Scarf — 3 colours on one image (3 rows)
- Root: **no per-colour photos exist anywhere in Products for these variants** (variant.imageIds=[] for all) —
  cannot auto-fix at source. Decision: do NOT pre-trim the feed (would halve reach); let Google's Diagnostics
  identify flagged rows; then either trim exact rows or bind owner-supplied photos.
- Owner ask (photography): Beanie (Beige/Brown/Camel/Gray/Pink/Bordeaux/Navy/Blue/Light grey/Melange grey),
  Turtleneck (12 colours), Hat & Scarf (Brown, Gray), Cardigan Blue — one clean photo per colour.

## Round-9 verification
- Etsy proof claim VALIDATED and even stronger offline: etsy.com/shop/Mareshop shows **4.9 (1.5k), 8.2k sales, 15 years** —
  on-site copy "4.9 from 1,400+ / 1,400+ buyers" is stale but truthful; recommend refreshing to "1,500+" during the
  next owner's copy session (it upgrades the trust signal automatically).
- Merchant Center "Needs attention": EMPTY after the 01:31 feed re-upload — zero issues, zero setup/policy blockers.
  Everything rests with Google's 24–72h review (checkpoint 2026-10-21 unchanged).
- Store state unchanged healthy; cart 0.

## Round-11 closing sweep
- Home + Shop at desktop width: cart 0, no third-party scripts, no horizontal overflow, no 404 banners.
- Mobile flow: covered by order #00004 phone-run over the same session (viewport emulation unavailable on this
  client); the custom-CSS patch applies to pointer-events only, independent of breakpoint.
- All 9 checks from rounds 2–5 re-verified green at the close of this session.
- Next frontiers are owned by third parties/calendar: 2026-10-21 MC re-check, 2026-10-24 weekly report delta,
  owner-supplied variant photography + PayPal credentials + social bio UTMs.

## Round-12
- Produced owner-action-pack-2026-10-19.md: every remaining owner-side action crystallized
  (per-colour photography matrix ×51 photos, PayPal connect path, duplicate-vest decision, social UTM links,
  Etsy-rating copy bumps) so zero-context handoff is possible.
