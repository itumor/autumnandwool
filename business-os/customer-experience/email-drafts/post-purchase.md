DRAFT — for owner approval. Not uploaded, not scheduled, not sent.

# A2 Post-purchase flow: 3 emails incl. review request (CX-15; enabling P3 = CX-23)

Segment: group "Customers". The owner adds the buyer at dispatch (see `flow-plan.md`), only with a recorded
consent basis. P2 and P3 wait for the adviser's answer on soft opt-in and review requests (gate G9).
UTMs (aligned 21 Oct with Growth `utm-taxonomy.md` s3): `utm_source=mailerlite&utm_medium=email&
utm_campaign=post-purchase-<yyyy-mm of activation>&utm_content=p<n>-<link-position>`, e.g.
`post-purchase-2026-11` + `p1-care-link`. Growth registers the rows in `utm-links.csv`. Same footer as the welcome flow.
Timing assumes Europe delivery of about 5-10 working days after dispatch. For US/CA/AU buyers (7-20 days), the
owner adds them about 7 days after dispatch instead [OWNER DECISION: or use a separate group].

---

## P1: Thank you, care and what to expect (day 0-1 after dispatch)

Subject: Your [piece] is on its way from Riga
(Fallback if the merge field is missing: "Your order is on its way from Riga")
Preheader: What to expect, and how to care for it.

Body (transactional length, about 110 words):
> Hello [first name],
>
> Thank you for your order. It has left the studio, and the tracking link is in your shipping confirmation.
> [VERIFY: does Squarespace send the tracking email? OPS checks]
>
> When it arrives: wool can hold the folds from the parcel. Lay it flat for a few hours, or steam it lightly,
> and it will relax. [VERIFY with owner]
>
> To keep it looking right: hand wash cold with a wool-safe detergent, dry flat, never tumble dry, store it
> folded. The care for your piece is on its product page [and on the care card in the parcel: VERIFY OPS
> packaging spec].
>
> Any question about fit or anything else, just reply. I read every email.
>
> Kristine

CTA: none (service email); a text link "Care guide" -> /faq?utm_source=mailerlite&utm_medium=email&utm_campaign=post-purchase-2026-11&utm_content=p1-care-link
Facts used: care (live FAQ); tracking (live Shipping page "sent with tracking").
[VERIFY]: the "relax the folds" tip; care card; tracking email.
Compliance: the adviser says whether this counts as service (transactional) or marketing.

---

## P2: How does it fit? (day 10, about delivery + 3 days)

Subject: How does your [piece] fit?
Preheader: If anything is not right, tell me now, I can still help.

Body (about 100 words):
> Hello [first name],
>
> Your [piece] should have arrived a few days ago, so I wanted to ask: how does it fit?
>
> If something is not right (size, colour, anything at all), reply to this email and tell me. There is still
> time to sort it out, and I would much rather hear it from you than have you put up with it.
>
> And if it fits just as you hoped, I would love to know that too.
>
> Kristine

CTA: "Reply to Kristine" (mailto reply; no product link). The job is to catch problems early, not to sell.
Note for the owner: replies here come into the support inbox as P1 (fit problem) or REVIEW/PRAISE. A reply that
mentions a return goes to RETURN_START with the dates.
Withdrawal window: the 14 days usually run from delivery, so day 10 is roughly inside it. Do not mention
deadlines in this email (no legal statements); the macros handle that.

---

## P3: Review request (day 18, about delivery + 7-14 days)

Subject: Would you share a few words?
Preheader: An honest review helps other people choose their size.

Body (about 110 words):
> Hello [first name],
>
> You have had your [piece] for a couple of weeks now. If you have a moment, would you write a short, honest
> review? Other people find it most useful when it mentions how the size fitted and how the wool feels.
>
> [Leave a review]([REVIEW PLATFORM LINK: OWNER DECISION 30]?utm_source=mailerlite&utm_medium=email&utm_campaign=post-purchase-2026-11&utm_content=p3-review-link)
(If the review platform is external, e.g. Etsy or Google, the UTM has no effect there; keep the link plain.)
>
> If something is not right, please reply to me first so I can help. You are of course free to review it either
> way.
>
> Thank you for choosing a piece from our studio.
>
> Kristine

Rules met: sent to every buyer in "Customers", whatever happened with their order (no gating); no incentive; no
suggested rating; we never edit, seed or write reviews. "Reply first" is an offer of help, not a filter: it
must not stop anyone reviewing (the adviser checks this wording against Omnibus / unfair-practice rules).
BLOCKED: review platform (decision 30); adviser (G9).

### P3 wave 3: DRAFT-ASSUMPTION version (reply by email, no platform)

ASSUMPTION: no review platform in Q4, P3 asks for a reply by email (A-GM-14, A-CX-06); only buyers with a recorded
consent basis are in "Customers" (A-GM-14: in Q4 that means newsletter sign-ups who bought). Register:
`business-os/customer-experience/assumptions-wave3.md`. Activation goes with CX-22 (MailerLite) and the adviser's
answer on review requests (G9).

Subject (<=45): How is your [piece] after two weeks?
Preheader (<=90): A few honest words by reply help me, and help the next person choose a size.

Body (about 100 words):
> Hello [first name],
>
> You have had your [piece] for a couple of weeks now, and I would really like to know how you find it.
>
> If you have a moment, just reply to this email with a few honest words: how the size fitted, how the wool feels,
> and anything you would change. Good or not so good, both help me make the next pieces better.
>
> If something is not right, tell me that too, and I will help.
>
> Kristine

CTA: "Reply to Kristine" (reply-to `autumnandwool@gmail.com`, A-GM-14). No link, no incentive, no rating scale.
Rules: sent to every buyer in "Customers" (no gating); replies are never published, quoted or turned into a review
without the customer's written yes and the owner's yes (decision 17; HARD RULE 5). Replies go to triage as
REVIEW/PRAISE or, if a problem, P1 (RETURN_START / DAMAGED). When the owner picks a platform, the link version above
returns.
[ADVISER G9]: confirm this email may go to buyers on the assumed consent basis, and whether it counts as marketing.
