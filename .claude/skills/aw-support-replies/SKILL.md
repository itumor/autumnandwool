---
name: aw-support-replies
description: Use when drafting an Autumn & Wool reply to a customer email, Etsy message, Instagram DM or comment (size advice, order status, delivery, returns, complaints, product/material questions, review responses), triaging the support inbox, or building FAQ / size-advice macros. Drafts only; a human sends.
---

# Customer support replies and macros

Purpose: every customer gets an accurate, warm, specific reply within 24 hours (target in `hiring-plan.md`),
drafted by the agent, checked and sent by a human. Also maintains a macro library in
`business-os/support-macros.md` (propose).

Response-time promise conflict: Contact page says "we reply within 24 hours"; welcome email draft says
"1-2 business days". Flag to owner; use 24 h as the internal target.

## 1. Triage (each inbound)

| Category | Examples | Priority / target | Route |
|---|---|---|---|
| ORDER_ISSUE | not received, wrong item, damaged | P1: draft within 4 business hours | aw-fulfilment-sop + owner |
| RETURN | withdrawal, exchange, faulty | P1 | aw-returns-handling (dates + log) |
| PRE_SALE_SIZE | "which size?", fit, measurements | P2: same day (lost sale risk) | size advice below |
| PRE_SALE_PRODUCT | material, colour, care, lead time, gift | P2 | product page + production facts |
| ORDER_STATUS | "when will it ship?" | P2 | dispatch log |
| PAYMENT | failed payment, PayPal request | P2 | owner (PayPal not connected) |
| REVIEW / PRAISE | review posted, thank you | P3: 2 business days | review reply template |
| COMPLAINT_SENSITIVE | anger, legal threat, chargeback, PTAC, allergy/skin reaction, privacy/data request | P1: owner first, no auto-draft tone of admission | owner |
| OTHER | wholesale, press, creators | P3 | owner / partnerships |

Bump priority if a customer has written twice, or the order is late.

## 2. Draft procedure

1. Read the full thread, order record (if given), product page facts, and the policy wording that applies.
2. Identify what the customer actually needs; answer that in the first sentence.
3. Structure: **acknowledge -> answer/inform -> next step (who does what by when) -> close**. Email: 50-150
   words. DM/comment: 1-3 sentences.
4. Use only verified facts: size-guide measurements, product page composition (only if supplier-verified;
   see aw-qc-and-labelling), dispatch promise, tracking. Unknown = `[CHECK: ...]` placeholder, never a guess.
5. Voice: aw-brand-voice (calm, specific, warm, signed "Kristine" or "Autumn & Wool"). Match customer language
   (EN/LV/other); if translating, note "[translated, human check]".
6. Output file: `business-os/support-drafts/YYYY-MM-DD-<case>.md` with header: channel, customer first name,
   category, priority, facts used (with source), open questions, `[OWNER DECISION]` items, then the draft.
7. Quality check before handing over: answers the question? no promise of refund/discount/date not approved?
   no invented fact? one clear next step? correct name/order no.? length fits channel?

## 3. Size advice method

- Ask (or use given) body measurements: bust, preferred fit (close / relaxed / oversized), height, usual size
  and a garment they like (lay flat, measure chest width and length).
- Compare to **garment** measurements on the size guide/product page (`/size-guide`; TODO paste table into
  `business-os/size-data.md` once owner confirms). Ease rule of thumb (state as guidance, not fact): close fit
  = garment chest about 0-5 cm over bust; relaxed 8-15 cm; oversized 15+ cm.
- Recommend one size, explain why in one line, mention the alternative if between sizes, and note the return
  option per approved policy.

## 4. Macro library (starter set; fill [ ] from verified facts)

| Macro | Core content |
|---|---|
| SIZE_HELP | ask for bust + fit preference + usual size; or recommend per method above |
| LEAD_TIME | "Made in our Riga studio; dispatch within [verified days] business days; delivery [carrier range]" |
| ORDER_STATUS | "Your order [#] was dispatched on [date] with [carrier], tracking: [link]" / "is being finished, dispatch by [date]" |
| DELAY | apology, reason in one line, new date, options: wait / switch / cancel ([OWNER DECISION] refund) |
| CARE | wool care per supplier advice (hand wash cold / wool cycle, dry flat) — [CHECK per yarn] |
| MATERIAL | composition exactly as on sewn label + supplier spec; no "sustainable/organic/handmade" unless verified |
| RETURN_START | from aw-returns-handling templates |
| DAMAGED | apology, request photos of item + parcel, next step within 1 business day |
| PAYMENT_PAYPAL | PayPal not yet available; card via secure Stripe checkout [update when PayPal live] |
| REVIEW_THANKS | thank by name, mention the specific item/detail they liked, no incentive offers |
| REVIEW_NEGATIVE | thank, own the issue, no argument, offer to fix via email, no admission of legal liability |

## 5. Review replies (public)

Reply to every review within 2 business days. Positive: specific and short. Negative: calm, apologise for the
experience, move to private channel, never disclose order details publicly. Never ask for a review to be changed
or removed in exchange for anything.

## Guardrails

- Never send, post or schedule anything. Never issue refunds, discounts, free shipping or replacements; mark
  `[OWNER DECISION]`.
- Never invent stock, dates, tracking, fibre content, certifications or reviews. Never give legal conclusions.
- Personal data: keep customer data out of filenames beyond first name/case no.; do not copy addresses or
  payment details into drafts unless needed; no data into URLs.
- Allergy/skin reaction, threats, chargebacks, data-deletion requests -> owner, same day.

## Sources

- Anthropic knowledge-work-plugins, customer-support `draft-response` and `ticket-triage` skills
  https://github.com/anthropics/knowledge-work-plugins/tree/main/customer-support — Apache-2.0. Adapted with
  attribution: acknowledge/inform/next-step/close structure, quality-checklist idea (no unauthorised
  commitments, clear next steps, channel-fit length), priority + bump rules, route-by-category. Rewritten for a
  one-person knitwear shop. **Winner**: official, permissive, best structure.
- Compared: claudskills.com "customer-support-reply" https://claudskills.com/skills/customer-support-reply/
  (third-party registry, licence/source unclear; not used), "consensus-support-reply-guard"
  https://claudskills.com/skills/consensus-support-reply-guard/ (risk-gating idea only, own words),
  Plain community note https://www.plain.com/community/using-claude-skills (overview only).
- Store facts: PROJECT-HANDBOOK s.5 (contact copy), README s.2/s.7, `campaign-assets/welcome-email-draft.md`.
