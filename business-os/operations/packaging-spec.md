DRAFT — for owner approval

# Packaging spec + supplies list

OPS-04, agent `aw-operations`, 2026-10-21. Proposal only: packaging style, supplier and every purchase are owner
decisions (decision 8 in the ops plan / decision 13 in the master plan, due 30 Oct). No supplier, price or
dimension below is invented: unknown = TODO / [VERIFY].

Sources: `business-os/README.md` s6 (care card, branding, protection) and s9 (illustrative packaging EUR 3 per
order); `.claude/skills/aw-fulfilment-sop` stage 4; `.claude/skills/aw-brand-voice` (claim rules, palette);
`.claude/skills/aw-qc-and-labelling` s3 (care info); `sku-economics.csv` (product types, packaging_eur blank).

## 1. Goals

1. Garment arrives clean, dry, uncrushed and presentable.
2. Parcel is as small and light as possible, so it fits the cheapest carrier size class (parcel lockers price by
   size class; Omniva business list uses S/M/L classes — exact dimensions [VERIFY per carrier]).
3. Same look every time (one person can pack it in under 10 minutes [VERIFY in dry run]).
4. No claim on packaging that we cannot prove: no "eco", "plastic-free", "recyclable", "compostable" wording
   unless the supplier certifies it and the owner approves (brand-voice s3).

## 2. Pack types

| Pack type | Use for (visible range) | Outer | Inner | Weight + size |
|---|---|---|---|---|
| P1 small | Rib-knit beanie, single accessories | Padded or plain mailer bag, size TODO | Tissue wrap, care card, packing slip | Weigh in dry run (TODO) |
| P2 standard | Sweaters, vests, raglan cardigans | Mailer bag or slim box, size TODO | Tissue wrap, care card, packing slip, optional thank-you card | Weigh in dry run (TODO) |
| P3 large | Long shawl cardigan, hat + scarf set, multi-item orders | Box (or large mailer), size TODO | As P2; second tissue wrap per item | Weigh in dry run (TODO) |
| Gift card | Digital gift card | None (no shipping) | — | — |

Rule: if a P2 garment does not fit the smallest locker class of the chosen carrier when folded, test the next
fold (roll vs flat) in the dry run before upsizing. Record the result per SKU in the table in section 5.

## 3. Packing steps (stage 4 of the SOP)

1. Hands clean, table clear, lint roller ready.
2. Garment passed QC (11 checks). Fold to the agreed fold for that SKU (photo reference TODO).
3. Wrap in tissue; seal with one sticker/label.
4. Add care card (matching the product's yarn) and packing slip with order no.
5. Optional thank-you card (owner decides; handwritten note = time cost, measure in dry run).
6. Moisture protection for outer mailers if the outer is paper-based [VERIFY need in dry run: wet weather in
   Nov-Dec].
7. Seal, weigh (g), photograph open pack and sealed parcel, attach label.

## 4. Inserts (text drafts, owner approves)

| Insert | Content | Status |
|---|---|---|
| Care card | Per yarn, from the supplier's care advice and the live product page only. Wool default to verify per yarn: hand wash cold or wool cycle, dry flat, no tumble dry. Never "machine washable" without supplier proof | Wording per yarn TODO (Production holds supplier spec sheets) |
| Packing slip | Order no., items, size, colour. "Questions or returns: autumnandwool@gmail.com". Return instructions = only after the returns wording is approved (master plan C12) | Template TODO after decision 13 + adviser |
| Thank-you card | Short, calm, signed Kristine. No discount code unless the owner creates one (plan may lock codes, ruling C6) | Optional |

Visual: oat `#F2EDE6`, ink `#24201C`, rust `#8E3B1F` accent; Instrument Serif / DM Sans (brand-voice s5).

## 5. Per-SKU pack record (fill in dry run and first orders)

| Product type | Pack type | Folded size (cm) | Packed weight (g) | Fits carrier class | Notes |
|---|---|---|---|---|---|
| Beanie | P1 | TODO | TODO | TODO | |
| Sweater (raglan / crew) | P2 | TODO | TODO | TODO | |
| Vest | P2 | TODO | TODO | TODO | |
| Raglan cardigan | P2 | TODO | TODO | TODO | |
| Long shawl cardigan | P3 | TODO | TODO | TODO | Heaviest item likely; weigh first |
| Hat + scarf set | P3 | TODO | TODO | TODO | |

## 6. Supplies list (quotes needed; owner buys)

| Item | Spec | Qty for first 30 orders (proposal) | Supplier + unit price | Source + date |
|---|---|---|---|---|
| Mailer P1 | TODO size | 10 | TODO quote | TODO |
| Mailer / box P2 | TODO size | 20 | TODO quote | TODO |
| Box P3 | TODO size | 5 | TODO quote | TODO |
| Tissue paper | Acid-free if available [VERIFY], neutral colour | 1 pack | TODO | TODO |
| Seal stickers | Logo optional (branded = owner approval) | 1 roll | TODO | TODO |
| Care cards | Printed per yarn | 50 | TODO | TODO |
| Packing slips | Printed from order (office paper) | — | existing | — |
| Thank-you cards | Optional | 30 | TODO | TODO |
| Shipping labels | Depends on carrier (thermal vs A4) | — | TODO after carrier choice | — |
| Scale (g) | Kitchen / parcel scale, 1 g to 5 kg [VERIFY owner has one] | 1 | TODO | — |
| Tape, lint roller | — | — | existing? | — |

Cost per pack (target to compare with `sku-economics.csv` packaging_eur and the README s9 illustration EUR 3):
`sum(unit prices of items used in that pack type)`. TODO until quotes exist. Write the result to the weekly ops
file as a proposal; Finance/owner updates the sheet.

## TODO / missing data

- Owner: packaging style (plain vs branded), budget cap for first order of supplies, thank-you card yes/no.
- Quotes for every supply line (supplier, unit price, MOQ, date).
- Carrier size classes and dimension limits (after carrier choice).
- Folded sizes and packed weights per product type (dry run, OPS-11).
- Care-card wording per yarn (Production, supplier spec sheets).
- Return instructions for the packing slip (after adviser + decision 13).
