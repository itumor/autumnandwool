# PageSpeed Insights, quiet re-run - autumnandwool.com - 2026-11-10

Collected via the PSI web UI (pagespeed.web.dev) in ego-browser, not the API. Lab data only: Lighthouse 13.6.0, HeadlessChromium 157, Moto G Power + Slow 4G (mobile), Desktop preset (desktop). Field data (CrUX) shows "No Data" for every URL and form factor. Same method as `pagespeed-after.md`; baselines are `../pagespeed.md` (morning) and `pagespeed-after.md` (earlier today).

## Method and data validity

- Three runs per cell (8 cells: 4 pages x 2 form factors). Run `r1` is the first pass, run alone. Runs `s1` and `s2` are a second pass in one process, run alone. Each run's raw text is saved in `raw-pagespeed-quiet/`.
- A run counts only if the PSI page URL contains the target page, the form factor matches, and the report shows that form factor's emulated device with no "Running analysis" text. All 24 counted runs pass this check.
- Rounds 2 and 3 are discarded. A background command was started twice by mistake, so two scripts drove the same browser page at once (about 18:18 to 18:27). Captures mixed reports from different URLs and devices. A 12-run re-run pass also overlapped with the stray process, so it is discarded too. These files are in `raw-pagespeed-quiet/discarded-concurrent-runs/` and must not be used.
- Medians are the middle of the three counted runs per metric.
- Verdict rules: Performance within 5 points of the morning value is within noise, as briefed. Larger changes are improved or worse, marked low confidence when the quiet range (max minus min) is at least as wide as the change. LCP is within noise when the morning value falls inside the quiet range; otherwise improved or worse.

## Before / after

| Page | Form factor | Morning Perf / LCP | Earlier today Perf / LCP | Quiet median Perf / LCP | Quiet range Perf / LCP | Verdict |
|---|---|---|---|---|---|---|
| /shop | Mobile | 52 / 13.2 s | 42 / 17.5 s | 38 / 15.3 s | 37-61 / 15.1-15.4 s | Perf worse (-14; range 24, low confidence). LCP worse (+2.1 s, outside range). |
| /shop | Desktop | 66 / 3.1 s | 53 / 3.3 s | 69 / 3.0 s | 46-78 / 2.6-3.4 s | Within noise (Perf +3; LCP inside range). |
| product | Mobile | 72 / 3.9 s | 52 / 21.1 s | 52 / 14.5 s | 37-60 / 14.3-14.7 s | Perf worse (-20; range 23, low confidence). LCP worse (+10.6 s, clear). |
| product | Desktop | 72 / 2.4 s | 50 / 3.1 s | 62 / 2.7 s | 58-76 / 2.4-2.7 s | Perf worse (-10; range 18, low confidence). LCP within noise (morning 2.4 s is the range floor). |
| / (home) | Mobile | 44 / 11.8 s | 60 / 12.9 s | 65 / 6.0 s | 56-71 / 5.3-6.1 s | Perf improved (+21; range 15, larger than the spread). LCP improved (-5.8 s, clear). |
| / (home) | Desktop | 76 / 1.0 s | 95 / 1.1 s | 74 / 1.0 s | 70-82 / 1.0-1.7 s | Within noise (Perf -2; LCP inside range). |
| /wool-sweaters | Mobile | not measured | 68 / 3.6 s | 55 / 11.3 s | 52-67 / 4.2-11.3 s | No baseline. LCP not stable (11.3, 4.2, 11.3 s), so the earlier 3.6 s is not confirmed. |
| /wool-sweaters | Desktop | not measured | 63 / 1.1 s | 90 / 1.0 s | 73-91 / 0.9-1.2 s | No baseline. Earlier 63 is below the quiet range. |

Caveat: the morning baseline is one run per cell. Where the morning value sits outside the quiet range, the verdict is a comparison with a single earlier sample, not a confirmed trend.

## Failed audits on /wool-sweaters

| Audit | Earlier today (mobile / desktop) | Quiet runs (mobile, 3 runs / desktop, 3 runs) |
|---|---|---|
| Does not use HTTPS | failed (10 / 13 insecure requests) | gone in all 6 runs |
| Image elements do not have [alt] attributes that are redundant text | failed | still failing in all 6 runs |
| Links do not have a discernible name | failed (site-wide) | still failing in all 6 runs (site-wide) |
| Best Practices score | 73 / 73 | 96 in all 6 runs (mobile 96, 96, 96; desktop 96, 96, 96) |

Other notes: the mobile run r1 and run s2 both show FCP, LCP and Speed Index at 11.3 s, the values PSI displayed in its metrics block. Treated as reported; the middle mobile run (s1) is 2.6 s / 4.2 s / 3.9 s. The earlier desktop CLS of 0.156 is not reproduced: 0, 0.026 and 0.039 across the three quiet runs.

## All counted runs

| Run | Form factor | Perf | A11y | BP | SEO | FCP | LCP | TBT | CLS | Speed Index |
|---|---|---|---|---|---|---|---|---|---|---|
| shop-m-r1 | Mobile | 38 | 96 | 96 | 100 | 3.3 s | 15.4 s | 1,050 ms | 0 | 8.5 s |
| shop-m-s1 | Mobile | 37 | 96 | 96 | 100 | 3.3 s | 15.1 s | 1,200 ms | 0 | 8.5 s |
| shop-m-s2 | Mobile | 61 | 96 | 96 | 100 | 2.9 s | 15.3 s | 240 ms | 0 | 5.6 s |
| shop-d-r1 | Desktop | 78 | 97 | 96 | 100 | 0.6 s | 3.0 s | 160 ms | 0.001 | 1.5 s |
| shop-d-s1 | Desktop | 69 | 97 | 96 | 100 | 0.6 s | 2.6 s | 320 ms | 0.001 | 1.7 s |
| shop-d-s2 | Desktop | 46 | 97 | 96 | 100 | 0.6 s | 3.4 s | 1,380 ms | 0.001 | 2.4 s |
| prod-m-r1 | Mobile | 37 | 96 | 96 | 100 | 2.6 s | 14.3 s | 1,890 ms | 0 | 7.4 s |
| prod-m-s1 | Mobile | 52 | 96 | 96 | 100 | 2.6 s | 14.7 s | 570 ms | 0.001 | 5.9 s |
| prod-m-s2 | Mobile | 60 | 96 | 96 | 100 | 2.6 s | 14.5 s | 330 ms | 0 | 5.1 s |
| prod-d-r1 | Desktop | 76 | 96 | 96 | 100 | 0.6 s | 2.4 s | 270 ms | 0.001 | 1.1 s |
| prod-d-s1 | Desktop | 62 | 96 | 96 | 100 | 0.6 s | 2.7 s | 500 ms | 0.001 | 1.3 s |
| prod-d-s2 | Desktop | 58 | 96 | 96 | 100 | 0.6 s | 2.7 s | 680 ms | 0.001 | 1.4 s |
| home-m-r1 | Mobile | 71 | 96 | 96 | 100 | 2.7 s | 6.0 s | 140 ms | 0 | 4.1 s |
| home-m-s1 | Mobile | 56 | 96 | 96 | 100 | 2.6 s | 6.1 s | 670 ms | 0.001 | 4.1 s |
| home-m-s2 | Mobile | 65 | 96 | 96 | 100 | 2.6 s | 5.3 s | 430 ms | 0.001 | 3.8 s |
| home-d-r1 | Desktop | 82 | 96 | 96 | 100 | 0.6 s | 1.7 s | 270 ms | 0.001 | 1.1 s |
| home-d-s1 | Desktop | 70 | 96 | 96 | 100 | 0.6 s | 1.0 s | 940 ms | 0.005 | 0.9 s |
| home-d-s2 | Desktop | 74 | 96 | 96 | 100 | 0.6 s | 1.0 s | 600 ms | 0 | 1.0 s |
| wool-m-r1 | Mobile | 52 | 96 | 96 | 100 | 11.3 s | 11.3 s | 210 ms | 0 | 11.3 s |
| wool-m-s1 | Mobile | 67 | 96 | 96 | 100 | 2.6 s | 4.2 s | 540 ms | 0.001 | 3.9 s |
| wool-m-s2 | Mobile | 55 | 96 | 96 | 100 | 11.3 s | 11.3 s | 110 ms | 0 | 11.3 s |
| wool-d-r1 | Desktop | 91 | 96 | 96 | 100 | 0.6 s | 0.9 s | 230 ms | 0 | 0.9 s |
| wool-d-s1 | Desktop | 73 | 96 | 96 | 100 | 0.6 s | 1.2 s | 600 ms | 0.026 | 1.1 s |
| wool-d-s2 | Desktop | 90 | 96 | 96 | 100 | 0.6 s | 1.0 s | 230 ms | 0.039 | 1.0 s |

Raw text per run: `raw-pagespeed-quiet/raw-<cell>-<m|d>-<r1|s1|s2>.txt`. Permalinks are in `raw-pagespeed-quiet/valid-24.json`.

## Not obtained

- Field data (CrUX): "No Data" for every URL and form factor, so no field LCP, INP, CLS, FCP or pass/fail.
- Morning baseline is one run per cell, so its spread is unknown.
- Values were pulled from each counted run's metrics block and checked against its permalink and device line; no run was dropped for a missing value.
