# Batch 2: new live pages (2026-11-10)

Site: www.autumnandwool.com (Squarespace 7.1, admin rose-tarpon-ld9w). Browser: ego-browser task space 7 (`aw-batch2-newpages-2026-11-10-a`).
Source: `business-os/seo-marketplace/live-2026-11-10/html/` (index.tsv + one HTML file per page). Code block content pasted byte-for-byte (9301 chars editor = 9301-byte file for the pilot).

## Result summary

| # | slug | created | settings set | section + code block | public 200 | h1 | size (bytes) | notes |
|---|------|---------|--------------|----------------------|-----------|----|--------------|-------|
| 1 (pilot) | /wool-sweaters | yes | yes (title, nav, slug, SEO title, SEO description; hide-from-search off; enabled) | yes (one blank section, one Code block, HTML mode, display source off) | 200 | 1 | 211054 | title, meta description, marker, mid sentence, last link "Shop the full collection" all verified |
| 2-9 | /wool-cardigans, /wool-sweater-vests, /wool-hats-and-scarves, /wool-gifts, /how-to-wash-a-wool-sweater, /merino-vs-lambswool, /oversized-fit-guide, /how-to-choose-a-wool-cardigan | NO | NO | NO | not created | - | - | Add Blank stopped creating pages after the pilot (see below) |

## Pilot detail (/wool-sweaters)
- Page created in Not Linked (group check: Not Linked). Blank page showed only "Add Page Content / ADD SECTION".
- Page settings: PAGE TITLE and NAVIGATION TITLE "Wool Sweaters, Oversized and Relaxed", URL SLUG "wool-sweaters", SEO TITLE "Wool Sweaters, Oversized and Relaxed | Autumn & Wool", SEO DESCRIPTION as index.tsv, "Hide Page from Search Results" unchecked, page enabled. Saved, read back in the SEO tab before save.
- Section: one blank section, Code block, Display Source Code off, pasted via synthetic ClipboardEvent. Saved (Save greyed out), exited.
- Public check (curl -A "Mozilla/5.0", ~30 s after save):
  - status 200, size 211054 bytes
  - `<title>` = "Wool Sweaters, Oversized and Relaxed | Autumn & Wool" (match)
  - meta description matches index.tsv (match)
  - `<h1` count 1
  - `aw-seo-page` count 16
  - `&lt;div class=` count 0 (no escaped markup)
  - demo/lorem text count 0
  - middle sentence from source found on page: yes
  - last link "Shop the full collection" found: yes

## Incidents
1. Add-page control. The Not Linked group "+" opens "Add a Page". The pilot page was created on the first attempt that clicked Add Blank in a freshly opened dialog. Afterwards, every Add Blank attempt (mouse click, hover then click, double click, DOM click, keyboard Enter, focus + Enter) left the dialog open and created nothing. Network capture on the click shows only analytics beacons (tracing.squarespace.com), no page-create request. After each attempt the page list was reloaded and counted: 17 entries (16 pre-existing + pilot), no stray "New Page" or "Untitled" page.
2. Header editor. While placing the section, a click opened the global "Editing Site Header" mode. Exit was chosen and the "Exit Without Saving?" prompt was answered with Exit (discard). Only unsaved draft changes were discarded (the blank section, re-added later). The header was not saved. Public home returns 200.
3. The batch stopped after the pilot as instructed (stop on unexpected behaviour). No other page was created, edited, moved or deleted.

## Post-batch checks
- https://www.autumnandwool.com/ : 200 (211691 bytes)
- https://www.autumnandwool.com/shop : 200 (933296 bytes)
- https://www.autumnandwool.com/sitemap.xml : 200 (76831 bytes), 39 `<loc>` entries. None of the 9 new URLs present (pilot /wool-sweaters not listed either).

## Follow-up: duplicate-based retry (coordinator instruction)

Fresh ego task space 8 (`aw-batch2-dup-2026-11-10-b`).

- Add Blank retried once after a full admin reload: no page created (list stays at 17 entries, no New Page or copy).
- Duplicate via pilot Page settings > General > DUPLICATE PAGE, three attempts:
  1. Mouse click on the button: no request, no copy.
  2. Hover, then mouse click with CDP network logging: only analytics beacons, no copy.
  3. DOM click on the button: the admin reloaded /config/pages, no duplicate request, no copy.
- Stop rule reached (3 failed duplicate attempts). No copy was created, so the duplicate-based steps (rename, slug, SEO, code block replacement, public verification) were not started for any of the 8 pages.
- Result: 8 of 8 remaining pages FAILED (not created): /wool-cardigans, /wool-sweater-vests, /wool-hats-and-scarves, /wool-gifts, /how-to-wash-a-wool-sweater, /merino-vs-lambswool, /oversized-fit-guide, /how-to-choose-a-wool-cardigan.
- The pilot was not saved or changed. The pilot panel was closed without saving each time.
- Pilot re-check at end: https://www.autumnandwool.com/wool-sweaters returns 200, 211054 bytes, one `<h1>` = "Wool sweaters for layering and everyday wear", title "Wool Sweaters, Oversized and Relaxed | Autumn &amp; Wool".
- Pages list at end: 17 entries (16 existing + pilot). Nothing else created, edited, or deleted.

## Follow-up 3: root cause found, remaining 8 pages created (ego task space 9, `aw-diag-newpages-2026-11-10-c`, now closed)

**Root cause (not a plan limit, no limit message exists):** in the "Add a Page" dialog, clicking "Add Blank" does not create a page. It opens a small second-step menu with two entries, "Page" and "Blog", directly under the Add Blank link. The page is only created after clicking "Page". The earlier attempts clicked Add Blank repeatedly (and the DOM/keyboard variants) and never clicked the submenu entry, so the dialog stayed open and no request fired. The submenu was easy to miss because it only shows on a real mouse click at the Add Blank coordinates and was never screenshotted. Evidence: `scratchpad/ego2/after.png` (submenu visible), `after2.png`/`after3.png` (page "New Page" created in Not Linked after clicking "Page"). Console: no errors. DUPLICATE PAGE was not retried (not needed).

Flow that works: Not Linked "+" > Add Blank > Page > Enter (accept inline name) > Page settings (title, nav title, slug, SEO title, SEO description) > SAVE > Edit > ADD SECTION > Add Blank section > ADD BLOCK > search "code" > Code > pencil > CodeMirror synthetic paste (editor text equals source file exactly) > Save > Exit.

| slug | public status | title/meta exact | h1 | aw-seo-page | last link "Shop the full collection" | escaped/lorem |
|---|---|---|---|---|---|---|
| /wool-cardigans | 200 | yes | 1 | yes | yes | 0 / 0 |
| /wool-sweater-vests | 200 | yes | 1 | yes | yes | 0 / 0 |
| /wool-hats-and-scarves | 200 | yes | 1 | yes | yes | 0 / 0 |
| /wool-gifts | 200 | yes | 1 | yes | yes | 0 / 0 |
| /how-to-wash-a-wool-sweater | 200 | yes | 1 | yes | yes | 0 / 0 |
| /merino-vs-lambswool | 200 | yes | 1 | yes | yes | 0 / 0 |
| /oversized-fit-guide | 200 | yes | 1 | yes | yes | 0 / 0 |
| /how-to-choose-a-wool-cardigan | 200 | yes | 1 | yes | yes | 0 / 0 |

Notes: all pages are in Not Linked, one section, one Code block (HTML mode). Two runs stopped mid-way (settings check bug, then a missed search-box focus); both were recovered without discarding anything or creating strays (merino page was saved with settings, then its content added on a second pass). One mistaken edit-mode entry on /wool-gifts was exited with Save greyed (no changes). Final /, /shop, /wool-sweaters: 200.
