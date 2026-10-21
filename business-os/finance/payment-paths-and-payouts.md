# Payment paths, payouts and test-order tie-out (FIN-14, plan goal F8) — DRAFT

Read-only record. Finance never logs into Stripe, PayPal, Etsy, Squarespace or the bank; owner fills from screens/exports.

## Payment paths
| Path | State | Source | Payout schedule | Fee rate on the account | Owner to fill |
|---|---|---|---|---|---|
| Stripe (card, Google Pay) via Squarespace | Live, proven with #00003/#00004 (refunded) | `PROJECT-HANDBOOK.md` | TODO | TODO (public list: EEA std 1.5% + EUR 0.25, read 2026-10-21, stripe.com/en-lv/pricing) | Schedule + actual fee line from one charge |
| PayPal | Not connected (owner action B1, due 2026-10-31) | `owner-action-pack-2026-10-19.md` | TODO | TODO | After connect |
| Squarespace store transaction fee | 2% if Basic plan [VERIFY plan] | squarespace.com/pricing read 2026-10-21 | Deducted how? TODO | 0% on Core/Advanced | Plan name |
| Etsy Payments (Mareshop) | Active status unconfirmed (master-plan decision 9) | `README.md` s2 | TODO | TODO (from Etsy statement) | Monthly statement |
| Market cash/card (if a stall is booked) | Not set up | `markets-and-gift-guides.md` (MyExpo asks for cash register / receipt book) | - | - | Accountant: register rules |

## Real test order + refund each month (README s5) — record template
| Date | Order # | Path (Stripe/PayPal) | Amount EUR | Fee charged EUR | Fee returned on refund? | Refund date | Payout line ref | Excluded from KPI row? |
|---|---|---|---|---|---|---|---|---|
| TODO (Oct) | #00003 | Stripe | TODO | TODO | TODO | TODO | TODO | Yes |
| TODO (Oct) | #00004 | Stripe | TODO | TODO | TODO | TODO | TODO | Yes |
| after 2026-10-31 | PayPal test (owner places + refunds) | PayPal | | | | | | Yes |

## Payout tie-out steps (monthly, for the accountant pack)
1. List Squarespace orders for the month (excluding TEST rows in `anomaly-log.md`).
2. Match each to a Stripe/PayPal charge; charge - fee = net; sum nets per payout; payout = bank credit.
3. Any order without a charge, charge without an order, payout not in bank, or fee off the account rate -> `anomaly-log.md`.
