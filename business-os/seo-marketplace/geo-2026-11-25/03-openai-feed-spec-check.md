# OpenAI feed spec check — 2026-11-25

## Verdict
Our 25-column header contains all 11 fields the **Stable** OpenAI file-upload spec requires for discovery (the nine basic fields plus `target_countries` and `store_country`), and all 14 optional fields we use are real. It is **not uploadable as-is for our intended market**: `target_countries` is sent as `LV,EE,LT` where the spec documents a JSON array of ISO-2 codes and explicitly says standard uploads use `["US"]` regardless of the column; `store_country=LV` is likewise overridden to `US` in standard uploads. The single most important required change is to **confirm country/currency support with OpenAI and set the real markets in Business Hub**, not to rely on uploaded country columns. The two non-schema columns (`google_product_category`, `product_type`) were replaced by the spec's `product_category` with the text path on 2026-11-25; the committed Google TSV was verified byte-identical after that change.

Source of truth: `https://developers.openai.com/commerce/specs/file-upload/products` (Stable, read 2026-11-25). A Draft version exists at `?version=draft` and is published for planning only — it is not the supported contract; we did not use it.

## Column-by-column table (25 columns)

| # | Our column | Official field | Requirement | Expected format | Verdict | Source |
|---|---|---|---|---|---|---|
| 1 | `item_id` | `item_id` | Required | String, stable, unique per item/variant | CORRECT | OFFICIAL products §Basic product data |
| 2 | `title` | `title` | Required | String, ≤150 chars suggested | CORRECT (generator truncates to 150) | OFFICIAL products §Basic product data |
| 3 | `description` | `description` | Required | String, factual, ≤5000 chars suggested | CORRECT as schema; content claims flagged separately | OFFICIAL products §Basic product data |
| 4 | `url` | `url` | Required | Absolute HTTP/HTTPS URL, public, stable | CORRECT | OFFICIAL products §Basic product data |
| 5 | `brand` | `brand` | Required | String, real brand not placeholder | CORRECT (`Autumn & Wool`) | OFFICIAL products §Basic product data |
| 6 | `seller_name` | `seller_name` | Required | String, real seller not placeholder | CORRECT (`Autumn & Wool`) | OFFICIAL products §Basic product data |
| 7 | `image_url` | `image_url` | Required | Direct image URL, public, shows this variant | CORRECT (known wrong-variant photos are a content issue, not schema) | OFFICIAL products §Basic product data |
| 8 | `additional_image_urls` | `additional_image_urls` | Optional | Array of URL strings, **or comma-separated string** in delimited files; commas inside URLs percent-encoded | LIKELY-CORRECT (we send a comma-separated string) | OFFICIAL products §Media |
| 9 | `availability` | `availability` | Required | `in_stock`, `out_of_stock`, `pre_order`, `backorder`, `unknown`; omitted/unrecognized rejects the row | CORRECT (only `in_stock`/`out_of_stock` present) | OFFICIAL products §Availability & inventory |
| 10 | `price` | `price` | Required | `amount CURRENCY`, e.g. `79.99 USD` — decimal, space, uppercase ISO 4217 | CORRECT syntactically (`126.00 EUR`); currency must be configured for the feed | OFFICIAL products §Price & promotions |
| 11 | `target_countries` | `target_countries` | **Required** | **Array of strings**, e.g. `["US"]`; uppercase ISO 3166-1 alpha-2; shared format currently represents `US`, `CA`, `MX` | **WRONG-FORMAT / WRONG-MARKET** — we send bare `LV,EE,LT` | OFFICIAL products §Geo tagging |
| 12 | `store_country` | `store_country` | **Required** | String, e.g. `US` (ISO alpha-2) | CORRECT format (`LV`) but **standard uploads use `US` regardless** — cannot select Latvia via the column | OFFICIAL products §Geo tagging |
| 13 | `group_id` | `group_id` | Conditionally required for variants | Stable parent ID shared by all variants; must differ from each `item_id` | CORRECT (product ID when >1 variant, blank otherwise) | OFFICIAL products §Variants |
| 14 | `listing_has_variations` | `listing_has_variations` | Conditionally required for variants | Boolean `true`/`false` | CORRECT (lowercase strings) | OFFICIAL products §Variants, §Value conventions |
| 15 | `variant_dict` | `variant_dict` | Conditionally required for variants | JSON object of string values, e.g. `{"color":"Black","size":"10"}`; needs `listing_has_variations=true` and `group_id != item_id` | CORRECT (`json.dumps`, nonempty keys/values; group ID is a product ID, item IDs are SKUs) | OFFICIAL products §Variants |
| 16 | `product_category` | `product_category` | Optional | Text path, broad → specific, `>` separated, e.g. `Apparel & Accessories > Shoes` | CORRECT after 2026-11-25 fix (replaced `google_product_category` + `product_type`, which are not OpenAI fields) | OFFICIAL products §Item information; §Compatibility notes |
| 17 | `condition` | `condition` | Optional | `new`, `refurbished`, `used` | CORRECT (`new`) | OFFICIAL products §Item information |
| 18 | `gender` | `gender` | Optional | `male`, `female`, `unisex` | CORRECT (`female`, `unisex`) | OFFICIAL products §Item information |
| 19 | `age_group` | `age_group` | Optional | `newborn`, `infant`, `toddler`, `kids`, `adult` | CORRECT (`adult`) | OFFICIAL products §Item information |
| 20 | `color` | `color` | Optional | String, consistent with image and `variant_dict` | CORRECT (empty on some rows = omitted, allowed) | OFFICIAL products §Item information |
| 21 | `size` | `size` | Optional | String label; use `variant_dict` when size distinguishes variants | CORRECT (`One size` is a label, allowed) | OFFICIAL products §Item information |
| 22 | `material` | `material` | Optional | String, principal materials | CORRECT (`Merino wool` etc.; no unverifiable fibre % — see policy note) | OFFICIAL products §Item information |
| 23 | `accepts_returns` | `accepts_returns` | Optional | Boolean; policy URL does not set it | CORRECT (`true`) | OFFICIAL products §Returns |
| 24 | `return_deadline_in_days` | `return_deadline_in_days` | Optional | Positive integer; only with `accepts_returns=true` (alias `return_window`) | CORRECT (`14`) | OFFICIAL products §Returns |
| 25 | `shipping_price` | `shipping_price` | Optional | Money string, same currency as `price`, nonnegative; omitted = unknown, not free | CORRECT syntactically (`0.00 EUR` asserts free shipping). Truthfulness confirmed on the live site: `live-text-2026-11-25.md` shows "Free shipping Latvia, US & many more countries"; display support still unconfirmed | OFFICIAL products §Fulfillment; REPO live-text capture |

Compatibility aliases the spec does allow: `id`/`sku` → `item_id`, `item_group_id` → `group_id`, `enable_search` → `is_eligible_search`, `enable_checkout` → `is_eligible_checkout`, `is_eligible_ads` → `is_ads_eligible`, `return_window` → `return_deadline_in_days`. `google_product_category` and `product_type` are **not** in that list. (OFFICIAL products §Compatibility notes.)

## Value-level questions

1. **`target_countries` real? format?** Yes, required. Array of strings, uppercase ISO 3166-1 alpha-2, e.g. `["US"]`; shared format currently represents `US`, `CA`, `MX`. Standard uploads use `["US"]` **regardless of the column**. Our `LV,EE,LT` is neither a JSON array nor a country the shared format lists. Source: OFFICIAL products §Geo tagging.
2. **`variant_dict` real? JSON? keys?** Yes. JSON object of string values mapping option names to selected values; spec example `{"color":"Black","size":"10"}`. Keys must be nonempty and unique per combination; ignored unless `listing_has_variations=true` and `group_id` differs from `item_id`. Source: OFFICIAL products §Variants.
3. **`price` format?** `amount CURRENCY` — decimal in major units, space, uppercase three-letter ISO 4217 code, e.g. `79.99 USD`. Our `126.00 EUR` matches. Currency must be one agreed/configured for the feed. Source: OFFICIAL products §Price & promotions.
4. **`shipping_price` real? currency/country?** Real and optional: money string in the **same currency as `price`**, nonnegative; zero means no charge. No country is attached to this field (the alternative `shipping` tuple is country-bearing but requires feed-specific setup). Spec says to confirm display support for the integration. Source: OFFICIAL products §Fulfillment.
5. **`currency` / `locale` field missing?** No dedicated `currency` field in the schema — currency is embedded in `price` (and `shipping_price`/`sale_price`). `language` appears in older/legacy references but is not a discovery field in the Stable products schema we read. Markets are chosen in Business Hub, not by a row field. Source: OFFICIAL products §Price & promotions, §Geo tagging; OFFICIAL submit-product-feeds.
6. **GTIN required?** No — `gtin` and `mpn` are optional. Spec says omit a GTIN when unassigned and **do not invent a value** to replace a missing GTIN. Our omission is compliant. Source: OFFICIAL products §Variants.
7. **`accepts_returns` / `return_deadline_in_days` naming?** Both real and optional. `return_window` is accepted as an alias but `return_deadline_in_days` wins. Window must be a positive integer and only supplied with `accepts_returns=true`. Source: OFFICIAL products §Returns, §Compatibility notes.
8. **Header row / TSV?** The spec names columns and shows CSV/TSV cell-encoding rules, so a header row with these column names is implied, but an explicit sentence "a header row is required" was **not found** in the pages read — UNVERIFIED. TSV is referenced explicitly ("JSON objects in CSV or TSV cells must be serialized as JSON"), so TSV is accepted. Third-party sources additionally list CSV, TSV, XML and JSON as accepted formats; that list is THIRD-PARTY and not relied on here. Sources: OFFICIAL products §Value conventions, §Media; OFFICIAL submit-product-feeds.

## Required changes before upload

1. **Do not upload until GEO-02 owner actions are complete.** Business Hub claim + identity verification are prerequisites to product upload (OFFICIAL submit-product-feeds); this is an account gate, not a schema fix.
2. **Resolve the market mismatch (blocking for our Baltic goal).** Ask OpenAI, during onboarding, whether multi-country processing is enabled and which countries/currencies are allowed. Set the real markets in Business Hub ("Choose the countries and currencies where you sell your products"). Do not expect `LV,EE,LT` or `LV` in the file to select Latvia — the spec says standard uploads target US regardless. If multi-country is not available, this feed cannot serve our intended market and should not be uploaded as a Baltic catalog.
3. **Fix `target_countries` value format** from `LV,EE,LT` to a JSON array (e.g. `["LV"]`) **only once step 2 confirms those codes are supported**; otherwise the value is inert and misleading. Keep the `-DRAFT-do-not-upload` filename until then.
4. **DONE — category columns fixed 2026-11-25.** `google_product_category` (numeric `212`/`173`) and `product_type` were replaced by the single spec field `product_category` carrying the existing text path, e.g. `Apparel > Knitwear > Sweaters`. `build_google_feed.py` was updated and the OpenAI draft regenerated to 25 columns; the committed Google TSV was verified byte-identical to the previous version.
5. **Truthfulness check closed 2026-11-25.** `shipping_price=0.00 EUR` and `return_deadline_in_days=14` match the live homepage text captured verbatim the same day (`live-text-2026-11-25.md`: "Free shipping Latvia, US & many more countries", "14-day returns Easy, no-fuss exchanges"). Only the question of whether the integration displays `shipping_price` remains unverified — the spec requires that to be confirmed during onboarding. Spec note: omitted/empty means unknown, not free shipping.
6. **Review description claims** for factual accuracy before upload: the copy contains `100%`, `extra-fine`, `Italian-spun`, `hand-sewn`, `kraft gift packaging` and a URL slug with `hand-knitted`. Schema accepts them as strings; our brand-voice policy does not allow unverifiable fibre/origin/handmade claims. This is a content gate, independent of the schema verdict.

## What could not be verified
- Whether an explicit header row is mandatory (implied by named columns, not stated in pages read).
- Whether our integration (as opposed to the shared/default format) has multi-country processing enabled, and whether `LV`/`EE`/`LT` are accepted codes for it.
- Whether `shipping_price` is displayed for our integration; the spec requires confirmation during onboarding.
- Whether the `0.00 EUR` shipping charge matches the live shipping policy (needs owner confirmation, not a docs question).
- Whether `additional_image_urls` as a bare comma-separated string (without CSV quoting) is accepted for **TSV** specifically; the spec shows the quoted CSV form and says array in JSONL. LIKELY-CORRECT, not CONFIRMED.
- We deliberately did **not** read the Draft spec (`?version=draft`); any differences between Draft and Stable are out of scope here.

## Sources
- OFFICIAL — Product feed schema (Stable): `https://developers.openai.com/commerce/specs/file-upload/products` — read 2026-11-25.
- OFFICIAL — File Upload index (points to Stable and Draft variants): `https://developers.openai.com/commerce/specs/file-upload/legacy.md` — read 2026-11-25.
- OFFICIAL — Submit product feeds (Business Hub, identity verification, country/currency setup): `https://developers.openai.com/commerce/guides/submit-product-feeds.md` — read 2026-11-25.
- OFFICIAL — Agentic Commerce docs index: `https://developers.openai.com/commerce/llms.txt` — read 2026-11-25.
- THIRD-PARTY — used only as background, not for any field verdict: `https://www.lengow.com/get-to-know-more/chatgpt-product-feed`, `https://commerceclarity.com/blog/chatgpt-product-feed-required-fields`, `https://ppcdatafeed.com/blog/chatgpt-ads-product-feed-guide` — search results 2026-11-25.
