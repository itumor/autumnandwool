# Finance — status 2026-10-21
Summary: 14 done · 7 blocked · 8 todo
| ID | Task | Due | Status | Output / blocker |
|---|---|---|---|---|
| FIN-01 | Cost-collection request for 22 visible SKUs, incl. data anomalies and public fee research | 2026-10-21 | DONE | [cost-collection-request-2026-10-21.md](../../../business-os/finance/cost-collection-request-2026-10-21.md) |
| FIN-02 | Cost-proposal staging sheet + review checklist for PRD proposals (8 SKUs 2026-10-30, 22 SKUs 2026-11-06, ruling C4) | 2026-10-30 | DONE | [sku-cost-proposals-staging.csv](../../../business-os/finance/sku-cost-proposals-staging.csv), checklist in FIN-01 file |
| FIN-03 | Run `unit_economics.py` on owner-confirmed costs; break-even CAC for 5 priority SKUs to GM/GRO | 2026-11-04 (GRO 2026-11-15) | BLOCKED | Owner G0 production inputs + PRD cost proposals + owner writes confirmed values to `sku-economics.csv` (G1); GM/owner 5 priority SKUs (2026-10-24) |
| FIN-04 | Minimum contribution per order: method + owner decision form | 2026-11-04 | DONE | [min-contribution-method.md](../../../business-os/finance/min-contribution-method.md) |
| FIN-05 | Minimum contribution EUR proposal + owner decision | 2026-11-04 (fallback 2026-11-11) | BLOCKED | Needs FIN-03 (CM2 of 5 SKUs) and owner fixed-cost list; owner decides |
| FIN-06 | Owner finance inputs form: opening balance + date, fixed costs, payout schedules, accountant details, committed spend | 2026-10-28 | DONE | [owner-finance-inputs-2026-10-21.md](../../../business-os/finance/owner-finance-inputs-2026-10-21.md) |
| FIN-07 | Cash buffer (proposal: 8 weeks of fixed costs) approved | 2026-10-28 | BLOCKED | Owner: fixed-cost list, then approval (proposal in FIN-06 file s6) |
| FIN-08 | First 13-week cash forecast (net change only, zero-sales base) | 2026-10-26 | DONE | [cash-forecast-2026-10-26.md](../../../business-os/finance/cash-forecast-2026-10-26.md); payments TODO until FIN-06 filled |
| FIN-09 | Weekly Monday routine SOP (exports, roll forecast, variance > EUR 100, CAC check, anomalies, GM hand-off) | 2026-10-26 | DONE | [weekly-finance-routine-sop.md](../../../business-os/finance/weekly-finance-routine-sop.md) |
| FIN-10 | WBR money-column check list + KPI formulas | 2026-10-26 | DONE | [weekly-finance-routine-sop.md](../../../business-os/finance/weekly-finance-routine-sop.md) s3 |
| FIN-11 | Baseline `kpi-weekly.csv` money columns, week 2026-10-19 (ruling C16), in WBR of 2026-10-26 | 2026-10-26 | TODO | Week closes 2026-10-25; needs Squarespace Orders export; owner appends |
| FIN-12 | Anomaly and test-order log, seeded with #00003/#00004, duplicate SKUs, placeholder stock, Squarespace 2% fee | 2026-10-21 | DONE | [anomaly-log.md](../../../business-os/finance/anomaly-log.md) |
| FIN-13 | Spend guardrail checklist (F7, ruling C10, ruling C13) | 2026-10-21 | DONE | [spend-guardrail-checklist.md](../../../business-os/finance/spend-guardrail-checklist.md) |
| FIN-14 | Payment paths, payout schedule record, monthly test-order tie-out template | 2026-10-31 | DONE | [payment-paths-and-payouts.md](../../../business-os/finance/payment-paths-and-payouts.md) |
| FIN-15 | PayPal connected + PayPal test order/refund recorded as excluded | 2026-10-31 | BLOCKED | Owner: connect PayPal (action pack B1, decision 14), place + refund test order |
| FIN-16 | Q4 spend-check worksheets: Squarespace upgrade, stalls, December test, creator gifting, yarn, backup site | 2026-11-04 | DONE | [spend-checks-q4-2026.md](../../../business-os/finance/spend-checks-q4-2026.md); verdicts wait on FIN-06/FIN-07 |
| FIN-17 | Market stall affordability verdicts (Baltic EXPO ASAP, KuKu 2026-11-10, White Xmas 2026-12-14) | 2026-11-10 | BLOCKED | Owner: opening balance + physical stock; PRD capacity file; stall prices (only KuKu EUR 50 published) |
| FIN-18 | Free-shipping cost by region vs CM2 (decision 21/28) | 2026-11-11 | BLOCKED | OPS + owner: carriers and rates per region (decision 8); FIN-03 CM2 |
| FIN-19 | Gift-season perks margin check (decision 31) | 2026-11-14 | BLOCKED | CX/CRO perk list + costs; FIN-03 CM2 |
| FIN-20 | Accountant question list (VAT/OSS, Etsy, markets, gifts, deadlines, year-end) | 2026-11-06 | DONE | [accountant-questions-2026-10-21.md](../../../business-os/finance/accountant-questions-2026-10-21.md); owner sends |
| FIN-21 | October 2026 accountant pack draft (checklist, request list, tie-out notes) | 2026-11-06 [VERIFY] | DONE | [accountant-pack-2026-10.md](../../../business-os/finance/accountant-pack-2026-10.md); all documents MISSING until owner exports after month-end |
| FIN-22 | Monthly finance review template (cash, payroll, SKU and channel profitability) | 2026-11-06 | DONE | [monthly-finance-review-template.md](../../../business-os/finance/monthly-finance-review-template.md) |
| FIN-23 | October monthly finance review | 2026-11-06 | TODO | Month closes 2026-10-31 |
| FIN-24 | November accountant pack + monthly review | 2026-12-04 | TODO | Month not started |
| FIN-25 | December / year-end 2026 pack + inventory count | 2027-01-08 | TODO | Year-end; count method from accountant (Q12) |
| FIN-26 | Q1 2027: year-end pack by 2027-01-15, season post-mortem by SKU/channel, all 82 SKUs costed or retired, VAT/OSS review, 2027 budget envelope by 2027-01-31 | 2027-03-31 | TODO | Starts 2027-01 |
| FIN-27 | Q2 2027: channel P&L and CAC verdicts, test caps tied to break-even CAC, observed repeat rate, pricing proposals, fee-mix review | 2027-06-30 | TODO | Starts 2027-04 |
| FIN-28 | Q3 2027: season purchase plan with cash timeline by 2027-08-31, stall costing, mid-year profitability, hire affordability | 2027-09-30 | TODO | Starts 2027-07 |
| FIN-29 | Q4 2027: weekly season cash watch, CM in KPI sheet, year-end pack by 2027-12-31, 2028 budget draft by 2027-12-15 | 2027-12-31 | TODO | Starts 2027-10 |

## Blocked on owner
- Opening bank balance + date, Stripe/Etsy balances, fixed-cost list, payout schedules, accountant deadlines (fill `business-os/finance/owner-finance-inputs-2026-10-21.md`, due 2026-10-28). Without them no cash verdict, buffer or spend check is possible.
- Production inputs (G0) and confirmation of cost proposals into `sku-economics.csv` (5 priority SKUs 2026-11-04, all 22 by 2026-11-11); also physical stock (turtleneck 360 / beanie 220) and whether 3 duplicate-title SKU pairs are duplicates.
- Approve cash buffer (proposal: 8 weeks of fixed costs) by 2026-10-28; set minimum contribution per order by 2026-11-04.
- Confirm Squarespace plan name: if Basic, every order pays a 2% store fee (EUR 0.90-3.30 per order at current prices); upgrade decision due 2026-11-04 (Core break-even at EUR 300.00/mo sales on annual billing, public prices read 2026-10-21).
- Connect PayPal and run one test order + refund by 2026-10-31.
- Send accountant question list (`accountant-questions-2026-10-21.md`) by 2026-11-06; supply October exports (Squarespace Orders, Stripe payouts, bank statement, invoices) after month-end.
- Market stall choice (Baltic EXPO ASAP, KuKu by 2026-11-10) only after the cash inputs above; decide whether to keep the Squarespace backup copy (trial ends 2026-11-01).
