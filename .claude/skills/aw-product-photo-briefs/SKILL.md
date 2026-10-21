---
name: aw-product-photo-briefs
description: Use when planning Autumn & Wool product photography, writing a shot list or shoot brief (flat lay, on-body, ghost mannequin, detail, variant-per-colour photos for Merchant Center), or deciding what AI image editing is allowed on garment photos.
---

# Autumn & Wool product photo briefs and shot lists

Purpose: real, true-colour photos for every visible SKU and colour, reusable across PDP, Google Merchant Center,
Pinterest, Instagram and ads. First priority (hiring-plan, owner-action-pack A): one photo per colour for every
visible SKU.

Read first: `.claude/skills/aw-brand-voice/SKILL.md` (visual identity s5, claim rules s3).

## Priority backlog (as of 19 Oct 2026, re-check `owner-action-pack-*.md` A)

| Product | Colours missing a variant photo | Feed rows at risk |
|---|---|---|
| Merino Turtleneck (Lightweight) | Berry Purple, Chestnut Brown, Classic Grey, Dusty Rose, Melange Beige, Melange Brown, Melange Taupe, Purple Brown, Rose Pink, Royal Blue, Sky Blue | 36 |
| Rib-Knit Beanie | Beige, Brown, Camel, Gray, Light grey, Melange grey, Pink, Bordeaux, Navy, Blue | 11 |
| Hat & Scarf Set | Brown, Gray | 3 |
| Merino Wool Raglan Cardigan | Blue | 1 |

Order: by feed rows at risk, then by safe-to-promote list. Only garments that physically exist in that colour.

## Shot types (standard set per SKU)

| # | Shot | Use | Notes |
|---|---|---|---|
| 1 | Variant flat lay, one colour per frame | Merchant Center main image, PDP swatch | From directly above, plain oat/off-white background, garment fills 75-90% of frame, no props, no text |
| 2 | On-body front | PDP hero, ads | Real person, natural light, neutral backdrop; record model height + size worn |
| 3 | On-body side + back | PDP, fit | Same light and pose height as #2 |
| 4 | Detail: rib / cuff / neckline / seam | PDP, Reels stills | Macro, raking side light to show stitch texture; hand-finished seams if relevant |
| 5 | Scale / fit cue | PDP, size questions | Hand in pocket, sleeve length at wrist, beanie fold |
| 6 | Lifestyle (Riga, home, studio) | Instagram, Pinterest, email | Warm neutrals, garment colour still true |
| 7 | Ghost mannequin (optional) | Clean shape for cardigans/vests | Only if a mannequin is available; shoot inside neck separately for the composite; skip for very loose pieces |
| 8 | Making-of still | Founder story, About | Machine, yarn cone, Kristine's hands |

## Technical spec

- Light: large window daylight or one soft continuous light + white reflector; avoid mixed light sources.
- Colour: grey card or white paper in the first frame of each colour; set white balance from it.
- Background: plain oat/off-white; off-white or light grey for cream/white garments.
- Prep: steam, lint-roll, check pilling and loose threads before shooting.
- Files: largest JPG or RAW; export 2000 px long edge minimum (Google minimum 500x500, recommends ~1500).
- Naming: `[product-slug]_[colour]_[shot#]_[YYYYMMDD].jpg` (lowercase, hyphens). One colour per file.
- Crops: 4:5 (PDP/feed), 1:1, 9:16 (Stories/Reels), 2:3 (Pinterest). Plan composition with space for all.
- Merchant Center image: no text, logos, watermarks, price, borders or multi-colour group shots.

## Shoot brief template

```
# Shoot brief — [date] — DRAFT
Goal: [e.g. 11 turtleneck colour flat lays for Merchant Center + 3 on-body]
SKUs and colours (only physically available): [table: product | colour | shots # | done]
Location / light: [studio window, time of day]
People: [model name, height, size worn, consent signed: yes/no]
Props: [none for #1; list for lifestyle]
Reference look: aw-brand-voice s5; DESIGN-DIFF-REPORT colours
Deliverables: [count, crops, naming, folder]
Owner time: [hours]   Who uploads to Squarespace: OWNER (product data frozen for agents)
Claim check: no on-image text, true colour confirmed against garment in daylight
```

## Allowed vs not allowed edits (AI or manual)

| Allowed | Not allowed |
|---|---|
| Exposure, white balance, crop, straighten | Changing garment colour, pattern, texture, shape, length or fit |
| Remove dust, lint, background marks | Removing pilling, holes or flaws that the real garment ships with |
| Background cleanup / replace with plain oat | Generating a garment, colourway or model that was not photographed |
| Resize, export crops | "Recolouring" one photo to fake a missing colour variant |
| AI concept moodboards (internal, labelled AI) | Using AI images as product photos or in ads as if real |

Any image with generative AI content: keep the AI metadata (Google requires IPTC DigitalSourceType for
AI-generated images), label it internally `AI-CONCEPT`, never upload to Merchant Center or a PDP. EU AI Act
Article 50 transparency duties apply from 2 Aug 2026; interpretation for product imagery is unsettled, so
default to no AI-generated product visuals at all.

## Hand-off

Save brief + shot list to `business-os/` or `campaign-assets/drafts/`. Photos go to the owner; the owner
uploads variant images in Squarespace (Inventory -> Variants -> EDIT ALL -> Upload variant image). Agents never
edit products or the feed.

## Sources

- Google Merchant Center, Image link [image_link] spec (official; facts only), https://support.google.com/merchants/answer/6324350
  : per-variant images, exact colour, 75-90% framing, no promo text/watermarks, AI metadata, size minimums.
- Shopify blog, Clothing photography (all rights reserved; facts only, own words), https://www.shopify.com/in/blog/clothing-photography
  : shot types (flat lay, model, mannequin, lifestyle, close-up, angles), garment prep, backdrop for light colours.
- Astria, Ghost mannequin photography (vendor blog; facts only), https://www.astria.ai/articles/ghost-mannequin-photography-ecommerce/
  : composite method, inside-neck shot, which garments suit it.
- rampstackco/claude-skills `art-direction` (MIT), https://github.com/rampstackco/claude-skills
  : brief layers (required vs optional shots, deliverable formats, things to avoid, consent/usage up front).
- Lewis Silkin, EU AI labelling rules (law-firm commentary, not legal advice), https://www.lewissilkin.com/insights/2026/07/24/the-eus-new-ai-labelling-rules-what-every-organisation-needs-to-know-102ne35
- Backlog: `owner-action-pack-2026-10-19.md` A; `PROJECT-HANDBOOK.md` s8.
