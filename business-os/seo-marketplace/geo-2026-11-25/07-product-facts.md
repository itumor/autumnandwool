# GEO-07: product facts, first sentences, hand-knitted clash (DRAFT, 2026-11-25)

Status: DRAFT for owner. Nothing on the live site was changed. Fibre % is never guessed: where a page does not give it, the cell says `[FILL]`.

How checked: each of the 22 product URLs in `llms.txt` was fetched live on 2026-11-25 with WebFetch (no shell/curl was available). WebFetch returns the visible page text only. It cannot show the `<title>` tag, meta description, image alts or JSON-LD, so those are marked UNVERIFIED. Prior work read: `business-os/seo-marketplace/live-2026-11-10/product-change-sheet.md`. The big Oct CSV `products_Oct-17_10-46-00PM.csv` was not read line by line (773 lines, blocked by a read hook); it is older than the 10 Nov live edits, so live pages were used as the fact source.

House phrase for how it is made: **machine-knitted on a manual knitting machine, hand-finished in Riga.** Origin "Riga/Latvia" is still an open claim (C-04, README §7). Every sentence below carries CLAIM-CHECK for that reason.

## 1. Product table

Quote column = exact "Material" or fibre wording on the live page today. Slug = path after `https://www.autumnandwool.com/shop/p/` (unchanged).

| # | Product (live H1) | URL slug | Fibre as stated now (quote) | % known? | Proposed first sentence (≤30 words) | Gaps |
|---|---|---|---|---|---|---|
| 1 | Long Wool Cardigan with Shawl Collar | `p/wool-cardigan-warm-cardigan-organic-wool-wrap-winter-sweater-cardigan-women-cardigan-sweater-minimalist-style-sweater` | "Material: 100% pure new wool" | Yes | Knee-length open-front cardigan in 100% pure new wool, straight relaxed fit with a draped shawl collar, machine-knitted on a manual knitting machine and hand-finished in Riga. (26) | [FILL: colour] |
| 2 | 100% Wool Long Shawl Cardigan | `p/hand-knitted-wool-cardigan-minimalist-open-front-sweater-1` | "Material: 100% pure new wool" | Yes | Long open-front cardigan in 100% pure new wool, straight relaxed fit with dropped shoulders and a draped collar, machine-knitted on a manual knitting machine and hand-finished in Riga. (28) | [FILL: colour] |
| 3 | Open-Front Wool Cardigan with Side Slits | `p/hand-knitted-wool-cardigan-open-front-winter-sweater-679428` | "Material: 100% pure new wool" | Yes | Straight-cut open-front cardigan in 100% pure new wool with side slits and ribbed cuffs, relaxed fit, machine-knitted on a manual knitting machine and hand-finished in Riga. (27) | [FILL: colour] |
| 4 | Merino Wool Raglan Cardigan | `p/black-merino-wool-cardigan-100-merino-wool-raglan-sweater-minimalist-knitwear-sustainable-handmade-womens-cardigan-1` | "A relaxed raglan cardigan in 100% merino wool" / "Material: 100% merino wool" | Yes | Relaxed, slightly oversized raglan cardigan in 100% merino wool, one size, machine-knitted on a manual knitting machine and hand-finished in Riga. (23) | Brown and Blue "to order": [FILL: lead time] |
| 5 | Oversized Wool Raglan Sweater - Beige Melange | `p/wool-sweater-sweater-for-women-knit-cozy-pullover-sweater-sustainable-knitwear-oversized-wool-jumper-relaxed-fit-wool-pullover-1` | "Material: 100% pure wool" | Yes, but wording differs from "pure new wool" elsewhere | Oversized raglan sweater in beige melange, [FILL: confirm 100% pure wool or pure new wool], machine-knitted on a manual knitting machine and hand-finished in Riga. (25) | [FILL: exact fibre wording] |
| 6 | Merino Wool Raglan Sweater - Dusty Pink | `p/hand-knitted-merino-wool-raglan-sweater-dusty-pink-oversized-jumper` | None. No Material line; only "Merino" in the H1 | **No** | Oversized raglan sweater in dusty pink, [FILL: fibre %] merino wool, machine-knitted on a manual knitting machine and hand-finished in Riga. (23) | [FILL: fibre %], [FILL: Material line missing] |
| 7 | Oversized Merino Turtleneck - Dusty Pink Raglan | `p/merino-wool-sweater-oversize-sweater-knitted-wool-jumper-stand-up-collar-jumper-relaxed-fit-wool-pullover-warm-pink-jumper-679519` | "Material: merino wool" | **No** | Oversized raglan turtleneck in dusty pink, [FILL: fibre %] merino wool, roomy fit, machine-knitted on a manual knitting machine and hand-finished in Riga. (24) | [FILL: fibre %] |
| 8 | Merino Striped Oversized Sweater | `p/hand-knitted-merino-wool-striped-sweater-oversized-jumper` | "Material: 100% merino wool" | Yes | Oversized striped sweater in 100% merino wool with fully fashioned shoulder shaping, machine-knitted on a manual knitting machine and hand-finished in Riga. (24) | [FILL: colour/stripe colours] |
| 9 | Distressed Oversized Wool Raglan Sweater | `p/hand-knitted-distressed-wool-sweater-oversized-raglan-jumper-1` | "Material: wool" | **No** (no % and no fibre type) | Oversized raglan sweater with distressed details in [FILL: fibre and %], roomy fit, machine-knitted on a manual knitting machine and hand-finished in Riga. (24) | [FILL: fibre type and %], [FILL: colour] |
| 10 | Lightweight Merino Turtleneck, 12 Colours | `p/merino-wool-turtleneck-sweater-womens-knit-pullover-soft-warm-lightweight-minimalist-sustainable-knitwear-sizes-sl-12-679428` | "Material: 100% merino wool" | Yes | Lightweight turtleneck in 100% merino wool, close fit, in 12 colours, machine-knitted on a manual knitting machine and hand-finished in Riga. (22) | Colour list on page: [FILL: confirm 12 colour names] |
| 11 | Pure Wool Side-Slit Sweater - Camel | `p/hand-knitted-wool-sweater-womens-organic-knit-jumper-1` | "100% pure new wool" | Yes | Camel round-neck sweater in 100% pure new wool with side slits and a longer back hem, relaxed fit, machine-knitted on a manual knitting machine and hand-finished in Riga. (29) | none |
| 12 | Pure Wool Side-Slit Sweater - Light Grey | `p/hand-knitted-wool-sweater-organic-knitwear-asymmetrical-design-1` | "100% pure new wool" | Yes | Light grey round-neck sweater in 100% pure new wool, asymmetric hem shorter at the front, relaxed fit, machine-knitted on a manual knitting machine and hand-finished in Riga. (29) | none |
| 13 | Pure Wool Stand-Collar Sweater - Beige | `p/hand-knitted-wool-sweater-stand-collar-knit-679503` | "Material: 100% pure new wool" | Yes | Beige stand-collar sweater in 100% pure new wool, relaxed fit, sizes S to XL, machine-knitted on a manual knitting machine and hand-finished in Riga. (25) | One photo only |
| 14 | Pure Wool Stand-Collar Sweater - Blue | `p/hand-knitted-wool-stand-collar-sweater-womens-knitwear-679510` | "Material: 100% pure new wool" | Yes | Blue stand-collar sweater in 100% pure new wool, relaxed fit, sizes S to XL, machine-knitted on a manual knitting machine and hand-finished in Riga. (25) | One photo only |
| 15 | Lambswool Raglan Crew Sweater - Brown | `p/cozy-and-sustainable-hand-knitted-lambswool-sweater-for-women` | "Material: 100% lambswool (pure new wool)" | Yes | Brown raglan crew sweater in 100% lambswool with a round ribbed neck and curved hem, relaxed fit, machine-knitted on a manual knitting machine and hand-finished in Riga. (28) | none |
| 16 | Lambswool Raglan Crew Sweater - Green | `p/hand-knitted-lambswool-sweater-womens-winter-knitwear-1` | "Material: 100% lambswool (pure new wool)" | Yes | Green raglan crew sweater in 100% lambswool with a round ribbed neck and curved hem, relaxed fit, machine-knitted on a manual knitting machine and hand-finished in Riga. (28) | none |
| 17 | Women's Classic Lambswool Crew Sweater | `p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper` | "Material: 100% lambswool (pure new wool)" | Yes | [FILL: colour] raglan crew sweater in 100% lambswool with ribbed cuffs and a gently curved hem, relaxed fit, machine-knitted on a manual knitting machine and hand-finished in Riga. (27) | [FILL: colour] (slug suggests grey, page does not say) |
| 18 | Oversized Merino Wool V-Neck Sweater Vest | `oversized-merino-wool-v-neck-sweater-vest` | "Material: 100% extra-fine merino wool" | Yes | Oversized V-neck vest in 100% merino wool with ribbed edging and Japanese-style shoulder shaping, relaxed fit, machine-knitted on a manual knitting machine and hand-finished in Riga. (28) | "extra-fine" needs spec; no "how made" line on page; [FILL: colour] (alts say grey) |
| 19 | Oversized Wool V-Neck Vest - Beige Melange | `p/wool-sweater-vest-knitted-wool-vest-oversized-vest-womens-woolen-pullover-vest-top-sleeveless-wool-knit-vest-soft-v-neck-vest` | "Material: wool" | **No** | Oversized V-neck vest in beige melange, [FILL: fibre and %], relaxed fit, machine-knitted on a manual knitting machine and hand-finished in Riga. (24) | [FILL: fibre type and %]; no "how made" line on page |
| 20 | Merino Rib-Knit Beanie - Unisex | `p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1` | "Material: 100% extra-fine merino wool, Italian-spun yarn" | Yes | Unisex rib-knit beanie in 100% merino wool with a fold-over cuff, one size for 54-58 cm heads, machine-knitted on a manual knitting machine and hand-finished in Riga. (28) | "extra-fine" and "Italian-spun" need spec; no "how made" line on page |
| 21 | Merino Wool Hat & Scarf Set | `p/merino-wool-hat-scarf-set-extra-fine-rib-knit-soft-on-skin-warm-not-bulky-unisex-gift` | "Material: 100% extra-fine merino wool, Italian-spun yarn" | Yes | Matching rib-knit beanie and scarf set in 100% merino wool, beanie one size for 54-58 cm heads, machine-knitted on a manual knitting machine and hand-finished in Riga. (27) | Same as 20; no "how made" line on page |
| 22 | Digital Gift Card for Wool Knitwear | `autumn-and-wool-digital-gift-card` | n/a (no fibre) | n/a | Digital gift card for Autumn & Wool knitwear: a unique code sent by email, redeemed at checkout to reduce the order total. (22) | [FILL: confirm "never expires" is policy] |

Notes on the table:
- Word counts in brackets are my count and are all ≤30. Items 6, 7, 9, 19 and 5 cannot be published until the owner supplies the fibre.
- "Japanese-style shoulder shaping" is the page's own wording. "Italian-spun" and "extra-fine" are on the live page but have no evidence on file (change sheet CLAIM-CHECK 2). They are left out of the proposed sentences on purpose.
- llms.txt names for items 10, 15, 16, 20 differ from the live H1s (llms.txt is stale on names: "Merino Turtleneck — Lightweight Knit" vs live "Lightweight Merino Turtleneck, 12 Colours"; "Rib-Knit Merino Beanie" vs "Merino Rib-Knit Beanie"; "Long Wool Cardigan — Women's Shawl Collar" vs "Long Wool Cardigan with Shawl Collar"; "Open-Front Wool Cardigan — Side-Slit Knit" vs "… with Side Slits"; "Lambswool Raglan Crew — Brown" vs "Lambswool Raglan Crew Sweater - Brown"; and others). That is a separate llms.txt sync item.

## 2. "Hand-knitted" clash

### Result of the live check (2026-11-25)
- **Visible product text, 22 of 22 pages: no "hand-knitted", "hand-knit" or "handmade".** The 10 Nov edits are live. Pages now say "Knitted on a manually operated knitting machine and hand-sewn in Latvia" (items 1-3, 5-9, 10-17), "machine-knitted and hand-finished in Riga" (item 4), and the footer reads "Machine-knitted, hand-finished knitwear by Kristine in Riga, Latvia."
- **The only live "hand-knitted"/"handmade" text is in the URL slugs.** The brief says to ignore the slug, but it also shows up in "Also see / Also in" related links (the URL text, not the link label) so a crawler sees it twice. Slugs stay unchanged.

Slugs that contain the clashing word (12 "hand-knitted", 1 "handmade"):

| Item | Slug word |
|---|---|
| 2, 3, 6, 8, 9, 11, 12, 13, 14, 15, 16, 17 | `hand-knitted` (12 products) |
| 4 | `handmade` (also `sustainable`) |

Other claim words in slugs, same rule (not changed here): `sustainable` (4, 10, 15, 19... per change sheet CLAIM-CHECK 8: items 03, 04, 10, 15, 19, 20, 21 in sheet numbering) and `organic` (1, 11, 12).

### Places that could still carry the old wording (UNVERIFIED)
| Place | Status | Replacement phrase if found |
|---|---|---|
| SEO title / meta description of each product | Could not be read (WebFetch drops `<head>`). The 10 Nov crawl had "hand-knitted in Riga" in the meta description of the Merino Raglan Cardigan (item 4). The change sheet replaces it | "machine-knitted and hand-finished in Riga" |
| Image alt text (192 alts, change sheet) | Cannot be read via WebFetch. New alts in the sheet contain no clashing word | none needed |
| Product JSON-LD (`description`) | Not visible to fetch (JS-injected) | Ask owner for a Rich Results Test result |
| Etsy listing titles for the same products | Out of scope here; Etsy titles often say "hand knitted" | "machine-knitted on a manual knitting machine, hand-finished" |
| `llms.txt` repo copy, line 3 | "Pieces are knitted by hand or on a manually operated knitting machine": "by hand" clashes | "Pieces are machine-knitted on a manually operated knitting machine, then hand-finished: hand-sewn, washed and pressed before shipping." |
| `llms.txt` repo copy, line 15 | "handmade in Riga" (restricted word, only OK as the owner-approved line "Handmade in Riga by Kristine") | "wool knitwear for cooler days, machine-knitted and hand-finished in Riga" |

Replacement phrases by place (use as is):
- Short: "machine-knitted on a manual knitting machine, hand-finished"
- Long: "knitted on a manually operated knitting machine, then hand-sewn, washed and pressed"
- Never: "hand-knitted", "hand-knit", bare "handmade".

Wording drift to unify while the owner is in the editor: items 13 and 14 have three versions of the same fact ("Made on a manually operated knitting machine, then hand-sewn in Latvia", "Knitted on ... hand-sewn in Latvia", footer "hand-finished"); item 11 says "Produced on". One phrase on all pages is better for AI answers.

## 3. Owner input list

### A. Fibre % or fibre type missing on the live page
| Product | What the page says | Needed |
|---|---|---|
| Merino Wool Raglan Sweater - Dusty Pink (6) | no Material line | [FILL: fibre and %] |
| Oversized Merino Turtleneck - Dusty Pink Raglan (7) | "merino wool" | [FILL: %] |
| Distressed Oversized Wool Raglan Sweater (9) | "wool" | [FILL: fibre type and %] |
| Oversized Wool V-Neck Vest - Beige Melange (19) | "wool" | [FILL: fibre type and %] |
| Oversized Wool Raglan Sweater - Beige Melange (5) | "100% pure wool" | [FILL: confirm it means "100% pure new wool"] |

Also confirm against the yarn spec before reuse: "extra-fine" (18, 20, 21), "Italian-spun" (20, 21), "pure new wool" vs "lambswool (pure new wool)" (15-17).
Also needed: colour name for 1, 2, 3, 8, 9, 17, 18; and an add of a "how made" line to 18, 19, 20, 21 (pages say nothing about knitting method).

### B. Colour-twin groups needing a distinct first line
Same text apart from the colour word today. Drafts in the table already differ by colour and one real detail. Owner needs to supply a second photo or a real difference.
1. Side-Slit Sweater: Camel (11) and Light Grey (12). Differ only by colour. Draft uses hem detail from each page.
2. Stand-Collar Sweater: Beige (13) and Blue (14). One photo each, same text. [FILL: one real difference, if any].
3. Lambswool Raglan Crew: Brown (15), Green (16) and the colourless Classic Lambswool Crew (17). [FILL: colour of 17] to make it a third distinct page.
4. Dusty Pink raglan pair: Raglan Sweater (6) and Oversized Merino Turtleneck (7). Same colour, same cut. Differ by collar only: round ribbed neck vs ribbed turtleneck collar. Use the collar as the first-line difference.
5. Shawl-collar cardigan pair: items 1 and 2, same fibre and size range, differ by collar ("draped shawl collar" vs "draped collar and double-folded cuffs and hem") and length (83-86 cm). [FILL: colour of each]. The change sheet already has an open C-03 decision on this pair plus item 3.
6. Vest pair: Merino V-Neck (18, grey in photos) and Beige Melange (19). Different colour; fibre of 19 unknown.
7. Beanie (20) and Hat & Scarf Set (21): same fibre line, different product. Not a twin; keep.

## Owner actions
1. Send fibre and % for items 6, 7, 9, 19; confirm wording for item 5.
2. Send colour names for items 1, 2, 3, 8, 9, 17, 18.
3. Confirm "extra-fine" and "Italian-spun" against the yarn spec, or drop them.
4. Check SEO titles, meta descriptions and alts in the Squarespace editor for "hand-knitted"/"handmade" (I could not read them). Run a Rich Results Test on 5 priority pages.
5. Decide on the llms.txt line 3 and line 15 edits.
6. Decide whether to add a "how made" line to items 18-21 (and approve origin "Riga" wording, C-04).
7. Slug clash (12 "hand-knitted", 1 "handmade", sustainable/organic): needs an owner-approved redirect list before any change. Not proposed here.

## Sources
- Live product pages, 22 URLs from `llms.txt` (fetched with WebFetch on 2026-11-25).
- `/Users/eramadan/autumnandwool/.claude/worktrees/ottoman-wall-seo-ranking-f1848c/llms.txt`
- `business-os/seo-marketplace/live-2026-11-10/product-change-sheet.md` (index, rules, CLAIM-CHECK)
- `business-os/seo-marketplace/geo-2026-11-25/CONTEXT.md`
- `.claude/skills/aw-brand-voice/SKILL.md` (claim rules), `.claude/skills/aw-product-page-copy/SKILL.md`
- Not used: `products_Oct-17_10-46-00PM.csv` (too large to read, older than the 10 Nov live edits).
