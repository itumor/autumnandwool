---
name: aw-returns-handling
description: Use when an Autumn & Wool customer asks to return, exchange, cancel or complain about a faulty item, when logging or tracking returns, when drafting a returns/withdrawal reply, or when checking how the EU 14-day withdrawal right or 2-year legal guarantee applies (summary only, not legal advice).
---

# Returns, withdrawals and faulty-goods handling

Purpose: handle every return request quickly, consistently and within EU consumer rules, while keeping
decisions with the owner. The agent classifies, logs, computes deadlines and drafts replies. It never approves a
return, issues a refund, or gives a legal conclusion.

## Rules summary (not legal advice; adviser confirms; README s.11)

**A. Withdrawal (change of mind), distance sales, EU / Latvia**
- 14 calendar days from the day the consumer (or their nominee) receives the goods. If the last day is a
  non-working day, it moves to the next working day.
- Consumer notifies by any clear statement (email is fine) or the model withdrawal form; no reason needed.
- Consumer returns goods within 14 days of notifying. Consumer may handle goods only as needed to inspect them
  (like in a shop) and is liable for diminished value beyond that.
- Trader refunds all payments **including standard outbound delivery** within 14 days of being notified; may
  withhold until goods or proof of sending arrive; same payment method unless agreed otherwise. If customer chose
  a pricier delivery option, only the standard cost is refunded.
- Return postage: consumer pays only if told so before purchase; otherwise trader pays.
- Discounted items: still covered. Exception = goods made to the consumer's specifications or clearly
  personalised; a standard design knitted after the order is generally NOT an exception.
- If the trader did not give withdrawal information, the period extends by up to 12 months.

**B. Faulty / not as described (legal guarantee)**
- At least 2 years from delivery. Defects showing within 1 year are presumed to have existed at delivery
  (seller must prove otherwise). Remedies: repair or replacement free of charge; if impossible or unreasonable
  delay, price reduction or refund. Trader bears return cost for faulty goods.
- The live policy's "report defects within 5 days" clause may conflict with this: never quote it to refuse a
  claim; flag to owner/adviser.

**Current live policy conflicts (do not quote as authority; flag):** excludes discounted and made-to-order items,
excludes shipping from refunds, 5-day defect window. Redline proposal exists in `implementation-report.md`.
Until the owner publishes revised terms, replies follow the statutory floor above, approved case by case.

## Procedure

1. **Classify:** Withdrawal (change of mind / size) | Exchange request | Faulty / damaged | Wrong item | Late /
   not received (aw-fulfilment-sop) | Outside window.
2. **Compute dates:** delivery date (dispatch log / tracking), withdrawal deadline, refund-due date (notice
   date + 14 days). Unknown delivery date = ask customer, note `TODO`.
3. **Collect:** order no., item, reason, photos (faulty), preferred outcome. Size issue? Offer size advice for a
   new order (aw-support-replies). Exchange flow per live FAQ: customer places new order for the right item and
   returns the original (verify page wording before quoting).
4. **Log** (propose `business-os/returns-log.csv`):
   `case_id,date_opened,order_no,channel,sku,size,colour,type,reason_code,delivered_date,withdrawal_deadline,notice_date,refund_due_by,photos(Y/N),status(open/awaiting-goods/received/inspected/refund-pending-owner/closed),owner_decision,refund_amount,return_postage_paid_by,notes`
   Reason codes: SIZE_SMALL, SIZE_LARGE, COLOUR_DIFF, NOT_AS_PICTURED, QUALITY, DAMAGED_TRANSIT, WRONG_ITEM,
   CHANGED_MIND, LATE.
5. **Draft reply** using templates below + aw-brand-voice. Put the decision request to the owner at the top of
   the draft file.
6. **On receipt:** QC the returned item (aw-qc-and-labelling), note condition; owner decides any deduction
   for diminished value (must be justified), then refund.
7. **Weekly:** return rate by SKU and reason; SIZE_* clusters -> propose size-guide/PDP fixes; QUALITY clusters
   -> aw-production-capacity (SKU AMBER).

## Draft templates (owner sends)

Withdrawal acknowledgement:
```
Subject: Your return for order [#]
Hello [name], thank you for letting us know. Your return request for [item] is noted.
Please send the item back by [notice date + 14 days] to: [return address TODO]. [Return postage: who pays — per
approved policy]. Please include your order number. Once it reaches us (or you send proof of posting) we refund
[amount incl. standard delivery] to your original payment method within 14 days of your request.
If the issue was size, I am happy to help you choose the right one: [size advice].
Kristine, Autumn & Wool
```
Faulty item: apologise, ask for 2-3 photos, offer repair / replacement / refund options for owner to choose,
state we cover return postage. Outside window: do not refuse in the draft; route to owner with dates.

## Guardrails

- Never approve, refuse, or promise a refund/return outcome without owner sign-off; drafts say
  "[OWNER DECISION]" where the decision goes.
- Never cite the live 5-day defect clause, sale or made-to-order exclusions to deny statutory rights.
- No legal conclusions: write "may", "adviser to confirm". Legal threats, chargebacks, PTAC complaints = escalate
  to owner immediately.

## Sources

- Your Europe, "Returns" https://europa.eu/youreurope/citizens/consumers/shopping/returns/index_en.htm and
  "Guarantees" https://europa.eu/youreurope/citizens/consumers/shopping/guarantees-returns/index_en.htm — EU
  site, own-words summary (period, exceptions, return cost, 2-year guarantee, 1-year presumption).
- PTAC "Right of withdrawal" https://www.ptac.gov.lv/en/right-withdrawal and "Purchases by electronic means"
  https://www.ptac.gov.lv/en/purchases-electronic-means — Latvian authority, summarized (14 days from receipt,
  return within 14 days, refund within 14 days, 1-year extension if not informed).
- Directive 2011/83/EU Arts. 9-14 https://eur-lex.europa.eu/eli/dir/2011/83/oj — refund of standard delivery,
  withholding until goods returned (from model knowledge of the text; verify).
- Existing A&W redline: `implementation-report.md` "Return-policy redline". No agent skill for EU returns found;
  winner = own summary of official sources.
