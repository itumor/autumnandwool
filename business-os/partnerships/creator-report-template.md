# Creator programme reports: templates (DRAFT, PAR-16)

Status: DRAFT templates. Filled from `creator-tracker.csv` and Squarespace Orders only. Zero is a valid result and
is reported as zero. No invented numbers. The figures feed the GM's weekly review. The `creator_cost_eur` line in
`kpi-weekly.csv` is entered by Finance/GM, not by Partnerships.

## 1. Monthly creator report (first: mid-Dec 2026, November data)

```
# Creator report <month yyyy>: DRAFT
Funnel: shortlisted __ | contacted __ | replied __ | agreed __ | shipped __ | posted __ (post rate __% of shipped)
Disclosure: __ of __ posts compliant (fixed: __, open: __)
Assets with written usage rights: __ (organic __, organic+ads __)

| Creator | Deal | Gift cost EUR | Commission EUR | Total cost EUR | Sessions (GA4) | Orders (code/name) | Net rev ex VAT EUR | Contribution after cost EUR | Cost per order EUR | vs BE_CAC | Decision |
|---|---|---|---|---|---|---|---|---|---|---|---|

Totals: cost __ | orders __ | cost per attributed order __ vs break-even CAC __ (SKU: __)
Platforms claim N, we can verify M.
Decisions proposed: repeat / ambassador / affiliate / close (one reason each)
MISSING:
```

Definitions:
- Total cost = gift cost (materials+labour+packaging+shipping) + commission + any approved fee.
- Contribution after cost = net revenue ex VAT minus variable costs of the orders (from `unit_economics.py`) minus total cost.
- Rule (`aw-creator-outreach` s1): total creator cost per attributed order must stay <= the SKU's break-even CAC
  within 60 days of shipping. Over that: stop or change the deal.

## 2. Q4 readout (31 Dec 2026)
Same table for the quarter, plus: what worked (SKU, creator type, format), what didn't, learning on post rate and
reply rate, owner time spent (hours, estimate), recommendation for January (pause / light-touch).

## 3. Day-90 programme verdict (by 31 Jan 2027)

```
Question: does gifting (or gift + code) acquire customers below break-even CAC?
Evidence: orders verified __ from __ creators; cost per order __ vs BE_CAC __; confidence __
Verdict: continue as is / change deal (cheaper SKU, code, affiliate) / stop
Wave 2 terms proposed: deal model, gift SKU and cap, code %, commission (if any), usage-rights default
Hire signal (hiring-plan wave 4): yes / not yet, with reason
```
