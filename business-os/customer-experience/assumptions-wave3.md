DRAFT — for owner approval. Nothing here is sent, published or activated.

# Customer Experience assumptions register, wave 3 (ASSUMPTION MODE)

Agent `aw-customer-experience`, 2026-10-21. Owner approved assumption mode on 2026-10-21. **Every value below is an
ASSUMPTION, not a fact.** CX uses the shared registers first and adds an A-CX row only where none of them has the
value. When a shared register changes, the "Used by" tasks are re-run.

Shared registers used (their values win; CX does not restate them as its own):
- GM: `business-os/head-of-ecommerce/assumptions-wave3.md` (A-GM-02 priority 5, A-GM-03 dispatch, A-GM-04 reply time,
  A-GM-10 claims, A-GM-14 MailerLite + consent + review platform, A-GM-16 returns, A-GM-18 shipping, A-GM-22 gift perks,
  A-GM-28 Christmas table publication; conflict ruling W3-1).
- Operations: `business-os/operations/assumptions-wave3.md` (A-OPS-12..24) and `returns-wording-draft-wave3.md` (R1, R2).
- Production: `business-os/knitwear-making/assumptions-wave3.md` (A-PRD-14, A-PRD-22) and `capacity-2026-W43.md`
  (GREEN (A) list).

## Register

| A-ID | Value | Basis | Range | Confidence | Task IDs | Owner confirms by |
|---|---|---|---|---|---|---|
| A-CX-01 | **Christmas made-to-order order-by in customer copy = Ops wave-3 table, recomputed after W3-1 (no CX value of its own).** Sweaters and cardigans (10 wd): LV Fri 4 Dec, EE/LT Thu 3 Dec, EU main zones Thu 19 Nov, US/CA/AU Fri 13 Nov (not guaranteed). Beanie / hat & scarf set (5 wd): LV Fri 11 Dec, EE/LT Thu 10 Dec, EU Thu 26 Nov, US/CA/AU Mon 23 Nov (not guaranteed). Orders before 12:00 Riga | A-OPS-16..19 and `operations/christmas-cutoffs-2026.md` wave-3 section (re-read 21 Oct after orchestrator update); EU = Production A-PRD-22 (earlier date wins, W3-1). CX row exists only to record **one CX choice: the per-zone dates, not a single stop**, in customer copy | If the owner rejects the local LV/Baltic stop (Ops: owner decision), LV and EE/LT fall back to 19 Nov / 26 Nov | L | CX-10, CX-25 | 20 Nov (A-GM-28, decision 33) |
| A-CX-02 | **In-stock Christmas order-by in customer copy** = Ops wave-3 values unchanged: LV Wed 16 Dec, EE/LT Tue 15 Dec, EU main zones Mon 7 Dec; US/CA/AU "Christmas delivery not guaranteed" (best chance: order in-stock pieces by Thu 26 Nov); Rest of World and remote EU zones: no date | A-OPS-16..20, ruling C3. Only for units the owner has physically confirmed (Ops rule 3); assumed stock (A-PRD-12) is not enough to quote "in stock" to a customer | as Ops | L-M | CX-10, CX-25 | 20 Nov |
| A-CX-03 | **After-cutoff message: no gift card.** Copy says the piece may arrive after Christmas and offers a gift note with the delivery date | A-GM-22 "digital gift card: not assumed to exist" (GM wins). Conflict: Ops `christmas-cutoffs-2026.md` and SEO pin drafts use a gift-card fallback | gift card exists -> swap one line | M | CX-10, CX-25 | 20 Nov (owner-inputs-wave2 #16) |
| A-CX-04 | **December "where is my order" chase threshold:** if tracking has not moved or the parcel has not arrived by the upper transit bound (A-OPS-14: LV 3, EE/LT 4, EU 8, US/CA/AU 20 working days) **+ 3 working days**, CX drafts a carrier chase. Customer copy says "December post is busy, so it can take a few extra days" (no number) | No register gives a December delay figure. A-OPS-09 is a price surcharge, not a delay. +3 wd = ORDER_STATUS macro rule already in v1 | +2 to +5 wd | L | CX-25 | 14 Nov (OPS carrier-backed table) |
| A-CX-05 | **Welcome W4 line-up = Production GREEN (A) list W43:** 1 Women's Classic Lambswool Crew (EUR 136), 2 Merino Raglan Sweater, Dusty Pink (EUR 155), 3 Merino Wool Hat & Scarf Set, **Black** (EUR 110). Alternate: Rib-Knit Beanie, photographed colour only (EUR 45) | `capacity-2026-W43.md` "Safe to promote": these four are the only GREEN (A) SKUs; P1 Raglan Cardigan is AMBER (thin CM2, Blue unphotographed) so it leaves W4. Prices A-GM-02 (17 Oct export). Re-check the GREEN list the week the flow goes live | swap any SKU that drops to AMBER/RED | L | CX-14 | 24 Oct (A-GM-02) + live week |
| A-CX-06 | **Review request P3 = "reply by email"**, no public platform link in Q4; replies are not published anywhere without the customer's and owner's yes | A-GM-14 "Review platform: none in Q4. Post-purchase P3 asks for a reply by email" | platform chosen later -> add link | M | CX-23 | 14 Nov (decision 30) |
| A-CX-07 | **Lead-time wording in macros:** in stock "dispatched within 2-5 working days"; made to order "dispatched within 10 working days" (sweaters, cardigans) / "5 working days" (beanie, hat & scarf set); delivery after dispatch LV 1-3, EE/LT 2-4, other EU 3-8, US/CA/AU 7-20 working days, estimates | A-GM-03 (incl. W3-1) + A-OPS-14; matches Ops `returns-wording-draft-wave3.md` s.A (updated by Ops 21 Oct) | MTO garments 7-15 wd | L | CX-10, CX-25, CX-06 macro 2 | 24 Oct (decision 3) |

Nothing assumed, ever (stays BLOCKED or `[VERIFY]`): garment measurements (CX-08), fibre percentages, certifications,
"hand-knitted", stock counts quoted to a customer, Kristine's own words, the return address, the footer postal
address, PayPal status, consent basis as a legal conclusion.

## Consent baseline used in drafts (CX-19 stays BLOCKED)

Recorded for planning only, from A-GM-14 (strictest reading until the adviser answers, G9). Not a legal reading.

| Audience | Basis assumed for drafting | Goes into a marketing group? |
|---|---|---|
| Newsletter sign-ups (site form) | consent via sign-up form | yes (A1 welcome) |
| Site buyers who did not sign up | none assumed (no soft opt-in) | no; P1 only if the adviser calls it a service email |
| Etsy buyers | none | no |
| Market sign-ups (paper/QR) | consent only if the form wording is approved | only after approval |

## CX-20 reply-promise sweep (A-GM-04: "We reply within 1-2 business days")

| Place | Wording now | Matches? |
|---|---|---|
| `support-macros.md` facts table | "We usually reply within 1-2 business days" | yes |
| `email-drafts/welcome.md` W1 | "I usually reply within 1-2 business days" | yes |
| `faq-proposals.md` P1 | proposes 1-2 business days everywhere | yes |
| `email-drafts/flow-plan.md` checklist 6 | 1-2 business days | yes |
| `cx-weekly-template.md`, `cx-weekly-2026-W44.md` | 1-2 business days public, 24 h internal | yes |
| Live FAQ, Shipping & Returns | 1-2 business days | yes |
| Live Contact page | "within 24 hours" | **no: CRO proposal to change; the owner applies it** |
| `campaign-assets/welcome-email-draft.md` (original) | 1-2 business days | yes (file not edited by CX) |

Internal target unchanged: CX drafts the same business day, owner sends within 24 h where possible.

## Conflicts found (for GM / Ops)

| # | Conflict | CX handling |
|---|---|---|
| CX-W3-a | MTO dispatch 5 wd vs 10 wd garments | Resolved 21 Oct: Ops updated its draft to 10 / 5 (W3-1) |
| CX-W3-b | Christmas MTO order-by on 5 wd | Resolved 21 Oct: Ops recomputed (A-OPS-16..19); CX uses Ops' values |
| CX-W3-c | Gift-card fallback (Ops, SEO pins) vs A-GM-22 "no gift card assumed" | CX uses no gift card (A-CX-03) |
| CX-W3-d | SEO pin/PDP drafts say the hat & scarf set "ships in gift packaging" vs A-GM-22 "gift wrap: no" | CX never says gift packaging; flag to SEO/CRO |
| CX-W3-e | Dusty Pink raglan URL slug contains "hand-knitted" (product data frozen) | W4 shows the product name without "Hand-Knitted"; slug change is an SEO/CRO proposal for the owner |
