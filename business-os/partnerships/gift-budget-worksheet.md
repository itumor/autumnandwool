# Gift budget worksheet (PAR-11 prep, also PAR-15) - DRAFT

Status: DRAFT, prepared 2026-10-21. Every EUR cell is TODO: 0 of 82 SKUs are costed in `sku-economics.csv`, no
capacity file exists, no carrier rate is filled and the minimum contribution is not set. No number here is invented.
Finish when the inputs in section 4 arrive (target 15 Nov).

**Wave 3 (2026-10-21, assumption mode):** cells are now filled with ASSUMED values from the shared registers, marked (A).
They are not facts. Register: `business-os/partnerships/assumptions-wave3.md`. Result in section 5.

## 1. Inputs and where they come from

| Input | Source (other department) | State 2026-10-21 |
|---|---|---|
| materials_labour_eur per gift SKU | `business-os/sku-economics.csv` via Production (master #5) | Empty |
| packaging_eur | `business-os/operations/packaging-spec.md` pack types: beanie = P1, hat & scarf set = P3 | Pack types set, quotes TODO |
| shipping_eur to creator country | `business-os/operations/carrier-rates.md` regions LV / BALT / EU-18 | Template only, rates TODO |
| CM2 = break-even CAC per SKU | `python3 business-os/unit_economics.py` (`contrib`) after costs | 0 costed |
| Minimum contribution per order | `business-os/finance/min-contribution-method.md` (owner decision, 4 Nov) | Method only |
| Gift SKUs allowed | GM rule (decision pack 31 Oct, #12): priority 5 only, G8-cleared; capacity GREEN/AMBER | Priority 5 provisional (`head-of-ecommerce/priority-5-sku-proposal-2026-10-21.md`) |
| Number of gifts | Owner D2 (form O6) | Open |

## 2. Formulas

```
gift_cost      = materials_labour_eur + packaging_eur(pack type) + shipping_eur(creator region)
BE_CAC         = CM2 of the gifted SKU (unit_economics.py contrib)
max_CAC        = CM2 - minimum contribution            (Finance method, step 6)
programme_cap  = approved_gifts x gift_cost
go rule        = gift_cost <= max_CAC x expected orders per gift   (we have no evidence for expected orders,
                 so plan with 1: each gift must pay back with at least one attributed order)
stop rule      = 60 days after shipping: total creator cost / attributed orders > BE_CAC -> stop or change deal
```

Note: a single gift costing more than max_CAC needs two or more attributed orders to pay back. The owner should see
that before approving it.

## 3. Per-SKU table (gift candidates in the priority 5 only)

Prices from the priority-5 proposal; ex VAT = price / 1.21.

| SKU | Price incl. VAT | Ex VAT | Pack | Materials+labour | Packaging | Ship LV | Ship EU-18 | Gift cost LV | Gift cost EU | CM2 (BE_CAC) | Min contribution | Max CAC | Gift fits? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rib-Knit Beanie, unisex | EUR 45.00 | EUR 37.19 | P1 | 13.33 (A) | 1.50 (A) | 5.00 (A) | 22.00 (A) | **19.83** (A) | 36.83 (A) | 13.09 LV (A) | 10 (A) | 3.09 LV (A) | No per gift. Yes at programme level if ~2 orders per gift (s5) |
| Merino Wool Hat & Scarf Set (Black only until photos) | EUR 110.00 | EUR 90.91 | P3 | 55.51 (A) | 1.50 (A) | 5.00 (A) | 22.00 (A) | **62.01** (A) | 79.01 (A) | 18.82 LV (A) | 10 (A) | 8.82 LV (A) | No: needs 4 orders to break even. Owner-approved swap only |

(A) = ASSUMPTION, wave 3. A-PRD-20/21, A-OPS-02/05/10, A-GM-20 and the GM CM2 table; register:
`business-os/partnerships/assumptions-wave3.md` (A-PAR-01). EE/LT shipping 6.00 adds EUR 1.00 per gift. The Nov-Dec +7%
surcharge (A-OPS-09) adds about EUR 0.35-0.42.

Dropped from wave-1 candidates: lightweight turtleneck (alternate only, not in the priority 5; GM rule #12). Re-add
if the GM swaps it in on 4 Nov.

## 4. Programme cap (owner fills O6/O7 in `owner-inputs-wave2.md`)

| Line | Value |
|---|---|
| Approved gifts (D2) | __ (proposal 5-8). **ASSUMED 5** (A-GM-17 as amended by GM ruling W3-5) |
| Mix (beanie / hat set) | __ / __. **ASSUMED 5 / 0**, hat set Black as a per-creator swap only (A-PAR-03) |
| Programme cap EUR | **ASSUMED EUR 110**, adopted by GM ruling W3-5 (5 x 21.25 Baltic worst case = 106.25; about EUR 150 with one hat-set swap, which needs a separate owner yes) (A-PAR-05) |
| Max per single gift EUR | **ASSUMED EUR 22** (beanie, LV/EE/LT only; A-PAR-04/05) |
| Cash out (excl. owner labour) | about EUR 71 + about 3 h of owner time (A-PAR-02) |
| Owner initials + date | __ |

## 5. Wave-3 result on assumptions (2026-10-21, PAR-11 ASSUMED)

ASSUMPTION: gift cost beanie LV 19.83 / EE-LT 20.83, hat set LV 62.01; 5 beanie gifts, cap EUR 110, max EUR 22 per
gift; break-even on blended priority-5 CM2 LV 18.92; register: `business-os/partnerships/assumptions-wave3.md`.

**Adopted reading (GM ruling W3-5, 2026-10-21; owner confirms the count by 28 Oct and EUR 110 by 15 Nov):**

| Term | Adopted value |
|---|---|
| Budget | Fixed test budget **EUR 110** (about EUR 71 cash + about 3 h owner time) |
| Gifts | **5 Rib-Knit Beanies**, one photographed colour [VERIFY which] |
| Creators | **LV / EE / LT only** (A-PAR-04) |
| Max per gift | **EUR 22** landed (beanie LV 19.83 / EE-LT 20.83; 21.25 with Nov-Dec surcharge) |
| Payback rule | CM2 of creator-attributed orders >= programme cost within **60 days** of each ship date (A-PAR-06/08). About **6** attributed orders (blended) for the programme |
| Verdict | **31 Jan 2027** (PAR-23 day-90 verdict) |
| Approval | **Each gift is an owner-approved spend**, one by one. **No gift ships before G4** |
| Not included | No code, no discount, no commission, no cash fee (A-PAR-10). Hat & scarf set swap needs a separate owner yes (raises the total to about EUR 150, outside the EUR 110) |

A-GM-17 is amended by the GM. The old per-gift reading below is kept as history only.

| Check | Result |
|---|---|
| Per gift vs the beanie's break-even CAC (A-GM-17 original wording, superseded by W3-5) | Failed: 19.83 > 13.09. No gift SKU passed per gift. Raised as W3-PAR-1, **resolved by W3-5** |
| Programme rule (skill s1, 60 days) | 5 beanies (106.25) break even at **6 attributed orders** (blended) / 9 (beanie-only). Keeping the EUR 10 minimum: 12 / 35 |
| Per creator | 1 beanie gift needs **2 attributed orders** to break even and **3** to keep the EUR 10 minimum (blended) |
| EU-other creators | Excluded in Q4: gift 36.83 and EU-other beanie CM2 -3.91 (A-PAR-04) |
| Expected orders per gift | **Not assumed** (A-PAR-07). The day-90 verdict tests it |

Full table: `assumptions-wave3.md` "Break-even per creator and per programme".

### History: the two readings of the A-GM-17 gift cap (W3-PAR-1, resolved by GM ruling W3-5 on 2026-10-21; Growth raised the same flag in `growth/assumptions-wave3.md`)

| Reading | Rule | Gifts allowed in Q4 | Cap |
|---|---|---|---|
| **1. As written** (A-GM-17) | Landed gift cost <= the beanie's break-even CAC (LV 13.09) | **0**. Beanie gift 19.83 and hat set 62.01 both fail. The creator test channel (A-GM-07 B) cannot run | EUR 0 |
| **2a. Proposed: programme payback** (skill s1) | Total creator cost / attributed orders <= break-even CAC within 60 days. Stop or change the deal if not | 5 beanies, needs >= 6 attributed orders (blended) to pass | EUR 110 |
| **2b. Proposed: fixed test budget** | Owner approves a capped EUR test budget, written off as a learning cost. Judged at day 90 (PAR-23) on cost per attributed order | 5 beanies | EUR 110 total, EUR 22 per gift, about EUR 71 cash |
| 2c. Variant: gift cost <= expected creator contribution | Needs an expected-orders figure. None exists, and none is assumed (A-PAR-07) | Can't be evaluated until wave-1 data exists | n/a |

Partnerships proposed **2a + 2b together**: a fixed EUR 110 cap, judged by the 60-day payback rule. (Before the ruling:
"Reading 1 stays the GM's rule until the GM rules.") **Outcome: GM ruling W3-5 accepted 2a + 2b** as the adopted
reading (table at the top of section 5); reading 1 is retired. Still an assumption until the owner confirms. No gift
is approved by the ruling: every gift still needs the owner's yes, and none ships before G4. The GM file is not
edited by Partnerships.

## 6. To finish (agent, when real numbers arrive)
1. Read costs once Production/Finance fill `sku-economics.csv` and run `unit_economics.py`. Replace every (A) cell.
2. Re-run section 5 per region, flag any gift where gift cost > max CAC.
3. Put the result in the owner form (O7) and the gift spec (`creator-brief-gifting.md` Part B).
