DRAFT — for owner approval

# Daily dispatch checklist (template) + dispatch log format

OPS-03, agent `aw-operations`, 2026-10-21. Used only on days when orders exist. Copy to
`business-os/operations/dispatch-YYYY-MM-DD.md`. The log lives in `dispatch-log.csv` (created from
`dispatch-log-template.csv` when the first real order or the 6 Nov dry run arrives; header only today because the
CSV must stay machine-readable).

Sources: `.claude/skills/aw-fulfilment-sop` (stages, log fields), `sop-order-to-delivery.md` (this folder).

## Log columns (`dispatch-log-template.csv`)

| Column | Meaning / rule |
|---|---|
| order_no | Squarespace order no. or Etsy receipt no. One row per order line; same order_no repeats for multi-item orders |
| channel | `squarespace` / `etsy` / `market` / `dryrun` |
| order_date | YYYY-MM-DD, Riga time |
| promised_dispatch_by | order_date (or next working day if after cut-off) + promised working days (SOP s2) |
| sku, title, size, colour, qty | From the order, never from memory |
| ship_country, region | region = `LV` / `EU` / `US-CA-AU` / `other` |
| stock_or_mto | `stock` only if owner-confirmed shelf unit, else `mto` |
| mto_due_date | From Production's capacity file |
| qc_pass | Y / N (aw-qc-and-labelling 11 checks) |
| packed_date, weight_g, pack_type | pack_type from `packaging-spec.md` (P1/P2/P3) |
| dispatched_date, carrier, service, tracking | From the label / acceptance receipt. Never invented |
| label_cost_eur, packaging_cost_eur | Actuals, incl. or excl. VAT stated in notes [VERIFY with Finance which basis] |
| last_scan_date, delivered_date | From carrier tracking |
| on_time | Y if dispatched_date <= promised_dispatch_by |
| issue | `none` / `stuck` / `lost` / `damaged` / `wrong_item` / `missing_item` / `address` / `customs` / `returned_to_sender` / `late_dispatch` |

KPIs from the log: on-time dispatch = rows with on_time=Y / orders dispatched; fulfilment errors = orders with
issue in (wrong_item, missing_item, damaged) / orders; cost per order = sum(label + packaging) / orders.

## Checklist: dispatch-YYYY-MM-DD

```
DRAFT — for owner approval
# Dispatch checklist YYYY-MM-DD (working day N of week)
Sources: Squarespace Orders export / screenshot [time], Etsy orders [time], capacity-YYYY-Www.md, dispatch-log.csv

## 1. New orders since last check
| order_no | channel | item / size / colour | country | paid? | address complete? | stock or MTO | promised_dispatch_by | flag |
Count check: Squarespace new = __, Etsy new = __, rows added = __ (must match)

## 2. Due today or overdue (promised_dispatch_by <= today, not dispatched)
| order_no | item | status (making / QC / packed) | blocker | action today |

## 3. Made-to-order status (from capacity file)
| order_no | item | due | on track? (Y / at risk / late) | notice draft needed? |

## 4. Packed and ready for carrier
| order_no | pack_type | weight_g | label bought? (owner) | handed over? |

## 5. Tracking sweep (every 2nd working day)
| order_no | carrier | tracking | last scan | days since scan | status | flag |

## 6. Exceptions -> customer-notice drafts for CX (owner sends)
| order_no | case | draft (SOP appendix A1/A2/A3) | [OWNER DECISION] needed? |

## 7. Proposed log rows (owner pastes into dispatch-log.csv)
<CSV rows>

## TODO / missing data
```

## TODO / missing data

- Cut-off time for day 0 (proposal 12:00); promised dispatch days (owner decision 3).
- Whether costs are logged incl. or excl. VAT (Finance).
- Who maintains `dispatch-log.csv` day to day (owner or agent-proposed rows pasted by owner).
