# QA Report: autumnandwool.com (redesign, Squarespace live site)

Tested: 2026-10-18, Chrome (one tab, read-only except cart actions). Desktop viewport 1512x728. Phone check done at 390px inside a same-origin iframe, because resizing the window did not change the page viewport. Reference: `.dc.html` design files in the scratchpad project folder.

## 1. Summary

| Area | Pass | Fail | Notes |
|---|---|---|---|
| Header/footer/internal links (home, shop, product, cart, about, contact, size-guide, shipping, faq, privacy) | all | 0 | Every internal link found on the tested pages returned HTTP 200 (fetch from page, redirects followed). External social links not opened. |
| Home bestseller/category targets | 2 | 2 | Two cards go to category pages, and the "Hats & scarves" tile goes to `/shop/sets`. |
| Size guide cm/inches toggle | 2 | 0 | Both directions work; conversions spot-checked and correct. |
| FAQ accordions | 12 | 0 | All 12 open and close. |
| FAQ / Privacy "on this page" anchors | 15 | 0 | All targets exist. |
| Contact form fields | 4 | 0 | Name, email, topic, message accept input. Not submitted. |
| Product add to cart, header count | 1 | 0 | Count went 0 to 1. |
| Product variant selection | 1 | 1 | Brown selected, but gallery still shows black cardigan and title stays "Black ...". |
| Cart qty +/-, subtotal, remove, empty state | 4 | 0 | Qty 2 = EUR 320. Cart ended empty. |
| Checkout button | 1 | 0 | Reached `/checkout` (Secure Checkout) showing cart line EUR 160. Nothing entered. |
| Sitemap URLs | 36 | 0 (1 unverified) | One product URL failed to fetch from page context. Not confirmed as a 404. |
| Title / meta description present on all tested pages | 11 | 0 | Titles have quality issues (see section 4). |
| H1 exactly one per page | 7 | 2 | Shop has none. Home has two (second is a footer wordmark). |
| Console errors | — | 0 JS errors | Six Squarespace YUI "NOT loaded" warnings on home. |
| Horizontal scroll at 390px | 6 | 0 | Checked on home, shop, product, faq, contact, size-guide, about. |

## 2. Differences from design

Known and accepted (not counted): native Squarespace header, announcement bar and footer; Shop/Product/Cart are native pages restyled with CSS.

| Page | Sev | Difference | Fix |
|---|---|---|---|
| Home | High | "Long Wool Cardigan" card links to `/shop/cardigans` (category), not the product. "Merino Wool Raglan Sweater" links to `/shop/sweaters`. | Point cards at product URLs, e.g. `/shop/p/...`, in the native block links. |
| Home | Med | "Hats & scarves" tile links to `/shop/sets`. `/shop/beanies--hats` is the hats category. | Link tile to `/shop/beanies--hats` or rename to "Sets". |
| Home | Med | Header nav has Shop, About, Contact. Design also has "Size guide" in header. | Add Size guide to native header nav (Squarespace Navigation settings). |
| Home | Low | Second H1 "Autumn and wool" in a native HTML block (footer area). | Change that block's tag to a `<div>` or `<p>`. |
| Home | Low | Two Instagram blocks: custom "@AUTUMNANDWOOL / Worn on cooler days" grid plus native "Follow us on Instagram" block, plus footer and header icons. | Remove one of the two Instagram CTAs. |
| Shop | Med | Design has "The collection" heading. Live Shop page has no H1 (only an H2 "Shop"). | Add a visible H1 "The collection" in the page header block. |
| Shop | Low | Category "Beanies" has 1 product, "Sets" 1, "Winter Wool Gifts" 3. | Fill or hide thin categories. |
| Product (vest) | High/Med | Product H1 "Oversized Merino Wool V-Neck Sweater Vest" but `<title>` is "Oversized Merino Wool Sweater Vest". | Align title and H1 names. |
| Product (cardigan) | High | Choosing "Brown" keeps the black gallery image and the title stays "Black Merino Wool Raglan Cardigan". Cart line also reads as the black product. | Per-variant images in the Squarespace variant config, or split Brown and Black into separate products. |
| Product | Med | Design shows size selector (S/M/L etc.) and "Size guide" link. Live product pages show colour only, no size selector. | Add size variant or a visible size guide link on product pages, per design. |
| Product | Low | Design heading "Pairs well with". Live "You Might Also Like". | Change heading text. |
| Cart | Low | Design heading "Your cart". Live "Shopping Cart". Live cart also uses native checkout. | Optional copy change. |
| Size guide | Low | Title "Find Your Perfect Fit – Shop Now". | Drop "Shop Now" from title. |

## 3. End-to-end results

| Step | Target | Result |
|---|---|---|
| Header | Shop `/shop`, About `/about`, Contact `/contact`, Home `/`, cart `/cart` | 200 each |
| Footer | Shipping `/shipping-returns`, Size Guide `/size-guide`, FAQs `/faq`, About, Contact, Privacy `/privacy-policy` | 200 each |
| Footer | Instagram, TikTok, Facebook, Pinterest | Links present. Not opened. Facebook and Pinterest point to legacy "AccessoriesMareshop" / "mmareshop" accounts. |
| Home hero | "Shop the collection" `/shop`, "Our story" `/about` | 200 |
| Home | Bestseller cards (4) | Vest and Oversized Raglan go to product pages (200). Long Wool Cardigan to `/shop/cardigans`. Merino Raglan to `/shop/sweaters`. Category targets return 200 but are not product pages. |
| Home | Category tiles (4) | `/shop/sweaters`, `/shop/cardigans`, `/shop/vests`, `/shop/sets` (200). Label mismatch on "Hats & scarves". |
| Home | "Meet the maker", "View all pieces" | `/about`, `/shop` (200) |
| Home | Instagram tiles (5) | All link to `https://www.instagram.com/autumnandwool` (external). Not opened. |
| Home | Newsletter form | Present. Not submitted. |
| Shop filters | All, Winter Wool Gifts, Vests, Sweaters, Cardigans, Beanies, Sets | Paths `/shop/winter-wool-gifts`, `/shop/vests`, `/shop/sweaters`, `/shop/cardigans`, `/shop/beanies--hats`, `/shop/sets` all 200. Product counts: sweaters 13, cardigans 4, vests 2, winter gifts 3, beanies 1, sets 1. |
| Shop | Product links (about 22 unique) | Spot-checked 10 entries in output: all 200. Output was truncated, so not every product URL was confirmed. |
| Size guide | cm to inches to cm | Values change both ways. Example S chest 84–90 cm = 33–35.5 in. |
| Size guide | "Email Kristine" | `mailto:autumnandwool@gmail.com`. Not clicked. |
| FAQ | 12 accordions | Open and close all work. |
| FAQ | Anchors (#orders, #shipping, #returns, #care, #sizing, #contact) | All targets present. |
| FAQ | "Contact us" | `/contact` (200) |
| Shipping | "FAQs", "Contact us", mailto | `/faq`, `/contact`, mailto. |
| Privacy | 9 anchors plus mailto | All targets present. |
| Contact | Fields | Name, email, Topic select, Order, Message accept input. Not submitted. Form has two actions (`mailto:` and native POST to `/contact`). Which one runs on submit is unverified. |
| Product | Variant "Brown" | Selectable. Image does not change (see section 2). |
| Product | Add to cart | Works. Header count 0 to 1 (all four cart links updated). |
| Cart | Qty + then - | Qty 2 = EUR 320.00, back to 1 = EUR 160.00. |
| Cart | Checkout | Opens `/checkout` ("Autumn & Wool | Secure Checkout"). Summary EUR 160.00, Shipping EUR 0.00, Tax EUR 0.00. Email field empty. Stopped here. |
| Cart | Remove | Cart empty: "You have nothing in your shopping cart." Count 0. Verified. |

## 4. Technical and accessibility findings

| Sev | Finding | Evidence |
|---|---|---|
| Med | Shop page has no H1. | `h1` count 0, only `h2` "Shop". |
| Med | Home has two H1s. Second is a footer wordmark "Autumn and wool". | `h1` list on `/`. |
| Med | Product gallery `alt` text is file names ("IMG_3336.JPEG") and shop tiles have empty `alt`. | DOM check on vest product page; shop `alt=""` on about 200 images. |
| Med | Footer text links and social icons below 24px tap target on phone. | At 390px: footer links 22px tall; social icons 20–25px; cart icon 39x25. |
| Med | Stored product photos on shop page have "ChatGPT Image …" file names. Check image provenance and licensing. | 7 DOM images on shop page. Only file names seen; content not verified. |
| Low | Six Squarespace YUI "NOT loaded" warnings in console on home. No JS exceptions. | `read_console_messages` on `/`. |
| Low | Page weight: shop initial load about 1.7 MB across 13 images (lazy loads rest). Product page has 83 `<img>` tags. | Performance entries. Full byte count not measured for all pages. |
| Low | Lazy images show `naturalWidth 0` until scrolled. Not broken; confirmed on home after scroll. | Home IG tiles and product page. |
| Low | Focus indicator: 2px solid outline on header link (spot check). | Computed style. Tab order not fully walked. |
| Info | Contrast: hero body text about 6.3:1, H1 about 13.9:1 (both pass AA). Footer contrast not measured reliably by script. | Computed styles. |
| Info | `lang="en-US"` on all pages checked. Site content is English. Set to `en` if it matches content; it's fine as is. | `documentElement.lang`. |

## 5. Content and UX findings

| Sev | Finding | Fix |
|---|---|---|
| High | Return conditions contradict. Shipping page: "Unworn, unused items". FAQ: "unworn, unwashed items". | Pick one wording and use it on both pages. |
| High | Brown variant shows black product image and black title. | See section 2. |
| Med | Privacy policy says changes are "posted with the revised date", but no date appears on the page. | Add "Last updated: <date>". |
| Med | Privacy policy names Google Analytics, but no Google Analytics request was seen on the home page load. Cookie banner present in footer. | Verify which analytics actually run and align the policy. Unverified. |
| Med | Legacy social handles. Facebook "AccessoriesMareshop", Pinterest "mmareshop". "Formerly Mareshop on Etsy" appears in footer and on product pages. | Confirm these handles are intended, or update them to Autumn & Wool accounts. |
| Med | Product page "4.9 from 1,400+ reviews on Etsy (as Mareshop)". | Confirm that review claim and its source are current. |
| Med | Duplicate announcement and trust claims. Announcement bar "Free shipping · 14-day returns · Handmade in Riga"; trust row repeats free shipping and 14-day returns. | Keep one place for these claims. |
| Med | Two Instagram CTA blocks plus footer and header icons. | Keep one. |
| Med | Product title vs H1 mismatch (vest). Variant image mismatch (cardigan). | See section 2. |
| Low | Title tags carry duplicate brand suffix: "… | Autumn & Wool — Autumn & Wool" on Shop; "Shipping Returns | …" on shipping (H1 "Shipping & returns"); marketing copy in titles ("Explore FAQs & Shop with Confidence", "Learn More & Protect Your Data", "Get in Touch Today"). | Shorten titles and remove duplicate suffix. |
| Low | Sitemap lists `/home` (duplicate of `/`) and `/shop/gift`. About 35 product URLs use legacy Etsy-style slugs such as `/shop/p/p/...-679510`. One sitemap product URL failed to fetch from the page (unverified). Home card link uses `/shop/p/p/wool-sweater-sweater-for-women-…`. | Remove `/home` and stale product entries from sitemap; use clean slugs. |
| Low | Cart page `<title>` is generic "Autumn & Wool". | Set "Your cart | Autumn & Wool". |
| Low | Shop product names are long SEO strings ("Merino Wool Raglan Sweater — Dusty Pink Oversized Jumper"). | Shorten names. |
| Low | Product measurements are inconsistent: the vest lists cm only, the cardigan lists cm and inches. | Use one format or show both on every product. |

Prioritised recommendations:
1. Fix variant image/title for Brown/Black cardigan, and product H1/title mismatch.
2. Make home cards and "Hats & scarves" tile go to correct product/category.
3. Reconcile return conditions (unused vs unwashed) across Shipping and FAQ.
4. Add Shop H1, remove second home H1, fix product image alt text.
5. Add Size guide to header nav and product size selector per design.
6. Add "Last updated" date to privacy policy; verify analytics claim.
7. Remove duplicate Instagram block; keep one place for shipping/returns claims.
8. Clean titles, sitemap (`/home`, `/shop/gift`, stale slugs), footer tap targets.

## 6. What was NOT tested

- Real purchase (intentionally stopped at checkout). Address, shipping method, payment not tested.
- Contact form submission (not sent). mailto behaviour not triggered. Which form action runs on submit is unverified.
- External links (Instagram, TikTok, Facebook, Pinterest, Etsy) not opened.
- Newsletter sign-up not submitted.
- Full keyboard tab order on every page (only one focus spot check).
- Full contrast audit (footer, announcement bar, product text) not measured numerically.
- Page weight in bytes for every page; lazy images not fully loaded on product page.
- Real phone device, iOS Safari, and other browsers. Phone layout checked only at 390px inside an iframe on desktop Chrome.
- Product pages beyond vest and cardigan. Gift card product not opened.
- Product size selector absence confirmed only on the two products checked.
- Account/login links (`href="#"`, shown on FAQ and Privacy) not investigated.
- Two shop product URLs in the sitemap not fully checked; one fetch failed and is unverified.
- Design vs live pixel-level comparison not done; differences above are from copy, structure and labels in the `.dc.html` files.
