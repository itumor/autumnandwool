# Minimum contribution per order: method and decision form (FIN-04) — DRAFT for owner

Decision: owner sets one EUR figure by 2026-11-04 (fallback 2026-11-11, ruling C4). Finance proposes the number only
after 5 priority SKUs are costed and confirmed. Not accounting or investment advice.

## What it is
The least CM2 (contribution before acquisition) an order must leave after paying for its acquisition.
- Max CAC per SKU = CM2 - minimum contribution. This is the bid ceiling for ads and creators.
- A SKU with CM2 below the minimum is not promotable with paid traffic (organic only).

## How Finance will build the proposal (no numbers until inputs exist)
| Step | Input | Source | Status |
|---|---|---|---|
| 1 | Monthly fixed costs (plan, tools, accountant, any pay) | Owner fixed-cost list (`owner-finance-inputs-2026-10-21.md`) | TODO: owner |
| 2 | Realistic orders/month for Q4 | None yet: 0 real orders, ~2 visits/day | Unknown; use scenarios, not a forecast |
| 3 | Overhead share per order = fixed costs / orders per month, for 3 order-volume scenarios (Illustrative volumes owner picks) | Steps 1-2 | TODO |
| 4 | CM2 per priority SKU | `unit_economics.py` `contrib` after costs confirmed | TODO: G1 |
| 5 | Proposal = the overhead share at the owner-chosen volume scenario, floored at a fixed EUR amount, rounded up to whole EUR | Steps 3-4 | TODO |
| 6 | Check: Max CAC = CM2 - minimum for each priority SKU; flag any SKU where Max CAC <= 0 | Step 4-5 | TODO |

## Decision form (owner fills)
| Field | Value |
|---|---|
| Minimum contribution per order (EUR) | __ |
| Basis chosen (volume scenario / fixed floor) | __ |
| Applies from (date) | __ |
| Review date | first review after 4 weeks of real orders |
| Owner initials + date | __ |

## Per-SKU table (filled after decision)
| SKU | CM2 EUR (break-even CAC) | Minimum contribution EUR | Max CAC EUR | Promotable with paid traffic? |
|---|---|---|---|---|
| TODO (5 priority SKUs, GM provisional pick 2026-10-24) | | | | |
