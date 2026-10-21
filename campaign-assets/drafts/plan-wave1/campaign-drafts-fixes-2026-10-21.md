DRAFT — for owner approval

# Fixes for the 6 existing organic drafts (CRE-05)

Source file reviewed, **not edited**: `campaign-assets/campaign-drafts.md` (3 Pinterest, 3 Instagram, images in
`campaign-assets/drafts/`). Below: what fails the brand-voice / master-plan rules and a replacement version for each.
If the owner approves, these replacements are the versions to post; the original file stays as the record.

## Issues that apply to all 6

| # | Issue | Rule | Fix |
|---|---|---|---|
| 1 | UTM uses `utm_medium=organic_social`, `utm_campaign=winter_knitwear`, underscores in `utm_content` | Ruling C15: one taxonomy, lowercase, hyphens, owned by Growth (`business-os/growth/utm-links.csv`, approve 31 Oct) | Provisional: `utm_medium=social`, `utm_campaign=autumn-2026`, hyphenated content IDs. Swap to Growth's names when approved |
| 2 | Account ownership | Decision 18 (31 Oct). Footer Instagram was unified to `@autumnandwool` (implementation-report, 18 Oct); Pinterest is still `mmareshop` | No Pinterest drafts go live until the owner confirms the Pinterest account. Instagram after confirmation |
| 3 | Image provenance | Decision 16: rights of the "ChatGPT Image" assets on the store. Drafts say images are copies of live product photos | Owner confirms each of the 6 images is a real photo of the real garment before use (`[VERIFY]` per image) |
| 4 | Promotion gate | G2: only SKUs on Production's safe-to-promote list | Product pins (beanie, set, vest) HOLD until listed. Vest stock is 1 (owner pack B2): post only if it is still in stock that day |
| 5 | Fibre wording | Brand voice s3: copy from each live page, never generalise | Product drafts below use live wording read 21 Oct |

## Pinterest 1 — Beanie (HOLD: G2, Pinterest account)

Image: `drafts/pinterest-beanie.jpg` `[VERIFY: real photo, colour shown has a variant on the page]`
Title: Rib-Knit Merino Beanie, One Size
Description: Medium-thick rib with gentle stretch, 100% extra-fine merino wool. One size, fits 54–58 cm heads.
From Autumn & Wool, Riga [CLAIM-CHECK G8]. Colours, care and delivery details on the product page.
URL: https://www.autumnandwool.com/shop/p/p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1?utm_source=pinterest&utm_medium=social&utm_campaign=autumn-2026&utm_content=pin-beanie
Change: "wool beanie" -> exact live fibre; added fit fact; UTM per issue 1.

## Pinterest 2 — Hat and scarf set (HOLD: G2, Pinterest account)

Image: `drafts/pinterest-hat-scarf-set.jpg` `[VERIFY: real photo]`
Title: Merino Wool Hat and Scarf Set
Description: Rib-knit beanie and scarf in 100% extra-fine merino wool. Beanie fits 54–58 cm heads; scarf about
190 × 36 cm. Colours on the product page.
URL: https://www.autumnandwool.com/shop/p/p/merino-wool-hat-scarf-set-extra-fine-rib-knit-soft-on-skin-warm-not-bulky-unisex-gift?utm_source=pinterest&utm_medium=social&utm_campaign=autumn-2026&utm_content=pin-hat-scarf-set
Change: dropped "Winter Gift Idea" from the title until gift-season gates clear (G4/G5); added measurements from the
live page. No "RWS"/"mulesing-free" (old export wording; banned, and gone from the live page).

## Pinterest 3 — Sweater vest (HOLD: G2, stock 1, Pinterest account)

Image: `drafts/pinterest-vest.jpeg` `[VERIFY: real photo]`
Title: Oversized Merino V-Neck Sweater Vest
Description: Relaxed V-neck vest in 100% extra-fine merino wool. Laid flat: width 59 cm, length 68 cm. Layer it over a
shirt or turtleneck. Measurements on the product page.
URL: https://www.autumnandwool.com/shop/p/oversized-merino-wool-v-neck-sweater-vest?utm_source=pinterest&utm_medium=social&utm_campaign=autumn-2026&utm_content=pin-vest
Change: exact fibre and measurements from the live page; stock check on posting day (stock 1). Duplicate beige vest
listings exist (owner pack B2): this link is the public merino vest only.

## Instagram 1 — Cooler layers (main fix: banned hashtag)

Image: `drafts/instagram-cooler-layers.jpg` `[VERIFY: real photo]`
Caption:
Cooler days, easy layers.
Knitwear and accessories from our studio in Riga [CLAIM-CHECK G8]. Fibre and measurements are on every product page.
Link in profile.
#AutumnAndWool #RigaMade #KnitwearStyle
URL: https://www.autumnandwool.com/shop?utm_source=instagram&utm_medium=social&utm_campaign=autumn-2026&utm_content=ig-cooler-layers
Change: **removed `#SlowStyle`** (slow-fashion claim hashtag, banned); removed "wool knitwear" generalisation
(some catalogue items are blends or other fibres); 4 hashtags -> 3. Pillar: general, no product named, so it can
go before G2 once the account is confirmed.

## Instagram 2 — Winter accessories (HOLD: G2 for beanie and set)

Image: `drafts/instagram-winter-accessories.jpg` `[VERIFY: real photo]`
Caption:
A rib-knit beanie and a matching hat and scarf set, both in 100% extra-fine merino wool.
Colours, fit and care on each product page. Link in profile.
#AutumnAndWool #MerinoKnit #WinterAccessories
URL: https://www.autumnandwool.com/shop?utm_source=instagram&utm_medium=social&utm_campaign=autumn-2026&utm_content=ig-winter-accessories
Change: exact fibre from both live pages; removed em-dash phrasing; hashtags kept at 3.

## Instagram 3 — Easy layers (fix: 4 hashtags)

Image: `drafts/instagram-easy-layers.jpeg` `[VERIFY: real photo]`
Caption:
Easy layers for cooler days: a relaxed sweater vest over a shirt, a long cardigan over everything.
Measurements and care on each product page. Link in profile.
#AutumnAndWool #SweaterVest #WoolCardigan
URL: https://www.autumnandwool.com/shop?utm_source=instagram&utm_medium=social&utm_campaign=autumn-2026&utm_content=ig-easy-layers
Change: 4 hashtags -> 3 (dropped `#KnitwearStyle`). Names a vest and long cardigan, so HOLD until both are on the
safe list; vest stock 1.

## Sources

`campaign-assets/campaign-drafts.md`; `implementation-report.md` (18 Oct: Instagram footer unified, claims removed);
live product pages read 2026-10-21 (beanie, hat & scarf set, vest); `owner-action-pack-2026-10-19.md` B2;
`plans/2026-2027/master-plan.md` G2, G8, C15, decisions 16, 18; `.claude/skills/aw-brand-voice/SKILL.md` s2-s3.

## Claim check result

Pass after fixes: no banned claims or claim hashtags; fibre wording copied from live pages; max 3 hashtags; no
exclamation marks; no price, stock or delivery promise in captions.

## Open [VERIFY] / CLAIM-CHECK

- Each of the 6 images is a real photo of the real garment (decision 16).
- Pinterest account and Instagram ownership (decision 18).
- "studio in Riga" / "Riga" wording (G8, decision 16).
- Vest stock on posting day; beanie/set/vest on the safe-to-promote list (G2).
