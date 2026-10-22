# Etsy batch 1 and 2 prep + price-parity sheet (SEO-19, SEO-20, SEO-30), 2026-10-21. DRAFT

Author: aw-seo-marketplace. **No Etsy rewrite is proposed here** (ruling C14: not before owner decision 9). This file
only prepares the work so batch 1 can be written the day the listings export arrives (owner-inputs-wave2 rows 16–17).
Products follow the GM's provisional 5 (decision 2). If an Etsy listing for a product doesn't exist, it drops out and
the next site product with an Etsy match takes its place.

## Step 1 when the export arrives: match table
| Site product (GM rank) | Site URL | Site price (feed, 21 Oct) | Etsy listing id | Etsy title | Etsy price | Match? |
|---|---|---|---|---|---|---|
| Merino Wool Raglan Cardigan (1) | /shop/p/p/black-merino-wool-cardigan-…-1 | EUR 160 | TODO export | | | |
| Merino Wool Raglan Sweater, Dusty Pink (2) | /shop/p/p/hand-knitted-merino-wool-raglan-sweater-dusty-pink-oversized-jumper | EUR 155 | TODO | | | |
| Women's Classic Lambswool Crew Sweater (3) | /shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper | EUR 136 | TODO | | | |
| Merino Wool Hat & Scarf Set (4) | /shop/p/p/merino-wool-hat-scarf-set-…-unisex-gift | EUR 110 | TODO | | | |
| Rib-Knit Beanie (5) | /shop/p/p/merino-beanie-100-wool-…-1 | EUR 45 | TODO | | | |

## Step 2: scoring sheet (aw-etsy-listing weights; filled per listing from the export + Stats)
| Listing | Title /30 | Tags /25 | Description /20 | Attributes /15 | Photos /10 | Total | Views 30d | Visits 30d | Orders 30d |
|---|---|---|---|---|---|---|---|---|---|
| (5 rows) | | | | | | | | | |

## Step 3: tag candidates, 13 per product (each ≤ 20 characters, counted)
Draft only, to be checked against Etsy search-bar autocomplete and the current tags in the export. No competitor
brand names. Tags that repeat the category or an attribute will be swapped out once the export shows them.

| # | Raglan cardigan | Dusty Pink raglan sweater | Lambswool crew | Hat & scarf set | Rib-knit beanie |
|---|---|---|---|---|---|
| 1 | merino cardigan (15) | oversized sweater (17) | lambswool sweater (17) | hat and scarf set (17) | merino beanie (13) |
| 2 | wool cardigan women (19) | merino wool sweater (19) | grey wool sweater (17) | merino beanie scarf (19) | rib knit beanie (15) |
| 3 | raglan cardigan (15) | pink wool sweater (17) | crew neck sweater (17) | wool scarf set (14) | wool beanie (11) |
| 4 | black cardigan (14) | dusty pink jumper (17) | womens wool jumper (18) | winter gift set (15) | cuffed beanie (13) |
| 5 | brown wool cardigan (19) | raglan sweater (14) | classic knit sweater (20) | rib knit scarf (14) | unisex beanie (13) |
| 6 | minimalist knitwear (19) | oversized jumper (16) | lambswool jumper (16) | matching hat scarf (18) | winter hat women (16) |
| 7 | relaxed cardigan (16) | slouchy sweater (15) | grey knit pullover (18) | merino wool scarf (17) | winter hat men (14) |
| 8 | merino wool sweater (19) | womens knit sweater (19) | raglan sweater women (20) | unisex hat scarf (16) | fold over beanie (16) |
| 9 | button cardigan (15) | pink knit pullover (18) | relaxed fit sweater (19) | gift for her (12) | merino wool hat (15) |
| 10 | layering knit (13) | merino jumper women (19) | everyday sweater (16) | gift for him (12) | stocking stuffer (16) |
| 11 | knit cardigan women (19) | minimalist sweater (18) | minimalist knitwear (19) | black wool scarf (16) | minimalist beanie (17) |
| 12 | winter cardigan (15) | winter sweater (14) | winter wool sweater (19) | christmas gift wool (19) | ribbed hat (10) |
| 13 | gift for her wool (17) | cozy wool pullover (18) | gift for her (12) | cold weather set (16) | gift under 50 (13) |

Attributes to fill on every listing (values from the export, never guessed): primary colour, secondary colour,
material (as the label states), size, style, occasion/holiday (Christmas only for gift items), "who made it" and "what
is it" as they truly are. **"Who made it" / "made by" must match the owner's G8 evidence** (owner-inputs-wave2 row 18):
Etsy's handmade policy is strict and this is the owner's call.

## Step 4: title and description pattern (filled on the day, facts from the site feed copy)
- Title: `<garment + fibre> <fit/style> <colour> – <secondary phrase>`, ≤ 15 words, no repeated words.
- First 160 characters of the description: what it is + fibre + fit. Then measurements in cm, fibre %, care, "see size
  chart in photos", dispatch 2–5 working days, returns as on the Etsy policy page (not the site's, ruling C12).
- Claims excluded until G8: hand-knitted, handmade, made in Latvia/Riga, extra-fine, Italian-spun, RWS, mulesing-free.
- Etsy proof wording stays on Etsy; nothing from Etsy reviews moves to the site.

## SEO-20: Etsy vs site price parity sheet (filled when costs + Etsy prices exist)
CM2 comes from `python3 business-os/unit_economics.py` once the owner has confirmed costs (G1, 11 Nov). Etsy fees are
read from the owner's Etsy payment account statement, not from memory: every fee column is `TODO owner` until then.

| SKU | Site price | Site CM2 (unit_economics) | Etsy price | Etsy fees per order (listing + transaction + payment processing + offsite ads if any) | Etsy CM2 | Gap site vs Etsy | Proposal |
|---|---|---|---|---|---|---|---|
| (5 rows) | from feed | TODO G1 | TODO export | TODO owner statement | = Etsy net − same variable costs − Etsy fees | | parity / Etsy higher / keep, owner decides |

Rule for the proposal column: never propose a lower Etsy price than the site's if Etsy CM2 is below the owner's minimum
contribution per order (decision 23). Price changes are owner decisions; I only propose.

## Batch 2 (SEO-30, 15 Dec)
Same steps for the next 5 Etsy listings by Etsy visits (from the Stats screenshot), skipping any SKU not on the GREEN
list. Starts only if batch 1 went live and has 30 days of Stats by mid-December; otherwise batch 2 moves to January.
