# Feed availability proposal on assumed stock (SEO-04), wave 3, 2026-10-21 — DRAFT for owner

Author: aw-seo-marketplace. **ASSUMPTION MODE.** Inputs: stock rule A-PRD-12, shared pools A-PRD-13 (72 assumed
physical units + 2 made-to-order SKUs, `knitwear-making/stock-duplicate-sheet.md`), MTO lead time A-PRD-14 / A-GM-03,
trim rule A-GM-24, handling-time approach A-SEO-09 (`seo-marketplace/assumptions-wave3.md`). None of these is an
owner stock count. The live `autumnandwool-google-feed.tsv` is unchanged; nothing was uploaded. Row-level diff:
[2026-10-21-feed-availability-diff-wave3.csv](2026-10-21-feed-availability-diff-wave3.csv).

## Result in one line
On the assumed stock, **no row becomes `out_of_stock`**. The 36 turtleneck rows are made to order with a 10-working-day
lead time, which is longer than the account handling time (2–5 business days). They stay `in_stock` and get a row-level
handling time of 5–10 days. The other 62 rows need no change.

## Row by row (98 rows)
| Rows (feed lines) | Product | 17 Oct listed → assumed (A-PRD-12/13) | Availability | Handling time | Why |
|---|---|---|---|---|---|
| 53–88 (36) | Merino Turtleneck, lightweight, 12 colours × XS/S/M | 360 → 0 on shelf, MTO | `in_stock` (unchanged) | **add `min_handling_time` 5, `max_handling_time` 10** | MTO garment 10 wd (A-PRD-14) is longer than the account's 5-day maximum. Without the row value, Google would show a delivery estimate we can't meet |
| 11–21 (11) | Rib-Knit Beanie, 11 colours | 220 → 0 on shelf, MTO | `in_stock` (unchanged) | account level (2–5) | MTO beanie 5 wd (A-PRD-14) fits inside the account's 5-day maximum |
| 30–41 (12) | Lambswool Raglan Crew A/B + Classic Lambswool Crew | 16 / 8 / 16 → pool D1 8 + 8 | `in_stock` | account | ≥ 1 assumed unit per size row on average. A pool of 8 over 8 rows can still leave one size at 0: `[VERIFY]` per size in the owner count |
| 22–29 (8) | Pure Wool Side-Slit A/B | 16 / 16 → pool D3 8 | `in_stock` | account | same caveat as above |
| 89–96 (8) | Stand-Collar Beige / Blue | 16 / 12 → pool D4 8 | `in_stock` | account | same caveat |
| 44–51 (8) | Long Shawl Cardigan, Long Wool Cardigan Shawl Collar | 16 / 12 → 8 / 6 | `in_stock` | account | 50% rule still ≥ 1 per size |
| 3–5 (3) | Merino Raglan Cardigan Black / Brown / Blue | 6 → 2 per colour | `in_stock` | account | See conflict C-1 below |
| 8–10 (3) | Hat & Scarf Set Black / Gray / Brown | 6 → 2 per colour | `in_stock` | account | Gray, Brown are RED for promotion (no photo) but in stock; trim follows A-GM-24, not stock |
| 2, 6, 7, 42, 43, 52, 97, 98, 99 (9) | single-SKU garments + Dusty Pink S/M, L/XL | 1–6 as listed | `in_stock` | account | Listed 1–8 = real (A-PRD-12). Stock-1 items go to 0 on one sale; the generator patch (SEO-03) handles that on the next run |

Totals: 98 rows; 0 → `out_of_stock`; 0 → `backorder`; 36 rows get a handling-time pair; 62 unchanged.

## Conditional trims (ruling C7, A-GM-24), not applied by this proposal
| Date | If not photographed and bound | Rows removed from the proposal feed |
|---|---|---|
| 31 Oct | Turtleneck, 11 of 12 colours | 33 (the handling-time rows above shrink to 3) |
| 14 Nov | Beanie 10 colours, Hat & Scarf Set Gray + Brown, Cardigan Blue | 13 |
Per-colour ticks: `2026-10-21-variant-bind-check.csv` (SEO-24).

## Conflicts and checks for the owner
- **C-1 Cardigan Brown/Blue:** the wave 2 CRO fix list says the PDP calls them "made to order"; Production's register
  assumes 2 per colour on the shelf. I followed the shared register (`in_stock`, account handling). If they are MTO, they
  get the turtleneck handling pair (5/10). The owner's count decides.
- **"13 out of stock"** (handbook §5.4) still can't be reproduced (feed QA F2). The assumed stock rule does not create
  any 0-stock row.
- Why not `backorder`: Google requires `availability_date` for it. A date written into a hand-run feed goes stale
  (A-SEO-09). The handling-time route is my reading of Google's help pages, not a quoted rule: check Diagnostics 24–72 h
  after the upload.

## How it gets applied (owner, one pass with SEO-24 and SEO-25)
1. Approve the generator patch (owner-inputs-wave2 row 4), with two extra optional columns `min_handling_time`,
   `max_handling_time` filled for MTO products only.
2. Replace assumed stock with the owner's physical count (decision 4). Rows at 0 then go `out_of_stock`.
3. Regenerate, I QA the TSV, the owner uploads (feed QA re-upload checklist).

ASSUMPTION: A-PRD-12, A-PRD-13, A-PRD-14, A-GM-03, A-GM-24, A-SEO-09. Not facts. DRAFT, nothing applied.
