DRAFT — for owner approval. PRE-DRAFT prepared 2026-10-21; fill from Mon 16 Nov, final on Fri 20 Nov.

# Ops freeze check: go / no-go for the Christmas peak (OPS-17)

Agent `aw-operations`. One page for the owner on 20 Nov (publish date of Christmas dates, master plan C3). Each row
is GO only with the evidence named; otherwise NO-GO with the fallback.

Sources (to read on 16 Nov): `christmas-cutoffs-2026.md`, `carrier-rates.md`, `dry-run-plan.md` results,
`delivery-promise-reconciliation.md`, `returns-handling.md`, `owner-inputs-wave2.md`, latest
`capacity-2026-W47.md` (Production, if it exists), `business-os/head-of-ecommerce/gate-tracker.md` (G4, G5).

## Checks

| # | Check | GO when | Evidence (fill) | Status (fill) | Fallback if NO-GO |
|---|---|---|---|---|---|
| 1 | Carrier-backed order-by dates per region (G5) | Every published row has carrier source URL + date; none later than the carrier supports | | | Publish worst-case provisional dates, labelled as estimates; US/CA/AU "not guaranteed" |
| 2 | Carriers' 2026 Christmas last-posting dates | Published by the carrier | | | Keep worst-case dates (Latvijas Pasts published 2025 dates only on 8 Dec) |
| 3 | Dry run done (6 Nov) | T1 + T2 delivered inside promise, undamaged, costs recorded | | | Widen published ranges to measured transit; no faster claims |
| 4 | Dispatch promise decided (MP 3) | Owner answer on file | | | Use 5 working days for all dates |
| 5 | Stock / production calendar | Owner-confirmed shelf stock per gift SKU; main MTO stop 19 Nov garments / 26 Nov accessories + Baltic second stop (LV 4 / EE-LT 3 Dec; 11 / 10 Dec) agreed with Production (W3-11); cardigan Brown/Blue promised MTO (W3-10) | | | In-stock column not published; MTO only, main stop; after-cutoff line "may arrive after Christmas" + gift note (W3-6) |
| 6 | Returns wording | Adviser answered; one wording live on page, Merchant Center, macros | | | Replies follow statutory floor case by case (C12); no "free returns" in December copy |
| 7 | Free-shipping regions (MP 21) | Owner decision on file (proposal W3-13: LV/EE/LT free; EU free >= EUR 150 else 12; US/CA/AU 15; RoW no promise); "Rest of World" handled | | | Owner decides before any Christmas copy names a region |
| 8 | Packaging supplies for peak | Stock of mailers/tissue/cards for [VERIFY expected orders] parcels on hand | | | Plain materials; owner buys |
| 9 | Tracking email | Owner confirmed fulfilled email shows tracking (item 16) | | | Manual tracking message via CX macro 3A |
| 10 | Market stall (if any) | Stall stock ring-fenced; packing hours planned | | | Online first |

## Verdict (fill 20 Nov)

GO / NO-GO: [ ]   Rows NO-GO: [ ]   Owner sign-off: [ ] date [ ]

## TODO / missing data

- Everything in the Evidence column (from 16 Nov).
- Production capacity file for W47 (Production path issue PRD-02).
