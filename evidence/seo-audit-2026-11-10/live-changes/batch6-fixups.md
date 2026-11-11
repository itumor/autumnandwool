# Batch 6: fix-ups (2026-11-10)

Browser: ego-browser task space 15 (`aw-batch6-fixups-2026-11-10`). Backups in `evidence/seo-audit-2026-11-10/backup/`.

## FIX 1: wool Code blocks (4 pages) - DONE
- Old: editor content = previous version (wool-sweaters 9301 chars, wool-cardigans 5536, wool-sweater-vests 4588, wool-hats-and-scarves 4597). Backups: `backup/<slug>-codeblock-before-fix1.html`.
- New: `business-os/seo-marketplace/live-2026-11-10/html/<slug>.html` (re-read from disk at paste time; contains `minmax(0,1fr)`). Sizes 9278 / 5612 / 4711 / 4695.
- CM6 synthetic paste; editor length = file length, equal. Saved, exited.
- Public (30 s+): all 200; no `?format=1500w?format=500w`; no `src="http://`; one `<h1`; "Shop the full collection" present; `minmax(0,1fr)` present; aw-seo-grid images all 200 (wool-sweaters 13, wool-cardigans 4, wool-sweater-vests 2, wool-hats-and-scarves 2).
- Screenshots (fresh headless Chrome): `evidence/seo-audit-2026-11-10/after/screenshots/fix-wool-sweaters-desktop.png` (4 columns visible at 1440) and `fix-wool-sweaters-mobile.png` (390x844, first viewport shows heading and grid below fold). Tall 390-wide capture: 2 columns, images visible, nothing clipped in capture.

## FIX 2: llms.txt - DONE
- Old: 7525 chars (`backup/llms-before-fix2.txt`), not checked for phrases before replacing.
- New: 7503 chars from `business-os/seo-marketplace/live-2026-11-10/llms.txt`. Paste equal; SAVE; closed.
- Public after 60 s: 200 text/plain, len 7503, contains "knitted on a manual knitting machine": yes; contains "knitted by hand": no.

## FIX 3: URL mapping last line - DONE
- Live had 7 lines (admin-recon section 9 had 6; the 7th `/shop/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper` line was added after the recon). Backup: `backup/url-mappings-before-fix3.txt`.
- Old last line: `/shop/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper -> /shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper 301`
- New last line: `/shop/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper -> https://www.autumnandwool.com/shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper 301`
- Lines 1-6 byte-identical (verified in script). Saved.
- Check: `curl -sSI .../shop/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper` -> 301, location https://www.autumnandwool.com/shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper. Target returns 200.

## FIX 4: product SEO title = name - DONE (17/17)
- Backup: `backup/seo-titles-before-fix4.json`. Admin Name field equalled the TSV name for all 17 (no Name-field override needed).
- Path note: product URLs for some rows are `/shop/p/p/<slug>`; checked with the path that returns 200.
- Public check per product: title = name, h1 = name, JSON-LD Product name = h1, Add To Cart present, visible price shown.

| n | slug (short) | SEO title before -> after | public |
|---|---|---|---|
| 2 | oversized-merino-wool-v-neck-sweater-vest | Oversized Merino Wool Sweater Vest -> Oversized Merino Wool V-Neck Sweater Vest | OK, EUR 126.00 |
| 3 | black-merino-wool-cardigan-...-1 | Merino Wool Raglan Cardigan in Black, Brown or Blue -> Merino Wool Raglan Cardigan | OK, EUR 160.00 |
| 4 | cozy-and-sustainable-hand-knitted-lambswool-... | Lambswool Raglan Crew Sweater, Brown -> Lambswool Raglan Crew Sweater - Brown | OK, EUR 136.00 |
| 6 | hand-knitted-lambswool-sweater-womens-grey-knit-jumper | Women's Classic... -> Women’s Classic Lambswool Crew Sweater | OK, EUR 136.00 |
| 7 | hand-knitted-lambswool-sweater-womens-winter-knitwear-1 | ... -> Lambswool Raglan Crew Sweater - Green | OK, EUR 136.00 |
| 8 | hand-knitted-merino-wool-raglan-sweater-dusty-pink-... | Merino Raglan Sweater, Dusty Pink -> Merino Wool Raglan Sweater - Dusty Pink | OK, EUR 155.00 |
| 10 | hand-knitted-wool-cardigan-minimalist-open-front-sweater-1 | Long Wool Shawl Cardigan, 100% Wool -> 100% Wool Long Shawl Cardigan | OK, EUR 145.00 |
| 12 | hand-knitted-wool-stand-collar-sweater-womens-knitwear-679510 | -> Pure Wool Stand-Collar Sweater - Blue | OK, EUR 136.00 |
| 13 | hand-knitted-wool-sweater-organic-knitwear-asymmetrical-design-1 | -> Pure Wool Side-Slit Sweater - Light Grey | OK |
| 14 | hand-knitted-wool-sweater-stand-collar-knit-679503 | -> Pure Wool Stand-Collar Sweater - Beige | OK, EUR 136.00 (save reported editor still open; CANCEL with no pending change) |
| 15 | hand-knitted-wool-sweater-womens-organic-knit-jumper-1 | -> Pure Wool Side-Slit Sweater - Camel | OK |
| 16 | merino-beanie-...-1 | Merino Rib-Knit Beanie, Unisex -> Merino Rib-Knit Beanie - Unisex | OK |
| 17 | merino-wool-hat-scarf-set-... | Merino Wool Hat & Scarf Set in Black, Gray or Brown -> Merino Wool Hat & Scarf Set | OK |
| 18 | merino-wool-sweater-oversize-...-679519 | -> Oversized Merino Turtleneck — Dusty Pink Raglan | OK, EUR 155.00 |
| 20 | wool-cardigan-warm-cardigan-... | Long Wool Shawl Collar Cardigan -> Long Wool Cardigan with Shawl Collar | OK |
| 21 | wool-sweater-sweater-for-women-... | -> Oversized Wool Raglan Sweater — Beige Melange | OK, EUR 155.00 |
| 22 | wool-sweater-vest-knitted-wool-vest-... | -> Oversized Wool V-Neck Vest - Beige Melange | OK, EUR 126.00 |

Notes: admin price field read as null by the helper for most rows; prices were not edited (only the SEO title field + APPLY + SAVE). Visible public prices listed above.

## FIX 5: logo alt - NOT CONFIRMED, NOT CHANGED
- Homepage logo `<img alt>` = `Autumn &amp;amp; Wool` (double escape), confirmed by curl.
- Could not locate a simple editable field containing the literal `Autumn &amp; Wool` in Settings > Website / Settings > Brand (the admin settings pages rendered the dashboard instead of the sections). Site header editor not opened. Nothing saved.

## Final checks (2026-11-10)
- `/` 200, `/shop` 200, `/wool-sweaters` 200, `/wool-gifts` 200, `/shop/p/oversized-merino-wool-v-neck-sweater-vest` 200, `/shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper` 200, `/llms.txt` 200.
