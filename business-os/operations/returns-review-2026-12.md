DRAFT — for owner approval. PRE-DRAFT skeleton prepared 2026-10-21; fill 26-31 Dec from Q4 logs.

# Post-peak review Q4 2026: cases, cost per order, carriers, return reasons (OPS-18)

Agent `aw-operations`. Numbers only from `dispatch-log.csv`, `returns-log.csv` and weekly ops files W44-W52.
Counts first; percentages only with 30+ orders (state n).

Sources (fill): `dispatch-log.csv` rows __-__, `returns-log.csv` rows __-__, `ops-weekly-2026-W44.md` ...
`ops-weekly-2026-W52.md`, carrier invoices/receipts (owner).

## 1. Volume and service
| Metric | Q4 2026 | Target | Note |
|---|---|---|---|
| Orders (site / Etsy / market) | | — | excl. test orders |
| On-time dispatch | n/N | >= 95% | |
| Fulfilment errors (wrong / missing / damaged) | n | <= 2%, 0 wrong item | |
| Delivered before 24 Dec when ordered by published date | n/N | 100% | |
| Tracking exceptions acted on before customer asked | n/N | 100% | |

## 2. Cost per order by region vs assumptions
| Region | Orders | Avg weight g | Avg label EUR | Avg packaging EUR | sku-economics shipping_eur / packaging_eur | Gap |

## 3. Carriers: promised vs actual transit
| Carrier + service | Region | Parcels | Median transit (working days) | Slowest | Promise | Inside promise n/N |

## 4. Returns and cases by reason and SKU
| SKU | SIZE_SMALL | SIZE_LARGE | COLOUR_DIFF | NOT_AS_PICTURED | QUALITY | DAMAGED_TRANSIT | WRONG_ITEM | CHANGED_MIND | LATE | Total |
Open cases and refund deadlines into January: | Case | Type | Next deadline | Owner decision needed |

## 5. Proposals for Q1 2027 (owner decides)
- Size guide / PDP (from SIZE_* clusters) -> CRO
- Packaging (from DAMAGED_TRANSIT) -> packaging spec
- Carrier / free-shipping regions (from section 2-3) -> owner, Finance
- Actual cost per order -> Finance staging for `sku-economics.csv` (OPS-19)

## TODO / missing data
- All Q4 data (no real order as of 2026-10-21).
- January withdrawal wave: gifts delivered in late December have deadlines into January; list them in section 4.
