# December review + Q4 close + plan-2027-Q1 (GM-20, DRAFT skeleton)

Author: GM (agent), 2026-10-21. Task GM-20. Due 2027-01-15. Every figure below is TODO/FILL until the December
and Q4 owner exports arrive. Targets for 2027 reset from Q4 actuals only (no invented targets; README s10). December
review also triggers the annual commercial review inputs for GM-24.

## 1. Q4 2026 actuals needed before any 2027 target is set
| Series | Oct (filled in `monthly-2026-10`) | Nov | Dec | Q4 total | Status |
|---|---|---|---|---|---|
| Orders site / Etsy | __ / __ | __ / __ | __ / __ | __ / __ | TODO |
| Net revenue ex VAT (EUR) | __ | __ | __ | __ | TODO |
| Sessions (GA4) | __ | __ | __ | __ | TODO |
| New / repeat customers | __ / __ | __ / __ | __ / __ | __ / __ | TODO |
| Contribution (once G1 clears) | __ | __ | __ | __ | TODO |
| Markets/stall revenue (if any) | __ | __ | __ | __ | TODO (GM-15) |

## 2. December review (peak, freeze, gift cutoffs)
| KPI | Dec | Evidence source | Status |
|---|---|---|---|
| Net revenue ex VAT | __ | Squarespace + Etsy | TODO |
| Orders site / Etsy | __ / __ | owner export | TODO |
| On-time dispatch % | __ | Ops log (OPS-15) | TODO |
| Gift cutoff outcome vs carrier table (G5, published 20 Nov) | __ | Ops + MC/visibility | TODO |
| Paid test run outcome (EUR 0 default, decision 33) | __ | GM-18, Growth gates | TODO |
| CAC vs BE_CAC (if any spend happened) | __ | `unit_economics.py` | TODO |

## 3. Year-end gates snapshot (from `gate-tracker.md` at 31 Dec)
Cleared __ of 10. Past-due owner rows from `owner-unblock-pack.md`: __. Any gate still OPEN at 31 Dec carries into
Q1 2027 as a blocker for the first budget line.

## 4. Q4 close questions for the owner (max 3)
| # | Question | Evidence available | Owner | By |
|---|---|---|---|---|
| 1 | Did any priority SKU (priority-5 list) cover its 3 x BE_CAC in the December test window? | pending data | | 15 Jan |
| 2 | Is the Squarespace plan decision (24) still correct after Q4 sales? | plan-upgrade memo | | 15 Jan |
| 3 | Which ZIP-less question or assumption A-ID must be confirmed before Q1? | assumptions-wave3.md | | 15 Jan |

## 5. `plan-2027-Q1` skeleton (fill from Q4 actuals only)
### 5.1 Targets reset from Q4 actuals (no new invention)
| Metric | Q4 2026 actual (avg/week) | Q1 2027 target | Basis / condition |
|---|---|---|---|
| Sessions | __ | TODO range (owner confirms direction) | needs 4 WBR rows pattern |
| Orders | __ | TODO range | needs G7 (measurement) |
| Net revenue | __ | TODO range | TODO |
| Contribution (if G1 closed) | __ | TODO range | TODO |

### 5.2 Channel and content (decision 35 in Q1 sets the range direction)
Channel CAC verdicts (scale/hold/stop) and content KPI ranges are not set here; they are owned by GM-21/GM-22 after a
quarter of measured data. This file only resets the baseline.

### 5.3 Assumptions carried forward
All A-GM, A-PRD, A-OPS assumptions still open on 31 Dec stay ASSUMED with their A-ID and move into
`business-os/head-of-ecommerce/assumptions-wave3.md` / next wave. None is re-stated as fact.

## 6. Decisions for January (max 3)
| # | Decision | Evidence | Owner | By | Reversible |
|---|---|---|---|---|---|
| 1 | Approve Q1 floors only, not targets | Q4 actuals | | 15 Jan | Yes |
| 2 | Approve or reject Squarespace plan change for Q1 | Billing screenshot + Q4 sales | | 15 Jan | Yes |
| 3 | Carry the December paid-test result into Q1 (continue / stop) | Growth readout | | 15 Jan | Yes |

## Inputs checklist for 15 Jan
- [ ] December Squarespace + Etsy exports  - [ ] December GA4 sessions
- [ ] Ops dispatch log for December (OPS-18)  - [ ] December finance close (FIN-24)
- [ ] Growth December readout and kill lines
- [ ] Q4-complete WBR rows (8+ by 28 Dec) for GM-17 re-baseline if not yet done

DRAFT skeleton. No number pasted. `business-os/kpi-weekly.csv` only after owner paste.
