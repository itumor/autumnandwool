DRAFT — for owner approval. Nothing here is sent. The owner reads, edits and sends every reply.

# Support macro library v1 (CX-05, CX-06, CX-09; skeletons for CX-10, CX-11, CX-25)

Owner: aw-customer-experience agent. Written 2026-10-21. Review: monthly, or when a policy fact changes.
How to use: pick a macro, replace every `[ ]`, delete what does not apply, and run the quality check (bottom of
the page). `[VERIFY: ...]` = fact not confirmed yet. Do not send a reply that still has one. `[OWNER DECISION]` =
only the owner decides.

## Facts used (and source)

| Fact | Wording to use | Source (read 2026-10-21) | Status |
|---|---|---|---|
| Reply time | "We usually reply within 1-2 business days" | Live `/faq` and `/shipping-returns`; master plan ruling C2 | Contact page still says "within 24 hours". Owner confirms C2 by 7 Nov (decision 26) |
| Dispatch | "In-stock pieces leave Riga in 2-5 working days. Made-to-order pieces follow the time on their product page" | Live `/faq`, `/shipping-returns` | Owner decision 3 (24 Oct) may change it |
| Delivery | "Europe about 5-10 working days; USA, Canada, Australia 7-20 working days. Estimates, not guarantees" | Live `/shipping-returns` | Carrier-backed ranges from OPS after 6 Nov (ruling C8) |
| Shipping cost | "Free to Latvia, the US and the destinations shown at checkout" | Live `/faq` | OK |
| Duties | "EU prices include VAT. Outside the EU, import duties may apply under local rules" | Live `/faq` | OK |
| Payment | "Card through secure checkout". PayPal not available | Live `/faq`; README s2 | Change when PayPal is live (decision 14) |
| Care (general) | "Hand wash cold with a wool-safe detergent, dry flat, do not tumble dry. Store folded" | Live `/faq` | Check the product page per piece |
| Fibre | Copy from that product's live page only | aw-brand-voice s3 | Never generalise |
| How it is made | "Knitted on manual machines and finished by hand in Riga" | aw-brand-voice s2-s3 | Live FAQ says "knitted by hand or on a manual machine": see `faq-proposals.md` P3 |
| Etsy proof | "4.9 stars, 1,400+ reviews on Etsy (Mareshop)" | Master plan ruling C1 | Change everywhere once owner picks (decision 17) |
| Returns | Statutory floor, case by case, owner approves. Do not quote the live exclusions or the 5-day defect window as a reason to refuse | aw-returns-handling; ruling C12 | Adviser review pending (decision 22) |
| Return address | none published | Live `/shipping-returns` ("contact us for instructions") | Owner decision 13 (30 Oct) |
| Christmas order-by dates | none published | OPS plan: provisional only | OPS carrier-backed 14 Nov, publish 20 Nov |

Signature: "Kristine, Autumn & Wool" for personal replies, "Autumn & Wool" otherwise. Email length 50-150 words.
DM/comment 1-3 sentences. Answer the customer's question in the first sentence. Reply in the customer's language.
If it is translated, mark it `[translated, human check]`.

---

## 1. SIZE_HELP (pre-sale, P2, same day)

See `size-advice.md` for the method and three variants (ask for measurements / recommend / between sizes).

## 2. LEAD_TIME (pre-sale, P2)

```
Subject: When your [product] would arrive

Hello [first name],

Thank you for asking. [Product] is [in stock / made to order: VERIFY on the product page today].
In-stock pieces leave our Riga studio in 2-5 working days. [Made to order: the product page gives
[VERIFY time] before dispatch.] Delivery then takes about [5-10 working days in Europe / 7-20 working
days to the USA, Canada and Australia]. These are estimates, not guarantees.
Shipping is free to [country, if listed at checkout].

If you need it by a particular date, tell me the date and the country and I will check honestly
whether we can make it.

Kristine, Autumn & Wool
```

## 3. ORDER_STATUS (P2; P1 if late)

A, dispatched:
```
Subject: Your order [#] is on its way

Hello [first name],

Your order [#] left Riga on [dispatch date: from dispatch log] with [carrier: VERIFY].
You can follow it here: [tracking link]. Delivery to [country] usually takes [range], so it should
arrive around [date range].

If the tracking has not moved by [date + 3 working days], write back and I will look into it with
the carrier.

Kristine, Autumn & Wool
```
B, not dispatched yet:
```
Hello [first name],

Your order [#] is being [finished / packed] in our Riga studio. It will be dispatched by
[date: VERIFY with owner/production] and I will send the tracking link the same day.

Kristine, Autumn & Wool
```

## 4. DELAY (P1; send before the customer asks)

```
Subject: A short delay on your order [#]

Hello [first name],

I am sorry: your [product] will leave Riga later than we said. [One-line honest reason, e.g. "the
yarn for this colour arrived late" — VERIFY]. The new dispatch date is [date: VERIFY].

What you can choose:
1. Wait: I will send tracking the day it ships.
2. Switch to [alternative in stock: VERIFY on the GREEN list].
3. Cancel: [OWNER DECISION: full refund wording].

Just reply with 1, 2 or 3. I am sorry for the wait.

Kristine, Autumn & Wool
```

## 5. CARE (P2)

```
Subject: Caring for your [product]

Hello [first name],

Good question. For [product] ([fibre exactly as on the product page]) we recommend: hand wash cold
with a wool-safe detergent, dry flat, and do not tumble dry. Store it folded in a breathable bag
(cedar or lavender helps). [Optional, VERIFY with owner: "press the water out gently, do not wring".]
[If the product page gives other care: use that wording instead. VERIFY per piece.]
Small bobbles can appear where wool rubs; a wool comb or sweater stone removes them.
[VERIFY: owner agrees with this tip.]

Kristine, Autumn & Wool
```
Do not use: "machine-washable", "itch-free", "never pills", "hypoallergenic".

## 6. MATERIAL (P2)

```
Hello [first name],

[Product] is [composition copied exactly from the live product page, e.g. "100% merino wool"].
It is knitted on manual machines and finished by hand in our Riga studio.
[Texture/feel: only what the product page says, e.g. weight, rib, drape.]
If you are sensitive to wool, please tell me which fibres you usually wear, and I will tell you
honestly whether this piece is a good idea.

Kristine, Autumn & Wool
```
Do not use: sustainable, eco, organic, certified, mulesing-free, RWS, hand-knitted. If a customer asks about
certification, write: "I do not have certification documents I can share for this yarn at the moment." [VERIFY
with owner before sending.]

## 7. RETURN_START (P1; dates and log per aw-returns-handling)

Before drafting: classify (withdrawal / exchange / faulty / wrong item / outside window), work out the dates,
and pass the case to OPS's `returns-log.csv` (proposed by OPS, due 30 Oct). Put the owner decision at the top
of the case file.

```
Subject: Your return for order [#]

Hello [first name],

Thank you for letting me know. Your return request for [item] is noted.
Please send it back by [notice date + 14 days] to: [return address: OWNER DECISION 13].
[Return postage: OWNER DECISION, per the approved policy.] Please put your order number inside.
Once it reaches us, or you send proof of posting, we refund [OWNER DECISION: amount; statutory
floor includes standard outbound delivery] to your original payment method, within 14 days of your
request.

If the size was the problem, I am happy to help you choose another one. Just send me your chest
measurement and the fit you like.

Kristine, Autumn & Wool
```
Exchange (live FAQ flow; owner confirms it is still current): "To swap, place a new order for the size or colour
you want and send the original back. We refund the first order once the return arrives [OWNER DECISION: timing]."
Outside the window: do not refuse in the draft. Send the case to the owner with the dates.

## 8. DAMAGED / FAULTY / WRONG ITEM (P1)

```
Subject: Your [product], order [#]

Hello [first name],

I am really sorry the [product] arrived [damaged / with a fault / as the wrong item]. That is not
how it should reach you.
Could you send me 2-3 photos: the item (close-up of the problem) and the parcel/label? Once I have
them, I will reply within one business day with the options: [OWNER DECISION: repair /
replacement / refund]. We cover the return postage for faulty or wrong items.

Kristine, Autumn & Wool
```
Never mention the live "report within 5 days" clause. Never ask the customer to prove the fault existed at
delivery.

## 9. PAYMENT_PAYPAL (P2)

While PayPal is not connected:
```
Hello [first name],

PayPal is not available in our shop yet, sorry. You can pay by credit or debit card at our secure
checkout. [If the payment failed: tell me roughly when and which step showed the error, and I will
check it — never send card details by email.]

Kristine, Autumn & Wool
```
When PayPal is live (decision 14): "You can pay by card or PayPal at checkout." Remove the first sentence.

## 10. REVIEW_THANKS (public reply, P3, within 2 business days)

```
Thank you, [first name]. I am glad the [product, colour] [detail they mentioned: "fits as you hoped"
/ "kept you warm in the wind"]. — Kristine
```
Rules: name the specific item or detail, keep it to 1-2 sentences, no incentive, no "tell your friends".

## 11. REVIEW_NEGATIVE (public reply, P1 internally)

```
Thank you for telling us, [first name], and I am sorry the [product] was not what you hoped for.
I would like to put this right. Please email me at autumnandwool@gmail.com so we can sort it out
together. — Kristine
```
Rules: no argument, no order details in public, no admission of legal liability, never ask for the review to be
changed or removed in exchange for anything. Draft the private follow-up with DAMAGED or RETURN_START.

## 12. GIFT (pre-sale, P2) — BLOCKED until OPS dates and owner decision 31

```
Hello [first name],

How lovely that it is a gift. [Gift note: OWNER DECISION 31 — can we add a handwritten note?]
[Prices on the packing slip: VERIFY whether Squarespace prints prices, OPS.]
To arrive before Christmas in [country], please order by [date: OPS cutoff table, published
20 Nov]. If the size is a guess, send me what you know (their usual size, or a sweater of theirs
laid flat), and I will suggest the safest choice. [Exchange after Christmas: OWNER DECISION 31.]

Kristine, Autumn & Wool
```

## 13. CHRISTMAS_DEADLINE (Dec) — BLOCKED until OPS dates

```
Hello [first name],

For delivery before 24 December, the last order dates are: Latvia [VERIFY OPS], EU [VERIFY OPS],
USA/Canada/Australia [VERIFY OPS, or "Christmas delivery cannot be guaranteed"].
Your country, [country], is [inside / past] the date, so [it should arrive in time / I cannot
promise it before Christmas, sorry]. [After the cutoff, a digital gift card: VERIFY it exists on
the store.]

Kristine, Autumn & Wool
```
The OPS provisional dates (about 10 Dec Latvia, about 3 Dec EU, about 18-19 Nov US/CA/AU) are worst-case
arithmetic. Do not quote them before the owner approves the table.

## 14. GIFT_SEASON_WISMO ("where is my order", Dec)

ORDER_STATUS A or B, plus: "December post is busy, so carriers may need [VERIFY OPS] extra days. If it has
not arrived by [date], reply and I will chase it straight away."

## 15. OUT_OF_OFFICE (markets, holidays)

```
Thank you for your email. I am [at a Christmas market / away] until [date], so my reply may take a
little longer than usual. I will answer by [date]. For delivery times and returns, see
https://www.autumnandwool.com/faq — Kristine, Autumn & Wool
```
The owner switches it on in Gmail. The agent never does.

## 16. ESCALATION protocol (CX-05): owner told the same day, no reply drafted before the owner sees it

| Trigger | What the agent does | Holding reply (owner may send) |
|---|---|---|
| Legal threat, PTAC complaint, lawyer | Owner the same day; summarise facts and dates; adviser flag | "Thank you, I have received your message and will reply in full by [date]." |
| Chargeback / payment dispute | Owner the same day; collect order no., dates, tracking (no card data) | none: owner replies to Stripe |
| Allergy / skin reaction | Owner the same day; ask nothing medical; no admission, no product claim | "I am very sorry to hear this. I have passed it to Kristine personally and she will reply today." |
| Data access / deletion request (GDPR) | Owner the same day; log the date received; no legal conclusion | "Thank you, we have received your request and will confirm the next steps by [date]." |
| Abuse or threats to safety | Owner the same day | none |

Case files hold the first name and case number only. No addresses, no payment details, no personal data in URLs.

---

## Quality check (each draft, before handing it to the owner)

1. Is the question answered in the first sentence?
2. Is there no refund, discount, free shipping, replacement or date promise without an owner decision?
3. Is every fact traced to the facts table above or a business-os file? Is no `[VERIFY]` left?
4. Is there one clear next step (who does what, by when)?
5. Are the name and order number correct, and does the length fit the channel?
6. No banned words (aw-brand-voice s3): sustainable, eco, organic, certified, hand-knitted, luxurious, must-have?

## Change log
- 2026-10-21 v1 drafted (16 macros incl. escalation). Owner review requested by 14 Nov (plan target).
