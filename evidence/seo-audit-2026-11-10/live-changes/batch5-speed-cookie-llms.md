# Batch 5: Home image tuning, /shop hover, cookie banner position, llms.txt (2026-11-10)

Site: https://www.autumnandwool.com (Squarespace 7.1, admin rose-tarpon-ld9w). Browser: ego-browser task space `aw-batch5-speed-cookie-llms-2026-11-10` (id 12). Spec: `business-os/seo-marketplace/live-2026-11-10/batch5-replacements.json`.

## A. Home Code block image tuning: DONE

- Method: Home page editor > Code block (CodeMirror 6 view, `state.doc`), source read unchanged, saved to `backup/home-codeblock-before-batch5.html` (11,173 chars = editor doc length, stable on re-read).
- Replacements applied locally with python (count check per pair): 7 of 7 pairs applied, 0 skipped. The 15x global `?format=1000w"` -> `?format=750w"` step ran first, then the hero `?format=1500w"` -> `?format=1000w" fetchpriority="high"`, then the five Instagram alts.
- After file: `backup/home-codeblock-after-batch5.html`, 11,254 chars (delta +81). 0 `?format=1500w` in the file; `fetchpriority="high"` 1; "Instagram photo 1" to "5" each 1; "reviews on Etsy" 2; "/wool-sweaters" 1.
- CM6 synthetic paste, editor length 11,254 = file length, editor text equal to file. Saved (Save greyed), Exit, no dialogs.
- Public check: `/` 200. `fetchpriority="high"` present (6 total on page, incl. other blocks), five "Instagram photo N" alts present, "reviews on Etsy" present, "/wool-sweaters" present, "Machine-knitted, hand-finished" present (2). Public page still contains `format=1500w` 17 times, all in other page blocks (ChatGPT Image banner and similar), none in the Home code block source.
- No revert needed.

## B. /shop alternate image on hover: NOT AVAILABLE

- /shop Store section settings (Shop page editor > section settings): Elements tab (Section Header, Store Title, Breadcrumbs, Filters, Product Thumbnails toggle, Add to Cart Button, Price) and Design tab (Layout, Product Layouts, Product Image: Aspect Ratio, Image Text Spacing, Corners). No hover or alternate-image option found.
- Site Styles editing mode in the Shop editor: no "hover" text found.
- Nothing changed; Save stayed greyed; editor exited with no edits.
- `<img` count on https://www.autumnandwool.com/shop (curl, UA Mozilla/5.0): before 203, after 203 (unchanged).
- Products on /shop: 22 (unique `data-product-id`), /shop 200.

## C. Cookie banner position on phones: REVERTED (original value restored)

- Original values: Site Styles > Accessories > Cookie Banner, BANNER > Position = **Bottom**. Settings > Website > Cookies and Data Privacy: layout Pill, non-essential cookies Restricted (not touched). Colour theme and Disclaimer Text Size untouched.
- Options offered: Top, Bottom Left, Bottom Right, Bottom.
- Measured, fresh headless Chrome (127.0.0.1:9341, own profile `scratchpad/b5/chrome-fresh`, owner profile not used), product page `/shop/p/oversized-merino-wool-v-neck-sweater-vest`, 10 s after load:

| variant | banner (x,y,w,h) | price y | Add To Cart y | notes |
|---|---|---|---|---|
| Bottom (original) 390x844 | 0,699,390,145 | 710-741 | 757-805 | banner covers price and ATC |
| Bottom Left 390x844 | 10,673,370,161 | 710-741 | 757-805 | full-width at phone size, covers price and ATC |
| Top 390x844 | 0,31,390,145 | 855-886 | 902-950 | banner does not cover them, but content shifts down: price and ATC below the 844 px fold |
| Top 1440x900 | 0,35,1440,70 | 373-405 | 421-476 | desktop sane |
| Bottom restored 390x844 | 0,699,390,145 | 710-741 | 757-805 | identical to original |
| Bottom restored 1440x900 | 0,830,1440,70 | 303-335 | 351-406 | desktop sane |

- Bottom Right not measured: at 390 px the Bottom Left variant is already full width, so the corner choice makes no difference on phones.
- Decision: no option left both price and Add To Cart fully visible in the first 390x844 screen with the banner usable. Top is the only one that stops covering them but pushes them below the fold. Restored Position = Bottom and saved. Banner text, buttons and consent behaviour were not touched; no CSS hiding.
- Screenshots: `screenshots/cookie-mobile-after.png` and `screenshots/cookie-desktop-after.png` (state after restore = original Bottom). Top-variant evidence kept as `screenshots/cookie-mobile-top-test.png` and `screenshots/cookie-desktop-top-test.png`.

## D. llms.txt: DONE (editor content replaced; public file updated)

- Old editor content (Marketing > SEO > LLMS.txt): 8,038 chars, verbatim in `backup/llms-before.txt` (8,038 chars, equal on re-read). Contains "since 2011".
- New content from `business-os/seo-marketplace/live-2026-11-10/llms.txt`: 7,525 chars. Pasted via keyboard paste into the textarea; editor length 7,525 = file length, equal. Saved (panel closed, Save greyed).
- Public check after 60 s: `curl -sSL -A "Mozilla/5.0" https://www.autumnandwool.com/llms.txt` = 200, text/plain, 7,525 chars; contains "wool-gifts": yes; contains "since 2011": no.
- URL mapping `/llms.txt -> static1 ... llms.txt 301` (Developer Tools > URL Mappings) and the Not Linked page "llms.txt" were NOT touched. The public result matches the new editor content, so the editor is what serves the file.

## Final checks

- `/` 200, `/shop` 200 (22 products, 203 img), `/shop/p/oversized-merino-wool-v-neck-sweater-vest` 200.
- Chrome started for measurements: stopped after the run (see notes below).
- No edit-mode into Site Header, no upgrade/discard/delete prompts seen. Task space closed with finish({ keep: [] }).
