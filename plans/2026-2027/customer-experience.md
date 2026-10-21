DRAFT — for owner approval. Nothing here is sent, uploaded, scheduled or promised to customers.

# Customer Experience & CRM plan: Q4 2026 and 2027 by quarter

Author: aw-customer-experience agent. Date: 2026-10-21. Scope: support, FAQ/size macros, returns handling,
MailerLite flows (welcome, post-purchase, review request, win-back), repeat purchase.
Targets are proposals. Anything marked TODO has no source yet and is not guessed.

## 1. Starting point (facts, with source)

| Fact | Source |
|---|---|
| Zero real direct orders to date. Payments: Stripe proven with test orders only. PayPal NOT connected. | `business-os/README.md` s2 |
| Traffic: 64 visits in 30 days, 2 from Google, 0 from Instagram/Pinterest. Zero orders is the expected result at that volume. | `zero-sales-diagnosis-2026-10-18.md` s1 |
| `kpi-weekly.csv` has a header row and no data. No baseline for repeat rate, replies or CSAT exists. | `business-os/kpi-weekly.csv` |
| GA4 has no ecommerce events. Orders must be counted from Squarespace Orders (and Etsy). | `business-os/README.md` s2, s9 |
| Marketplace proof: Etsy/Mareshop, ~8.2k sales, ~1.5k reviews, 4.9 stars, 15 years. Not direct-store sales. Site strip says 1,400+, owner pack suggests 1,500+. | `business-os/README.md` s2; `owner-action-pack-2026-10-19.md` D |
| Contact page promises reply within 24 h. Welcome draft says "1-2 business days". Conflict is unresolved. | `PROJECT-HANDBOOK.md` s5; `campaign-assets/welcome-email-draft.md`; `business-os/ai-team.md` decision 5 |
| Welcome email: 1 draft, plain, not uploaded or sent. Consent capture, destination list, unsubscribe and sender identity unverified. Links to `/shop` and `/size-guide` have no UTM. | `campaign-assets/welcome-email-draft.md` |
| Newsletter, contact and account flows "work". Abandoned-cart email is reported live. Where newsletter contacts land is unconfirmed. | `PROJECT-HANDBOOK.md` s6; `GROWTH-PLAN-100-IDEAS.md` s1, idea 75 |
| MailerLite Free (verify): 250 subscribers, 2,500 emails/month, 3 automations of up to 5 steps, no ecommerce triggers. Buyers must be added to groups by hand. | `business-os/README.md` s8; `.claude/skills/aw-email-lifecycle/SKILL.md` |
| Live returns policy conflicts with EU rules as summarised: sale and made-to-order exclusions, shipping not refunded, 5-day defect window. Adviser review pending. Wording also differs ("unworn, unused" vs "unworn, unwashed"). | `business-os/README.md` s11; `zero-sales-diagnosis-2026-10-18.md` A6 |
| Size data: no size table in files (`size-data.md` TODO). Garments have no size selector and measurements are inconsistent (cm vs cm+in). | `zero-sales-diagnosis-2026-10-18.md` A4; `aw-support-replies` skill s3 |
| Missing ops data: return address, carriers, labour and lead times, review platform. | `business-os/ai-team.md` decision 8 |
| Deliverables to date: skills exist (support, returns, email). No macro library, flow drafts (only welcome email 1 of 4), returns log or weekly CX file exist yet. | repo listing; `business-os/ai-team.md` |
| Season: Christmas markets and gift guides run now. Market stalls would create offline-to-email contacts and in-person size questions. | `markets-and-gift-guides.md`; `GROWTH-PLAN-100-IDEAS.md` s1 |

Implication: Q4 CX is about being ready for the first direct orders (and gift questions), not about volume.
Repeat-purchase work cannot be measured until real direct customers exist.

## 2. Q4 2026 (21 Oct to 31 Dec): "ready for the first customers"

### Goals
1. Every inbound answered with a human-approved draft inside 24 h, size questions same day.
2. Macro library and returns process ready before the first gift-season order.
3. Welcome flow and a minimal post-purchase flow live (owner-activated) with a recorded consent basis.
4. A clean, measured baseline for 2027 (first reply time, first reviews, first repeat data).

### KPIs and targets
No direct-order baseline exists, so targets are process targets. Volume targets are TODO until 4 weeks of data.

| KPI | Definition | Q4 target | Source of truth |
|---|---|---|---|
| First-reply draft ready | Within business hours of receipt, owner sends < 24 h | 100% of inbound; report actual median | Support drafts folder, owner send times |
| Size questions | Draft same day | 100% | Same |
| P1 cases (order issue, return, sensitive) | Draft within 4 business hours; owner told same day | 100% | Same |
| Public review replies | Within 2 business days | 100% of reviews that exist | Owner |
| Macro library | `business-os/support-macros.md` with 11 starter macros filled from verified facts | Done by 14 Nov | File |
| Flow drafts | Welcome 4, post-purchase 3, win-back 3 in `business-os/email-drafts/` | Welcome + post-purchase by 14 Nov, win-back by 30 Nov | Files |
| Welcome flow live | Owner-activated after checks s5 | By 28 Nov (before Black Friday week), if owner decides in time | MailerLite (owner) |
| Returns log | `returns-log.csv` created, every case logged with computed deadlines | 100% of cases | File |
| Subscribers vs Free cap | Active subscribers / 250 | Report weekly; alert at 200 | MailerLite (owner) |
| Repeat purchase rate | Customers with 2+ orders / customers | Not measured in Q4 (too few customers). Record the first value in Jan | `kpi-weekly.csv` |
| Review rate | Reviews received / orders delivered | Record only; no target until 10+ delivered orders | Review platform TODO |

### Weekly actions (agent drafts, owner sends)
- Daily batch: triage new inbound, draft replies to `business-os/support-drafts/YYYY-MM-DD-<case>.md`.
- Mon: CX summary `business-os/cx-weekly-YYYY-Www.md` (volume by category, median response time, open cases, top
  questions turned into FAQ/PDP proposals). Feeds Monday review (`kpi-weekly.csv` replies and repeat columns).
- Fri: open returns and deadline check; list of cases awaiting owner decision.
- Escalate same day to owner: threats, chargebacks, allergy or skin reports, data-deletion requests.

### Monthly actions
| When | Action |
|---|---|
| Nov (wk 1-2) | Macro library v1: SIZE_HELP, LEAD_TIME, ORDER_STATUS, DELAY, CARE, MATERIAL, RETURN_START, DAMAGED, PAYMENT_PAYPAL, REVIEW_THANKS, REVIEW_NEGATIVE. Add GIFT (gift note, last order date, gift receipt) once Ops confirms |
| Nov (wk 1-2) | Fix welcome draft: one reply promise (owner picks 24 h or 1-2 business days), UTM on links, sender identity and unsubscribe check, sign as Kristine. Draft emails 2-4 (story, fit+size+care, 3 GREEN products) |
| Nov | Post-purchase 3 emails (care + what to expect; fit check; review request) and win-back 3 drafts. Win-back stays unused until a lapsed segment exists |
| Nov | Propose FAQ/PDP edits from the first 2 weeks of questions (delivery time, sizing, returns wording). Proposals only, product data stays frozen |
| Dec | Christmas-deadline reply macro (last order dates per zone from Operations). Gift-season "where is my order" macro. No new flows after 10 Dec |
| 31 Dec | `business-os/crm-monthly-2026-12.md`: first email and retention report, 2027 Q1 campaign drafts |

### Rules for Q4 emails
- Features only from the current GREEN list (Production). No discount codes unless owner approves margin.
- No review gating, no incentivised reviews, no invented or paraphrased quotes. Etsy quotes only with owner OK, verbatim, labelled "Etsy review".
- Market-stall or in-person signups: consent must be recorded (date, source) before any contact goes into MailerLite.
- Volume stays under 2 manual campaigns per month at this list size.

## 3. 2027 by quarter

Budget baseline: MailerLite Free, EUR 0. Illustrative whole-company cap EUR 100-250/month for tools is set in
`business-os/README.md` s8 (not a CX-specific allocation). Hiring: the CX role is currently covered by agent
drafts plus the owner. Any hire is TODO and only after order volume justifies it (`business-os/hiring-plan.md`).

### Q1 2027 (Jan-Mar): measure and fix
| Item | Plan |
|---|---|
| Goals | Establish real baselines. Close the gaps found in Q4 cases. Recover post-Christmas returns and exchanges well |
| KPIs | Reply < 24 h at 100%; size-query reply same day at 100%; return rate by reason, SIZE_* share (record, set target after 20+ orders); first repeat purchase rate recorded; welcome flow: record clicks and unsubscribes |
| Initiatives | January returns/exchange surge handling with the returns log and weekly SIZE_* clusters; publish revised returns wording only after adviser sign-off; size-chart-based macro, using `size-data.md` once owner confirms the table; first review request wave; post-Christmas "how does it fit" emails; January campaign (care, no sale pressure); decide whether to buy a MailerLite paid plan if subscribers near 250 |
| Budget ask | MailerLite paid tier only if subscribers exceed 200 (price: TODO verify); adviser fee for consent and returns wording (TODO, one-off, owned by Finance/GM) |

### Q2 2027 (Apr-Jun): reviews and post-purchase
| Item | Plan |
|---|---|
| Goals | Review collection works on a platform the owner chose. Post-purchase flow is stable. Early repeat signal |
| KPIs | Review request sent to 100% of delivered orders (no gating); review rate recorded, target set in April from Q1 data (TODO); post-purchase flow open and click rates indicative only; reply time unchanged |
| Initiatives | Review platform decision implemented (Google Business Profile, Trustpilot, on-site; adviser confirms Omnibus-compliant wording); owner reply to every review in 2 business days; care and mending content as emails (cheap, useful); spring light-knit campaign from GREEN list; first win-back test only if there are lapsed customers with consent |
| Budget ask | Review tool: free tier first, paid TODO. Optional AI-translated Latvian macros with native check (cost TODO) |

### Q3 2027 (Jul-Sep): pre-season build
| Item | Plan |
|---|---|
| Goals | Pre-sell autumn without discount pressure. Make the 2027 gift season support-ready by September |
| KPIs | Repeat purchase rate vs Q1 baseline (target set after 2 quarters of data, TODO); win-back flow: reactivation rate recorded; unsubscribe rate watched; Christmas macros and last-order dates approved by 15 Sep |
| Initiatives | Back-in-stock and new-season lists (opt-in only); first win-back (180 days is a proposal from the skill, owner to confirm); segment by country for Christmas deadlines; refresh the macro library with a year of questions; FAQ and size guide updates from top-10 questions |
| Budget ask | Higher MailerLite tier if list > 250 (TODO price); possibly ecommerce integration if the Squarespace plan upgrade happens (see s4) |

### Q4 2027 (Oct-Dec): gift season with data
| Item | Plan |
|---|---|
| Goals | Hit the 24 h reply promise at peak volume. Convert gift buyers into subscribers. Leave 2028 with a full-year retention report |
| KPIs | Reply < 24 h at peak (target: stay at 100% or report why not); gift-related questions answered same day; delivery-deadline emails sent to 100% of active subscribers in time; yearly repeat purchase rate (first full year); review rate vs Q2 |
| Initiatives | Gift campaigns using GREEN items and Ops last-order dates; gift-related macros; post-Christmas exchange process ready; annual `crm-annual-2027` summary; decide on a part-time support helper if replies slip (TODO, owner decision) |
| Budget ask | Seasonal help for replies if volume demands (TODO). Everything else carries over |

## 4. Dependencies on other departments

| Needs from | What | By when |
|---|---|---|
| Owner | Reply-time promise (24 h or 1-2 business days); consent basis per audience; MailerLite signup and activation; where newsletter contacts land | Before 14 Nov |
| Operations | Dispatch log, returns log, return address, carriers and delivery ranges, Christmas last-order dates, tracking emails | Return address and last-order dates by 15 Nov |
| Production | Weekly capacity and GREEN list for email features; lead time for LEAD_TIME macro; fibre and care wording per yarn (CARE, MATERIAL macros) | Weekly; care wording by 14 Nov |
| E-commerce / CRO | PayPal live (PAYMENT_PAYPAL macro changes); delivery times on PDPs; size data on PDPs; review display; Squarespace plan decision (Code Injection unlocks GA4 events); newsletter form destination | PayPal and sizes before Black Friday if possible |
| Growth / SEO | UTM naming (`utm_source=mailerlite&utm_medium=email&utm_campaign=<flow>_<n>`); top questions for FAQ and Pinterest content | Nov |
| Finance / GM | Margin check before any discount or free exchange offer; MailerLite spend; adviser budget | As needed |
| Legal adviser | Consent basis and soft opt-in, returns wording, review rules (Omnibus), data-deletion process | Before post-purchase emails 2-3 and win-back go live |
| Creative | Real photos per colour for email images; Kristine's story and studio photos for welcome email 2 | Nov |

## 5. Risks and owner decisions

### Risks
| Risk | Effect | Mitigation |
|---|---|---|
| Very low traffic, so few customers | Flows run on almost no data. Repeat rate not measurable in 2026 | Process KPIs now; targets set from real data in Q1-Q2 |
| Consent basis unclear for buyers or Etsy customers | Legal exposure, spam complaints | No contact added without recorded basis; Etsy rules apply (idea 78); adviser confirms |
| Free plan cap (250 subs, 3 automations) | Sending locks | Weekly count; alert at 200; plan to upgrade by Q1 if growth works |
| Manual buyer-to-group step | Post-purchase emails late or missed | Owner adds buyers at dispatch; weekly check of orders vs group; consider integration later |
| Returns policy still conflicts with EU rules | Wrong refusals, PTAC complaints | Replies follow statutory floor case by case; owner decides; never quote the 5-day clause |
| Reply promise missed during markets or holidays | Bad reviews | Owner sets out-of-office wording; drafts prepared in batches; 24 h only if the owner can send |
| Gift deadlines not clear | Late deliveries, complaints | Ops last-order dates published before 15 Nov |
| Missing size table | Wrong size advice, returns | No advice without garment measurements; `[CHECK]` placeholders |
| Review claims | Trust and legal issues | No invented or gated reviews; Etsy quotes only with owner OK |
| Personal data in drafts | Privacy exposure | First name and case number only; no addresses in files |

### Owner decisions needed (all pending)
1. Reply promise: 24 h or 1-2 business days; align Contact page, welcome email and macros. By 14 Nov.
2. MailerLite: approve account, list destination, sender identity (AUTUMN AND WOOL, SIA, postal address TODO), unsubscribe.
3. Consent basis per audience (newsletter signups, buyers, market visitors, Etsy past buyers). Adviser to confirm.
4. Process for adding buyers to the Customers group at dispatch (who, when).
5. Return address, who pays return postage, and approval path for refunds, exchanges, goodwill. Adviser review of the policy.
6. Review platform and how reviews are displayed. Permission to use verbatim Etsy quotes.
7. Whether to offer any gift-season perk (free exchange, gift wrap, discount). Needs Finance margin check.
8. Size table: owner confirms garment measurements for `size-data.md`.
9. Squarespace plan upgrade (events, Code Injection) and, later, an email integration.
10. Whether and when to add support help in 2027 (hire or part-time). TODO budget.
