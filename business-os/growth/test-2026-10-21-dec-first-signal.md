# Test: dec-first-signal   Status: BLOCKED

Drafted 2026-10-21 by aw-growth-marketing (skill `aw-paid-ads-testing`). Default under master ruling C10 is **no
December test, EUR 0**. This brief exists so that, if all gates pass by 20 Nov, the owner can decide in one sitting.
Purpose: learning (first CAC read), not gift-season revenue.

Gates: costed FAIL / safe-to-promote MISSING / PDP FAIL / orders countable PASS / conversion signal UNVERIFIED / budget MISSING
(detail and owners: `paid-test-gates.md`)

SKU(s): ONE SKU, owner's pick from the 5 priority SKUs (master decision 2, re-confirmed 4 Nov). TODO.
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
