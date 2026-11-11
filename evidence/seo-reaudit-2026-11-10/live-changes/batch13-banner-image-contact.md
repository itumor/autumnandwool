# Batch 13 live changes (2026-11-11): wool-gifts, contact, cookie banner, social image

Task space: aw-batch13-2026-11-11 (spaceId 27). Public checks use UA Mozilla/5.0.

| Task | Result | Backup / evidence | Public check |
|---|---|---|---|
| 1 /wool-gifts Code block | DONE. Live text == before file (5654 chars). Replaced with html/wool-gifts.html (5684 chars), editor == file, Saved | backup/wool-gifts-codeblock-before-b13.html | 200; h1=1; "unwashed items in their original condition"=yes; "unused items"=no |
| 2 /contact Code block | DONE. Needle count 1. Removed Pinterest + Facebook anchors. Old 4176, new 4049, delta 127 (brief said 131; the given string is 127 chars, removed exactly as given) | backup/contact-codeblock-before-b13.html | 200; h1=1; AccessoriesMareshop=0; mmareshop=0; instagram.com/autumnandwool=8; `<form` = 2 (same as before) |
| 3 Cookie banner disclaimer | DONE. Disclaimer replaced with the requested text, links /privacy-policy and /cookie-policy kept. Imprint link removed (not in requested text). Toggles, buttons, layout not touched. Saved (toast "Saved") | backup/cookie-banner-before-b13.txt | phone CDP measurement below |
| 4 Social sharing image | DONE. Replaced site-wide image a2ce269e-...png with social-image-1200x630.jpg via REPLACE > Upload File, SAVE | backup/social-image-before-b13.txt (the recorded URL is the 100w variant of the same file) | `/`: og:image = .../social-image-1200x630.jpg?format=1500w, og:image:width 1200, og:image:height 630, twitter:image same |
| 5 Header logo alt | PLATFORM. Public siteTitle JSON = "Autumn & Wool", title tag = Autumn &amp; Wool. Header logo alt renders Autumn &amp;amp; Wool. No site-title field in Settings > Website or Brand to change. Nothing changed | n/a | n/a |

## Phone-sized first visit (headless Chrome, fresh profile, 390x844, CDP port 9343)
Profile: scratchpad/b13/chrome-fresh-2026-11-11-b13. Product: /shop/p/oversized-merino-wool-v-neck-sweater-vest, 10 s wait.
- Banner .gdpr-cookie-banner: x0 y751 w390 h93 (yesterday y709 h135).
- Banner buttons: Accept all x12 y800 w95; Decline all x113 y800 w101; Manage cookies x220 y800 w133. All visible, height 36.
- Price €126.00: y 710-741 (clear of banner, which starts at 751).
- Add To Cart: y 757-805. Banner starts at 751, so the button still overlaps the banner by about 54 px. NOT clear.
- Banner innerText not captured in this run.

## Finish
Curl: / 200, /shop 200, /contact 200, /wool-gifts 200, product page 200.
