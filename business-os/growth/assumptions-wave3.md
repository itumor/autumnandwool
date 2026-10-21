# Growth assumptions register, wave 3   Status: DRAFT for owner   2026-10-21

aw-growth-marketing, ASSUMPTION MODE (owner-approved 2026-10-21). **Every value is an ASSUMPTION, not a fact.**
Growth uses the shared baselines first and adds its own A-GRO row only where none of them has the value:
- Costs, stock, capacity, GREEN list: `business-os/knitwear-making/assumptions-wave3.md` (A-PRD-xx), `capacity-2026-W43.md`
- Shipping, packaging, cutoffs: `business-os/operations/assumptions-wave3.md` (A-OPS-xx)
- Owner decisions, CM2 per destination: `business-os/head-of-ecommerce/assumptions-wave3.md` (A-GM-xx),
  `business-os/head-of-ecommerce/min-contribution-assumed-2026-10-21.md` (GM rulings win on conflicts)
- Finance `sku-margins-assumed-wave3.md`: **not present at 2026-10-21 run time**. BE_CAC below is taken from GM's
  hand-calculated CM2 table (same CM layers as `unit_economics.py`). `unit_economics.py` was not run by Growth (no shell
  in this run). GM reports it at 0 costed / 82 TODO. When FIN publishes, FIN's values replace these and GRO-15 is re-checked.

Assumptions never permit spend, ad-account changes, posts or live edits (HARD RULES 1-3).

| A-ID | Value | Basis / URL | Range | Conf. | Task IDs | Owner confirms by |
|---|---|---|---|---|---|---|
| A-GRO-01 | **BE_CAC = CM2 by destination** from GM's table: P2 Dusty Pink LV 25.82 / EE-LT 24.82; P3 Lambswool Crew 23.00 / 22.00; P4 Hat & Scarf Black 18.82 / 17.82; P1 Cardigan 13.87 / 12.87; P5 Beanie 13.09 / 12.09; EU-other and US/CA/AU at or below 8.82 (several negative) | `head-of-ecommerce/min-contribution-assumed-2026-10-21.md` (A-PRD-01..21, A-OPS-02/03/05/06/08/10, A-GM-05/20/21). Production's indicative CM2 in `capacity-2026-W43.md` (flat EUR 12 ship, EUR 3 pack) is **superseded** per GM rulings W3-2/W3-3 | follows A-PRD labour range (largest effect) | L | GRO-15, GRO-18, GRO-14, GRO-22 | 4 Nov (G1 cost confirm) |
| A-GRO-02 | Any paid test that targets LV + EE + LT together uses the **lower (EE/LT) BE_CAC** for budget and kill lines, so a mix of countries can't hide a loss | Conservative choice; skill s1 "BE_CAC caps everything" | LV column would raise budget by EUR 3 per concept | M | GRO-15, GRO-18 | 20 Nov |
| A-GRO-03 | Test countries for any paid test = **LV, EE, LT only** (no EU-other, no US/CA/AU) | Max CAC is negative outside the Baltics on assumed costs (GM table); A-GM-18 | add EU-other only if real costs raise CM2 by EUR 2+ | M | GRO-15, GRO-18, GRO-19 | 20 Nov |
| A-GRO-04 | Concepts live in any December test = **2** (B proof, C product truth). Concept A (making-of) wording is allowed by A-GM-10, but no real footage file is on record and photo rights (decision 16) are open, so it isn't counted in the budget | A-GM-10, A-GM-11; brief `test-2026-10-21-dec-first-signal.md` | 2-3 | M | GRO-18 | 31 Oct (G8 / decision 16) |
| A-GRO-05 | Illustrative Meta CPC for a sanity check only: **EUR 0.40 per link click** (apparel) | Apparel CPC USD 0.45 (trendtrack.io, https://www.trendtrack.io/fr/blog-post/meta-ad-spend-by-industry, 2025); global average USD 0.82 (vaizle, https://insights.vaizle.com/facebook-ad-benchmarks/); USD 1.06-1.32 Nov-Dec (superads.ai). No Latvia/Baltic figure was found. USD to EUR conversion not checked | EUR 0.10-1.20 | L | GRO-18 (expected-orders check) | Replaced by the first real week of spend |
| A-GRO-06 | Illustrative site conversion rate from paid click to Squarespace order: **1.0%** | Agent estimate for a new store with 0 orders to date and 64 visits / 30 days; no A&W data. GA4 has no purchase events | 0.3-2.0% | L | GRO-18 | Replaced by real orders |

## Derived checks (arithmetic on the rows above, ASSUMPTION)
- **Break-even CPC** = CAC goal x CVR. P2 EE/LT: 14.82 x 1.0% = **EUR 0.15**; at BE_CAC 24.82 it is **EUR 0.25**.
  P3 EE/LT: 12.00 x 1.0% = **EUR 0.12**; at BE_CAC 22.00 it is **EUR 0.22**.
- At the assumed CPC of EUR 0.40 and 1.0% CVR, the expected CAC is about **EUR 40**: above BE_CAC for every SKU. Inference
  (L): a December test would most likely end on the kill line. It would still buy a first real CPC/CVR read, which is its
  only stated purpose (learning, not revenue).
- The CPC and CVR rows are **not** forecasts and are never quoted as results. They exist so the owner sees the likely
  outcome before choosing a ceiling.

## Cross-register flag for GM / PAR (not edited by Growth)
- A-GM-17 says the gift cap is "at or below the beanie's break-even CAC". On assumed values the landed gift cost in LV
  (13.33 + 1.50 + 5.00 = about EUR 19.83, GM file) is **above** the beanie's BE_CAC (LV 13.09). The rule as written blocks
  every beanie gift. GM to rule: cap per gift = P2/P3 Max CAC (about EUR 15), or accept the gift as a fixed marketing cost
  per creator. Growth's view: treat each gift against the CAC of the orders it brings, read by UTM (A-GM-06).

## TODO / missing data
FIN `sku-margins-assumed-wave3.md`; real costs (G1); owner ceiling (decision 33); real CPC and CVR (first spend week).
