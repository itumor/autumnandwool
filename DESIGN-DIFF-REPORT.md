# Autumn & Wool: live site vs design, fidelity audit

Audited 2026-10-19, read-only. Live: https://www.autumnandwool.com/ . Design ground truth: the ten `*.dc.html` files in the artifact `project/` folder (read in full). The rendered canvas URL needs a claude.ai login (page returned "Sign in to view this page"), so it was NOT used; the `.dc.html` source is the only design reference.

## Method and limits (read first)

- Browser: ego-browser, task space 12 "design audit autumnandwool 20261019" (finished, no pages kept). Cart test: one item added then removed; `.sqs-cart-quantity` verified back to 0.
- Default viewport was 1272x864 (screenshots at that size). Design is a 1440 canvas, so computed-style measurements were taken in a same-origin iframe at 1440 (effective content width 1425 because of the 15px scrollbar; 1360px container therefore starts at x=65) and at 390 (effective 375).
- Measured = computed styles / rects from `getComputedStyle`. Seen = screenshots in `/Users/eramadan/ego/design-audit-20261019/` (`s-<page>-top|mid|bot.png`, `s390-*`). Items marked UNVERIFIED were not measured.
- Design has NO mobile comps. 390px was checked only for: horizontal overflow (none on any of 10 pages), wordmark, stacking.
- Not verified at all: hover/focus states, accordion open/close, cm/inch toggle, shop filter behaviour, Quick View, newsletter submit, checkout, design image identity (design images are `/_blob/...` ids that cannot be mapped to live Squarespace CDN images), privacy section-number colour, table borders on size guide.
- Match % are my estimates from the measured/seen items (share of design elements that match), not a tool output.
- Severity: High = missing/broken section or function, or clearly visible brand/layout break. Med = visible layout/copy/style deviation. Low = small style delta.
- Global items (header, footer, h2 letter-spacing, breadcrumbs) are listed once in "Global" and NOT counted in the per-page counts, except where a page differs from the others.

## Summary

| Page | Est. match | High | Med | Low |
|---|---|---|---|---|
| / (Home) | ~75% | 1 | 2 | 5 |
| /shop | ~30% | 1 | 5 | 3 |
| /shop/p/oversized-merino-wool-v-neck-sweater-vest | ~40% | 0 | 6 | 5 |
| /cart (empty + filled) | ~25% | 1 | 4 | 3 |
| /about | ~88% | 0 | 1 | 2 |
| /contact | ~68% | 1 | 2 | 3 |
| /size-guide | ~93% | 0 | 0 | 3 |
| /shipping-returns | ~92% | 0 | 0 | 3 |
| /faq | ~93% | 0 | 0 | 3 |
| /privacy-policy | ~45% | 0 | 2 | 2 |
| Global header / wordmark | ~65% | 0 | 1 | 4 |
| Global footer (separate section below) | ~10% | 3 | 3 | 3 |

Things that matched exactly (measured): wordmark font/size/colours; Home hero h1 100.8px, 56px/48px h2s, 18px lead copy, button height 52 / radius 999 / ink fill, trust-strip grid, 4-col bestseller grid with 4:5 images and 32/24 gaps, category cards 3:4 radius 4 opacity .78, story section (sand bg, padding 104, 3:4 images with 64px offset), Instagram 5-up grid 250px squares gap 12; all FAQ questions and answers (12 of 12 exact); About, Size guide, Shipping copy (word-for-word except one card); colours (oat body bg rgb(242,237,230), sand rgb(231,224,214), rust rgb(142,59,31), ink rgb(36,32,28)); Instrument Serif and DM Sans both load.

## Logo (exactly what renders)

- Renders on all 10 pages at 1440 (seen in a header strip of every page) and at 390 (seen on home, product, cart, contact, shipping, faq, privacy; DOM confirmed on all 10; /shop, /about, /size-guide 390 top shots were scrolled so those three are DOM-confirmed only).
- It is a CSS wordmark, not an image: inside `.header-title-logo a[href="/"]` (desktop) and `.header-mobile-logo a[href="/"]` (mobile). `::before` on the `<a>` = "Autumn"; `::before` on the inner `<picture>` = "&" ; `::after` on the `<picture>` = "Wool". The old logo `<picture>` still exists in the DOM (sources point at the ChatGPT png) but draws nothing.
- Computed: Instrument Serif, 34px, line-height 34px, letter-spacing -0.34px (= design -0.01em), colour #24201C; "&" italic, colour rgb(142,59,31) = #8E3B1F. This matches the design spec (34px, italic rust "&"). Links to `/` (`href="/"`).
- Deviations: (1) link box is 183x20 although the glyphs are 34px tall, so the clickable area is only 20px high (Low; fix `header .header-title-logo a, header .header-mobile-logo a {min-height:34px; align-items:center}` in Custom CSS). (2) Text is generated content, so it cannot be selected/copied and a screen reader gets it only if the engine exposes pseudo content (ego snapshot did list "Autumn", "&", "Wool"); Low.
- Centred on the viewport (x 538..721 at 1272 wide, centre 629 vs viewport centre 628); design places it centre-ish between nav and icons, effectively the same.

## Global: header

| Element | Design | Live (measured) | Sev | Fix and where |
|---|---|---|---|---|
| Right-hand icons | Search, Account, Cart (44x44 buttons, 20px stroke icons, no count) | Instagram, TikTok, Facebook, Pinterest icons + cart icon with count "0"; no search, no account | Med | Squarespace: Pages > Header > Elements: turn off Social links, turn on Account, add Search (Design > Site header). Cart count: Custom CSS `.header-actions .cart-style-icon{...}` or `.sqs-cart-quantity{display:none}` |
| Nav item style | 14px / 500 / letter-spacing 0.02em, gap 28px | 13px / 400 / normal, gap about 17-20px (Shop x38 w31, About x86) | Low | Custom CSS: `.header-nav-item a{font-size:14px;font-weight:500;letter-spacing:.02em}` and `.header-nav-list{gap:28px}` |
| Label | "Size guide" | "Size Guide" | Low | Squarespace: Pages > edit nav title to "Size guide" |
| Header alignment | content in 1360px container, padding 32 (nav starts x=65 at 1440) | nav starts x=43, cart ends x=1382 (full-width, 40px side padding); page content starts x=65 | Low | Custom CSS `#header .header-inner{max-width:1360px;margin:0 auto;padding:22px 32px}` |
| Header height | padding 22px | 92px block incl. wrapper | Low | covered by the rule above |
| Announcement bar | n/a | accepted difference | - | - |
| h2 letter-spacing (all pages) | none | -0.02em (e.g. Bestsellers -1.12px at 56px) | Low | Custom CSS `.aw-w h2{letter-spacing:0}` (the `.aw-*` page code blocks) |
| Active nav | underline on current page | underline present on Shop/About/Contact/Size Guide pages | OK | - |

## Footer vs design

Design has two footers: the Home page has a light-oat 4-column footer; every other design page has a compact one-line footer (copyright + nav links). Live uses one native dark footer on every page.

| Element | Design | Live (measured/seen) | Sev | Fix and where |
|---|---|---|---|---|
| Background / border | oat #F2EDE6, 1px #CFC6BA top border, ink text | background rgb(36,32,28) (ink), light text, links underlined, no top border | High | Squarespace: Pages > Footer > edit section: set colour theme to light/oat, or replace the footer content with a Code Block holding the design markup (Main.dc.html lines 138-165) and hide the native newsletter block with Custom CSS |
| Newsletter "Sign Up" button | (design newsletter is a separate dark card on Home, "Subscribe" button oat on ink) | Button bg rgb(26,26,26) with text rgb(36,32,28): text is essentially invisible (contrast about 1.1:1) on every page | High | Custom CSS: `footer .newsletter-form button, footer .newsletter-form button span{background:#F2EDE6!important;color:#24201C!important}` (or invert when footer is light) |
| Email input | pill (radius 999), 52px, transparent with 1px #6B625A border | square (radius 0), 54px, white bg, grey placeholder "Email Address" | Med | Custom CSS on `footer .newsletter-form input` |
| Columns (Home design) | 4: brand wordmark 30px + tagline "Wool knitwear for cooler days. Handmade in Riga, Latvia." / Shop (All pieces, Sweaters & cardigans, Hats & scarves, Gift cards) / Help (Shipping & returns, Size guide, FAQs, Privacy policy) / Contact (email, address, Instagram, TikTok, Pinterest, Facebook) | Link columns: [Shipping & Returns, Size Guide, FAQs], [About, Contact, Privacy Policy], [Instagram, Tiktok, Facebook, Pinterest, Company Registration]; newsletter text + form at right; tagline "Handmade knitwear by Kristine in Riga, Latvia. Formerly Mareshop on Etsy." bottom-left | High | Footer section rebuild as above. Missing: footer wordmark, whole Shop column, email link, address block. Extra: newsletter, About/Contact links, Company Registration link (lursoft.lv), "Formerly Mareshop on Etsy" |
| Bottom bar | 12px #5E554D: "© 2026 SIA Autumn & Wool · Reg. no. 40203644965" left, "Prices in EUR" right | 11.3px uppercase light: "© 2026 AUTUMN AND WOOL, SIA · Reg. no. ... · Braslas iela 22d, Rīga, LV-1035, Latvia · autumnandwool@gmail.com"; no "Prices in EUR" | Med | edit footer bottom text / code block |
| Divider line | 1px #CFC6BA above bottom bar, clear of text | horizontal rule at y=3842 runs through the copyright line (text y 3828-3846) on every page | Med | Custom CSS: add `margin-top:16px` to the copyright block or move the `hr` |
| Extra band above footer | none | "FOLLOW US / Autumn and wool / ON INSTAGRAM" strip on every page (h2 57.9px on Home in light text; h4 19.9px on About) | Med | Squarespace: delete that footer/page section or hide with Custom CSS; confirm which Fluid Engine section `fe-690875624a17f81b7629f719` / the 88-98px strip is |
| Extra photo bands | none | full-bleed photo above the footer on /shop (539px tall sweater close-up) and /about (435px, IMG_0976 with overlay quote "Every stitch tells a story of patience and purpose."); not seen on other pages | Med | remove those page sections in Squarespace (Shop page and About page last section) |
| Link labels | "Shipping & returns", "FAQs", "Privacy policy", "TikTok" | "Shipping & Returns", "FAQs", "Privacy Policy", "Tiktok" | Low | edit footer link titles |
| Cookie banner | none | native "Cookie Preferences" tab fixed bottom-left over content and footer on every page | Low | Squarespace: Settings > Cookies & visitor data (cannot change in read-only audit; flagged only) |
| Footer text size | 14px links, 13px/14px body | 14.7px DM Sans | Low | Custom CSS `footer p, footer a{font-size:14px}` |

## Per page

### / Home (est. ~75%)

| Element | Design | Live | Sev | Fix and where |
|---|---|---|---|---|
| Newsletter card ("New knits, first" / "Hear about new colours and small-batch drops before anyone else." / pill input + Subscribe) between Instagram section and footer | dark #24201C card, radius 4, padding 64/48, h2 44px serif | absent; native footer newsletter text reads "Get new knits, restocks and gift ideas from Riga. A few emails a season, no spam." | High | add Code Block section after the Instagram grid with Main.dc.html lines 124-136 (or restyle the Squarespace newsletter block into this card) |
| Trust strip icons | 24px rust SVG icon left of each of 4 items, gap 14px, item text starts after icon | 0 SVGs (`.aw-t` contains only `<b>` + `<span>`); text starts 24px from left edge | Med | Code Block: add `<svg>` from Main.dc.html lines 58-61 inside each `.aw-t` (Home page code block) |
| Story paragraph 2 | "...1,400+ reviews. Autumn & Wool is the same studio, the same care — now with its own home." | ends at "...1,400+ reviews." (last sentence missing) | Med | Home code block: append the missing sentence |
| Bestseller names/subs | "Oversized Raglan Sweater", "Merino Raglan Sweater", "Merino V-Neck Sweater Vest" + sub "Oversized fit" | "Oversized Wool Raglan Sweater", "Merino Wool Raglan Sweater", "Oversized Merino V-Neck Vest" + sub "Sweater vest" (Cardigan card matches) | Low | Home code block text (live names follow product titles; decide which is right) |
| Bestseller card links | `Product.dc.html` | 3 of 4 point to `/shop/p/p/...` (double `p`); all return 200 | Low | change hrefs to `/shop/p/<slug>` |
| Trust title weight | 600 | 700 (`<b>`) | Low | CSS `.aw-t b{font-weight:600}` |
| "View all pieces" underline | border-bottom 1px, padding-bottom 2px | border 1px, padding-bottom 0 | Low | CSS `.aw-head a{padding-bottom:2px}` |
| Instagram tile images | design blobs (gift card, beanie, dusty pink, knit-in-progress, hat set) | IMG_2369, IMG_3022, IMG_2929, IMG_2166, IMG_2373 (different pictures) | Low | UNVERIFIED which is intended; links all go to instagram.com/autumnandwool (OK) |
| Hats & scarves category image | hat+scarf set photo | a Squarespace image_1.jpg (visually hat+scarf, looks right) | Low | seen, not id-verified |

Matched: eyebrow 13px/600/0.14em rust uppercase; hero 640px image with 4.9 badge; story, category and Instagram grids and spacing (hero to trust gap 72px, section padding 104px, story margin-top 120px).

### /shop (est. ~30%)

| Element | Design | Live | Sev | Fix and where |
|---|---|---|---|---|
| Page header | breadcrumb "Home / Shop", h1 "The collection" clamp(56,6vw,88) = 86px, intro "Small-batch wool and merino knitwear, machine-knitted by hand and sewn in Riga.", "{n} pieces" right | none visible on desktop; the only title is an `h2.nested-category-title.hidden-up-md` that is `display:none` on desktop; no h1 on the page | High | Squarespace: edit Shop page, add a section above the product list with a Code Block (Shop.dc.html lines 37-46) |
| Filter | pill buttons: All, Sweaters, Cardigans, Vests, Hats & scarves, Gift cards (44px, radius 999, ink fill when active, 1px #A89D90 otherwise) + bottom border #CFC6BA | centred text list separated by pipes: All, Winter Wool Gifts, Vests, Sweaters, Cardigans, Beanies, Sets (active bold 14.5px) | Med | Custom CSS on `.product-list-filter-list`/nested category nav; rename/reorder Squarespace categories |
| Grid | auto-fill minmax(280px), gap 48px 24px = 4 columns in a 1296px container | 3 columns of 427px, gap 28.8px (row) / 18px, container x=43 w=1339 | Med | Custom CSS `.product-list-container{grid-template-columns:repeat(4,1fr)!important;gap:48px 24px;max-width:1360px;padding:0 32px}` |
| Card meta | name 16px/500 left + price right on one row, then 13px grey sub-line; image radius 4 | name 15px/500 above, price 14px #5E554D below left; no sub-line; long SEO names ("Oversized Wool Raglan Sweater — Beige Melange"); price "€126.00" / "FROM €25.00" vs "€126" / "from €25"; image radius 0 | Med | Custom CSS flex row for `.product-list-item-meta`; shorten product titles in Squarespace (or hide via `.product-list-item-title` rewrite); `img{border-radius:4px}` |
| Tags | pill tags "Bestseller" (Cardigan), "Gift idea" (hat set), 12px/600 uppercase on oat | none | Low | Squarespace product badges or Custom CSS pseudo-elements |
| Bottom band | sand panel, 3 columns: "Not sure of your size?" + "Open the size guide", "Looking for a gift?" + "Gift cards from €25", "Questions?" + email; 28px serif headings | plain text row with top border: "Free shipping to eligible destinations" / "Returns information" / "Replies within 1–2 business days" | Med | replace with Code Block from Shop.dc.html lines 74-80 |
| Extra photo band | none | 539px full-bleed photo between that row and the footer | Med | delete the section |
| Catalogue | 7 sample products | 22 products (Gift Card renders last, same as design) | Info | not an error; design shows only a sample |
| Quick View label | none | each card has a "QUICK VIEW" element (45 `[class*=quick-view]` nodes, not visible at rest) | Low | UNVERIFIED on hover; hide with CSS if unwanted |

### /shop/p/oversized-merino-wool-v-neck-sweater-vest (est. ~40%; design shows a cardigan, so only structure/style compared)

| Element | Design | Live | Sev | Fix and where |
|---|---|---|---|---|
| Breadcrumb | "Home / Shop / Cardigans" 13px #5E554D | "The collection › <product name>" 14.7px ink | Med | Squarespace: Product page > breadcrumbs setting / Custom CSS font-size+colour |
| Gallery | main image 4:5; thumbnails in a vertical 84x104 column on the left, 2px ink border on active | main 736x982 (3:4, ratio 0.749); 10 thumbnails in a horizontal row of 50px under the image; prev/next arrows | Med | Squarespace: Product gallery layout "Thumbnails left" (Pages > Product > Gallery); CSS for aspect-ratio 4/5 |
| Eyebrow + subtitle | eyebrow "Handmade in Riga" (13px rust uppercase), subtitle line, price row with "★★★★★ 4.9 shop rating" | no eyebrow/subtitle; price alone | Med | product excerpt/ code block or CSS pseudo-element |
| Price | 26px DM Sans | 26px Instrument Serif, letter-spacing 0.26px | Low | CSS `.product-price{font-family:'DM Sans'}` |
| h1 | 56px, letter-spacing -0.01em | 56px, letter-spacing -1.12px (-0.02em), wraps to 2 lines | Low | CSS letter-spacing -0.01em |
| Info chips | two sand tiles "Free shipping to LV, US & more" and "14-day returns" | one light box: "★ 4.9 from 1,400+ reviews on Etsy (as Mareshop) / ✓ Free shipping / ✓ Dispatched from Riga in 2–5 working days / ✓ 14-day returns" | Med | live copy is richer; restyle into two sand tiles or accept |
| Size selector | S/M/L/XL pill-squares 56x48, ink fill when selected | none (this product has no variants: `select`/variant nodes = 0) | Med | correct for one-size items; UNVERIFIED for multi-size products |
| Add to cart button | 56px, 16px/600, label "Add to cart — size M" | 55px, 13px/600, letter-spacing 0.65px, label "Add To Cart" | Low | Custom CSS `.sqs-add-to-cart-button{font-size:16px;letter-spacing:0;min-height:56px}` |
| Details | 3 accordions: Materials & care (open), Fit & measurements, Shipping & returns (1px dividers, 18px padding, 600 summary) | flat paragraphs with plain-text headings "MEASUREMENTS (garment)", "CARE", "DELIVERY & RETURNS"; `details` count = 0 | Med | rebuild the description as Squarespace Accordion/Code Block (Product.dc.html lines 80-93) |
| Body text | 16px/15px #4A423B | 14.7px #24201C | Low | CSS `.product-excerpt p{font-size:16px;color:#4A423B}` |
| "Pairs well with" | 48px, 4 cards (hat set, beanie, vest, raglan), name 16px/500 + price on one row | h2 57.9px with +0.58px letter-spacing, 3 cards (hat set, beanie, Gift Card), 3 columns 427px, "QUICK VIEW" labels, name above price | Med | Custom CSS for `.product-list-header h2` 48px; change related-products setting to 4 items |
| Size guide link | "Size guide" link beside the Size legend | absent (no variant legend) | Low | add link in description |
| Image radius | 4px | 0px | Low | CSS |

### /cart (est. ~25%)

| Element | Design | Live | Sev | Fix and where |
|---|---|---|---|---|
| Filled-cart summary | sand panel (radius 4, padding 32): "Summary" 32px serif, Subtotal, Shipping "Free" (green #3F5B2E/600), note "To Latvia, the US & destinations shown at checkout", Total 20px/600, "EU VAT included. Duties may apply outside the EU.", optional gift note textarea, Checkout 56px pill, "Ships from Rīga in 2–5 working days", "14-day returns · details" | only "Subtotal €126.00" (22px) and a Checkout button (386x56); no panel, no Shipping/Total/VAT/ship notes (a `textarea` exists on the page but no gift-note label seen) | High | Custom CSS to box `.cart-summary` + add `::before/::after` text or Code Block injection |
| Heading | h1 "Your cart" clamp(48,5vw,72) = 72px | h2 "Shopping Cart" 44px, letter-spacing -0.88px | Med | CSS font-size 72px; Squarespace cart title text cannot be renamed in UI (use `content`) |
| Empty state | sand panel: "Your cart is empty" 36px serif, "Find something warm for cooler days.", ink pill "Shop the collection" 52px/500 | plain "You have nothing in your shopping cart." (16px) + "Continue Shopping" outline button, 2px border, 18px/700, 67px tall | Med | CSS to restyle `.cart-container .empty-cart` + button 52px/500/1px border |
| Line item image | 132px wide, 4:5, radius 4 | 132x132 square, radius 0 | Med | CSS `.cart-row-product-image{aspect-ratio:4/5;border-radius:4px}` |
| Line item text | name 18px/600 + total, grey variant line "Size M · €145.00 each" | name 16px/500, no variant line, price right | Low | Squarespace limitation |
| Qty / remove | bordered pill with −/+ 44px, "Remove" underlined text | borderless −/+ icons, X icon button 36px | Low | CSS |
| Checkout button | 16px/600 | 13px/600 | Low | CSS |
| Line borders | 1px #CFC6BA top/bottom | present (seen) | OK | - |

### /about (est. ~88%)

| Element | Design | Live | Sev | Fix and where |
|---|---|---|---|---|
| Copy | as design | identical (automated diff: only the announcement bar and design footer string differ) | OK | - |
| Sections/grids | hero 2-col, 21:9 banner (ratio 2.335 live vs 2.333), numbers grid 4-col, 2-col process + staggered images, dark promise band, CTA | all match, h1 93.6px (6.5vw) | OK | - |
| Extra band + photo | none | "autumn and wool / FOLLOW US / ON INSTAGRAM" strip and 435px photo with overlay quote before the footer | Med | see Footer section |
| h2 letter-spacing | none | -0.02em | Low | global |
| Banner image | grey knit on mannequin | alt "Grey Autumn & Wool knit sweater on a mannequin" (matches intent; id not verified) | Low | UNVERIFIED |

### /contact (est. ~68%)

| Element | Design | Live | Sev | Fix and where |
|---|---|---|---|---|
| Submit button | "Send message" 56px ink pill | `<button type="submit">Send message</button>` exists but computed `display:none` (0x0): the form has no visible send control | High | Custom CSS `form.aw-f button[type="submit"]{display:block!important}`; find the rule that hides it (Squarespace form-button reset) |
| Breadcrumb vs eyebrow | breadcrumb "Home / Contact", no eyebrow | eyebrow "CONTACT" (13px/600 uppercase rust); no breadcrumb | Med | Contact code block |
| Info-row icons | 22px rust SVG icons (mail, Instagram, pin, building) beside each row | none (labels only) | Med | add SVGs from Contact.dc.html lines 45-48 |
| Extras | none | row of links "Instagram TikTok Pinterest Facebook" under the info list; paragraph "Questions? Email us at autumnandwool@gmail.com — we reply within 1–2 business days." inside the form box | Low | remove |
| Form fields | 50px inputs, radius 4, border #A89D90, bg oat | match (inputs 50px, radius 4, 1px rgb(168,157,144), bg oat); textarea 179px; panel sand, padding 40 | OK | - |
| h1/h2 | 86px/36px | 86.4px/36px (letter-spacing -0.02em vs design -0.02em h1 OK, h2 differs) | Low | global |
| Copy | as design | identical except the missing button label and "Thank you!" state (mailto accepted) | OK | - |

### /size-guide (est. ~93%)

| Element | Design | Live | Sev | Fix and where |
|---|---|---|---|---|
| Breadcrumb | "Home / Size guide" | absent | Low | add to code block |
| "Between sizes?" box width | inside 1296px column | spans 1360px (x=33..1393) while all other sections sit at x=65..1361 | Low | CSS `.aw-last{padding-left:32px;padding-right:32px}` (has `padding:88px 0 104px`) |
| h2 letter-spacing | none | -0.02em | Low | global |

All copy (steps, table cm values, fit types, tip) matches. Table header (ink bg, oat text, 600), size cells Instrument Serif 28px, 4 steps grid measured OK. Table borders and the inches toggle behaviour UNVERIFIED.

### /shipping-returns (est. ~92%)

| Element | Design | Live | Sev | Fix and where |
|---|---|---|---|---|
| Breadcrumb | "Home / Shipping & returns" | absent | Low | add |
| Exchange card text | "Swap for another size or colour, subject to stock." | "Place a new order for the size or colour you prefer, return the original within 14 days, and we refund the first purchase." | Low | edit the code block copy (decide which is right) |
| h2 letter-spacing | none | -0.02em | Low | global |

Glance cards (dark Free card, three sand cards, 48px serif values), 4-step returns grid, 3-column non-returnable block and closing sand box (aligned x=65 w=1296) match.

### /faq (est. ~93%)

| Element | Design | Live | Sev | Fix and where |
|---|---|---|---|---|
| Breadcrumb | "Home / FAQs" | absent | Low | add |
| Closing dark "Still wondering?" box | 1296px | 1360px (x=33) | Low | CSS padding as size guide |
| h2 letter-spacing | none | -0.02em | Low | global |

All 6 topic links, all 12 questions and 12 answers match the design exactly (compared string-by-string). Details open/close behaviour UNVERIFIED.

### /privacy-policy (est. ~45%)

| Element | Design | Live | Sev | Fix and where |
|---|---|---|---|---|
| Copy | short policy: intro "Autumn & Wool is a handmade knitwear studio in Riga, Latvia. This page explains what personal data we collect, why, and the choices you have."; section titles "What we collect", "How we use it"; one-paragraph sections | rewritten longer policy: intro "At Autumn & Wool, we respect your privacy...", titles "What information we collect", "How we use your information"; bullet lists; names Stripe, Squarespace Analytics, Google Analytics | Med | decide whether live text is the final legal text and update the design/source of truth; no code change if live is right |
| "Last updated" | "Last updated: [DATE]" under h1 | no date at all | Med | add real date under the h1 |
| Breadcrumb | "Home / Privacy policy" | present (this is the only live page that has one) | OK | - |
| Layout | TOC left (240px) + article max 760px, sections h2 34px, closing sand box | measured: article x=601 w=760, h2 34px, closing sand box 760px | OK | - |
| Placeholders | "[UPDATE WHEN THE NEW PLATFORM IS CHOSEN]" | removed (good) | OK | - |
| Number colour in h2 / TOC eyebrow | rust | UNVERIFIED | - | - |
| Contact box text | "Autumn & Wool, Rīga, Latvia" | "Riga" | Low | edit |

## Breadcrumbs (cross-page)

Design: breadcrumb on Shop, Product, Contact, Size guide, Shipping, FAQs, Privacy (not Home/About/Cart). Live: only Privacy has "Home / Privacy policy"; Product has "The collection › name"; Shop, Contact, Size guide, Shipping, FAQ have none. Fix: add `<div class="aw-bc">Home / ...</div>` (13px, #5E554D) to each page's code block.

## Top 10 fixes (priority order)

1. Footer "Sign Up" button is invisible on every page (rgb(36,32,28) text on rgb(26,26,26)). Custom CSS on `footer .newsletter-form button`. Live conversion blocker.
2. Contact "Send message" button is `display:none`. Custom CSS `form.aw-f button[type=submit]{display:block!important}` (or find the hiding rule).
3. Replace the native dark footer with the design footer (light oat, 4 columns, bottom bar with "Prices in EUR"): Squarespace Pages > Footer, code block + hide native newsletter/Instagram strip; fix the divider line through the copyright.
4. Add the Shop page header (breadcrumb, h1 "The collection", intro, count): section above the product list, code block from Shop.dc.html.
5. Add the missing Home dark newsletter card ("New knits, first") after the Instagram grid.
6. Cart: build the Summary panel (Shipping Free, Total, VAT/ship notes, gift note) and the empty-state panel (Custom CSS plus injected text), plus 72px "Your cart" heading and 4:5 line-item image.
7. Remove the extra bands above the footer: "FOLLOW US ON INSTAGRAM" strip (all pages) and the full-bleed photos on /shop (539px) and /about (435px).
8. Header right side: replace the four social icons with Search / Account / Cart per design (Squarespace header settings), and align the header to the 1360px container; set nav to 14px/500/28px gap and "Size guide" label.
9. Shop grid and filters: 4 columns, 48px/24px gaps, pill filters with design categories, name+price row, shortened titles/sub-lines, tags, 4px image radius.
10. Product page: left vertical thumbnails and 4:5 main image, accordions for details, two sand info tiles, eyebrow "Handmade in Riga", 16px/56px add-to-cart, "Pairs well with" at 48px with 4 items.

Next tier: Home trust-strip icons and the truncated story paragraph; breadcrumbs on 6 pages; Size guide / FAQ closing boxes width 1296; privacy "Last updated" date; h2 letter-spacing global fix; clickable height of the wordmark link.
