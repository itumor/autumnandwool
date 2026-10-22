DRAFT — for owner approval. PRE-DRAFT prepared 2026-10-21; finish and re-date on Mon 26 Oct.

# Ops weekly 2026-W44 (issued Mon 26 Oct; reports week_start 2026-10-19, Mon 19 - Sun 25 Oct)

Agent `aw-operations`, OPS-14, format from `ops-weekly-template.md`. Readiness edition: there is no real direct
order yet, so section 1 reports counts only and sections 2-4 stay empty until the first order.
Sources: `dispatch-log-template.csv` (no live `dispatch-log.csv` yet), `returns-log-template.csv` (no live log),
`plans/2026-2027/status/operations.md`, `owner-inputs-wave2.md`; capacity file: none exists (Production write
blocked, PRD-02).

## 1. KPIs (counts only; % from 30+ orders)

| KPI | This week | Q4 to date | Target | Note |
|---|---|---|---|---|
| Orders received (site / Etsy / market) | [FILL 26 Oct: Squarespace Orders export 19-25 Oct, excl. test #00003/#00004] / [FILL Etsy, if active] / 0 | same | none (no baseline) | Owner export, same one GRO-06/GM-07 ask for |
| Orders dispatched | [FILL] | | | |
| On-time dispatch | [FILL n/N] | | >= 95% | |
| Fulfilment errors | [FILL] | | <= 2%, 0 wrong item | |
| Fulfilment cost per order EUR | n/a | | vs `shipping_eur` + `packaging_eur` (both blank in sku-economics) | No carrier rate or packaging cost known |
| Tracking sent same day | n/a | | 100% | |
| Tracking exceptions acted on early | n/a | | 100% | |
| Returns / withdrawals opened | [FILL] | | 100% logged | |
| Refunds due within 3 days | none | | 0 missed | |

If the export shows 0 orders: write "0" in every count and "n/a" in rates.

## 2. Cost per order by region
No orders. Carrier rates: none filled (OPS-06 BLOCKED, owner item 4).

## 3. Returns by reason and SKU
No cases.

## 4. Open cases with deadlines
None. [FILL if any CX hand-off arrived 21-25 Oct.]

## 5. Proposed kpi-weekly.csv values (owner/Finance append; agent never edits the CSV)
week_start=2026-10-19, on_time_dispatch_pct=[blank if 0 dispatched], shipping_packaging_payment_eur=[blank if 0
orders; payment fees from Finance, `business-os/finance/payment-paths-and-payouts.md`]

## 6. Readiness status (until first real order)

| Item | Status 21 Oct | Due | Owner input (form item) |
|---|---|---|---|
| SOP, dispatch checklist, log templates, packaging spec, returns procedure | Drafted (wave 1) | done | approve |
| Dispatch promise | Open | 24 Oct | item 1 (MP 3) |
| Physical stock per SKU | Open | 24 Oct | item 2 (MP 4) |
| Packer + daily cut-off | Open | 24 Oct | item 3 |
| Carriers used | Open | 28 Oct | item 4 (MP 8) |
| Dry-run inputs (scale, items, recipients, label budget) | Open | 30 Oct | items 6-9 |
| Return address, return postage, packaging | Open | 30 Oct | items 10-12 (MP 13) |
| Free-shipping regions | Open | 31 Oct | item 13 (MP 21) |
| Adviser pack sent | Ready to send: `adviser-pack-shipping-returns.md` | 3 Nov | item 15 (MP 22) |
| Dry run | Planned Fri 6 Nov | 6 Nov | needs items 4, 6-9 |
| Carrier-backed Christmas dates (G5) | Provisional table only | 14 Nov | needs dry run + items 1, 2, 4, 13 |

[FILL 26 Oct: tick any item answered between 21 and 25 Oct.]

## 7. Proposals
- None new. If 0 orders again: keep weekly readiness edition; first full edition the Monday after the first
  real order.

## TODO / missing data
- Owner Squarespace Orders export 19-25 Oct (and Etsy if active) — fill section 1 on 26 Oct.
- Owner answers in `owner-inputs-wave2.md` received by 25 Oct — update section 6.
