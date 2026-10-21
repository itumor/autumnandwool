# Customer Experience — status 2026-10-21
Summary: 14 done · 11 blocked · 8 todo

| ID | Task | Due | Status | Output / blocker |
|---|---|---|---|---|
| CX-01 | Daily triage + support case-file template (categories, priorities, quality check, personal-data rules) | 21 Oct | DONE | [triage-and-case-template.md](../../../business-os/customer-experience/triage-and-case-template.md) |
| CX-02 | Daily inbound batch: triage + reply drafts for real messages | daily from 21 Oct | BLOCKED | Owner: paste or export inbound (Gmail, IG DMs, Etsy) each business day; none supplied yet |
| CX-03 | Weekly CX summary template (volume, reply time, open cases, reviews, list cap, top questions) | 26 Oct | DONE | [cx-weekly-template.md](../../../business-os/customer-experience/cx-weekly-template.md) |
| CX-04 | Friday returns and deadline check (refund-due dates, cases waiting on the owner) | Fridays from 23 Oct | DONE | Section 5 of [cx-weekly-template.md](../../../business-os/customer-experience/cx-weekly-template.md); reads OPS `returns-log.csv` (OPS, due 30 Oct) |
| CX-05 | Same-day escalation protocol (threats, chargebacks, allergy, data requests) | 21 Oct | DONE | Section 16 of [support-macros.md](../../../business-os/customer-experience/support-macros.md) |
| CX-06 | Macro library v1: SIZE, LEAD_TIME, ORDER_STATUS, DELAY, CARE, MATERIAL, RETURN_START, DAMAGED, PAYMENT_PAYPAL, REVIEW x2, OUT_OF_OFFICE | 14 Nov | DONE | [support-macros.md](../../../business-os/customer-experience/support-macros.md) (facts from live FAQ/Shipping, read 21 Oct; return address, carrier and care-per-yarn are [VERIFY]) |
| CX-07 | Size-advice method + size macros (ask / recommend / one size / gift / DM) | 14 Nov | DONE | [size-advice.md](../../../business-os/customer-experience/size-advice.md) (live body chart staged) |
| CX-08 | Garment measurement table per visible SKU (size data) | 14 Nov | BLOCKED | Owner decision 8: confirm garment measurements, or approve copying them from the live PDPs |
| CX-09 | Review reply templates (positive and negative, public) | 14 Nov | DONE | Macros 10-11 in [support-macros.md](../../../business-os/customer-experience/support-macros.md) |
| CX-10 | GIFT macro (gift note, last order date, gift exchange) | 14 Nov | BLOCKED | OPS: carrier-backed cutoffs (14 Nov). Owner decision 31: gift perks (FIN margin check). Skeleton is macro 12 |
| CX-11 | PAYMENT_PAYPAL macro switched to "card or PayPal" | when PayPal live | BLOCKED | Owner decision 14: connect PayPal (31 Oct). Both versions drafted in macro 9 |
| CX-12 | Fix welcome W1: one reply promise (ruling C2), UTMs, signed Kristine, original file untouched | 14 Nov | DONE | [email-drafts/welcome.md](../../../business-os/customer-experience/email-drafts/welcome.md) W1 |
| CX-13 | Welcome W2 (how it is made) + W3 (fit, size, care) | 14 Nov | DONE | [email-drafts/welcome.md](../../../business-os/customer-experience/email-drafts/welcome.md) (W2 needs Kristine's own words, decision 20) |
| CX-14 | Welcome W4: three products to start with | 14 Nov | BLOCKED | PRD: no SKU is GREEN yet (costs unknown; first GREEN after 4 Nov). CRE: real photo per colour. Skeleton in welcome.md |
| CX-15 | Post-purchase P1-P3 (care + what to expect, fit check, review request) | 14 Nov | DONE | [email-drafts/post-purchase.md](../../../business-os/customer-experience/email-drafts/post-purchase.md) |
| CX-16 | Win-back B1-B3 drafts | 30 Nov | DONE | [email-drafts/win-back.md](../../../business-os/customer-experience/email-drafts/win-back.md) (unused until a lapsed segment with consent exists) |
| CX-17 | Email flow plan: 3 automations, activation checklist, consent table, buyers-to-group process, market signup wording | 14 Nov | DONE | [email-drafts/flow-plan.md](../../../business-os/customer-experience/email-drafts/flow-plan.md) |
| CX-18 | Adviser question pack: consent, soft opt-in, review rules, data requests, returns replies | 3 Nov | DONE | [adviser-questions-cx.md](../../../business-os/customer-experience/adviser-questions-cx.md) |
| CX-19 | Consent basis per audience recorded and approved | 14 Nov | BLOCKED | Owner sends the adviser pack (decision 22); adviser answers (G9); owner decides (decision 30) |
| CX-20 | One reply-time promise on the Contact page, FAQ, emails and macros | 7 Nov | BLOCKED | Owner confirms ruling C2 (decision 26). CRO edits the Contact page (still says 24 h; FAQ and Shipping say 1-2 business days) |
| CX-21 | FAQ and policy-wording proposals from the live pages (9 inconsistencies, 7 new entries) | 14 Nov | DONE | [faq-proposals.md](../../../business-os/customer-experience/faq-proposals.md) |
| CX-22 | MailerLite set up and welcome flow live (owner-activated) | 28 Nov | BLOCKED | Owner decision 30: account, where newsletter contacts land, sender identity and address, unsubscribe, test send |
| CX-23 | Review platform chosen; review request (P3) enabled | 14 Nov | BLOCKED | Owner decision 30 (platform) + adviser (Omnibus wording, G9) |
| CX-24 | Weekly subscribers vs 250 Free cap, alert at 200 | weekly from 28 Nov | BLOCKED | Needs the MailerLite account (CX-22) |
| CX-25 | Christmas-deadline and gift-season "where is my order" macros | 20 Nov | BLOCKED | OPS: carrier-backed cutoffs 14 Nov, published 20 Nov after owner approval. Skeletons are macros 13-14 |
| CX-26 | First weekly CX summary `cx-weekly-2026-W44.md` | 26 Oct | TODO | Uses the template from CX-03 |
| CX-27 | FAQ/PDP proposals from the first 2 weeks of real questions | 4-14 Nov | TODO | Needs 2 weeks of inbound (CX-02) |
| CX-28 | No new automations after 10 Dec (freeze check) | 10 Dec | TODO | Rule is in flow-plan.md |
| CX-29 | `crm-monthly-2026-12.md`: first email and retention report + Q1 campaign drafts | 31 Dec | TODO | Needs December data |
| CX-30 | Q1 2027: baselines (reply time, SIZE_* return share, first repeat rate), January returns surge, first review wave, care campaign, MailerLite tier decision | 31 Mar 2027 | TODO | Starts Jan 2027 |
| CX-31 | Q2 2027: review platform live, post-purchase stable, care/mending emails, spring campaign, first win-back test if eligible | 30 Jun 2027 | TODO | Starts Apr 2027 |
| CX-32 | Q3 2027: back-in-stock and new-season opt-in lists, first win-back, country segments, macro refresh, Christmas macros approved by 15 Sep | 30 Sep 2027 | TODO | Starts Jul 2027 |
| CX-33 | Q4 2027: gift campaigns (GREEN + OPS dates), peak replies at 100%, post-Christmas exchange process, annual CRM report, support-help decision | 31 Dec 2027 | TODO | Starts Oct 2027 |

## Blocked on owner
- Paste or export inbound customer messages daily (Gmail, Instagram DMs, Etsy) so drafts can start (CX-02).
- Confirm the reply-time promise of 1-2 business days (ruling C2, decision 26, by 7 Nov). Contact page still says 24 h (CX-20).
- MailerLite: account, where Squarespace newsletter contacts land, sender name and postal address, unsubscribe, test send (decision 30, by 14 Nov) (CX-22, CX-24).
- Send the adviser pack (decision 22, by 3 Nov), then record the consent basis per audience (CX-18, CX-19).
- Choose the review platform and say whether verbatim Etsy quotes may be used (decisions 30, 17) (CX-23).
- Confirm garment measurements per visible SKU (CX plan decision 8) (CX-08).
- Return address and who pays return postage (decision 13, by 30 Oct), needed in RETURN_START (CX-06).
- Connect PayPal (decision 14, by 31 Oct) (CX-11).
- Gift-season perks after the FIN margin check (decision 31) (CX-10).
- Kristine's own words for welcome W2 (decision 20) (CX-13).
- Claims: confirm whether any piece is hand-knitted. The live FAQ says "knitted by hand or on a manual machine" (decision 16; faq-proposals P3).
