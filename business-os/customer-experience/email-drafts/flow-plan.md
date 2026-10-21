DRAFT — for owner approval. Nothing is uploaded to MailerLite, imported, scheduled or sent. The owner sets up
and activates everything.

# Email flow plan: MailerLite Free (CX-17)

Written 2026-10-21 by the aw-customer-experience agent. Drafts: `welcome.md` (A1, 4 emails),
`post-purchase.md` (A2, 3 emails including the review request), `win-back.md` (A3, 3 emails).

## Constraints (MailerLite Free; seen Oct 2026 per the skill; owner re-checks https://www.mailerlite.com/pricing)
250 active subscribers, 2,500 emails a month, 3 active automations of up to 5 steps each, one trigger each, no
ecommerce triggers. Squarespace orders do not reach MailerLite on their own, so buyers enter a group by hand.

## The three automations

| # | Automation | Trigger | Steps (delay) | Goal | Exit | Go-live gate |
|---|---|---|---|---|---|---|
| A1 | Welcome | joins group "Newsletter" | W1 now -> W2 day 3 -> W3 day 6 -> W4 day 10 | first order | owner removes buyers; unsubscribe | Activation checklist below. Target 28 Nov |
| A2 | Post-purchase | owner adds buyer to "Customers" at dispatch | P1 day 0-1 -> P2 day 10 (about delivery + 3) -> P3 day 18 (about delivery + 7-14) | care, catch problems early, honest reviews | unsubscribe | P1 after the checklist; P2-P3 only after the adviser rules on consent (G9) |
| A3 | Win-back | owner adds to "Lapsed" (no order for [OWNER DECISION: 180 days proposed]) | B1 day 0 -> B2 day 4 -> B3 day 11 | second order, or a cleaner list | buys; picks a preference; unsubscribe | Not before lapsed customers with consent exist (2027 Q3 at the earliest) |
| C | Manual campaigns | owner schedules | at most 2 a month | new pieces, care, Christmas dates | — | GREEN list only |

Volume check at the cap: 250 subscribers x 4 welcome emails = 1,000, which leaves about 1,500 a month for
campaigns and A2. Watch it weekly in the CX summary.

## Activation checklist (owner; all must be "yes" before A1 goes live)

| # | Check | How to verify | Status |
|---|---|---|---|
| 1 | MailerLite account exists and the owner controls it | login | TODO owner (decision 30) |
| 2 | Squarespace newsletter block -> where contacts land (Squarespace list? Mailchimp? MailerLite?) | owner looks in Squarespace Marketing > Email / Form storage | TODO owner |
| 3 | Signup form tells people what they will get and records date and source | screenshot of the form | TODO owner + adviser |
| 4 | Sender name "Kristine from Autumn & Wool", sending domain/email verified | MailerLite domain settings | TODO owner |
| 5 | Footer: legal name AUTUMN AND WOOL, SIA, postal address, unsubscribe link | copy the address from the site footer (already live per `implementation-report.md`) | [VERIFY] |
| 6 | Reply promise matches the site (ruling C2: 1-2 business days) | read the Contact page | Contact page still says 24 h (CRO) |
| 7 | UTM names match GRO's `business-os/growth/utm-links.csv` | compare | Drafts aligned 21 Oct to `utm-taxonomy.md` v1 (`<flow>-<yyyy-mm>` + `w/p/b<n>-<position>`); owner approves the taxonomy by 31 Oct (C15); Growth adds the CX rows |
| 8 | Products in W4 / campaigns are on this week's GREEN list | PRD `capacity-YYYY-Www.md` | none GREEN yet (costs unknown) |
| 9 | Test send to the owner's inbox, links clicked, mobile view checked | owner | TODO |

## Consent basis per audience (CX-18/19): summary for the adviser, not a legal conclusion

| Audience | Proposed basis | Gets | Open question for the adviser |
|---|---|---|---|
| Website newsletter signups | Consent (form) | A1, campaigns | Is the current form wording enough? Double opt-in needed? |
| Direct buyers | Soft opt-in for similar products, opt-out at checkout and in every email, **or** a consent tick at checkout | A2 P1 as a service/care email; P2-P3 and A3 only with a valid basis | Is P1 transactional? Does Latvian law allow soft opt-in here, and in what form? Is a review request marketing? |
| Market or in-person signups | Written consent: name, email, date, place, tick box | A1 | Paper wording below OK? How long to keep the forms? |
| Etsy past buyers | **None** by default. Etsy's rules limit using buyer emails for marketing | none | Confirm: no import |

Market signup card wording (draft; the adviser checks it):
"Yes, I would like letters from Autumn & Wool (new pieces, care tips, about 2 a month). I can unsubscribe at any
time. Name / Email / Date / Signed." + privacy notice link. Typed into MailerLite with source "market-<name>-<date>".

## Getting buyers into "Customers" (proposal for owner decision 4)
1. At dispatch, the owner (or the packer) adds the buyer's email and first name to "Customers", only if the
   order shows a recorded basis (checkout tick or soft opt-in, per the adviser).
2. Monday check in the CX summary: orders dispatched last week vs buyers added. Any gap is listed by case
   number, never by email address.
3. When buyers are added to "Customers", the owner also removes them from A1 (exit rule).
4. Later (Q3 2027 or after the plan upgrade): look at a Squarespace -> MailerLite integration to remove the
   manual step.

## Review platform (owner decision 30)
Squarespace has no native reviews. Etsy reviews are for Etsy orders only. Options: Google Business Profile (if
it exists), Trustpilot free, an on-site app after the plan decision. P3 has a placeholder link until the owner
picks. Rules: ask every customer the same way (no gating), no incentive, never write or seed reviews. On-site
display needs a statement of how reviews are checked (Omnibus; the adviser confirms the wording).

## Metrics (monthly, `crm-monthly-YYYY-MM.md`)
Per flow: delivered, clicks, unsubscribes, replies, orders with the email UTM in Squarespace/GA4 sessions.
Open rate is indicative only. Business KPIs: repeat purchase rate (from January), review count and rate,
subscribers vs the 250 cap.

## Rules
One email, one job, one link. Value before the ask. No fake "Re:", no countdowns, no discount codes without a
Finance margin check and owner approval. Features come from the GREEN list only. No new automations after
10 Dec (CX-28).
