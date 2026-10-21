# Cash buffer, minimum contribution and stall verdict, on assumptions (FIN-05, FIN-07, FIN-17) — DRAFT for owner

Author: aw-finance (agent), 2026-10-21, wave 3, ASSUMPTION MODE. **Every number here is an ASSUMPTION or an
illustration, not a fact.** Registers: `business-os/head-of-ecommerce/assumptions-wave3.md` (A-GM-08/09/15/20/23/27/29),
`business-os/finance/assumptions-wave3.md` (A-FIN-04/06), margins in `business-os/finance/sku-margins-assumed-wave3.md`.
**Opening balance: UNKNOWN. No value is assumed.** Every verdict is conditional: "affordable if the bank balance on
the day is at least EUR X". The owner checks that line against the bank.
Not accounting, tax or investment advice. Nothing paid, booked or sent.

## 1. FIN-07 Cash buffer (rule: 8 weeks of fixed costs, A-GM-09)
| Fixed-cost scenario (illustrative, README s8 cap) | EUR / month | Weekly (x 12 / 52) | Buffer = 8 weeks |
|---|---|---|---|
| Lean | 100.00 | 23.08 | 184.62 |
| Mid | 175.00 | 40.38 | 323.08 |
| **High (planning case, A-GM-09)** | 250.00 | 57.69 | **461.54** |

**Proposed buffer: EUR 461.54** (the GM register says "about EUR 460"). This is ASSUMED until the owner's fixed-cost
list (form row 2) replaces the scenario and the owner approves (form row 6). Trigger: when the projected closing balance
falls below the buffer in any of the 13 weeks, pause all uncommitted spend and tell the GM.

## 2. 13-week net change, zero-sales base (FIN-08 roll-forward input; net change only)
Base = 0 orders (no direct sales history). Committed spend EUR 0 (A-FIN-06). Payments = fixed costs only, spread
weekly (real pay dates TODO owner). Downside = Base + one unplanned cost equal to one month of fixed costs.
| Scenario | Net change, 13 weeks | Balance needed today to stay >= buffer through week 13 (Base) | Downside |
|---|---|---|---|
| Lean | -300.00 | 484.62 | 584.62 |
| Mid | -525.00 | 848.08 | 1,023.08 |
| **High** | **-750.00** | **1,211.54** | **1,461.54** |

Read: **if the bank balance (plus Stripe/Etsy balances that pay out within 13 weeks) is at least EUR 1,461.54, the business
stays above the High buffer for 13 weeks with zero sales and one surprise bill.** Below EUR 1,211.54, cut fixed costs or
add sales before any new spend. Etsy payouts are excluded because there is no figure (TODO owner, form row 4).

## 3. FIN-05 Minimum contribution per order
**ASSUMED: EUR 10 per order (A-GM-20)**, sensitivity EUR 5 / 15. Finance check of the GM's figure:
- Method `min-contribution-method.md`: Mid fixed costs EUR 175 / 20 orders a month = EUR 8.75, rounded up. At the High
  case (EUR 250) the same volume gives EUR 12.50, so EUR 10 is not conservative at High costs. Finance flags it but
  does not change it: a EUR 15 minimum would leave only P2/P3 in the Baltics, and there are 0 orders to test with.
- With EUR 10 (from `sku-margins-assumed-wave3.md`): bid ceilings LV P2 15.83, P3 13.00, P4 8.82, P1 3.87, P5 3.09.
  No priority SKU has bid room in EU other or US/CA/AU.
- Finance proposal for the owner: **approve EUR 10 now, and re-set it to monthly fixed costs / actual orders after
  the first full month with 10 or more orders.**

## 4. FIN-17 Market stall verdict (A-GM-15: KuKu Tirgus, LIDO, 2026-11-29, EUR 50.00, apply by 2026-11-10)
Stall sale contribution per unit (A-FIN-04: no shipping, no Squarespace fee, card fee proxy 2.8% + 0.25, packaging 1.50):
| SKU | Contribution per stall sale EUR | Sales to cover the EUR 50.00 fee | Assumed physical units (A-PRD-12) |
|---|---|---|---|
| P2 Dusty Pink Merino Raglan | 40.33 | 2 | 6 |
| P3 Classic Lambswool Crew | 36.34 | 2 | 8 |
| P4 Hat & Scarf Set (Black) | 30.57 | 2 | 6 |
| P1 Merino Raglan Cardigan | 28.68 | 2 | 6 |
| P5 Rib-Knit Beanie | 20.85 | 3 | 0 (made to order; bring only units the owner counts) |

**Conditional verdict: KuKu is affordable only if the bank balance is at least EUR 1,261.54 on the booking day**
(13-week High base EUR 1,211.54 + fee EUR 50.00; extras such as a table, float and travel are TODO and must be
added). Break-even = 2 garment sales or 3 beanies. No stall revenue is counted in the forecast until the owner books.
Baltic EXPO (non-refundable) and White Xmas (after the EU cutoff): **not affordable on this evidence** (A-GM-15).
Status stays **BLOCKED**: the verdict needs the real bank balance, a physical stock count and the owner's stall choice.
Finance never books.

## Open (owner)
Bank + platform balances and dates (form row 1); fixed-cost list (row 2); payout schedules (row 4); stall choice and
extras (row 15); physical stock (row 16).

DRAFT for owner. Assumptions and illustrations, not facts. Not sent.
