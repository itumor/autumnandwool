# Batch 8: four guide Code blocks + footer links (2026-11-10)

ego-browser task space `aw-batch8-guides-2026-11-10` (spaceId 19). Left OPEN (not finished) because the footer editor holds an unsaved, unintended change. See Task 2.
Source: business-os/seo-marketplace/live-2026-11-10-b. Backups: evidence/seo-reaudit-2026-11-10/backup/.

## TASK 1: guide Code blocks (4 pages) - DONE, saved, verified publicly
Method: admin Pages > page > page-level Edit > pointer events on code block in preview iframe > block Edit > CodeMirror 6 (read via cmTile.parent chain). Live text compared to before/<slug>.html (trailing-whitespace normalised) before any change. Paste = synthetic ClipboardEvent on .cm-content after select-all; editor text === html/<slug>.html; Save; Exit (no dialogs).

| page | before -> after (chars) | backup | saved | public (curl UA Mozilla/5.0, ~30 s) |
|---|---|---|---|---|
| /how-to-wash-a-wool-sweater | 4989 -> 6577 | backup/how-to-wash-a-wool-sweater-codeblock-before-b8.html | yes | 200; h1=1; aw-byline=1; table=1; "Updated 10 November 2026"=1; src="http:// =0 |
| /merino-vs-lambswool | 5371 -> 7638 | backup/merino-vs-lambswool-codeblock-before-b8.html | yes | 200; h1=1; aw-byline=1; table=1; updated=1; http src=0 |
| /oversized-fit-guide | 5065 -> 7210 | backup/oversized-fit-guide-codeblock-before-b8.html | yes | 200; h1=1; aw-byline=1; table=1; updated=1; http src=0 |
| /how-to-choose-a-wool-cardigan | 5301 -> 7288 | backup/how-to-choose-a-wool-cardigan-codeblock-before-b8.html | yes | 200; h1=1; aw-byline=1; table=1; updated=1; http src=0 |

Skipped: none. Size deltas are chars (file bytes differ where text has multi-byte characters).

## TASK 2: site footer - STOPPED, NOT SAVED
- Footer editor opened from Home preview (EDIT SITE FOOTER, dispatched events). Footer text block (website.components.html) read before any change: backup/footer-links-before-b8.txt. The block has FIVE paragraphs, not four: Instagram, Tiktok, Facebook, Pinterest, and "Company Registration" (https://company.lursoft.lv/en/autumn-and-wool/40203644965). The Company Registration line was not in the task; it was to be kept.
- Attempted: DOM selection from start of "Facebook" paragraph to start of "Company Registration" paragraph, then Delete key. Intended result: only Facebook and Pinterest paragraphs removed.
- Actual result in the editor DOM: the whole footer text block (Instagram, Tiktok, Facebook, Pinterest, Company Registration) disappeared from the editor. Admin now shows Save enabled (unsaved change). STOPPED here. Save NOT clicked. Exit NOT clicked (would offer Discard).
- Public check after the stop (live site untouched because nothing was saved): / has AccessoriesMareshop=1, mmareshop=1, lursoft=1, >Tiktok< text=1.
- Owner action needed: in the open admin editor (task space aw-batch8-guides-2026-11-10), Exit and choose Discard, or undo the deletion, before anything else is saved. Do not Save that footer editor as it stands.
- Not done: the footer edit, the public footer checks (60 s), the /contact check of the footer change.

## /contact observation (no edit)
- Current live /contact: AccessoriesMareshop count = 2 (saved copy: backup/contact-check-b8.html). Second occurrence is not in the footer: `...<a href="https://www.pinterest.com/mmareshop/">Pinterest</a><a href="https://www.facebook.com/AccessoriesMareshop">Facebook</a></div>` (a link group on the Contact page, no target attribute). Not edited.

## Final status curls (2026-11-10)
/ 200, /shop 200, /how-to-wash-a-wool-sweater 200, /merino-vs-lambswool 200, /oversized-fit-guide 200, /how-to-choose-a-wool-cardigan 200, /contact 200.
