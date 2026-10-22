# Gift guide page proposal: "Wool gifts", 2026-10-21 (DRAFT for owner approval)

Author: aw-seo-marketplace. Task SEO-21. Written to `business-os/seo-marketplace/` (my lane folder for this wave)
instead of `business-os/proposals/`. Nothing is built or published.

## Decision for the owner
Option A (lighter, recommended): reuse the existing category `/shop/winter-wool-gifts` (3 products, in the sitemap).
Add the intro below as its category description and assign the beanie, the set, the vest and one cardigan to it (no gift
card: none exists, A-GM-22 / W3-6). No new URL, no redirect.
Option B: a new page `/wool-gifts` with three product blocks by price tier. More work, plus one more page to keep
indexed. Only if the owner wants a page for the pitches.
Either way: hide or merge `/shop/gift` (thin, in sitemap), so the site does not have two gift pages competing for
"wool gifts".

## Page fields
- SEO title: **Wool Gifts for Her: Merino Beanies, Sets & Sweaters | Autumn & Wool** = 68 chars, too long →
  **Wool Gifts for Her, Merino & Wool Knitwear | Autumn & Wool** (58)
- Meta (≤ 155): "Wool gifts for her at three prices: a merino beanie, a merino hat and scarf set, and wool sweaters and cardigans.
  Add a handwritten gift note." (142)
- H1: Wool gifts

## Intro (≈ 70 words)
> Wool gifts at three prices. A rib-knit merino beanie in 11 colours, a matching merino hat and scarf set, and
> sweaters, cardigans and sweater vests in merino, lambswool or pure new wool. Add a handwritten gift note, and we leave
> prices off the packing slip. Not sure of her size? Choose a one-size piece. Shipping is free to eligible destinations.
> [Order-by dates per country: added only after Operations publishes them, 20 Nov.]

## Tiers (prices from live `llms.txt`, 21 Oct; recheck on the day)
| Tier | Products |
|---|---|
| Under EUR 50 | Rib-Knit Merino Beanie, EUR 45 |
| EUR 50–120 | Merino Wool Hat & Scarf Set, EUR 110; Merino Turtleneck, Lightweight Knit, EUR 110 (only colours with real photos, ruling C7) |
| Special | Oversized Merino Wool V-Neck Sweater Vest, EUR 126; Merino Wool Raglan Cardigan, EUR 160; Merino Striped Oversized Sweater, EUR 165 |

Gate: any product listed must be on Production's GREEN list (G2) the week it goes live. Swap out AMBER/RED items.

## CLAIM-CHECK
- No "handmade", "made in Latvia/Riga", "sustainable". No "perfect gift" or urgency.
- Wave 3 (GM rulings W3-6, W3-7; A-GM-22): no gift card and no "ships in gift packaging" (no gift wrap). Allowed
  perks only: handwritten gift note, prices left off the packing slip `[VERIFY how the customer asks for the note]`.
  The live feed still says "Ships in kraft gift packaging" on the 14 beanie and set rows; removal is proposed in
  `feed/2026-10-21-feed-claims-proposal-wave3.md` R4.
- Fibre: names only, no % and no "extra-fine" (W3-8, A-GM-10).
- No returns promise in the intro (ruling C12).
