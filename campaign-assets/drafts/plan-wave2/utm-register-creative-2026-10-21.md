DRAFT — for owner approval

# Creative UTM register, aligned to Growth's taxonomy v1 (CRE-17)

Written 2026-10-21 (wave 2) by aw-creative-content. This register applies Growth's single taxonomy
(`business-os/growth/utm-taxonomy.md`, `business-os/growth/utm-links.csv`, ruling C15) to every Creative draft.
It replaces the "provisional" UTM notes in `plan-wave1/`. Wave-1 files are not edited. When a wave-1 link and this
register differ, **this register wins**. Nothing is live. The owner approves the scheme as part of decision 18 (31 Oct).

## 1. Rules applied (from Growth, section 2-3)

- Organic post, Reel or pin: `utm_source=<instagram|tiktok|pinterest|facebook>&utm_medium=social`.
- `utm_campaign` = registered theme: `autumn-2026`, `gift-2026`, `making-in-riga`, `mareshop-story`. New themes
  proposed below (section 4) need Growth to register them first.
- `utm_content` = Creative script ID (`vs-YYYY-MM-DD-x`) or `<format>-<sku-slug>`. TikTok and Instagram versions
  of the same video keep the same `utm_content`; `utm_source` tells them apart.
- Bio links: `campaign=bio-link`, no content (exactly as `utm-links.csv` rows 2-5). Stories link stickers use the
  bio-link row for that platform unless a post-specific row exists.
- Lowercase, hyphens only. No UTMs on internal site links.

## 2. Wave-1 drafts: status after alignment

| Draft ID (file) | Wave-1 link | Matches taxonomy? | Final full URL | In `utm-links.csv`? |
|---|---|---|---|---|
| vs-2026-10-21-a IG (video-scripts, captions) | making-in-riga / vs-2026-10-21-a | Yes | `https://www.autumnandwool.com/shop?utm_source=instagram&utm_medium=social&utm_campaign=making-in-riga&utm_content=vs-2026-10-21-a` | Yes (row 13) |
| vs-2026-10-21-a TikTok | same, source tiktok | Yes | `https://www.autumnandwool.com/shop?utm_source=tiktok&utm_medium=social&utm_campaign=making-in-riga&utm_content=vs-2026-10-21-a` | Yes (row 14) |
| vs-2026-10-21-b IG (beanie texture) | captions row lacked source/medium | Fixed here | `https://www.autumnandwool.com/shop/p/p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1?utm_source=instagram&utm_medium=social&utm_campaign=autumn-2026&utm_content=vs-2026-10-21-b` | No: propose (section 3) |
| vs-2026-10-21-b TikTok | — | Fixed here | same URL with `utm_source=tiktok` | No: propose |
| vs-2026-10-21-c IG (turtleneck answer) | captions row lacked source/medium | Fixed here | `https://www.autumnandwool.com/shop/p/p/merino-wool-turtleneck-sweater-womens-knit-pullover-soft-warm-lightweight-minimalist-sustainable-knitwear-sizes-sl-12-679428?utm_source=instagram&utm_medium=social&utm_campaign=autumn-2026&utm_content=vs-2026-10-21-c` | No: propose |
| vs-2026-10-21-c TikTok | — | Fixed here | same URL with `utm_source=tiktok` | No: propose |
| vs-2026-10-21-d IG (founder) | mareshop-story / vs-2026-10-21-d | Yes | `https://www.autumnandwool.com/shop?utm_source=instagram&utm_medium=social&utm_campaign=mareshop-story&utm_content=vs-2026-10-21-d` | Yes (row 15) |
| vs-2026-10-21-d TikTok | — | Fixed here | same URL with `utm_source=tiktok` | No: propose |
| pin-beanie, pin-hat-scarf-set, pin-vest (fixes file) | autumn-2026 | Yes | as `utm-links.csv` rows 7-9 | Yes |
| ig-cooler-layers, ig-winter-accessories, ig-easy-layers | autumn-2026 | Yes | as rows 10-12 (story sticker only) | Yes |
| pin-making-1 (captions) | making-in-riga / pin-making-1 | Yes | `https://www.autumnandwool.com/shop?utm_source=pinterest&utm_medium=social&utm_campaign=making-in-riga&utm_content=pin-making-1` | No: propose |
| pin-founder-1 (captions) | lacked source/medium | Fixed here | `https://www.autumnandwool.com/shop?utm_source=pinterest&utm_medium=social&utm_campaign=mareshop-story&utm_content=pin-founder-1` | No: propose |
| gs-a (gift beanie, IG + TikTok) | gift-2026 / gs-a | Content ID renamed for clarity | `https://www.autumnandwool.com/shop/p/p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1?utm_source=instagram&utm_medium=social&utm_campaign=gift-2026&utm_content=gs-a-beanie` | No: propose |
| gs-b (gift set, IG + TikTok) | gift-2026 / gs-b | Renamed | `https://www.autumnandwool.com/shop/p/p/merino-wool-hat-scarf-set-extra-fine-rib-knit-soft-on-skin-warm-not-bulky-unisex-gift?utm_source=instagram&utm_medium=social&utm_campaign=gift-2026&utm_content=gs-b-hat-scarf-set` | No: propose |
| gift-pin-beanie / gift-pin-hat-scarf-set | lacked source/medium | Fixed here | beanie / set PDP + `?utm_source=pinterest&utm_medium=social&utm_campaign=gift-2026&utm_content=gift-pin-beanie` (or `gift-pin-hat-scarf-set`) | No: propose |
| gift-pin-category | — | Fixed here | `https://www.autumnandwool.com/shop/winter-wool-gifts?utm_source=pinterest&utm_medium=social&utm_campaign=gift-2026&utm_content=gift-pin-category` | No: propose `[VERIFY URL loads]` |
| st-2026-10-27 (Stories) | bio link | Yes | `utm-links.csv` row 2 (instagram bio-link) | Yes |

## 3. Rows proposed for Growth to add to `utm-links.csv`

Growth owns the CSV. These are proposals in the CSV's own column order, status `draft-proposed-by-creative`.
Creative does not edit the file.

```
created,owner,placement,landing_url,utm_source,utm_medium,utm_campaign,utm_content,full_url,discount_code,status
2026-10-21,aw-creative-content,reel-beanie-texture-b,https://www.autumnandwool.com/shop/p/p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1,instagram,social,autumn-2026,vs-2026-10-21-b,<landing>?utm_source=instagram&utm_medium=social&utm_campaign=autumn-2026&utm_content=vs-2026-10-21-b,,draft-hold-g2
2026-10-21,aw-creative-content,tiktok-beanie-texture-b,<same landing>,tiktok,social,autumn-2026,vs-2026-10-21-b,<landing>?utm_source=tiktok&...,,draft-hold-g2
2026-10-21,aw-creative-content,reel-turtleneck-answer-c,https://www.autumnandwool.com/shop/p/p/merino-wool-turtleneck-sweater-womens-knit-pullover-soft-warm-lightweight-minimalist-sustainable-knitwear-sizes-sl-12-679428,instagram,social,autumn-2026,vs-2026-10-21-c,<landing>?utm_source=instagram&...,,draft-hold-g2-and-size-fix
2026-10-21,aw-creative-content,tiktok-turtleneck-answer-c,<same landing>,tiktok,social,autumn-2026,vs-2026-10-21-c,<landing>?utm_source=tiktok&...,,draft-hold-g2-and-size-fix
2026-10-21,aw-creative-content,tiktok-mareshop-story-d,https://www.autumnandwool.com/shop,tiktok,social,mareshop-story,vs-2026-10-21-d,...,,draft-hold-decision-17-20
2026-10-21,aw-creative-content,pinterest-pin-making-1,https://www.autumnandwool.com/shop,pinterest,social,making-in-riga,pin-making-1,...,,draft-hold-decision-18-g8
2026-10-21,aw-creative-content,pinterest-pin-founder-1,https://www.autumnandwool.com/shop,pinterest,social,mareshop-story,pin-founder-1,...,,draft-hold-decision-17-18-20
2026-10-21,aw-creative-content,reel-gift-beanie-gs-a,<beanie PDP>,instagram,social,gift-2026,gs-a-beanie,...,,draft-hold-g2-g4-g5
2026-10-21,aw-creative-content,reel-gift-hat-scarf-gs-b,<set PDP>,instagram,social,gift-2026,gs-b-hat-scarf-set,...,,draft-hold-g2-g4-g5
2026-10-21,aw-creative-content,pinterest-gift-pin-beanie,<beanie PDP>,pinterest,social,gift-2026,gift-pin-beanie,...,,draft-hold-g2-decision-18
2026-10-21,aw-creative-content,pinterest-gift-pin-hat-scarf-set,<set PDP>,pinterest,social,gift-2026,gift-pin-hat-scarf-set,...,,draft-hold-g2-decision-18
2026-10-21,aw-creative-content,pinterest-gift-pin-category,https://www.autumnandwool.com/shop/winter-wool-gifts,pinterest,social,gift-2026,gift-pin-category,...,,draft-verify-url
```

TikTok versions of gs-a / gs-b: same rows with `utm_source=tiktok`. Wave-2 drafts (section 4) add their own rows
in the same pattern; each wave-2 file lists its IDs.

## 4. New campaign themes proposed (Growth to register before use)

| Proposed `utm_campaign` | Used by | Why not an existing theme |
|---|---|---|
| `black-friday-2026` | `black-friday-edit-2026-11-27.md` | Lets the WBR read the BF week separately; no code, no discount |
| `christmas-cutoff-2026` | `december-gift-peak-prep-2026-10-21.md` (CRE-22 posts) | Order-by reminders behave differently from gift browsing |
| `care-and-mend` (standing series, no date) | reset weeks, Q1 2027 | Evergreen care content |
| `reset-2026-12` | year-in-review, 2027 teaser | One-off |

If Growth prefers fewer themes, fall back to `gift-2026` for the first two and `making-in-riga` for the rest.

## 5. Conflict for Growth and SEO (not changed by Creative)

SEO's Pinterest plan (`business-os/seo-marketplace/2026-10-21-pinterest-plan.md` line 29) uses
`utm_campaign=<board-slug>` (e.g. `wool-beanies`). Growth's taxonomy uses a theme (`autumn-2026`). Same pin, two
names. Proposal: keep Growth's theme in `utm_campaign`, put the pin ID in `utm_content` (`p8-beanie`), and record the
board in the CSV `placement` column (`pinterest-board-wool-beanies-p8`). Growth decides; SEO and Creative follow.

## Sources

`business-os/growth/utm-taxonomy.md` s2-5; `business-os/growth/utm-links.csv` rows 2-30;
`campaign-assets/drafts/plan-wave1/` video-scripts, captions, gift-season, campaign-drafts-fixes (2026-10-21);
`business-os/seo-marketplace/2026-10-21-pinterest-plan.md` s Boards; master plan ruling C15, decision 18.

## Claim check result

Pass. Links and IDs only; no product claims added. Live slugs copied as they are (the turtleneck slug contains
"sustainable": that is the live URL, not copy, and must not be quoted in captions).

## Open [VERIFY]

- `/shop/winter-wool-gifts` loads with the query string intact (check before the owner pastes it).
- Owner approves the scheme (decision 18, 31 Oct); Growth registers section 3 and 4 rows.
