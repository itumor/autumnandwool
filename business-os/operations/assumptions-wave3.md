DRAFT — for owner approval

# Operations assumptions register, wave 3 (shared baseline)

Agent `aw-operations`, 2026-10-21. ASSUMPTION MODE (owner-approved 2026-10-21). **Every value below is an
ASSUMPTION, not a fact.** It lets work go ahead while the owner answers `owner-inputs-wave2.md`. Any file that uses a
value must cite its A-ID and the word "ASSUMPTION". When the owner answers, the answer replaces the assumption and every
file that used the A-ID gets re-checked (list in "Used by").

Rules: prices are taken from carriers' public pages where one was readable (URL + date below). Where no public price
could be read, the value is an agent estimate and its confidence is L. Nothing here is a carrier choice, contract,
purchase or published promise. Free-shipping regions, carrier choice and all wording stay owner decisions.

Confidence: H = public carrier source read today and it fits our case; M = public source, but carrier or parcel size is
assumed; L = estimate from indirect sources (older year, other country, aggregator) or no source.

## 1. Carriers and shipping cost per parcel

Parcel assumed = one folded knit garment in a mailer, packed weight 0.5-1.0 kg, fits a parcel-locker size "S"
(Smartposti S = max 12 x 34 x 42 cm) or a long cardigan in "M" (20 x 34 x 42 cm). Prices incl. 21% VAT where stated.

| A-ID | Assumed value | Basis (source, date read 2026-10-21) | Low-high range | Conf. | Used by | Owner confirms by |
|---|---|---|---|---|---|---|
| A-OPS-01 | Carrier, **Latvia**: parcel-locker network, locker-to-locker (Omniva, Smartposti or Latvijas Pasts locker; price modelled on Smartposti) | Owner has not named a carrier (form item 4). Smartposti public LV list valid from 15.07.2026; Omniva LV only shows a calculator, no readable static list | — | L (carrier) | OPS-06, OPS-09, OPS-11, FIN-18 | 28 Oct (MP 8) |
| A-OPS-02 | Shipping cost, **Latvia**: **EUR 5.00 per parcel** planning value (incl. VAT) | Smartposti LV locker S EUR 2.90, M EUR 3.90, courier S EUR 5.19 (https://www.smartposti.lv/paku-nosutisana/sutijumu-cenas, valid 15.07.2026); Latvijas Pasts registered domestic parcel up to 1 kg EUR 7.01 from 1 Jan 2026 (LSM 28.11.2025); Omniva old cached private list about EUR 7.93-10.14 (outdated) | 2.90-8.14 | M | OPS-06, FIN-18 (`shipping_eur`), FIN unit economics | 28 Oct |
| A-OPS-03 | Carrier + cost, **Estonia / Lithuania**: parcel locker, **EUR 6.00 per parcel** | Smartposti locker LV->EE/LT: XS 4.79, S 5.39, M 6.69; courier S 6.99-7.90 (same URL, valid 15.07.2026; VAT not stated) | 4.79-8.90 | M | OPS-06, OPS-09, FIN-18 | 28 Oct |
| A-OPS-04 | Carrier, **EU (other)**: tracked locker/pickup-point road service (Smartposti / DPD class; postal tracked parcel as fallback) | No owner answer; Smartposti publishes per-country EU prices; DPD LV prices only via eserviss.dpd.lv (no static list) | — | L (carrier) | OPS-06, OPS-09, OPS-11 | 28 Oct |
| A-OPS-05 | Shipping cost, **EU (other)**: **EUR 22.00 per parcel** planning value | Smartposti LV->EU size S: DE 21.90, AT 20.90, NL 20.90, PL 14.99, CZ 14.99, SE 25.90, FR/IT zone 1 29.90, ES zone 1 18.99; size XS (beanie, flat sweater) 13.99-18.90 (same URL, valid 15.07.2026). Remote zones (FR/ES/PT zone 2+, CY, MT) cost EUR 40-370: **excluded**, see A-OPS-07 | 14.00-30.00 (main zones) | M | OPS-06, FIN-18, CRO-25, GRO (free-shipping margin) | 28 Oct |
| A-OPS-06 | Carrier + cost, **US / Canada / Australia**: national post tracked international parcel (Latvijas Pasts via mans.pasts.lv, or Omniva Standard), **EUR 28.00 per parcel** at 0.5-1 kg, before US duty (A-OPS-08) | No readable Latvian list. Anchor: Omniva LT private price list 2025, US 1 kg Standard about EUR 21.85 incl. VAT (search summary of https://www.omniva.lt/wp-content/uploads/sites/5/2024/07/pricelist-international-parcels-private-ltu-en-2025-2.pdf, not opened); aggregator average about USD 40 to other continents (swotzy.com). Latvijas Pasts resumed private US parcels 18.12.2025, online registration only (LSM) | 20.00-40.00 | L | OPS-06, FIN-18, CRO-25, CX-25 | 28 Oct |
| A-OPS-07 | **Rest of World** (UK, NO, CH, all others) and EU remote zones: **not costed; propose no free shipping and no Christmas promise** until the owner restricts the zone. If a cost is needed: EUR 28.00 (same as A-OPS-06) | No delivery range stated anywhere (`delivery-promise-reconciliation.md`); Smartposti remote EU zones EUR 40-370 | 20.00-45.00 (UK/NO/CH); remote EU up to 370 | L | OPS-06, OPS-09, FIN-18 (decision 21) | 31 Oct (MP 21) |
| A-OPS-08 | **US duty + clearance**: paid by us at label purchase (post collects a provisional duty + clearance fee from the sender). Planning: **15% of customs value + EUR 3.00 fee** per US parcel | US de minimis ended Aug 2025; Latvijas Pasts collects provisional customs duty + clearance fee from the sender (LSM 18.12.2025); pasts.lv business page cites a EUR 2.58 per-shipment US fee (undated); 15% = EU-US tariff ceiling agreed in 2025 (agent knowledge, not checked against the US tariff schedule for knitted wool) | 0-20% + EUR 2.58-5.00 | L | FIN-18 (US contribution), GRO/ads US targeting, CX customs macro | Accountant/adviser (FIN accountant Q3, adviser pack Q9) |
| A-OPS-09 | **Seasonal surcharge** Nov-Dec: +7% on locker/courier parcels | Omniva applied 7% seasonal index 1 Nov-31 Dec 2025 (jauns.lv; omniva.ee business notice). 2026 not announced | 0-7% | L | FIN-18 (Q4 cost), OPS-06 | Check omniva.lv 1 Nov |

Fulfilment cost per order (shipping + packaging, planning values): LV EUR 6.50; EE/LT EUR 7.50; EU EUR 23.50; US/CA/AU
EUR 29.50 + US duty (A-OPS-08). Formula: A-OPS-02/03/05/06 + A-OPS-10.
GM rulings W3-2 / W3-3 (`business-os/head-of-ecommerce/assumptions-wave3.md`): CM2 uses these Ops values by
destination (not Production's flat EUR 12 shipping placeholder) and packaging EUR 1.50 (not Production's
EUR 3.00 / 2.00).

## 2. Packaging

| A-ID | Assumed value | Basis | Low-high range | Conf. | Used by | Owner confirms by |
|---|---|---|---|---|---|---|
| A-OPS-10 | Packaging cost per order: **EUR 1.50** (plain recyclable-look kraft or poly mailer + tissue + printed care card + sticker; no branded box) | Agent estimate, **no supplier quote read**; `packaging-spec.md` lists items, quotes TODO | 0.80 (plain) - 3.00 (branded box + thank-you card) | L | FIN `packaging_eur`, OPS-04, OPS-11 | 30 Oct (MP 13, form item 12) |
| A-OPS-11 | Packed weight: beanie/hat 0.15-0.25 kg; sweater 0.5-0.8 kg; long cardigan 0.8-1.2 kg. Locker size: beanie XS, sweater S, cardigan M | Agent estimate from garment type; replaced by dry-run weights (OPS-11) | ±30% | L | OPS-06 (size band), FIN-18 | 6 Nov (dry run) |

Note: do not use the words "plastic-free", "recyclable" or "eco" on packaging copy (brand-voice claim gate) unless the
supplier proves it.

## 3. Dispatch promise and transit

| A-ID | Assumed value | Basis | Low-high range | Conf. | Used by | Owner confirms by |
|---|---|---|---|---|---|---|
| A-OPS-12 | In-stock (owner-confirmed units only): public "dispatched in 2-5 working days", internal target **2 working days**. Made-to-order: **garments 10 working days, beanie / hat set 5 working days** (= Production A-PRD-14, adopted per **GM ruling W3-1**; replaces the earlier Ops value of 5 wd for all MTO) | FAQ "up to 5 business days"; brand voice "Dispatch 2-5 working days"; Production A-PRD-14 (`business-os/knitwear-making/assumptions-wave3.md`); GM ruling W3-1 (`business-os/head-of-ecommerce/assumptions-wave3.md`) | MTO garments 7-15 wd; accessories 3-7 wd | L (MTO), M (in-stock) | OPS-09, OPS-17, PRD-04, CX LEAD_TIME macro, CRO PDP line | 24 Oct (MP 3) |
| A-OPS-13 | Daily order cut-off **12:00 Riga time**; orders after 12:00 count from the next working day. Packer = owner | Proposal in form item 3 | 10:00-15:00 | L | OPS-15, OPS-09 | 24 Oct |
| A-OPS-14 | Transit (working days after hand-over): LV 1-3; EE/LT 2-4; EU 3-8; US/CA/AU 7-20; RoW no promise | LV/EU/US upper bounds = Merchant Center ranges already submitted (C8); aggregator LV->DE 4-9 days (ecoparcel.eu); Latvijas Pasts says cross-border 4-35 days | as stated | M (LV, EU), L (US/CA/AU) | OPS-09, CX-10, CRO PDP line | 6 Nov (dry run) |
| A-OPS-15 | Working days = Mon-Fri minus LV public holidays **Wed 18 Nov, Thu 24 Dec, Fri 25 Dec, Thu 31 Dec 2026** | Latvian public holiday law (agent knowledge); transferred days for 2026 not checked | — | M | OPS-09, all Christmas copy | Agent re-checks official calendar by 1 Nov |

## 4. Christmas 2026 (assumed carrier last hand-over dates and our order-by dates)

Delivery target Wed 23 Dec (24 Dec is a Latvian holiday; carriers run reduced service). Order-by = carrier last
hand-over minus our handling days (A-OPS-12), orders before 12:00 (A-OPS-13). Full table and arithmetic:
`christmas-cutoffs-2026.md` section "Wave 3 assumed version".

Updated after GM ruling W3-1 (MTO garments 10 wd, beanie / hat set 5 wd; earlier date wins where Production has its
own date).

| A-ID | Zone | Assumed carrier last hand-over 2026 | Basis (2025 reference) | Range | Conf. | MTO garments order-by | MTO beanie / hat set order-by | In-stock order-by |
|---|---|---|---|---|---|---|---|---|
| A-OPS-16 | Latvia | Fri 18 Dec | Omniva 2025: hand over by 20 Dec (Sat) for delivery by 23 Dec (omniva.lv notice 12.12.2025); Latvijas Pasts 2025 domestic: 19 Dec (lvportals.lv 08.12.2025) | 17-19 Dec | M | **Fri 4 Dec** | **Fri 11 Dec** | **Wed 16 Dec** |
| A-OPS-17 | Estonia / Lithuania | Thu 17 Dec | Omniva 2025: EE/LT last safe date 19 Dec (same notice); one day buffer | 16-18 Dec | M | **Thu 3 Dec** | **Thu 10 Dec** | **Tue 15 Dec** |
| A-OPS-18 | EU (other) | Wed 9 Dec (Production uses Thu 3 Dec, ruling C3) | Latvijas Pasts 2025: EU "early December"; road/locker networks usually later; 8-day transit upper bound from 9 Dec lands Mon 21 Dec | 3-14 Dec | L | **Thu 19 Nov** (= A-PRD-22; Ops calc 25 Nov) | **Thu 26 Nov** (= A-PRD-22; Ops calc 2 Dec) | **Mon 7 Dec** |
| A-OPS-19 | US / Canada / Australia | Mon 30 Nov | No 2025 date found for non-EU from Latvia; US customs clearance adds days since 2025 | 20 Nov-7 Dec | L | **Fri 13 Nov** (not guaranteed; before the 20 Nov publish date) | **Mon 23 Nov** (not guaranteed) | **Thu 26 Nov** (not guaranteed) |
| A-OPS-20 | Rest of World | none | No promise (A-OPS-07) | — | — | No Christmas date | No Christmas date | No Christmas date |

Reconciliation with Production A-PRD-22: same lead times; Production counts back from a last EU dispatch of Thu 3 Dec
(C3), Ops from an assumed carrier hand-over of Wed 9 Dec. Per W3-1 the earlier dates (19 / 26 Nov) apply to the EU.
US/CA/AU: a 20-working-day transit (Merchant Center upper bound) ends after 24 Dec, so the message stays "Christmas
delivery not guaranteed" (C3). **MTO stop for Production = garments Thu 19 Nov, beanie / hat set Thu 26 Nov** (EU,
earliest guaranteed zone; C3, W3-1).

## 5. Returns

| A-ID | Assumed value | Basis | Low-high range | Conf. | Used by | Owner confirms by |
|---|---|---|---|---|---|---|
| A-OPS-21 | Return address = the owner's Riga studio address `[RETURN ADDRESS — owner fills]`. No address invented | Form item 10 open | — | L | OPS-16, CX RETURN_START macro, packing slip | 30 Oct (MP 13) |
| A-OPS-22 | Change-of-mind returns: **customer pays return postage**, stated before purchase (Shipping & Returns page + checkout link). Faulty, damaged or wrong item: **we pay** (prepaid label or refund of postage) | Merchant Center return policy already says customer pays; EU rule lets the trader charge return cost only if disclosed before purchase (aw-returns-handling, Your Europe). Adviser not consulted (C12) | Alternative: we pay all returns | M (matches MC), legal L | OPS-16, CX-19, FIN returns_allowance | 30 Oct (MP 13); adviser via 3 Nov pack |
| A-OPS-23 | Refund: within 14 days of the customer's notice, incl. standard outbound delivery actually charged (under W3-13: EUR 0 LV/EE/LT and EU >= 150; EUR 12 EU < 150; EUR 15 US/CA/AU), may wait for goods or proof of posting; same payment method. Withdrawal 14 days from delivery. No sale/MTO exclusion for standard designs; no 5-day defect window | Statutory floor summary (aw-returns-handling); live page conflicts flagged (README s11) | — | M (rules), legal L | OPS-16, CX-19, CRO policy page proposal | Adviser (decision 22) |
| A-OPS-24 | Customer's return postage cost (for FAQ wording "about EUR X"): LV about EUR 3-5; EE/LT about EUR 5-7; EU about EUR 14-30 | Smartposti public prices (A-OPS-02/03/05) | — | M | CX return macro, FIN returns_allowance | with A-OPS-22 |
| A-OPS-25 | (For CM2 use the GM value: **5% of net**, ruling W3-4 / A-GM-21. Ops' figure below is the operational return-rate view, consistent with 5% of net when the customer pays change-of-mind postage.) Returns: 8% of orders returned, our cost per return EUR 0 for change-of-mind (customer pays) + refund of item; faulty share 1% at our cost (outbound + return postage) | Agent estimate, no A&W return data (0 direct orders) | 3-15% | L | FIN returns_allowance | First 3 months of real orders |

## 6. Top 5 for other departments

1. **A-OPS-12** in-stock dispatch "2-5 working days" (internal 2); MTO garments 10 wd, beanie / hat set 5 wd (GM
   ruling W3-1 = Production A-PRD-14); cut-off 12:00 (A-OPS-13).
2. **A-OPS-02/03/05/06** shipping per parcel: LV 5.00, EE/LT 6.00, EU 22.00, US/CA/AU 28.00 + packaging 1.50 (A-OPS-10).
3. **A-OPS-16..19** Christmas MTO order-by, garments / accessories: LV 4 Dec / 11 Dec, EE/LT 3 Dec / 10 Dec,
   EU 19 Nov / 26 Nov, US/CA/AU 13 Nov / 23 Nov (not guaranteed); MTO stop for Production 19 Nov garments, 26 Nov
   accessories. Internal only until owner approves publication (decision 33).
4. **Shipping policy per GM ruling W3-13 (proposal; owner decision 21):** LV/EE/LT free; EU-other free from EUR 150
   basket, else flat EUR 12; US/CA/AU flat EUR 15, not promoted, no paid traffic; Rest of World + EU remote zones no
   promise (A-OPS-07). Zone table: `carrier-rates.md` s1. Christmas: main MTO stop 19 / 26 Nov + Baltic second stop
   (W3-11); after-cutoff line "may arrive after Christmas" + gift note, no gift card (W3-6); cardigan Brown/Blue = MTO
   (W3-10). Table: `christmas-cutoffs-2026.md`.
5. **A-OPS-22** change-of-mind return postage paid by the customer (disclosed before purchase), faulty/wrong at our
   cost; **A-OPS-08** US parcels carry duty + fee paid by us (about 15% + EUR 3) on top of the EUR 15 US charge (W3-13).

## Sources (read 2026-10-21)

- Smartposti LV price list, valid 15.07.2026: https://www.smartposti.lv/paku-nosutisana/sutijumu-cenas
- LSM, Latvijas Pasts 2026 tariffs (28.11.2025): https://eng.lsm.lv/article/economy/transport/28.11.2025-latvian-postal-services-will-be-costlier-in-2026.a624186/
- LSM, Latvijas Pasts resumes private US parcels (18.12.2025): https://eng.lsm.lv/article/economy/transport/18.12.2025-latvian-postal-service-resumes-private-shipping-to-the-usa.a626988/
- pasts.lv business US delivery page: https://pasts.lv/en/useful/business-parcel-and-small-parcel-delivery-to-us
- Omniva LV price page (calculator only): https://www.omniva.lv/en/price-lists/ ; parcel-machine sizes https://www.omniva.lv/palidziba/pakomatu-skapisu-izmeri
- Omniva LT international private price list 2025 (search summary only): https://www.omniva.lt/wp-content/uploads/sites/5/2024/07/pricelist-international-parcels-private-ltu-en-2025-2.pdf
- Omniva LV Christmas 2025 hand-over dates (12.12.2025): https://www.omniva.lv/en/news/omniva-informs-about-parcel-handover-dates-and-urges-customers-to-act-in-time/
- Latvijas Pasts Christmas 2025 reminder (08.12.2025): https://lvportals.lv/dienaskartiba/383783-latvijas-pasts-atgadina-par-sutijumu-terminiem-svetkos-2025
- Omniva seasonal surcharge 2025: https://jauns.lv/raksts/bizness/676246-dalai-klientu-omniva-uz-laiku-palielinas-cenas ; https://www.omniva.ee/en/news/important-notice-to-business-clients-about-omniva-pricing-policy/
- DPD LV sending (sizes, price only in eserviss): https://www.dpd.com/lv/en/receiving-parcels/pickup-network/parcel-sending-receiving/
- Ecoparcel LV->DE estimate (aggregator): https://www.ecoparcel.eu/en/parcel/from-latvia-to-germany/
- Swotzy Latvijas Pasts average (aggregator): https://www.swotzy.com/carriers/latvijas-pasts
- Internal: `owner-inputs-wave2.md`, `christmas-cutoffs-2026.md`, `delivery-promise-reconciliation.md`, `returns-handling.md`,
  `business-os/head-of-ecommerce/owner-unblock-pack.md`, master plan rulings C3, C8, C12.

## TODO / missing data

- Owner answers to `owner-inputs-wave2.md` items 1-4, 10-13 replace A-OPS-01..07, 10, 12, 13, 21, 22.
- Latvijas Pasts tariff book PDF (`pasts.lv/media/491/download/Tarifu_Gramata.pdf`) could not be read as text today
  (compressed PDF); international postal rates to US/CA/AU/UK still unread. Owner or agent: read the PDF or the
  mans.pasts.lv calculator for one 1 kg parcel to DE and US.
- Omniva and DPD LV prices are calculator-only; one quote each from the calculator would lift A-OPS-02/05 to H.
- Carriers' 2026 Christmas dates (usually published late Nov to mid Dec) replace A-OPS-16..19.
- US duty rate for knitted wool garments (HS 6110) from EU: accountant/adviser.
- Packaging supplier quotes (A-OPS-10) and dry-run weights (A-OPS-11).
