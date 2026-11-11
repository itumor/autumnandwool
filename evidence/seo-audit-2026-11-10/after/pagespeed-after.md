# PageSpeed Insights, after run - autumnandwool.com - 2026-11-10

Collected via the PSI web UI (pagespeed.web.dev) in ego-browser, not the API. Values are exactly as PSI showed them in the finished report. Lab data: Lighthouse 13.6.0, HeadlessChromium 157, Moto G Power + Slow 4G (mobile), Desktop preset (desktop). Same method and fields as `../pagespeed.md`.

Field data (CrUX) shows "No Data" for every URL and form factor, so field metrics and pass/fail are not available.

Raw text of each finished report is in `raw-pagespeed/` (file names give the run label; `r1`/`r2`/`r3` = repeat run).

## Run-to-run noise

Mobile home and mobile /shop were each run three times (the morning run was once per page). Mobile product and both desktop runs were run once, per the brief.

- Homepage mobile, this run: Performance 60, 60, 61. LCP 12.9 s, 12.9 s, 5.1 s. The morning's own homepage mobile runs spanned 42 to 44 Performance and LCP 11.8 s to 18.7 s, so LCP varies a lot between runs.
- /shop mobile, this run: Performance 42, 42, 42. LCP 17.5 s in all three. Metrics were identical across the three runs.
- Single-run pages (product mobile, all desktop) cannot be separated from noise with one sample. The 5-point rule is applied as briefed, but a single run is weak evidence for a change.

## Before / after

Baseline = `../pagespeed.md` (morning, one run per cell; homepage mobile baseline = the kept run, 44; the morning's first run gave 42).
After, mobile home and /shop = median of three runs (individual values in brackets).

| Page | Form factor | Perf before -> after | LCP before -> after | TBT before -> after | CLS before -> after | SEO before -> after | Accessibility before -> after |
|---|---|---|---|---|---|---|---|
| / | Mobile | 44 -> 60 [60, 60, 61] | 11.8 s -> 12.9 s [12.9, 12.9, 5.1] | 950 ms -> 370 ms [370, 370, 570] | 0 -> 0.001 [0.001, 0.001, 0] | 100 -> 100 | 96 -> 96 |
| / | Desktop | 76 -> 95 | 1.0 s -> 1.1 s | 530 ms -> 150 ms | 0 -> 0 | 100 -> 100 | 96 -> 96 |
| /shop | Mobile | 52 -> 42 [42, 42, 42] | 13.2 s -> 17.5 s [17.5, 17.5, 17.5] | 490 ms -> 970 ms [970 x3] | 0 -> 0 | 100 -> 100 | 96 -> 96 |
| /shop | Desktop | 66 -> 53 | 3.1 s -> 3.3 s | 330 ms -> 690 ms | 0 -> 0.001 | 100 -> 100 | 97 -> 97 |
| /shop/p/oversized-merino-wool-v-neck-sweater-vest | Mobile | 72 -> 52 (1 run) | 3.9 s -> 21.1 s | 340 ms -> 580 ms | 0.011 -> 0.011 | 100 -> 100 | 96 -> 96 |
| /shop/p/oversized-merino-wool-v-neck-sweater-vest | Desktop | 72 -> 50 (1 run) | 2.4 s -> 3.1 s | 330 ms -> 1,400 ms | 0.001 -> 0.014 | 100 -> 100 | 96 -> 96 |
| /wool-sweaters (new, no baseline) | Mobile | not measured before | 3.6 s | 670 ms | 0.001 | 100 | 96 (BP 73) |
| /wool-sweaters (new, no baseline) | Desktop | not measured before | 1.1 s | 950 ms | 0.156 | 100 | 96 (BP 73) |

Desktop Best Practices and FCP/Speed Index are in the per-run table below.

### Verdicts per metric

- **Homepage mobile, Performance:** improved (44 -> 60; all three runs 60 to 61, well beyond the 5-point noise band).
- **Homepage mobile, LCP:** within noise. Median 12.9 s is 1.1 s above the 11.8 s baseline, but the morning's runs ranged 11.8 to 18.7 s and one run today hit 5.1 s.
- **Homepage mobile, TBT:** likely improved (370 ms median vs 950 ms baseline). The morning's first run was 540 ms and today's third run was 570 ms, so the gap is partly within the spread.
- **Homepage mobile, CLS:** within noise (0 to 0.001 both times).
- **Homepage mobile, Speed Index:** improved (4.0 to 4.4 s vs 6.6 s). The morning's first run was 11.3 s, so the spread is wide.
- **Homepage desktop, Performance:** improved (76 -> 95, single run, 19 points). TBT fell from 530 ms to 150 ms. LCP unchanged (1.0 -> 1.1 s, within noise).
- **/shop mobile, Performance:** worse (52 -> 42, all three runs 42; 10 points, beyond noise). The morning value was one run, so the baseline spread is unknown.
- **/shop mobile, LCP:** worse (13.2 -> 17.5 s, all three runs identical). Same caveat.
- **/shop mobile, TBT:** worse (490 -> 970 ms, all three identical).
- **/shop desktop, Performance:** worse (66 -> 53, single run). TBT worse (330 -> 690 ms). LCP within noise (3.1 -> 3.3 s).
- **Product mobile, Performance:** worse (72 -> 52, single run). LCP worse (3.9 -> 21.1 s), TBT worse (340 -> 580 ms). Needs a repeat run before it is treated as real.
- **Product desktop, Performance:** worse (72 -> 50, single run). TBT worse (330 -> 1,400 ms). CLS worse (0.001 -> 0.014). LCP worse (2.4 -> 3.1 s).
- **CLS:** no page moved outside 0 to 0.016 mobile, but the new /wool-sweaters desktop run shows 0.156 (see opportunities).
- **SEO** stayed 100 on every page. **Accessibility** stayed 96 to 97 everywhere except /wool-sweaters (see failed audits).

## Per-run results

| Run | Form factor | Perf | A11y | BP | SEO | FCP | LCP | TBT | CLS | SI | Report time | Permalink |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| home-m-r1 | Mobile | 60 | 96 | 96 | 100 | 2.6 s | 12.9 s | 370 ms | 0.001 | 4.4 s | 5:17:18 PM | https://pagespeed.web.dev/analysis/https-www-autumnandwool-com/6t4l4jmbbh?form_factor=mobile |
| home-m-r2 | Mobile | 60 | 96 | 96 | 100 | 2.6 s | 12.9 s | 370 ms | 0.001 | 4.4 s | 5:18:05 PM | https://pagespeed.web.dev/analysis/https-www-autumnandwool-com/5gys5jglp1?form_factor=mobile |
| home-m-r3 | Mobile | 61 | 96 | 96 | 100 | 2.6 s | 5.1 s | 570 ms | 0 | 4.0 s | 5:18:23 PM | https://pagespeed.web.dev/analysis/https-www-autumnandwool-com/p1cl1pvggl?form_factor=mobile |
| shop-m-r1 | Mobile | 42 | 96 | 96 | 100 | 2.9 s | 17.5 s | 970 ms | 0 | 7.6 s | 5:18:53 PM | https://pagespeed.web.dev/analysis/https-www-autumnandwool-com-shop/qvuc87erq9?form_factor=mobile |
| shop-m-r2 | Mobile | 42 | 96 | 96 | 100 | 2.9 s | 17.5 s | 970 ms | 0 | 7.6 s | 5:19:32 PM | https://pagespeed.web.dev/analysis/https-www-autumnandwool-com-shop/d6ha5wvro7?form_factor=mobile |
| shop-m-r3 | Mobile | 42 | 96 | 96 | 100 | 2.9 s | 17.5 s | 970 ms | 0 | 7.6 s | 5:19:42 PM | https://pagespeed.web.dev/analysis/https-www-autumnandwool-com-shop/s0gbdq6dzo?form_factor=mobile |
| prod-m-r1 | Mobile | 52 | 96 | 96 | 100 | 2.6 s | 21.1 s | 580 ms | 0.011 | 6.0 s | 5:19:53 PM | https://pagespeed.web.dev/analysis/https-www-autumnandwool-com-shop-p-oversized-merino-wool-v-neck-sweater-vest/jjp2xohs2h?form_factor=mobile |
| wool-m-r1 | Mobile | 68 | 96 | 73 | 100 | 2.6 s | 3.6 s | 670 ms | 0.001 | 4.1 s | 5:20:24 PM | https://pagespeed.web.dev/analysis/https-www-autumnandwool-com-wool-sweaters/h97boj09tk?form_factor=mobile |
| home-d-r1 | Desktop | 95 | 96 | 96 | 100 | 0.6 s | 1.1 s | 150 ms | 0 | 1.0 s | 5:20:49 PM | https://pagespeed.web.dev/analysis/https-www-autumnandwool-com/w36hpwphfr?form_factor=desktop |
| shop-d-r1 | Desktop | 53 | 97 | 96 | 100 | 0.6 s | 3.3 s | 690 ms | 0.001 | 1.8 s | 5:21:18 PM | https://pagespeed.web.dev/analysis/https-www-autumnandwool-com-shop/44yi23v6qc?form_factor=desktop |
| prod-d-r1 | Desktop | 50 | 96 | 96 | 100 | 0.6 s | 3.1 s | 1,400 ms | 0.014 | 1.8 s | 5:21:49 PM | https://pagespeed.web.dev/analysis/https-www-autumnandwool-com-shop-p-oversized-merino-wool-v-neck-sweater-vest/sbf4m0e1vq?form_factor=desktop |
| wool-d-r1 | Desktop | 63 | 96 | 73 | 100 | 0.6 s | 1.1 s | 950 ms | 0.156 | 1.0 s | 5:22:29 PM | https://pagespeed.web.dev/analysis/https-www-autumnandwool-com-wool-sweaters/rkif2n6k50?form_factor=desktop |

The homepage mobile first run (home-m-r1) was made in the interactive session before the runner script existed, so its raw text was not saved; its values were read from the finished report on screen.

## Failed audits (PSI non-passed lists)

- **Accessibility:** "Links do not have a discernible name" on every page (morning baseline also). /shop desktop scored 97 (one fewer failing item). /wool-sweaters adds "Image elements do not have [alt] attributes that are redundant text" (mobile and desktop).
- **Best Practices:** "Browser errors were logged to the console" on every page (baseline item). /wool-sweaters adds "Does not use HTTPS" (10 insecure requests on mobile, 13 on desktop) and "Issues were logged in the Issues panel in Chrome Devtools". The Trust and Safety items (CSP, HSTS, COOP, Trusted Types) also appear in PSI's non-passed list on every page; the morning file did not list them, so this run lists them for completeness, without confirming each one's state.
- **SEO:** no failed audits on any page (score 100). "Structured data is valid" is in PSI's manual-check list only.
- **Agentic Browsing (out of the four requested categories):** "Accessibility tree is not well-formed" fails on every page.

## Insights and diagnostics (savings as PSI shows them)

Full text per run is in `raw-pagespeed/`. Largest recurring items:

- Render-blocking requests: 1,750 to 1,910 ms estimated savings on every mobile page; 300 to 400 ms on desktop.
- Reduce unused JavaScript: 949 KiB (home), 1,117 KiB (/shop), 965 KiB (product), 965 KiB (wool-sweaters) on mobile.
- Reduce unused CSS: 167 to 178 KiB on every page.
- Improve image delivery: 27 KiB (home mobile), 2,504 KiB (/shop mobile), 205 KiB (product mobile), 1,139 KiB (home desktop), 137 to 279 KiB (other desktop pages).
- Use efficient cache lifetimes: 762 KiB on product mobile (this run), 220 KiB on wool-sweaters mobile.
- Reduce JavaScript execution time: 1.3 to 2.6 s (mobile); 2.0 to 3.1 s (desktop shop and product).
- Legacy JavaScript: 48 to 51 KiB on every page.
- /wool-sweaters desktop: Layout shift culprits listed (CLS 0.156).

## Not obtained

- Field data (CrUX): "No Data" for all runs; no field LCP/INP/CLS/FCP/TTFB or pass/fail.
- Morning homepage mobile first-run permalink (morning file, unchanged).
- Single-run values (product mobile, all desktop) have no repeat, so their changes cannot be separated from noise.
