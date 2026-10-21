DRAFT — for owner approval

# Returns, withdrawals and faulty goods: log format, procedure, reply drafts, CX hand-off

OPS-07, agent `aw-operations`, 2026-10-21. Not legal advice. The owner decides every return acceptance or refusal,
refund, deduction, replacement and reship. The agent classifies, logs, computes dates and drafts.

Sources: `.claude/skills/aw-returns-handling` (own-words summary of Your Europe, PTAC, Directive 2011/83/EU);
`business-os/README.md` s11; `implementation-report.md` "Return-policy redline" and Merchant Center return-policy
row; master plan ruling C12.

## 1. Which rules apply today

| Item | Status |
|---|---|
| Live Shipping & Returns page | Excludes discounted and made-to-order items, excludes shipping from refunds, 5-day defect window. Flagged as likely conflicting with EU rules; legal review not done |
| Merchant Center return policy (Latvia) | 14 days, customer pays return postage, refund in 7 days (pending Google review) |
| Redline | Prepared in `implementation-report.md`, not published |
| Interim rule (master plan C12) | Replies follow the statutory floor case by case; owner approves each. Never cite the 5-day clause, sale or made-to-order exclusions to refuse. No "free returns" / "14 days" wording in pitches until the adviser answers |

Statutory floor summary (adviser confirms): withdrawal 14 calendar days from receipt (last day on a non-working day
moves to the next working day); consumer returns within 14 days of notice; trader refunds all payments incl.
standard outbound delivery within 14 days of notice, may withhold until goods or proof of posting arrive; return
postage paid by the consumer only if disclosed before purchase; faulty goods = legal guarantee, at least 2 years,
trader bears return cost.

## 2. Log: `returns-log.csv` (header in `returns-log-template.csv`)

| Column | Rule |
|---|---|
| case_id | `R-YYYYMMDD-NN` |
| type | `withdrawal` / `exchange` / `faulty` / `damaged_transit` / `wrong_item` / `not_received` / `outside_window` |
| reason_code | SIZE_SMALL, SIZE_LARGE, COLOUR_DIFF, NOT_AS_PICTURED, QUALITY, DAMAGED_TRANSIT, WRONG_ITEM, CHANGED_MIND, LATE |
| delivered_date | From `dispatch-log.csv` / tracking. Unknown = ask the customer, write TODO |
| withdrawal_deadline | delivered_date + 14 calendar days, moved to next working day if needed |
| notice_date | Date the customer's clear statement arrived (email, Etsy message, form) |
| refund_due_by | notice_date + 14 calendar days. Shown in red in the weekly file when within 3 days |
| status | `open` / `awaiting-goods` / `received` / `inspected` / `refund-pending-owner` / `closed` |
| owner_decision | Free text from the owner, with owner_decision_date. Empty = not decided |
| return_postage_paid_by | `customer` / `us` / `TBD` — per the approved policy, never assumed |

Reason codes feed: SIZE_* clusters -> size-guide / PDP proposals (CRO, via owner); QUALITY -> Production (SKU
AMBER); COLOUR_DIFF / NOT_AS_PICTURED -> variant-photo list (Creative); DAMAGED_TRANSIT -> packaging / carrier.

## 3. Procedure

1. Classify (type + reason code). "Not received" goes to the SOP delivery-problems table, not here, until
   confirmed lost.
2. Compute delivered_date, withdrawal_deadline, refund_due_by.
3. Collect: order no., item, reason, photos (faulty/damaged), preferred outcome.
4. Log the row (proposed row in the draft; owner pastes).
5. Draft reply (section 5); put `[OWNER DECISION: ...]` at the top of the draft.
6. On receipt: QC the returned item (aw-qc-and-labelling checks 1-11), note condition and photos; any deduction
   for diminished value is an owner decision and must be justified in writing.
7. Owner issues the refund (same payment method unless agreed otherwise); log refund_date and amount.
8. Weekly: returns by reason and SKU, open cases with deadlines (ops weekly file). Monthly: returns review.

## 4. Hand-off to CX (format)

```
CASE R-YYYYMMDD-NN | order [#] | channel | [type] / [reason_code]
Customer asked: [one line]
Dates: delivered [date] | withdrawal deadline [date] | notice [date] | refund due by [date]
Facts we hold: dispatch log row, tracking [no.], packing photo Y/N, QC result Y/N
[OWNER DECISION]: [question, options]
Draft reply: [below, CX formats in brand voice; owner sends]
```
Same working day as the case arrives.

## 5. Reply drafts (owner sends)

R1 Withdrawal acknowledgement
```
Subject: Your return for order [#]
Hello [name], thank you for letting me know. Your return request for [item] is noted.
Please send the item back by [notice date + 14 days] to: [RETURN ADDRESS — TODO owner decision 13].
[Return postage: per approved policy — OWNER DECISION]. Please include your order number.
Once it reaches us, or you send proof of posting, we refund [amount incl. standard delivery — OWNER DECISION]
to your original payment method, within 14 days of your request.
If the issue was size, I am happy to help you choose the right one: [size advice from the product page].
Kristine, Autumn & Wool
```

R2 Faulty item
```
Subject: Your order [#] — sorry about the fault
Hello [name], I am sorry the [item] is not right. Could you send 2-3 photos showing the problem?
Then I can offer [OWNER DECISION: repair / replacement / refund]. We cover the return postage for faulty items.
Kristine, Autumn & Wool
```

R3 Exchange request (size)
```
Subject: Your order [#] — exchanging for another size
Hello [name], happy to help. The quickest way is to place a new order for [size] and return the original
[per approved policy wording — VERIFY live FAQ before quoting]. Garment measurements for each size are on the
product page: [link]. [OWNER DECISION if any perk, e.g. covering return postage]
Kristine, Autumn & Wool
```

R4 Outside the window: no draft refusal. Route to owner with all dates; owner decides.

Legal threats, chargebacks, PTAC complaints: escalate to the owner the same day; no reply draft without the owner.

## TODO / missing data

- Return address and who pays return postage (owner decision 13, 30 Oct).
- Adviser review of the live policy and the redline (owner sends 3 Nov, decision 22).
- Refund mechanics in Squarespace / Stripe and Etsy (owner action; note for the log only).
- Live FAQ exchange wording (verify before quoting R3).
