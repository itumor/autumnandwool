---
name: aw-product-page-copy
description: Use when drafting or rewriting Autumn & Wool product titles, product descriptions, SEO titles/meta descriptions, size-and-fit or care copy for a product page, or proposing PDP text changes as a diff for owner approval.
---

# aw-product-page-copy — product page copy proposals

Product data is **frozen**. This skill produces proposals only: a CSV row or a markdown diff the owner pastes into
Squarespace herself. Voice rules come from `aw-brand-voice`; read it first if it exists.

## Fact sources (only these)
1. Current PDP text (WebFetch the product URL) and `products_Oct-17_10-46-00PM.csv`.
2. `build_google_feed.py` `D` list (cleaned descriptions with measurements) and `llms.txt` product list.
3. Verified rows of `catalog-claims-cleanup-v3.csv`. Unverified claims stay out.
4. Size guide (`/size-guide`): S–XL = EU 36–42, UK 8–14, US 6–12; many oversized pieces are one size.
5. Shipping/returns facts in `llms.txt` (free shipping, 2–5 working days dispatch, 14-day returns).

If a fact is missing (fibre %, a measurement, colour list), write `[OWNER: confirm …]`. Never fill the gap.

## Claims that need evidence before use
`handmade`, `hand-knitted`, `made in Latvia/Riga`, `sustainable`, `organic`, `eco`, `Italian-spun`,
`extra-fine`, `itch-free`, `non-pilling`, any review count or star rating on a PDP. Current approved wording:
"Knitted on a manually operated knitting machine and hand-sewn in Latvia" appears in the feed script, but
origin evidence is still an open item (README §7, `markets-and-gift-guides.md` warning). Mark such lines
`CLAIM-CHECK` in the proposal.

## Page structure (what a PDP needs, in order)
1. **Title** — garment + key attribute + colour if single-colour. Plain, no keyword strings, ≤ 60 chars.
   e.g. "Merino Wool Raglan Cardigan". Matches the feed `title` and the H1 (QA found vest title ≠ H1).
2. **Opening line** (≤ 25 words) — what it is, how it wears, who it suits. Visible above the fold at 390px.
3. **Fit** — relaxed / oversized / regular; model height + size worn if known; "between sizes, size …"
   advice only if the owner confirms it.
4. **Measurements** — garment cm (width, length, sleeve), one line each. Link to size guide.
5. **Material + care** — fibre % exactly as labelled; hand wash cold, dry flat (from `llms.txt` care section).
6. **Colours** — list available colours; "select your colour below" when the product has variants
   (Add-To-Cart silently fails without a selection).
7. **Delivery + returns** — one line, same wording on every PDP.
8. **SEO title** ≤ 60 chars "<Product> — <colour/benefit> | Autumn & Wool"; **meta description** ≤ 155 chars:
   what, fibre, fit, free shipping. Feed `aw-ecommerce-seo` keyword choices in here.

Copy principles (adapted from marketingskills `copywriting`): clarity over cleverness; turn each feature into
what it means for the wearer (ribbed cuffs → stay put when sleeves are pushed up); specific and checkable
(cm, %, days); customer words from Etsy reviews/messages if the owner supplies them; no exclamation marks;
cut lines a competitor could paste unchanged.

## Procedure
1. Pick the SKUs (default: the 5 priority PDPs). Pull current text for each.
2. Build a fact sheet per SKU: fibre, fit, measurements, colours, sizes, price, image count per colour. Flag gaps.
3. Run the `aw-cro-audit` funnel steps 2–3 on the current copy; list what is missing or contradictory.
4. Draft the new copy in the structure above. Keep the owner's voice where it is already good (point edits).
5. Self-check: every factual line traces to a source; title = H1 = feed title; no banned claim without evidence;
   lengths within limits; colours match variant names exactly.
6. Write the proposal file and a CSV for bulk paste.

## Output
`business-os/proposals/pdp-copy-<YYYY-MM-DD>.md`:
```
## <Product name> (<product id>, <url>)
Fact sheet: fibre | fit | measurements | colours | sizes | gaps
### Title
- Merino Wool Raglan Cardigan — Black Merino Wool Raglan …   (old, struck)
+ Merino Wool Raglan Cardigan
### Description (diff, - old / + new)
### SEO title / meta description
CLAIM-CHECK: <lines needing evidence>   OWNER: <questions>
```
Plus `business-os/proposals/pdp-copy-<YYYY-MM-DD>.csv` with columns
`product_id,url,field,current,proposed,reason,source,claim_check`.

## Guardrails
- Never edit Squarespace. Never invent reviews, quotes, specs, stock, lead times or awards.
- Do not translate into LV/DE unless asked; translations are flagged for native review.
- Keep the Etsy history accurate: "4.9★ from 1,500+ Etsy reviews as Mareshop" is marketplace history, never
  presented as reviews of the individual product.

## Sources
- coreyhaines31/marketingskills `skills/copywriting/SKILL.md` — https://github.com/coreyhaines31/marketingskills
  — MIT. Taken: clarity/benefit/specificity/customer-language principles, "supportable claims only", point-edit
  rule, three-line test. Adapted.
- nexscope-ai/ecommerce-skills `product-description-generator` —
  https://github.com/nexscope-ai/ecommerce-skills — repo states MIT, file has no license line. Compared; took only
  the idea of separate DTC vs Etsy length limits. Its keyword-scoring web scrape is not used.
- Google Merchant Center apparel best practices — https://support.google.com/merchants/answer/7348545 — Google
  help content, cited. Taken: keep colour names identical across title, description and variant.
- Baymard apparel size information — https://baymard.com/blog/apparel-size-information — cited, own words.
