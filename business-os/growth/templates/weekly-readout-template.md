# Weekly growth readout, week starting YYYY-MM-DD   Status: DRAFT

Copy to `business-os/growth/readout-YYYY-MM-DD.md` (date = the Monday of the WBR). Under 200 words in the
summary block. Fill from owner exports only. Unknown = MISSING. Never estimate.

## 0. Inputs the owner exports each Monday (15 min)
| Input | Where | Pasted? |
|---|---|---|
| Orders, revenue, discount codes used, customer new/returning | Squarespace > Commerce > Orders (filter last week; exclude test orders) | [ ] |
| Etsy orders (if Etsy open, decision 9) | Etsy > Orders | [ ] |
| Sessions by source/medium and campaign | GA4 > Reports > Acquisition > Traffic acquisition (add `session campaign`) | [ ] |
| Visits, top referrers | Squarespace > Analytics > Traffic | [ ] |
| GSC clicks, impressions (28d) | Search Console > Performance | [ ] |
| Merchant Center approved / disapproved count | Merchant Center > Products > Diagnostics | [ ] |
| Ad spend, impressions, clicks, platform-claimed conversions | Meta Ads Manager / Google Ads (only if a test is running) | [ ] |

## 1. Summary (under 200 words)
Results vs target (green / amber / red), top movers with cause and confidence, calls, MISSING.

## 2. Readout in order, one call per line (HOLD / FIX / TEST / INVESTIGATE; INVESTIGATE overrides)
| Line | This week | Last week | Call | Why |
|---|---|---|---|---|
| Spend (EUR) | | | | |
| Clicks / sessions (GA4, by source) | | | | |
| Squarespace orders (new / repeat), with code or UTM if visible | | | | |
| Creative (per concept) | | | | |
| Landing page (PDP state, stock) | | | | |
| Tracking (GA4 tag, UTMs intact, pixel state) | | | | |

## 3. Attribution readout (skill `aw-utm-attribution` s5)
Question / decision:
Source of truth: Squarespace Orders (n = __), Etsy (n = __)
| Channel or creator | Sessions (GA4) | Orders with their code | Orders after their UTM visit (if visible) | Platform claims | Notes |
|---|---|---|---|---|---|
Survey answers ("How did you hear about us?"), if collected:
Platforms claim N, we can verify M.
Confidence: low / medium / high, and why
Gaps / MISSING:
Recommendation + one test that would settle it:

## 4. Proposed `kpi-weekly.csv` row (owner appends; I never edit the file)
```
week_start,sessions,orders_site,orders_etsy,new_customers,repeat_customers,gross_sales_eur,returns_eur,net_revenue_ex_vat_eur,product_cost_eur,shipping_packaging_payment_eur,ad_spend_eur,creator_cost_eur,conversion_rate,aov_eur,cac_eur,gross_margin_pct,contribution_eur,on_time_dispatch_pct,units_sold,units_available,notes
```
Growth fills: sessions, orders_site, new_customers, ad_spend_eur, cac_eur (blank until spend > 0 and new_customers > 0),
conversion_rate (= orders_site / sessions). Cost, margin, dispatch and stock columns: FIN / PRD / OPS.

## 5. Results-log rows appended to `ads-results-log.csv`
(one row per test x concept; if no test, one `none` row with call)

## 6. Next week
1-2 test briefs or updates (each BLOCKED with unblock list until gates pass). Owner asks, batched, max 15 min each.
