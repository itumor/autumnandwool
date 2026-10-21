DRAFT — for owner approval. Pre-drafts for CX tasks dated later (wave 2, 2026-10-21). Nothing is sent, scheduled
or uploaded. Each section says what is still missing and the date it gets finished.

# Prepared work for CX-27, CX-28, CX-29, CX-30 to CX-33

## CX-27 FAQ/PDP proposals from real questions (finish 14 Nov)
Needs 2 weeks of inbound (owner-inputs-wave2 #1). Method, ready now:
1. Each week, from the case files, list every PRE_SALE_* and ORDER_STATUS question, paraphrased, no names.
2. Group by product and topic (size, fibre, care, lead time, delivery, payment, gift).
3. A question that appears 2+ times, or once on a priority-5 SKU, becomes a proposal: FAQ entry (to the owner),
   PDP line (to CRO, using its size-fit block), or macro update (CX).
4. Never add a fact the live page does not hold; unknown = `[VERIFY]`.

| Question (paraphrased) | Times (2 weeks) | Product | Proposal type | Draft wording | To |
|---|---|---|---|---|---|
| [FILL 14 Nov] | | | | | |

If fewer than 2 real questions arrive by 14 Nov, the output is "no evidence yet" and `faq-proposals.md` stands.

## CX-28 Automation freeze check (run 10 Dec)
Rule from `email-drafts/flow-plan.md`: no new automation goes live after 10 Dec (peak + holidays).

| # | Check on 10 Dec | Source | Result |
|---|---|---|---|
| 1 | Which automations are live (A1 welcome / A2 post-purchase / A3 win-back) and since when | owner screenshot of MailerLite Automations | [FILL] |
| 2 | Any automation planned to start between 10 Dec and 4 Jan? If yes, postpone to January | CX plan, owner | [FILL] |
| 3 | Active subscribers vs 250 Free cap; emails sent this month vs 2,500 | MailerLite dashboard (owner) | [FILL]; alert at 200 |
| 4 | Every product in a live email is still GREEN this week | PRD capacity file | [FILL] |
| 5 | Any date in a live email (Christmas cutoffs) matches the owner-approved OPS table | OPS table, decision 33 | [FILL] |
| 6 | Reply promise and out-of-office (macro 15) ready for market days and 24-26 Dec | owner | [FILL] |
Output: one line per row in the CX weekly of that week, plus "freeze confirmed" or the exception list.

## CX-29 `crm-monthly-2026-12.md` (finish 31 Dec, after month close)
Skeleton to copy into the monthly file:
```
DRAFT — for owner approval
# Email + retention report — December 2026
Sources: MailerLite reports (owner export), Squarespace Orders + Etsy (owner export), GA4 sessions with
utm_source=mailerlite, review platform, OPS returns-log.
## 1. List: subscribers start / end of month, new by source, unsubscribes, cap headroom (250)
## 2. Flows: per email delivered, clicks, unsubscribes, replies (opens indicative only)
## 3. Orders with email UTM (GA4 sessions; Squarespace order notes); "we can verify M"
## 4. Reviews: requests sent (all buyers equally), reviews received, replied within 2 business days
## 5. Support: threads, median reply, top questions, returns by reason (from CX weeklies)
## 6. Repeat purchase rate: not yet meaningful (first value Jan 2027)
## 7. Q1 2027 campaign drafts (max ~2/month): see below
## 8. Owner decisions needed
```
Q1 campaign slots (drafts below need GREEN products and approved dates before use):
| Month | Campaign | Job | Status |
|---|---|---|---|
| Jan | Care letter (no product push) | help winter buyers keep pieces well; reduce "pilling" complaints | Draft below |
| Feb | One GREEN piece + fit note | first non-gift sale | Needs GREEN list (Feb) |
| Mar | Lighter layer / spring colours | if Production has a spring piece (PRD-31) | Needs Production |

### Draft: January care letter (campaign, all consented subscribers)
Subject (<=45): How to look after your wool this winter
Preheader (<=90): Washing, drying, storing, and what to do about little bobbles.
Body (about 170 words):
> Hello [first name],
>
> January is when knitwear works hardest, so here is how I look after mine.
>
> Washing: wool needs less washing than you think. Air it out after wearing. When it does need a wash, use cold
> water and a wool-safe detergent, by hand. [VERIFY per product page: some pieces may allow a wool cycle; never
> say machine-washable unless the page does.]
>
> Drying: press the water out gently in a towel, never wring, and dry it flat. Never tumble dry.
>
> Storing: fold it, do not hang it, so the shoulders keep their shape.
>
> Little bobbles where the sleeves rub are common with wool. [VERIFY owner: her advice, e.g. a fabric comb, in her
> own words.]
>
> If something has come loose or worn through, reply and tell me. [OWNER DECISION: mending offer, if any, and its
> terms.]
>
> Kristine
CTA: "Read the care guide" -> https://www.autumnandwool.com/faq?utm_source=mailerlite&utm_medium=email&utm_campaign=care-2027-01&utm_content=care-guide-button
Facts used: hand wash cold, wool-safe detergent, dry flat, no tumble dry, store folded (live `/faq`, as used in
welcome W3). Not used: itch-free, never pills, machine-washable (brand voice s3).
Compliance: consent basis per audience (CX-19); unsubscribe; sender identity + postal address.

## CX-30 Q1 2027 (finish 31 Mar 2027)
- **January returns window.** Christmas deliveries of about 14-24 Dec mean withdrawal deadlines of about 28 Dec -
  7 Jan (14 calendar days from receipt; a deadline on a non-working day moves to the next working day; adviser
  confirms). Refund due = notice date + 14 days. From 2 Jan the Friday returns check runs on every open case. Gift
  exchanges follow owner decision 31 (owner-inputs-wave2 #9).
- **Baselines to set in January:** median first reply (from CX weeklies), SIZE_* share of returns (OPS log),
  repeat purchase rate = customers with 2+ orders / customers (owner export, all time and Q4 cohort), review count.
- **First review wave:** P3 to every Q4 buyer with a consent basis, all equally (no gating), once the platform is
  chosen (CX-23).
- **Care campaign:** draft above.
- **MailerLite tier decision:** if active subscribers > 200 or a 4th automation is needed, a costed proposal to
  the owner (Free plan limits re-verified on the pricing page first).

## CX-31 Q2 2027 (finish 30 Jun 2027)
Review platform live (after adviser, CX-23); post-purchase stable (weekly gap check: dispatched vs added to
"Customers"); care/mending email to Q4 buyers; spring campaign on GREEN pieces; win-back test only if a lapsed
segment with a valid basis exists (180 days after Q4 orders = June earliest).

## CX-32 Q3 2027 (finish 30 Sep 2027)
Back-in-stock and new-season opt-in forms (explicit consent wording via adviser); first win-back B1-B3 with
`win-back-<yyyy-mm>` UTMs; country segments only if the list is big enough to matter; macro refresh from Q1-Q2
questions; Christmas 2027 macros (12-14) approved by 15 Sep using OPS's 1 Oct carrier-backed dates (OPS-22).

## CX-33 Q4 2027 (finish 31 Dec 2027)
Gift campaigns on GREEN SKUs with approved OPS dates; peak replies inside the promise at 100%; post-Christmas
exchange process (draft once decision 31 is made for 2026 and tested in January 2027); annual CRM report; support
help decision against the hiring trigger (`head-of-ecommerce/hiring/cx-support-part-time-scorecard.md`).
