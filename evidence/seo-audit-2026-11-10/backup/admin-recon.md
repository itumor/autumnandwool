# Squarespace admin recon, read-only (2026-11-10)

Site: www.autumnandwool.com, Squarespace site id `rose-tarpon-ld9w`, admin https://rose-tarpon-ld9w.squarespace.com/config
Method: ego-browser task space `aw-admin-recon-2026-11-10`. Only views, tab switches, panel open/close. Nothing saved, published, typed or deleted. Panels closed with CLOSE/navigation. Not checked items are marked.

## 1. Login, plan, public
- Logged in: yes. `/config/` shows "Welcome, Autumn and", site badge "Public".
- Plan: Settings > Billing (`/config/settings/billing`) > Subscriptions (`/config/settings/billing/subscriptions`). Active subscription "Website", "Renews on Nov 22, 2026 for €15.00 monthly plus applicable taxes". Upsell text shows "Email Campaigns from €8/mo".
- Site visibility: Settings > Website > Site Availability = Public (`/config/settings/website/site-availability`, label "Public").

## 2. Pages panel (`/config/pages`)
Click path: Website > Pages.
- Main Navigation: Shop (`/shop`), About (`/about`), Size Guide (`/size-guide`), Contact (`/contact`), Home (`/`).
- Not Linked: Imprint (`/imprint`), Cookie Policy (`/cookie-policy`), Redesign Preview (Hidden) (`/redesign-preview`, Enable Page = off), yandex_7685f89afd6f008a.html (Link page to `/s/yandex_7685f89afd6f008a.html`), llms.txt (Link page to `/s/llms.txt`), sitemap-alt.xml (Link page, LINK title "sitemap.xml", target `/s/sitemap-kd5g.xml`), sitemap.xml (Link page, LINK title "sitemap.txt", target `/s/sitemap.txt`), Blog (`/blog`, a blog collection, Enable Page = OFF, "Posts per Page" 20), Shipping Returns (`/shipping-returns`), FAQs (slug `faq`), Privacy Policy (`/privacy-policy`).
- Blog collection: yes (type "Blog Settings" panel, disabled). Its SEO title field reads "Blog 2".
- Add-page control: no visible "Add page" button or text in the Pages panel. Each group header has an unlabeled icon button; not clicked, so not confirmed.
- Store (Shop) settings tab set: General, Categories, SEO, Social Image, Advanced.

## 3. About page settings (Pages > Page settings About)
- General: PAGE TITLE "About", NAVIGATION TITLE "About", URL SLUG "about", QR Code off, Enable Page on, Password empty.
- SEO tab: SEO TITLE (OPTIONAL) "Our story | Autumn & Wool" (75 chars shown), SEO DESCRIPTION (OPTIONAL) "Discover Autumn & Wool, a Riga-based knitwear brand inspired by a family connection to knitting, relaxed silhouettes and everyday style." (264 chars shown), checkbox "Hide Page from Search Results" = off.
- Social Image tab: "Alternate social sharing image (optional)" file upload, empty.
- Advanced tab: marked "PREMIUM FEATURE / Access more features by upgrading to a different plan". Contains "PAGE HEADER CODE INJECTION" with the Google Tag Manager snippet (GTM-M4F6NP5J) filled in. Second textarea (footer injection, presumably) empty.
- Canonical field: not found in any tab.

## 4. Shop and category
- Shop page settings (Store Settings): General: PAGE TITLE "The collection", NAV TITLE "Shop", URL SLUG "shop", Enable Page on, TOP CATEGORY NAME "All", Filter Visibility on. SEO: SEO title "Shop wool sweaters, cardigans & accessories | Autumn & Wool" (41 chars), SEO description "Shop wool cardigans, sweaters, sweater vests, beanies and scarves at Autumn & Wool. Browse the collection and explore sizes, materials and care details." (248 chars), "Hide Page from Search Results" off.
- Categories tab (Shop > Categories): Winter Wool Gifts, Gift, Vests, Sweaters, Cardigans, Beanies, Fingerless gloves, Kids fingerless gloves, Socks, Headbands, Sets, Boot cuffs.
- Sweaters category: row options (three-dot, `data-test=category-dropdown-options`) > Edit. Edit Category panel fields: NAME "Sweaters", URL SLUG "sweaters", Enable Page on, Filter Visibility on, button "ADD TO YOUR MAIN NAVIGATION". No SEO title, description, canonical or "hide from search" field found. Options menu also has DELETE (not used).

## 5. Product: Oversized Merino Wool V-Neck Sweater Vest
Click path: Commerce > Products > Physical > row overflow (...) > Edit. Editor is a dialog (Details, Forms, Images, Inventory, Payment options, ..., Marketing).
- Product name: "Oversized Merino Wool V-Neck Sweater Vest" (Details).
- Description (rich text, Details): "Oversized V-neck vest with ribbed edging and Japanese-style shoulder shaping that moves the seam slightly back for a clean line. Easy to layer over shirts and dresses." + Material "100% extra-fine merino wool", Fit "Oversized, relaxed.", measurements "Width 59 cm, length 68 cm, armhole 30 cm", care, delivery/returns and a Layering & Fit FAQ block (text in the description).
- Price 126.00, Stock 1, SKU SQ2078364, On sale off, Unlimited off, Feature off.
- SEO and URL (Marketing > SEO and URL > EDIT): URL slug `oversized-merino-wool-v-neck-sweater-vest` (URL shown `/shop/p/...`), SEO title "Oversized Merino Wool Sweater Vest" (placeholder is product name), SEO description "Explore an oversized V-neck sweater vest with a relaxed fit. View garment measurements, layering details and care guidance at Autumn & Wool.", alternate social image empty.
- Images: 12 `<img>` elements in the editor. 10 have alt text, e.g. "Grey oversized V-neck merino wool vest layered over a black top on a mannequin", "Back of grey merino wool sweater vest showing relaxed fit and ribbed hem". 2 have empty alt (both point to IMG_3334). Alt is edited in the per-image editor, which was not opened.
- Editor not saved. Cancel did not close it, so the page was left by navigating away. Nothing was changed.

## 6. Marketing > SEO (`/config/seo`, "SEO SETTINGS" > Search appearance)
- Search Visibility Score 88% (Great). Pages with metadata 10/10. Images with alt text 0/0. AI Visibility: 0 AI credits.
- Home title format: "Handmade wool knitwear from Riga | Autumn & Wool" (placeholder "%s").
- Pages title format: "%p" (placeholder "%p — %s").
- Items title format: "%i | Autumn & Wool" (placeholder "%i — %s").
- SEO site description (home): "Discover wool cardigans, sweaters, beanies and scarves from Autumn & Wool, based in Riga, Latvia. Explore the collection, fit details and care tips." (252 chars).

## 7. Business information (Settings > Selling > Business Information, `/config/settings/selling/business-information`)
- Business name: AUTUMN AND WOOL, SIA
- Email: info@autumnandwool.com
- Phone: +37129838090
- Address: 22d Braslas iela, Rīga, 1035, Latvia
- Hours: Mon-Fri 8am - 5pm, Sat Closed, Sun Closed
- Note: /llms.txt content lists autumnandwool@gmail.com as the email, which differs from this email.

## 8. Cookie banner
- Path: Settings > Website > Cookies and Data Privacy (`/config/settings/website/cookies`). Cookie banner on. Layout "Pill". Non-essential cookies "Restricted".
- Banner style (Design > Site Styles > Accessories > Cookie Banner, `/config/site-styles/accessories/cookie-banner`): Position "Bottom". Theme/colour options shown but not changed.
- Banner text: "We use essential cookies to operate our store. With your permission, we also use analytics and other non-essential cookies. Choose “Accept all”, “Decline all” or “Manage cookies”. You can change your choice later using Cookie Preferences. Read our Privacy Policy, Cookie Policy and Imprint."
- Buttons: Accept all, Manage cookies, Decline all. Preferences label "Cookie Preferences". Saved Preferences on, Activity log included.

## 9. URL Mappings (Settings > Developer Tools > URL Mappings, `/config/settings/developer-tools/url-mappings`)
Available on this plan (page loads, no upgrade badge). Current content, verbatim:
```
/sitemap.txt -> https://static1.squarespace.com/static/6908755e4a17f81b7629f4bc/t/6921aefa64e235315d526063/1763815162973/sitemap.txt 301
/sitemap-alt.xml -> https://static1.squarespace.com/static/6908755e4a17f81b7629f4bc/t/6921adc943a7227189a1968e/1763814857084/sitemap.xml 301
/llms.txt -> https://static1.squarespace.com/static/6908755e4a17f81b7629f4bc/t/6921c67743a7227189a3f46e/1763821175900/llms.txt 301
/e410eec01fde483e97a124814d7d778a.txt -> https://static1.squarespace.com/static/6908755e4a17f81b7629f4bc/t/69231e06cbc652248dacb2f8/1763909126419/e410eec01fde483e97a124814d7d778a.txt 301
/yandex_7685f89afd6f008a.html -> https://static1.squarespace.com/static/6908755e4a17f81b7629f4bc/t/692326f08da258289eddd34e/1763911408031/yandex_7685f89afd6f008a.html 302
/shop/p/p/wool-sweater-vest-knitted-wool-vest-oversized-vest-womens-woolen-pullover-vest-top-sleeveless-wool-knit-vest-soft-v-neck-679427 -> /shop/p/p/wool-sweater-vest-knitted-wool-vest-oversized-vest-womens-woolen-pullover-vest-top-sleeveless-wool-knit-vest-soft-v-neck-vest 301
```

## 10. Custom CSS (`/config/pages/custom-css`)
- Length: 16,418 characters, 287 lines (16,438 bytes on disk).
- Saved verbatim to `evidence/seo-audit-2026-11-10/backup/custom-css-before.css` (same folder as this file).
- Contains `.sqs-widgets-confirmation-overlay`: yes. Rule `.sqs-widgets-confirmation-overlay{pointer-events:none !important;}` present (line 263), plus `.sqs-widgets-confirmation{pointer-events:none !important;}`.

## 11. Commerce
- Related Products (Commerce > Selling Tools > Related Products, `/config/commerce/selling-tools/related-products`): shows an "Upgrade" badge. Toggle "Show Related Products" exists; its on/off state was not read.
- Product Reviews (Selling Tools > Product Reviews, `/config/commerce/selling-tools/product-reviews-dashboard`): dashboard present, "No reviews yet". Requests are sent by automation 14 days after fulfilment ("Manage in Automations"). Product editor shows reviews block as "SET UP". Native reviews feature is available on this site's setup.

## 12. Crawlers (Settings > Website > Crawlers, `/config/settings/website/crawlers`)
- Block Search Engine Crawlers: OFF.
- Block Known Artificial Intelligence Crawlers: OFF.

## 13. Social links (Settings > Website > Social Links, `/config/settings/website/social-links`)
- instagram.com/autumnandwool (Visible)
- tiktok.com/@autumnandwool (Visible)
- facebook.com/AccessoriesMareshop (Visible)
- pinterest.com/mmareshop/ (Visible)
- No email link listed.

## 14. Home and About page structure (public render, read-only)
- Home (`/`) and About (`/about`) each have exactly one `sqs-block-code` block holding the main content (website-component block type). Plus several `sqs-block-html` blocks for header/footer (e.g. "FOLLOW US", "ON INSTAGRAM", "Shipping & Returns Size Guide FAQs"). So it is one main Code block per page plus HTML blocks, not a single block.
- "1,400+": Home = in the main code block ("from 1,400+ customers", "4.9★ by 1,400+ buyers"); About = in the main code block ("from 1,400+ reviews").
- "8,000": Home = in the main code block ("more than 8,000 orders", Mareshop on Etsy text); About = "8,000+" in the main code block.
- Not checked in the admin editor itself; checked on the public render.

## 15. /llms.txt
Three places:
1. SEO > LLMS.txt tab (`/config/seo`, "SEO SETTINGS" > LLMS.txt): text content in the editor, 8,038 characters, 62 lines. Starts with "# Autumn & Wool". Copy saved to `scratchpad/ego/llms-admin.txt` (not in evidence).
2. Pages panel, Not Linked: page "llms.txt" is a Link page pointing to `/s/llms.txt`.
3. URL Mappings: `/llms.txt -> https://static1.squarespace.com/.../llms.txt 301`.
- Public GET `https://www.autumnandwool.com/llms.txt` returns 200, text/plain, 8,038 characters (same length as the SEO editor content). Which of the three is served is not confirmed here.

## Other observations
- Public `/robots.txt` is the Squarespace default (AI crawler user-agents listed).
- Email mismatch: business info email info@autumnandwool.com vs llms.txt autumnandwool@gmail.com.
- Shop SEO title and About SEO title are set; Blog SEO title "Blog 2" and Blog collection disabled.
