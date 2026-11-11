# Batch 16: hero image on phones + PageSpeed results after batches 14-17 (2026-11-11, 12:15-12:40 EET)

## Hero image `sizes` - DONE
- Home Code block, hero `<img>`: `sizes="(max-width:800px) 100vw, 50vw"` -> `sizes="(max-width:800px) 60vw, 50vw"`. One attribute; nothing else changed.
- Source: `business-os/seo-marketplace/live-2026-11-11-psi/v2/`. Backup: `backup/home-codeblock-before-b16.html`.
- Editor text equalled the before file (19,140 chars) before paste; saved; public HTML has the new value once.
- Effect: phones with screen density under about 2.1 take the 500w file (40 KB) instead of 750w (102 KB). Trade-off: hero slightly softer on those phones. Revert = put `100vw` back.

## Manager verification of batch 15 (newsletter move) and batch 17 (font)
Fresh headless Chrome, 12 s per page, request counts:
| Page | reCAPTCHA | Typekit | newsletter script | console errors |
|---|---|---|---|---|
| / | 0 | 0 | 0 | 0 |
| product (merino vest) | 0 | 0 | 0 | 0 |
| /newsletter (after batch 15, before 17) | 3 | 4 | 2 | 0 |
Public HTML, 5 pages (/, /shop, /newsletter, product, /contact): all 200; footer link `href="/newsletter"` on each; newsletter block only on /newsletter; company registration link present on each.
Not tested: an actual signup on /newsletter (no test email was sent).

## PageSpeed Insights, home, after all changes (three runs, about 2 minutes apart)
| Run | Mobile Perf | Mobile FCP / LCP / TBT | Desktop Perf | Desktop LCP / TBT | A11y | Best Practices | Agentic |
|---|---|---|---|---|---|---|---|
| 1 | 55 | 2.9 s / 11.1 s / 350 ms | 84 | 1.0 s / 330 ms | 100 | 100 | 3/3 |
| 2 | 78 | 2.6 s / 4.4 s / 180 ms | 91 | 1.0 s / 220 ms | 100 | 100 | 3/3 |
| 3 | 60 | 2.6 s / 10.9 s / 340 ms | 98 | 1.1 s / 60 ms | 100 | 100 | 3/3 |
| Median | 60 | | 91 | | | | |
| Before, 10:45 (one run) | 59 | 2.6 s / 5.7 s / 570 ms | 74 | 1.3 s / 520 ms | 96 | 96 | 2/3 |

Reading: desktop up (74 -> median 91). Best Practices 96 -> 100 (reCAPTCHA console error gone). Mobile median 60 vs a single 59 before; today's earlier mobile samples were 47-54 after batch 14 and 48 at 08:22, so mobile is probably better but the lab numbers swing too much (55 to 78 here) to give a firm figure. The 11.3 s first-paint mode did not appear in these three runs.
