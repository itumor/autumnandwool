---
name: aw-merchant-feed-qa
description: Use when checking the Autumn & Wool Google Merchant Center feed (autumnandwool-google-feed.tsv / build_google_feed.py), reviewing Merchant Center diagnostics or disapprovals, preparing a feed re-upload after variant photos, or checking Google free-listing / Pinterest catalog readiness.
---

# aw-merchant-feed-qa — Google feed quality (read-only)

## Known state
- Live feed = `autumnandwool-google-feed.tsv` (98 rows, uploaded 19 Oct 01:31 EET). Approval due from 21 Oct.
- Generator = `build_google_feed.py`. **Do not run it**: it writes to `/mnt/user-data/outputs/...` (outside this
  repo) and its product list is hand-maintained. Read it as data.
- Open risk: ~48 colour variants share one image (beanie 11 colours, turtleneck 12 colours × XS/S/M, hat & scarf,
  cardigan blue). Google wants each variant's image to show that variant. Owner photography pending
  (`owner-action-pack-2026-10-19.md` A). Re-upload only after photos are bound (handbook §8.6).
- Merchant Center account edits and uploads are owner actions. You produce a checked TSV proposal + report.

## Checks (run in this order, record row ids)
1. **Structure:** header columns present: id, item_group_id, title, description, link, image_link,
   additional_image_link, availability, price, brand, condition, identifier_exists, google_product_category,
   product_type, gender, age_group, color, size, material. Tab-separated, UTF-8, no blank required cells.
2. **IDs:** `id` unique (SKU). Products with >1 variant share one `item_group_id` (parent product id); single
   products leave it blank; no group id reused across different products (case-insensitive).
3. **Apparel attributes:** every row has `color`, `size`, `gender`, `age_group=adult`. One colour per row, no
   "Black, Brown" lists. Colour name identical to the PDP swatch name. Size values match the PDP (S–XL, S/M,
   L/XL, One size).
4. **Titles:** ≤ 150 chars; brand/product type + key attributes first 70 chars; colour/size suffix matches row
   attributes; no promo text ("free shipping", "sale") or ALL CAPS. Title should match the PDP H1.
5. **Description:** facts only from `aw-product-page-copy` fact sources; flag `CLAIM-CHECK` phrases
   (handmade, sustainable, made in Latvia, Italian-spun) that lack evidence in `catalog-claims-cleanup-v3.csv`.
6. **Price/availability:** price + " EUR" equals the live PDP price. **The generator hard-codes
   `availability=in_stock` for every row** — cross-check against the product export/inventory; rows with 0 stock
   must be `out_of_stock` (handbook says 13 were out). Flag mismatches as High.
7. **Images:** `image_link` loads (HTTP 200), ≥ 1500px requested, real product photo, no text overlay; for
   variant rows, image shows that colour — else list as "variant image mismatch". `additional_image_link`
   ≤ 10, comma-separated.
8. **Links:** `link` returns 200 and opens the right product; ideally preselects the variant (Squarespace cannot
   deep-link a variant — note as accepted limitation).
9. **Category:** `google_product_category` id matches Google's taxonomy for sweaters/cardigans/vests/hats —
   verify the id in Google's published taxonomy file before proposing a change; `product_type` consistent.
10. **Shipping/tax:** set at account level (free, 4–10 business days per region); feed shipping column dropped on
    purpose. Do not add per-row shipping unless the owner changes policy.

Use Read/Grep on the TSV; for counts, reason over the file content (e.g. Grep `in_stock` count vs product export).

## Diagnostics review (when owner shares Merchant Center screenshots/exports)
Group issues: account-level (shipping, business info, website claim) → item disapprovals → warnings
(missing attributes, image mismatch, price mismatch). For each: rows affected, cause, fix layer (feed TSV /
PDP data — frozen / photo / account setting — owner), and whether re-upload is needed.

## Output
- `business-os/feed/<YYYY-MM-DD>-feed-qa.md`: summary (rows, pass, fail by check), findings table
  `check | rows | severity | evidence | proposed fix | owner action`.
- `business-os/feed/<YYYY-MM-DD>-feed-proposal.tsv`: full corrected feed, same columns, **only** with changes the
  report lists; plus a `-diff.csv` (`id,column,current,proposed,reason`). Never overwrite the live TSV.
- Re-upload checklist for the owner (when photos are bound): bind variant images → regenerate → QA → upload →
  check diagnostics after 24–72 h.

## Guardrails
- Never log in to or edit Merchant Center, Squarespace, Pinterest or Etsy. Never upload.
- Never mark an item in stock without inventory evidence; never invent GTINs (`identifier_exists=no` is
  correct for own-brand handmade goods).
- Don't promote free listings for SKUs off the safe-to-promote list.

## Sources
- Google Merchant Center Help: apparel best practices https://support.google.com/merchants/answer/7348545 ;
  item_group_id https://support.google.com/merchants/answer/6324507 ; missing required attributes
  https://support.google.com/merchants/answer/7495313 — Google help content, cited and paraphrased. Taken:
  title structure, first-70-chars rule, colour consistency, one variant per row, group-id rules, image size and
  variant-image match.
- nexscope-ai/ecommerce-skills `google-shopping-optimization`, `shopify-google-channel` —
  https://github.com/nexscope-ai/ecommerce-skills — MIT per repo; compared, beta, capability list only (no
  checklist), not used.
- finsilabs/awesome-ecommerce-skills — MIT; no feed-specific skill found in the visible catalogue.
- Local: `build_google_feed.py`, `PROJECT-HANDBOOK.md` §5.4, §8, §9.
