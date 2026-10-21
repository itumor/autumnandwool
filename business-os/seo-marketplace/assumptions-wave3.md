# SEO & Marketplace assumptions register, wave 3 (ASSUMPTION MODE) — DRAFT for owner

Author: aw-seo-marketplace, 2026-10-21. Owner approved assumption mode on 2026-10-21. **Every value here is an
ASSUMPTION, not a fact.** It covers only values that the shared registers do not have. Shared baselines win on overlap:
- Production: `business-os/knitwear-making/assumptions-wave3.md` (A-PRD-xx: stock rule, costs, lead time) and `stock-duplicate-sheet.md`
- Operations: `business-os/operations/assumptions-wave3.md` (A-OPS-xx: shipping, Christmas order-by dates)
- GM: `business-os/head-of-ecommerce/assumptions-wave3.md` (A-GM-xx: priority 5, Etsy, claims, accounts)

Nothing here permits a live change, a feed upload, an Etsy edit, a price change or a post.

| A-ID | Assumed value | Basis | Low–high | Conf. | Task IDs | Owner confirms by |
|---|---|---|---|---|---|---|
| A-SEO-01 | Etsy **transaction fee 6.5%** of the order total (item + any shipping charged; with free shipping = item price) | Etsy help centre fee page (https://help.etsy.com/hc/articles/115015628847) and 2026 third-party fee guides (Printful) | 6.5% | M | SEO-20 | 28 Oct (Etsy payment account statement, owner-inputs-wave2 row 17) |
| A-SEO-02 | Etsy **payment processing, Latvian bank account: 4% + EUR 0.30** per order | Third-party fee tables (outfy.com, 2024); Etsy's own country table not readable today | 3–5% + 0.25–0.35 | L | SEO-20 | 28 Oct (statement) |
| A-SEO-03 | Etsy **listing/renewal fee USD 0.20 ≈ EUR 0.18** per item sold (auto-renew) | Etsy fee page; USD→EUR at about 1.10 (agent estimate) | 0.17–0.19 | M | SEO-20 | 28 Oct |
| A-SEO-04 | **VAT 21% charged on Etsy fees** (seller not VAT-registered with Etsy, no reverse charge) | Conservative case; EU sellers without a VAT ID on Etsy pay VAT on seller fees `[VERIFY with accountant]` | 0% (VAT ID, reverse charge) – 21% | L | SEO-20 | Accountant (FIN accountant question list) |
| A-SEO-05 | **Etsy Offsite Ads: base case 0% of orders attributed**; stress case every order attributed at **15%** (12% if the shop sold > USD 10k in the last 12 months; fee capped at USD 100 per order) | Etsy Offsite Ads terms (agent knowledge, not re-read today) `[VERIFY in Shop Manager → Settings → Offsite Ads]`; attribution share unknown | 0–100% of orders at 12–15% | L | SEO-20 | 28 Oct (owner: opted in/out, 12% or 15%) |
| A-SEO-06 | Etsy listing currency = **EUR** and payout account in EUR (no 2.5% currency conversion fee) | Shop sells from Latvia; not checked | 0 or 2.5% | L | SEO-20 | 28 Oct |
| A-SEO-07 | **Etsy price = site price** for the parity check (Etsy prices unknown: WebFetch of etsy.com/shop/Mareshop returned 403 on 21 Oct, listings export not received) | No data; the "parity" scenario is the neutral case | Etsy 0–30% above site | L | SEO-20, SEO-19 | 28 Oct (listings export) |
| A-SEO-08 | Etsy orders carry the **same variable costs as site orders** except the payment line: M+L (A-PRD), packaging EUR 1.50 (A-OPS-10), shipping by destination (A-OPS-02/03/05/06/08), returns 5% of net (A-GM-21), VAT 21% (net = price / 1.21). Squarespace 2% + Stripe fee (A-GM-05) replaced by Etsy fees | Same product, same parcel, same stock pool (A-GM-13) | — | L | SEO-20 | With A-PRD / A-OPS confirmations |
| A-SEO-09 | **Made-to-order rows in the feed stay `in_stock`** and carry row-level `min_handling_time` / `max_handling_time` when the MTO lead time is longer than the account handling time (2–5 business days). `backorder` not used: it needs an `availability_date` that a hand-run generator would let go stale | Google Merchant Center help: availability (https://support.google.com/merchants/answer/6324448), availability_date (https://support.google.com/merchants/answer/6324470), handling time (https://support.google.com/merchants/answer/7388496). "MTO = in_stock + handling time" is my reading, not a quoted Google rule `[VERIFY in MC Diagnostics after upload]` | alt: `backorder` + date | M | SEO-04 | 24 Oct (with generator patch approval, owner-inputs-wave2 row 4) |
| A-SEO-10 | Merged category **"Hats & scarves"**, proposed slug `/shop/hats-scarves`; old category URLs `/shop/beanies` and `/shop/sets` 301 to it | A-GM-24 (merge); current slugs not fetched today `[VERIFY in Squarespace → Commerce → Categories]` | hide instead of merge | L | SEO-13 | 14 Nov (decision 29) |

## Values used from shared registers (not redefined here)
| Value | A-ID | Used in |
|---|---|---|
| Physical stock rule: 1–8 as listed; 12/16 = 50%; beanie 220 / turtleneck 360 = 0 on shelf, made to order; duplicates share one pool (72 assumed units) | A-PRD-12, A-PRD-13 | SEO-04 |
| MTO lead time: garments 10 wd, beanie / hat set 5 wd; in-stock 2–5 wd | A-PRD-14, A-GM-03 (ruling W3-1) | SEO-04, SEO-26, SEO-13 |
| Christmas order-by dates per zone (MTO garments / MTO accessories / in-stock) | A-OPS-16..19 | SEO-26 |
| Priority 5 and GREEN (A) list | A-GM-02; `knitwear-making/capacity-2026-W43.md` | SEO-26, SEO-20 |
| Claims allowed / not allowed | A-GM-10 | SEO-25, SEO-26, SEO-13 |
| Etsy stays open, no listing rewrites in Q4 | A-GM-13 | SEO-19 (stays BLOCKED), SEO-20 |
| Trim unphotographed colours by 14 Nov (turtleneck 31 Oct); merge Beanies + Sets | A-GM-24 | SEO-04, SEO-13, SEO-24 |
| No digital gift card assumed; no gift wrap (gift note + prices off the packing slip only) | A-GM-22, GM rulings W3-6, W3-7 | SEO-26 (gift-card pin dropped, also from the wave 2 draft), SEO-15, SEO-17, SEO-18, SEO-21, SEO-25 R4 |
| No fibre % and no "extra-fine" in new pins/metas: "merino wool [CLAIM-CHECK]" | A-GM-10, GM ruling W3-8 | SEO-15, SEO-17, SEO-18, SEO-12 (vest intro) |
| Baltic second stop: MTO garments LV 4 Dec / EE-LT 3 Dec, accessories LV 11 / EE-LT 10 Dec, Baltic addresses only | GM ruling W3-11 | SEO-26, SEO-22 |
| Publish Christmas dates only after owner approval on 20 Nov | A-GM-28 | SEO-26 |
| Site CM2 per destination | `head-of-ecommerce/min-contribution-assumed-2026-10-21.md` (A-PRD + A-OPS + A-GM-05/20/21) | SEO-20 |

DRAFT. Not sent, nothing applied.
