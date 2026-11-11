# Batches 18-19: phone hero, make text the LCP (2026-11-11, 12:45-13:25 EET)

Goal asked: mobile PageSpeed Performance 90. Result: not reached. Mobile stays in a 59-78 band.

## Measurement before (headless Chrome, 412x823, first visit)
- Hero photo top at y=696: a 127 px strip on the first screen, 93 px of it under the cookie banner. Chrome still reported the photo as the LCP element.

## Batch 18 - DONE (home Code block, one CSS rule)
- Added `@media (max-width:800px){.aw-hl{min-height:calc(100svh - 170px)}}` so the hero text block fills the first phone screen and the photo starts just below it.
- Backup `backup/home-codeblock-before-b18.html`. Source `business-os/seo-marketplace/live-2026-11-11-psi/v3/`.
- After: LCP element is the `<h1>` at 412x823 and 390x664. Desktop unchanged (LCP is the photo, 680x640).
- One PageSpeed run then showed CLS 0.129 on mobile (text was vertically centred in the taller block).

## Batch 19 - DONE (same rule, top-aligned)
- Rule now `{min-height:calc(100svh - 170px);justify-content:flex-start}`: heading, sentence and buttons sit where they sat before; empty space is below the buttons.
- Backup `backup/home-codeblock-before-b19.html`. Source `.../v4/`.
- After: h1 y=222, sentence y=356, buttons y=500 (same as before batch 18); photo top y=811. CLS 0 / 0 / 0.001 in three runs.

## PageSpeed Insights, home (single lab samples)
| When | Mobile Perf | Mobile FCP / LCP / TBT / CLS | Desktop Perf |
|---|---|---|---|
| Before batch 18 (round 2 runs + owner's 12:34 run) | 55, 78, 60, 77 | LCP 4.3-11.1 s | 84, 91, 98 |
| After batch 18 | 73, 76, 75, 70 | 2.6 s / 5.1, 2.6, 4.8, 4.3 s / 230, 490, 190, 320 ms / CLS 0.129 once | 94, 96, 96 |
| After batch 19 | 60, 59, 78 | 2.6 s / 10.4, 10.6, 4.6 s / 350, 370, 130 ms / CLS 0 | 86, 84, 94 |

Reading: no measurable gain from making the text the LCP element. PageSpeed reports the heading as LCP but still times it at 4-10 s in most runs. Mobile first paint is 2.6 s in every run and comes from Squarespace's render-blocking CSS (about 160 KiB); blocking time comes from Squarespace scripts (about 1.1 MB) and Google Analytics. With those fixed, the best possible mobile score is about 89 (my arithmetic from PageSpeed's weights: FCP 2.6 s, LCP 2.6 s, TBT 230 ms, CLS 0, SI 3.2 s), so 90 is not reachable on this platform.

Visible effect kept live: on phones the photo no longer peeks at the bottom of the first screen (returning visitors without the cookie banner see blank space there). Revert = paste `backup/home-codeblock-before-b18.html`.
