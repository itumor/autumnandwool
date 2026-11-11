# Batch 15: Newsletter signup moved to /newsletter, footer form removed (2026-11-11)
Task space aw-batch15-newsletter-2026-11-11 (spaceId 35), closed with finish({ keep: [] }). All steps DONE, saved, verified publicly.

## Step A (read-only) - footer Newsletter block settings - DONE
Footer editor opened, block settings read, exited with no change (Save stayed disabled, no dialog).
- Content: Form Name "Newsletter Form 2"; Title empty; Description "Get new knits, restocks and gift ideas from Riga. A few emails a season, no spam."; Disclaimer empty; Button Text "Sign Up"; Show Name Field off.
- Post-Submit: Message mode, text "Thank you!", HTML box empty.
- Design: Layout Float, alignment left, Background off, Stroke none, Blend Normal, Blur off.
- Storage: Squarespace (Contacts); Add to mailing list = None; Send Confirmation Email off; Google reCAPTCHA ON. No other storage connected.
- Screenshot: screenshots/b15-footer-before.jpg
- Footer text block before (Instagram block): Instagram -> instagram.com/autumnandwool | Tiktok -> tiktok.com/@autumnandwool | Company Registration -> company.lursoft.lv/en/autumn-and-wool/40203644965

## Step B - page + block - DONE
- Copy/paste of the block was not practical (settings panel covered the block, Cmd+C did nothing visible). Block REBUILT as a fresh Newsletter block.
- Page: Pages > Not Linked > + > Add Blank > Page, titled "Newsletter", slug /newsletter (confirmed in preview path), published, not in main nav.
- Content: one text block with H1 "Join the newsletter" and paragraph "New pieces, restocks and the occasional offer. No spam, unsubscribe any time."; one Newsletter block below it.
- New block settings set to match footer: Title empty, Description same as footer text, Disclaimer cleared (default was "We respect your privacy."), Button "Sign Up", name field off, Post-Submit "Thank you!" (default already same), alignment set to left (default was centre), Layout Float, Storage Squarespace / list None / confirmation off / reCAPTCHA on (defaults, verified identical). Only differences: Form Name "Newsletter Form 4" vs "Newsletter Form 2" (auto), placement.
- Note: block description duplicates the gist of the page line (kept to match "exactly like footer").
- Block was positioned under the text with arrow keys (mouse drag did not work). Saved, exited.

## Step C - public check - DONE
/newsletter: 200; sqs-block-newsletter matches 2 right after save (footer block still present then), 1 after Step E; "Join the newsletter" 1.

## Step D - footer link - DONE
Footer text block after (4 lines): Instagram | Tiktok | Company Registration | Join our newsletter (href="/newsletter", page link picked from suggestion). Added as last line; original three links unchanged. Saved, exited no dialog.
Public home: 200, href="/newsletter" 1, Join our newsletter 1.

## Step E - delete footer Newsletter block - DONE
Before saving, checked: only the newsletter block gone, all 5 text blocks intact. Saved.
Public after: home 200: sqs-block-newsletter 0, href="/newsletter" 1, instagram.com/autumnandwool 12, tiktok.com/@autumnandwool 6, lursoft 1. /newsletter 200: sqs-block-newsletter 1.
Footer look: empty space on the right where the form was (no redesign). Screenshots: b15-footer-after-desktop.jpg, b15-footer-after-390.jpg, b15-newsletter-page-desktop.jpg.

## Unexpected / unverified
- Two early clicks opened Section Design panel instead of the block (no change made; Escape closed it).
- Home HTML still contains the word "recaptcha" 2x (site-config recaptchaEnterpriseContext key, also on /newsletter). Whether the reCAPTCHA script itself still loads on home was NOT checked (no network trace).
- No form submission made. Mobile 390 footer screenshot saved but only the desktop ones were visually reviewed.
