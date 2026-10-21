# Autumn & Wool — Weekly measurement snapshot

**Checked:** 19 October 2026, 02:0X EET
**Reporting window:** 20 September–19 October 2026 (matching 10/17 snapshot)
**Store orders this window:** 2 — both were controlled test orders placed/refunded by the assistant while
verifying the Stripe chain (orders #00003 desktop & #00004 mobile, refunded instantly; no real customer order yet).

This is the second weekly snapshot and the first after the emergency fixes landed (overlay soft-lock, cardigan colourway,
shipping-copy alignment, Merchant Center country/shipping sweep, contact-form mitigation, vest restock).

## Baselines (30-day window)

| Metric | 17 Oct | 19 Oct | Delta / state |
|---|---:|---:|---|
| Visits | 62 | — (Squarespace view unchanged, next reading on the 24th) | |
| Bounce rate | 94.34% | — | |
| Organic clicks (GSC 90d) | 11 | 11 | steady so far |
| Impressions (GSC 90d) | — | 388 | new data baseline |
| CTR / position (GSC 90d) | — | 2.8% / 14.1 | baseline |
| Google-known pages | — | 37 discovered, 11 indexed, 4 not-indexed | indexing recovery started 10/18 |
| Merchant Center | 2 auto items; 0 approved | 98 primary rows live; **0 not-approved, 98 under review** | review window 24–72h |
| Orders | 0 | 2 (both test+refunded) | Stripe chain PROVEN working |
| Cart hygiene | — | 0 items after every test | ✓ |

## Funnel instrumentation state (where we'll measure from now on)

- **GA4**: tag G-7TV8PK060Z loads; one `collect` voxel per accepted-cookie page_view ✓. **Ecommerce
  events are NOT emitted by Squarespace under this plan** (no Code Injection → no event listener possible). Until plan
  upgrade, funnel events are unavailable — measured proxy: Squarespace Analytics traffic + completed orders.
- **Veil soft-lock**: fixed — every add-to-cart fail-click remains recoverable; radio interaction verified on
  cardigan + beanie this week.
- **Newsletter + contact + registration**: functional; contact's insecure `mailto:` POST neutralised (button hidden,
  guidance rendered).
- **Catalogue health**: 22 live cards, all images healthy, no sold-out public items; vest restocked to 1.

## Leading indicators to watch at next report (2026-10-24)

1. Merchant Center: Approved > 0 (expected within 24–72h of 10/18 sweep). Diagnostics after the 10/19 01:31 EET
   re-upload now shows the image-mismatch class reduced from 50 → 48 rows.
2. GSC: query "oversized merino wool sweater" (position 27) should improve as product indexing spreads; the
   "timeless knitwear" (5.9) and "wool size chart" (44) clusters are quick winners.
3. Squarespace: any add-to-cart attempt in engagement panel; any order inside the 30-day window — a first
   real order is expected only after MC approval and/or owner-side UTM tagging on social bios.

## Actions shipped this week

| # | Change |
|---|---|
| 1 | Invisible click-trap overlay fix (sqs-widgets-confirmation CSS neutraliser) |
| 2 | Cardigan: renamed, colourway copy live, SEO title updated, neutral H1 per variant state |
| 3 | Shipping-exchange wording aligned between /shipping-returns and /faq |
| 4 | Size-guide entry 20 px under Add To Cart on clothing PDPs |
| 5 | Merchant Center: 45+ auto-targeted countries trimmed; EU-19 + UK/NO/CH shipping services built (free 4–10d); Brown-row feed image corrected |
| 6 | Contact form: insecure mailto POST mitigated |
| 7 | Vest restocked to 1 |
| 8 | Old 'Website Speedy' third-party scripts verified absent from live HTML |
| 9 | Cookie-consent + GA4 collect chain verified firing (no gate defect) |

## What we still cannot see (blind spots)

- add_to_cart/begin_checkout/purchase events (plan-gated) — funnel anonymity persists until plan upgrades
  or events are enabled in GA4 under a feature flag I can't toggle.
- Bounce-rate decomposition between consent-opted-in vs declined (Squarespace panel does not split).
