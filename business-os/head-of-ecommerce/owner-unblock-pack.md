# Owner unblock pack: every owner-blocked task, all 10 departments (DRAFT for owner)

Author: Head of E-commerce / GM (agent), 2026-10-21 (wave 2). Sources: `plans/2026-2027/status/*.md` (wave-1 state),
`OPEN-TASKS.md` (87 blocked), master plan s6 decisions 1-37. Deduplicated: one row per owner action, even when
several departments asked for it. Nothing here is spend, a live change or a message. You send, apply and pay.
Time estimates are GM estimates, not measured.

**One line:** 86 of 87 blocked tasks wait on at least one owner action. Five actions (about 4.5-6.5 hours of your time
in total, most of it unit timing and the stock count) unblock 40 distinct blocked tasks across 9 departments. Do them first.

## Do these first (highest leverage)
| Rank | Owner action (row #) | Due | Time | Unblocks |
|---|---|---|---|---|
| 1 | Allow agent writes to `business-os/production/` (the `prod-guard` hook blocks the folder), or name another folder (row 2) | 23 Oct | 2 min | **9 tasks**: PRD-02, 03, 04, 05, 08, 10, 12, 14, 17. Also lets the weekly capacity file run (PRD-22, then CRE-14, CX-14, SEO-26) |
| 2 | Production inputs G0: approve the 5 SKUs, time 3 units each, weigh yarn, fill the facts form (rows 5, 9, 12) | 24-28 Oct | ~2-3 h spread over the week | **17 tasks**: PRD-06, 07, 09, 15, 16, 20, 21, FIN-03, 05, 18, 19, GRO-15, PAR-11, PAR-15, SEO-20, CRO-26, GM-05. Starts the money chain G0 -> G1 -> break-even CAC |
| 3 | Physical stock count + made-to-order lead time, 5 priority SKUs now, 22 visible by 31 Oct (row 8) | 24 / 31 Oct | 1-2 h | **9 tasks**: PRD-11, SEO-04, CRE-12, CRE-13, CRO-23, OPS-09, FIN-17, PAR-11, PAR-15 |
| 4 | Claims evidence: yarn invoices/spec sheets for the 5 priority SKUs, one sentence on who knits/finishes and where, which photos are real (row 26) | 31 Oct | 45-60 min | **7 tasks**: SEO-25, PAR-06, PAR-13, CRE-23, CRO-27, PRD-17, PRD-18. Clears G8 (first creator DM, ads, PDP copy, feed) |
| 5 | Cash inputs: fill `business-os/finance/owner-finance-inputs-2026-10-21.md`, say yes/no to the 8-week buffer (row 13) | 28 Oct | 15-20 min | **5 tasks**: FIN-05, FIN-07, FIN-17, PRD-20, GM-05. Without it no spend, stall, yarn or hire can get a yes/no |

Next after the five: PayPal + test order (row 22, 5 tasks) and the Monday data batch (row 10, the first WBR and
every readout after it). Counts overlap (one task can need several actions), so they are not additive. The 40 is
the number of distinct blocked tasks across ranks 1-5 (9 + 17 + 7 + 6 + 1 new per rank).

## Full checklist, by due date
Fill-in fields: `__`. Yes/no: circle one. "Unblocks" lists the blocked task IDs that name this action; ids in
brackets are to-do tasks or downstream effects.

| # | Owner action | Due | Time | Unblocks task IDs |
|---|---|---|---|---|
| 1 | Paste or export each business day's inbound messages (Gmail, Instagram DMs, Etsy) to a file CX can read | daily from 21 Oct | 5 min/day | CX-02 (CX-27) |
| 2 | Production folder: allow agent writes to `business-os/production/` (adjust `prod-guard` pattern `**/production/**`) **yes / no**; if no, folder to use: `__` | 23 Oct | 2 min | PRD-02, PRD-03, PRD-04, PRD-05, PRD-08, PRD-10, PRD-12, PRD-14, PRD-17 (PRD-22; CRE-14, CX-14 via capacity file) |
| 3 | Merchant Center: screenshot Products > Diagnostics + disapproved list; note which image shows the brown cardigan | 23 Oct | 5 min | CRO-02, SEO-02 (G6; MC count for GM-07) |
| 4 | Decision 1: tick master plan, KPI targets, rulings C1-C16 in `owner-decision-pack-2026-10-24.md` | 24 Oct | 15 min | PRD-01 (rulings used by CX-20, SEO-19, CRO-24 and others) |
| 5 | Decision 2: provisional 5 priority SKUs (cardigan raglan, Dusty Pink raglan, lambswool crew, hat & scarf set, beanie) **yes / change to** `__` | 24 Oct | 5 min | PRD-06, FIN-03, GRO-15 (SEO working set, GM-12) |
| 6 | Decision 3: one dispatch promise "in-stock items dispatched in 2-5 working days" **yes / other** `__`; approve OPS interim delivery line (`operations/delivery-promise-reconciliation.md` s3) **yes / no** | 24 Oct | 5 min | PRD-04, OPS-09 |
| 7 | CRO screenshots: Custom CSS panel, Contact page and Shop page at phone width, add-to-cart without colour on phone; then weekly | 24 Oct, weekly | 10 min | CRO-21, CRO-22 |
| 8 | Decision 4: physical count + MTO lead time per SKU (form in `owner-decision-pack-2026-10-24.md`): 5 priority today, 22 visible by 31 Oct; include cardigan Brown/Blue (stock or MTO?) and which of the 24 un-photographed colours exist | 24 Oct / 31 Oct | 1-2 h | PRD-11, SEO-04, CRE-12, CRE-13, CRO-23, OPS-09, FIN-17, PAR-11, PAR-15 |
| 9 | Decision 5a: time 3 units per priority SKU (minutes per step) and weigh yarn per garment on PRD's timing sheet; 8 SKUs by 31 Oct | 25 Oct (8 by 31 Oct) | ~5 min recording per unit while knitting, 24 units (estimate) | PRD-06, PRD-09, PRD-15, PRD-21, FIN-03, GRO-15, PAR-11, GM-05 (then FIN-05, FIN-18, FIN-19, SEO-20, CRO-26, PAR-15 via costs) |
| 10 | Monday data batch, Mon 26 Oct 09:00 then every Monday: Squarespace Orders export 19-25 Oct (excl. test #00003/#00004), Etsy order count, GA4 traffic acquisition by source/medium, ad spend this week **EUR 0 yes / no**, MC approved count | 26 Oct, weekly | 20 min | GM-07, GRO-06 (FIN-11, GM-11, GRO-17, CRO-20, SEO-11) |
| 11 | Decision 6: who films `__`, weekly 2-hour slot `__ day/time`, consent form for anyone on camera **yes** | 27 Oct | 10 min | CRE-16, CRE-12, PAR-21 |
| 12 | Decision 5b: production facts: people `__` x hours/day `__`, labour rate EUR/h `__`, yarn on hand by colour/dye lot, suppliers, lead times, MOQs | 28 Oct | 30 min | PRD-07, PRD-09, PRD-15, PRD-16, PRD-20, FIN-03 |
| 13 | Decision 7: fill `finance/owner-finance-inputs-2026-10-21.md` (balances + dates, fixed costs incl. plan name, payout schedules); buffer = 8 weeks of fixed costs **yes / other** `__` | 28 Oct | 15-20 min | FIN-07, FIN-05, FIN-17, GM-05, PRD-20 (GM-15, GM-18, every spend check) |
| 14 | Decision 8: carrier(s) used today per region `__`; business account **yes / no** | 28 Oct | 5 min | OPS-06, OPS-09, OPS-11, FIN-18 |
| 15 | Decision 9: Etsy/Mareshop selling this season **yes / no**; if yes, listings export + Stats screenshot | 28 Oct | 2 min + 10 min | SEO-07, SEO-19, SEO-20, PAR-20 |
| 16 | Decision 10: request indexing for 10 URLs, Bing import, `/home` 301, `/shop/gift` hide or merge, GSC Performance export, Rich Results screenshots (5 PDPs); Pinterest: convert `mmareshop` **or** new business account | 28 Oct | 45 min | SEO-05, SEO-06 |
| 17 | Decision 11: two screenshots: Settings > Billing (plan name, term, renewal date) and Marketing > Discounts (codes + per-code report?) | 28 Oct | 3 min | GM-13, PAR-14 (G7; FIN plan-fee line) |
| 18 | Decision 12: check scorecard lines 3/5/6 on live creator profiles (or set up a view the agent can read), approve shortlist, number of gifts `__`, approve each DM | 28 Oct | 45-60 min | PAR-04, PAR-06, PAR-13, PAR-11, PAR-15 |
| 19 | Decision 13: return address `__`; return postage paid by **customer / us** (pending adviser); packaging style and spend cap EUR `__` | 30 Oct | 10 min | OPS-16 (CX returns macro) |
| 20 | OPS dry run: 3-4 recipients (LV, EU, optional EE/LT, US), spare items, scale **yes / no**, label budget EUR `__` (spend: your approval) | 30 Oct | 15 min | OPS-11 (then OPS-06, OPS-09) |
| 21 | Turtleneck colours: confirm which exist, shoot and upload (ruling C7, session 1) | 31 Oct | 2-3 h | CRE-12, CRO-23, SEO-24 |
| 22 | Decision 14: connect PayPal (Settings > Payments), place one test order, refund it | 31 Oct | 30 min | CRO-03, FIN-15, CX-11, CRO-13, PAR-15 |
| 23 | Decision 15: Squarespace backup copy **keep (paid) / let lapse**. Not reversible after 1 Nov | 31 Oct | 5 min | none blocked (fixed-cost list in row 13) |
| 24 | Decision 17: Etsy proof line **"4.9 stars, 1,400+ reviews on Etsy (Mareshop)" / live figure** `__`; verbatim Etsy quotes allowed **yes / no** | 31 Oct | 5 min | CRE-10, CX-23, PAR-20 (SEO `llms.txt`, Pinterest About) |
| 25 | Decision 18: brand accounts (IG `@autumnandwool` vs `@mare.knitwear`, Facebook, Pinterest, TikTok) `__`; approve `growth/utm-links.csv` **yes / no**; paste bio links | 31 Oct | 20 min | CRE-15, SEO-06, PAR-13 |
| 26 | Decision 16 (+34 first part): yarn invoices/spec sheets for the 5 priority SKUs; one sentence on who knits/finishes and where (hand-knitted or manual machine?); proof for "Italian-spun", "extra-fine", "hand-sewn in Latvia" or drop; which photos are real vs "ChatGPT Image" | 31 Oct | 45-60 min | SEO-25, PAR-06, PAR-13, CRE-23, CRO-27, PRD-17, PRD-18 (G8, GRO ad concept A, CX FAQ P3) |
| 27 | Decision 19: scoped unfreeze for the 5 priority PDPs **yes / proposals only**; approve or reject CRO proposals in `business-os/ecommerce-cro/` | 31 Oct | 5 min + 30 min review | CRO-27 |
| 28 | Decision 20a: dedupe (keep which listing: lambswool crew, side-slit, beige vest, stand-collar); vest **restock / hide**; QC tolerance `__` cm; create `qc-log.csv` **yes** | 31 Oct | 15 min | PRD-11, PRD-13 |
| 29 | Decision 20b: answer the 8 founder-story questions in Kristine's own words (`campaign-assets/drafts/plan-wave1/founder-story-draft-2026-10-21.md`) | 31 Oct | 30 min | CRE-10 (CX welcome W2) |
| 30 | Decision 21: keep free shipping LV/US/Rest of World until rates **yes / no**; paid express for late orders **yes / no** (final 11 Nov) | 31 Oct | 5 min | FIN-18 |
| 31 | Decision 22: send the adviser pack (Shipping & Returns, MTO return rule, consent, label wording and languages). Fee TODO owner | 3 Nov | 15 min to send | OPS-16, CX-19, PRD-19, CX-23, CRO-27 (G9) |
| 32 | Decision 28a: confirm PRD cost proposals for the 5 priority SKUs and paste them into `sku-economics.csv` | 4 Nov | 30 min | FIN-03, GRO-15, PAR-11, SEO-20, CRO-26, FIN-18, FIN-19 (GM-12) |
| 33 | Decision 23: minimum contribution per order EUR `__` (FIN proposes after row 32; form in `finance/min-contribution-method.md`) | 4 Nov (fallback 11 Nov) | 10 min | GM-05, FIN-05, GRO-15, PAR-14 |
| 34 | Creator terms (PAR D5): code % `__`, commission `__`, usage rights **yes / no** | 4 Nov | 10 min | PAR-14 |
| 35 | Decision 24: Squarespace plan upgrade **yes / no** (memo: `plan-upgrade-memo-prep-2026-10-21.md`) | 4 Nov | 10 min | GRO-16 (G7) |
| 36 | Decision 25: send accountant question list (`finance/accountant-questions-2026-10-21.md`) | 6 Nov | 10 min | none blocked now (FIN-23, FIN-25 inputs) |
| 37 | Run the November test-order checklist (card, then PayPal) and refund each | 7 Nov | 45 min | CRO-13 |
| 38 | Decision 26: public reply promise "1-2 business days" **yes / other** `__` | 7 Nov | 2 min | CX-20 |
| 39 | Decision 27: market stall **none / KuKu (closes 10 Nov, EUR 50) / other** `__`, only after FIN verdict. Baltic EXPO is non-refundable | 10 Nov | 10 min | PRD-16, CRE-23, FIN-17 (GM-15, PRD-24) |
| 40 | Decision 28b: confirm all 22 cost proposals; final free-shipping policy against carrier rates | 11 Nov | 60 min | PRD-15, FIN-18 (GM-16) |
| 41 | Decision 29: shoot and upload beanie, hat set, cardigan Blue colours **or** approve trimming the 46 at-risk feed rows; Beanies/Sets categories merge into "Hats & scarves" **yes / no** | 14 Nov | 3-4 h photos, or 2 min trim | CRE-13, CRO-23, CRO-24, SEO-24, SEO-13 (CX-14) |
| 42 | Garment facts: confirm measurements per visible SKU **or** approve copying them from live PDPs; fibre % (dusty pink, beige vest, distressed); model height/size; turtleneck size range (page offers XS/S/M, table lists S/M/L) | 14 Nov | 2 min (copy) or 1 h (measure) | CX-08, CRO-27 (CRE-21) |
| 43 | Decision 30: MailerLite account, newsletter destination, sender name + postal address, review platform, consent basis per audience (after adviser) | 14 Nov | 45 min | CX-22, CX-24, CX-23, CX-19 |
| 44 | Decision 31: gift perks (wrap, note, free exchange) **yes / no each**, after FIN margin check | 14 Nov | 10 min | CX-10, CRO-26 |
| 45 | Decision 32: December yarn purchase per PRD proposal **yes / no / amount** `__` (spend) | 16 Nov | 15 min | PRD-20 |
| 46 | Decision 33: December paid test **go / no-go**, ceiling EUR `__` (EUR 0 valid; memo prep: `dec-paid-test-memo-prep-2026-10-21.md`); approve Christmas cutoff table + banner for publishing; label languages | 20 Nov | 20 min | CRO-25, CRE-22, CX-25, SEO-26 (GRO-18, GRO-19, GM-18) |
| 47 | Decision 34: supplier spec sheets for all remaining yarns | 30 Nov | 30-60 min | PRD-18, PRD-17, SEO-25 |
| 48 | Decision 35: 2027 range direction (core cull, spring drop, crochet gloves, slug clean-up) | 15 Jan 2027 | 30 min | (PRD-30, SEO-31, GM-21) |
| 49 | Decision 36: 2027 budget envelope per line; Partnerships hire after verdict | 31 Jan 2027 | 60 min | (all 2027 budgets, GM-21, PAR-23) |

Optional, nothing blocked: 5-minute look at Meta Ad Library and the PappusStore Etsy page for Growth (GRO-20);
approve the content drafts in `campaign-assets/drafts/plan-wave1/` before anything is posted.

## Not on the owner (for the record)
- CRE-17 waits on Growth's `business-os/growth/utm-links.csv`. That file now exists (created 21 Oct, rows in
  `draft`), so Creative can switch drafts once you approve it (row 25).
- CRE-22, CX-25, SEO-26, CRO-25 also wait on Operations' carrier-backed cutoffs (G5, 14 Nov); your part is row 46.
- GM-07 also waited on Finance's cash forecast; that now exists (`finance/cash-forecast-2026-10-26.md`, net change
  only until row 13).

DRAFT for owner. Not sent. GM rolls unanswered rows into each Monday batch (ruling C11).
