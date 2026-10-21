---
name: aw-fulfilment-sop
description: Use when processing or planning Autumn & Wool order fulfilment end to end (order check, stock/production, packing, carrier choice, dispatch, tracking, delivery problems), writing or updating the order-to-delivery SOP, comparing carrier rates per region, or measuring on-time dispatch and fulfilment errors.
---

# Order-to-delivery SOP (Autumn & Wool)

Purpose: every paid order is checked, made or picked, inspected, packed and dispatched inside the promised lead
time, with tracking sent, and no missed or duplicate orders. Implements README s.6. The agent drafts checklists,
logs and customer-notice drafts; humans touch orders, labels and parcels.

Facts to verify before use (TODO owner): promised dispatch time (FAQ says made-to-order may need up to 5
business days before dispatch); delivery ranges (Merchant Center lists free shipping, 4-10 business days, per
region); carriers used (TODO: e.g. Latvijas Pasts, Omniva, DPD - confirm); shipping currently free for Latvia,
US and Rest of World in Squarespace settings (only Latvia checkout-tested). Contact email:
autumnandwool@gmail.com.

## Stages

| # | Stage | Do | Control / exception |
|---|---|---|---|
| 1 | Order in | Daily at fixed time: read new Squarespace Orders + Etsy. Payment status = paid (Stripe). Check product, size, colour, address complete (flat/apartment no., postcode, phone for parcel lockers) | No missed/duplicate orders: order no. logged once. Suspicious (mismatched country, many units) = owner review before work |
| 2 | Stock or make | Finished unit on shelf? Reserve it (physical tag with order no.). Made-to-order? Add to production queue with due date = order date + promised dispatch days | Will miss promise? Draft customer notice same day (aw-support-replies "delay"): new date + options (wait / switch item / cancel with full refund — owner decides refunds) |
| 3 | QC | Run aw-qc-and-labelling checklist on the actual unit | Critical/major defect = do not pack |
| 4 | Pack | Fold in tissue, care card, (optional) thank-you card, branded mailer/box; weigh; photo of packed item for records (helps damage claims) | Packaging matches item size; parcel weight logged for carrier cost |
| 5 | Label + dispatch | Buy label at the service the customer paid for (free standard unless chosen otherwise); hand to carrier; keep acceptance receipt | Mark fulfilled in Squarespace with tracking (human); stock update in store is a human action |
| 6 | Tracking | Squarespace fulfilment email sends tracking (verify setting). Check tracking every 2 business days | Exception (failed delivery, returned to sender, stuck > 5 business days) = act before customer asks |
| 7 | Delivered | Log delivery date (starts 14-day withdrawal clock: aw-returns-handling) | Trigger review-request timing (aw-email-lifecycle) |
| 8 | Close-out | Record actual shipping cost, packaging cost vs `sku-economics.csv` assumptions | Feed real costs to aw-unit-economics (propose; don't edit CSV unasked) |

## Delivery problems

- **Lost / stuck:** open carrier trace after carrier's stated window; draft customer update; owner decides
  reship vs refund. Risk of loss in transit sits with the trader until the consumer receives goods (general EU
  rule; adviser to confirm wording).
- **Damaged on arrival:** ask customer for photos of parcel + item (draft), keep packing photo, file carrier
  claim; treat as faulty goods (aw-returns-handling, legal guarantee route), not a withdrawal.
- **Wrong item sent:** apologise, send correct item first if stock allows (owner approves), prepaid return.
- **Address error:** contact customer before dispatch; never guess an address.
- **Customs (non-EU: UK, US, CA, AU, NO, CH):** duties/VAT may be charged to recipient; check what site/checkout
  says before telling customers (TODO verify policy text). Commercial invoice with HS code for knitted wool
  garments (TODO accountant/carrier confirms codes).

## Carrier rate table (to fill, `business-os/carrier-rates.md`)

```
| Region | Carrier + service | Tracked? | Price for 0.5 kg / 1 kg / 2 kg | Transit (carrier stated) | Parcel locker? | Notes |
| Latvia | ... | Baltics | ... | EU-other | ... | UK | ... | US/CA | ... | AU | ... | NO/CH | ... |
```
Source each price from the carrier's public price list with date; never estimate. Compare to the free-shipping
promise and shipping_eur in `sku-economics.csv`.

## Daily dispatch log template (`business-os/dispatch-log.csv`, propose)

`order_no,channel,order_date,promised_dispatch_by,sku,size,colour,stock_or_mto,qc_pass,packed_date,dispatched_date,carrier,tracking,delivered_date,on_time(Y/N),issue`

Weekly KPIs (to `kpi-weekly.csv` row, via owner): on-time dispatch = dispatched by promised date / orders;
fulfilment errors = wrong/missing/damaged / orders; fulfilment cost per order = shipping + packaging.

## Guardrails

- Agent never buys labels, marks orders fulfilled, edits stock, or emails customers. It drafts; humans act.
- Never promise a delivery date beyond carrier-stated transit. Never invent tracking or carrier rates.
- Refunds, reships and compensation = owner decision.

## Sources

- Chaser, "Order fulfillment checklist for ecommerce teams" https://www.trychaser.com/checklist-articles/order-fulfillment-checklist-for-ecommerce-teams
  — (c) Chaser, no licence; ideas only (payment/fraud check before picking, address validation, out-of-stock
  notice within 1 business day with options, act on carrier exceptions early). Winner: best fit for a tiny
  in-house team.
- Compared: Shopify "Order fulfillment checklist" https://www.shopify.com/blog/order-fulfillment-checklist
  (proprietary; generic), Docsie fulfilment SOP template https://www.docsie.io/assets/templates/retail-ecommerce/ecommerce-order-fulfillment-sop/template.pdf
  (template, licence unclear; used only as section skeleton idea), Opulo SOP (page 404 at fetch time).
  No Claude SKILL.md for fulfilment found worth adopting.
- Stages: Autumn & Wool `business-os/README.md` s.6; delivery facts: `implementation-report.md`, PROJECT-HANDBOOK s.5.
