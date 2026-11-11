# Batch 9 live product twin-link paragraphs (2026-11-10)

Scope: 8 products, one paragraph prepended to the description (`prepend_html` from `business-os/seo-marketplace/live-2026-11-10-b/twin-prepends.json`). Nothing else changed: no name, price, variants, stock, images, alt, SEO fields, slug, categories or visibility. Save via editor SAVE, not Cancel.

Method: admin Commerce > Products > Physical > row overflow (...) > Edit. Slug checked in the editor's SEO and URL section before any edit. Description backed up to `backup/twin-<n>-description-before-b9.html`. Caret placed at description start, Enter, then ArrowUp and paste of the paragraph (rich paste keeps the relative href). Editor paragraph count went 17 -> 18 for each product.

Incidents (both resolved, no save of a wrong state):
- Product 2 (Beige): first attempt merged the new paragraph into the old first paragraph. Undo x2 restored the backup HTML exactly (verified byte-equal). Re-done cleanly before SAVE.
- Product 3 (Light Grey): first attempt split at the wrong place (trailing empty paragraph). One undo restored backup HTML exactly before any paste.
- Product 1 (Blue): first attempt had an accidental split, reverted with one undo (17 paragraphs, original text) before the real edit.

| n | slug (URL) | done/skipped | link ok? | public check (curl, 200) | price before / after |
|---|---|---|---|---|---|
| 1 | hand-knitted-wool-stand-collar-sweater-womens-knitwear-679510 | done | yes (href /shop/p/p/hand-knitted-wool-sweater-stand-collar-knit-679503, text "beige") | PASS: new text, twin href, old start present, h1 "Pure Wool Stand-Collar Sweater - Blue", Add To Cart | 136.00 / 136.00 |
| 2 | hand-knitted-wool-sweater-stand-collar-knit-679503 | done | yes (href .../679510, text "blue") | PASS (same checks, h1 "Pure Wool Stand-Collar Sweater - Beige") | 136.00 / 136.00 |
| 3 | hand-knitted-wool-sweater-organic-knitwear-asymmetrical-design-1 | done | yes (href .../organic-knit-jumper-1, text "camel") | PASS (h1 "Pure Wool Side-Slit Sweater - Light Grey") | 136.00 / 136.00 |
| 4 | hand-knitted-wool-sweater-womens-organic-knit-jumper-1 | done | yes (href .../asymmetrical-design-1, text "light grey") | PASS (h1 "Pure Wool Side-Slit Sweater - Camel") | 136.00 / 136.00 |
| 5 | hand-knitted-lambswool-sweater-womens-winter-knitwear-1 | done | yes (href .../cozy-and-sustainable-hand-knitted-lambswool-sweater-for-women, text "brown") | PASS (h1 "Lambswool Raglan Crew Sweater - Green") | 136.00 / 136.00 |
| 6 | cozy-and-sustainable-hand-knitted-lambswool-sweater-for-women | done | yes (href .../winter-knitwear-1, text "green") | PASS (h1 "Lambswool Raglan Crew Sweater - Brown") | 136.00 / 136.00 |
| 7 | hand-knitted-wool-cardigan-minimalist-open-front-sweater-1 | done | yes (href .../wool-cardigan-warm-...-minimalist-style-sweater, text "shawl-collar cardigan") | PASS (h1 "100% Wool Long Shawl Cardigan") | 145.00 / 145.00 |
| 8 | wool-cardigan-warm-cardigan-organic-wool-wrap-winter-sweater-cardigan-women-cardigan-sweater-minimalist-style-sweater | done | yes (href .../hand-knitted-wool-cardigan-minimalist-open-front-sweater-1, text "here") | PASS (h1 "Long Wool Cardigan with Shawl Collar") | 145.00 / 145.00 |

Public check method: curl -sS -A "Mozilla/5.0", ~25 s after SAVE. Raw pages: scratchpad post-1..8.html. Checks per product: HTTP 200; first 40 chars of new paragraph present; twin href present; old description start present; h1 text as before; "Add To Cart" present (2 occurrences); price value unchanged in page JSON.

Not checked: the 40-char and href checks are substring matches on the raw HTML, not a rendered-DOM check. Editor-side checks were done before save.
