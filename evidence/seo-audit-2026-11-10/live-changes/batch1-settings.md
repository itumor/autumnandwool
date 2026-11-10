# Batch 1 live Squarespace settings change, 2026-11-10

Site: www.autumnandwool.com (Squarespace site rose-tarpon-ld9w). Operator: Claude subagent via ego-browser task space `aw-batch1-settings-2026-11-10-a` (space id 6). Owner approved exactly these changes. No Custom CSS, code injection, page content, products, prices, navigation, billing, domains, "Hide page from search results", or URL slugs were touched.

Method: each field's current value was read from the admin before editing. Saves were confirmed by a full page reload and read-back of the field values.

## 1. Settings > Business Information

| Field | Old value | New value | Saved | Read-back |
|---|---|---|---|---|
| Email | info@autumnandwool.com | autumnandwool@gmail.com | yes (SAVE in Settings panel header) | verified (after reload) |
| Phone number | +37129838090 | (empty) | yes | verified, empty |
| Monday | 8am - 5pm | (empty) | yes | verified, empty |
| Tuesday | 8am - 5pm | (empty) | yes | verified, empty |
| Wednesday | 8am - 5pm | (empty) | yes | verified, empty |
| Thursday | 8am - 5pm | (empty) | yes | verified, empty |
| Friday | 8am - 5pm | (empty) | yes | verified, empty |
| Saturday | Closed | (empty) | yes | verified, empty |
| Sunday | Closed | (empty) | yes | verified, empty |

Hours UI is free-text per day. Clearing every day to empty was chosen as "no hours published". The UI offered no separate "Closed only" option, so no SKIP.
Unchanged: Business Name `AUTUMN AND WOOL, SIA`, address `22d Braslas iela` / `Rīga, , 1035` / `Latvia`.

## 2. Marketing > SEO > Search appearance (/config/seo)

| Field | Old value | New value | Saved | Read-back |
|---|---|---|---|---|
| Home SEO title format | Handmade wool knitwear from Riga \| Autumn & Wool | Autumn & Wool \| Wool sweaters and cardigans from Riga | yes | verified |
| Home SEO site description | Discover wool cardigans, sweaters, beanies and scarves from Autumn & Wool, based in Riga, Latvia. Explore the collection, fit details and care tips. | Oversized sweaters, long cardigans and soft accessories in merino and wool, from our studio in Riga, Latvia. Size guide, care tips and free shipping. | yes | verified |
| Items SEO title format | %i \| Autumn & Wool | %i | yes | verified |
| Pages SEO title format | %p | %p (not touched) | n/a | n/a |

## 3. Page settings > SEO tab

| Page (/slug) | SEO title old | SEO title new | SEO description old | SEO description new | Saved | Read-back |
|---|---|---|---|---|---|---|
| About (/about) | Our story \| Autumn & Wool | About our Riga knitwear studio \| Autumn & Wool | Discover Autumn & Wool, a Riga-based knitwear brand inspired by a family connection to knitting, relaxed silhouettes and everyday style. | kept | yes | verified |
| FAQs (/faq) | FAQs \| Autumn & Wool | Wool Knitwear FAQs: Sizing, Care and Returns | Find answers to common questions about autumn and wool products, shipping, returns, and more to enhance your shopping experience. | kept | yes | verified |
| Size Guide (/size-guide) | Size guide \| Autumn & Wool | Knitwear Size Guide: Measurements and Fit | Find accurate size measurements for Autumn wool garments with our comprehensive size guide, including conversions and tips for a perfect fit. | kept | yes | verified |
| Contact (/contact) | Contact \| Autumn & Wool | Contact our Riga studio \| Autumn & Wool | Contact Autumn and Wool for inquiries on sizing, yarns, custom orders, or sharing your experience. We respond within 1-2 business days. | kept | yes | verified |
| Privacy Policy (/privacy-policy) | Privacy policy \| Autumn & Wool | kept | Explore Autumn & Wool's privacy policy outlining data collection, usage, and protection practices for customers in accordance with GDPR and privacy standards. | How Autumn & Wool collects, uses and protects your personal data when you shop with us or get in touch. | yes | verified |
| Shipping Returns (/shipping-returns) | Shipping & returns \| Autumn & Wool | kept | Learn about shipping and return policies for Autumn & Wool, including domestic and international shipping, exchanges, and refunds for handmade apparel. | Learn about shipping and return policies for Autumn & Wool, including domestic and international shipping, exchanges, and refunds for knitwear. | yes | verified |

Note: the About page SEO title was read as "Our story | Autumn & Wool" in the earlier recon. The live value matched.

## 4. Settings > Developer Tools > URL Mappings

- Before save: the editor (CodeMirror) held exactly the 6 original lines, matching admin-recon.md section 9.
- Added as line 7: `/shop/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper -> /shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper 301`
- Saved: yes (SAVE in Settings panel header). Read-back after reload: 7 lines, original 6 unchanged, new line present.

## Public verification (curl -sS -A "Mozilla/5.0")

Run after the admin saves. Note: the first request to /shipping-returns returned 503 once; the retry returned 200 and the new text.

- `GET /shop/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper`: `HTTP/2 301`, `location: http://www.autumnandwool.com/shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper`. The Location scheme is http, not https. Following it with -L ends at `https://www.autumnandwool.com/shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper` with 200.
- Home `<title>`: `Autumn &amp; Wool | Wool sweaters and cardigans from Riga`
- Home meta description: `Oversized sweaters, long cardigans and soft accessories in merino and wool, from our studio in Riga, Latvia. Size guide, care tips and free shipping.`
- /about `<title>`: `About our Riga knitwear studio | Autumn &amp; Wool`
- /faq `<title>`: `Wool Knitwear FAQs: Sizing, Care and Returns`
- /size-guide `<title>`: `Knitwear Size Guide: Measurements and Fit`
- /contact `<title>`: `Contact our Riga studio | Autumn &amp; Wool`
- /privacy-policy meta description: `How Autumn &amp; Wool collects, uses and protects your personal data when you shop with us or get in touch.`
- /shipping-returns meta description (itemprop/og): `Learn about shipping and return policies for Autumn &amp; Wool, including domestic and international shipping, exchanges, and refunds for knitwear.`
- Product /shop/p/oversized-merino-wool-v-neck-sweater-vest: `<title>Oversized Merino Wool Sweater Vest</title>`. Product JSON-LD `"name"`: `Oversized Merino Wool Sweater Vest`. The " | Autumn & Wool" suffix is gone from both the title and the JSON-LD name.
- Homepage JSON-LD:
  - Organization: `email` = `autumnandwool@gmail.com`; `telephone` = `""` (empty string present); no openingHours.
  - LocalBusiness: `name` = `AUTUMN AND WOOL, SIA`; no email, telephone or openingHours keys.
  - WebSite: name `Autumn & Wool`.
  - `openingHours` occurrences in homepage HTML: 0.
- HTTP status: `/` 200, `/shop` 200.
