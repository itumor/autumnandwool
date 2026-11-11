# PageSpeed Insights re-measure, 2026-11-11

Source: public web UI https://pagespeed.web.dev (PSI API was over quota, HTTP 429). Lighthouse 13.6.0, HeadlessChromium, one run per URL and form factor. Lab data only; field data reads "No Data" for every run.

Run times (GMT+2): Home 08:22 (mobile and desktop from one report), /shop 08:25, product page 08:29, all 2026-11-11.

Delta = today minus yesterday's morning run (from the brief). "n/a" = yesterday value not supplied.

## Six runs

| Page | Strategy | Perf | Delta vs yesterday | A11y | BP | SEO | FCP | LCP | Delta LCP | TBT | Delta TBT | CLS | SI |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Home | Mobile | 48 | +4 (44) | 96 | 96 | 100 | 11.3 s | 18.0 s | +6.2 s (11.8 s) | 340 ms | -610 ms (950 ms) | 0 | 11.3 s |
| Home | Desktop | 90 | +14 (76) | 96 | 96 | 100 | 0.6 s | 1.3 s | +0.3 s (1.0 s) | 200 ms | n/a | 0.001 | 1.2 s |
| /shop | Mobile | 64 | +12 (52) | 96 | 96 | 100 | 2.9 s | 17.5 s | +4.3 s (13.2 s) | 150 ms | -340 ms (490 ms) | 0.001 | 5.7 s |
| /shop | Desktop | 49 | -17 (66) | 97 | 96 | 100 | 0.6 s | 3.5 s | +0.4 s (3.1 s) | 810 ms | n/a | 0.001 | 2.1 s |
| Product | Mobile | 48 | -24 (72) | 96 | 96 | 100 | 2.6 s | 14.5 s | +10.6 s (3.9 s) | 720 ms | n/a | 0.001 | 6.2 s |
| Product | Desktop | 66 | -6 (72) | 96 | 96 | 100 | 0.6 s | 2.9 s | +0.5 s (2.4 s) | 390 ms | n/a | 0 | 1.3 s |

Note: the PSI page showed "+N" comparison badges against an earlier PSI run for the same URL. They were not used. Deltas above are computed against the brief's yesterday numbers.

## Opportunities (top 5 per run, as stated by PSI)

### Home, mobile (Perf 48)
- Render-blocking requests: est savings 1,180 ms
- Improve image delivery: est savings 134 KiB
- Legacy JavaScript: est savings 48 KiB
- Reduce unused JavaScript: est savings 949 KiB
- Reduce unused CSS: est savings 169 KiB
- Also listed: Reduce JavaScript execution time 1.3 s; Avoid enormous network payloads 3,289 KiB total

### Home, desktop (Perf 90)
- Improve image delivery: est savings 1,139 KiB
- Render-blocking requests: est savings 380 ms
- Reduce unused JavaScript: est savings 949 KiB
- Reduce unused CSS: est savings 169 KiB
- Legacy JavaScript: est savings 48 KiB
- Also listed: Avoid enormous network payloads 4,172 KiB total

### /shop, mobile (Perf 64)
- Improve image delivery: est savings 2,467 KiB
- Render-blocking requests: est savings 1,920 ms
- Reduce unused JavaScript: est savings 1,117 KiB
- Reduce unused CSS: est savings 167 KiB
- Legacy JavaScript: est savings 48 KiB
- Also listed: Avoid enormous network payloads 5,787 KiB total

### /shop, desktop (Perf 49)
- Improve image delivery: est savings 137 KiB
- Reduce unused JavaScript: est savings 1,116 KiB
- Reduce unused CSS: est savings 168 KiB
- Render-blocking requests: est savings 350 ms
- Legacy JavaScript: est savings 48 KiB
- Also listed: Reduce JavaScript execution time 2.4 s; Minimize main-thread work 3.9 s; Avoid enormous network payloads 3,697 KiB total

### Product, mobile (Perf 48)
- Render-blocking requests: est savings 1,900 ms
- Improve image delivery: est savings 205 KiB
- Reduce unused JavaScript: est savings 963 KiB
- Reduce unused CSS: est savings 178 KiB
- Use efficient cache lifetimes: est savings 51 KiB
- Also listed: Reduce JavaScript execution time 2.0 s; Avoid enormous network payloads 3,458 KiB total; Image elements do not have explicit width and height

### Product, desktop (Perf 66)
- Use efficient cache lifetimes: est savings 650 KiB
- Improve image delivery: est savings 279 KiB
- Reduce unused JavaScript: est savings 1,066 KiB
- Reduce unused CSS: est savings 178 KiB
- Render-blocking requests: est savings 370 ms
- Also listed: Reduce JavaScript execution time 1.4 s; Image elements do not have explicit width and height

## Not read

- LCP element for each run: not captured. The LCP breakdown / LCP request discovery audits were listed but not expanded.
- Accessibility, Best Practices and SEO failing items: only the scores were read, not the individual failing audits.
- Each run is a single Lighthouse sample. Mobile LCP and Performance moved a lot between yesterday and today (product mobile -24), so treat individual deltas as noisy until repeated.
