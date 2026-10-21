---
name: aw-email-lifecycle
description: Use when planning or drafting Autumn & Wool email marketing in MailerLite (welcome flow, post-purchase care email, review request, new-drop newsletter, win-back), deciding flow timing/segments, checking consent before any send, or reporting on email and repeat-purchase metrics. Drafts only; nothing is uploaded or sent by the agent.
---

# Email lifecycle flows (MailerLite)

Purpose: turn subscribers and first-time buyers into repeat customers with a few calm, useful emails. Owner
approves and activates. Starting asset: `campaign-assets/welcome-email-draft.md` (status: not uploaded, not
sent; activate only after consent capture, destination list, unsubscribe and sender identity are verified).

## Platform constraints (MailerLite Free, as seen on pricing page Oct 2026 — re-verify)

- 250 active subscribers, 2,500 emails/month; over the limit, sending locks.
- 3 active automations, max 5 steps each; one trigger per automation; **no e-commerce triggers** on Free.
- Squarespace orders are not connected to MailerLite: buyers must be added to a "Customers" group by a human
  (CSV import of buyers who consented, or manual add) to start post-purchase flows. TODO owner decides process.
- Squarespace newsletter block is the current signup point (handbook: newsletter flow works); confirm where
  those contacts land before building flows.

So the plan uses exactly 3 automations + manual campaigns.

## Flow plan

| # | Automation | Trigger | Emails (timing) | Goal | Exit |
|---|---|---|---|---|---|
| A1 | Welcome | joins "Newsletter" group | 1: welcome (immediately, existing draft) -> 2: story from the Riga studio + how garments are made (day 3) -> 3: fit + size guide + care (day 6) -> 4: three priority products from safe-to-promote list (day 10) | first order | buys (removed by human) / unsubscribes |
| A2 | Post-purchase | human adds to "Customers" group at dispatch | 1: thank you + care guide + what to expect (day 0-1) -> 2: fit check "how does it fit?" with reply invitation (delivery + 3 days, ~day 10) -> 3: review request (delivery + 7-14 days, ~day 18) | care, catch problems early, reviews | unsubscribes |
| A3 | Win-back | human adds to "Lapsed" group (no order in TODO days, e.g. 180 for knitwear seasonality) | 1: new-season pieces + note from Kristine -> 2: (4 days later) one bestseller + care/mending tip -> 3: (7 days later) "should we keep writing?" preference/unsubscribe check | second order or list hygiene | buys / clicks preference |
| C | Campaigns (manual) | owner schedules | new drop, seasonal edit, back-in-stock — max ~2/month at this list size | repeat purchase | — |

Products featured in any email must come from the current GREEN list (aw-production-capacity). No discount codes
unless the owner approves margin with aw-unit-economics.

## Per-email draft format (`business-os/email-drafts/<flow>-<n>.md`)

```
Flow / step / trigger + delay / segment:
Subject (<= 45 chars):          Preheader (<= 90 chars):
Body (story 150-300 words; transactional 50-125):
Primary CTA (button text -> URL with UTM: ?utm_source=mailerlite&utm_medium=email&utm_campaign=<flow>_<n>):
Facts used + source:            [CHECK]/[OWNER DECISION] items:
Compliance checks: consent basis, unsubscribe link, sender identity (AUTUMN AND WOOL, SIA + postal address TODO)
```

Copy rules: one email, one job, one CTA. Value before ask. Open with why you are writing; end with one specific
action. No fake "Re:" subjects, no countdown pressure, no "it's not X, it's Y" lines. Voice per aw-brand-voice
("letter from Riga": one news item, one product, one link).

## Review request rules

- Ask all customers equally (no review gating: never ask only happy customers or filter by rating).
- No incentive unless the owner approves AND it is disclosed; never reward positive reviews only.
- Never write, edit or seed reviews. If the site shows reviews, the owner must say how they are collected and
  checked (EU Omnibus rules; adviser to confirm wording).
- Link to the review platform actually in use (TODO: Squarespace has none native; Etsy reviews only for Etsy
  orders; Google review link if Business Profile exists).

## Consent and compliance (not legal advice)

- Marketing emails need prior consent, or the existing-customer "soft opt-in" (similar products, opt-out offered
  at collection and in every email) where Latvian law allows: adviser to confirm before A2 emails 2-3 and A3.
- Every email: unsubscribe link, sender identity, postal address. Keep consent records (date, source form).
- No buyer is added to marketing groups without a recorded consent basis.

## Metrics (monthly, to owner)

Per flow: delivered, open rate (indicative only, privacy protection inflates it), click rate, unsubscribes,
replies, orders attributed (UTM in GA4 sessions + Squarespace order notes; GA4 has no purchase events).
Business KPIs: repeat purchase rate (customers with 2+ orders / customers), review count/rate, list growth vs
250 free cap.

## Guardrails

- Agent never uploads, schedules or sends in MailerLite; never imports contacts. Drafts + plan only.
- Never invent product facts, stock, reviews, discounts or deadlines.
- Respect the frozen product data: links point to existing URLs.

## Sources

- coreyhaines31/marketingskills, `skills/emails/SKILL.md` https://github.com/coreyhaines31/marketingskills —
  MIT. Adapted with attribution: per-email output fields (trigger, timing, subject, preview, body, CTA,
  segment, exit), "one email one job / value before ask / relevance over volume", welcome 5-7 over ~2 weeks
  (shortened to 4 for Free plan limits), re-engagement 3-4 over 2 weeks, length bands, anti-AI-pattern list.
  **Winner**: most mature, permissive, structured.
- Compared: sidchaudhary gtm-skills email-campaign (Klaviyo/Omnisend benchmark claims, unverified; not used),
  hyperfx-ai/marketing-skills email-lifecycle https://skillselion.com/skills/hyperfx-ai/marketing-skills/email-lifecycle
  (small, not used), Klaviyo help "product review flow" https://help.klaviyo.com/hc/en-us/articles/115002779391
  (proprietary; timing idea 7-14 days after delivery), Glaze Digital win-back guide
  https://glazedigital.com/blogs/news/winback-flow-klaviyo-guide (2-3 emails, 3-5 days apart; ideas only).
- MailerLite pricing https://www.mailerlite.com/pricing (limits; re-verify). Omnibus reviews:
  Directive (EU) 2019/2161 summary via HSF https://www.hsfkramer.com/notes/tmt/2020-07/omnibus-directive-a-new-deal-for-eu-consumers-part-3 .
