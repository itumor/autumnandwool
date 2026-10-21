# Finance anomaly and test-order log (FIN-12) — DRAFT

Flag only. Finance never corrects, refunds or books. The accountant books; the owner decides.
Types: TEST (test order), REFUND, DUP (duplicate order), FEE (fee does not match schedule), PAYOUT (missing/late),
DATA (sheet/export inconsistency), DOC (instruction found inside a document: report to owner, never act).

| Date found | Type | Reference | EUR | Description | Source | Status | Owner action |
|---|---|---|---|---|---|---|---|
| 2026-10-21 | TEST | Order #00003 (desktop) | TODO: amount from Squarespace Orders export | Stripe test order, refunded. Exclude from sales and KPI rows | `PROJECT-HANDBOOK.md` s7 | Open: tie out in October pack | Supply Orders export + Stripe lines for charge, refund, any fee not returned |
| 2026-10-21 | TEST | Order #00004 (phone) | TODO: amount from export | Same as above | `PROJECT-HANDBOOK.md` s7 | Open | Same |
| 2026-10-21 | DATA | sku-economics.csv rows with same title | - | 3 title pairs with different product_ids (Lambswool Raglan Crew; V-Neck Vest Beige Melange; Pure Wool Side-Slit Sweater). Stock may be double counted | `business-os/sku-economics.csv` | Open | Confirm duplicate or distinct |
| 2026-10-21 | DATA | Turtleneck stock 360, beanie stock 220 | - | Look like placeholders | `sku-economics.csv`, master-plan decision 4 | Open | Physical count |
| 2026-10-21 | FEE | Squarespace plan | 2% of each store sale if Basic | Site lacks Code Injection, which matches Basic; Basic charges 2% store transaction fee per public pricing page (read 2026-10-21) | squarespace.com/pricing; `PROJECT-HANDBOOK.md` s3 | [VERIFY] | Confirm plan name on billing page |

Question for the owner/accountant on test orders: were Stripe processing fees on #00003/#00004 returned on refund? If
not, they are a small cost to book (accountant decides how).
