# "Hats & scarves" category: merge Beanies + Sets (SEO-13), wave 3, 2026-10-21 — DRAFT for owner

Author: aw-seo-marketplace. **ASSUMPTION MODE:** GM assumes decision 29 = merge (A-GM-24,
`head-of-ecommerce/assumptions-wave3.md`); the slug and redirects are A-SEO-10. This is an apply-ready proposal. The
owner makes the change in Squarespace, or doesn't. Options (a) hide / (b) merge are in `2026-10-21-onpage-proposals.md` §D.

## Why
Beanies and Sets each hold 1 product (QA-REPORT): two thin pages that compete with each other. The home tile already says
"Hats & scarves", so the merged name also fixes the label mismatch (QA §2).

## Steps (owner, Squarespace → Commerce → Products / Categories, about 15 min)
1. Create category **Hats & scarves**, slug `hats-scarves` (A-SEO-10).
2. Assign the Rib-Knit Beanie (`69105690dc1b…`) and the Merino Wool Hat & Scarf Set (`69105624c6bf…`) to it.
3. Remove the Beanies and Sets categories.
4. **Redirect list (needs owner approval before step 3):** Settings → Developer tools → URL mappings:
   ```
   /shop/beanies -> /shop/hats-scarves 301
   /shop/sets -> /shop/hats-scarves 301
   ```
   `[VERIFY the current category URLs first: they are assumed, not fetched today]`. Product URLs don't change, so the
   feed and pins are unaffected.
5. Point the home "Hats & scarves" tile to `/shop/hats-scarves`.
6. Rollback: re-create the old categories and delete the two mappings.

## Copy
- **SEO title (56):** Merino Wool Beanies & Hat and Scarf Sets | Autumn & Wool
- **Meta description (145):** Rib-knit merino wool beanie with a fold-over cuff, and a matching hat and scarf set. Fits
  54–58 cm heads. Free shipping to eligible destinations.
- **Intro (≈ 75 words, category description field):**
  > Two pieces for cold days. The rib-knit beanie in merino wool has a fold-over cuff and fits heads of 54–58 cm. The
  > hat and scarf set pairs the same beanie with a matching rib-knit scarf, about 190 × 36 cm, and is often chosen as a
  > gift. Colours are listed on each product page. In-stock pieces are dispatched in 2–5 working days; made-to-order
  > beanies and sets within 5 working days.

Facts: measurements from the feed `D` list as in `2026-10-21-onpage-proposals.md` §B. Dispatch lines: A-GM-03 /
A-PRD-14 (the MTO line is an assumption until decision 3). "Merino wool" without %, A-GM-10 `[CLAIM-CHECK]`. No origin or
"handmade" wording in title, meta or intro, so nothing waits on decision 16. No colour count in the copy, because unphotographed colours may be trimmed on 14 Nov (A-GM-24).

ASSUMPTION: A-GM-24, A-GM-03, A-GM-10, A-PRD-14, A-SEO-10; registers: `business-os/head-of-ecommerce/assumptions-wave3.md`,
`business-os/seo-marketplace/assumptions-wave3.md`. DRAFT, nothing applied.
