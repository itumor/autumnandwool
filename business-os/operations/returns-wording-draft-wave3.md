DRAFT — for owner approval

# Shipping & Returns wording draft on ASSUMPTIONS (OPS-16 prep, wave 3)

Agent `aw-operations`, 2026-10-21. **ASSUMPTION: change-of-mind return postage paid by the customer (A-OPS-22),
faulty/wrong at our cost, return address = owner's Riga studio (A-OPS-21, not filled), dispatch in-stock 2-5 working days,
made-to-order garments 10 / accessories 5 working days (A-OPS-12, GM ruling W3-1), refund within 14 days incl. standard outbound delivery (A-OPS-23).** Register:
`assumptions-wave3.md`. Not legal advice. Nothing here is published: the live page is frozen, the adviser has not
answered (decision 22), ruling C12 applies (no "14 days" / "free returns" in pitches until the adviser answers).
This draft is meant to travel **with** `adviser-pack-shipping-returns.md` so the adviser reviews concrete text.

Sources: `.claude/skills/aw-returns-handling` (statutory floor summary of Your Europe, PTAC, Directive 2011/83/EU);
`returns-handling.md`; `implementation-report.md` return-policy redline; `delivery-promise-reconciliation.md`;
brand voice (calm, specific; no "eco", no "free returns").

## [OWNER DECISION] before use

1. Return postage for change of mind: customer (as Merchant Center already says) **or** us. `__`
2. Return address: `__`
3. Free shipping regions (decision 21) and the Rest of World restriction (A-OPS-07). Proposed (GM ruling W3-13):
   LV/EE/LT free; EU-other free from EUR 150, else EUR 12; US/CA/AU flat EUR 15; Rest of World no promise. `__`
4. Send this text with the adviser pack on 3 Nov. `Sent on: __`

## A. Proposed Shipping & Returns page text

```
Shipping

Every piece is checked and packed in our Riga studio. Items in stock are dispatched within 2 working days.
Made-to-order pieces are dispatched within 10 working days (beanies and hat sets within 5).
[ASSUMPTION A-OPS-12 / GM ruling W3-1 — owner decision 3] You get a tracking number by email when your
parcel leaves us.

Delivery after dispatch (estimates from our carriers, not guarantees):
- Latvia: 1-3 working days
- Estonia and Lithuania: 2-4 working days
- Other EU countries: 3-8 working days
- United States, Canada, Australia: 7-20 working days
Shipping cost: free to Latvia, Estonia and Lithuania. Other EU countries: free from EUR 150, otherwise EUR 12.
United States, Canada, Australia: EUR 15. [ASSUMPTION GM ruling W3-13 — OWNER DECISION 21: list of countries we
ship to; other countries not offered]

Orders to the United States, Canada and Australia may be charged import duties or taxes on arrival.
[ADVISER/ACCOUNTANT: confirm wording; for US parcels we currently assume we pre-pay duty at label purchase (A-OPS-08) —
if so, say "duties for US orders are included".]

Returns (change of mind)

You can withdraw from your purchase within 14 days of receiving your order, without giving a reason. Tell us by
email at autumnandwool@gmail.com (order number and item), or use the withdrawal form below. Then send the item
back within 14 days of telling us, to the address below. You can try it on as you would in a shop; please do not
wear or wash it. [ADVISER: confirm diminished-value wording]
Address:
[RETURN ADDRESS]

Return postage for change-of-mind returns is paid by you. [OWNER DECISION / ADVISER: keep or change]
We refund the price of the item and the standard delivery cost you paid within 14 days of your message, to your
original payment method. We may wait to refund until the item arrives or you send proof of posting.
This applies to sale items and to made-to-order pieces in our standard sizes and colours.
[ADVISER: confirm; personalised pieces made to your own measurements may be an exception]

Exchanges

The quickest way to get another size or colour is to place a new order and return the original as above.
Garment measurements for every size are on each product page; write to us if you are between sizes.

Faulty, damaged or wrong items

If something is wrong with your order, write to us with your order number and 2-3 photos. We will offer a
repair, a replacement or a refund, and we cover the return postage. Your legal guarantee rights (at least
2 years) are not affected by anything on this page.
[ADVISER: confirm wording; replaces the live 5-day defect window]
```

Notes for the adviser (from the live page conflicts, README s11): removes the sale and made-to-order exclusions,
removes "shipping not refunded", removes the 5-day defect window. Withdrawal form: model form text from Directive
2011/83/EU Annex I(B) to be added (adviser to confirm language versions).

## B. Short lines for other teams (only after owner approval + adviser answer)

| Where | Line (ASSUMPTION) |
|---|---|
| PDP / cart note | "Dispatched in 2-5 working days from Riga. Tracked delivery." |
| FAQ returns | "14 days to change your mind after delivery. Return postage is paid by the customer; faulty items are on us." |
| CX RETURN_START macro | uses R1 below |

Never use: "free returns", "hassle-free", "no questions asked" (claim not backed until the adviser answers).

## C. Reply drafts R1 and R2 with assumed values (owner sends; supersede `returns-handling.md` s5 placeholders)

R1 Withdrawal acknowledgement
```
Subject: Your return for order [#]
Hello [name], thank you for letting me know. Your return for [item] is noted.
Please send it back by [notice date + 14 days] to: [RETURN ADDRESS]. Return postage is paid by you
[ASSUMPTION A-OPS-22 — OWNER DECISION]; a tracked parcel-locker service is the easiest option (in Latvia
usually a few euros). Please put your order number in the parcel.
When it reaches us, or when you send proof of posting, I refund [item price + standard delivery paid]
to your original payment method, at the latest by [notice date + 14 days].
If the size was the issue, I am happy to help you choose another: [size advice from the product page].
Kristine, Autumn & Wool
```

R2 Faulty or damaged item
```
Subject: Your order [#] — sorry about this
Hello [name], I am sorry the [item] did not arrive as it should. Could you send 2-3 photos of the item
(and the parcel, if it was damaged in transit)? Then I can offer [OWNER DECISION: repair / replacement / refund].
We cover the return postage for faulty items. [OWNER DECISION: prepaid label or refund of postage]
Kristine, Autumn & Wool
```

## TODO / missing data

- Owner decisions 13 (address, postage), 21 (regions), 22 (send to adviser) — OPS-16 stays BLOCKED on these.
- Adviser: return-postage disclosure wording, MTO/personalised exception, guarantee wording, withdrawal form, label
  languages, customs/duties line.
- Accountant: US duty handling (A-OPS-08).
- Verify the live FAQ exchange wording before quoting the "Exchanges" paragraph.
