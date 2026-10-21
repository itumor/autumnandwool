DRAFT — for owner approval

# Carrier comparison (template + research notes)

OPS-05, agent `aw-operations`, 2026-10-21. Template only: **no rate is filled**. Every price must come from the
carrier's own public price list or the owner's account quote, with URL and date. Carrier choice and any contract =
owner decision 8 (due 28 Oct). Filling the table = OPS-06 (blocked, see status file).

Sources: `.claude/skills/aw-fulfilment-sop` (rate-table format); Merchant Center shipping policy as recorded in
`implementation-report.md`; web checks 2026-10-21 listed in section 4.

## 1. Regions to price (from current promises)

| Region code | Countries | Current promise (Merchant Center, not carrier-backed) | Squarespace zone | Checkout tested? |
|---|---|---|---|---|
| LV | Latvia | Free; 2-5 handling + 2-5 transit | Latvia (EUR 0) | Yes (to payment step only) |
| EU-18 | Austria, Belgium, Finland, France, Germany, Greece, Ireland, Italy, Netherlands, Portugal, Slovakia, Spain, Czechia, Denmark, Hungary, Poland, Romania, Sweden | Free; 2-5 + 5-10 | Rest of World (EUR 0) | No |
| BALT | Estonia, Lithuania | **Not in the Merchant Center list** (see `delivery-promise-reconciliation.md`) | Rest of World (EUR 0) | No |
| US-CA-AU | United States, Canada, Australia | Free; 2-5 + 7-20 | United States / Rest of World (EUR 0) | No |
| OTHER | UK, NO, CH and all other countries | No Merchant Center promise | Rest of World (EUR 0) | No |

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

## Sources

- Omniva LT business price list 2025 (PDF): https://www.omniva.lt/wp-content/uploads/sites/5/2025/09/BC_PRICELIST_LT_2025_EN_INPUT.pdf (via search summary, not opened; [VERIFY])
- Omniva private customer terms change: https://www.omniva.lt/?p=6563 (via search summary; [VERIFY])
- Omniva EE business notice on seasonal index: https://www.omniva.ee/en/news/important-notice-to-business-clients-about-omniva-pricing-policy/
- LSM, "Latvian postal services will be costlier in 2026" (28 Nov 2025): https://eng.lsm.lv/article/economy/transport/28.11.2025-latvian-postal-services-will-be-costlier-in-2026.a624186/
- lvportals.lv, Latvijas Pasts Christmas 2025 posting reminder (8 Dec 2025): https://lvportals.lv/dienaskartiba/383783-latvijas-pasts-atgadina-par-sutijumu-terminiem-svetkos-2025

## TODO / missing data

- Carriers used today and any account numbers (owner).
- Packed weights and sizes per product type (dry run, 6 Nov).
- Every price cell, each with URL + date; account quotes if the owner has a business account.
- Claim deadlines and liability caps per carrier and service.
- Christmas 2026 last posting dates per carrier (often published late Nov / early Dec).
- Owner: keep free shipping per region? Paid express for late orders?
