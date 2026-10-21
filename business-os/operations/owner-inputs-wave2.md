DRAFT — for owner approval

# Operations: owner inputs, one form (wave 2)

Agent `aw-operations`, 2026-10-21. This form replaces the open rows of `owner-questions-2026-10-21.md` (OPS-01).
Write your answer in the last column; a short phrase is enough. "MP #" = decision number in
`business-os/head-of-ecommerce/owner-decision-pack-2026-10-24.md` / `-2026-10-31.md`. Nothing here asks you to
spend money; any purchase stays your decision.

Wave-2 check (21 Oct): no other department's wave-1 output answers these. Finance, CX, CRO and Production all list
the same inputs as open (e.g. FIN cost-collection request `shipping_eur` waits on MP 8; CX macros wait on MP 13;
Production capacity file not written yet). So OPS-06, OPS-09, OPS-11 and OPS-16 stay BLOCKED until you answer.

Sources: `owner-questions-2026-10-21.md`; `dry-run-plan.md`; `christmas-cutoffs-2026.md`;
`delivery-promise-reconciliation.md`; `returns-handling.md`; HoE owner decision packs 24 Oct and 31 Oct;
`business-os/finance/cost-collection-request-2026-10-21.md`; `business-os/customer-experience/support-macros.md`.

## A. Answer by Sat 24 Oct

| # | Question | Why | MP # | Due | Unblocks (OPS) | Also unblocks | Your answer |
|---|---|---|---|---|---|---|---|
| 1 | Public dispatch promise: keep "2-5 working days"? Different for in-stock vs made-to-order (how many days)? | Every deadline and Christmas date is counted from it | 3 | 24 Oct | OPS-09, OPS-17 (and OPS-02 [VERIFY] marks) | PRD-04, CX LEAD_TIME macro | |
| 2 | Which units are physically on the shelf today (SKU, size, colour, count)? Beanie and turtleneck first. Everything else = made-to-order? | In-stock column of the Christmas table; SOP stage 2 | 4 | 24 Oct | OPS-09, OPS-17 | PRD-11, SEO-04, CRO-23 | |
| 3 | Who packs, and at what time of day? Daily order cut-off (proposal: 12:00 Riga time)? | Daily dispatch rhythm, "order by" maths | — | 24 Oct | OPS-15 | — | |

## B. Answer by Wed 28 Oct

| # | Question | Why | MP # | Due | Unblocks (OPS) | Also unblocks | Your answer |
|---|---|---|---|---|---|---|---|
| 4 | Which carrier(s) did you use to ship (Etsy/Mareshop years included), per region: Latvia, EU, US/CA/AU? Any business account or contract number? | Rates are researched only for carriers you actually use; no new contract asked | 8 | 28 Oct | OPS-06, OPS-09, OPS-11 | FIN-18, PAR-11, CX-10/25, CRO-25, CRE-22, SEO-26 (all via G5) | |
| 5 | Is Etsy (Mareshop) still taking orders this season? | One order intake and one stock pool in the dispatch log | 9 | 28 Oct | OPS-14, OPS-15 | SEO-07 | |

## C. Answer by Fri 30 Oct (dry run is Fri 6 Nov)

| # | Question | Why | MP # | Due | Unblocks (OPS) | Also unblocks | Your answer |
|---|---|---|---|---|---|---|---|
| 6 | Do you have a parcel scale (grams)? | Packed weight decides the price band | — | 30 Oct | OPS-11, OPS-06 | — | |
| 7 | Spare items for 2-4 test parcels (not taken from orders): which items? | Dry-run content (`dry-run-plan.md` T1-T4) | — | 30 Oct | OPS-11 | — | |
| 8 | Recipients: one Latvian address or parcel locker; one EU address (ideally DE); optional EE/LT; optional US. Names can stay with you; I only need the countries | Measures real transit vs the promise | — | 30 Oct | OPS-11, OPS-09 | — | |
| 9 | Budget cap for the test labels (EUR) | You buy the labels; I record the price paid | — | 30 Oct | OPS-11 | — | |
| 10 | Return address for customer returns (studio or other) | Return drafts, packing slip | 13 | 30 Oct | OPS-16 | CX RETURN_START macro | |
| 11 | Who pays return postage for change-of-mind returns? (May stay "pending adviser" per ruling C12; say so) | Must be told to customers before purchase if they pay | 13 | 30 Oct | OPS-16 | FIN returns_allowance | |
| 12 | Packaging: plain or branded? Thank-you card yes/no? Budget cap for the first batch of supplies (spend only after FIN check)? | Supplier quotes in `packaging-spec.md`; packaging_eur per order | 13 | 30 Oct | OPS-11 (pack materials), OPS-15 | FIN cost column `packaging_eur` | |

## D. Answer by Sat 31 Oct - Tue 3 Nov

| # | Question | Why | MP # | Due | Unblocks (OPS) | Also unblocks | Your answer |
|---|---|---|---|---|---|---|---|
| 13 | Free shipping per region: keep Latvia / US / Rest of World as today until rates exist (11 Nov)? Restrict "Rest of World" to the countries with a stated delivery range? Paid express for late Christmas orders yes/no? | Today every country ships free with no range stated (`delivery-promise-reconciliation.md` gaps) | 21 | 31 Oct (final 11 Nov) | OPS-09, OPS-17 | FIN-18 | |
| 14 | Approve the interim delivery line in `delivery-promise-reconciliation.md` s3 for CRO/SEO use (uses only ranges already in Merchant Center) | One promise everywhere until the dry run | C8 | 31 Oct | (OPS-12 follow-up) | CRO PDP line, SEO feed | |
| 15 | Send the adviser pack: `adviser-pack-shipping-returns.md` (this folder) together with CX's `adviser-questions-cx.md` | Returns wording must be consistent before peak (20 Nov) | 22 | 3 Nov | OPS-16 | CX-19, PRD-19 | Sent on: |

## E. Later (no action before these dates)

| # | Question | Why | MP # | Due | Unblocks (OPS) | Your answer |
|---|---|---|---|---|---|---|
| 16 | Screenshot of Commerce > Customer notifications > "Order fulfilled": does it include the tracking number? | SOP stage 6 (tracking sent) | — | 6 Nov | OPS-15 | |
| 17 | Market stall: which one, if any? | Stock ring-fence, packing time in the freeze check | 27 | 10 Nov | OPS-17 | |
| 18 | Approve publication of the carrier-backed Christmas table on 20 Nov (and the provisional one for internal use now) | Banner, gift copy, macros | 33 | 20 Nov | OPS-09, OPS-17 | |

## What I do as soon as an answer lands

| Answer | Agent action (same day) |
|---|---|
| 4 (carriers) | Fill `carrier-rates.md` from that carrier's public price list, dated; mark [VERIFY] where only dynamic pricing exists |
| 6-9 (dry run) | Pre-fill `DRY-01..04` rows in the dispatch-log sheet; daily tracking check 6 Nov onwards |
| 1, 2, 13 | Recompute `christmas-cutoffs-2026.md` |
| 10, 11 | Fill R1/R3 drafts in `returns-handling.md`; tell CX the macro facts changed |

## TODO / missing data

- All answers above (none received as of 2026-10-21).
- Not an owner question, agent keeps checking: carriers' 2026 Christmas last-posting dates; official 2026 Latvian
  holiday calendar incl. transferred working days.
