# Pinterest plan v1: profile, 5 boards, 10 pin briefs, 2026-10-21 (DRAFT, nothing posted)

Author: aw-seo-marketplace. Task SEO-17. Pinterest is the intent-discovery channel (README §4). It is judged on
outbound clicks and GA4 sessions with source = pinterest, not on impressions or followers. Baseline: 0 sessions from
Pinterest in the 30 days to 18 Oct (zero-sales diagnosis §1).

## Gates before anything is posted
| Gate | Why | Owner / dept |
|---|---|---|
| Account decision: rename legacy `mmareshop` to Autumn & Wool and keep followers, or open a new account (decision 10/18) | The footer links to `mmareshop`; the incident log (round 6) found it live and active, so renaming keeps the audience | Owner |
| Business account + claim `autumnandwool.com` | Needed for analytics and rich pins | Owner |
| Production GREEN list (G2) | Pins promote only SKUs Production marks safe to promote | Production |
| UTM taxonomy (ruling C15, approved 31 Oct) | One naming scheme across departments | Growth owns `business-os/growth/utm-links.csv` |
| Real photos at 1000 × 1500 (2:3) | The current drafts in `campaign-assets/drafts/` are 3:4 crops of PDP photos; Pinterest favours 2:3. No AI-altered garments | Creative crops; owner approves |

## Profile (owner applies)
- Display name: **Autumn & Wool | Wool Knitwear** (keyword in the name, `aw-ecommerce-seo`).
- About (≤ 500 characters): "Wool sweaters, cardigans and sweater vests for women from a small studio in Riga, by
  Kristine. Formerly Mareshop on Etsy. Merino, lambswool and pure new wool; garment measurements on every product page."
  (No "handmade" or "made in Latvia" until G8.)
- Website: `https://www.autumnandwool.com/shop?utm_source=pinterest&utm_medium=social&utm_campaign=bio-link`
  (owner-action-pack C). Claim the domain.
- Rich pins: Squarespace PDPs already carry Product schema with price and availability (zero-sales diagnosis §2D), so
  product rich pins should work once the domain is claimed `[VERIFY with Pinterest's rich pin check after claiming]`.
- Catalog (shoppable product pins from the feed) is **not** in Q4: it waits for variant photos and a clean Merchant
  Center pass (plan Q2 2027).

## Boards (one per real search theme)
UTM per pin: `?utm_source=pinterest&utm_medium=social&utm_campaign=<board-slug>&utm_content=<pin-id>`
`[VERIFY against Growth's utm-links.csv after 31 Oct; the campaign-drafts file uses medium=organic_social, which ruling C15 replaces]`.

| # | Board title | Slug | Description (1–2 sentences) | Seeds to check in Pinterest search + Trends |
|---|---|---|---|---|
| 1 | Oversized wool sweaters | oversized-wool-sweaters | Oversized wool and merino sweaters for women: raglan sleeves, relaxed shapes and garment measurements, from a knitwear studio in Riga. | oversized wool sweater, oversized knit sweater outfit, chunky sweater |
| 2 | Merino and wool cardigans | wool-cardigans | Merino raglan cardigans and long shawl-collar wool cardigans to wear open over turtlenecks and vests. | merino cardigan outfit, long cardigan outfit, wool cardigan |
| 3 | Sweater vest outfits | sweater-vest-outfits | Oversized V-neck sweater vests layered over shirts, dresses and long sleeves. | sweater vest outfit, oversized sweater vest, knit vest layering |
| 4 | Wool beanies and winter accessories | wool-beanies | Rib-knit merino beanies in 11 colours and matching hat-and-scarf sets for cold days. | wool beanie, merino beanie, ribbed beanie |
| 5 | Wool gift ideas for her | wool-gifts-for-her | Wool gifts at different prices: a merino beanie, a hat and scarf set and sweaters. Add a handwritten gift note at checkout `[VERIFY how the note is requested]`. | gifts for her winter, wool gift ideas, cozy gift ideas |

## 10 pin briefs (week of 26 Oct, first batch)
All images = real product photos from the live PDP gallery (Squarespace CDN files named below) or the unaltered
copies in `campaign-assets/drafts/`. Crop to 1000 × 1500 without editing the garment. Text overlay optional, DM Sans,
ink `#24201C` on oat `#F2EDE6`, ≤ 6 words. Each pin links to the exact PDP.

| # | Board | Product (status) | Image source | Pin title (≤ 100) | Description (≤ 500, keyword first) | Link (before UTM) |
|---|---|---|---|---|---|---|
| P1 | 1 | Merino Striped Oversized Sweater (stock 1 on 17 Oct, check G2) | PDP image_1.jpg (`1762679338414-…`) | Oversized merino wool sweater with stripes | Oversized merino wool sweater in stripes, with Japanese-style shoulder shaping. Merino wool [CLAIM-CHECK], 59 cm wide. Measurements and fit on the product page. | /shop/p/p/hand-knitted-merino-wool-striped-sweater-oversized-jumper |
| P2 | 1 | Oversized Wool Raglan Sweater, Beige Melange (stock 1) | PDP image_1.jpg (`1762678236514-…`) | Oversized wool raglan sweater in beige melange | Oversized wool sweater in beige melange with raglan sleeves and ribbed cuffs. Pure wool [CLAIM-CHECK]; front shorter than back. Full measurements on the product page. | /shop/p/p/wool-sweater-sweater-for-women-knit-cozy-pullover-sweater-sustainable-knitwear-oversized-wool-jumper-relaxed-fit-wool-pullover-1 |
| P3 | 2 | Merino Wool Raglan Cardigan, Black (stock 2) | PDP image_1.jpg (`1762677080229-…`) | Black merino wool cardigan, relaxed raglan fit | Merino wool cardigan in black with raglan sleeves and a relaxed, slightly oversized fit. Wear it open or buttoned. Also in brown and blue. | /shop/p/p/black-merino-wool-cardigan-100-merino-wool-raglan-sweater-minimalist-knitwear-sustainable-handmade-womens-cardigan-1 |
| P4 | 2 | Merino Wool Raglan Cardigan, Brown | PDP image_10.jpg (`1762677181680-…`), **only after feed QA F5 confirms it shows the brown cardigan** | Brown merino wool cardigan for layering | Merino wool cardigan in brown, relaxed raglan fit, merino wool [CLAIM-CHECK]. Select Brown on the product page. | same as P3 |
| P5 | 2 | Long Wool Cardigan, Shawl Collar (stock 3 per size) | PDP image_1.jpg (`1762679342615-…`) or `campaign-assets/source/long-cardigan.jpg` `[VERIFY which product that file shows]` | Long wool cardigan with a shawl collar | Long wool cardigan, knee length, open front with a draped shawl collar and dropped shoulders. Pure new wool [CLAIM-CHECK], sizes S–XL. | /shop/p/p/wool-cardigan-warm-cardigan-organic-wool-wrap-winter-sweater-cardigan-women-cardigan-sweater-minimalist-style-sweater |
| P6 | 3 | Oversized Merino Wool V-Neck Sweater Vest (stock 1 after 19 Oct restock; check before posting) | `campaign-assets/drafts/pinterest-vest.jpeg` (unaltered PDP photo) | Oversized sweater vest outfit: merino V-neck over a shirt `[VERIFY the photo shows a shirt]` | Oversized sweater vest in merino wool [CLAIM-CHECK], V-neck with ribbed edges. Layer it over shirts and dresses. 59 cm wide, 68 cm long. | /shop/p/oversized-merino-wool-v-neck-sweater-vest |
| P7 | 3 | Oversized Wool V-Neck Vest, Beige Melange (stock 1; dedupe decision 20 first) | PDP image_1.jpg (`1762677841592-…`) | Beige wool sweater vest, oversized V-neck | Beige melange wool sweater vest with an oversized V-neck and ribbed finish, made to layer. 57 cm wide, 69 cm long. | /shop/p/p/wool-sweater-vest-knitted-wool-vest-oversized-vest-womens-woolen-pullover-vest-top-sleeveless-wool-knit-vest-soft-v-neck-vest |
| P8 | 4 | Rib-Knit Merino Beanie (stock 20 per colour, figure needs owner confirmation) | `campaign-assets/drafts/pinterest-beanie.jpg` | Merino wool beanie, rib knit with a fold-over cuff | Merino wool beanie in rib knit with a fold-over cuff. One size, fits 54–58 cm heads. 11 colours; only the pictured colour is shown here. | /shop/p/p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1 |
| P9 | 5 | Merino Wool Hat & Scarf Set (stock 2 per colour) | `campaign-assets/drafts/pinterest-hat-scarf-set.jpg` | Merino wool hat and scarf set, a winter gift idea | Merino wool hat and scarf set: a matching rib-knit beanie and scarf. Beanie fits 54–58 cm heads; scarf about 190 × 36 cm. Add a handwritten gift note; prices are left off the packing slip. | /shop/p/p/merino-wool-hat-scarf-set-extra-fine-rib-knit-soft-on-skin-warm-not-bulky-unisex-gift |
| P10 | 1 | Size guide (supports "wool size chart", pos 44) | One garment photo from P1 or P2 + overlay "How oversized fits" | Wool sweater size chart: how oversized knitwear fits | Wool size chart for women's knitwear: S–XL (EU 36–42, UK 8–14, US 6–12), one-size oversized pieces, and how to measure a sweater you already own. | /size-guide |

Brand-voice check: no "handmade", "made in Latvia", "sustainable", "extra-fine" or "Italian-spun"; no exclamation marks;
no hashtags beyond what Pinterest needs (none used). Gift pins (P9, board 5) make **no delivery-by-Christmas claim**
until Operations publishes the cut-off table (G5, 20 Nov).

Wave 3 fixes (GM rulings W3-6/7/8, 2026-10-21): no gift-card wording or pin (no gift card exists, A-GM-22); "Ships in
gift packaging" replaced by the allowed gift-note / no-price packing slip line (no gift wrap); merino fibre % removed,
now "merino wool [CLAIM-CHECK]" until the spec sheet clears G8 (A-GM-10). P2 "pure wool" and P5 "pure new wool" also
lose the % (A-GM-10: fibre % only after an invoice). `[CLAIM-CHECK]` is a marker; delete it before posting.

## Cadence and review
- 5–10 new pins per week from Creative's content batch (from Nov), one board each, fresh image per pin.
- Weekly note logs pins posted (by the owner) and GA4 sessions with source = pinterest.
- First review after 4 weeks (by 23 Nov, ruling C9): any non-zero sessions = KPI met for week 4; no session target
  before then.
