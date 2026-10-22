DRAFT — for owner approval. Not uploaded, not scheduled, not sent. Stays unused until a lapsed segment with a
valid consent basis exists (Q3 2027 at the earliest; the adviser confirms the basis first).

# A3 Win-back flow: 3 emails (CX-16)

Segment: group "Lapsed" = customers with no order for [OWNER DECISION: 180 days proposed, because knitwear buying
is seasonal]. Exit: buys, picks a preference, unsubscribes. UTMs (aligned 21 Oct with Growth
`utm-taxonomy.md` s3): `utm_campaign=win-back-<yyyy-mm of first send>&utm_content=b<n>-<sku-slug or position>`.
Same footer. Features come from the GREEN list on the send date only.

---

## B1: New for the season (day 0)

Subject: New from the Riga studio this [season]
Preheader: [VERIFY: name the new piece or colour.]

Body (about 150 words):
> Hello [first name],
>
> It has been a while since your [previous piece, if the merge field exists; otherwise "your last order"], so I
> wanted to show you what is new in the studio.
>
> [One new piece or colour from the GREEN list: name, fibre exactly as on its PDP, fit type, one specific detail,
> price from the live page.]
>
> [One line from Kristine on why she made it: owner's words. VERIFY]
>
> Kristine

CTA: "See [piece]" -> [PDP URL]?utm_source=mailerlite&utm_medium=email&utm_campaign=win-back-[yyyy-mm]&utm_content=b1-[sku-slug]

---

## B2: One favourite and a care tip (day 4)

Subject: A small tip for the wool you already have
Preheader: And one piece that goes well with it.

Body (about 140 words):
> Hello [first name],
>
> A quick one. If your knitwear has small bobbles where it rubs, a wool comb or sweater stone takes them off in a
> minute [VERIFY: owner agrees]. A light steam brings back its shape between washes.
>
> If you are thinking of adding a piece, this is the one people come back to most:
> [GREEN SKU with real repeat or sales evidence: VERIFY. If there is no evidence, say "the one I would pick" and
> do not call it a bestseller].
>
> Kristine

CTA: "See [piece]" -> [PDP]?utm_source=mailerlite&utm_medium=email&utm_campaign=win-back-[yyyy-mm]&utm_content=b2-[sku-slug]
Do not call anything a "bestseller" without order data (brand voice: no invented proof).

---

## B3: Should we keep writing? (day 11)

Subject: Should I keep writing to you?
Preheader: One click to stay, or to hear from us less.

Body (about 90 words):
> Hello [first name],
>
> I do not want to fill your inbox with letters you no longer read. If you would like to keep hearing about new
> pieces and care tips, click below and nothing changes.
>
> [Keep me on the list](preference link)
>
> If not, no hard feelings: you can unsubscribe here [unsubscribe link], or simply do nothing and I will stop
> writing after [VERIFY: e.g. 30 days].
>
> Thank you for having been a customer.
>
> Kristine

Owner action: anyone who does not click within [30 days] is removed or marked unsubscribed (list hygiene and the
250 cap). No discount in this flow unless Finance has checked the margin and the owner approves.
