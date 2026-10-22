DRAFT — for owner approval

# Carrier comparison (template + research notes)

OPS-05, agent `aw-operations`, 2026-10-21. Section 2 is the template (no rate filled from the owner's own carrier).
Section 2a (wave 3) = OPS-06 filled on **ASSUMPTIONS** from public candidate-carrier prices; register
`assumptions-wave3.md`. Every price must come from the
carrier's own public price list or the owner's account quote, with URL and date. Carrier choice and any contract =
owner decision 8 (due 28 Oct). Filling the table = OPS-06 (blocked, see status file).

Sources: `.claude/skills/aw-fulfilment-sop` (rate-table format); Merchant Center shipping policy as recorded in
`implementation-report.md`; web checks 2026-10-21 listed in section 4.

## 1. Regions to price (from current promises)

| Region code | Countries | Current promise (Merchant Center, not carrier-backed) | Squarespace zone (live today) | Checkout tested? | **Proposed policy (GM ruling W3-13, ASSUMPTION; owner changes store settings)** | Planning cost / parcel incl. packaging (A-OPS) | Gap per order after charge (gross) |
|---|---|---|---|---|---|---|---|
| LV | Latvia | Free; 2-5 handling + 2-5 transit | Latvia (EUR 0) | Yes (to payment step only) | **Free** | 6.50 | 6.50 |
| BALT | Estonia, Lithuania | **Not in the Merchant Center list** (see `delivery-promise-reconciliation.md`) | Rest of World (EUR 0) | No | **Free** | 7.50 | 7.50 |
| EU-18 | Austria, Belgium, Finland, France, Germany, Greece, Ireland, Italy, Netherlands, Portugal, Slovakia, Spain, Czechia, Denmark, Hungary, Poland, Romania, Sweden | Free; 2-5 + 5-10 | Rest of World (EUR 0) | No | **Free from EUR 150 basket; below EUR 150 flat EUR 12.** Remote zones (FR/ES/PT zone 2+, CY, MT, GR zone 2): no promise (A-OPS-07) | 23.50 (FR/IT up to 31.40) | >= 150: 23.50; < 150: 11.50 |
| US-CA-AU | United States, Canada, Australia | Free; 2-5 + 7-20 | United States / Rest of World (EUR 0) | No | **Flat EUR 15** (about EUR 12.40 net), **not promoted, no paid traffic**; Christmas "not guaranteed" | 29.50 + US duty (A-OPS-08) | 14.50 + US duty |
| OTHER | UK, NO, CH and all other countries | No Merchant Center promise | Rest of World (EUR 0) | No | **No promise** (no free shipping, no delivery range, no Christmas date; restrict or remove the zone, A-OPS-07) | not costed | — |

Policy column = proposal only (W3-13, `business-os/head-of-ecommerce/assumptions-wave3.md`; GM A-GM-18 amended);
owner confirms 31 Oct, final 11 Nov (decision 21). Ops changes no store setting. Gap = planning cost minus the
shipping charge, both gross; Finance computes CM2 by zone net of VAT (FIN-18). Merchant Center and Squarespace
zones must be changed together by the owner so Google and checkout show the same charge.

## 2. Comparison table (fill per carrier x service x region)

Weight bands follow the packed weights from the dry run (`packaging-spec.md` s5); until then use 0.5 / 1 / 2 kg.

| Region | Carrier | Service | Tracked? | Door / locker / post office | Price 0.5 kg | Price 1 kg | Price 2 kg | Size class limits | VAT incl.? | Fuel / seasonal surcharge | Transit (carrier-stated) | Claim deadline + liability cap | Christmas 2026 last posting date | Source URL + date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LV | TODO | TODO | | | | | | | | | | | | |
| BALT | TODO | | | | | | | | | | | | | |
| EU-18 | TODO | | | | | | | | | | | | | |
| US-CA-AU | TODO | | | | | | | | | | | | | |
| OTHER | TODO | | | | | | | | | | | | | |

Then per region: cheapest tracked option, fastest option, and the gap vs the free-shipping promise:
`cost per order at expected weight` vs `shipping_eur` in `sku-economics.csv` (blank today; README s9 illustration
EUR 12). Free-shipping keep/drop per region = owner decision 21.

## 2a. Wave 3 rate table on ASSUMPTIONS (OPS-06, 2026-10-21)

**ASSUMPTION, not a carrier choice.** Owner has not named a carrier (decision 8). Prices below are public list prices
read 2026-10-21 for a candidate carrier, used as planning values. Register: `assumptions-wave3.md` (A-IDs). Prices
incl. 21% VAT for LV; VAT not stated on the page for EE/LT/EU rows. Sizes = locker compartments, not weight bands
(Smartposti XS up to 5 kg, S-XL up to 35 kg; sizes XS 5x34x42, S 12x34x42, M 20x34x42, L 34x36x42 cm).

| Region | Carrier (candidate) | Service | Tracked? | Door / locker | XS (beanie) | S (sweater) | M (cardigan) | Courier S | Transit (assumed, A-OPS-14) | Christmas 2026 last hand-over (assumed) | Planning value / parcel | Source URL + date | Conf. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| LV | Smartposti (Omniva / Latvijas Pasts lockers equivalent class) | Locker-to-locker | Yes | Locker | 2.50 | 2.90 | 3.90 | 5.19 | 1-3 wd | Fri 18 Dec (A-OPS-16) | **5.00** (A-OPS-02, conservative vs Omniva/LP) | smartposti.lv sūtījumu cenas, valid 15.07.2026, read 21.10.2026 | M |
| LV (alt.) | Latvijas Pasts | Registered domestic parcel up to 1 kg | Yes | Post office / locker | — | 7.01 (1 kg) | +1.25 per extra kg | — | 1-3 wd | 19 Dec in 2025 | — | LSM 28.11.2025 (SPRK decision 27.11.2025) | H (price), owner use unknown |
| EE / LT | Smartposti | Locker-to-locker | Yes | Locker | 4.79 | 5.39 | 6.69 | 6.99 (LT) / 7.90 (EE) | 2-4 wd | Thu 17 Dec (A-OPS-17) | **6.00** (A-OPS-03) | smartposti.lv, valid 15.07.2026 | M |
| EU (DE) | Smartposti | International locker/pickup | Yes | Pickup point / locker | 13.99 | 21.90 | 25.99 | — | 3-8 wd | Wed 9 Dec (A-OPS-18) | **22.00** (A-OPS-05) | same | M |
| EU (AT / NL / SE / PL / CZ) | Smartposti | same | Yes | same | 13.99-15.99 | 14.99-25.90 | 25.99-27.90 | — | 3-8 wd | Wed 9 Dec | 22.00 | same | M |
| EU (FR / IT / ES zone 1) | Smartposti | same | Yes | same | 15.99-18.90 | 18.99-29.90 | 28.98-33.90 | — | 3-8 wd | Wed 9 Dec | 22.00 (FR/IT run over: 29.90) | same | M |
| EU remote (FR/PT/ES zone 2+, CY, MT, GR zone 2) | Smartposti | same | Yes | same | 32.99-255.90 | 45.98-282.90 | up to 317.90 | — | — | — | **not costed; propose exclude from free shipping** (A-OPS-07) | same | M |
| US / CA / AU | Latvijas Pasts (mans.pasts.lv) or Omniva Standard | Tracked international parcel | Yes | Door / post | — | ~21.85 (Omniva LT 2025, US 1 kg) | — | — | 7-20 wd | Mon 30 Nov (A-OPS-19) | **28.00 + US duty ~15% + fee ~3.00** (A-OPS-06, A-OPS-08) | Omniva LT 2025 PDF (search summary only); LSM 18.12.2025 (US resumed, sender pays provisional duty + fee) | L |
| UK / NO / CH / rest | Postal tracked parcel | — | Yes | Door / post | — | — | — | — | no promise | none | 28.00 if forced; **propose no free shipping** (A-OPS-07) | none read | L |

Gap vs free shipping (planning, shipping + packaging A-OPS-10 EUR 1.50): LV 6.50; EE/LT 7.50; EU 23.50 (FR/IT up to
31.40); US/CA/AU 29.50 + duty (on a EUR 155 sweater about EUR 19 more at the assumed 15% of the net customs value; L).
`shipping_eur` in `sku-economics.csv` is blank; README s9 illustration EUR 12 is **below** the EU and US planning
values. Finance decides how to use this; this file does not edit the CSV. Free shipping per region = owner decision 21;
proposed charges per zone (W3-13) and the remaining gap: section 1.

Nov-Dec: add up to +7% seasonal surcharge if the carrier repeats 2025 practice (A-OPS-09).

## 3. Candidates to research (not recommendations)

Carriers known to operate parcel services from Latvia. Inclusion is not a choice; the owner may already use one
(question 1 in `owner-questions-2026-10-21.md`).

| Candidate | Why look | Notes / what to check |
|---|---|---|
| Latvijas Pasts (national post) | Domestic + international, parcel lockers, universal postal network for US/CA/AU | Tariffs changed from 1 Jan 2026 (LSM). Check tracked international parcel product, US acceptance rules |
| Omniva | Baltic parcel-locker network | Business price list for LT/LV/EE valid from 1 Nov 2025, excl. VAT, S/M/L classes, volume discounts from 41 parcels/month; seasonal Nov-Dec surcharge reported as +5% (PDF) or 7% (EE notice, 2025). Private-customer terms with dynamic pricing from 22 July 2026 [VERIFY on omniva.lv] |
| DPD Latvia | Courier + Pickup points, EU road network | TODO price list |
| An express integrator (e.g. DHL Express) | Only if the owner wants paid express for late Christmas orders (decision 21) | TODO account-based quote |

## 4. Research log

| Date | Check | Result |
|---|---|---|
| 2026-10-21 | Latvijas Pasts 2026 parcel price list | Not found via search; go to pasts.lv tariff page directly (TODO) |
| 2026-10-21 | Omniva Latvia 2026 locker prices | No official 2026 LV list found; only 2025 business list (LT site) and secondary resellers. Reseller prices not used |
| 2026-10-21 | Latvijas Pasts Christmas 2026 dates | Not published yet. Reference only: 2025 domestic last posting 19 Dec; EU "early December"; non-EU "now is the last moment" in an article dated 8 Dec 2025 (no exact date given) |
| 2026-10-21 (wave 3) | Smartposti LV public list | Read: LV, EE/LT/FI and every EU country by locker size, valid 15.07.2026. No non-EU prices |
| 2026-10-21 (wave 3) | Latvijas Pasts tariff book PDF / postal-service-rates PDF | Downloaded, text not readable with agent tools (compressed). International rates still unread |
| 2026-10-21 (wave 3) | Omniva LV, DPD LV | Calculator only (omniva.lv/en/price-lists, eserviss.dpd.lv); no static list. Omniva 2025 Christmas: LV hand-over by 20 Dec, EE/LT 19 Dec |
| 2026-10-21 (wave 3) | US status | Latvijas Pasts resumed private US parcels 18.12.2025 (online registration, provisional duty + clearance fee paid by sender); Omniva resumed private US 30.10.2025 |

## Sources

- Omniva LT business price list 2025 (PDF): https://www.omniva.lt/wp-content/uploads/sites/5/2025/09/BC_PRICELIST_LT_2025_EN_INPUT.pdf (via search summary, not opened; [VERIFY])
- Omniva private customer terms change: https://www.omniva.lt/?p=6563 (via search summary; [VERIFY])
- Omniva EE business notice on seasonal index: https://www.omniva.ee/en/news/important-notice-to-business-clients-about-omniva-pricing-policy/
- LSM, "Latvian postal services will be costlier in 2026" (28 Nov 2025): https://eng.lsm.lv/article/economy/transport/28.11.2025-latvian-postal-services-will-be-costlier-in-2026.a624186/
- lvportals.lv, Latvijas Pasts Christmas 2025 posting reminder (8 Dec 2025): https://lvportals.lv/dienaskartiba/383783-latvijas-pasts-atgadina-par-sutijumu-terminiem-svetkos-2025

- Smartposti LV price list (valid 15.07.2026): https://www.smartposti.lv/paku-nosutisana/sutijumu-cenas
- LSM, Latvijas Pasts resumes private US parcels (18.12.2025): https://eng.lsm.lv/article/economy/transport/18.12.2025-latvian-postal-service-resumes-private-shipping-to-the-usa.a626988/
- Omniva LV Christmas 2025 hand-over dates: https://www.omniva.lv/en/news/omniva-informs-about-parcel-handover-dates-and-urges-customers-to-act-in-time/
- Omniva LT international private price list 2025 (search summary only): https://www.omniva.lt/wp-content/uploads/sites/5/2024/07/pricelist-international-parcels-private-ltu-en-2025-2.pdf
- Full list: `assumptions-wave3.md` Sources.

## TODO / missing data

- Replace section 2a with the owner's actual carrier(s) after decision 8; one calculator quote each for Omniva / DPD /
  Latvijas Pasts (1 kg to DE and US) lifts confidence.
- Carriers used today and any account numbers (owner).
- Packed weights and sizes per product type (dry run, 6 Nov).
- Every price cell, each with URL + date; account quotes if the owner has a business account.
- Claim deadlines and liability caps per carrier and service.
- Christmas 2026 last posting dates per carrier (often published late Nov / early Dec).
- Owner: keep free shipping per region? Paid express for late orders?
