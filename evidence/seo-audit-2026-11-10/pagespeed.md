# PageSpeed Insights - autumnandwool.com - 2026-11-10

Collected via the PSI web UI (pagespeed.web.dev) in ego-browser, not the API. Values are exactly as shown in the finished report. Lab data: Lighthouse 13.6.0, HeadlessChromium 157, Moto G Power + Slow 4G (mobile), Desktop preset (desktop). Field data (CrUX) shows "No Data" for every URL and form factor, so field LCP/INP/CLS/FCP/TTFB and pass/fail are not available.

## Summary

| Page | Form factor | Perf | A11y | BP | SEO | FCP | LCP | TBT | CLS | Speed Index | Field data |
|---|---|---|---|---|---|---|---|---|---|---|---|
| / | Mobile | 44 | 96 | 96 | 100 | 2.6 s | 11.8 s | 950 ms | 0 | 6.6 s | No Data |
| / | Desktop | 76 | 96 | 96 | 100 | 0.6 s | 1.0 s | 530 ms | 0 | 1.0 s | No Data |
| /shop | Mobile | 52 | 96 | 96 | 100 | 2.9 s | 13.2 s | 490 ms | 0 | 6.3 s | No Data |
| /shop | Desktop | 66 | 97 | 96 | 100 | 0.6 s | 3.1 s | 330 ms | 0 | 1.7 s | No Data |
| /shop/p/oversized-merino-wool-v-neck-sweater-vest | Mobile | 72 | 96 | 96 | 100 | 2.6 s | 3.9 s | 340 ms | 0.011 | 5.7 s | No Data |
| /shop/p/oversized-merino-wool-v-neck-sweater-vest | Desktop | 72 | 96 | 96 | 100 | 0.6 s | 2.4 s | 330 ms | 0.001 | 1.3 s | No Data |

Repeat-run variance: the homepage mobile report was run three times. Performance was 42 (first run, LCP 18.7 s, TBT 540 ms, SI 11.3 s, permalink not captured), then 44 (report kept above). The homepage desktop was run twice; the first run (permalink https://pagespeed.web.dev/analysis/https-www-autumnandwool-com/8wu8vm91w6?form_factor=desktop) showed FCP 0.6 s, LCP 1.0 s, TBT 530 ms, CLS 0, SI 1.0 s, and its Performance score was not captured. Treat homepage mobile as 42-44.

## Permalinks (finished reports)

- / Mobile: https://pagespeed.web.dev/analysis/https-www-autumnandwool-com/g1gj0ecc27?form_factor=mobile
- / Desktop: https://pagespeed.web.dev/analysis/https-www-autumnandwool-com/569f8lhx53?form_factor=desktop
- /shop Mobile: https://pagespeed.web.dev/analysis/https-www-autumnandwool-com-shop/unpz1xerxm?form_factor=mobile
- /shop Desktop: https://pagespeed.web.dev/analysis/https-www-autumnandwool-com-shop/ohfiha4qv5?form_factor=desktop
- Product Mobile: https://pagespeed.web.dev/analysis/https-www-autumnandwool-com-shop-p-oversized-merino-wool-v-neck-sweater-vest/95zu6bg56c?form_factor=mobile
- Product Desktop: https://pagespeed.web.dev/analysis/https-www-autumnandwool-com-shop-p-oversized-merino-wool-v-neck-sweater-vest/wke75ywp6t?form_factor=desktop

## Opportunities and diagnostics per run

Insights and Diagnostics are listed as PSI shows them (savings in brackets where PSI gives one). "Failed" audits are the ones PSI renders as failing.

### / Mobile (Perf 44)
- Insights: Render-blocking requests (Est savings of 1,760 ms); Font display (40 ms); Improve image delivery (225 KiB); Legacy JavaScript (48 KiB); Forced reflow; LCP request discovery; Network dependency tree; Use efficient cache lifetimes (1 KiB); Optimize DOM size
- Diagnostics: Reduce JavaScript execution time (2.3 s); Minimize main-thread work (3.4 s); Reduce unused CSS (169 KiB); Reduce unused JavaScript (949 KiB); Avoid enormous network payloads (3,632 KiB); Avoid long main-thread tasks (16 long tasks); Avoid non-composited animations (12 elements)
- Failed Accessibility: Links do not have a discernible name
- Failed Best Practices: Browser errors were logged to the console
- Failed SEO: none (score 100)

### / Desktop (Perf 76)
- Insights: Improve image delivery (2,039 KiB); Render-blocking requests (330 ms); Font display (90 ms); Forced reflow; LCP request discovery; Network dependency tree; Use efficient cache lifetimes (14 KiB); Legacy JavaScript (48 KiB); Layout shift culprits
- Diagnostics: Reduce JavaScript execution time (1.6 s); Minimize main-thread work (2.7 s); Reduce unused CSS (169 KiB); Reduce unused JavaScript (928 KiB); Avoid enormous network payloads (5,075 KiB); Avoid long main-thread tasks (13 long tasks); Avoid non-composited animations (327 elements)
- Failed Accessibility: Links do not have a discernible name
- Failed Best Practices: Browser errors were logged to the console
- Failed SEO: none (score 100)

### /shop Mobile (Perf 52)
- Insights: Render-blocking requests (1,910 ms); Legacy JavaScript (48 KiB); Forced reflow; Network dependency tree; Use efficient cache lifetimes (1 KiB); Font display (20 ms); Improve image delivery (2,504 KiB); Layout shift culprits
- Diagnostics: Reduce JavaScript execution time (1.8 s); Minimize main-thread work (2.9 s); Reduce unused CSS (167 KiB); Reduce unused JavaScript (1,116 KiB); Avoid enormous network payloads (5,831 KiB); Avoid long main-thread tasks (13 long tasks); User Timing marks and measures (1)
- Failed Accessibility: Links do not have a discernible name
- Failed Best Practices: Browser errors were logged to the console
- Failed SEO: none (score 100)

### /shop Desktop (Perf 66)
- Insights: Render-blocking requests (360 ms); Font display (30 ms); Forced reflow; Network dependency tree; Use efficient cache lifetimes (12 KiB); Improve image delivery (137 KiB); Legacy JavaScript (48 KiB); Layout shift culprits
- Diagnostics: Reduce JavaScript execution time (1.4 s); Minimize main-thread work (2.5 s); Reduce unused JavaScript (1,116 KiB); Reduce unused CSS (168 KiB); Avoid enormous network payloads (3,698 KiB); Avoid long main-thread tasks (12 long tasks); User Timing marks and measures (1)
- Failed Accessibility: Links do not have a discernible name
- Failed Best Practices: Browser errors were logged to the console
- Failed SEO: none (score 100)

### Product page Mobile (Perf 72)
- Insights: Render-blocking requests (1,920 ms); Legacy JavaScript (48 KiB); Network dependency tree; Use efficient cache lifetimes (16 KiB); Font display (10 ms); Improve image delivery (205 KiB); Layout shift culprits
- Diagnostics: Reduce JavaScript execution time (1.4 s); Minimize main-thread work (2.2 s); Reduce unused CSS (178 KiB); Image elements do not have explicit width and height; Reduce unused JavaScript (965 KiB); Avoid enormous network payloads (3,449 KiB); Avoid long main-thread tasks (11 long tasks); User Timing marks and measures (1)
- Failed Accessibility: Links do not have a discernible name
- Failed Best Practices: Browser errors were logged to the console
- Failed SEO: none (score 100)

### Product page Desktop (Perf 72)
- Insights: Render-blocking requests (380 ms); Forced reflow; LCP request discovery; Network dependency tree; Use efficient cache lifetimes (1 KiB); Font display (10 ms); Improve image delivery (279 KiB); Legacy JavaScript (48 KiB); Layout shift culprits
- Diagnostics: Reduce JavaScript execution time (1.4 s); Minimize main-thread work (2.3 s); Reduce unused JavaScript (967 KiB); Reduce unused CSS (178 KiB); Image elements do not have explicit width and height; Avoid enormous network payloads (3,484 KiB); Avoid long main-thread tasks (11 long tasks); User Timing marks and measures (1)
- Failed Accessibility: Links do not have a discernible name
- Failed Best Practices: Browser errors were logged to the console
- Failed SEO: none (score 100)

## Not obtained

- Field data (CrUX): "No Data" for all six runs; no field LCP/INP/CLS/FCP/TTFB or pass/fail exists to record.
- Homepage desktop Performance score from the first desktop run (see variance note above).
- Homepage mobile permalink from the first run (superseded by the kept run).
- Out of scope but seen: "Accessibility tree is not well-formed" failed in the Agentic Browsing category on every run (not one of the requested categories).
- Note: the "Failed" lists are read from the rendered audit classes in the visible (selected) report. The PSI "Accessibility" / SEO item lists contain no further failures beyond those above.
