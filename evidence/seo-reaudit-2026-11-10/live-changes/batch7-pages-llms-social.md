# Batch 7: pages, llms.txt, privacy, social links (2026-11-10)

Site: https://www.autumnandwool.com (Squarespace 7.1, admin rose-tarpon-ld9w). ego-browser task space `aw-batch7-pages-2026-11-10` (spaceId 18), closed with finish({ keep: [] }).
Source: business-os/seo-marketplace/live-2026-11-10-b. Backups: evidence/seo-reaudit-2026-11-10/backup/.

## TASK 1: wool Code blocks (4 pages) - DONE
- Each page: editor text read in chunks and saved to backup/<slug>-codeblock-before-b7.html. Equal to before/<slug>.html after trailing-whitespace normalisation (raw equal too): yes for all 4.
- Old -> new: wool-sweaters 9278 -> 9879 chars; wool-cardigans 5612 -> 5907; wool-sweater-vests 4711 -> 4938; wool-hats-and-scarves 4695 -> 4921.
- CM6 select-all + synthetic paste; editor text == file for all 4. Save greyed, Exit, no dialogs.
- Public check (after ~30 s, curl UA Mozilla/5.0): all 200; one <h1 each; aw-price 13 / 4 / 2 / 2; aw-lead present; no src="http:// .
- /wool-gifts not touched.

## TASK 2: llms.txt - DONE
- Backup backup/llms-before-b7.txt = 7503 chars (7518 bytes), equal to before/llms.txt.
- Replaced with html/llms.txt (6661 chars / 6662 bytes). Save: dialog closed.
- Public after 60 s: 200 text/plain, 6662 bytes, contains wool-sweaters, does not contain /shop/cardigans).

## TASK 3: /privacy-policy Code block - DONE
- Backup backup/privacy-codeblock-before-b7.html (6088 chars). Needle "is a handmade knitwear brand" count 1.
- Replacement -> "is a knitwear brand". Length 6088 -> 6079 (-9). Editor == new text.
- Public: /privacy-policy 200; grep -o -i handmade = 0; "is a knitwear brand" = 1.

## TASK 4: Social Links - DONE (partial leftover in page text, see below)
- Before (backup/social-links-before-b7.txt): instagram.com/autumnandwool, tiktok.com/@autumnandwool, facebook.com/AccessoriesMareshop, pinterest.com/mmareshop/ (all Visible).
- Removed Facebook (REMOVE + CONFIRM "Are you sure you want to remove this link?") and Pinterest the same way. Instagram and TikTok kept.
- After reload: Social Links = instagram + tiktok only.
- Public home check (after ~45 s): facebook.com/AccessoriesMareshop count 1 (was 4), pinterest.com/mmareshop count 1 (was 4).
  Remaining occurrences are not social icons. Each is a hard-coded link in a text block:
  `...<p ...><a target="_blank" href="https://www.facebook.com/AccessoriesMareshop">Facebook</a></p><p...`
  and `...<a target="_blank" href="https://www.pinterest.com/mmareshop/">Pinterest</a></p>`.
  Not edited (per instruction). Owner to remove those text-block links if wanted.

## TASK 5: per-category SEO description - NO FIELD, NOT CHANGED
- Pages > Shop > Page settings > Store Settings > Categories > Cardigans > EDIT shows only NAME, URL SLUG, Enable Page, Filter Visibility, Add to main navigation. No SEO description.
- Store Settings > SEO tab holds one store-level SEO title and description (Shop page) only. Not changed.
- Nothing saved. Store Settings closed without edits.

## Final checks
- / 200, /shop 200, /wool-sweaters 200, /privacy-policy 200, /llms.txt 200 (6662 bytes).

## Notes
- Several "Save" clicks were sent at computed coordinates; each save was verified by Save greyed out. Public checks above confirm the saved content for Tasks 1-3.
- Editor used for code blocks: section overlay in preview frame; block selected via dispatched pointer events (elementFromPoint in preview frame). No Delete/Discard/Upgrade choices made except the approved social-link removal confirmations.
