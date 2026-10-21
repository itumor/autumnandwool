# Gift budget worksheet (PAR-11 prep, also PAR-15) - DRAFT

Status: DRAFT, prepared 2026-10-21. Every EUR cell is TODO: 0 of 82 SKUs are costed in `sku-economics.csv`, no
capacity file exists, no carrier rate is filled and the minimum contribution is not set. No number here is invented.
Finish when the inputs in section 4 arrive (target 15 Nov).

## 1. Inputs and where they come from

| Input | Source (other department) | State 2026-10-21 |
|---|---|---|
| materials_labour_eur per gift SKU | `business-os/sku-economics.csv` via Production (master #5) | Empty |
| packaging_eur | `business-os/operations/packaging-spec.md` pack types: beanie = P1, hat & scarf set = P3 | Pack types set, quotes TODO |
| shipping_eur to creator country | `business-os/operations/carrier-rates.md` regions LV / BALT / EU-18 | Template only, rates TODO |
| CM2 = break-even CAC per SKU | `python3 business-os/unit_economics.py` (`contrib`) after costs | 0 costed |
| Minimum contribution per order | `business-os/finance/min-contribution-method.md` (owner decision, 4 Nov) | Method only |
| Gift SKUs allowed | GM rule (decision pack 31 Oct, #12): priority 5 only, G8-cleared; capacity GREEN/AMBER | Priority 5 provisional (`head-of-ecommerce/priority-5-sku-proposal-2026-10-21.md`) |
| Number of gifts | Owner D2 (form O6) | Open |

## 2. Formulas

```
gift_cost      = materials_labour_eur + packaging_eur(pack type) + shipping_eur(creator region)
BE_CAC         = CM2 of the gifted SKU (unit_economics.py contrib)
max_CAC        = CM2 - minimum contribution            (Finance method, step 6)
programme_cap  = approved_gifts x gift_cost
go rule        = gift_cost <= max_CAC x expected orders per gift   (we have no evidence for expected orders,
                 so plan with 1: each gift must pay back with at least one attributed order)
stop rule      = 60 days after shipping: total creator cost / attributed orders > BE_CAC -> stop or change deal
```

Note: a single gift costing more than max_CAC needs two or more attributed orders to pay back. The owner should see
that before approving it.

## 3. Per-SKU table (gift candidates in the priority 5 only)

Prices from the priority-5 proposal; ex VAT = price / 1.21.

| SKU | Price incl. VAT | Ex VAT | Pack | Materials+labour | Packaging | Ship LV | Ship EU-18 | Gift cost LV | Gift cost EU | CM2 (BE_CAC) | Min contribution | Max CAC | Gift fits? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rib-Knit Beanie, unisex | EUR 45.00 | EUR 37.19 | P1 | TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO |
| Merino Wool Hat & Scarf Set (Black only until photos) | EUR 110.00 | EUR 90.91 | P3 | TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO | TODO |

Dropped from wave-1 candidates: lightweight turtleneck (alternate only, not in the priority 5; GM rule #12). Re-add
if the GM swaps it in on 4 Nov.

## 4. Programme cap (owner fills O6/O7 in `owner-inputs-wave2.md`)

| Line | Value |
|---|---|
| Approved gifts (D2) | __ (proposal 5-8) |
| Mix (beanie / hat set) | __ / __ |
| Programme cap EUR | = sum of gift costs = TODO |
| Max per single gift EUR | __ (proposal: <= max CAC of that SKU) |
| Owner initials + date | __ |

## 5. To finish (agent)
1. Read costs once Production/Finance fill `sku-economics.csv` and run `unit_economics.py`.
2. Fill section 3 per region, flag any gift where gift cost > max CAC.
3. Put the result in the owner form (O7) and the gift spec (`creator-brief-gifting.md` Part B).
