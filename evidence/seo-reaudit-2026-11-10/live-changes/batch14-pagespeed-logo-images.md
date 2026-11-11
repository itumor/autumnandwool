# Batch 14: PageSpeed fixes, home page (2026-11-11, 11:20-11:50 EET)

ego-browser task space `aw-batch14-psi-2026-11-11`, closed with finish({ keep: [] }).
Sources: `business-os/seo-marketplace/live-2026-11-11-psi/` (`build.py`, `before/`, `html/`).
Backups: `backup/home-codeblock-before-b14.html`, `backup/custom-css-before-b14.css`, `backup/custom-css-before-b14b.css`, `backup/custom-css-after-b14.css`.

## 1. Custom CSS: logo link name - DONE
- Cause: line 275 hid the logo `<img>` with `display:none` (text wordmark is drawn with CSS). Lighthouse: "Links must have discernible text" on the logo link, which failed Agentic browsing (2/3) and Accessibility (96).
- Change: image is now visually hidden (1 px, opacity 0) instead of `display:none`; the three CSS wordmark texts get an empty alt (`content:'Autumn' / ''`), placed after the original rules, so the link is read once.
- Saved twice: first save had the empty-alt rules before the original rules (no effect, name read "Autumn & Autumn &amp; Wool Wool"); second save moved them after. Editor text equalled the expected file before each save.
- Public `custom.css` version 22: both overlay guard rules present (`.sqs-widgets-confirmation-overlay{pointer-events:none !important}`, `.sqs-widgets-confirmation{pointer-events:none !important}`).
- Fresh headless Chrome: wordmark box unchanged (desktop 183x20 at 585,48; mobile 140x26 at 25,62). Accessibility tree link name: `Autumn &amp; Wool` (the `&amp;` is the platform's double-escaped logo alt, not editable).

## 2. Home Code block: responsive images - DONE
- Change: `srcset` + `sizes` added to all 16 `<img>` tags. Nothing else changed (build.py asserts this). Hero 500w/750w/1000w, cards 300w/500w/750w.
- Editor text equalled `before/home.html` (11,604 chars) before paste; after paste equalled `html/home.html` (19,140 chars). Saved, exited, no dialog.
- Public: `/` 200, 16 `srcset`, one `<h1>`. Product page 200.
- Fresh headless Chrome, desktop 1350 px: cards now load 500w (were 750w), hero 750w (was 1000w). Image bytes on first load 601 KB -> 289 KB.

## PageSpeed Insights, home (lab, single samples)
| Run (EET) | Mobile Perf | Mobile FCP / LCP / TBT | Desktop Perf | Desktop LCP / TBT | A11y | Agentic |
|---|---|---|---|---|---|---|
| 10:45 before (owner's run) | 59 | 2.6 s / 5.7 s / 570 ms | 74 | 1.3 s / 520 ms | 96 | 2/3 |
| ~11:40 after | 54 | 11.3 s / 17.2 s / 140 ms | 89 | 1.7 s / 160 ms | 100 | 3/3 |
| ~11:45 after | 50 | 2.6 s / 12.2 s / 700 ms | 72 | 1.0 s / 680 ms | 100 | 3/3 |
| ~11:50 after | 47 | 11.3 s / 16.5 s / 380 ms | 91 | 1.8 s / 90 ms | 100 | 3/3 |

Mobile is not improved and the samples are noisy. The same two-mode pattern (FCP 2.6 s or 11.3 s) was already there before this batch: 08:22 today, home mobile 48, FCP 11.3 s, LCP 18.0 s (`findings-after/pagespeed.md`). The 10:45 score of 59 was a good-mode sample. LCP element is the hero image in every run; PageSpeed's remaining items are Squarespace's own CSS (render-blocking, about 160 KiB) and scripts, plus reCAPTCHA.

## Not done (owner decision)
- reCAPTCHA (about 705 KiB, about 0.8 s CPU on phone) is loaded by the footer newsletter form on every page. Moving the form to its own page with a footer link would remove it sitewide. Changes where people sign up.
