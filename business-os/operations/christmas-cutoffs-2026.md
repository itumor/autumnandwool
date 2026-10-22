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

## Wave 3 assumed version (OPS-09 on ASSUMPTIONS, 2026-10-21)

**ASSUMPTION, internal planning only, not for publication.** Register: `assumptions-wave3.md` (A-OPS-12..20).
GM rulings W3-6, W3-10, W3-11, W3-13 applied 2026-10-21 (`business-os/head-of-ecommerce/assumptions-wave3.md`).
Carrier last hand-over dates are 2026 estimates from 2025 carrier notices; no carrier has published 2026 dates.
Inputs: handling in-stock 2 wd (A-OPS-12); **made-to-order per GM ruling W3-1 = Production A-PRD-14: garments 10 wd,
beanie / hat set 5 wd**; order before 12:00 Riga (A-OPS-13), handling starts the next working day; transit A-OPS-14;
holidays Wed 18 Nov, Thu 24 Dec, Fri 25 Dec (A-OPS-15); delivery target Wed 23 Dec.
Rule: order-by = carrier last hand-over minus handling days, never later than the transit upper bound allows; where
Production has its own date for the same zone, **the earlier date wins** (W3-1) until the owner times units.
(The provisional table above used 5 wd for all MTO; it is superseded for MTO garments.)

| Region | Assumed carrier + last hand-over | Transit upper (wd) | MTO garments order-by (10 wd) | MTO beanie / hat set order-by (5 wd) | In-stock order-by (2 wd) | Guaranteed? | Conf. |
|---|---|---|---|---|---|---|---|
| Latvia | Parcel locker, Fri 18 Dec | 3 | **Fri 4 Dec** | **Fri 11 Dec** | **Wed 16 Dec** | Yes, if carrier confirms | M (carrier), L (lead time) |
| Estonia / Lithuania | Parcel locker, Thu 17 Dec | 4 | **Thu 3 Dec** | **Thu 10 Dec** | **Tue 15 Dec** | Yes, if carrier confirms | M / L |
| EU (other, main zones) | Locker/pickup road service, Wed 9 Dec | 8 (lands Mon 21 Dec) | **Thu 19 Nov** (Production A-PRD-22; Ops calc Wed 25 Nov) | **Thu 26 Nov** (Production A-PRD-22; Ops calc Wed 2 Dec) | **Mon 7 Dec** | Yes, if carrier confirms | L |
| US / Canada / Australia | Postal tracked, Mon 30 Nov | 20 (lands after 24 Dec) | Fri 13 Nov | Mon 23 Nov | Thu 26 Nov | **No: "Christmas delivery not guaranteed"** (C3) | L |
| Rest of World + EU remote zones | — | — | none | none | none | No Christmas date | — |

### MTO stops: main stop and Baltic second stop (GM ruling W3-11, ASSUMED yes to both; owner confirms by 4 Nov)

| Stop | Garments MTO order-by (10 wd) | Beanie / hat set MTO order-by (5 wd) | Valid for delivery addresses in | Christmas promise |
|---|---|---|---|---|
| **Main stop** | **Thu 19 Nov** | **Thu 26 Nov** | All EU zones incl. LV / EE / LT (EU-other main zones end here) | Yes, if carrier confirms |
| **Baltic second stop** | **LV Fri 4 Dec / EE-LT Thu 3 Dec** | **LV Fri 11 Dec / EE-LT Thu 10 Dec** | Latvia, Estonia, Lithuania **only** | Yes, if carrier confirms |
| US / CA / AU | Fri 13 Nov | Mon 23 Nov | US, Canada, Australia | **No: "Christmas delivery not guaranteed"** |
| Rest of World | — | — | — | No Christmas date |

- Copy rule: an MTO order placed after the main stop with a non-Baltic EU address gets the after-cutoff message
  below; with a Baltic address it is still inside the second stop until the LV / EE-LT date.
- Publication timing (W3-11a): the MTO order-by line goes on the cardigan, beanie and hat set PDPs + FAQ by **Mon
  9 Nov** (CRO A-CRO-07 drafts; owner applies), because the 19 Nov main stop falls before the 20 Nov table
  publication. Ops supplies the dates only; it changes no page.
- Capacity: the second stop adds MTO load 20 Nov - 18 Dec for Baltic orders; Production confirms in its capacity
  file. Shipping charge per zone (W3-13) does not move any date.

### Cardigan colours (GM ruling W3-10, ASSUMED; owner physical count due 24 Oct)

| Cardigan colour | Customer promise | Column to use |
|---|---|---|
| Brown, Blue | **Made to order, 10 wd** (as live PDP; A-CRO-01). Production's 2 units per colour on the shelf are upside only, not promised | MTO garments |
| Black | In stock | In-stock (only owner-confirmed units) |

If the 24 Oct count confirms Brown/Blue units, the promise still stays MTO until the owner changes the PDP; a shelf
unit simply ships early.

Reconciliation with Production (A-PRD-22): Production counted 10 / 5 wd back from a last EU dispatch of **Thu 3 Dec**
(ruling C3's conservative date) -> 19 Nov / 26 Nov. Ops counts from an assumed EU carrier hand-over of **Wed 9 Dec**
(A-OPS-18, L) -> 25 Nov / 2 Dec. Same lead times; the only difference is the last EU dispatch day. Per W3-1 the
earlier dates (19 Nov / 26 Nov) apply. If a carrier publishes an EU date of 9 Dec or later, the owner may move EU to
25 Nov / 2 Dec.

Arithmetic (owner can recount):
- LV garments: order Fri 4 Dec; handling Mon 7-Fri 11, Mon 14-Fri 18 Dec (10 wd); hand-over Fri 18 Dec; transit
  Mon 21-Wed 23 Dec.
- EE/LT garments: order Thu 3 Dec; handling Fri 4 - Thu 17 Dec (10 wd).
- EU garments (Ops calc): order Wed 25 Nov; handling Thu 26 Nov - Wed 9 Dec (10 wd). Production: order Thu 19 Nov;
  handling Fri 20 Nov - Thu 3 Dec (10 wd).
- US garments: order Fri 13 Nov; handling Mon 16, Tue 17, Thu 19 (Wed 18 Nov holiday), Fri 20, Mon 23 - Fri 27,
  Mon 30 Nov (10 wd). This is before the 20 Nov publish date: US garments are effectively closed for Christmas when
  the table goes public.
- Accessories rows = 5 wd back from the same hand-over dates.

Derived planning dates (ASSUMPTION):
- **Main MTO stop for Production: garments Thu 19 Nov, beanie / hat set Thu 26 Nov** (EU, earliest guaranteed zone;
  rulings C3, W3-1). **Baltic second stop (W3-11b, assumed yes):** garments LV Fri 4 Dec / EE-LT Thu 3 Dec,
  accessories LV Fri 11 Dec / EE-LT Thu 10 Dec, Baltic delivery addresses only; Production confirms capacity.
- After-cutoff message (W3-6 = CX A-CX-03; **no gift card exists**, A-GM-22): "may arrive after Christmas" + offer
  of a handwritten gift note with the expected delivery date. Starts the day after the applicable order-by date
  (MTO date for MTO items, in-stock date for owner-confirmed units) in each zone.
- Publication: only after owner approval (decision 33, 20 Nov) and, if out by then, the carriers' own 2026 dates
  (rule 1 below: take the earlier date).

## What each team may use now (internal only)

| Team | Use |
|---|---|
| Production | Main MTO stop garments Thu 19 Nov / accessories Thu 26 Nov; Baltic second stop LV 4 / EE-LT 3 Dec garments, LV 11 / EE-LT 10 Dec accessories (W3-11, assumed). Cardigan Brown/Blue counted as MTO (W3-10) |
| Partnerships | Gifts shipped by 30 Nov (master plan) fits the EU window |
| CRO / CX / Creative / Growth | Per-zone dates from the stops table (A-CX-01); MTO order-by line on cardigan / beanie / hat set PDPs + FAQ by Mon 9 Nov (owner applies); full table **not published** until carrier-backed version + owner approval (20 Nov) |

After each cutoff, the message is "may arrive after Christmas" + a handwritten gift note with the expected delivery
date (W3-6, CX A-CX-03). No gift card exists (A-GM-22); if the owner creates one by 20 Nov, swap this one line.

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
- Paid express for US/CA/AU: yes/no and rates. Assumed US/CA/AU charge = flat EUR 15, not promoted (W3-13).
- Owner confirms by 4 Nov: PDP/FAQ order-by line by 9 Nov and the Baltic second stop (W3-11); Production capacity
  for second-stop orders.
- Owner physical count of cardigan Brown/Blue (24 Oct, decision 4); promise stays MTO either way (W3-10).
