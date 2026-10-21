# UTM fix for campaign-assets/campaign-drafts.md   Status: DRAFT for owner / Creative

Written 2026-10-21 by aw-growth-marketing. Proposal only: `campaign-drafts.md` is Creative's file and is not edited
here. Nothing is published. Landing pages checked to load on 2026-10-21 (beanie, hat & scarf set, vest, /shop).

## Decision: Growth adopts Creative's provisional names
Creative's fix file (`campaign-assets/drafts/plan-wave1/campaign-drafts-fixes-2026-10-21.md`, issue 1) already
replaces `organic_social` / underscores with `utm_medium=social`, `utm_campaign=autumn-2026` and hyphenated content
IDs. These comply with the taxonomy (`utm-taxonomy.md`). To avoid a second rename, Growth registers them as final in
`utm-links.csv` (rows `pinterest-pin-*`, `instagram-post-*`). **Creative does not need to swap anything.**

| Draft | Current (campaign-drafts.md) | Final (registered) |
|---|---|---|
| Pinterest 1, beanie | `utm_medium=organic_social&utm_campaign=winter_knitwear&utm_content=beanie` | `utm_medium=social&utm_campaign=autumn-2026&utm_content=pin-beanie` |
| Pinterest 2, hat and scarf set | `...winter_knitwear&utm_content=hat_scarf` | `...autumn-2026&utm_content=pin-hat-scarf-set` |
| Pinterest 3, vest | `...winter_knitwear&utm_content=vest` | `...autumn-2026&utm_content=pin-vest` |
| Instagram 1 | `...utm_content=cooler_layers` | `...autumn-2026&utm_content=ig-cooler-layers` |
| Instagram 2 | `...utm_content=winter_accessories` | `...autumn-2026&utm_content=ig-winter-accessories` |
| Instagram 3 | `...utm_content=easy_layers` | `...autumn-2026&utm_content=ig-easy-layers` |

Also registered from Creative's wave-1 drafts: campaigns `making-in-riga`, `mareshop-story`, `gift-2026`
(content = script ID, e.g. `vs-2026-10-21-a`). One gap to fix in Creative's captions file: rows `vs-2026-10-21-b/c/d`
and `pin-founder-1` show only `campaign=...&utm_content=...`; they need `utm_source` and `utm_medium=social` too.

## Notes for Creative
- Instagram captions don't make URLs clickable. Feed posts send people to the bio link, so their visits will show
  as `bio-link`. Post-level UTMs only work in Story link stickers. Rows are marked `draft-story-sticker-only`.
- Holds stay as Creative listed them: G2 (no SKU GREEN yet), decision 18 (account ownership), decision 16 (image rights).

Owner approval: [ ] (initials + date)
