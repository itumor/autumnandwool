# Owner decision pack — due 25-31 Oct 2026 (DRAFT)

Author: Head of E-commerce / GM (agent), 2026-10-21. Master plan s6 decisions 5-21, ordered by gate (ruling C11:
production data outranks content). Each line: decision, GM recommendation, evidence, effect, cost, blocks, reversible.
Nothing here is spend, a live change or a message. Owner sends, applies and pays.

**One line:** 17 decisions this week; the first five (production inputs, cash, PayPal, claims, stock-linked
photos) clear gates G0, G1, G3, G4 and G8. If time runs short, do 5, 7, 14, 16 first and defer 12, 18, 20.

## A. Gate-critical (do first)
| # | Due | Decision | GM recommendation | Evidence | KPI effect | Cost | Blocks | Reversible |
|---|---|---|---|---|---|---|---|---|
| 5 | 25-28 Oct | Production inputs: time 3 units per priority SKU, yarn grams, yarn on hand, people/hours, labour rate, suppliers | Do it on the 5 priority SKUs + 2 alternates (8 total). Production gives the timing sheet | `unit_economics.py`: 0 of 82 costed | Unlocks CM2 = break-even CAC (G0 -> G1) | Owner time; EUR 0 | PRD, FIN, GRO, PAR, all promotion | n/a (data) |
| 7 | 28 Oct | Opening bank balance + date; buffer; fixed-cost list | Buffer = 8 weeks of fixed costs (FIN proposal); list every recurring charge with amount and day of month | Opening cash unknown; README s8 costs are illustrative | Cash forecast stops being "net change only" (G3) | EUR 0 | FIN, all spend and hires | Buffer: yes |
| 14 | 31 Oct | Connect PayPal | Connect, then one real test order + refund, excluded from sales | Stripe proven (#00003/#00004); PayPal not connected | Removes a known checkout drop-off (G4) | Fees per PayPal schedule `[VERIFY on account]` | CRO, FIN, PAR, CX, GRO | Yes |
| 16 | 31 Oct | Claims evidence: "handmade", "made in Latvia/Riga", fibre %; photo rights of "ChatGPT Image" assets | Supply supplier spec sheets / invoices for yarn in the 5 priority SKUs first; one sentence describing who knits and where; drop any claim without proof | Claims cleanup partly verified; hat set PDP claims RWS / Italy spinning | Unblocks creator DMs, ads, PDP copy (G8); avoids misleading-claims risk | EUR 0 | PAR, CRE, SEO, GRO, CRO, PRD | Yes |
| 17 | 31 Oct | One Etsy proof line; verbatim Etsy quotes allowed? | Read the live Etsy figure, pick one line; until then use C1 line | 4 conflicting figures (C1) | One consistent trust line | EUR 0 | CRE, CRO, SEO, GRO, CX, PAR | Yes |

## B. Operations and store
| # | Due | Decision | GM recommendation | Evidence | KPI effect | Cost | Blocks | Reversible |
|---|---|---|---|---|---|---|---|---|
| 8 | 28 Oct | Carrier(s) per region; carriers used today | Name what you use now; OPS researches rates; no new contract | No carrier data in repo | Delivery ranges and shipping cost per order (CM2 input) | EUR 0 now | OPS, CRO, SEO, FIN | Yes |
| 9 | 28 Oct | Is Etsy/Mareshop still selling; both channels open this season? | Answer yes/no; if yes, one shared stock list (C14) | Etsy activity unconfirmed | Etsy orders counted in KPI row; avoids double-selling 1-unit items | EUR 0 | SEO, CRO, PRD, GRO, CX | Yes |
| 13 | 30 Oct | Return address; who pays return postage; packaging style and spend | Give the address; keep return-postage rule pending adviser (C12); packaging spend only after FIN check | MC policy vs live page differ (C12) | Returns allowance column (CM2) | Packaging TODO | OPS, CX, CRO, SEO | Yes |
| 15 | 31 Oct | Keep or let lapse the Squarespace backup copy (trial ends 1 Nov) | Let it lapse unless you want to pay for it; export anything you need first `[VERIFY: what is on it]`. Keeping it is a subscription = your call | Memory: backup copy, trial ends 2026-11-01 | None on sales | Plan price `[VERIFY on Squarespace pricing page]` | CRO, SEO | No after 1 Nov |
| 19 | 31 Oct | Scoped unfreeze of product data for the 5 priority PDPs, or proposals-only | Scoped unfreeze for the 5 only (size, per-colour images, titles, descriptions), each change approved by you before CRO drafts are applied | CRO plan risk 7 | Lets 5 PDPs reach the conversion checklist | EUR 0 | CRO, PRD, SEO | Yes |
| 20 | 31 Oct | Dedupe listings (lambswool crew, side-slit, beige vest, stand-collar); vest restock or hide; QC tolerance; founder story in your words | Keep the listing with more images and hide the other; decide vest per stock; 3-5 sentences of founder story | Duplicates seen in export (2 x side-slit, 2 x lambswool raglan crew, 2 x beige vest, 2 x stand-collar) | Cleaner catalogue, less feed risk | EUR 0 | PRD, CRO, CRE | Yes |
| 21 | 31 Oct | Free shipping per region | Keep current free shipping (Latvia/US/RoW) until carrier rates (11 Nov); paid express only for late orders | No carrier rates yet | Shipping column in CM2 | TODO after rates | OPS, FIN, CRO, GRO | Yes |

## C. Marketing and measurement
| # | Due | Decision | GM recommendation | Evidence | KPI effect | Cost | Blocks | Reversible |
|---|---|---|---|---|---|---|---|---|
| 6 | 27 Oct | Who films; weekly 2-hour slot; consent form | Owner films 2 h/week; consent form for anyone on camera before filming | CRE plan | Content output for Pinterest/IG | EUR 0 | CRE, PAR | Yes |
| 10 | 28 Oct | Verify GSC + Bing; noindex `/redesign-preview`; 301 `/home`; Pinterest business account (rename vs new) | Do verification first (15 min); Pinterest: convert existing account if it has followers, else new | SEO plan | Search clicks measurable | EUR 0 | SEO, CRE | Yes |
| 11 | 28 Oct | Do discount codes + per-code order reports exist on current plan (screenshot)? | Screenshot of Marketing > Discounts page | C6 conflict | Decides attribution method for creators (G7) | EUR 0 | PAR, GRO, CRO | n/a |
| 12 | 28 Oct | Gifting cap; which SKUs to gift; approve shortlist and each DM | Defer the EUR cap until costs exist (4 Nov); gift only from priority 5 that are G8-cleared; you approve each DM | PAR plan D2; no product cost known | Creator test (proposed test channel B) | Product + shipping per gift: TODO | PAR | Yes |
| 18 | 31 Oct | Instagram handle, Facebook, Pinterest ownership; approve UTM scheme; paste 5 bio links | Confirm which handle is the brand; approve Growth's UTM file; paste links (owner-action-pack s C) | Instagram/Pinterest sessions 0 of 64 | Sessions by source measurable | EUR 0 | CRE, GRO, SEO | Yes |

## D. Early read for 4 Nov (decision 24, not due this week)
Squarespace plan upgrade: unlocks Code Injection -> GA4 ecommerce events, Clarity, possibly discounts (README s8,
handbook s3). Weigh: plan price difference `[VERIFY on current pricing page; owner screenshot of current plan]`
against what it measures. GM view today: decide after decision 11 and after the first 2 WBRs show whether sessions
are high enough for funnel data to matter (64 visits/30 days today). No recommendation to buy yet.

DRAFT for owner. Not sent. GM rolls unanswered items into the Monday batch.
