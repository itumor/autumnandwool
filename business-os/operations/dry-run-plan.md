DRAFT — for owner approval

# Dry run: test parcels, Fri 6 Nov 2026

OPS-10 (plan), agent `aw-operations`, 2026-10-21. Execution = OPS-11 (owner). Purpose: before the first real
order, run the whole SOP once by hand and replace guesses with measured weight, cost and transit time.

Sources: `plans/2026-2027/operations.md` s2 (6 Nov dry run); master plan C8 (no new delivery range before dry-run
parcels); `sop-order-to-delivery.md`, `packaging-spec.md`, `carrier-rates.md` (this folder).

## Scope

| Parcel | Destination | Content | Why |
|---|---|---|---|
| T1 | Latvian address (owner picks: friend/family, or a parcel locker) | Heaviest common item, e.g. long shawl cardigan in P3 (or P2 sweater if no spare unit) | Measures domestic cost and transit; tests locker size |
| T2 | One EU-18 address (owner picks a willing recipient, ideally Germany or another large market) | P2 sweater or P1 beanie | Measures EU cost and transit vs the 5-10 day promise |
| T3 (optional) | Estonia or Lithuania | P1 beanie | Baltic transit; Baltics missing from Merchant Center list |
| T4 (optional, owner decides) | US address | P1 beanie | Customs paperwork + real US transit; tests whether the 7-20 day promise holds |

Items: owner's own stock or samples; recipients send them back or keep them (owner decides). No customer is
involved. No live order is created by the agent.

## Steps (owner does the physical steps; agent prepares sheets)

1. Agent: pre-fill dispatch-log rows with `channel=dryrun`, order_no `DRY-01..04`, today's promised_dispatch_by.
2. Owner: run QC checklist on each item (time it: minutes).
3. Owner: pack per `packaging-spec.md`; time it (minutes); folded size (cm); packed weight (g); photos.
4. Owner: buy labels with the candidate carrier(s) (decision 8); record service, price paid, incl./excl. VAT,
   receipt.
5. Owner: hand over; record acceptance time.
6. Agent: tracking check every working day until delivered (dry run only; normal cadence is 2 days).
7. Recipient: confirms delivered date/time and condition (photo of parcel on arrival).
8. Agent: write results into `carrier-rates.md` (actual rows, marked "dry run") and `packaging-spec.md` s5;
   compare transit with the promise; propose changes to the delivery ranges (C8) and to the cutoff table.

Optional, owner only: if CRO's PayPal / checkout test produces a real test order, mark it fulfilled with T1's
tracking to see whether the Squarespace shipping-confirmation email shows tracking. The agent does not do this.

## Results sheet

| Test | Carrier + service | Pack | Weight g | Size cm | Label EUR | Pack materials EUR | QC min | Pack min | Handed over | Delivered | Transit working days | Promise | Inside promise? | Condition | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T1 | | | | | | | | | | | | LV 2-5 | | | |
| T2 | | | | | | | | | | | | EU 5-10 | | | |
| T3 | | | | | | | | | | | | none | | | |
| T4 | | | | | | | | | | | | 7-20 | | | |

## Wave 3 prefill on ASSUMPTIONS (ready to run once the owner confirms)

**ASSUMPTION** values from `assumptions-wave3.md`; the owner replaces any of them before 6 Nov. Execution (buying
labels, packing, handing over) stays with the owner: OPS-11 is BLOCKED until then.

| Test | Assumed carrier + service (A-ID) | Locker size | Expected label EUR (list price) | Expected pack materials EUR (A-OPS-10) | Expected weight (A-OPS-11) | Promise to test (A-OPS-14) | Christmas row it validates |
|---|---|---|---|---|---|---|---|
| T1 LV | Parcel locker-to-locker (A-OPS-01) | M (cardigan) or S | 3.90 (M) / 2.90 (S) Smartposti; Omniva/LP via calculator | 1.50 | 0.8-1.2 kg | 1-3 wd | LV, A-OPS-16 |
| T2 EU (DE) | Locker/pickup road service (A-OPS-04) | S | 21.90 (S) / 13.99 (XS beanie) | 1.50 | 0.5-0.8 kg | 3-8 wd | EU, A-OPS-18 |
| T3 EE or LT (optional) | Parcel locker (A-OPS-03) | XS | 4.79 | 1.50 | 0.15-0.25 kg | 2-4 wd | EE/LT, A-OPS-17 |
| T4 US (optional) | Postal tracked via mans.pasts.lv (A-OPS-06) | — | about 22-28 + provisional duty + fee (A-OPS-08) | 1.50 | 0.15-0.25 kg | 7-20 wd | US, A-OPS-19; tests duty charge at label purchase |

Budget the owner can approve against (ASSUMPTION): T1 + T2 about EUR 29; with T3 about EUR 35; with T4 about
EUR 60-70 incl. duty on a low declared value. Proposed dispatch-log rows (agent pre-fills on the day, `channel=dryrun`):
`DRY-01..04`, order_date Fri 6 Nov, promised_dispatch_by Fri 6 Nov (same-day test), carrier per table above.

Timing: hand over Fri 6 Nov before the locker's last pickup; agent checks tracking every working day; results by
Fri 13 Nov (LV, EE/LT, EU) feed the carrier-backed Christmas table on 14 Nov; US by about 4 Dec (too late for 14 Nov;
the US row stays "not guaranteed").

## Go / no-go for the first real order

Go when: T1 and T2 delivered inside the promise, undamaged; label + packaging cost recorded; SOP steps done without
improvisation (any improvised step becomes an SOP edit). Otherwise: propose range or packaging changes to the owner.

## TODO / missing data

- Carrier(s) to test (decision 8) and recipients/addresses (owner).
- Packaging supplies bought (decision 13) — if not, use plain materials on hand and note it.
- Spare units to send (owner; not taken from orders).
- Budget for test labels (owner).
