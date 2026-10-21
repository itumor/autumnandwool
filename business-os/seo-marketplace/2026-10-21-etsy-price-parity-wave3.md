# Etsy vs site price parity on assumed costs (SEO-20), wave 3, 2026-10-21 — DRAFT for owner

Author: aw-seo-marketplace. **ASSUMPTION MODE. Every figure is built on assumptions, not facts.** Costs: A-PRD
(Production), shipping and packaging: A-OPS, site CM2: `head-of-ecommerce/min-contribution-assumed-2026-10-21.md`
(A-GM-05/20/21). Etsy fees and Etsy price: A-SEO-01..08 (`seo-marketplace/assumptions-wave3.md`). Etsy's real prices
are unknown (export not received; the public shop page returned 403), so the check assumes **Etsy price = site price**
(A-SEO-07) and shows the price at which Etsy would match the site. Hand calculation, same layers as `unit_economics.py`.
Nothing changed on Etsy; no price is proposed for Q4 (A-GM-13: Etsy stays as it is).

## Fee model (A-SEO-01..04, base case, no Offsite Ads)
Etsy fees per order at price P = (6.5% × P + 4% × P + EUR 0.30 + EUR 0.18) × 1.21 VAT = **0.12705 P + 0.58**.
Site payment line it replaces = 4.8% × P + 0.25 (Stripe EEA premium + Squarespace Basic 2%).
Etsy CM2 = site CM2 − (0.07905 P + 0.33). Each extra EUR 1 of Etsy price adds EUR 0.658 to CM2
(net 0.826 − returns 0.041 − Etsy fees 0.127).

| SKU (A-GM-02) | Price | Etsy fees (A) | Site fees | Gap | Site CM2 LV | **Etsy CM2 LV** | Site CM2 EU-other | **Etsy CM2 EU-other** | Etsy CM2 US/CA/AU | Etsy price for site-equal CM2 |
|---|---|---|---|---|---|---|---|---|---|---|
| P1 Merino Raglan Cardigan | 160 | 20.91 | 7.93 | 12.98 | 13.87 | **0.89** | −3.13 | **−16.11** | −44.94 | ≈ EUR 180 (+19.72) |
| P2 Dusty Pink Merino Raglan | 155 | 20.27 | 7.69 | 12.58 | 25.82 | **13.24** | 8.82 | **−3.76** | −31.97 | ≈ EUR 174 (+19.12) |
| P3 Classic Lambswool Crew | 136 | 17.86 | 6.78 | 11.08 | 23.00 | **11.92** | 6.00 | **−5.08** | −30.94 | ≈ EUR 153 (+16.84) |
| P4 Hat & Scarf Set | 110 | 14.56 | 5.53 | 9.03 | 18.82 | **9.79** | 1.82 | **−7.21** | −29.84 | ≈ EUR 124 (+13.72) |
| P5 Rib-Knit Beanie | 45 | 6.30 | 2.41 | 3.89 | 13.09 | **9.20** | −3.91 | **−7.80** | −22.38 | ≈ EUR 51 (+5.91) |

Fees rounded to cents. Site fees = 4.8% × P + 0.25. Gap = Etsy fees − site fees.

## Stress case: order attributed to Etsy Offsite Ads (A-SEO-05)
Extra fee = P × 15% × 1.21 (or 12% × 1.21 if the shop is above USD 10k/12 months).
| SKU | Extra at 15% | Etsy CM2 LV at 15% | Extra at 12% | Etsy CM2 LV at 12% |
|---|---|---|---|---|
| P1 | 29.04 | −28.15 | 23.23 | −22.34 |
| P2 | 28.13 | −14.89 | 22.51 | −9.27 |
| P3 | 24.68 | −12.76 | 19.75 | −7.83 |
| P4 | 19.97 | −10.18 | 15.97 | −6.18 |
| P5 | 8.17 | 1.03 | 6.53 | 2.67 |

## What this says (under the assumptions only)
1. **At the same price, an Etsy order leaves EUR 4–13 less than a site order** (fees about 13% of price vs about 5%).
2. Against the EUR 10 minimum contribution (A-GM-20): at site price, only **P2 and P3 clear it on Etsy, and only for
   Latvia (and EE/LT: about 1 EUR lower)**. P1 leaves EUR 0.89. Every EU-other and US Etsy order loses money with free
   shipping, which is the same pattern as the site, only worse.
3. **Any order that Offsite Ads attributes loses money on four of the five SKUs.** Whether the shop is opted in is the
   single biggest unknown (A-SEO-05).
4. Parity direction: **Etsy should never be cheaper than the site.** To leave the same contribution as the site, Etsy
   prices would sit about 12–13% above the site (P1 ≈ 180, P2 ≈ 174, P3 ≈ 153, P4 ≈ 124, P5 ≈ 51).
5. The real Etsy prices may already be higher (Etsy-era prices). The export decides; this table then shows the actual
   gap per listing.

## Proposals for the owner (decisions, nothing applied; A-GM-13 keeps Etsy unchanged in Q4)
| # | Proposal | Evidence | Owner / by |
|---|---|---|---|
| E1 | Check Offsite Ads: opted in? 12% or 15%? If under USD 10k/12 months and opted in, consider opting out | Stress table | Owner, 28 Oct (Shop Manager → Settings → Offsite Ads) |
| E2 | Rule: Etsy price ≥ site price for every shared SKU. No Etsy price cut below the site | Table, A-GM-20 | Owner, with the export |
| E3 | Etsy shipping to EU-other / US: same decision as the site (A-GM-18): charge shipping or set a minimum, as on assumed costs every such order loses money | Etsy CM2 EU/US columns | Owner, 31 Oct (decision 21) |
| E4 | P1 cardigan on Etsy: do not push (Etsy CM2 LV ≈ 0.89) until real minutes are timed (PRD-06) | P1 row | Owner, after PRD-06 |

## To make this real
Owner: Etsy listings export (prices), one Etsy payment statement (fee lines, VAT on fees), Offsite Ads setting
(owner-inputs-wave2 rows 16–17). Finance: confirmed costs (G1, 11 Nov), then re-run with `unit_economics.py`.

ASSUMPTION: A-SEO-01..08; A-PRD-01..21 (M+L); A-OPS-02/03/05/06/08/10; A-GM-05, A-GM-13, A-GM-20, A-GM-21.
Registers: `business-os/seo-marketplace/assumptions-wave3.md`, `business-os/knitwear-making/assumptions-wave3.md`,
`business-os/operations/assumptions-wave3.md`, `business-os/head-of-ecommerce/assumptions-wave3.md`. DRAFT, not sent.

Sources: Etsy fees help page https://help.etsy.com/hc/articles/115015628847 ; Printful 2026 Etsy fee guide
https://printful.com/blog/how-much-does-etsy-take-per-sale ; outfy fee table
https://www.outfy.com/blog/how-much-does-it-cost-to-sell-on-etsy (Latvia 4% + EUR 0.30, third-party, unverified).
