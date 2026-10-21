# Size, fit and measurement standard for all PDPs — 2026-10-21 — DRAFT

Owner: aw-ecommerce-cro. Task CRO-11 (plan: "size/fit and measurement format proposal, one table for all", by 7 Nov).
Product data frozen: the owner pastes this per PDP after approval. KPI: conversion (step 2 Explores) and returns
avoided (fit questions answered before purchase).

## 1. The block (same order and wording on every garment PDP)

```
FIT
<Oversized | Relaxed | Straight, relaxed | Close to the body>. <One size | Sizes S–XL | Sizes S/M, L/XL | Sizes XS–M>.
Model is <cm> cm and wears <size>.            <- only if known; otherwise omit the line, never guess

MEASUREMENTS (garment laid flat, cm) — see Size Guide
<size>: width <cm> · front length <cm> · back length <cm, only if hem is curved/asymmetric> · sleeve from neck <cm>
(one line per size; inches optional in brackets, e.g. 61 cm (24 in), same on every page or none)
Measurements may vary slightly between knits.

MATERIAL
<exact label wording, e.g. 100% merino wool>   <- never "wool" without % if the label states one

CARE
Hand wash cold with a wool-safe detergent. Do not tumble dry. Lay flat to dry.
```

Rules
- cm first, always. Inches either on every page or on none (decision for owner; today vest = cm only, cardigan = cm +
  in, QA s5). CRO recommends cm only + the Size Guide's cm/in toggle, to keep the block short on a phone.
- Width = armpit to armpit, laid flat. Length = shoulder high point to hem. Sleeve from neck = neck seam to cuff.
  [OWNER: confirm this is how existing numbers were taken, so all pages measure the same way]
- Accessories: beanie = head circumference range + height in cm; scarf = length x width.
- "Measurements may vary slightly between knits" is the live wording on the vest and dusty pink PDPs; reuse it, do
  not invent a tolerance in cm.

## 2. Gap matrix (visible garments)

Source: `build_google_feed.py` `D` (cleaned descriptions), live WebFetch for the 6 PDPs fetched on 21 Oct.
"Not checked live" = the live page may have more than the feed script; verify before asking the owner to measure.

| Product | Sizes | Fit stated | Measurements on file | Model line | Fibre % | Action |
|---|---|---|---|---|---|---|
| Oversized Merino V-Neck Sweater Vest | one size | Oversized, relaxed | W59 L68 armhole 30 (live) | no | 100% | Add model line if known |
| Merino Wool Raglan Cardigan | one size | Relaxed, slightly oversized | W61 FL67 sleeve 82/49, collar 4 (live, cm+in) | no | 100% | Decide inches rule |
| Oversized Wool V-Neck Vest — Beige Melange | one size | not in feed text | W57 L69 (feed) | ? | "Wool" (no %) | Fibre % [OWNER]; not checked live |
| Oversized Wool Raglan Sweater — Beige Melange | one size | Oversized (title) | W59 FL60 BL69 (feed) | ? | 100% pure wool | Not checked live |
| Pure Wool Side-Slit Sweater — Camel | S–XL | Relaxed | none in feed | ? | 100% pure new wool | Measure 4 sizes |
| Pure Wool Side-Slit Sweater — Light Grey | S–XL | Relaxed | none in feed | ? | 100% | Same numbers as Camel? [OWNER] |
| Lambswool Raglan Crew — Brown | S–XL | Relaxed | none in feed | ? | 100% lambswool | Measure 4 sizes |
| Lambswool Raglan Crew — Green | S–XL | Relaxed | none in feed | ? | 100% | Same as Brown? [OWNER] |
| Women's Classic Lambswool Crew Sweater | S–XL | Relaxed | none in feed | ? | 100% | Same as Brown? [OWNER] |
| Distressed Wool Raglan Sweater | one size | Oversized | W57 FL66 BL71 (feed) | ? | "Wool" (no %) | Fibre % [OWNER] |
| Merino Striped Oversized Sweater | one size | Oversized | W59 FL67 sleeve 74 (feed) | ? | 100% merino | Not checked live |
| 100% Wool Long Shawl Cardigan – Warm Knit | S–XL | not in feed text | none in feed | ? | 100% pure new wool | Measure 4 sizes |
| Long Wool Cardigan — Women's Shawl Collar | S–XL | Straight, relaxed | none (live confirmed) | 171 cm, M | 100% pure new wool | Measure 4 sizes |
| Open-Front Wool Cardigan — Side-Slit Knit | one size | not in feed text | W56 L70 (feed) | ? | 100% pure new wool | Fit word [OWNER] |
| Merino Turtleneck — Lightweight Knit | XS, S, M | Close to the body | none in feed | ? | 100% merino | Measure 3 sizes |
| Pure Wool Stand-Collar Sweater — Beige | S–XL | Relaxed | none in feed | ? | 100% pure new wool | Measure 4 sizes |
| Pure Wool Stand-Collar Sweater — Blue | S–XL | Relaxed | none in feed | ? | 100% | Same as Beige? [OWNER] |
| Oversized Merino Turtleneck — Dusty Pink Raglan | one size | Oversized | W53 FL63 BL70 (feed) | ? | "Merino wool" (no %) | Fibre % [OWNER] |
| Merino Wool Raglan Sweater — Dusty Pink | S/M, L/XL | Oversized | per size (live) — model example | no | "merino wool" (no %) | Fibre %, size mapping |
| Rib-Knit Beanie | one size | n/a | head 54–58 cm | n/a | 100% (CLAIM-CHECK qualifiers) | Height cm |
| Merino Wool Hat & Scarf Set | one size | n/a | head 54–58; scarf 190 x 36 | n/a | 100% (CLAIM-CHECK) | none |

Count from this matrix: 10 sized garments have no garment measurements in the feed text; 4 garments lack a fibre % (Beige Melange vest, Distressed raglan, both Dusty Pink pieces).
Only 1 PDP (Long Wool Cardigan) states the model's height and size.

## 3. Owner measuring task (for PRD / owner, batch of <= 15 min per product)
Lay one finished piece of each size flat, measure width, length (front/back if different), sleeve from neck. Write
numbers into a copy of this table and send to CRO; CRO turns them into the paste-ready block. Colour twins (side-slit,
lambswool, stand-collar) need measuring once if the owner confirms the pattern is identical.
