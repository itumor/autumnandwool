# Test: dec-first-signal   Status: BLOCKED

Drafted 2026-10-21 by aw-growth-marketing (skill `aw-paid-ads-testing`). Default under master ruling C10 is **no
December test, EUR 0**. This brief exists so that, if all gates pass by 20 Nov, the owner can decide in one sitting.
Purpose: learning (first CAC read), not gift-season revenue.

Gates: costed FAIL / safe-to-promote MISSING / PDP FAIL / orders countable PASS / conversion signal UNVERIFIED / budget MISSING
(detail and owners: `paid-test-gates.md`)

## Wave 3 fill on assumptions (2026-10-21) — brief stays BLOCKED
ASSUMPTION: test SKU P2 Dusty Pink, BE_CAC EUR 24.82 (EE/LT, used for the whole Baltic set), CAC goal EUR 14.82, 2 concepts,
countries LV/EE/LT, December decision NO-GO EUR 0; register: `business-os/growth/assumptions-wave3.md` (A-GRO-01..06),
`head-of-ecommerce/assumptions-wave3.md` (A-GM-02, -05, -08, -10, -20), `operations/assumptions-wave3.md` (A-OPS-16/17).

| Gate | On assumption | Why it still blocks spend |
|---|---|---|
| Costed | ASSUMED (P2 BE_CAC 24.82 EE/LT, 25.82 LV) | Not owner-confirmed; Production says no paid spend until cost confirmed |
| Safe to promote | ASSUMED GREEN, max 6 from stock (`knitwear-making/capacity-2026-W43.md`) | Capacity file is DRAFT, not owner-approved; it says "Paid ads: none" |
| PDP | MISSING | CRO landing brief not PASS for P2 |
| Orders countable | PASS | Squarespace Orders (manual) |
| Conversion signal | FAIL on assumption | A-GM-05: Basic plan, no Code Injection, so traffic objective only |
| Budget | MISSING | A-GM-08: no ceiling assumed; default EUR 0 |

Numbers if the owner ever says GO (ASSUMPTION):
| Line | Value |
|---|---|
| SKU | P2 Merino Raglan Sweater, Dusty Pink (`69105bd9b0c4`), in-stock units only, max 6 |
| Countries | LV, EE, LT (A-GRO-03). EU-other and US/CA/AU excluded: Max CAC negative |
| Concepts | 2: B proof, C product truth (A-GRO-04) |
| Budget per concept | 3 x 24.82 = **EUR 74.46** |
| Test total | 2 x 74.46 = **EUR 148.92** (owner ceiling may be lower; the lower wins) |
| Window | Earliest launch Mon 23 Nov to in-stock order-by Tue 15 Dec (EE/LT, A-OPS-17) / Wed 16 Dec (LV, A-OPS-16): 17 working days, minus LV holiday 18 Nov (before launch) |
| Daily | 148.92 / 17 = **about EUR 8.76 per day** (both concepts) |
| Kill 1 (per concept) | spend >= **EUR 49.64** with 0 Squarespace orders -> stop |
| Kill 2 (per concept) | spend >= **EUR 74.46** with CAC > EUR 24.82 -> stop |
| CAC goal | <= **EUR 14.82** (lower of 0.6 x BE_CAC 14.89 and Max CAC 14.82) |
| Scale | none in December |
| Expected outcome (L, A-GRO-05/06) | CPC 0.40 at 1% CVR -> CAC about EUR 40: likely Kill 1. Break-even CPC EUR 0.15-0.25 |

The Baltic in-stock window (17 working days) is longer than the wave-2 EU MTO window (about 9 days), because P2 ships
from stock and the test excludes EU-other.

SKU(s): ONE SKU, owner's pick from the 5 priority SKUs (master decision 2, re-confirmed 4 Nov). TODO.
Candidates (wave 2, from `../head-of-ecommerce/priority-5-sku-proposal-2026-10-21.md`): raglan cardigan, Dusty Pink
sweater, lambswool crew, hat & scarf set (Black only until photos), beanie. Net prices and BE_CAC cells:
`be-cac-worksheet-priority-skus.md`.
BE_CAC: MISSING (no `contrib` in `unit_economics.py`). Target CAC: `target_cac_eur` or 0.6 x BE_CAC = MISSING.
Capacity this week: MISSING (no `capacity-YYYY-Www.md`). Never promote more than its "Max units to promote".
The README s9 EUR 33.10 example is illustrative and is **not** used.

Hypothesis: Because Mareshop's Etsy history (4.9 stars, 1,400+ reviews on Etsy) is proof no competitor in our scan
shows on its own site (`competitors/_summary-2026-10-21.md`), we believe a proof-led ad (concept B) on [SKU] for
broad women 25-45 in the delivery-safe countries will bring orders at CAC <= target CAC [MISSING], beating a
making-of (A) and a product-truth close-up (C). We'll know when each concept reaches its decision spend or the
decision date, read on Squarespace Orders.

Platform / objective / placement: Meta, one campaign, one ABO ad set. Objective **Traffic (landing page views)**
because no purchase signal is verified (gate 5). If the conversion checklist in `paid-test-gates.md` passes before
launch, re-brief as Sales. Placements: Advantage+ placements (default). No edits for the first 3-5 days.
Audience: broad, women 25-45 is the creative's job, not a targeting layer. Countries: only those inside OPS's
Christmas order-by date on launch day (G5; master C3: EU about 3 Dec, LV about 10 Dec, provisional). TODO from OPS table
(31 Oct provisional, 14 Nov carrier-backed). Exclusions: none possible yet (no customer list).
Provisional window (wave 2, from `../operations/christmas-cutoffs-2026.md`, worst-case, [VERIFY], not for publication):
go 20 Nov -> launch at the earliest Mon 23 Nov. EU-18 made-to-order order-by Thu 3 Dec (in-stock Wed 9 Dec, only
for owner-confirmed units); Latvia MTO Thu 10 Dec (in-stock Wed 16 Dec). US/CA/AU order-by 19 Nov is before go, so
they are excluded. So the EU window is about 9 working days for MTO: too short to scale, enough only for a first read.

Concepts (copy passes `aw-brand-voice` s3; bracketed items filled from the live PDP on the day):
- A, making-of (**parked until G8**, claims evidence 31 Oct): Kristine at the manual machine, then hand finishing.
  Text: "Knitted on a manual machine, finished by hand in Riga. [SKU name], [exact fibre wording from PDP]."
  Asset: real footage from Creative's shoot (`campaign-assets/drafts/plan-wave1/shot-list-2026-10-27.md`). TODO path.
- B, proof: product on a real person or flat lay. Text: "Formerly Mareshop on Etsy: 4.9 stars, 1,400+ reviews on Etsy.
  [SKU name], now at autumnandwool.com." (Line per master C1; update once owner reads Etsy, decision 17.)
  Asset: real product photo, e.g. `campaign-assets/source/<sku>.jpg` [VERIFY photo rights, decision 16].
- C, product truth: knit close-up. Text: "[SKU name]. [exact fibre wording]. Free shipping to eligible destinations;
  in-stock pieces ship from Riga in 2-5 working days." [VERIFY delivery wording with OPS, C8]
No AI-altered garments. No scarcity, discounts or "best-selling" labels. No competitor named.

Landing URL + UTM: PDP of the chosen SKU, rows `meta-test-dec-first-signal-concept-a/b/c` in `utm-links.csv`
(`utm_source=facebook&utm_medium=paid-social&utm_campaign=dec-first-signal&utm_content=concept-a|b|c`).
Landing readiness: `landing-brief-2026-10-21-dec-first-signal.md` must be PASS (CRO).

Budget (formula; numbers MISSING):
- Test budget per concept = 3 x BE_CAC. Concepts live = 2 (B, C) or 3 (if G8 clears A).
- Test total = concepts x 3 x BE_CAC. Monthly ceiling = lower of owner ceiling and test total.
- Daily = test total / days in window. Window = launch (after 20 Nov go) to the last order-by date of the target countries.
Kill line (per concept): spend >= 2 x BE_CAC with 0 Squarespace orders -> stop. Spend >= 3 x BE_CAC with CAC > BE_CAC -> stop.
Scale line: none in December. Scaling needs contribution after CAC > 0 on >= 3 orders (Q1 2027 earliest).
Decision date: last order-by date of the target countries, or when every concept hits a kill line, whichever first.
Read: Squarespace Orders (orders on that SKU in the window, new customers), GA4 sessions by `utm_content`, Meta
claims shown separately ("Meta claims N, we verify M"). Low volume: no significance claimed.

Risks / claims check: no "handmade", "sustainable", "made in Latvia" or generalised fibre claims; "Riga" wording
waits for G8; Etsy proof always attributed; capacity cap enforced; window too short for a gift effect (C10).
Owner approval: [ ] (owner initials + date)

## Unblock list (in order)
1. Owner picks 5 priority SKUs (24 Oct provisional, 4 Nov confirmed) - decision 2.
2. Owner times units, PRD costs them, owner confirms; `unit_economics.py` gives BE_CAC (G0, G1; by 4-11 Nov).
3. FIN sets minimum contribution per order (decision 23, 4 Nov) and confirms cash above buffer (G3).
4. PRD lists the SKU GREEN with max units (G2).
5. Owner/CRE bind variant photos; CRO passes the landing brief (G4, by 14 Nov).
6. Owner decides plan upgrade (decision 24, 4 Nov); conversion checklist run if upgraded.
7. OPS publishes order-by dates (G5, 14 Nov).
8. Owner sets December ceiling or says EUR 0 (decision 33, 20 Nov).
