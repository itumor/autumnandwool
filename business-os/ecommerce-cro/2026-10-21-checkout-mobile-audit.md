# CRO audit: cart, checkout, mobile and site-wide buying copy — 2026-10-21 — DRAFT

Owner: aw-ecommerce-cro. Tasks CRO-14 (audit), CRO-19 (site-wide copy conflicts), CRO-27 (plan-upgrade input).
Read-only: no cart actions, no checkout, no payment fields were touched. Evidence = repo files + WebFetch text of
public pages on 21 Oct. WebFetch cannot see JS, CSS `content` lines, overlays or the checkout iframe: those rows are
UNVERIFIED and go into the November test-order checklist.
KPI: checkout completion (cart → order) and conversion rate.

Scope / traffic source / primary action: Shop → PDP → Cart → Squarespace Secure Checkout → confirmation email, on
phone (390px) and desktop; all sources; primary action = completed order.

## 1. Funnel checklist (site-wide)

| Step | Check | Result | Evidence |
|---|---|---|---|
| 1 Arrives | No horizontal scroll at 390px | PASS (iframe test, not a real phone) | QA-REPORT s1, s6 |
| 1 Arrives | Shop page has one H1 | FAIL: H2 "The collection", no H1 | WebFetch /shop 21 Oct; QA s4 |
| 1 Arrives | Shop page shows no false empty state | UNVERIFIED: "No results found / No results match your search" is in the HTML next to 22 products; may be hidden by JS | WebFetch /shop; `squarespace-implementation-proposal.md` SHOP |
| 2 Explores | Size guide reachable from PDP | PASS (link text on 6/6 PDPs fetched) | WebFetch |
| 2 Explores | Size guide in header nav | FAIL (QA 18 Oct; not re-checked) | QA s2 |
| 3 Decides | One returns condition wording | FAIL: `/shipping-returns` "Unworn, unused items"; `/faq` "unworn, unwashed items" | WebFetch 21 Oct (still live) |
| 3 Decides | One reply-time promise | PASS in page text: Contact, FAQ, Shipping all "1–2 business days" (ruling C2). UNVERIFIED: CSS-rendered Contact line from 19 Oct says "we reply within 24 hours" | WebFetch; handbook s5.5 |
| 3 Decides | Made-to-order handling clear | FAIL: cardigan Brown/Blue "to order", no lead time; returns page excludes made-to-order pieces | WebFetch PDP + /shipping-returns |
| 3 Decides | Payment methods stated | FAIL/partial: FAQ "All major credit and debit cards"; Google Pay seen at checkout not mentioned; no PayPal | WebFetch /faq; zero-sales-diagnosis #3 |
| 3 Decides | Claims within brand rules | FAIL: "hand-knitted" on raglan cardigan; "Each piece is handmade" on /shipping-returns (restricted word, approved only as "Handmade in Riga by Kristine") | WebFetch; aw-brand-voice s3 |
| 4 Checks out | Stripe card order completes, desktop + phone | PASS on 18–19 Oct (#00003 desktop, #00004 phone, refunded) | handbook s7; README s2 |
| 4 Checks out | Earlier desktop blank payment frame (beanie, 18 Oct) | Superseded by #00003 after overlay fix; not re-tested since 19 Oct | implementation-report l.220, l.224 |
| 4 Checks out | PayPal | FAIL: not connected | implementation-report l.272 |
| 4 Checks out | Checkout default country | FAIL/low: defaults to United States | implementation-report l.329 |
| 4 Checks out | Tax line shows EUR 0.00 | UNVERIFIED (accountant question: are prices VAT-inclusive with tax set inside price? FIN lane) | implementation-report l.326; QA s3 |
| 4 Checks out | Multi-currency checkout on | UNVERIFIED display (converted prices vs EUR charge) | implementation-report l.272 |
| 4 Checks out | Guest checkout (no account forced) | UNVERIFIED | — |
| 4 Checks out | ATC with no variant selected shows a message, no dead click | UNVERIFIED since 19 Oct fix | handbook s4 |
| 4 Checks out | Cart totals, qty, remove | PASS (18 Oct) | QA s3 |
| 4 Checks out | Abandoned-cart recovery | PASS: "Recover abandoned carts" Live, 1 reminder after 1 day | implementation-report l.252 |
| 5 Receives | Order confirmation email content, tracking promise | UNVERIFIED (test orders placed, email content not on file) | — |
| 5 Receives | Tracking promised | PASS on /shipping-returns "sent with tracking" | WebFetch |
| 6 Returns | Care advice on PDPs | PARTIAL (missing on Long Wool Cardigan) | WebFetch |
| 6 Returns | Footer tap targets >= 24px on phone | FAIL: 22px links, 20–25px icons | QA s4 |

## 2. Findings

| # | Step | Finding | Evidence | Layer | ICE | Proposed fix |
|---|---|---|---|---|---|---|
| C1 | 4 | No PayPal: second payment route missing for EU/US gift buyers | implementation-report | NATIVE SETTING (owner) | 4/4/4 | Connect PayPal (decision 14, 31 Oct), then PayPal test order + refund (checklist) |
| C2 | 3 | Made-to-order colours: no lead time + excluded from returns | PDP + policy | COPY + OWNER DECISION + adviser (G9) | 5/4/3 | Owner states lead time; adviser confirms whether standard items made after order can be excluded (README s11 says likely not) |
| C3 | 3 | "hand-knitted" (cardigan) and "Each piece is handmade" (Shipping & Returns) | WebFetch | COPY | 4/5/5 | Cardigan: see PDP proposals. Shipping page: "Each piece is knitted and finished in small runs, so slight variations in texture or colour are normal." [OWNER: confirm "small runs" or drop it] |
| C4 | 3 | Returns condition differs between Shipping and FAQ | WebFetch | COPY (adviser before final) | 3/5/5 | Both pages: "Unworn, unwashed items in their original condition can be returned within 14 days of delivery." Hold final wording for adviser (decision 22) |
| C5 | 3 | Possible leftover "24 hours" in CSS `content` on Contact | handbook s5.5 | CSS | 3/3/5 | See CSS proposals P3 |
| C6 | 3 | FAQ payment answer omits Google Pay / PayPal | WebFetch /faq | COPY | 2/4/5 | After PayPal is live: "Cards (Visa, Mastercard and others), Google Pay and PayPal at a secure checkout." Confirm the card brands and wallets shown at checkout first [OWNER screenshot] |
| C7 | 1 | Shop page no H1 | WebFetch | NATIVE SETTING | 2/5/5 | In the Shop page header text block, set "The collection" to Heading 1 |
| C8 | 1 | "No results found" text in Shop HTML | WebFetch | CSS (selector to verify) / screenshot first | 2/2/4 | Screenshot at 390px; if visible, CSS proposals P4 |
| C9 | 4 | Checkout default country = United States; studio and only tested delivery country = Latvia | implementation-report l.329 | NATIVE SETTING | 2/3/5 | Owner checks Commerce → Checkout / store address settings; set Latvia if the option exists [VERIFY setting exists on plan] |
| C10 | 6 | Footer tap targets under 24px | QA s4 | CSS | 2/5/5 | CSS proposals P2 |
| C11 | 3 | Cart has no reassurance line near Checkout | QA s2 (heading "Shopping Cart") | CSS or native text | 2/3/4 | CSS proposals P5 (by 21 Nov) |
| C12 | 2 | Size guide not in header nav | QA s2 | NATIVE SETTING | 2/4/5 | Navigation → add /size-guide |
| C13 | 4 | Funnel blind past pageviews (no add_to_cart / purchase events) | weekly-measurement-report-2026-10-19 | NEEDS PLAN UPGRADE | 3/5/2 | See s4 |

## 3. Quick wins (< 15 min each, owner applies after approval)
1. C1 PayPal connect (native). 2. C7 Shop H1 (native). 3. C4 one returns sentence on both pages (copy, interim until
adviser). 4. C10 footer tap targets (CSS P2). 5. C12 Size guide in header nav (native).

## 4. Plan-upgrade input for decision 24 (4 Nov) — CRO view only
What CRO gets from Code Injection / a higher plan (README s8, handbook s3, implementation report): GA4 ecommerce
events (add_to_cart, begin_checkout, purchase), Microsoft Clarity recordings, Discounts, promotional pop-up, auto
Google feed sync. Price difference: TODO, owner verifies on the current Squarespace pricing page.
Recommendation: at ~64 visits/month the events would record a handful of hits, so the upgrade is not worth it for
CRO alone today. It becomes necessary before any paid traffic (GRO gates) or creator codes (ruling C6), because those
need attribution beyond Squarespace Orders. Decide together with GRO/PAR on 4 Nov; label every dependent proposal
`NEEDS PLAN UPGRADE` until then.

## 5. Experiment log entry
| Field | Value |
|---|---|
| ID | EXP-02 (fix-forward) |
| Hypothesis | Because the store offers only card/Google Pay and EU/US gift buyers often prefer PayPal, connecting PayPal for all traffic will raise checkout completion (cart → order) |
| Metric | Abandoned checkouts vs orders per week (owner screenshot), payment method on each order |
| Dates | Start = PayPal connect date (target by 31 Oct); read 4 weeks later |
| Rollback | Disconnect PayPal in Payments (native) |
| Result | TODO |

## 6. Unverified — owner screenshots needed (all are in the November checklist)
Shop page at 390px (empty-state text); Contact page CSS line wording; ATC with no colour; guest checkout; tax line;
multi-currency display; order and refund email content; checkout payment methods shown.
