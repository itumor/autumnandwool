# Batches 20-21: "mobile 71 to 90" plan, phases 0-3 (2026-11-11, 13:25-14:10 EET)

Outcome: mobile 90 not reached. Net live change from this round: none (one trial applied and reverted).

## Phase 0: local Lighthouse (repeatable measurement)
- `npx lighthouse@12` (12.8.2), mobile, simulated slow 4G, performance only. Not added to the repo.
- Baseline, 5 runs (page as left after batch 19): 77, 84, 81, 85, 82, median 82. FCP 2.8-3.0 s, LCP 3.5-4.7 s, TBT 60-90 ms, LCP element `<h1>`.
- This Mac shows lower blocking time than PageSpeed's servers (60-100 ms vs 130-490 ms), so local scores read higher than pagespeed.web.dev.

## Phase 1: why the heading paints "late"
Cold load in headless Chrome, 412x823, real timings:
- First paint 476 ms shows only a small text (2,808 px2, announcement bar). The hero heading paints at 496 ms, one frame later.
- Lighthouse run: observed first paint 986 ms, observed LCP 1,150 ms; simulated first paint 3.7 s, simulated LCP 11.4 s.
- So the real gap is 20-160 ms. The simulator turns it into 1-8 s because every file that finishes before the LCP moment (fonts, Squarespace script bundles) is counted as something the heading waited for. Which bundles land before that moment changes run to run. That is the 4 s / 10 s flip.
- The hero is in a later part of the HTML (byte 338k of 418k) than the header, so the browser paints the header first. Not controllable from a Code block.

### Trial (batch 20): preload the heading font - APPLIED, then REVERTED (batch 21)
- Added two `<link rel="preload" as="font">` (Instrument Serif regular + italic) at the top of the home Code block.
- Effect on real paint: fonts started at ~250 ms instead of ~460 ms, but the paragraph (fallback font) became the LCP element, still one frame after first paint.
- Local Lighthouse, 5 runs: 77, 76, 75, 78, 78, median 77 (FCP 3.6 s, LCP 3.9-4.3 s, element `<p>`).
- Reverted by pasting the previous block. Public check: 0 preload tags, 1 `<h1>`, 16 `srcset`, home 200.
- Local Lighthouse after revert, 5 runs: 75, 76, 77, 79, 76, median 76 (FCP 3.5-3.8 s). Same page as the 82 baseline an hour earlier, so the 82 vs 77 difference was network conditions, not the preload. Conclusion: preload had no measurable effect.
- Backups: `backup/home-codeblock-before-b20.html`, `backup/home-codeblock-before-b21.html`.

## Phase 2: blocking time - NOT CHANGED
Local Lighthouse, main-thread time by source: Squarespace 574 ms (118 ms blocking), Google Tag (GA4) 108 ms (0 ms blocking), customer-account scripts about 10 ms.
- Customer accounts off: about 10 ms. Not worth a site setting change. Skipped.
- GA4 off: on PageSpeed's slower machine about 80 ms of blocking, roughly 2 points. Costs all GA4 data. Not done; needs an explicit owner decision.

## Phase 3: final numbers (home)
| Source | Mobile Performance | Notes |
|---|---|---|
| Local Lighthouse, 5 runs | 75, 76, 77, 79, 76 (median 76) | FCP 3.5-3.8 s, LCP 3.8-4.1 s, TBT 60-100 ms |
| pagespeed.web.dev, 3 runs | 56, 71, 61 | FCP 2.6 s each; LCP 10.2, 5.0, 10.8 s; TBT 430, 300, 300 ms |
| pagespeed.web.dev desktop, 3 runs | 92, 81, 85 | |

## Phase 4: what 90 would take
First paint under about 1.8 s on simulated slow 4G. Squarespace ships about 160 KiB of render-blocking CSS and 1.1 MB of scripts on every page; first paint is 2.6 s on PageSpeed in every run today. Reaching 90 means a storefront where the page code is ours (replatform). Not started; owner decision.

## Addendum 14:25 EET: exact mechanism (read-only, nothing changed)
Home HTML as served to a phone (171 KB): `<header>` ends with Squarespace's inline script `reserveSpaceForHeader.js` (byte 104,950), immediately before `<main>`; the hero Code block starts at byte 116,472. It is the only script in `<body>` before the hero.
- That script is parser-blocking and measures the header, so the browser must wait for all page CSS before running it. While it waits, only the header exists in the page.
- When the CSS arrives the browser paints what it has (header: first paint), runs the script, then parses `<main>` and paints the hero in a later frame.
- By then the page's deferred Squarespace bundles (about 1.1 MB, listed in `<head>` with `defer`) and Google Tag are downloaded or running. Lighthouse counts everything finished before the hero frame as "needed for LCP". How many bundles make it in varies per run: LCP 4-5 s or 10-11 s.
- The script is part of every Squarespace 7.1 header. It cannot be removed, moved or deferred from Custom CSS or a Code block, and the hero cannot be placed before it.
Conclusion: the hero cannot be in the first painted frame on this platform, so mobile LCP cannot be brought down to first paint. Mobile 90 is not achievable here by page-level changes.
