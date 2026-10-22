# Q2 2027: channel CAC verdicts (scale/hold/stop) + Growth/CRO hire decisions (GM-22, DRAFT skeleton)

Author: GM (agent), 2026-10-21. Task GM-22. Due 2027-06-30. Verdicts are made on measured CAC vs BE_CAC and on
hiring triggers, not on assumptions. Every cell below is TODO/FILL; assumed values (A-GM-*) stay ASSUMED until
confirmed.

## 1. Channel CAC vs BE_CAC (from `unit_economics.py` once G1 clears)
| Channel | Q2 spend (EUR) | Orders attributed | CAC actual (EUR) | BE_CAC per SKU/channel (EUR) | Verdict | Evidence | Notes |
|---|---|---|---|---|---|---|---|
| Google free listings (organic) | 0 | __ | 0 | n/a (free) | keep / grow | GSC/SEO | |
| Pinterest | __ | __ | __ | __ | scale / hold / stop | TODO | |
| Meta (paid, default EUR 0) | __ | __ | __ | __ | scale / hold / stop | only if GM-18 = go | |
| Google paid (Shopping/Search) | __ | __ | __ | __ | scale / hold / stop | only if GM-18 = go | |
| Creator gifting | __ | __ | __ | __ | scale / hold / stop | UTM + codes/notes | |
| Markets / stalls | __ | __ | __ | __ | run / stop | GM-15 outcome | |
| Store direct / email | __ | __ | __ | __ | keep / grow | owned traffic | |

Verdict rule: channel runs only if CAC <= BE_CAC of the SKU it promotes (money chain). If CAC > BE_CAC, hold or
stop until cost, PDP, or targeting changes.

## 2. Quarterly paid-test review (if any spend happened)
| Concept | SKU | Spend (EUR) | BE_CAC | Outcome | Decision |
|---|---|---|---|---|---|
| | | __ | __ | pass / fail / inconclusive | continue / kill |
Total ceiling spent: __ of __ approved. Kill lines respected: yes / no. Lessons feed Q3 plan.

## 3. Growth hire decision against triggers
| Trigger | Threshold (owner) | Q2 measured | Met? | Evidence | Decision | By |
|---|---|---|---|---|---|---|
| Rolling 3-month order avg above threshold | TODO | __ | yes / no | GM-11 rows | hire / hold | 30 Jun |
| Paid test closed or running | TODO | __ | yes / no | GM-18 outcome | hire / hold | 30 Jun |
| BE_CAC known per promoted SKU | yes/no | TODO | yes / no | `unit_economics.py` | hire / hold | 30 Jun |
Decision: hire Growth in Q3 / defer. No hire on assumption alone (C13). Cost line appears only in the 2027 budget.

## 4. CRO hire decision against triggers
| Trigger | Threshold (owner) | Q2 measured | Met? | Evidence | Decision | By |
|---|---|---|---|---|---|---|
| Conversion rate improvement (G7 required) | TODO | __ | yes / no | GA4 + plan decision | hire / hold | 30 Jun |
| PDP conversion signal verified | TODO | __ | yes / no | CRO packs + Code Injection outcome | hire / hold | 30 Jun |
Decision: hire CRO in Q3 (fractional/full-time) / defer. Capacity referenced from PRD capacity file.

## 5. Cre-retable / CX / Fulfilment / Production triggers
| Role | Trigger source | Q2 status | Decision |
|---|---|---|---|
| CX part-time | orders/volume (hiring triggers) | TODO | |
| Fulfilment operator | dispatch volume | TODO | |
| Production capacity (weaving/knitting) | PRD queue + capacity | TODO | |
| SEO/Pinterest freelancer | SEO trigger check | TODO | |

## 6. Assumptions status at 30 Jun 2027
A-GM/A-PRD/A-OPS rows still UNCONFIRMED: __ of __. Closures recorded in the assumption registers with dated
evidence; none re-stated as fact.

## Decisions for owner (max 3)
| # | Decision | Evidence | Owner | By | Reversible |
|---|---|---|---|---|---|
| 1 | Scale / hold / stop per channel (table 1) | channel CAC vs BE_CAC | | 30 Jun | Mostly yes |
| 2 | Growth hire go / no-go | triggers table 3 | | 30 Jun | Partly |
| 3 | CRO hire go / no-go | triggers table 4 | | 30 Jun | Partly |

DRAFT skeleton. No number pasted. No hire approved without a trigger met and owner yes (C13).
