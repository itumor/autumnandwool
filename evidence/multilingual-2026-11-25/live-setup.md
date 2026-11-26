# Live Weglot setup evidence — 2026-11-25

Live admin and storefront checks through ego-browser, after the owner created the Weglot account with
`autumnandwool@gmail.com`. Screenshots in this folder: `site-languages-panel.png`, `weglot-oauth-consent.png`,
`latvian-home-live.png`, `weglot-glossary-live.png`. Nothing in this file is a proposal — these are observed states.

## Verified live facts

| Item | Observed value |
|---|---|
| Site Languages panel | Settings → Website → Site Languages exists on the current plan; "Multilingual by Weglot" with free ≤2,000 words / 1 language |
| Weglot account | Connected, created with the store email; Squarespace admin shows "Weglot Account", plan **Free** |
| Word count (admin) | **396 / 2,000** after switching the **home page only** to Latvian |
| Word count (Weglot dashboard, EN→LV) | 270 total translated words, **0% manually translated** |
| Languages | English default; **Latvian enabled, Public** (checkbox checked) |
| Customer notification emails | Multilingual Customer Notifications **on** (default) |
| Switcher | Live in site header: `listbox "language picker"` with options "Latviešu" / "English" |
| LV behaviour | Title changed to "Rudens un vilna \| Vilnas džemperi un kardigāni no Rīgas"; body translated client-side on the **same URL** |
| hreflang | none observed; "Multilingual SEO → Setup Subdomains" still offered in admin |
| Subdomain setup | Admin link opens a generic Weglot "Setup finished" page, not a subdomain config; no DNS change made |
| Glossary | 9 "Never translate" rules added for all language pairs (below) |

## Glossary rules added (live, Weglot dashboard)

`Autumn & Wool`, `Mareshop`, `Kristine`, `autumnandwool@gmail.com`, `Merino Wool Raglan Cardigan`,
`Merino Wool Raglan Sweater`, `Women's Classic Lambswool Crew Sweater`, `Merino Wool Hat & Scarf Set`,
`Merino Rib-Knit Beanie`. All case-insensitive, all language pairs. Source: `business-os/localization/lv-money-pages-draft.md` §2.

## Quality observations (not fixes)

- Machine output on the homepage is rough: "Wool knitwear for cooler days" → "Vilnas trikotāža „” vēsākām dienām"
  (stray quotation marks), "oversized" → "Pārmērīgi liela izmēra", brand name translated in `<title>`.
  The glossary rules above protect brand/product terms going forward but do not fix already-generated strings.
- Latvian is served on the **same URL** (no `lv.` subdomain), so hreflang/SEO separation is not yet in place.
- The overlay click-trap guard in `custom.css` was **not** touched during setup.

## Gates still open

- **G1:** free 2,000-word limit is already 396 words after one page; the full site cannot fit. Owner must choose a paid
  Weglot plan (a 20% Squarespace promo code `WELOVESQSP` is displayed in the admin) or exclude pages. No payment was made.
- **G2:** subdomain / hreflang not configured; needs Weglot DNS guidance.
- **G3:** native Latvian reviewer name still `[FILL]`. No draft from `lv-money-pages-draft.md` has been published.
- **G4:** PRD-19 adviser answer pending; legal lines stay machine output, not the reviewed draft.
- **G5:** priority PDP list still provisional.

## What was deliberately not done

- No paid plan, no card, no Weglot AI language-model setup (dismissed with "Set up later").
- No manual application of the LV draft translations (they are `translation-draft`, unreviewed).
- No DNS changes, no Custom CSS edits, no status-table edits.
