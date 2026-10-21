---
name: aw-etsy-listing
description: Use when auditing or rewriting Etsy (Mareshop) listings — titles, 13 tags, attributes, categories, descriptions, photo order, Etsy SEO keyword research, or aligning Etsy listings with autumnandwool.com products.
---

# aw-etsy-listing — Etsy listing optimisation proposals

Etsy shop: etsy.com/shop/Mareshop (4.9★, ~1.5k reviews, ~8.2k sales, 15 years). Etsy is the marketplace discovery
channel (README §4). You prepare proposals; the owner edits in Shop Manager.

## How Etsy search works (Seller Handbook, 2025)
- Etsy first gathers listings that match the query, then ranks them. It reads **title, tags, attributes,
  categories, description, first photo, reviews** together.
- Categories and attributes act like tags → choose the most specific subcategory and fill **every** relevant
  attribute (primary/secondary colour, material, occasion, holiday, size, style). Do not spend tags repeating
  phrases already covered by category/attributes.
- Title word order does not directly change ranking, but shoppers scan the start: put the clearest product
  phrase first. Keep titles readable — no stuffing, no repeated words.
- Up to **13 tags, max 20 characters each**, multi-word phrases allowed (verify limits in the listing form;
  third-party guides agree, official page could not be fetched).

## Procedure
1. **Inventory.** Owner exports listings (Shop Manager → Settings → Options → Download data) or pastes listing
   text. Do not scrape while logged in. Public listing pages may be WebFetched for title/price only.
2. **Match** each Etsy listing to its autumnandwool.com product (title, colour, price). Note price differences
   (Etsy fees: check against `aw-unit-economics` contribution before proposing price parity).
3. **Keyword research** per product: Etsy search-bar autocomplete, competitor listing titles (read only),
   GSC queries from `aw-ecommerce-seo`. Build: 1 primary phrase, 3–5 secondary, long-tail (fit, fibre, style,
   gift/occasion, season).
4. **Score** each listing 0–100: title 30, tags 25, description 20, attributes 15, photos 10. Note the gaps.
5. **Rewrite:**
   - *Title* (≤ 140 chars, aim ≤ 15 words): `<garment + fibre> <fit/style> <colour> – <secondary phrase>`.
     e.g. "Merino Wool Raglan Cardigan, Relaxed Fit Women's Knit Cardigan in Black, Brown or Blue".
   - *Tags*: 13 distinct phrases ≤ 20 chars, no duplicates of category/attribute words, cover synonyms
     (jumper/sweater/pullover), style (minimalist, oversized), use (layering, winter gift).
   - *Attributes*: list every attribute value to set.
   - *Description*: first 160 chars = what it is + fibre + fit (Google snippet). Then measurements in cm,
     fibre %, care, sizing note + link text "see size chart in photos", dispatch time, returns. Facts only from
     `aw-product-page-copy` sources.
   - *Photos* (up to 20 + video): order = 1 clean first photo on model, full garment visible, natural light;
     2 colour/texture close-up; 3 flat lay with measurements; 4 fit on body side/back; 5 size chart image;
     then each colour variant. Briefs via `aw-product-photo-briefs`. Never AI-alter the garment.
6. **Shop-level checks:** shop title/announcement, About section matches `llms.txt` facts, policies match
   site Shipping & Returns (and README §11 legal notes), sections mirror site categories.
7. **Measure:** Etsy Stats per listing (views, visits, favourites, orders) before/after, 30-day windows,
   one change batch per listing per month.

## Output — `business-os/etsy/<YYYY-MM-DD>-listing-proposals.md` + `.csv`
```
## <Listing title> (<listing id>) ↔ <site product url>
Score: 54/100 (title 15/30, tags 10/25, desc 12/20, attrs 9/15, photos 8/10)
Title:  - old  + new  (chars)
Tags:   1 merino cardigan … 13 (each ≤ 20 chars, count shown)
Attributes to set: …
Description diff: …
Photo order: …
CLAIM-CHECK / OWNER questions
```
CSV columns: `listing_id,field,current,proposed,chars,reason,source`.

## Guardrails
- Never log in to Etsy, edit listings, message buyers, reply to reviews or change prices/policies.
- Never invent reviews or move Etsy reviews onto the site as product reviews; Etsy history wording only as
  "4.9★ from 1,500+ reviews on Etsy as Mareshop".
- No claims without evidence (handmade, made in Latvia, sustainable, organic). Etsy's handmade policy is strict:
  "made by" attributes must be true; flag for owner.
- No trademarked brand names of others in tags/titles.

## Sources
- Etsy Seller Handbook, "Keywords 101" (updated 26 Aug 2025) —
  https://www.etsy.com/seller-handbook/article/keywords-101-everything-you-need-to-know/382774281517 —
  © Etsy; WebFetch returned 403, content taken from search-result summaries and paraphrased (search reads
  title/tags/attributes/description/first photo/reviews; categories act as tags; title order). UNVERIFIED in full.
- nexscope-ai/ecommerce-skills `etsy-seo` — https://github.com/nexscope-ai/ecommerce-skills/blob/HEAD/etsy-seo/SKILL.md
  — repo states MIT, file lacks license line, requires a Python analyzer script (not used). Taken: 5-dimension
  weighted score (30/25/20/15/10), title formula idea, HIGH/MED/LOW action plan.
- Tag limits (13 × 20 chars): alura.io https://alura.io/docs/article/etsy-tags-guide and Printify
  https://printify.com/blog/etsy-tags/ — third-party, cited.
- claudskills.com "Etsy Integration"/"Etsy Multi Shop" — API/shop-management skills, compared, rejected (need
  Etsy API access, no listing-SEO method).
