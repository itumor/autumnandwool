# Batch 4 live product SEO changes (2026-11-10)

Scope: 22 products, Squarespace product editor. Per product: backup (products-before.json), name (if changed), SEO title + description (SEO panel APPLY), description (replace / prepend / append links), image alt texts (by position, key checked), save, public check ~30 s later (curl, check.py: title, meta description, h1, canonical, new strings, alts, price, Add To Cart).

Skipped on all products: nothing skipped by key mismatch; no slug changed; no price, stock, SKU, variant or image changes.

## n=1 Gift Card -> Digital Gift Card for Wool Knitwear
- Name: changed. SEO title + description: set. Description: append links block. Alts: 2/2 (spec lists 2 of 3 gallery images; 3rd image left untouched, not in spec). Saved. Price before/after: 25.00.
- Public check: HTTP 200, PASS. Gift Cards tab.

## n=2 Oversized Merino Wool V-Neck Sweater Vest
- Name: kept. SEO title + description: set. Description: append links block. Alts: 10/10. Saved. Price before/after: 126.00.
- Public check: HTTP 200, PASS. Pilot. First save lost the SEO description because the SEO panel needs its APPLY button; fixed, saved, re-checked.

## n=3 Merino Wool Raglan Cardigan
- Name: kept. SEO title + description: set. Description: 2 replacements + append links block. Alts: 14/14. Saved. Price before/after: 160.00.
- Public check: HTTP 200, PASS. Both replacement old strings gone from the public page.

## n=4 Lambswool Raglan Crew — Brown -> Lambswool Raglan Crew Sweater - Brown
- Name: changed. SEO title + description: set. Description: prepend + append links block. Alts: 8/8. Saved. Price before/after: 136.00.
- Public check: HTTP 200, PASS. First attempt's description edits did not persist (prepend helper dropped focus). Re-applied, verified, saved; passed on the second save.

## n=5 Distressed Wool Raglan Sweater — Oversized -> Distressed Oversized Wool Raglan Sweater
- Name: changed. SEO title + description: set. Description: append links block. Alts: 10/10. Saved. Price before/after: 155.00.
- Public check: HTTP 200, PASS.

## n=6 Women’s Classic Lambswool Crew Sweater
- Name: kept. SEO title + description: set. Description: append links block. Alts: 8/8. Saved. Price before/after: 136.00.
- Public check: HTTP 200, PASS.

## n=7 Lambswool Raglan Crew — Green -> Lambswool Raglan Crew Sweater - Green
- Name: changed. SEO title + description: set. Description: prepend + append links block. Alts: 7/7. Saved. Price before/after: 136.00.
- Public check: HTTP 200, PASS.

## n=8 Merino Wool Raglan Sweater — Dusty Pink Oversized Jumper -> Merino Wool Raglan Sweater - Dusty Pink
- Name: changed. SEO title + description: set. Description: append links block. Alts: 9/9. Saved. Price before/after: 155.00.
- Public check: HTTP 200, PASS.

## n=9 Merino Striped Oversized Sweater — Women’s Jumper -> Merino Striped Oversized Sweater
- Name: changed. SEO title + description: set. Description: append links block. Alts: 8/8. Saved. Price before/after: 165.00.
- Public check: HTTP 200, PASS.

## n=10 100% Wool Long Shawl Cardigan – Warm Knit -> 100% Wool Long Shawl Cardigan
- Name: changed. SEO title + description: set. Description: append links block. Alts: 9/9. Saved. Price before/after: 145.00.
- Public check: HTTP 200, PASS.

## n=11 Open-Front Wool Cardigan — Women’s Side-Slit Knit -> Open-Front Wool Cardigan with Side Slits
- Name: changed. SEO title + description: set. Description: append links block. Alts: 9/9. Saved. Price before/after: 155.00.
- Public check: HTTP 200, PASS. Two admin rows share this name; picked the row whose slug matches. First run stopped before any change.

## n=12 Pure Wool Stand-Collar Sweater — Blue -> Pure Wool Stand-Collar Sweater - Blue
- Name: changed. SEO title + description: set. Description: prepend + append links block. Alts: 1/1. Saved. Price before/after: 136.00.
- Public check: HTTP 200, PASS.

## n=13 Pure Wool Side-Slit Sweater — Light Grey -> Pure Wool Side-Slit Sweater - Light Grey
- Name: changed. SEO title + description: set. Description: prepend + append links block. Alts: 7/7. Saved. Price before/after: 136.00.
- Public check: HTTP 200, PASS.

## n=14 Pure Wool Stand-Collar Sweater — Beige -> Pure Wool Stand-Collar Sweater - Beige
- Name: changed. SEO title + description: set. Description: prepend + append links block. Alts: 1/1. Saved. Price before/after: 136.00.
- Public check: HTTP 200, PASS.

## n=15 Pure Wool Side-Slit Sweater — Camel -> Pure Wool Side-Slit Sweater - Camel
- Name: changed. SEO title + description: set. Description: prepend + append links block. Alts: 7/7. Saved. Price before/after: 136.00.
- Public check: HTTP 200, PASS. First attempt stopped at row lookup before any change; retry clean.

## n=16 Rib-Knit Beanie — Unisex
- Name: kept. SEO title + description: set. Description: append links block. Alts: 18 in spec; draft verified (each alt new or original) before save. Saved. Price before/after: 45.00.
- Public check: HTTP 200, PASS. First run stopped at a false pre-save check (&amp; vs &); finished from the same draft, no re-append.

## n=17 Merino Wool Hat & Scarf Set
- Name: kept. SEO title + description: set. Description: append links block. Alts: 17/17. Saved. Price before/after: 110.00.
- Public check: HTTP 200, PASS.

## n=18 Oversized Merino Turtleneck — Dusty Pink Raglan
- Name: kept. SEO title + description: set. Description: append links block. Alts: 9/9. Saved. Price before/after: 155.00.
- Public check: HTTP 200, PASS.

## n=19 Merino Turtleneck — Women’s Lightweight Knit -> Lightweight Merino Turtleneck, 12 Colours
- Name: changed. SEO title + description: set. Description: append links block. Alts: 9/9. Saved. Price before/after: 110.00.
- Public check: HTTP 200, PASS.

## n=20 Long Wool Cardigan — Women’s Shawl Collar -> Long Wool Cardigan with Shawl Collar
- Name: changed. SEO title + description: set. Description: append links block. Alts: 9/9. Saved. Price before/after: 145.00.
- Public check: HTTP 200, PASS.

## n=21 Oversized Wool Raglan Sweater — Beige Melange
- Name: kept. SEO title + description: set. Description: append links block. Alts: 10/10. Saved. Price before/after: 155.00.
- Public check: HTTP 200, PASS.

## n=22 Oversized Wool V-Neck Vest - Beige Melange
- Name: kept. SEO title + description: set. Description: append links block. Alts: 10/10. Saved. Price before/after: 126.00.
- Public check: HTTP 200, PASS.

