# Operations — status 2026-10-21
Summary: 10 done · 4 blocked · 8 todo
| ID | Task | Due | Status | Output / blocker |
|---|---|---|---|---|
| OPS-01 | Owner question list (carriers, dispatch promise, stock, packer, return address, packaging, free-shipping regions, adviser extras) | 24 Oct | DONE | [owner-questions-2026-10-21.md](../../../business-os/operations/owner-questions-2026-10-21.md) |
| OPS-02 | Order-to-delivery SOP (8 stages, working-day rules, delivery problems, customs flags, notice drafts) | 24 Oct | DONE | [sop-order-to-delivery.md](../../../business-os/operations/sop-order-to-delivery.md). Facts marked [VERIFY] until owner answers OPS-01 |
| OPS-03 | Daily dispatch checklist + dispatch log template | 24 Oct | DONE | [dispatch-checklist-template.md](../../../business-os/operations/dispatch-checklist-template.md), [dispatch-log-template.csv](../../../business-os/operations/dispatch-log-template.csv) |
| OPS-04 | Packaging spec + supplies list | 30 Oct | DONE | [packaging-spec.md](../../../business-os/operations/packaging-spec.md). Quotes, sizes, weights TODO (owner decision 13, dry run) |
| OPS-05 | Carrier comparison template + candidate list + research log | 28 Oct | DONE | [carrier-rates.md](../../../business-os/operations/carrier-rates.md). No rate filled |
| OPS-06 | Carrier rates per region from public price lists, dated | 28 Oct | BLOCKED | Owner: carriers used today / business accounts (MP decision 8); packed weights from OPS-11. No official 2026 LV price list found 21 Oct (Omniva moved to dynamic pricing) |
| OPS-07 | Returns log format, procedure, withdrawal/faulty/exchange drafts, CX hand-off format | 30 Oct | DONE | [returns-handling.md](../../../business-os/operations/returns-handling.md), [returns-log-template.csv](../../../business-os/operations/returns-log-template.csv) |
| OPS-08 | Provisional Christmas cutoff table [VERIFY] | 31 Oct | DONE | [christmas-cutoffs-2026.md](../../../business-os/operations/christmas-cutoffs-2026.md). MTO order-by: LV 10 Dec, EU 3 Dec, US/CA/AU 19 Nov (before 20 Nov publish date) |
| OPS-09 | Carrier-backed cutoffs + delivery ranges (gate G5) | 14 Nov | BLOCKED | Needs OPS-06, OPS-11 and carriers' 2026 Christmas dates (Latvijas Pasts published 2025 dates on 8 Dec); owner decision 3 (dispatch promise) |
| OPS-10 | Dry-run plan (test parcels LV + EU, optional EE/LT, US) | 6 Nov | DONE | [dry-run-plan.md](../../../business-os/operations/dry-run-plan.md) |
| OPS-11 | Dry-run execution: pack, weigh, ship, track, record cost/transit | 6 Nov | BLOCKED | Owner: carrier choice, recipients, spare items, scale, label budget (OPS-01 Q1, Q6) |
| OPS-12 | Delivery-promise reconciliation across MC, Squarespace, FAQ, handbook (ruling C8) | 28 Oct | DONE | [delivery-promise-reconciliation.md](../../../business-os/operations/delivery-promise-reconciliation.md). Found: EE/LT missing from MC; Rest of World ships free to every country |
| OPS-13 | Weekly ops KPI file template | 26 Oct | DONE | [ops-weekly-template.md](../../../business-os/operations/ops-weekly-template.md) |
| OPS-14 | Weekly ops KPI file every Monday (readiness status until first order) | 26 Oct, then weekly | TODO | First issue Mon 26 Oct (`ops-weekly-2026-W44.md`) |
| OPS-15 | Daily dispatch file + 2-day tracking sweep; real label + packaging cost per order | From first real order | TODO | Triggered by first real order (0 to date) |
| OPS-16 | Returns wording to adviser; consistent wording before peak | 3 Nov send / 20 Nov | BLOCKED | Owner: send adviser pack (MP decision 22) and return address / postage rule (MP decision 13) |
| OPS-17 | Freeze check go/no-go note (policy status, carrier dates, stock/production calendar) | 20 Nov | TODO | Starts 16 Nov |
| OPS-18 | Post-peak review: Q4 cases, cost/order, carriers, return reasons | 26-31 Dec | TODO | `returns-review-2026-12.md` |
| OPS-19 | Q1 2027: actual cost/order proposals for sku-economics, returns wave, monthly returns review, customs/HS clarity | Jan-Mar 2027 | TODO | Needs Q4 data |
| OPS-20 | Q2 2027: carrier refresh, lockers, promised-vs-actual transit (80th pct), error reduction | Apr-Jun 2027 | TODO | Needs Q1 data |
| OPS-21 | Q3 2027: peak readiness 30 Sep, packaging pre-buy proposal, hire trigger, SLA review | Jul-Sep 2027 | TODO | — |
| OPS-22 | Q4 2027: carrier-backed cutoffs by 1 Oct, peak ops, annual review by 15 Jan 2028 | Oct-Dec 2027 | TODO | — |

## Blocked on owner
- Carrier(s) used today and any business account (MP decision 8, due 28 Oct): blocks OPS-06, OPS-09, OPS-11.
- Public dispatch promise, 2-5 working days or other (MP decision 3, due 24 Oct): blocks OPS-09; every cutoff date moves with it.
- Physical stock per SKU vs made-to-order (MP decision 4, due 24 Oct): blocks the in-stock column of the cutoff table.
- Return address and who pays return postage; packaging style and budget (MP decision 13, due 30 Oct): blocks OPS-16, packing slip, supplies quotes.
- Dry-run inputs: recipients (LV, EU, optional EE/LT, US), spare items, scale, label budget (due 30 Oct): blocks OPS-11.
- Send Shipping & Returns plus 3 ops questions to the EU adviser (MP decision 22, due 3 Nov): blocks OPS-16.
- Free shipping per region, restrict "Rest of World", paid express for late orders (MP decision 21, due 31 Oct / 11 Nov).
- Approve the interim delivery line in `delivery-promise-reconciliation.md` s3 for CRO/SEO use.
