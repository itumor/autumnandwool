# Partnerships folder: index, weekly cycle, owner decisions (DRAFT)

Owner of folder: `aw-partnerships`. Everything here is a DRAFT. Nothing is sent, shipped, created or spent by the
agent. Plan: `plans/2026-2027/partnerships.md`. GM rulings in `plans/2026-2027/master-plan.md` override it.

## 1. Files

| File | Task | What |
|---|---|---|
| `creator-tracker.csv` | PAR-01 | One row per creator from `shortlisted` on. Header only today |
| `vetting-scorecard.md` | PAR-02 | 0-14 score, red flags, data rules |
| `leads-2026-W43.md` | PAR-03 | Search log and 9 unscored leads [VERIFY] |
| `outreach-dm-drafts.md` | PAR-05 | EN/LV first message, follow-up, replies, pre-send checklist |
| `creator-brief-gifting.md` | PAR-07, PAR-10 | Brief for the parcel + gift spec sheet + candidate gift SKUs |
| `disclosure-rules.md` | PAR-08 | EU/PTAC rules, weekly check, fix messages |
| `attribution-scheme.md` | PAR-09 | Codes (if plan allows), UTM pattern, rows for Growth, weekly readout |
| `usage-rights-template.md` | PAR-12 | Written usage-rights request and terms table |
| `creator-report-template.md` | PAR-16 | Monthly report, Q4 readout, day-90 verdict |
| `owner-inputs-wave2.md` | all BLOCKED | **One form for every owner answer Partnerships needs** (O1-O15) + lead check sheet |
| `gift-budget-worksheet.md` | PAR-11, PAR-15 | Gift cost, BE_CAC, max CAC, programme cap (all TODO until costs) |
| `per-creator-launch-pack.md` | PAR-14 | Copy-per-creator block: gift spec, code, UTM, row for Growth, approvals |
| `weekly-ops-kit.md` | PAR-17 (18, 19) | Weekly file shell: follow-ups, disclosure check, readout |
| `ideas-65-71-prep.md` | PAR-20, PAR-21 | Etsy-buyer photo permission route, cafe shoot/giveaway frame |
| `close-out-and-2027-prep.md` | PAR-23 to 26 | Close/repeat rule, thank-you note, affiliate pilot and ambassador frames |

## 2. Weekly cycle (from the week the gates clear)

| Day | Agent | Owner (max 15 min batches, ruling C11) |
|---|---|---|
| Mon | Shortlist update (3-5 scored), personalised DMs, follow-up list (sent 7+ days ago, no reply, one follow-up only) | Approve or strike in the Monday WBR list |
| Tue-Thu | Tracker updates from the owner's notes | Send approved DMs and follow-ups, reply to yes/no |
| Fri | Disclosure check on new posts, attribution readout from Orders | Paste order count by code/name if the agent can't see Orders |

If the owner's list overflows, the GM drops Partnerships gifts first (ruling C11). That is expected and fine.

## 3. Owner decisions (plan D# with master-plan #)

| Plan | Master # | Decision | Proposal | Due |
|---|---|---|---|---|
| D1 | G4 | Gifts wait for a buyable store? | GM roadmap already says gifts ship **after G4** (PayPal 31 Oct; delivery/size info 14 Nov). Agree. DMs can start once G8 is clear, with gift dates set after G4 | 28 Oct |
| D2 | 12 | Q4 gifting cap: number of gifts and max EUR per gift | Up to 5-8 gifts. Max per gift <= that SKU's break-even CAC (`unit_economics.py`). Cap EUR = gifts x gift cost: **TODO** until costs are filled (G1, 22 SKUs by 11 Nov) | 28 Oct (number), 15 Nov (EUR) |
| D3 | 4, 12 | Which SKUs to gift; confirm beanie/turtleneck physical stock | Beanie first, then hat & scarf set, only if GREEN/AMBER in the capacity file | 28 Oct |
| D4 | 12 | Approve shortlist, each DM and every gift; which account sends | Send from `@autumnandwool` [VERIFY account ownership, master #18] | Weekly |
| D5 | 11, 23 | Code yes/no and %, commission, usage-rights terms and length | Check discounts on the plan first (#11). % only after min contribution (#23). No commission in Q4. Usage rights: 3 months organic by default, ads only on a separate yes | 28 Oct / 4 Nov |
| D6 | 16 | Claims: "finished by hand", "Riga", fibre lines | Until cleared, DMs and briefs say "knitted on manual machines and finished by hand" with `[VERIFY G8]` | 31 Oct |
| D7 | 24 | Squarespace upgrade (Code Injection, maybe discounts) | Weigh together with codes (ruling C6) | 4 Nov |
| D8 | 36 | 2027 budget, Partnerships hire after the verdict | After day-90 verdict | 31 Jan 2027 |

Also needed (not the owner's decision, but blocking): costed SKUs and the capacity file (Production/Finance), carrier
rates and packaging (Operations), discount-feature screenshot (owner, #11), native LV check of drafts.

## 4. Gift budget formula (fill when costs exist)
```
gift_cost      = materials_labour_eur + packaging_eur + shipping_eur(creator country)
programme_cap  = approved_gifts x gift_cost                      (owner sets approved_gifts, D2)
stop rule      = total creator cost / attributed orders > BE_CAC  (60 days after shipping) -> stop or change deal
```
