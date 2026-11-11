# Batch 3: live wording replacements (2026-11-10)

Site: https://www.autumnandwool.com (Squarespace 7.1, admin rose-tarpon-ld9w). Browser: ego-browser task space `aw-batch3-wording-2026-11-10-a` (id 10). Spec: `business-os/seo-marketplace/live-2026-11-10/batch3-replacements.json`. Backups: `evidence/seo-audit-2026-11-10/backup/`.

Method: Code block source read from the CodeMirror 6 EditorView (`state.doc`), written to disk unchanged, replacements applied locally with python (count check per pair), written to `<page>-codeblock-after.html`, pasted back with the synthetic CM6 paste, editor text compared to the after file (equal), editor closed, Save, Exit, public check.

## Home (Code block)

- Backup: `backup/home-codeblock-before.html`, 10,902 chars = editor doc length (stable on re-read).
- Pairs: 8 of 8 applied, 0 skipped.
- Alts: 4 of 4 category tiles set (`/wool-sweaters` "Wool sweaters", `/wool-cardigans` "Wool cardigans", `/wool-sweater-vests` "Merino and wool sweater vests", `/wool-hats-and-scarves` "Wool hats and scarves").
- After: `backup/home-codeblock-after.html`, 11,173 chars. Length delta +271 = expected +271. `<` delta +4 = `<a`/`</a>` delta +4.
- Editor after paste: 11,173 chars, equal to file. Saved (Save greyed), exited.
- Public: 200. New strings present (`Machine-knitted, hand-finished`, `reviews on Etsy`, `8,000+ orders`, `href="/wool-sweaters"`, `/wool-hats-and-scarves`, alt texts). Old strings gone (`Handmade in Riga` in the block, `from 1,400+ customers`, `4.9★ by 1,400+ buyers`, `more than 8,000 orders`, `/shop/sweaters`, `/shop/beanies--hats`).
- Size: not comparable (see Notes).

## About (Code block)

- Backup: `backup/about-codeblock-before.html`, 5,531 chars = doc length.
- Pairs: 3 of 3 applied, 0 skipped. After: `backup/about-codeblock-after.html`, 5,596 chars (delta +65 = expected).
- Editor equals file, saved, exited.
- Public: 200. `orders on Etsy`, `reviews on Etsy`, `manual knitting machine` present; `orders shipped worldwide`, `from 1,400+ reviews`, `by hand or on a manually operated machine` gone.

## FAQs (Code block)

- Backup: `backup/faq-codeblock-before.html`, 5,964 chars = doc length.
- Pairs: 1 of 1 applied, 0 skipped. After: `backup/faq-codeblock-after.html`, 5,951 chars (delta -13 = expected).
- Editor equals file, saved, exited.
- Public: 200. `It is knitted on a manual knitting machine in Latvia` present; old sentence gone.

## Shipping Returns (Code block)

- Backup: `backup/shipping-returns-codeblock-before.html`, 6,148 chars = doc length.
- Pairs: 1 of 1 applied, 0 skipped. After: `backup/shipping-returns-codeblock-after.html`, 6,173 chars (delta +25 = expected).
- Editor equals file, saved, exited.
- Public: 200. New sentence present, old sentence gone.

## Footer text block

- Edited in the Home editor footer (ProseMirror text block). Selected the word `Handmade` (CDP double-click, selection checked = "Handmade"), typed `Machine-knitted, hand-finished` (insertText). Result: `Machine-knitted, hand-finished knitwear by Kristine in Riga, Latvia. Formerly Mareshop on Etsy.`
- Saved, exited.
- Public: `/` and `/about` 200, new sentence present, old gone.

## Custom CSS

- Live CSS read from the CodeMirror 5 instance (`.CodeMirror.CodeMirror`): 16,418 chars, equal to `backup/custom-css-before.css`.
- Replacements: 2 of 2 applied (`Free shipping  ·  14-day returns  ·  Made in Riga, Latvia` and `... Made in Riga"`).
- Appended block: a `@media (max-width: 767px)` block with selectors adjusted to the live banner classes (see below). Only padding, font-size, line-height, margin, min-height in the block. The `.sqs-widgets-confirmation-overlay` rule is unchanged (byte-identical; verified in the file).
- After: `live-changes/custom-css-after.css`, 16,954 chars.
- Saved via the Custom CSS menu Save (`data-test="menuHeader-save"`, DOM click; the frame-toolbar Save was overlapping it). Exited the editor cleanly.
- Public `https://www.autumnandwool.com/site.css`: contains `Made in Riga` (2), no `Handmade in Riga`, the `.sqs-widgets-confirmation-overlay{pointer-events:none !important}` rule is present, the new cookie rules are live (minified: comments stripped).

### Cookie-bar selectors

The spec's selectors `.sqs-cookie-banner-v2-cta` and bare `p`/`button` were replaced: `.sqs-cookie-banner-v2-cta` does not exist on the live banner. Live classes (from the earlier crawl `measure.json`):
- wrapper: `.gdpr-cookie-banner` (fixed bottom bar)
- text: `.sqs-cookie-banner-v2-text`
- button group: `.sqs-cookie-banner-v2-cta-container`
- buttons: `.sqs-button-element` with `sqs-cookie-banner-v2-accept` / `-deny`

Final block used:

```
@media (max-width: 767px) {
  .gdpr-cookie-banner { padding: 10px 12px !important; }
  .gdpr-cookie-banner p, .gdpr-cookie-banner .sqs-cookie-banner-v2-text { font-size: 11px !important; line-height: 1.3 !important; margin: 0 0 6px !important; }
  .gdpr-cookie-banner button, .gdpr-cookie-banner .sqs-cookie-banner-v2-cta-container .sqs-button-element { padding: 6px 10px !important; min-height: 32px !important; font-size: 12px !important; }
}
```

### Cookie-bar measurement (390x844, mobile emulation, fresh headless Chrome profile, no owner cookies)

Fresh profile was a separate Chrome instance (`scratchpad/b3/chrome-fresh`), not the owner's ego profile. Product page `/shop/p/oversized-merino-wool-v-neck-sweater-vest`, 10 s after navigation. Screenshot: `screenshots/product-vest-mobile-390-after.png`.

| item | before (earlier crawl) | after |
|---|---|---|
| banner top / height | y=666 / 178 | y=699 / 145 |
| price (`€126.00`) rect | not recorded | y=710 to 741 |
| Add To Cart rect | y=757 (per crawl) | y=757 to 805 |

Result: the banner is shorter (-33 px), but it still covers the price (overlap: price bottom 741 > banner top 699) and the Add To Cart button (757 to 805 under the banner from 699). The CSS change did not uncover price or Add To Cart. Buttons stay 42 px tall because min-height 32 px is below the current rendered height; no rule that would hide or move the banner was added, per the hard limits.

## Final public checks (after all edits)

- `/` 200, `/about` 200, `/faq` 200, `/shipping-returns` 200, `/shop` 200, `/shop/p/oversized-merino-wool-v-neck-sweater-vest` 200.

## Notes and incidents

- Page sizes are not stable between requests, so the "within 2% of before" check cannot be applied: Home 287,896 bytes (x3), then 170,212 later; About 290,296 before the edit, then 233,661 (x2). The content checks above are the evidence.
- Exit of the About editor: an attempted FAQ open ran before About's editor had closed, and the FAQ open failed (no change saved). About's Save was greyed and the editor was then exited cleanly. About re-checked publicly afterwards.
- Edit-mode entries: none into Site Header edit mode. The Home header "EDIT SITE HEADER" overlay was present but not clicked.
- A first FAQ open attempt used a wrong iframe selector and stopped on its guard before any edit.
