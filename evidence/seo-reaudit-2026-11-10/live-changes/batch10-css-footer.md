# Batch 10: Custom CSS cookie bar (phone) + footer link removal attempt (2026-11-10)

ego-browser task space `aw-batch10-css-footer-2026-11-10` (spaceId 21), closed with finish({ keep: [] }).
Backups: evidence/seo-reaudit-2026-11-10/backup/custom-css-before-b10.css, custom-css-after-b10.css.
Public and measurement captures: evidence/seo-reaudit-2026-11-10/live-changes/b10/.

## TASK 1: Custom CSS cookie block - DONE (saved, public)
- Live Custom CSS before: 16954 chars (CodeMirror 5 instance). Cookie block (6 lines, `/* SEO audit 2026-11-10: compact cookie bar on phones...`) found exactly once, at line 288.
- Guards present in current text: `.sqs-widgets-confirmation-overlay{pointer-events:none !important;}` and `.sqs-widgets-confirmation{pointer-events:none !important;}`, both present.
- Replacement: block swapped for html/cookie-block.css (7 lines). Diff touches only that block. After: 17175 chars.
- Editor setValue, getValue equal to file, Save clicked (menuHeader-save), Save disappeared. Exited via Pages back.
- Public after 60 s: custom.css (static1 custom-css/.../custom.css) contains `gdpr-cookie-banner button ... height:36px !important` (1 match) and both guard rules in minified form (1 each). / 200, product page 200.

### Phone measurement (fresh headless Chrome profile, 390x844 mobile emulation, product page vest, 10 s)
| item | earlier today (batch3) | now |
|---|---|---|
| banner x,y,w,h | 0,699,390,145 | 0,709,390,135 |
| banner buttons | - | Accept all 95x36, Decline all 101x36, Manage cookies 133x36; all visible |
| banner text | - | 11px, y 717-792 |
| price (EUR 126.00) | y 710-741 | y 710-741 (still under banner top 709) |
| Add To Cart | y 757-805 | y 757-805 (still under banner) |
Result: banner is shorter and buttons are readable, so no revert. The CSS does NOT stop the banner covering price and Add To Cart on a first visit. Needs a different fix (owner decision).

## TASK 2: footer Facebook + Pinterest lines - FAILED, NOT SAVED
- Footer editor opened via footer overlay ("Edit Site Footer" button dispatched in the preview iframe). Text block (website.components.html, 5 paragraphs: Instagram, Tiktok, Facebook, Pinterest, Company Registration) read before any change: unchanged.
- Could not put the text block into text-edit mode. Tried: CDP single click and double-click on blank space right of the Facebook line, CDP double-click on the words Facebook and Instagram, dispatched pointer/click events on the text block. No contenteditable or ProseMirror appeared in the preview frame. Undo and Save stayed disabled throughout, so no change was made.
- Accidental side effect: one early CDP click landed on the "Company Registration" link and opened company.lursoft.lv as a new tab (p2). Closed it. No page change.
- Footer editor closed with Exit (frameToolbarCancel). No dialog appeared.
- Note on batch8: the batch8 unsaved deletion did not appear in this admin session. The footer showed all five lines when opened, and the public site still has the five lines.

## Public check (current state, nothing saved for footer)
| page | status | AccessoriesMareshop | mmareshop | lursoft | instagram.com/autumnandwool | tiktok.com/@autumnandwool |
|---|---|---|---|---|---|---|
| / | 200 | 1 | 1 | 1 | 12 | 6 |
| /about | 200 | 1 | 1 | 1 | 6 | 6 |
| /shop | 200 | 1 | 1 | 1 | 6 | 6 |
Target was 0/0/1/>=1/>=1 after the footer save. Not met because the footer was not changed.
