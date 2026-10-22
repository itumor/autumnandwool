# CRO wave 2 updates — 2026-10-21 — DRAFT for owner approval

Owner: aw-ecommerce-cro. Inputs used from wave 1 of other departments:
`head-of-ecommerce/priority-5-sku-proposal-2026-10-21.md` (GM 5), `operations/delivery-promise-reconciliation.md`
(OPS-12), `operations/christmas-cutoffs-2026.md` (OPS-08, provisional), `customer-experience/faq-proposals.md`,
`head-of-ecommerce/owner-decision-pack-2026-10-24.md` / `-10-31.md`. Live pages read with WebFetch on 21 Oct
(text only; no JS, no overlays, no variant images). Nothing on the store was changed. Product data stays frozen.
Owner questions are collected in one form: `owner-inputs-wave2.md`.

## 1. Priority set aligned with the GM proposal

The GM's provisional 5 differ from CRO's wave-1 set in one place:

| # | GM 5 (decision 2, 24 Oct) | CRO wave-1 work | Gap closed in wave 2 |
|---|---|---|---|
| 1 | Merino Wool Raglan Cardigan | audit + copy (s1 of pdp-copy-proposals) | — |
| 2 | Merino Raglan Sweater, Dusty Pink | audit + copy (s5) | — |
| 3 | **Women's Classic Lambswool Crew Sweater** | not covered | **Audit + copy below (s4) and CSV rows** |
| 4 | Merino Wool Hat & Scarf Set | audit + copy (s3) | — |
| 5 | Rib-Knit Beanie | audit + copy (s2) | — |
| alt | Long shawl cardigan (`69105a2903d8`, "100% Wool Long Shawl Cardigan – Warm Knit") | CRO s4 covered the *twin* `69105a2ab0c4` ("Long Wool Cardigan — Women's Shawl Collar") | Note: if the alternate is swapped in, the audit must be redone on `69105a2903d8`, not the twin. Owner dedupe (decision 20) decides which listing survives |

The GM's open item for the crew sweater ("Garment measurements in cm not found in description [VERIFY CRO]") is
answered: **the live PDP has a full cm table per size** (the 17 Oct export is older than the live page). See s4.

## 2. Shared PDP delivery line v2 (replaces CRO-06 v1; reconciled with OPS-12)

OPS-12 s3 sets the interim single source of truth (only ranges already submitted to Merchant Center). CRO copies
it unchanged, in brand-voice form, and uses "working days" for every region (OPS gap 4).

```
- Free shipping. In-stock items ship from Riga within 2–5 working days. 14-day returns.        (live, 5 of 6 PDPs)
- Free shipping to eligible destinations. In-stock items leave Riga in 2–5 working days; delivery takes about
- 5–10 working days in Europe and 7–20 days to the US, Canada and Australia. 14-day returns ...  (CRO v1, withdrawn)
+ Free shipping to eligible destinations. In-stock items leave Riga in 2–5 working days. Delivery after that:
+ Latvia 2–5, EU 5–10, USA, Canada and Australia 7–20 working days. 14-day returns, see Shipping & Returns.
```
Made-to-order variant (only on PDPs with made-to-order colours/sizes), unchanged from v1:
`+ Made to order: leaves Riga within [OWNER/PRD: X] working days, then the delivery times above.`

Rules: same sentence on all 22 visible PDPs, FAQ and Shipping & Returns (the two pages need "working days" added to
US/CA/AU and a Latvia row, s3). No UK/NO/CH, no Estonia/Lithuania-specific time until OPS has carrier data (OPS gaps
1, 3). Revisit after the OPS dry run (6 Nov) and carrier rates (14 Nov). Owner approves (form item 14).

## 3. Live policy re-check (OPS-12 gap 5, CX P1/P9), WebFetch 21 Oct

| Page | Finding | Status |
|---|---|---|
| /contact | Page text: "Write to us — we reply within 1–2 business days." | Text conflict with FAQ resolved in HTML. **UNVERIFIED:** the CSS-rendered "24 hours" line (handbook s5.5, proposal P3) cannot be seen by WebFetch. Owner screenshot at 390px still needed |
| /faq | Dispatch "2–5 working days"; Europe "about 5–10 working days"; "USA, Canada and Australia: 7–20 days" (unit missing); no Latvia time; cards only, no PayPal mention; no gift-wrap/gift-note answer | OPS gap 4 open; Latvia row missing |
| /faq | "Made-to-order items ship within the time shown on the product page." No PDP fetched shows a lead time in days (raglan cardigan only says Brown/Blue are "to order") | **Contradiction** — fix with the MTO line in s2 once PRD/owner give the days |
| /shipping-returns | Leaves Riga "2–5 days" (working, in-stock); Europe 5–10 working; US/CA/AU "7–20 days"; "Delivery times are estimates, not guarantees"; Latvia no time | Same gaps as FAQ |
| /shipping-returns | "Custom or made-to-order pieces" are non-returnable; FAQ returns answer does not mention this exclusion | Two returns statements differ; final wording waits for adviser (G9). CRO C4 interim sentence still stands |
| both | The older "1–2 business days dispatch / 2–4 days EU" version (OPS gap 5) is **not** on FAQ or Shipping & Returns | OPS gap 5 closed for these two pages |

## 3b. Overlay click-trap CSS — public stylesheet scan (CRO-22 evidence, not a pass)

The live Custom CSS is served inside the public `/site.css` (1.3 M characters). Owner custom rules were seen near the
end of the file (e.g. `a.sqs-block-button-element[href="/size-guide"]`, `form.aw-f>button[type="submit"]`). Three
WebFetch passes over characters 1,100,000 to the end found **no** `sqs-widgets-confirmation` selector.
WebFetch reads the file in 100 k chunks through a summarising model, so this is not proof of absence; it is enough to
raise the check to **urgent**. The handbook s4 rules that must be present:
```css
.sqs-widgets-confirmation-overlay{pointer-events:none !important;}
.sqs-widgets-confirmation{pointer-events:none !important;}
```
Owner: Design → Custom CSS, Ctrl/Cmd+F `confirmation`. If the two lines are missing, paste them back at the end
(rollback: none needed, they only restore the 19 Oct fix) and send a screenshot (form item 4). Without them, any
failed Add-To-Cart makes the page unclickable (the root cause of zero sales, handbook s1).

## 4. CRO audit + copy: Women's Classic Lambswool Crew Sweater (GM priority 3)

`691059dfdc1bc40ece1f4648`, https://www.autumnandwool.com/shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper
Scope: PDP, primary action Add To Cart (size), traffic Google free listings (feed rows SQ8973335/SQ4628527/
SQ5713917/SQ3869977, colour Grey) + Instagram.

Fact sheet (live PDP 21 Oct unless stated): EUR 136 | sizes S, M, L, XL | "Material: 100% lambswool (pure new
wool)" | "Fit: Relaxed." | raglan sleeves, ribbed cuffs, gently curved hem | machine-knitted and hand-sewn in Latvia,
washed and pressed (CLAIM-CHECK) | care: hand wash cool, mild wool detergent, do not wring, dry flat | 8 images
(export) | stock 4 per size (17 Oct export, unconfirmed) | colour: feed says Grey, PDP names no colour.

Garment measurements on the live PDP (cm, as read by WebFetch; owner re-check before reuse elsewhere):

| Size | EU / US / UK | Width | Front length | Back length | Sleeve |
|---|---|---|---|---|---|
| S | 36 / 6 / 8 | 51 | 57 | 62 | 71 |
| M | 38 / 8 / 10 | 54 | 59 | 64 | 72 |
| L | 40 / 10 / 12 | 57 | 61 | 66 | 73 |
| XL | 42 / 12 / 14 | 60 | 63 | 68 | 74 |

### Funnel checklist
| Step | Result | Evidence |
|---|---|---|
| 1 Arrives | PASS (text) / UNVERIFIED (390px) | H1 = feed title, price shown, ATC present; fold position needs screenshot |
| 2 Explores | PARTIAL | Fibre %, fit, cm per size + EU/US/UK mapping: PASS (best size block on the site with dusty pink). Size-guide link is in the description; next to the selector UNVERIFIED. Colour never named on the page (feed: Grey) |
| 3 Decides | PARTIAL | v1 delivery line present (dispatch only, no arrival time). No model height/size. Etsy proof not on PDP (decision 17) |
| 4 Checks out | UNVERIFIED | Size selector; whether ATC without a size silently no-ops like the beanie colour bug needs a phone test (form item 5) |
| 5 Receives | PASS | Contact and FAQ: reply within 1–2 business days |
| 6 Returns | PARTIAL | Care block PASS. "Pairs well with" shows Stand-Collar Blue, Stand-Collar Beige, Side-Slit Light Grey, Dusty Pink Turtleneck, Lambswool Raglan Crew Green: mostly 1-unit or duplicate listings the GM excluded from promotion |

### Findings (ICE = impact, confidence, ease, 1–5)
| # | Step | Finding | Layer | ICE | Proposed fix |
|---|---|---|---|---|---|
| L1 | 3 | Delivery line gives dispatch only | COPY | 4/4/5 | Shared line v2 (s2) |
| L2 | 2 | Colour not named; feed says Grey. Google wants the same colour name in title/description/attribute | COPY | 3/4/5 | Add "Colour: Grey [OWNER: confirm name, e.g. Grey / Light grey / Melange grey]" |
| L3 | 3 | No model height/size: "relaxed" alone does not answer "which size do I take" | COPY + OWNER fact | 4/3/4 | Model line once owner gives height and size worn |
| L4 | 6 | Related products push one-offs and duplicates | NATIVE (if plan allows manual related) / OWNER decision 20 | 2/3/3 | Prefer beanie and hat & scarf set (both priority, gift add-ons); CSS proposal N6 |
| L5 | 2 | Live claim "hand-sewn in Latvia" and "pure new wool" label wording | CLAIM-CHECK (G8, PRD-17) | 3/3/2 | Keep until evidence; drop if none by 31 Oct |
| L6 | — | URL slug contains "hand-knitted" (banned phrase for machine pieces) | OWNER decision | 1/5/1 | Leave: slug change breaks feed links and needs a redirect plan (aw-ecommerce-seo rule) |
| L7 | 1 | Footer/brand strip says "Handmade knitwear by Kristine in Riga"; approved live line is "Handmade in Riga by Kristine" | COPY (site-wide) | 1/4/5 | Owner: confirm which is the approved wording; not PDP-specific |

### Copy diff (proposal; CSV `2026-10-21-wave2-pdp-copy-lambswool-crew.csv`)
Title: no change ("Women's Classic Lambswool Crew Sweater", 38 chars, = H1 = feed). Check the apostrophe: feed uses
the curly ’, the page title was returned with a straight ' by WebFetch [VERIFY in the product editor].
```
  Classic lambswool crew-neck sweater with raglan sleeves, ribbed cuffs and a gently curved hem.   (keep)
+ Colour: Grey [OWNER: confirm exact name].
+ Fit: relaxed. Model is [OWNER: confirm] cm and wears size [OWNER: confirm]. Between sizes? Compare the
+ width with a sweater you own (measurement table below, Size Guide).
  (Material, measurement table, care: keep as live)
- Free shipping. In-stock items ship from Riga within 2–5 working days. 14-day returns.
+ [shared delivery line v2, s2]
```
"Between sizes" sentence gives a method, not a sizing claim, so it needs no owner fact.

SEO title: keep "Women's Classic Lambswool Crew Sweater | Autumn & Wool" (55).
Meta description (154, hand count): "Classic crew-neck sweater in 100% lambswool with raglan sleeves and rib trims.
Relaxed fit, sizes S–XL (EU 36–42). Free shipping to eligible destinations."

CLAIM-CHECK: "hand-sewn in Latvia"; "100% lambswool (pure new wool)" (PRD-17 label check). OWNER: colour name, model
height/size, physical stock per size.

### Experiment log entry
EXP-03: Because the crew sweater PDP gives no arrival time and no model size, adding delivery line v2 + colour +
model line on this PDP for Google free-listing and Instagram traffic will increase size-selected ATCs and orders.
Metric: orders and abandoned checkouts containing this SKU, customer sizing questions (CX). Start: date owner
applies; read +14 days. Layer COPY. Rollback: paste the old description (kept in the CSV `current` column).
Result: TODO. At current traffic, report qualitative evidence only.

## 5. Corrections to wave-1 CRO drafts
- Christmas template in `2026-10-21-css-native-proposals.md` mentions "the UK" and asks OPS for UK/NO/CH cut-offs.
  OPS-12 gap 3 drops UK/NO/CH from all copy until priced; the corrected banner copy is in
  `2026-10-21-wave2-prepared-drafts.md` s2 and supersedes that template.
- CRO-06 v1 delivery line is superseded by s2 above.
