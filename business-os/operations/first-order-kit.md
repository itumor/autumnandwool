DRAFT — for owner approval. PRE-DRAFT for OPS-15; becomes live on the day of the first real order.

# First real order: what happens on day 0 (OPS-15 kit)

Agent `aw-operations`, 2026-10-21. Joins the wave-1 outputs of three departments so the first order runs without
improvising: OPS SOP + dispatch checklist, CX support macros, Finance payment-path record, CRO test-order
checklist. The agent drafts; the owner touches orders, labels, parcels, emails and refunds.

Sources: `sop-order-to-delivery.md`, `dispatch-checklist-template.md`, `dispatch-log-template.csv`,
`returns-handling.md` (this folder); `business-os/customer-experience/support-macros.md` (macros 3, 4, 7, 8, 14),
`business-os/customer-experience/triage-and-case-template.md`; `business-os/finance/payment-paths-and-payouts.md`;
`business-os/ecommerce-cro/2026-10-21-test-order-checklist-november.md`.

## 1. Trigger

First Squarespace or Etsy order that is **not** a test order (tests: #00003, #00004 and every CRO/Finance monthly
test order, which are refunded and excluded from KPIs). Owner tells the agent "order #__ in" with a screenshot or
export line. The agent never reads the store itself.

## 2. Day-0 steps

| # | Who | Step | File |
|---|---|---|---|
| 1 | Agent | Create `dispatch-log.csv` from `dispatch-log-template.csv` (proposed; owner saves) and the first `dispatch-YYYY-MM-DD.md` from the checklist template | this folder |
| 2 | Agent | Compute promised_dispatch_by = order date (next working day if after cut-off) + promised working days. Until owner item 1/3 answered: 5 working days, 12:00 cut-off, both marked [VERIFY] | owner form items 1, 3 |
| 3 | Owner | Confirm: paid (Stripe/PayPal), address complete (flat no., postcode, phone for lockers), item/size/colour | SOP stage 1 |
| 4 | Owner | Stock unit on shelf? Tag it with the order no. Otherwise made-to-order: give the due date | SOP stage 2 |
| 5 | Agent | If the due date misses the promise: draft CX macro 4 DELAY the same day, with [OWNER DECISION] on options | CX macro 4 |
| 6 | Owner | QC (11 checks), pack, weigh, photo, buy label, hand over, mark fulfilled with tracking | SOP stages 3-5 |
| 7 | Agent | Record label_cost_eur and packaging_cost_eur from the receipt the owner shares (state incl./excl. VAT) | log |
| 8 | Agent | Tracking sweep every 2nd working day; exception = CX macro 3 ORDER_STATUS (A dispatched) draft before the customer asks | SOP stage 6 |
| 9 | Agent | Delivered date logged = start of the 14-day withdrawal clock | `returns-handling.md` |
| 10 | Agent | Ask Finance for the payment fee on this charge (record template in `payment-paths-and-payouts.md`) so the KPI cost column is complete | Finance |

## 3. Which draft to use (SOP exception -> CX macro)

| Situation | SOP section | CX macro | Owner decision? |
|---|---|---|---|
| Customer asks "where is my order" | stage 6 | 3 ORDER_STATUS (A dispatched / B not yet) | No, unless late |
| Made-to-order will miss the promise | stage 2 | 4 DELAY | Yes: wait / switch / cancel + refund |
| Stuck > 5 working days, lost | delivery problems | 3 ORDER_STATUS + [OWNER DECISION] | Yes: reship or refund |
| Damaged on arrival, wrong item | delivery problems | 8 DAMAGED / FAULTY / WRONG ITEM | Yes |
| Return / withdrawal | `returns-handling.md` | 7 RETURN_START (return address = owner item 10) | Yes |
| December "where is my order" | stage 6 | 14 GIFT_SEASON_WISMO | Only if late |

Wording rule: macros carry the customer text; the SOP appendix drafts (A1-A3) are only the fallback when CX is
not available. If the two disagree, CX's version wins on tone, the SOP wins on dates and facts.

## 4. After the first order is delivered

- First full ops weekly file the next Monday (KPIs with real counts, cost per order by region).
- Propose actual label + packaging cost to Finance for the `shipping_eur` / `packaging_eur` columns (Finance
  stages it in `sku-cost-proposals-staging.csv`; the agent never edits `sku-economics.csv`).
- Any improvised step becomes an SOP edit proposal.

## TODO / missing data

- Owner form `owner-inputs-wave2.md` items 1, 3, 4, 10, 12, 16 (promise, cut-off, carrier, return address,
  packaging, tracking email).
- Whether the Squarespace "fulfilled" email includes tracking (item 16): until known, the owner sends tracking by
  hand using macro 3A.
