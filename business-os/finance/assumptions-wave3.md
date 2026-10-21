# Finance assumptions register, wave 3 — DRAFT for owner

Author: aw-finance (agent), 2026-10-21. ASSUMPTION MODE (owner-approved 2026-10-21). **Every value below is an ASSUMPTION,
not a fact.** It covers only the values the three shared registers do not have. Shared baselines used first, and their
values win over anything here:
- Production `business-os/knitwear-making/assumptions-wave3.md` (A-PRD: costs, labour EUR 12/h, stock rule)
- Operations `business-os/operations/assumptions-wave3.md` (A-OPS: shipping LV 5 / EE-LT 6 / EU 22 / US-CA-AU 28, packaging 1.50, US duty)
- GM `business-os/head-of-ecommerce/assumptions-wave3.md` (A-GM: Basic plan, min contribution EUR 10, buffer scenarios, returns 5%, rulings W3-1..4)

Cite as `ASSUMPTION A-FIN-xx; register: business-os/finance/assumptions-wave3.md`. Nothing here was written to
`sku-economics.csv`, `kpi-weekly.csv`, the store or any account. Not accounting, tax or investment advice; the accountant
has the final word on VAT/OSS and bookkeeping.

| A-ID | Value | Basis / URL (read 2026-10-21) | Range | Conf. | Task IDs | Owner confirms by |
|---|---|---|---|---|---|---|
| A-FIN-01 | Payment cost, **EEA card orders** (LV, EE/LT, EU) = **price x 4.8% + EUR 0.25**: Stripe EEA premium card 2.8% + EUR 0.25, plus Squarespace Basic 2% store fee on the price incl. VAT | https://stripe.com/en-lv/pricing ; https://www.squarespace.com/pricing ; plan = Basic per A-GM-05. Premium rate chosen as the safe (higher) case | Low: Stripe EEA standard 1.5% + 0.25, no store fee (Core plan) = EUR 0.92-2.73 per order; high as stated = EUR 2.41-8.17 | M (public list rates; account rates unknown) | FIN-03, FIN-05, FIN-18, FIN-19 | 2026-10-28 (Billing screenshot + one Stripe fee line, form rows 3-4) |
| A-FIN-02 | Payment cost, **US/CA/AU card orders** = **price x 5.15% + EUR 0.25**: Stripe international card 3.15% + EUR 0.25, plus Squarespace 2%. No Stripe FX fee assumed because the store charges EUR (the card issuer converts) [VERIFY] | Same URLs. Stripe adds 2% if Stripe converts currency | +2% if Stripe converts (EUR 0.90-3.30 more per order) | M | FIN-03, FIN-18 | 2026-10-28 |
| A-FIN-03 | **VAT basis: net revenue = price / 1.21 for every zone, US/CA/AU included** (the same basis as `sku-economics.csv` and the GM's CM2 file). This is a conservative planning basis. **It is not a VAT treatment.** | `sku-economics.csv` vat_rate 0.21; the VAT registration status, OSS and export zero-rating are accountant questions (`accountant-questions-2026-10-21.md` Q1) | US/CA/AU if exports are zero-rated: net = price. CM2 rises by about 13.9% of price (the extra net, less duty and the 5% returns on the larger base) = EUR 6.25 (beanie) to 22.92 (EUR 165 sweater). EU other at destination VAT 17-27% (OSS): CM2 moves by -3.9% to +2.8% of price, about -6.05 to +4.38 on a EUR 155 sweater | L | FIN-03, FIN-18 | Accountant, via owner (form row 18) |
| A-FIN-04 | **Market-stall sale costs**: card reader fee proxy 2.8% + EUR 0.25 (no reader chosen, no quote), packaging EUR 1.50 (A-OPS-10), no shipping, no Squarespace fee, no returns allowance. Stall fee KuKu Tirgus **EUR 50.00** (published; whether it includes VAT is unknown). Staffing = owner's own time, not costed | KuKu fee: `spend-checks-q4-2026.md` s2; stall = A-GM-15 | Fee 2.8% to 1.69% (no quote read); cash sales 0% | L | FIN-17 | 2026-11-10 (stall choice, form row 15) |
| A-FIN-05 | **Gift-note perk cost: EUR 0.90 per gift order**: card + envelope EUR 0.30 (agent estimate, no quote) + 3 min handwriting at EUR 0.20/min (A-PRD-01). Gift wrap EUR 0 (not offered, A-GM-22). Prices left off the packing slip EUR 0 | A-GM-22 perk set | 0.40-1.50 | L | FIN-19 | 2026-11-14 (decision 31) |
| A-FIN-06 | **Committed spend in the 13 weeks = EUR 0**: no paid test (A-GM-08), no yarn order (A-GM-27), no hire (A-GM-29), backup site lapses (A-GM-23), stall not booked (A-GM-15). Creator gifts: 5 beanies at landed cost (A-GM-17) are **not committed** until the owner approves each gift | GM register rows listed | Gifts 5 x about EUR 20 = about EUR 100 if all approved (LV landed: M+L 13.33 + pack 1.50 + ship 5.00) | M (follows the GM register) | FIN-07, FIN-17 | 2026-10-28 (form row 5) |

## GM rulings applied (W3-13, W3-14; GM 2026-10-21, owner confirms)
| Ruling | Finance handling |
|---|---|
| W3-13 shipping policy (assumed; owner changes store settings): LV/EE/LT free; EU other free from EUR 150 basket, else flat EUR 12.00; US/CA/AU flat EUR 15.00, not promoted, no paid traffic; RoW no promise | New section "W3-13 policy" in `sku-margins-assumed-wave3.md` + 8 `w313_*` columns in the CSV. Charge treated as revenue incl. 21% VAT (A-FIN-03 basis), so payment fee and 5% returns apply to it; carrier cost unchanged; no US duty on the charge [VERIFY]; basket rule per single-item order. Free-shipping table kept for comparison |
| W3-14 minimum contribution | **Stays EUR 10** (A-GM-20, Mid case). Trigger: owner's fixed-cost list >= EUR 200/month -> **EUR 15**. Applied in FIN-05 and the margins file; at EUR 15 the EU-other count >= line falls 13 -> 9 and US/CA/AU to 0, Baltic ranking unchanged |

**Not assumed, ever (stay with the owner):** bank, Stripe, Etsy and PayPal balances; payout dates and lags; VAT return
dates; the accountant's deadlines. Those tasks stay BLOCKED or use conditional verdicts ("affordable if balance >= ...").

## Cross-register notes (no conflict with a GM ruling; flagged for GM)
| # | Note | Finance handling |
|---|---|---|
| F-1 | GM CM2 file uses the EEA rate (4.8%) for US/CA/AU orders | I use A-FIN-02 (5.15%). US CM2 is EUR 0.40-0.56 lower than in GM's file. The sign and the verdict do not change |
| F-2 | Production's file says "13 of 22 SKUs below 40% CM1". The same inputs give **14**: the list is rows 1-7, 9-14, 21-22 of the table in `sku-margins-assumed-wave3.md`, which is 14 because the stand-collar pair (21-22) is counted | Finance figure: 14. Production to re-count |
| F-3 | Stock rule A-PRD-12 is applied per listing. A-PRD-13 says duplicates share one pool (larger listed number), never the sum | Margins file shows per-listing stock and a pooled total |

DRAFT for owner. Assumptions, not facts. Nothing sent, nothing paid, nothing written to shared CSVs.
