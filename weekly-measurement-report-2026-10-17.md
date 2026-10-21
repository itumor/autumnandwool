# Autumn & Wool — Weekly measurement snapshot

**Checked:** 17 October 2026  
**Reporting window:** 18 September–17 October 2026 (Squarespace Last 30 Days)  
**Store orders:** 0 completed orders in Squarespace Orders.  

This is the first verified snapshot, not a week-over-week trend. Refresh weekly with the same reporting window and label each date range. Product CSV imports were performed on 17 October; one row failed in the second import, and the public product copy did not reflect that final pass. Product data edits are paused per the user’s instruction.

| Metric | Current value | Source / confidence |
|---|---:|---|
| Visits | 62 | Squarespace Analytics → Traffic |
| Unique visitors | 62 | Squarespace Analytics → Traffic |
| Pageviews | 59 | Squarespace Analytics → Traffic |
| Bounce rate | 94.34% | Squarespace Analytics → Traffic |
| Average time on page | 27 sec | Squarespace Analytics → Engagement |
| Exit rate | 89.83% | Squarespace Analytics → Engagement |
| Traffic sources | Direct 59; Google 2; Facebook 1 | Squarespace Analytics → Traffic; medium not shown |
| Landing page | Not available | No landing-page-by-session view captured |
| Product page views | Not verified | Sparse page-level counts are not a complete product-event report |
| Add-to-cart events | Not available | No reliable event report captured |
| Checkout starts | Not available | Sales funnel showed unrelated sample data; excluded |
| Completed orders | 0 | Squarespace Products & Services → Orders: “No orders yet” |
| Revenue | €0 confirmed from no completed orders | Commerce dashboard has no recorded sales |
| Conversion rate | 0% orders / visits | 0 / 62; same reporting window |
| Average order value | Not available | No orders |
| Newsletter signups | Not verified | Signup form is visible; consent/subscriber records not checked |
| Google organic clicks | 11 total shown | Autumn & Wool Search Console property; date window not clear in overview, so not compared to the 30-day baseline |
| Merchant Center products | 2 auto-discovered; 0 owner-provided; 0 approved | Autumn & Wool Merchant Center; both items not approved for missing shipping information and pending review; last update 6 Oct 2026 |
| Pinterest referrals | Not listed | No Pinterest source appears in the current source counts |
| Instagram referrals | Not listed | No Instagram source appears in the current source counts |

## Reading the snapshot

Only 62 visits were recorded. With 94.34% bounce and 27 seconds average time on page, the current dataset is too small to diagnose a single conversion cause. Product-page engagement appears sparse. No purchase has been recorded, and measurement for cart/checkout events is not reliable yet.

## Next weekly check

1. Use the same 30-day window; record visits, sources, product views, orders and revenue.
2. Use the Autumn & Wool Search Console property. Fix Merchant Center shipping and feed setup; verify GA4 property and purchase events. Record clicks and approvals only for a stated window.
3. Keep product data unchanged. Confirm add-to-cart, checkout-start and purchase events using reliable platform diagnostics.
4. Compare against this baseline; do not treat traffic targets as guaranteed outcomes.

## Recheck — 18 October 2026

**Reporting window:** 19 September–18 October 2026 (Squarespace Last 30 Days).

| Metric | Current value | Source / confidence |
|---|---:|---|
| Visits | 64 | Squarespace Analytics → Traffic |
| Unique visitors | 64 | Squarespace Analytics → Traffic |
| Pageviews | 61 | Squarespace Analytics → Traffic |
| Bounce rate | 95.95% | Squarespace Analytics → Traffic |
| Completed orders | 0 | Products & Services → Orders says “No orders yet” |
| Revenue | €0 recorded | No orders in Products & Services → Orders |
| Conversion rate | 0% orders / visits | 0 / 64 in the same 30-day window |
| Add-to-cart / checkout / purchase events | Not verified | GA4 has page/engagement events only in the recent event list; no ecommerce events. Zero orders means purchase delivery remains untested. |
| Product sales panel | Excluded | Sales by Product listed furniture products absent from the verified knitwear catalog; data mismatch requires Squarespace support. |

The 64-visit count is only 2 above the prior 62-visit snapshot, but the date windows overlap and span different dates. This is not a clean weekly growth comparison. The low traffic and 95.95% bounce remain the clearest measured constraints. Do not infer that the unrelated product sales belong to this store.

Product records remain frozen. No product data, checkout, or order changed during this recheck.


## GA4 verification — 18 October 2026

- Squarespace is configured with `G-7TV8PK060Z`, matching the Autumn & Wool GA4 web stream for `https://www.autumnandwool.com/` (stream ID 13239857437). Collection was active in the past 48 hours; Enhanced Measurement is enabled.
- Recent GA4 events: `click`, `first_visit`, `page_view`, `scroll`, `session_start`, `user_engagement`. No ecommerce events appeared. `purchase` is marked as a key event but has no stream data. Since Squarespace Orders shows zero orders, purchase tracking cannot be verified without an actual order/test order. No test order or settings change was made.
- Squarespace Traffic currently shows 64 visits, 64 unique visitors, 61 pageviews, and 95.95% bounce for Sep 19–Oct 18.
- Dashboard breakdowns disagree with the 64 visits: device total is 106 and browser subtotals add to 101. Top sources Direct 61, Google 2, Facebook 1 sum to 64. Do not use device/browser totals until Squarespace explains the discrepancy.

- One controlled public-page click on the beanie Purchase button resulted in a blank browser page; a separate cart check found the beanie in cart and it was removed. GA4 Recent events still showed only page/engagement events; no `add_to_cart` event surfaced. Treat add-to-cart and checkout tracking as unverified. Empty-cart screenshot: [evidence](/Users/eramadan/autumnandwool/evidence/cart-empty-2026-10-18.jpg).
- Abandoned-checkout recovery was enabled and verified on 18 Oct: Squarespace shows “Recover abandoned carts” as Live. It sends one reminder after 1 day if no order is placed, with an unsubscribe link. No recovered order is yet evidenced.

- Organic content: saved six unpublished local campaign drafts with authentic, unaltered product photos, captions, and UTM destination URLs at [campaign-drafts.md](/Users/eramadan/autumnandwool/campaign-assets/campaign-drafts.md). Social account ownership and publishing remain unverified.
- Welcome-email copy is drafted locally at [welcome-email-draft.md](/Users/eramadan/autumnandwool/campaign-assets/welcome-email-draft.md). Newsletter consent and welcome-email automation remain unverified; no email sent. The separate abandoned-cart automation is now Live (see below).

### Merchant Center and payment recheck — 18 October 2026

- Merchant Center was checked under the store Google profile. No shipping policy exists. The setup wizard was inspected but not saved because verified delivery-time ranges are unavailable.
- Squarespace has €0 shipping options for Latvia, the United States (54/54 states and territories), and the rest of the world. The inspected rate setup has no delivery-time range.
- Squarespace Payments shows Stripe Connected, Test Mode Off, EUR, and multi-currency checkout On; PayPal is not connected. Stripe connection does not verify payouts or successful checkout. No settings changed.
- Product data remains unchanged.


### Abandoned-cart recovery — 18 October 2026

- Squarespace confirms “Recover abandoned carts” is **Live**. It triggers when a customer leaves a cart at checkout, waits 1 day, then sends one reminder if no order was placed. The reminder includes an unsubscribe link.
- This is an enabled system flow, not evidence of recovered carts or sales; no automation analytics or order has been recorded yet. No product data changed.
