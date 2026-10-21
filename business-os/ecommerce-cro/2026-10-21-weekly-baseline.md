# CRO weekly note #0 (baseline) — week starting 2026-10-19 — DRAFT

Owner: aw-ecommerce-cro. Tasks CRO-05 (KPI-row input), CRO-23 (weekly note + experiment log). The first regular
note is due Fri 24 Oct; this baseline fixes the "before" side so every later change has something to compare to.
`kpi-weekly.csv` is not edited (shared file; ruling C16: baseline row drafted in the WBR of Mon 26 Oct, owner appends).

## 1. Changes applied by the owner since the last note
None since the overnight fixes of 19 Oct (handbook s5): overlay CSS, cardigan title/description, size-guide line,
Merchant Center rebuild, contact-form CSS, vest restock, home card links. These are the "before" anchor.

## 2. Baseline numbers (sources; no new data collected by CRO)
| Metric | Value | Source |
|---|---|---|
| Sessions | 62 visits / 30 d to 17 Oct (64 / 30 d in master plan) | handbook s7; master plan s1 |
| Bounce | 94.34% | handbook s7 |
| Real orders | 0 (2 test orders #00003, #00004 excluded) | README s2 |
| Conversion rate | n/a (0 orders) | — |
| AOV | n/a | — |
| Abandoned checkouts | TODO: owner screenshot (Squarespace) | — |
| GSC 90 d | 11 clicks, 388 impressions, CTR 2.8%, avg pos 14.1 | handbook s7 |
| Merchant Center | 98 under review, 0 approved (19 Oct); 21 Oct status TODO owner screenshot | handbook s7 |
| PDPs with delivery line | 5 of 6 fetched (raglan cardigan missing); 16 not checked | WebFetch 21 Oct |
| Priority PDPs perfected | 0 of 5 (5 audited + proposals drafted 21 Oct, provisional set) | this folder |

## 3. Proposed `kpi-weekly.csv` input for week_start 2026-10-19 (for the WBR; owner/FIN append)
- sessions: TODO (GA4 or Squarespace Analytics, 19–25 Oct)
- orders_site: 0 real
- conversion_rate: blank (no orders); aov_eur: blank
- notes (suggested text): "Baseline week. Test orders #00003/#00004 (18-19 Oct, refunded) excluded. Overlay
  click-trap CSS live since 19 Oct. No CRO changes applied this week."

## 4. Next 3 proposals (ICE order, all need owner approval)
1. Raglan cardigan copy: remove "hand-knitted", add delivery line, state Brown/Blue lead time (COPY; ICE 5/5/5).
   File: `2026-10-21-pdp-copy-proposals.md` s1.
2. Connect PayPal, then run the November checklist (NATIVE; ICE 4/4/4). File: `2026-10-21-test-order-checklist-november.md`.
3. One returns sentence on Shipping & FAQ ("unworn, unwashed … original condition"), interim until adviser
   (COPY; ICE 3/5/5). File: `2026-10-21-checkout-mobile-audit.md` C4.

## 5. Experiment log
| ID | Hypothesis (short) | Page / layer | Metric | Start | Read | Rollback | Result |
|---|---|---|---|---|---|---|---|
| EXP-01 | Delivery line + lead time + claim fix raises cardigan ATC/orders | Raglan cardigan / COPY | cardigan orders, abandoned carts | on apply | +14 d | paste old text | TODO |
| EXP-02 | PayPal raises checkout completion | Checkout / NATIVE | abandoned vs completed, payment method | on connect | +28 d | disconnect | TODO |
Rule: one change per page per 2 weeks; at this traffic report qualitative evidence, never a % lift from < 5 orders.
