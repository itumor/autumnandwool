# Paid budget proposal, January 2027   Status: DRAFT skeleton (GRO-22), prepared 2026-10-21, finish 15 Dec 2026

aw-growth-marketing. Rule: ceiling = lower of the owner's number and (planned tests x 3 x BE_CAC). No budget for any
SKU without BE_CAC, GREEN capacity and Max CAC > 0. Evidence comes from December; every TODO is filled on 15 Dec.

## 1. December evidence (fill 15 Dec; update after 31 Dec)
| Line | Value | Source |
|---|---|---|
| Paid spend Dec | TODO (EUR 0 if NO-GO) | owner confirmation |
| Squarespace orders Nov / Dec to date | TODO | Orders export |
| New customers | TODO | Orders export |
| Free-channel sessions by source (Merchant Center free listings, Pinterest, bio, Etsy link, referral) | TODO | GA4 |
| Orders after a UTM visit, by campaign (directional) | TODO | GA4 + Orders |
| December test result (if run): CAC vs BE_CAC per concept, call | TODO | `ads-results-log.csv` |
| Conversion signal in place (plan decision #24) | TODO | `paid-test-gates.md` |

## 2. BE_CAC table (copy from `be-cac-worksheet-priority-skus.md`)
| SKU | BE_CAC | Max CAC | GREEN Jan? | Max units Jan |
|---|---|---|---|---|
| TODO | | | | |

## 3. Proposal options (pick one on 15 Dec)
| Option | When it applies | Tests | Ceiling |
|---|---|---|---|
| A. EUR 0, free channels only | Fewer than 6/6 gates, or free channels not yet measured for 4 weeks | 0 | EUR 0 |
| B. One concept test | 6/6 gates pass for 1 SKU; no December read | 1 SKU x 2-3 concepts | concepts x 3 x BE_CAC = TODO |
| C. Continue a December winner | A December concept with >= 1 order and CAC <= BE_CAC (still no scaling below 3 orders) | same concept + 1 new | TODO |

January context: post-Christmas demand and returns surge (CX/OPS); Q1 plan starts real tests (GRO-24). Budget per
SKU never above PRD max units x BE_CAC.

Owner decision: [ ] A  [ ] B  [ ] C, ceiling EUR ___ (initials + date)
