DRAFT — for owner approval

# Weekly ops KPI file (template)

OPS-13, agent `aw-operations`, 2026-10-21. Copy every Monday to `business-os/operations/ops-weekly-YYYY-Www.md`.
Numbers come only from `dispatch-log.csv` and `returns-log.csv`; the agent never edits `kpi-weekly.csv` — it
proposes the `on_time_dispatch_pct` and `shipping_packaging_payment_eur` values for the owner/Finance to append
(baseline row week_start 2026-10-19 per ruling C16; test orders #00003/#00004 excluded).

Sources: `.claude/skills/aw-fulfilment-sop` (KPI definitions); `business-os/README.md` s9; ops plan KPI table.

```
DRAFT — for owner approval
# Ops weekly YYYY-Www (Mon DD Mon - Sun DD Mon)
Sources: dispatch-log.csv (rows N-M), returns-log.csv, capacity-YYYY-Www.md, carrier tracking pages (dates)

## 1. KPIs (counts first; % only from 30+ orders)
| KPI | This week | Q4 to date | Target | Note |
| Orders received (site / Etsy / market) | | | none (no baseline) | |
| Orders dispatched | | | | |
| On-time dispatch (dispatched by promised date / dispatched) | n/N | | >= 95% | |
| Fulfilment errors (wrong / missing / damaged) | n | | <= 2%, 0 wrong item | |
| Fulfilment cost per order (label + packaging) EUR | | | compare sku-economics shipping_eur + packaging_eur | |
| Tracking sent same day | n/N | | 100% | |
| Tracking exceptions acted on before customer asked | n/N | | 100% | |
| Returns / withdrawals opened | n | | 100% logged | |
| Refunds due within 3 days (owner) | list | | 0 missed | |

## 2. Cost per order by region
| Region | Orders | Avg weight g | Avg label EUR | Avg packaging EUR | vs promise (free) |

## 3. Returns by reason and SKU
| SKU | SIZE_SMALL | SIZE_LARGE | COLOUR_DIFF | NOT_AS_PICTURED | QUALITY | DAMAGED_TRANSIT | WRONG_ITEM | CHANGED_MIND | LATE |

## 4. Open cases with deadlines
| Case / order | Type | Next deadline | Owner decision needed |

## 5. Proposed kpi-weekly.csv values (owner appends)
week_start=YYYY-MM-DD, on_time_dispatch_pct=__, shipping_packaging_payment_eur=__ (payment fees from Finance)

## 6. Proposals (size guide, packaging, carrier)

## TODO / missing data
```

## TODO / missing data

- First real order (until then the weekly file reports readiness status only: open owner decisions and OPS task
  status).
- Payment fee per order (Finance) to complete `shipping_packaging_payment_eur`.
