# CRO prepared drafts for later tasks — 2026-10-21 (wave 2) — DRAFT

Owner: aw-ecommerce-cro. Pre-drafts for tasks that cannot finish today (owner inputs, OPS/FIN gates, or future
dates). Every date, cost or count left open is a placeholder; nothing here is published or applied.
Owner inputs for all of these: `owner-inputs-wave2.md`.

---

## 1. CRO-20 — Weekly site-improvement note #1, Fri 24 Oct (skeleton; finish on 24 Oct)

File on the day: `business-os/ecommerce-cro/2026-10-24-weekly.md`.

```
# CRO weekly note #1 — week starting 2026-10-19 — DRAFT
## 1. Changes applied by the owner this week
- [OWNER: list, with date] (CRO saw on 21 Oct: Contact page text now says "reply within 1–2 business days";
  who/when changed: [OWNER: confirm])
- Overlay CSS still present? [form item 4 answer]
## 2. Numbers (before -> this week)
| Metric | Baseline (note #0) | This week | Source |
| Sessions | 62 / 30 d to 17 Oct | [OWNER/GA4: 19–25 Oct] | GA4 or Squarespace Analytics |
| Real orders | 0 | [OWNER: Squarespace Orders] | Orders (exclude tests) |
| Conversion rate | n/a | [orders / sessions, blank if 0 orders] | kpi-weekly.csv rule |
| AOV | n/a | [blank if 0 orders] | |
| Abandoned checkouts | TODO | [OWNER: count] | Squarespace abandoned carts |
| Merchant Center approved | 0 (19 Oct) | [OWNER screenshot] | MC Diagnostics |
| Priority PDPs passing checklist | 0 of 5 | [count] | this folder |
## 3. Next 3 proposals (ICE order)
1. Restore/confirm overlay CSS (CSS, urgent if missing) — wave2-updates s3b
2. Delivery line v2 on the 5 priority PDPs (COPY) — wave2-updates s2
3. Raglan cardigan copy (COPY, EXP-01) or PayPal connect (NATIVE, EXP-02), whichever the owner can do first
## 4. Experiment log (EXP-01 cardigan copy, EXP-02 PayPal, EXP-03 crew sweater copy: status + dates)
## 5. kpi-weekly.csv notes suggestion (owner/FIN append, ruling C16)
"[changes applied + dates]. Test orders excluded. No split tests."
```
Rule: if 0 orders, write "no conversion read" rather than a rate; never a % lift from fewer than 5 orders.

---

## 2. CRO-25 — Christmas order-by banner and Shipping block (copy ready; dates blocked)

Supersedes the template in `2026-10-21-css-native-proposals.md` (that one named the UK; OPS-12 gap 3 removes
UK/NO/CH until priced). Dates come only from the OPS carrier-backed table (OPS-09, 14 Nov) after owner approval
(20 Nov, ruling C3). OPS-08 provisional worst-case dates are shown for sizing only and **must not be published**.

| Region | Placeholder | OPS-08 provisional (internal, MTO / in-stock, deliver 23 Dec) |
|---|---|---|
| Latvia | [OPS-09 date LV] | Wed 9 Dec / Tue 15 Dec |
| EU | [OPS-09 date EU] | Wed 2 Dec / Tue 8 Dec |
| US, Canada, Australia | "not guaranteed" unless paid express (decision 21) | MTO date falls before publication (17–19 Nov) |

Announcement bar (one line, phone-safe; pick A if in-stock and MTO dates are close, else B):
- A: `Christmas delivery: order by [LV date] in Latvia, [EU date] in the EU. Details in Shipping.`
- B: `Christmas: order in-stock pieces by [EU date] (EU). Made-to-order colours by [EU MTO date].`

FAQ / Shipping & Returns block:
> **Ordering a gift?** For delivery before Christmas, order by [LV date] in Latvia and by [EU date] elsewhere in
> the EU. Made-to-order colours need [PRD: X] extra working days, so order those by [MTO date]. We cannot
> guarantee Christmas delivery to the US, Canada or Australia. After these dates, [gift-card line if the owner
> offers one, else delete this sentence].

PDP line (priority 5 only, under the delivery line): `Christmas: order by [EU date] for EU delivery before 24 Dec.`

Rules: no countdown, no "last chance", no exclamation marks; the earliest regional date governs the PDP line;
remove everything on 25 Dec; if OPS has no carrier data by 14 Nov, publish the OPS worst-case dates only after owner
approval. Owner applies via Announcement Bar (native) and page text; no script needed.

---

## 3. CRO-26 — Gift options (proposal skeleton; blocked on FIN-19 cost check + owner decision 31)

What exists today: hat & scarf set and beanie ship in kraft packaging (live PDP text). FAQ has no gift answer
(CX proposed one in `customer-experience/faq-proposals.md`). No gift wrap, note or receipt is promised anywhere.

| Option | How on Squarespace (no script) | Cost input for FIN | Copy if approved | Recommendation |
|---|---|---|---|---|
| G1 Gift note | Custom checkout form field "Gift message (optional)" [VERIFY available on current plan] | Card + printing per order [FIN/OPS: EUR] | "Add a short gift note at checkout; we handwrite it on a card [VERIFY: handwritten or printed]." | Lowest cost, do first if FIN agrees |
| G2 Price-free packing slip | Owner prints packing slip without prices, or leaves it out [VERIFY Squarespace packing-slip options] | EUR 0 | "Sending it as a gift? Use the recipient's address; we do not put prices in the parcel." | Only if OPS can do it reliably every order |
| G3 Gift wrap | Separate EUR [X] product "Gift wrap" added to cart, or free | Wrap materials + minutes [PRD/OPS] vs CM2 (FIN-03) | "Gift wrap: [description of real material]" | Hold until CM2 known; kraft packaging already exists |
| G4 Gift exchange after Christmas | Policy text only | Returns allowance (CM2) | Needs adviser (G9) | Do not draft wording until adviser |

Owner decides (form item 16); FIN checks margin (FIN-19). CX macro GIFT (CX-10) and Creative posts reuse the same
wording, so one approved line per option is enough.

---

## 4. CRO-28 — Site-change freeze from 12 Dec + defect-watch 12–24 Dec (checklist; run from 12 Dec)

Freeze rule: from Sat 12 Dec to Thu 24 Dec no CSS, navigation, template or product-structure changes. Allowed: stock
counts, sold-out toggles, Christmas banner date swap, fixing a defect found by the watch below.

Before freeze (owner, by Fri 11 Dec):
- [ ] Overlay CSS lines present (Custom CSS, search `confirmation`)
- [ ] Christmas banner + Shipping block live with approved dates
- [ ] December test order (CRO-29) done and refunded
- [ ] Sold-out variants set to 0 stock (feed availability follows)

Defect watch (owner, 5 min, Mon / Wed / Fri 14–23 Dec, phone):
| Check | How | Pass |
|---|---|---|
| ATC works | Beanie: pick a colour, add to cart; then tap ATC without a colour and confirm the page still responds | Item in cart; page clickable |
| Cart -> checkout | Open cart, press Checkout, stop at the payment step (do not pay) | Checkout loads, totals right, shipping EUR 0 |
| Banner | Dates match the approved table | Yes |
| Orders | Squarespace Orders: any in-stock order unfulfilled after 5 working days (dispatch promise) | None |
| Messages | Contact form test or inbox check | Reply within 1–2 business days |
Record each run in the weekly note; a FAIL is the only reason to change the site during the freeze.

---

## 5. CRO-29 — December test order + refund (owner; run by 15 Dec)

Reuse `2026-10-21-test-order-checklist-november.md` run R2 only (phone, card or Google Pay, one sized garment
size M + beanie, Latvia), plus a PayPal run if PayPal failed or was not live in November.
Add these December checks:
- [ ] Christmas banner and Shipping block visible on the phone, dates match the approved table
- [ ] Order email shows the correct delivery wording (no promise beyond the approved line)
- [ ] Refund the same day; mark the order "test, excluded" for FIN (as #00003/#00004)
Record in section D of the November checklist (new row R2-Dec).

---

## 6. CRO-30 — Q4 retrospective (template; fill on 31 Dec)

| Metric / item | Before (source, date) | After (31 Dec) | Change applied (date) | Read |
|---|---|---|---|---|
| Sessions / week | 62 per 30 d to 17 Oct (handbook s7) | | | |
| Real orders (site) | 0 (to 21 Oct) | | | |
| Conversion rate | n/a | | | no % if < 5 orders |
| AOV | n/a | | | |
| Abandoned checkouts / week | TODO (owner) | | | |
| Priority PDPs passing checklist | 0 of 5 | | | |
| PDPs with delivery line v2 | 0 of 22 | | | |
| PayPal live | No | | | |
| Merchant Center approved | 0 of 98 (19 Oct) | | | |
| Variant-image mismatch feed rows | 46 (CRO-01) | | | |
| Monthly test orders run | 0 | | | target Nov + Dec |
| EXP-01/02/03 | — | | | qualitative |
Sections after the table: what worked, what did not, defects found in freeze, 3 inputs for the Q1 plan.

---

## 7. 2027 quarters — preparation notes (CRO-31 to CRO-34; nothing to draft in detail yet)

| Task | Gate before work can start | Already prepared |
|---|---|---|
| CRO-31 Q1 | Plan-upgrade decision (decision 24, 4 Nov); adviser returns wording (G9); dedupe (decision 20) | One PDP template = size-fit standard + delivery line v2 + copy structure; colour-twin opening lines in SEO on-page proposals; category intros are SEO's (aw-ecommerce-seo) |
| CRO-32 Q2 | Q1 conversion read; costs (G1) for bundles/threshold (aw-unit-economics) | Feed QA method (CRO-01) for monthly refresh |
| CRO-33 Q3 | ~1,000 sessions/week for any A/B; review platform (CX-23) | Hiring trigger 3 in GM hiring-triggers file |
| CRO-34 Q4 2027 | OPS cutoffs by 1 Oct 2027 | Sections 2–6 of this file are reusable |
