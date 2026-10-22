# Q1 2027: actual cost/order proposals for sku-economics, returns wave, monthly returns review, customs/HS clarity (OPS-19, DRAFT skeleton)

Author: Operations (agent), 2026-10-22. Task OPS-19. Window Jan-Mar 2027 (due 31 Mar 2027). Future-quarter task
prepared now from the wave-3 baseline (`plans/2026-2027/status/operations.md`). No Q4 data, no measured
cost per order, no returns wave yet; every figure is TODO/FILL. Nothing is written to `sku-economics.csv`
(HARD RULE 1) until owner-confirmed costs.

## 1. Actual cost per order -> proposals for `sku-economics.csv`
- Source: Q4 2026 ops weeklies, dispatch log, dry-run records (T1-T4) and Finance staging (FIN-19).
- Cost lines per order to separate later: packaging EUR 1.50 (A-OPS-10), shipping by zone (A-OPS-02..08),
  payment (A-FIN-01/02), returns allowance 5% of net (A-GM-21), label cost (dry run).
- Proposal format: cost/order by zone + weight band; owner confirms before any CSV write. All values FILL.
- `ops-weekly-2026-W44.md`-style lines and any new ops weeklies feed this. No assumed value restated as fact.

## 2. Returns wave
- Returns received in Q4 2026 by reason (change of mind / faulty / wrong / delivery): FILL (from `returns-log-template.csv`).
- Return rate vs orders: FILL.
- Refund amounts and postage cost recovered (A-OPS-22): FILL.
- CSI CX hand-off format review and any wording changes: FILL (depends on adviser reply, OPS-16).

## 3. Monthly returns review
- Reviews filed: Jan / Feb / Mar 2027, one page each, filed last day of month.
- Sections: volume, reasons, cost, actions, adviser items. All FILL.
- Reused skeleton: `returns-review-2026-12.md` pattern. Numbers carry over from the quarterly cost-per-order work.

## 4. Customs / HS clarity
- Adviser question already on file: `adviser-pack-shipping-returns.md` Q9 (customs/HS).
- FIN accountant question: Q3 (`owner-inputs-wave2.md`).
- Owner answers (HS codes per product, CN/UK/rest-of-world rules, incoterms): FILL.
- Changes to delivery promise per region once HS clarity lands: FILL.

## 5. Reporting cadence
- Monthly ops KPI file (`ops-weekly-template.md`) each Monday through Q1; freeze-check pattern reused.
- Cost per order readout folded into WBR runs (head-of-ecommerce WBR runbook).
- All values TODO until the owner sends Q1 order/returns exports and HS answers.

## 6. Decisions needed from owner
| # | Decision | Evidence | Owner | By |
|---|---|---|---|---|
| 1 | Approve cost/order proposals before `sku-economics.csv` write | Dry runs + Q4 logs | | |
| 2 | Send adviser pack answer on customs/HS (Q9) | Adviser | | |
| 3 | Returns rate target for Q1 2027 | Q4 returns data | | |
Inputs: OPS-07/15/16, FIN-19, A-OPS-10/21/22, `adviser-pack-shipping-returns.md`, `owner-inputs-wave2.md`.
