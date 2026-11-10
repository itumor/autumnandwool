# SEO fixes applied and re-measured — autumnandwool.com — 2026-11-10

Follows [2026-11-10-seo-audit-and-action-plan.md](2026-11-10-seo-audit-and-action-plan.md). Changes were made on the live Squarespace site the same day, then the site was re-crawled, tested end to end, and re-audited by fresh claude-seo passes against the morning findings.

**SEO Health Score: 56 → 61.** Four areas went up, two went down.

## Scores before and after

| Area | Weight | Morning | After | Change | Detail |
|---|---|---|---|---|---|
| Technical SEO | 22% | 70 | 65 | −5 | [after/findings/technical.md](../../evidence/seo-audit-2026-11-10/after/findings/technical.md) |
| Content quality | 23% | 55 | 61 | +6 | [after/findings/content-onpage.md](../../evidence/seo-audit-2026-11-10/after/findings/content-onpage.md) |
| On-page SEO | 20% | 40 | 56 | +16 | same file |
| Schema / structured data | 10% | 45 | 46 | +1 | [after/findings/schema-ecommerce.md](../../evidence/seo-audit-2026-11-10/after/findings/schema-ecommerce.md) |
| Performance | 10% | 61 | 57 | −4 | [after/pagespeed-after-quiet.md](../../evidence/seo-audit-2026-11-10/after/pagespeed-after-quiet.md) |
| AI search readiness | 10% | 64 | 78 | +14 | [after/findings/geo-agentic.md](../../evidence/seo-audit-2026-11-10/after/findings/geo-agentic.md) |
| Images | 5% | 62 | 66 | +4 | [after/findings/images-visual.md](../../evidence/seo-audit-2026-11-10/after/findings/images-visual.md) |
| **Total** | | **56** | **61** | **+5** | |

E-commerce readiness (reported separately, not in the total): 60 → 51.

How to read these:
- The "after" audit scores were taken **before** the last fix-up batch. That batch repaired three of the newly found defects (broken pictures on four landing pages, a redirect that hopped through `http://`, product names not matching structured-data names). By the re-auditors' own point rules that is worth about +2 on Technical and +5 on E-commerce; Images was not re-scored after the picture fix. I have not re-run the audit a third time, so the table shows the measured values.
- Scores are specialist judgement on a rubric, each run by a different fresh agent. Differences of a few points are within judgement noise; On-page and AI search are the two clear gains.
- Performance is my 2:1 mobile/desktop blend of PageSpeed medians (three runs each, quiet site).

## PageSpeed before and after (lab data; Google still has no real-user data)

| Page | Device | Performance morning → now (three runs) | LCP morning → now | Verdict |
|---|---|---|---|---|
| Home | Mobile | 44 → 65 (71, 56, 65) | 11.8 s → 6.0 s | Improved |
| Home | Desktop | 76 → 74 (82, 70, 74) | 1.0 s → 1.0 s | Same |
| /shop | Mobile | 52 → 38 (38, 37, 61) | 13.2 s → 15.3 s | Worse |
| /shop | Desktop | 66 → 69 (78, 69, 46) | 3.1 s → 3.0 s | Same |
| Product (V-neck vest) | Mobile | 72 → 52 (37, 52, 60) | 3.9 s → 14.5 s | Worse |
| Product (V-neck vest) | Desktop | 72 → 62 (76, 62, 58) | 2.4 s → 2.7 s | Slightly worse |
| /wool-sweaters (new) | Mobile | 55 (52, 67, 55) | 11.3 s (4.2 s on one run) | No baseline |
| /wool-sweaters (new) | Desktop | 90 (91, 73, 90) | 1.0 s | No baseline |

SEO score is 100 and Accessibility 96 on every run, as before.

- **Home got faster** because the hero picture is now requested at a smaller size with priority, and the other home pictures at 750 px instead of 1000 px.
- **/shop and the product page measured slower, and I have not found the cause.** Nothing changed today targets how those pages load pictures or scripts (the edits there were text, alt text and SEO fields). The morning figure was a single run and single runs swing widely (the same page gave 37 and 60 within minutes), but the product page's mobile LCP was 14.3–14.7 s on all three runs against 3.9 s in the morning, which is too consistent to dismiss as noise. Treat this as open.

### Follow-up: why /shop and the product page measured slower (investigated same evening)

The pages did not load slower. The LCP figure changed because of which element Lighthouse picked and how it models Squarespace's JavaScript. Evidence: [after/lcp-element-comparison.md](../../evidence/seo-audit-2026-11-10/after/lcp-element-comparison.md) (read from the saved PageSpeed reports) plus two local Lighthouse runs.

- **Product page:** in the 14:22 report the LCP element was the `<h1>` product title (text in the HTML, 3.9 s). In the 17:19 report and every run since, it is a product gallery picture. Squarespace loads gallery pictures with JavaScript (`data-src`, not in the initial HTML), so the slow-4G simulation places it at 13–21 s. Unthrottled, the same picture paints at 0.9 s. First paint (2.6 s), Speed Index (5.7 → 6.0 s) and page weight (3,449 KiB) are unchanged.
- **/shop:** the LCP element is the cookie banner text in both the 14:21 and 17:18 reports. The banner is drawn by JavaScript, so its time moves with script load on each run (13.2 s, then 15–17 s). Unthrottled it paints at 0.8 s.
- **What triggered the switch on the product page is not proven.** The only edit to that gallery picture was its alt text, which does not affect LCP. Squarespace released new versions of its own scripts between the two crawls (component bundles and `performance-*.js` have new file names). All 22 products were edited, so there is no untouched product to compare against.
- **What this means:** the morning 3.9 s was the flattering reading; 13–15 s is what Lighthouse reports whenever a JS-loaded picture or the cookie banner is the largest element, which is also why Home and /shop were already at 11.8 s and 13.2 s in the morning. Neither can be changed on this plan (no script access, pictures and banner are loaded by the platform). Real-user data from Google does not exist yet for this site.

## What was changed on the live site

| Batch | Change | Verified |
|---|---|---|
| 1 Settings | Home title now leads with the brand; new home description; product titles no longer carry " \| Autumn & Wool" (which also removed it from product structured data); SEO titles for About, FAQ, Size guide, Contact; descriptions for Privacy and Shipping; Business Information: Gmail address, no phone, no opening hours; old single-`/p/` product URL redirects (301, straight to https). | Read back in admin and on the public pages |
| 2 New pages | Five landing pages with their own URL, H1, intro and product grid: `/wool-sweaters`, `/wool-cardigans`, `/wool-sweater-vests`, `/wool-hats-and-scarves`, `/wool-gifts` (gift guide, no cut-off dates). Four guides: `/how-to-wash-a-wool-sweater`, `/merino-vs-lambswool`, `/oversized-fit-guide`, `/how-to-choose-a-wool-cardigan`. All nine are in the sitemap. | 200, one H1 each, all grid pictures load |
| 3 Wording | Reviews claim now reads "4.9 from 1,400+ reviews on Etsy" with a link to the Etsy shop, on Home and About; "8,000+ orders on Etsy". "Handmade" replaced by "machine-knitted, hand-finished" on Home, About, FAQ, Shipping, the footer and the header bar ("Made in Riga"). Home category tiles link to the new landing pages. | Old strings gone, new present |
| 4 Products | All 22: SEO title and description; 15 renamed (URLs unchanged); colour-specific first paragraph on six colour twins; "More …" links to the landing page and two related products; 192 image alt texts. Price, stock, variants untouched. | Each product checked publicly after saving |
| 5 Speed and llms.txt | Home pictures smaller, hero prioritised, five distinct Instagram alts; `llms.txt` replaced (no internal notes, no "since 2011", new pages listed, making wording corrected). | Public file and page checked |
| 6 Fix-ups | Repaired broken picture URLs and grid width on four landing pages (my page-builder bug, caught by the re-audit and the end-to-end test); 17 product SEO titles set equal to the product name. | Pictures 200; structured-data name = page heading |

Before-values are saved for every change: `evidence/seo-audit-2026-11-10/backup/` (Custom CSS, four page code blocks, all 22 products, old `llms.txt`, admin settings record) and the per-batch logs in `evidence/seo-audit-2026-11-10/live-changes/`.

## End-to-end test (after the changes)

Report: [after/e2e-report.md](../../evidence/seo-audit-2026-11-10/after/e2e-report.md)

- Buying path works on desktop and phone: choose options, add to cart, cart shows the right item and price, checkout page loads. Nothing was entered; the cart was left empty as found.
- All 52 internal links return 200. Host and https redirects are one hop. The overlay guard (`pointer-events:none`) is intact.
- Edited pages (Home, About, FAQ, Shipping, footer, header bar, /shop with 22 products, three product pages) render correctly.
- The two failures it found (broken landing-page pictures, grid too wide) were fixed afterwards and re-checked: every picture returns 200, four columns on desktop, two on a phone.

## Not done, and why

| Item | Reason |
|---|---|
| The 7 `/shop/<category>` filter pages still point to `/shop`, with no H1 or description | Squarespace gives categories no SEO fields. The landing pages are the workaround; the re-audit scores this as still open, and now also flags the overlap between the two sets. |
| Cookie bar still covers price and Add To Cart on a phone's first visit | Shrunk from 178 to 145 px, not enough. Moving it to the top pushes price and button below the fold. Original position restored. Needs a shorter consent text (your decision) or a different banner type. |
| `/home` still listed in the sitemap | It is the homepage's own address; hiding it would hide the homepage from search. |
| /shop loads 203 pictures | This template has no switch for the second (hover) picture. |
| "Handmade" in the Privacy Policy body; missing H1 on Cookie Policy; `http://` link on Imprint | Legal pages: left for your approval. |
| "How our knitwear is made" guide | Draft was thin and self-referential; not published. Draft kept in `live-2026-11-10/`. |
| About page addition; social preview image; logo alt text ("Autumn &amp; Wool" shown doubled) | About layout and the image need you; the logo alt field was not found in the admin. |
| Product URLs with "hand-knitted", "sustainable", "organic" | Unchanged on purpose, to keep what Google has indexed. |
| Lines marked `[OWNER]` in the product sheet (unknown colours on 7 products, "pairs with" lines) | Not guessed. |
| Empty phone field and missing organisation name/logo in structured data | Empty phone is how Squarespace prints a cleared number. Name/logo not attempted. |
| Google feed | Unchanged. Titles in the feed now differ from 14 renamed products; price, availability, link and image still match 98/98. Availability is still hard-coded "in stock". |

## New problems found by the re-audit, still open

- Black merino cardigan page says Brown and Blue are "to order" while the page and feed mark them in stock; that page also has no shipping/returns text. Both predate today.
- Gift guide: fixed prices will go stale; the "packed by hand … sent with tracking" line is wrong for a digital gift card; title says "Christmas" but the text does not.
- Guides are linked only from the new pages, not from Home, FAQ or product pages.
- Vests and hats landing pages are thin (two products each).
- FAQ says returns must be "unworn, unwashed"; Shipping says "unworn, unused".

## How the work was run

Main session planned, checked and wrote the reports; browser and audit work went to Haiku subagents, one in the Squarespace admin at a time. One job (creating pages) failed twice on Haiku and was finished by a Sonnet agent, which found the cause: "Add Blank" opens a second menu where "Page" must be clicked.
