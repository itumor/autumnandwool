# Finance plan, Q4 2026 and 2027 — DRAFT for owner approval

Owner of this plan: `aw-finance` (prepares and flags). The accountant books, reconciles and files. The owner decides.
Written 2026-10-21. Not accounting, tax or investment advice; the accountant has the final word.
Rules: no invented costs, balances, stock or sales. Unknown = `TODO: <who>` or `[VERIFY]`. EUR, ISO dates.
Labels: **Actual** (from a file), **Target** (goal, owner to approve), **Illustrative** (example only, not real).

---

## 1. Starting point (facts)

| Fact | Value | Source |
|---|---|---|
| Real direct-store orders to date | **0**. Two test orders #00003/#00004, both refunded; exclude from sales | `weekly-measurement-report-2026-10-19.md`, `PROJECT-HANDBOOK.md` s7 |
| Traffic, 30 days to 2026-10-18/19 | 62-64 visits, 94-96% bounce, Google 2 visits, Instagram/Pinterest 0 | `zero-sales-diagnosis-2026-10-18.md`, `weekly-measurement-report-2026-10-19.md` |
| Search (GSC 90d) | 11 clicks, 388 impressions, CTR 2.8%, position 14.1 | `weekly-measurement-report-2026-10-19.md` |
| Root cause of no sales | Click-trap overlay, CSS fix live 2026-10-19; checkout and Stripe proven | `PROJECT-HANDBOOK.md` s1, s4, s5 |
| Payments | Stripe live (card, Google Pay). **PayPal not connected** (owner action B1) | `owner-action-pack-2026-10-19.md` |
| Measurement | GA4 has pageviews only. No purchase events (plan gate). Orders and revenue must come from Squarespace Orders + Etsy exports | `weekly-measurement-report-2026-10-19.md` |
| Merchant Center | 98 rows under review, 0 approved, approval expected from 2026-10-21 | `PROJECT-HANDBOOK.md` s5, s9 |
| Unit economics | `unit_economics.py --selftest` ok. **0 costed / 82 TODO (22 visible TODO)** (run 2026-10-21). Break-even CAC is unknown for every SKU | `business-os/sku-economics.csv`, `unit_economics.py` |
| Weekly KPI sheet | Header only, **no data rows** | `business-os/kpi-weekly.csv` |
| Opening cash balance | **UNKNOWN. Never assumed.** Forecast shows net change only until the owner supplies a bank balance and date | skill rule, `aw-cash-flow` |
| Fixed costs | Not listed by owner. README s8 cap of EUR 100-250/month (example EUR 150) is **illustrative** | `business-os/README.md` s8 |
| Prices (visible range, no costs) | Beanie EUR 45, hat+scarf set EUR 110, sweaters EUR 110-165, cardigans EUR 145-160, vest EUR 126, gift card from EUR 25 | `markets-and-gift-guides.md` |
| Stock | Export of 2026-10-17, may be stale. Turtleneck 360 / beanie 220 need owner confirmation | `ai-team.md` owner decisions, `sku-economics.csv` |
| Etsy/Mareshop | ~8.2k sales, 1.5k reviews. Historical proof only. Not a forecast base for the direct store | `README.md` s2 |
| Tax | Latvia VAT 21% assumed in the sheet. OSS status and VAT per destination: unknown | `sku-economics.csv`, TODO: accountant |
| Pending cost-like items | Christmas market stall fees (mostly unpublished), Squarespace plan upgrade, MailerLite, ad tests: none priced | `markets-and-gift-guides.md`, `README.md` s8 |
| Shipping | Site advertises free shipping, EU-19 + UK/NO/CH services at 4-10 days. Carrier cost per region unknown, so free shipping is an unpriced variable cost | `PROJECT-HANDBOOK.md` s5 |

Consequence: finance cannot yet say what any sale earns, what a customer may cost, or how much cash exists.
The plan starts by closing those three gaps. No revenue target is set until real conversion, margin and CAC exist
(`README.md` s10).

---

## 2. Q4 2026 (2026-10-21 to 2026-12-31): peak gift season

Theme: **get costed, get measured, stay solvent through the season.** Orders may arrive late in the season;
cash and margin discipline matter more than forecasting revenue.

### Goals and numeric targets (Target; owner approves)

| # | Goal | KPI and target | Deadline |
|---|---|---|---|
| F1 | Cost the visible SKUs | 22 of 22 visible SKUs with all five cost columns filled (owner/Production supplies; Finance proposes, owner writes to CSV) | First 5 priority SKUs by 2026-10-28; all 22 by 2026-11-11 |
| F2 | Minimum contribution per order | One owner-approved EUR figure. Finance proposes a number once 5 SKUs are costed | 2026-11-04 |
| F3 | Opening cash and buffer | Owner supplies bank balance + date. Owner approves buffer. Proposed buffer = 8 weeks of fixed costs (EUR TODO) | 2026-10-28 |
| F4 | 13-week cash forecast | Rolled every Monday; Base and Downside; closing balance at or above buffer in all 13 weeks. Flag first week below buffer and below zero | First draft 2026-10-26, then weekly |
| F5 | Weekly KPI rows | `kpi-weekly.csv` baseline row for week of 2026-10-19 plus every Monday after. 100% of money columns sourced or marked TODO | First row 2026-10-26 |
| F6 | Accountant pack | October pack complete and tied out 5 working days before the accountant's deadline (TODO: accountant gives deadline) | 2026-11-06 (Oct), 2026-12-04 (Nov), 2027-01-08 (Dec) [VERIFY] |
| F7 | Spend guardrail | 0 euros of paid ads or creator cost committed unless: SKU costed, CAC below break-even, capacity GREEN, forecast stays above buffer, owner approves | Always |
| F8 | Payment path checks | PayPal connected (owner), test order + refund booked as excluded, payout schedule documented | PayPal by 2026-10-31 (owner) |

### Weekly actions (every Monday)
1. Collect exports from owner: Squarespace Orders, Etsy orders, Stripe payouts/balance, bank movement, ad/creator log. List what is missing.
2. Draft `kpi-weekly.csv` row in the WBR draft: net revenue ex VAT = (gross - returns)/1.21, contribution, CAC. Owner appends. Never estimate.
3. Roll the cash forecast `business-os/reviews/cash-forecast-YYYY-MM-DD.md`; variance vs last week; explain gaps over EUR 100.
4. Check campaign CAC against break-even CAC from `unit_economics.py`. Any campaign over break-even = stop/fix flag to GM.
5. Anomaly list: refunds, duplicate orders, fee mismatches, payouts missing. Flag only; do not correct.

### Monthly actions
- By the 3rd working day: accountant pack for the previous month (`accountant-pack-YYYY-MM.md`): documents checklist, tie-out (orders vs payout lines, refunds, platform fees), questions.
- Monthly finance review (`monthly-finance-YYYY-MM.md`): cash, payroll (if any), profitability by SKU and channel.
- Real test order + refund each month (README s5): record for tie-out so it is not read as sales.

### Q4 calendar
| Date | Action | Who |
|---|---|---|
| 2026-10-21 | Plan filed. Cost-collection request for 22 visible SKUs sent to owner (owner sends to Production/self) | Finance drafts, owner sends |
| 2026-10-24 | First measurement check: Merchant Center approved count, any real order | GM / Finance review |
| 2026-10-26 | First cash forecast (net change only if no opening balance) and first KPI row | Finance |
| 2026-11-04 | Minimum contribution decision | Owner |
| 2026-11-10 | KuKu Tirgus application window closes (EUR 50 craft fee) | Owner decides; Finance checks cash |
| 2026-11-27 | Old Riga Christmas market opens; stall price unpublished | Owner decides; see section 5 |
| 2026-12-14 | White Xmas booking closes; Baltic EXPO 11-13 Dec (fee non-refundable) | Owner decides |
| 2026-12-31 | Year-end: accountant pack, inventory count for year-end valuation [VERIFY: accountant] | Owner + Finance |

(Market dates and fees: `markets-and-gift-guides.md`, as of 2026-10-19; fees mostly TODO.)

### Q4 spend checks Finance must answer (each as "affordable now / after week N / no", lowest balance shown)
| Request | Cost | Status |
|---|---|---|
| Squarespace plan upgrade (unlocks Code Injection, GA4 purchase events, Clarity) | EUR TODO (check current pricing page, cite date) | Priced against one month of blind ad spend (README s8). Recommend decide before any paid test |
| Christmas market stall(s) | KuKu EUR 50; others TODO | Stalls also need stock on hand and cash-register records [VERIFY accountant] |
| Meta/Google/PMax test (idea 52 suggests EUR 5-10/day) | **Not approved.** Cost TODO | Blocked until SKUs costed and purchase events verified |
| Creator gifting | Product cost + shipping per gift: TODO | Count gifted product as a cost, not as zero |
| Yarn for restock | TODO: Production | Needs the stock truth first |

### Q4 downside rules
Downside scenario: sales at 50% of base, payouts one week later, one unplanned cost. With a zero-sales base, the
Downside is driven by fixed costs and committed spend. If the buffer is breached in any week, Finance flags it to
the owner on that Monday and recommends pausing uncommitted spend. It does not pause anything itself.

---

## 3. 2027 by quarter

Revenue targets stay **TODO** until at least 4 weeks of real conversion, margin and CAC exist. Targets below are
process and discipline targets; numeric revenue/cost lines get filled after Q4 actuals.

### Q1 2027 (Jan-Mar): close the year, reset the baseline
- **Goals:** clean 2026 year-end; post-season review of what the season really earned; unit economics based on actuals, not estimates.
- **KPIs:**
  - 2026 year-end pack to accountant by 2027-01-15 [VERIFY deadline].
  - 100% of 82 SKUs costed or explicitly retired (visible SKUs first; already 22 in Q4).
  - Actual contribution per order reported for every SKU sold; CM2 vs minimum contribution flagged.
  - Forecast variance: weekly closing balance within EUR 100 of forecast (or explained) in at least 10 of 13 weeks.
- **Initiatives:**
  1. Season post-mortem by SKU and channel (site, Etsy, markets): CM1, CM2, CM3.
  2. Reconcile Etsy fees and payouts vs statements; decide with the accountant how to book them.
  3. VAT/OSS review with the accountant: EU distance-sales threshold position, destination VAT rates, UK/NO/CH/US treatment [VERIFY].
  4. Returns data: replace the owner's returns allowance assumption with observed returns.
  5. Decide the 2027 budget envelope and buffer with the owner.
- **Budget ask:** accountant fee TODO (owner); software cap (illustrative EUR 100-250/month, README s8); inventory/yarn: TODO Production; paid tests: TODO, only if Q4 data supports.

### Q2 2027 (Apr-Jun): prove channels
- **Goals:** know the CAC and payback of each channel tested; fund only channels with CM3 above the minimum.
- **KPIs:**
  - CAC per channel computed from new customers (never blended); each channel has a verdict: scale / hold / stop.
  - Contribution after acquisition (CM3) positive on the tested SKUs, or the test is stopped.
  - Cash: closing balance above buffer in 13 of 13 forecast weeks for the approved plan.
  - Monthly accountant pack on time 3 of 3 months.
- **Initiatives:**
  1. Channel P&L: Squarespace, Etsy, Merchant Center free listings, social, creators, markets.
  2. Test budget caps tied to break-even CAC per SKU; weekly reviews with GM.
  3. Observed repeat rate from Squarespace + Etsy (LTV stays "unknown" until observed).
  4. Pricing proposals to the owner where CM2 is below minimum (proposals only; owner changes prices).
  5. Review payment fee mix (Stripe vs PayPal) from actual account rates, not remembered ones.
- **Budget ask:** ad/creator test pool: **EUR TODO (owner)**; plan upgrade if not done in Q4: EUR TODO.

### Q3 2027 (Jul-Sep): prepare for the season
- **Goals:** fund the Q4 2027 yarn and production build without breaching the buffer; avoid summer cash dip.
- **KPIs:**
  - Season purchasing plan with cash timeline by 2027-08-31: yarn paid before the sweater sells, payouts after the sale.
  - Forecast covers 13 weeks past the planned purchase dates; lowest balance reported with the Downside.
  - Sell-through by SKU (units sold / available) from Production data; slow SKUs flagged for the owner.
  - Gross margin per SKU vs Q2 actuals; variance over 5 percentage points explained.
- **Initiatives:**
  1. Stock and yarn purchase affordability checks with Production (reorder points, supplier lead times: TODO).
  2. Market and event calendar costed (stall fees, travel, packaging, permits) with expected CM from Q4 2026 market results.
  3. Mid-year profitability by SKU and channel; stop list for losing products.
  4. Hiring affordability checks against contribution (see `hiring-plan.md` wave order). A hire is affordable only if contribution after acquisition covers it with buffer intact.
- **Budget ask:** yarn/materials for season: TODO Production; hire costs: TODO owner; markets: TODO.

### Q4 2027 (Oct-Dec): season and year-end
- **Goals:** run the season on a tested plan; year-end ready 2 weeks earlier than 2026.
- **KPIs:**
  - Weekly cash forecast variance explained for every gap over EUR 100.
  - Contribution margin reported weekly in `kpi-weekly.csv`; no paid campaign above break-even CAC for more than one week without owner sign-off.
  - Closing balance above buffer all 13 weeks.
  - Year-end pack to accountant by 2027-12-31 plus stock count (target; accountant to confirm).
- **Initiatives:** season peak cash watch (weekly during Nov-Dec); promotion and discount impact on CM2; 2028 budget draft with owner by 2027-12-15.
- **Budget ask:** TODO, built from Q1-Q3 actuals.

### 2027 budget request summary (all values owner/accountant to supply)
| Cost line | Type | Amount | Source / owner |
|---|---|---|---|
| Accountant (bookkeeping, VAT, annual) | Fixed | TODO | Owner / accountant quote |
| Squarespace plan (current + upgrade option) | Fixed | TODO | Owner; check pricing page |
| Tools (MailerLite, Canva, AI usage) | Fixed | Illustrative cap EUR 100-250/month | `README.md` s8 (not a quote) |
| Payment fees (Stripe, PayPal, Etsy) | Variable | Rates TODO from actual accounts | Owner / dashboards |
| Shipping (free to customer, cost to us) | Variable | TODO by region | Owner / carrier rates |
| Materials and labour per SKU | Variable | TODO per SKU | Founder / Production |
| Packaging (care card, box) | Variable | TODO | Production / Operations |
| Paid ads and creator cost | Variable, capped | TODO, owner approves | Growth / Partnerships |
| Market stalls | One-off | KuKu EUR 50 (published); others TODO | `markets-and-gift-guides.md` |
| Salaries / contractors (waves 1-4 of hiring plan) | Fixed | TODO, only after contribution proven | Owner, `hiring-plan.md` |
| VAT / tax payments | Timing | Dates TODO | Accountant |
| EU consumer-law adviser (one-off) | One-off | TODO | Owner |

---

## 4. Dependencies on other departments

| Department | Finance needs | Finance gives |
|---|---|---|
| Head of E-commerce (GM) | Decisions on 5 priority SKUs, 2 test channels; spend approvals relayed to owner | Weekly money check of WBR; short findings with EUR impact; break-even CAC per SKU |
| Growth Marketing | Campaign spend, new customers per channel, UTM codes | Max CAC per SKU; stop/fix flags; cash check before any spend increase |
| Partnerships | Creator log: gifted items, fees, codes, orders | Creator cost per order and profit per creator; gifted stock counted as cost |
| Creative | Shoot, photo and freelancer costs; invoices | Budget tracking; contractor invoice checklist for the pack |
| CRO | Date PayPal live; plan upgrade decision; purchase events verified | Cost of upgrade vs blind spend; conversion cost baseline |
| SEO / Marketplace | Etsy statements and payouts; Etsy fees; Merchant Center status | Etsy channel P&L; tie-out Etsy payouts to orders |
| Production | Materials + labour per SKU, yarn per lot, supplier lead times, weekly capacity and safe-to-promote list, stock truth | Yarn purchase affordability; sell-through; margin per SKU |
| Operations | Shipping cost per region, packaging cost, dispatch log, returns log | Fulfilment cost per order; refund and return tie-out |
| CX | Refund requests and reasons (owner approves refunds) | Returns allowance replaced by actuals; refund cash impact |
| Owner | Bank balance + date, buffer, fixed-cost list, exports, accountant contact | Everything in this plan as drafts |

---

## 5. Risks and owner decisions

### Risks (ranked by likely EUR impact)
1. **Unpriced free shipping.** Free shipping to EU, UK, NO, CH, US with no carrier cost known. One heavy sweater to a far zone may erase CM2. EUR impact TODO per region. Mitigation: carrier rates first (Operations); consider shipping thresholds as a proposal.
2. **Spend before measurement.** Paid ads before costs and purchase events exist can burn cash with no way to judge them. Mitigation: F7 guardrail.
3. **Inventory and market commitments.** Stall fees (Baltic EXPO non-refundable) and yarn bought for a season with 0 proven orders. EUR TODO. Mitigation: affordability check before booking; start with the lowest-cost market.
4. **VAT/OSS errors.** The sheet assumes 21% for all. Distance sales to other EU countries may need destination VAT; UK/NO/CH/US differ [VERIFY with accountant]. Wrong VAT misstates net revenue and margin.
5. **Stale or placeholder stock.** 360 turtlenecks and 220 beanies look like placeholders; planning on them overstates what can be sold or what is tied up in stock.
6. **Test orders and refunds in the books.** #00003/#00004 refunded. Tie out so they are not counted as sales; flag any payout line that does not match.
7. **Payment fees and payout lag.** Stripe payout timing not documented; PayPal not connected; Etsy payout schedule unknown. Cash may arrive later than the sale.
8. **Sparse data.** With about 2 visits a day, any early conversion rate is noise. Do not set revenue targets or judge channels on a handful of orders.

### Owner decisions needed
| # | Decision | Needed by | Finance proposal |
|---|---|---|---|
| 1 | Provide opening bank balance + date | 2026-10-28 | Forecast shows net change only until given |
| 2 | Approve cash buffer | 2026-10-28 | 8 weeks of fixed costs (EUR TODO once the fixed-cost list exists) |
| 3 | Supply fixed-cost list (plan, tools, accountant, salaries) | 2026-10-28 | One sheet; replaces the illustrative README s8 |
| 4 | Fill costs for 22 visible SKUs; confirm stock | 5 SKUs by 2026-10-28, all by 2026-11-11 | Finance sends the request list, owner writes the CSV |
| 5 | Minimum contribution per order | 2026-11-04 | Proposal after 5 SKUs costed |
| 6 | Squarespace upgrade yes/no | 2026-11-04 | Decide before any paid test; price from current pricing page [VERIFY] |
| 7 | Free shipping policy vs cost | 2026-11-11 | Review once carrier rates arrive |
| 8 | Markets: which, if any | KuKu 2026-11-10; Baltic EXPO ASAP (limited spots); White Xmas 2026-12-14 | Affordability check per stall, with stock |
| 9 | Test-spend cap (ads + creators) | After items 4-6 | EUR TODO; only on costed GREEN SKUs |
| 10 | Connect PayPal | 2026-10-31 | Owner action pack B1 |
| 11 | Accountant: VAT/OSS position, Etsy fee booking, deadlines, stall/cash-register rules | 2026-11-06 | Question list in the October pack; owner sends |
| 12 | 2027 budget envelope | 2027-01-31 | Draft from Q4 actuals |

Not accounting, tax or investment advice. All items above are drafts; nothing here has been sent, paid or booked.
