# Page change sheet, live site, 2026-11-10

Status: PROPOSAL for owner application. Nothing on the live site has been changed. Covers non-product pages only: /shop, the seven /shop/<category> pages, the home page, About, FAQ, Contact, Size guide, Privacy, Cookie policy, Shipping and returns, the site-wide footer, and the two review claims on Home and About. Product pages are in `product-change-sheet.md`.

Sources: `evidence/seo-audit-2026-11-10/crawl/html/*.html` (live HTML as crawled 2026-11-10) and `crawl/pages.tsv` (current titles and metas, lengths as crawled). The brief's "live About/Imprint page" rule was applied to the category CLAIM-CHECK items.

Rules applied: (1) no visible value says "hand-knit", "hand knit" or "handmade" (owner decision 1); (2) no SEO title carries a brand suffix (brief; OWNER: check whether Squarespace adds a suffix itself); (3) no URL or slug changes; (4) every new value is plain British English, and no claim is added that the page does not already make, except where a claim is replaced by a supported one (listed).

---

## A. /shop (collection page)

- **URL:** https://www.autumnandwool.com/shop
- **H1:** none today → `Shop wool sweaters, cardigans and accessories` (set in the collection title settings; see QA V-02 if the template does not render an H1).
- **SEO title:** `Shop wool sweaters, cardigans & accessories | Autumn & Wool` (59) → `Shop wool sweaters, cardigans & accessories` (43)
- **SEO description:** keep (152). `Shop wool cardigans, sweaters, sweater vests, beanies and scarves at Autumn & Wool. Browse the collection and explore sizes, materials and care details.`

---

## B. Category pages (seven)

Each category page currently has no H1 and no meta description, and its canonical points to /shop (O-01, platform limit; the category pages need their own content, SEO-35). Owner go-ahead needed. The H1 is set in the collection title field. Titles and metas below have no brand suffix.

| # | URL | Title: current → new (chars) | Meta: new (chars) | H1: new | Claim-check status |
|---|---|---|---|---|---|
| B1 | https://www.autumnandwool.com/shop/beanies--hats | `Beanies — Shop wool sweaters, cardigans & accessories \| Autumn & Wool` (69) → `Unisex Wool Beanies` (19) | `Unisex rib-knit beanies with a fold-over cuff and smooth front panel. One size. Care details and sizing on each product page.` (125) | `Beanies and hats` | "Merino" dropped from the title: the About page does not name merino for beanies (it names merino, lambswool and pure new wool for the range). The beanie product copy does say merino, so it can return once the owner approves. |
| B2 | https://www.autumnandwool.com/shop/cardigans | `Cardigans — Shop wool sweaters, cardigans & accessories \| Autumn & Wool` (71) → `Wool Cardigans, Long and Open-Front` (35) | `Long and open-front wool cardigans with shawl collars and side slits, from our Riga studio. Garment measurements on each product page.` (134) | `Cardigans` | "Knitted in Riga" replaced by "from our Riga studio": About says "a small knitwear studio in Riga, Latvia". |
| B3 | https://www.autumnandwool.com/shop/gift | `Gift — Shop wool sweaters, cardigans & accessories \| Autumn & Wool` (66) → `Gift Cards and Wool Gift Ideas` (30) | `Digital gift card for wool knitwear. Sent by email and redeemable at checkout on autumnandwool.com.` (99) | `Gift cards` | None. |
| B4 | https://www.autumnandwool.com/shop/sets | `Sets — Shop wool sweaters, cardigans & accessories \| Autumn & Wool` (66) → `Merino Hat and Scarf Sets` (25) | `Matching merino hat and scarf set with a rib-knit beanie. Soft on the skin and warm without bulk. Colours and care on the product page.` (135) | `Hat and scarf sets` | "Soft on the skin and warm without bulk" is on the 17 product page (kept). |
| B5 | https://www.autumnandwool.com/shop/sweaters | `Sweaters — Shop wool sweaters, cardigans & accessories \| Autumn & Wool` (70) → `Wool and Merino Sweaters` (24) | `Oversized and relaxed wool and merino sweaters from our Riga studio. Raglan, side-slit, stand-collar and turtleneck styles.` (123) | `Sweaters` | "Knitted in Riga" replaced by "from our Riga studio" (About). Intro copy of 80–150 words (C-02) is not written in this sheet. |
| B6 | https://www.autumnandwool.com/shop/vests | `Vests — Shop wool sweaters, cardigans & accessories \| Autumn & Wool` (67) → `Oversized Wool Sweater Vests` (28) | `Oversized merino and wool sweater vests with a V-neck and ribbed finish. Measurements on each product page.` (107) | `Sweater vests` | "Most come in one size" dropped: it is in the size guide, not in About or Imprint. |
| B7 | https://www.autumnandwool.com/shop/winter-wool-gifts | `Winter Wool Gifts — Shop wool sweaters, cardigans & accessories \| Autumn & Wool` (79) → `Winter Wool Gifts` (17) | `Winter wool gifts from Autumn & Wool: a merino hat and scarf set, a rib-knit beanie and a digital gift card. Free shipping, 14-day returns.` (139) | `Winter wool gifts` | "Sent with tracking" dropped: it is on the shipping page only, not About or Imprint. |

Collection grid images: the crawl shows "Handmade" in the grid markup of /shop/cardigans (and a few other category pages), taken from product names or product photo alts. After the product alt changes, check the grid tile alt text on each category page in the editor, and set any that still say "handmade" or "hand-knitted". OWNER.

---

## C. Home page (`/`)

- **URL:** https://www.autumnandwool.com/
- **SEO title:** `Handmade wool knitwear from Riga | Autumn & Wool` (48) → `Wool sweaters and cardigans from Riga` (37)
- **SEO description:** `Discover wool cardigans, sweaters, beanies and scarves from Autumn & Wool, based in Riga, Latvia. Explore the collection, fit details and care tips.` (148) → `Oversized sweaters, long cardigans and soft accessories in merino and wool, from our studio in Riga, Latvia. Size guide, care tips and free shipping.` (149)
- **H1:** keep `Wool knitwear for cooler days`.
- **Og and schema name:** the og:title and the schema name follow the SEO title in Squarespace. Check after saving.

### C1. Hero rating (desktop badge and mobile trust line)

Current HTML (`<div class="aw-rate">`): `<big>4.9</big><div><s>★★★★★</s>from 1,400+ customers</div>`
- Replace the text `from 1,400+ customers` → `from 1,400+ reviews on Etsy`
- Result reads: **4.9 from 1,400+ reviews on Etsy**

### C2. Trust strip (four tiles)

- Tile 1. Current: `<b>Handmade in Riga</b><span>Manual machine knit, hand-sewn</span>` → New: `<b>Machine-knitted, hand-finished</b><span>Manual machine knit, hand-sewn in Riga</span>`
- Tile 4. Current: `<span>4.9★ by 1,400+ buyers</span>` → New: `<span>4.9 from 1,400+ reviews on Etsy</span>`

### C3. Story paragraph (Our story block)

- Current: `For 15 years you may have known us as Mareshop on Etsy — more than 8,000 orders and a 4.9-star rating from 1,400+ reviews.`
- New: `For 15 years you may have known us as Mareshop on Etsy: 8,000+ orders on Etsy and 4.9 from 1,400+ reviews on Etsy.`

### C4. Category tile images (four, empty alt today)

| Tile | File (CDN) | Current alt | New alt |
|---|---|---|---|
| Sweaters | …/1762678236514-ISG5HGL1TIN2JE3M6EIP/image_1.jpg | (empty) | Wool sweaters, go to category |
| Cardigans | …/1762679342615-6S4AVCS6KE3TOH9YO18X/image_1.jpg | (empty) | Wool cardigans, go to category |
| Vests | …/62180209-cc63-4af8-bbc1-ae0a19636fba/IMG_3336.JPEG | (empty) | Merino and wool sweater vests, go to category |
| Hats & scarves | …/1762678311409-26KFX7XKIYQW97QLAA9Q/image_1.jpg | (empty) | Hats and scarves, go to category |

### C5. Instagram photos (five tiles, one shared alt today: "Autumn &amp; Wool on Instagram")

| # | File | New alt |
|---|---|---|
| 1 | IMG_2369.JPEG | Autumn & Wool knitwear, Instagram photo 1 |
| 2 | IMG_3022.JPEG | Knitwear in progress in the Riga studio, Instagram photo 2 |
| 3 | IMG_2929.JPEG | Finished wool sweater detail, Instagram photo 3 |
| 4 | IMG_2166.JPEG | Autumn & Wool knitwear, Instagram photo 4 |
| 5 | IMG_2373.JPEG | Autumn & Wool knitwear, Instagram photo 5 |

Neutral descriptions only. OWNER: if you want a more specific alt, describe what the photo shows.

### C6. Home H1 (none change), hero image

- The hero image already has a descriptive alt ("Model wearing an oversized Autumn & Wool knit sweater"). Keep.

---

## D. About (`/about`)

- **URL:** https://www.autumnandwool.com/about
- **SEO title:** `Our story | Autumn & Wool` (25) → `About our Riga knitwear studio` (31)
- **SEO description:** keep (136).
- **H1:** keep `Every stitch tells a story of patience and purpose`.

### D1. Stats block (reviews claim)

Current HTML: `<div><b>15</b>years as Mareshop on Etsy</div><div><b>8,000+</b>orders shipped worldwide</div><div><b>4.9★</b>from 1,400+ reviews</div><div><b>100%</b>made in Latvia</div>`

- Tile 2. `<b>8,000+</b>orders shipped worldwide` → `<b>8,000+</b>orders on Etsy`
- Tile 3. `<b>4.9★</b>from 1,400+ reviews` → `<b>4.9</b>from 1,400+ reviews on Etsy`
- Tile 4. `<b>100%</b>made in Latvia`: CLAIM-CHECK, not changed. See below.

### D2. "How each piece is made" block

- Step 2 current: `<span><b>Knitted</b> by hand or on a manually operated machine</span>` → New: `<span><b>Knitted</b> on a manual knitting machine</span>` (owner decision 1; "by hand" is removed).
- Step 3 keep: `<b>Hand-sewn</b> and finished, seam by seam`.
- Intro sentence (CLAIM-CHECK, not changed): `Nothing here comes off a factory line. Every garment is made in Latvia from merino, lambswool or pure new wool.`

### D3. Review claim, About page (exact replacement, for the About page only)

- Current (HTML): `<b>4.9★</b>from 1,400+ reviews`
- New: `<b>4.9</b>from 1,400+ reviews on Etsy`

---

## E. Reviews claim on Home and About: exact replacement sentences

Owner rule: the review claim must read **4.9 from 1,400+ reviews on Etsy**, with the word Etsy. "8,000+ orders" must become "8,000+ orders on Etsy". The Etsy shop URL must be quoted from the HTML, not invented.

| Page | Location | Current sentence (quoted from HTML) | New sentence |
|---|---|---|---|
| Home | Hero rating | `4.9` + `from 1,400+ customers` | `4.9` + `from 1,400+ reviews on Etsy` |
| Home | Trust strip, tile 4 | `4.9★ by 1,400+ buyers` | `4.9 from 1,400+ reviews on Etsy` |
| Home | Story paragraph | `For 15 years you may have known us as Mareshop on Etsy — more than 8,000 orders and a 4.9-star rating from 1,400+ reviews.` | `For 15 years you may have known us as Mareshop on Etsy: 8,000+ orders on Etsy and 4.9 from 1,400+ reviews on Etsy.` |
| About | Stats tile 2 | `8,000+` / `orders shipped worldwide` | `8,000+` / `orders on Etsy` |
| About | Stats tile 3 | `4.9★` / `from 1,400+ reviews` | `4.9` / `from 1,400+ reviews on Etsy` |

**Etsy shop link:** `ETSY URL NOT FOUND`. The site's `sameAs` list (Home schema) contains only Instagram (`https://www.instagram.com/autumnandwool`), TikTok (`https://www.tiktok.com/@autumnandwool`), Facebook (`https://www.facebook.com/AccessoriesMareshop`) and Pinterest (`https://www.pinterest.com/mmareshop/`). No `etsy.com` URL appears in any page of the crawl. Owner: if the review claim should link to the shop, add the Etsy shop URL to the social links. This sheet does not invent one.

No review text, star rating schema or aggregate rating is added. The 4.9 and 1,400+ figures are marketplace history, labelled as Etsy.

---

## F. Other information pages

### F1. FAQ (`/faq`)

- **SEO title:** `FAQs | Autumn & Wool` (20) → `Wool Knitwear FAQs: Sizing, Care and Returns` (45)
- **SEO description:** keep (129).
- **H1:** `Questions, answered` → `Wool knitwear FAQs: orders, shipping, returns and care` (55)

### F2. Size guide (`/size-guide`)

- **SEO title:** `Size guide | Autumn & Wool` (26) → `Knitwear Size Guide: Measurements and Fit` (42)
- **SEO description:** keep (141). **H1:** keep `Find your fit`.

### F3. Contact (`/contact`)

- **SEO title:** `Contact | Autumn & Wool` (23) → `Contact our Riga studio` (23)
- **SEO description:** keep (135). **H1:** keep `Let's talk wool`.

### F4. Privacy policy (`/privacy-policy`)

- **SEO title:** keep `Privacy policy | Autumn & Wool` → `Privacy policy` (suffix rule; 14)
- **SEO description:** current raw text is 158 characters, over the 155 limit (`pages.tsv` shows only "Explore Autumn & Wool" because the crawl cut the text at an apostrophe). Replace the whole field → `How Autumn & Wool collects, uses and protects your personal data when you shop with us or get in touch.` (103)
- **Body sentence (handmade and sustainable claims; both removed):**
  - Current: `Autumn & Wool is a handmade knitwear brand based in Riga, Latvia, creating sustainable garments from 100% natural yarns.`
  - New: `Autumn & Wool is a knitwear brand based in Riga, Latvia.`
  - Removed on purpose: "handmade" (owner decision 1), "sustainable" (banned claim, owner removed it on 18 Oct), "100% natural yarns" (no support on the page; fibre is stated per product instead).

### F5. Cookie policy (`/cookie-policy`)

- **H1:** none today → `Cookie policy` (13)
- **SEO title:** `Cookie Policy | Autumn & Wool` → `Cookie policy` (suffix rule)
- **SEO description:** keep (128).

### F6. Shipping and returns (`/shipping-returns`)

- **SEO description (151) → (143):** `Learn about shipping and return policies for Autumn & Wool, including domestic and international shipping, exchanges, and refunds for knitwear.`
- **Body sentence (handmade, removed):** `Each piece is handmade, so slight variations in texture or colour are normal and part of its character.` → `Each piece is machine-knitted and hand-finished, so slight variations in texture or colour are normal and part of its character.`
- **CLAIM-CHECK, not changed:** `Every order is packed by hand in our Riga studio and sent with tracking.` This is not on About or Imprint. Owner to confirm, then keep or edit.
- **SEO title:** keep `Shipping & returns` → `Shipping & returns` (suffix rule).

### F7. Imprint (`/imprint`)

- No change proposed. Title and meta are already fine. H1 keep `Imprint`.

---

## G. Site-wide footer (every page)

- Current (HTML, footer block on every page): `Handmade knitwear by Kristine in Riga, Latvia. Formerly Mareshop on Etsy.`
- New: `Machine-knitted and hand-finished knitwear by Kristine in Riga, Latvia. Formerly Mareshop on Etsy.`
- Change once in the footer block. Owner applies. This removes "Handmade" from every page.

---

## H. Out of scope for this sheet (noted so they are not missed)

- `/llms.txt` contains "handmade" (SEO-46 replaces it with the corrected draft; check that the replacement has no "handmade").
- `/home` duplicates `/` (SEO-41: hide /home from search engines, remove it from the sitemap).
- Category intro copy (80–150 words, C-02) and the category canonical (O-01, platform) are not written here.
- Collection grid alt text (see section B note) comes from product photo alts and needs a check after the product changes.
- Slugs on the 22 product pages and on categories (contain "hand-knitted", "sustainable", "organic") are not changed (no redirect plan).

---

## CLAIM-CHECK (page copy kept, owner to confirm)

1. "100% made in Latvia" (About stats tile 4, D1) and "Every garment is made in Latvia from merino, lambswool or pure new wool." (About, D2). Origin is open (C-04). Kept as written.
2. "Nothing here comes off a factory line." (About, D2). A process claim, kept as written.
3. "Every order is packed by hand in our Riga studio and sent with tracking." (Shipping and returns, F6). Not on About or Imprint.
4. "Free shipping" and "14-day returns" on the home and category metas. Taken from product pages. Confirm they stay true.
5. "This gift card never expires." is on the product page (product sheet, 01).

## Self-check

- **Lengths:** all new titles and metas were counted character by character (spaces included), with no tool. Longest new meta: 149 (home), 139 (winter gifts), 143 (shipping and returns), 103 (privacy). Longest new title: 45 (FAQ). Limits: title 60, meta 155. All pass.
- **Banned words in new values:** no new value in this sheet contains "hand-knit", "hand knit" or "handmade". The "current" quotes contain them on purpose. The footer and privacy body sentences are replaced in full (sections G and F4).
- **URLs:** every URL here is from `pages.tsv` (category, info and shop pages) or from the crawl. Etsy: none found, written as ETSY URL NOT FOUND.
- **Coverage:** /shop H1 and metas (A); the seven category pages (B1–B7); home (C); About (D); FAQ, Size guide, Contact, Privacy, Cookie policy, Shipping and returns (F1–F6); footer (G); reviews claim on Home and About (E).
