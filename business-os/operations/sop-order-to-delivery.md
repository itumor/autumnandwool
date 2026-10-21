DRAFT — for owner approval

# SOP: order to delivery (Autumn & Wool, AUTUMN AND WOOL SIA, Riga)

Version 0.1, 2026-10-21, agent `aw-operations` (OPS-02). Run by hand first: there are zero real direct orders, so
nothing below is automated. Humans touch orders, labels, parcels and customers. The agent drafts checklists, logs
and customer notices.

Sources: `business-os/README.md` s6, s9, s11; `.claude/skills/aw-fulfilment-sop`, `aw-returns-handling`,
`aw-qc-and-labelling`, `aw-production-capacity`; `implementation-report.md` (shipping recheck 18 Oct, FAQ and
Merchant Center rows); `plans/2026-2027/operations.md`; `plans/2026-2027/master-plan.md` (rulings C3, C8, C12).

## 0. Facts this SOP depends on (each needs owner confirmation)

| Fact | Current value | Source | Status |
|---|---|---|---|
| Public dispatch promise | "Dispatch 2-5 working days" (live FAQ, updated per implementation report) | `implementation-report.md` FAQ row; brand-voice skill | [VERIFY] owner decision 3 (due 24 Oct) |
| Delivery ranges (public) | Latvia 2-5 transit; 18 EU countries 5-10; US/CA/AU 7-20 (business days, after handling) | Merchant Center shipping policy (pending Google review) | Not carrier-verified. Interim ceiling only (ruling C8) |
| Shipping price | EUR 0 for Latvia, United States, Rest of World in Squarespace | Shipping recheck 18 Oct | Only Latvia checkout-tested |
| Carriers | None chosen | — | TODO owner decision 8 (due 28 Oct) |
| Return address | None on file | — | TODO owner decision 13 (due 30 Oct) |
| Who packs | Owner (assumed: one person) | Master plan C11 | [VERIFY] |
| Order channels | Squarespace Orders; Etsy (Mareshop) if still selling | README s2 | Etsy status = owner decision 9 |
| Payment | Stripe (Squarespace Payments). PayPal not connected | README s2 | — |
| Contact email | autumnandwool@gmail.com | aw-fulfilment-sop skill | — |
| Physical stock | Unconfirmed. Turtleneck 360 / beanie 220 look like made-to-order placeholders | `ai-team.md`, production plan | Treat every unit as made-to-order until the owner confirms shelf stock |

## 1. Daily rhythm

| When | Who | What |
|---|---|---|
| Every working day, fixed time (proposal 09:00 Riga) | Owner | Open Squarespace Orders and Etsy orders. Paste new orders into `dispatch-log` (one row per order line). Agent prepares the day's checklist from the log (`dispatch-checklist-template.md`) |
| Same day | Owner | Pack and hand over everything due; record tracking |
| Every 2 working days | Agent drafts, owner checks | Tracking sweep on all undelivered parcels (section 6) |
| Monday | Agent | Weekly ops KPI file (`ops-weekly-template.md`) |

Order cut-off for "same-day counts as day 0": proposal 12:00 Riga time [VERIFY owner]. Orders after cut-off count
from the next working day.

## 2. Working-day rules (deadline calculations)

- Working day = Monday-Friday, excluding Latvian public holidays. Q4 2026 holidays to exclude: Wed 18 Nov,
  Thu 24 Dec, Fri 25 Dec, Sat 26 Dec, Thu 31 Dec; 1 Jan 2027. [VERIFY against the Cabinet's 2026 calendar,
  including any transferred working days.]
- `promised_dispatch_by` = order date (day 0, or next working day if after cut-off) + promised dispatch days in
  working days (default 5 until owner decision 3).
- Withdrawal deadline (for the returns log) = delivered date + 14 calendar days; if the last day is a non-working
  day it moves to the next working day (aw-returns-handling summary; adviser confirms).
- Refund-due date = date of the customer's withdrawal notice + 14 calendar days.

## 3. Stages

| # | Stage | Do | Control / exception | Record |
|---|---|---|---|---|
| 1 | Order in | Check payment = paid (Stripe in Squarespace; Etsy marked paid). Check product, size, colour against the order. Check address is complete: flat/apartment no., postcode, phone (needed for parcel lockers and couriers), country inside a shipping zone | Order no. logged once (no duplicates, no misses: count Squarespace + Etsy orders = new log rows). Suspicious order (billing/shipping country mismatch, many units, rushed changes) = owner review before any work. Incomplete address = draft customer question the same day; never guess | `dispatch-log`: order_no, channel, order_date, promised_dispatch_by, sku, size, colour |
| 2 | Stock or make | Finished unit on the shelf and owner-confirmed? Tag it with the order no. Otherwise add to Production's made-to-order queue with due date = promised_dispatch_by minus 1 working day (QC + pack buffer) | Production's weekly `capacity-YYYY-Www.md` shows it will miss the date = draft a delay notice the same day (Appendix A1). Options in the draft: wait / switch item / cancel with full refund. Refund = owner decision | stock_or_mto |
| 3 | QC | Run the 11-point aw-qc-and-labelling checklist on the actual unit (right item, measurements, symmetry, knit surface, seams, finish, shade, pilling, trims, fibre + care label, paperwork) | Critical or major defect = do not pack; rework or remake and re-check stage 2 dates | qc_pass (Y/N); defects to `qc-log.csv` if owner approves it (Production) |
| 4 | Pack | Per `packaging-spec.md`: fold in tissue, care card, packing slip with order no. and return instructions, mailer/box. Weigh. Photo of the item in the open pack and of the sealed, labelled parcel | Pack size matches item; weight recorded (drives carrier cost); photo kept for damage claims | packed_date, weight_g, pack_type |
| 5 | Label + dispatch | Buy the label for the service the customer paid for (today: free standard). Hand to carrier. Keep the acceptance receipt / scan | Owner marks the order fulfilled in Squarespace with carrier + tracking number (human action). Etsy: mark dispatched with tracking. Store stock update = human action | dispatched_date, carrier, service, tracking, label_cost_eur |
| 6 | Tracking | Confirm the customer received the Squarespace shipping-confirmation email with tracking [VERIFY setting: Commerce > Customer notifications]. Sweep every 2 working days | Exception (section 6) = act before the customer asks; draft notice the same day | issue |
| 7 | Delivered | Record delivered date from carrier tracking | Starts the 14-day withdrawal clock (returns log). Triggers the review-request timing (CX) | delivered_date |
| 8 | Close-out | Record actual label cost + packaging cost per order. Compare with `sku-economics.csv` shipping_eur / packaging_eur (README s9 illustration: EUR 12 + 3) | Never edit `sku-economics.csv`: actuals go to the weekly ops file as proposals for Finance/owner | packaging_cost_eur, on_time |

## 4. Customs (non-EU: US, CA, AU; UK, NO, CH if ever enabled)

Not legal or tax advice. Duties and import VAT may be charged to the recipient. No statement to customers about
duties until the accountant and the chosen carrier confirm (TODO owner/accountant). Commercial invoice / customs
declaration (CN22/CN23 or carrier equivalent) with HS code for knitted wool garments: TODO accountant/carrier to
confirm codes per product type. Note: Latvijas Pasts cited US customs policy changes as a factor in its
international parcel business (LSM, 23 Apr 2026); check the current US import rules for low-value parcels with the
carrier before the first US order [VERIFY].

## 5. Delivery problems

| Case | Do (agent drafts, owner acts) | Decision |
|---|---|---|
| Stuck: no scan for more than 5 working days, or past the carrier's stated window | Open a carrier trace; draft customer update (A2) | Owner: reship vs refund once carrier confirms loss |
| Lost | Carrier claim with acceptance receipt + packing photo. Risk of loss in transit generally sits with the trader until the consumer receives the goods (general EU rule; adviser confirms wording) | Owner: reship or refund |
| Failed delivery / at pick-up point | Draft customer note with pick-up deadline from tracking | — |
| Returned to sender | Contact customer to confirm address before re-sending | Owner: who pays re-send |
| Damaged on arrival | Draft request for 2-3 photos of parcel and item (A3); file carrier claim within the carrier's deadline [VERIFY per carrier]; treat as faulty goods (legal guarantee), not withdrawal | Owner: repair / replace / refund |
| Wrong item sent | Apologise; send correct item first if stock allows; prepaid return of the wrong one | Owner approves reship + label |
| Address error found before dispatch | Hold parcel; ask customer | — |

## 6. Tracking sweep (every 2 working days)

For each log row with `dispatched_date` set and `delivered_date` empty: open tracking, note last scan date and
status. Flag: no scan > 5 working days; "returned to sender"; "delivery failed"; "held by customs"; past the
public delivery range. Each flag gets an `issue` note and a customer-notice draft for CX the same day.

## 7. Hand-offs

| To | What | When |
|---|---|---|
| CX agent | Order no., case type, dates (dispatch, delivered, withdrawal deadline), draft notice text | Same working day |
| Production | Made-to-order queue rows, defect notes, return reasons QUALITY / SIZE_* | Same day; weekly cluster summary |
| Finance | Actual label + packaging cost per order and per region | Weekly ops file |
| Owner | Every refund, reship, replacement, compensation, return acceptance | Marked `[OWNER DECISION]` at the top of the draft |

## Appendix A: customer-notice drafts (owner sends; CX formats)

Calm, specific, no promises beyond carrier-stated transit (aw-brand-voice).

A1 Delay before dispatch
```
Subject: Your order [#] — new dispatch date
Hello [name], your [item, colour, size] is taking longer to finish than planned. I now expect to send it on
[new date, from Production's capacity file]. If that works for you, there is nothing to do. If you prefer, I can
suggest a similar piece that is ready now, or cancel the order with a full refund. [OWNER DECISION on options]
Kristine, Autumn & Wool
```

A2 Tracking exception
```
Subject: Your order [#] — delivery update
Hello [name], your parcel left Riga on [dispatch date] with [carrier], tracking [number]. The tracking has not
updated since [last scan date]. I have asked [carrier] to check and will write again by [date, 2 working days].
Kristine, Autumn & Wool
```

A3 Damaged on arrival
```
Subject: Your order [#] — sorry it arrived damaged
Hello [name], I am sorry. Could you send 2-3 photos of the parcel and the item? Then I will suggest how to put it
right [OWNER DECISION: repair / replacement / refund]. We cover any return postage for damaged items.
Kristine, Autumn & Wool
```

## TODO / missing data

- Owner decisions 3 (dispatch promise), 8 (carriers), 13 (return address, return postage, packaging), 21 (free
  shipping per region), 9 (Etsy active?).
- Whether the Squarespace shipping-confirmation email includes tracking (check Commerce > Customer notifications).
- Order cut-off time; who packs; parcel-locker option wanted?
- HS codes and customs paperwork (accountant + carrier).
- Carrier claim deadlines per carrier.
- 2026 Latvian holiday calendar and transferred working days.
