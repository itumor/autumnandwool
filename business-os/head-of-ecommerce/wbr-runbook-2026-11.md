# Weekly WBR + gate-tracker runbook (loop), Mondays 2026-11-02 to 2026-12-28

Author: Head of E-commerce / GM (agent), 2026-10-21. Task GM-11 (Head of E-commerce, plans/2026-2027/status/head-of-ecommerce.md).
GM-07 (first WBR, week of 2026-10-19) is still blocked on the owner Monday data batch, so this file is the
**reusable runbook + empty skeleton** rather than a filled report. It contains no orders, revenue or sessions and
no KPI number. Every number enters only from the owner export on Monday morning.

Replaces the ad-hoc pre-fill (`business-os/head-of-ecommerce/wbr-2026-10-26-prefill.md`) for all Mondays from 2 Nov 2026.
Per-week output path: `business-os/reviews/wbr-YYYY-MM-DD.md` (with `week_start` Monday). `business-os/reviews/`
does not exist yet; create it on the first run or copy the skeleton folder. Same template each week; the 26 Oct run
is the first concrete instance.

Linked prepared drafts (fill evidence from these):
- `business-os/head-of-ecommerce/wbr-template-and-agenda-2026-10-26.md` (section 3 template, skill `aw-weekly-business-review`)
- `business-os/head-of-ecommerce/wbr-2026-10-26-prefill.md` (assumption-mode pre-fill pattern, used only until data clears)
- `business-os/head-of-ecommerce/min-contribution-assumed-2026-10-21.md` (GM-12; CM2 tables feed the scorecard)
- `business-os/head-of-ecommerce/plan-upgrade-memo-prep-2026-10-21.md` (GM-13; plan/codes status feed G7)
- `business-os/head-of-ecommerce/gate-tracker.md` (G0-G9 definitions and chain; update here each Monday)
- `business-os/head-of-ecommerce/owner-unblock-pack.md` (full owner action checklist, ranked)
- `business-os/head-of-ecommerce/market-stall-prep-2026-10-21.md` (market cash verdict, feeds GM-15)
- `business-os/head-of-ecommerce/assumptions-wave3.md` (A-GM rows; every draft still cites its A-ID)

Loop window: 9 Mondays - 2, 9, 16, 23, 30 Nov, 7, 14, 21, 28 Dec 2026. Idempotent: run the same Monday's file
again after the data batch arrives rather than creating a second one.

## 0. Rules that never change
- Orders and revenue come from Squarespace Orders and Etsy only. GA4 shows sessions. **Never** fill a revenue or
  order cell from GA4. (HARD RULE 5.)
- Unknown = blank + `TODO: <who supplies it>`. Never invent costs, stock, orders, sessions, CAC, conversion, margin.
  (HARD RULE 4.)
- GM never edits `business-os/kpi-weekly.csv` or `business-os/sku-economics.csv`. Propose a row in the WBR; the
  owner pastes it only after the data arrives and G1 is cleared on cost rows. (HARD RULE 6.)
- A gate shows `CLEARED` only with evidence (export, screenshot, file). Anything unpaid stays at EUR 0 until then.
- Thrift rule: every new cell is either written by the owner, derived from cells the owner supplied, or blank.
  Assumed values that survived the 26 Oct WBR are marked `ASSUMED` with A-ID and must not be pasted later.

## 1. Monday run (30 minutes, owner + GM)
Run these steps in order. Do not skip a step; if data is missing, stop at step 3 and send the owner batch (step 7).

### Step 1 - Create the weekly file
Copy the empty skeleton in section 3 to `business-os/reviews/wbr-YYYY-MM-DD.md` with `YYYY-MM-DD` = that Monday
(e.g. `wbr-2026-11-02.md`). Fill the `week_start` in the CSV block with the previous Monday and `week` with the
6-letter code. Create `business-os/reviews/` if absent. At the top add the one-line status: "Data batch: pending".

### Step 2 - Owner data batch (owner, by 09:00 Monday, ~20 min)
Spec (identical every Monday, from `owner-unblock-pack.md` #10 and `wbr-template-and-agenda-2026-10-26.md` 1):
1. Squarespace Orders export, week Mon-Sun (e.g. 26 Oct - 1 Nov for the 2 Nov WBR), **excluding** test orders
   #00003 and #00004.
2. Etsy order count for the same week, or "Etsy closed".
3. GA4 `G-7TV8PK060Z`: sessions total and by source/medium, week matching the above. Screenshot accepted.
4. Ad and creator spend this week (confirm EUR 0 if nothing ran): Meta, Google, any creator cost.
5. Merchant Center: approved / pending / disapproved count (screenshot).
6. Any dispatch in the week (none expected until first sale; Ops log).

Output is the six rows the Owner Monday batch field reads. If any of 1-4 is missing, **leave the scorecard blank**
and mark "Data batch: incomplete" rather than guessing.

### Step 3 - GM fills the WBR from the batch only
Fill the scorecard headers from steps 2 (1)-(6). Derive `conversion_rate`, `AOV` and `CAC` only from those.
`Gross margin %` and `Contribution` stay `TODO: G1` until `unit_economics.py` shows costed SKUs. `Sell-through`
stays `TODO` until the physical count (decision 4). Do not use the Production register costs for the WBR even if
they are the only numbers in hand; label them `ASSUMED` only in a separate note, never in the CSV row.

### Step 4 - Skim department inputs (read-only; do not re-derive)
- `business-os/finance/` cash forecast for the week's opening/lowest-week numbers; per-department weekly notes if
  present; Production capacity lists; `aw-cro-audit` / SEO weekly notes when published.
- `business-os/growth/` weekly readout template output (`weekly-readout-template.md`).
- `business-os/operations/` `ops-weekly-YYYY-Www.md` readiness row.

### Step 5 - Live 30-min review (owner + GM)
Agenda (unchanged; from `wbr-template-and-agenda-2026-10-26.md` 2): 0-5 one line + scorecard, 5-12 controllable
inputs, 12-18 gate tracker G0-G9, 18-25 decisions (max 3), 25-30 owner Monday batch ordered by gate. Output:
`business-os/reviews/wbr-YYYY-MM-DD.md`, gate-tracker diff in `gate-tracker.md`, proposed CSV row in the file only.

### Step 6 - Gate tracker update
Open `business-os/head-of-ecommerce/gate-tracker.md`. Move a gate OPEN -> PARTIAL -> CLEARED only with evidence
from step 2 or a department file. Append one row to the `Date / Gate / From / To / Evidence` log table. Never mark
CLEARED from an owner yes that happened after the Monday, or from assumed data.

### Step 7 - Owner Monday batch (max 15-minute tasks, ordered by gate)
Copy the surviving week's unchecked items from `owner-unblock-pack.md` "Full checklist, by due date", filtered to
anything due this week or past due. Each row: action, due, time, unblocks task IDs. Cap 15 minutes of owner work.
Order: G0 before G1, G4 before traffic, G3 before any spend. Do not add new actions that are not in the unblock
pack; only re-order.

### Step 8 - Close the week
Fill "Re-baseline" boxes only after 4 weeks of data (GM-17, 23 Nov). Update `business-os/kpi-weekly.csv` only after
the owner pastes the row from step 5.

## 2. Fill instructions and legend
- Header/top: `One line: <single most important fact>` (examples below must be data-derived, never assumed).
  - Bad: "Store is growing."
  - Good: "Week of 2 Nov: <n> site orders, <m> Etsy orders, <x> sessions, <r> EUR revenue (owner export)."
- Scorecard flags: KPI change > 20% and > EUR 50, any order change at under 10/week, any gate past due. New-orders
  at these volumes are always a flag; expect that rather than reading it as a trend.
- `ASSUMED` values from `assumptions-wave3.md` may appear in a note inside the WBR only if they are explicitly
  labelled `ASSUMED` with the A-ID. They must not sit in the CSV row or in the one-line summary.
- Variances section: only flagged lines, one sentence each: what, evidence, likely cause, action, owner, due.
- Decisions section: max 3. Each row: decision, evidence, owner, by, reversible/approval.
- Owner Monday batch section: max 15 mins owner effort; ordered by gate.
- `Missing data / TODO`: blank cells with the owner or department that supplies them.
- Proposed `kpi-weekly.csv` row: blank cells unless the owner supplied them; assumed values stay out.

## 3. Weekly skeleton (copy verbatim into `business-os/reviews/wbr-YYYY-MM-DD.md`; edit nothing else)

```markdown
# WBR week of <YYYY-MM-DD> - DRAFT for owner

Author: GM (agent), <YYYY-MM-DD>, task GM-11. Template: business-os/head-of-ecommerce/wbr-runbook-2026-11.md
(stand-in GM-07 template pending data). Skill: aw-weekly-business-review. Week `week_start` <YYYY-MM-DD>
(Mon to Sun, owner export 2 contains it). No value below is assumed; every paid number enters only from the
owner's Monday data batch.

**One line:** <single most important fact, from the owner's export>

**Data batch status:** pending / incomplete / complete (owner: fill the six items in step 2 of the runbook before 09:00 Monday)

## Scorecard
| KPI | This wk | Last wk | 4-wk avg | Flag | Basis |
|---|---|---|---|---|---|
| Net revenue ex VAT (EUR) | TODO: Squarespace + Etsy export | (prior week) | (once 4 weeks) | | Owner export. Not assumed |
| Orders (site / Etsy) | TODO / TODO | | | any order change at < 10/wk | Orders/revenue come from Squarespace and Etsy only. Test #00003/#00004 excluded |
| Sessions | TODO: GA4 | | | | Context: GA4 has no purchase events. If the count is new, state it as such |
| Conversion rate | derive (orders_site / sessions) | | | | blank if sessions are 0 |
| AOV (EUR) | derive (net revenue / all orders) | | | | blank if orders are 0 |
| CAC new customers (EUR) | n/a if spend is 0 | | | | Owner confirms spend this week; assumed EUR 0 only as a note, never in the row |
| Gross margin % | TODO: no costed SKU, G1 | | | | min-contribution file once costs confirmed |
| Contribution after acquisition (EUR) | TODO: G1 | | | | only when product_cost and shipping columns exist |
| On-time dispatch % | n/a (no order shipped) / TODO: Ops log | | | | First filled in OPS-15 |
| Sell-through | TODO (decision 4, physical count) | | | | Do not paste Production register counts as if measured |

## Variances (only flagged lines; rule: > 20% and > EUR 50, or any order change at < 10/week)
- (one line per flagged variance: what, evidence, likely cause, action, owner, due)

## Inputs we control (status <YYYY-MM-DD>; GM updates each Monday)
- Sessions by channel: GA4 screenshot TODO owner. Only UTM-tagged (A-GM-12) sensitivity.
- Merchant Center: approved / pending / disapproved TODO owner (gate G6).
- PDP fixes shipped: product data frozen; CRO has 5 priority PDP packs ready (A-GM-19 applies unless the owner unfreezes).
- SKUs safe to promote (GREEN list): none yet (G1/G2 OPEN); AMBER at best until costs confirmed.
- Campaigns live: none (paid EUR 0 unless the 20 Nov go/no-go flips, GRO-18; A-GM-08).
- Creator gifts shipped: TODO (G4 gates this; A-GM-17).

## Gates (changes since last week, G0-G9; full definitions in gate-tracker.md)
| Gate | Real status | Change since last week | Evidence |
|---|---|---|---|
| G0 production inputs | OPEN / PARTIAL / CLEARED | | |
| G1 SKU costs confirmed | OPEN / PARTIAL / CLEARED | | |
| G2 safe-to-promote GREEN list | OPEN / PARTIAL / CLEARED | | |
| G3 cash | OPEN / PARTIAL / CLEARED | | |
| G4 buyable store | OPEN / PARTIAL / CLEARED | | |
| G5 carrier-backed cutoffs | OPEN / PARTIAL / CLEARED | | |
| G6 Merchant Center approved | OPEN / PARTIAL / CLEARED | | |
| G7 measurement | OPEN / PARTIAL / CLEARED | | |
| G8 claims evidence | OPEN / PARTIAL / CLEARED | | |
| G9 legal | OPEN / PARTIAL / CLEARED | | |

## Decisions for owner (max 3)
| # | Decision | Evidence | Owner | By | Reversible / approval |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

## Owner Monday batch (max 15 minutes, by gate)
| # | Action | Due | Time | Unblocks |
|---|---|---|---|---|
| 1 | Data batch of step 2: Orders export (excl. #00003/#00004), Etsy count, GA4 sessions, spend confirm, MC screenshot | Mon 09:00 | 20 min | GM-07 / this WBR, GRO-06 |
| 2 | Week's past-due action from owner-unblock-pack.md rows | this week | __ min | __ |
| 3 | Week's past-due action from owner-unblock-pack.md rows | this week | __ min | __ |
(Fill from owner-unblock-pack.md "Full checklist, by due date"; cap 15 mins.)

## Missing data / TODO
- sessions, orders_site, orders_etsy, new_customers, repeat_customers, gross_sales, returns, units_sold:
  owner export (step 2).
- ad_spend_eur, creator_cost_eur: owner confirmation per account (assumed EUR 0, never pasted).
- units_available, sell-through: physical count (decision 4).
- gross_margin_pct, contribution_eur: unit_economics.py after G1 (nothing costed as of 21 Oct).

## Proposed kpi-weekly.csv row (owner pastes only after approval; blank = unknown; ASSUMED values never pasted)
```text
week_start,sessions,orders_site,orders_etsy,new_customers,repeat_customers,gross_sales_eur,returns_eur,net_revenue_ex_vat_eur,product_cost_eur,shipping_packaging_payment_eur,ad_spend_eur,creator_cost_eur,conversion_rate,aov_eur,cac_eur,gross_margin_pct,contribution_eur,on_time_dispatch_pct,units_sold,units_available,notes
<YYYY-MM-DD>,,,,,,,,,,,,,,,,,,,,,,"WBR week of <YYYY-MM-DD>. TODO owner: Squarespace orders (excl. #00003/#00004), Etsy count, GA4 sessions, spend confirm. product_cost and shipping TODO until SKU costs (G1). units_available TODO until stock count (decision 4). No assumed values pasted (HARD RULE 6)"
```

Derivations once filled: net revenue = (gross - returns) / 1.21 (accountant confirms per-country VAT);
conversion = orders_site / sessions; AOV = net revenue / all orders; CAC = (ad + creator) / new customers;
contribution only when product_cost and shipping columns exist; contribution columns stay blank until G1.

**DRAFT for owner. Not posted or sent. No spend, no store change, no publish.**
```

## 4. Monday calendar 2026-11-02 to 2026-12-28
| Monday | Week (Mon-Sun) | Notes | Looks at |
|---|---|---|---|
| Mon 2 Nov | 26 Oct - 1 Nov | First run of this loop; also content-measurement-prep re-baseline watch, SEO weekly Monday starts (SEO-11/18), Growth weekly readouts start (GRO-17) | Week 1 baseline row |
| Mon 9 Nov | 2 - 8 Nov | MTO PDP copy-by date (W3-11, Ops: order-by 19 Nov EU) | PDP line live |
| Mon 16 Nov | 9 - 15 Nov | Black Friday week: no promotions without G1 cleared; Finance November pack preparation; GM-14 done already | Volume watch |
| Mon 23 Nov | 16 - 22 Nov | GM-17 4-week target re-baseline (C9) and CRE-24 content KPI re-baseline | 4-week averages start being usable |
| Mon 30 Nov | 23 - 29 Nov | Payday / post-peak check-in; gift shipping last push | Orders by DCs per cut-off table |
| Mon 7 Dec | 30 Nov - 6 Dec | Freeze period starting 1 Dec; no new site changes after 10 Dec; CX freeze check checklist (CX-28) prepared | Readiness |
| Mon 14 Dec | 7 - 13 Dec | Gift-peak wrap; freeze 12 Dec (CRO-28); carrier lock dates | No new SKUs, no new macros |
| Mon 21 Dec | 14 - 20 Dec | Last WBR before peak; posting stops 19-20 Dec for balance flow changes | Read-only review |
| Mon 28 Dec | 21 - 27 Dec | Year-close review, feeds Dec review; POST-PEAK review (OPS-18, CX-29, CRE-25) start | Output feeds FIN-24 and GM-19 |

## 5. Assumed-mode to data-mode transition
GM-07 (week of 2026-10-19) is the only blocked item and stays on its assumption-based draft
(`wbr-2026-10-26-prefill.md`). From 2 Nov onward this runbook is the sole weekly artefact. The transition happens
as follows and is one-way; once a number is filled from an owner export it never goes back to assumption mode.

- Week of 26 Oct: `wbr-2026-10-26-prefill.md` runs (one last time) with assumption cells.
- Week of 2 Nov: this runbook begins. Assumed values from the assumption registers may be cited in notes (labelled
  `ASSUMED`) until owner input clears the gate, but never in the CSV row.
- Once G1 (SKU costs) clears and the account owner pastes the first confirmed KPI row, `business-os/reviews/`
  becomes the source of truth for weekly numbers; the 26 Oct pre-fill is archived, not re-run.
- `GM-17` (re-baseline sessions/content targets after 4 weeks of data) cannot fire until there are 4 complete
  WBR rows in `business-os/reviews/`. Target date is 23 Nov 2026; if fewer than 4 rows arrive, the target date slips
  to the Monday after the 4th complete row, never in advance of the data.

## 6. Cross references that must exist for the loop to run
- `business-os/kpi-weekly.csv` (header + row paste target; do not modify except by owner paste).
- `business-os/head-of-ecommerce/gate-tracker.md` (rule for CLEARED stays evidence-only).
- `business-os/head-of-ecommerce/owner-unblock-pack.md` (weekly source for the Monday batch items).
- `business-os/head-of-ecommerce/assumptions-wave3.md` (A-IDs for any `ASSUMED` cell).
- `business-os/knitwear-making/assumptions-wave3.md` and `operations/assumptions-wave3.md` (numbered assumptions for
  production, carrier and cutoff rows).
- `business-os/head-of-ecommerce/min-contribution-assumed-2026-10-21.md` (GM-12) and
  `business-os/head-of-ecommerce/plan-upgrade-memo-prep-2026-10-21.md` (GM-13) (evidence tables the GM reads;
  nothing is copy-and-pasted into the CSV).
- `business-os/reviews/` (create on first Monday run; the WBR file path above).

## 7. Do not fabricate (guardrails for this loop)
- No order count, revenue in EUR, sessions, conversion, AOV, CAC, margin or contribution lands in a WBR or CSV row
  before the owner export arrives. An empty cell is the correct state.
- No `CLEARED` gate without an export, screenshot or file reference on dated evidence. The agent task ends at
  `PARTIAL` until the evidence does.
- No new owner action in the Monday batch that is not already in `owner-unblock-pack.md`. Re-order only.
- No plans to spend (ads, gifts, yarn, hires, stalls, plan upgrades) or to publish (store, posts, emails, DMs)
  appear in a draft WBR. Those stay in the decision pack and require an owner yes.
- No "re-baseline", "scale" or "stop" call before 4 complete WBR rows plus an owner yes.
- No change to `PROJECT-HANDBOOK.md`, `business-os/README.md`, `business-os/brand.md` or any `assets/` file. Hard
  rule 1 applies even when the WBR template only complains about their absence.

**DRAFT. Reusable runbook + empty skeleton. Nothing posted or sent.**
