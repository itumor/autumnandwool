DRAFT — for owner approval

# Christmas 2026 order-by dates — PROVISIONAL [VERIFY], not for publication

OPS-08, agent `aw-operations`, 2026-10-21. Governs per master plan ruling C3. Worst-case arithmetic from the
public promises only; **no carrier data yet**. Carrier-backed version due 14 Nov (OPS-09); publication only after
owner approval (decision 33, 20 Nov).

Sources: Merchant Center shipping policy (handling 2-5 + transit by region, `implementation-report.md`);
`plans/2026-2027/operations.md` s2; master plan C3; Latvijas Pasts Christmas 2025 reminder (lvportals.lv,
8 Dec 2025) as a reference point only.

## Method

- Order day D (before the daily cut-off) -> handling working days start D+1 -> transit working days -> delivered.
- Working days = Mon-Fri, excluding Latvian public holidays Wed 18 Nov and Thu 24 Dec 2026 [VERIFY official
  2026 calendar and transferred days]. Destination holidays (e.g. US Thanksgiving Thu 26 Nov) are **not** modelled
  [VERIFY per carrier].
- Two delivery targets: Thu 24 Dec (ops plan baseline; 24 Dec counted as the delivery day itself) and Wed 23 Dec
  (conservative: 24 Dec is a Latvian public holiday and many carriers run reduced service on Christmas Eve).
- Made-to-order (MTO) = full handling (5 working days). In-stock = 1 working day handling, **only for units the
  owner has physically confirmed** (placeholder stock 360/220 does not count).

## Table

| Region | Worst-case working days (handling + transit) | MTO order by (deliver 24 Dec) | MTO order by (deliver 23 Dec) | In-stock order by (24 Dec / 23 Dec) | Status |
|---|---|---|---|---|---|
| Latvia | 5 + 5 = 10 | Thu 10 Dec | Wed 9 Dec | Wed 16 Dec / Tue 15 Dec | [VERIFY] carrier dates. Reference: Latvijas Pasts 2025 domestic last posting was 19 Dec |
| EU-18 | 5 + 10 = 15 | Thu 3 Dec | Wed 2 Dec | Wed 9 Dec / Tue 8 Dec | [VERIFY]. Reference: Latvijas Pasts 2025 said EU "early December" |
| Estonia, Lithuania | No Merchant Center promise; Squarespace "Rest of World" | Use EU-18 row until carrier data | — | — | [VERIFY] likely faster than EU-18; do not publish faster dates without carrier data |
| US / Canada / Australia | 5 + 20 = 25 | Thu 19 Nov | Tue 17 Nov | Wed 25 Nov / Tue 24 Nov | [VERIFY]. **19 Nov is before the planned publish date (20 Nov)**: per ruling C3 the message is "Christmas delivery not guaranteed" unless paid express exists (decision 21) |
| Other countries | No promise | — | — | — | Not offered for Christmas |

Check (arithmetic, EU MTO 24 Dec): D = Thu 3 Dec; handling Fri 4, Mon 7, Tue 8, Wed 9, Thu 10 Dec; transit
Fri 11 Dec ... Thu 24 Dec = 10 working days. Owner can recount from this pattern.

## What each team may use now (internal only)

| Team | Use |
|---|---|
| Production | MTO stop date for Christmas = earliest regional cutoff, about 2-3 Dec for EU (ruling C3); replaces PRD's 11 Dec |
| Partnerships | Gifts shipped by 30 Nov (master plan) fits the EU window |
| CRO / CX / Creative / Growth | Plan copy slots with placeholders; **no dates published** until carrier-backed version + owner approval |

After each cutoff, the fallback message is the digital gift card (no shipping risk; growth idea #85).

## Rules for the carrier-backed version (OPS-09)

1. Published date = min(this worst-case date, carrier last-posting date minus our handling days).
2. Each region row has a carrier source URL and date.
3. Never publish a date later than the carrier supports. In-stock dates only with owner-confirmed units.

## TODO / missing data

- Carrier choice (decision 8) and each carrier's 2026 Christmas last-posting dates. Risk: Latvijas Pasts published
  its 2025 dates on 8 Dec, after our 14 Nov target. If dates are not out by 14 Nov, keep worst-case dates.
- 2026 Latvian holiday calendar incl. transferred working days.
- Dispatch promise (decision 3): if the owner shortens handling, every date moves later.
- Owner-confirmed shelf stock per SKU for the in-stock column.
- Paid express for US/CA/AU: yes/no and rates.
