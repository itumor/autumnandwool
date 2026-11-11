# Performance re-audit, autumnandwool.com (lab), 2026-11-10

## Method
- PSI API v5 keyless: all 6 runs returned HTTP 429 `Queries per day` (daily quota exhausted). Retried twice, 20s apart, still 429. Raw 429 bodies saved as `pagespeed/{mobile,desktop}*.json`. No PSI scores exist for this run.
- CrUX: none returned (PSI response carries no `loadingExperience`). No field data. Low traffic.
- Fallback used: local Lighthouse 13.6.0 via `npx lighthouse`, headless Chrome, `--form-factor=mobile` and `--preset=desktop`, default simulated throttling. JSON in `pagespeed/local-lh-*.json`.
- NOT comparable 1:1 with PSI baseline (different Lighthouse build, different host, single run each). Treat deltas as directional.
- Mobile LCP here is Lighthouse **simulated** LCP (what PSI also reports). Observed trace LCP is 0.6-0.8s (unthrottled local run). The gap is large. Product mobile varied between two runs (simulated LCP 14.2s vs 18.5s; observed 0.8s vs 3.5s; score 65 vs 57). Single-run mobile product numbers are unstable.

## Results (local Lighthouse 13.6.0, lab)

| Page / strategy | Score | LCP (sim) | TBT | CLS | FCP | Speed Index | Page wt | Image bytes (count) | Requests | Baseline (PSI) score / LCP / TBT |
|---|---|---|---|---|---|---|---|---|---|---|
| Home mobile | 66 | 10.7s | 100ms | 0.072 | 2.9s | 4.3s | 2,577 KiB | 529 KiB (8) | 71 | 44 / 11.8s / 950ms |
| Shop mobile | 64 | 11.9s | 90ms | 0.002 | 3.1s | 5.9s | 5,108 KiB | 2,831 KiB (25) | 98 | 52 / 13.2s / n/a |
| Product mobile | 65 (rerun 57) | 14.2s (rerun 18.5s) | 150ms | 0.010 | 2.8s | 4.9s | 2,746 KiB | 594 KiB (6) | 82 | 72 / 3.9s / n/a |
| Home desktop | 95 | 1.2s | 0ms | 0.002 | 0.9s | 1.3s | 3,472 KiB | 1,410 KiB (14) | 77 | 76 / 1.0s / n/a |
| Shop desktop | 83 | 2.5s | 0ms | 0.001 | 0.9s | 1.8s | 2,894 KiB | 601 KiB (21) | 95 | 66 / 3.1s / n/a |
| Product desktop | 85 | 2.4s | 0ms | 0.016 | 0.9s | 1.4s | 2,759 KiB | 622 KiB (15) | 91 | 72 / 2.4s / n/a |

Deltas vs baseline (directional only):
- Home mobile: score +22, LCP -1.1s, TBT -850ms. CLS 0.072 (baseline ~0).
- Shop mobile: score +12, LCP -1.3s.
- Product mobile: score -7 (rerun -15), LCP +10.3s (rerun +14.6s). Unexplained; do not act on this number until PSI quota resets and it is re-checked.
- Home desktop: score +19, LCP +0.2s.
- Shop desktop: score +17, LCP -0.6s.
- Product desktop: score +13, LCP 0.0s.

LCP elements: home = hero model image (`img` in `section.aw-w`, fetchpriority=high). Shop (mobile and desktop) = **GDPR cookie-banner paragraph**, not a product image (mobile elementRenderDelay 561ms). Product = vest gallery image; mobile shows late discovery (simulated lcpLoadDelay 11s, observed 0.5s).

Performance score blend (mobile weight 2, desktop 1, mean of 3 pages): now 73 (71 with product-mobile rerun). Baseline 61.

## Top opportunities (Lighthouse est. savings)
Home mobile: unused JS 2,610ms / 761 KiB; render-blocking 1,730ms; unused CSS 870ms / 136 KiB; legacy JS 350ms / 47 KiB; bootup 200ms.
Shop mobile: unused JS 3,840ms / 928 KiB; render-blocking 1,690ms; unused CSS 690ms / 134 KiB; legacy JS 350ms; bootup 150ms.
Product mobile: unused JS 3,270ms / 791 KiB; render-blocking 1,680ms; image delivery 1,050ms / 205 KiB; unused CSS 860ms / 145 KiB; legacy JS 350ms.
Home desktop: image delivery 1,133 KiB; render-blocking 460ms; unused CSS 130ms / 136 KiB; font-display 50ms.
Shop desktop: unused JS 470ms / 942 KiB; render-blocking 460ms; unused CSS 60ms; font-display 50ms.
Product desktop: unused JS 440ms / 779 KiB; render-blocking 460ms; image delivery 272 KiB; unused CSS 120ms; font-display 50ms.

## Fixes by owner
Owner can fix (Squarespace settings and content):
1. Shop grid images: 21-25 product images, 2.8 MB on mobile. Reduce image dimensions/quality on product thumbnails; check whether hover-image swaps are enabled (each adds a second image per product; not verified this run).
2. Product and home hero images: serve smaller uploads, re-export at display size (home desktop image-delivery ~1.1 MB savings; product mobile 205 KiB). Hero image is the home LCP.
3. Reduce section/image count on home (71 requests mobile, 8 images at 529 KiB).
4. Fonts: font-display savings 50-70ms. Cut font families/weights in Site Styles.
5. Consent banner (shop LCP): owner can change consent-tool settings or banner layout if the banner is the owner's; verify which vendor renders it.

Platform / third-party code (not editable without code injection, which is off):
1. Unused JS 760-930 KiB on mobile (Squarespace core bundles plus third-party scripts). Largest single item on every page.
2. Render-blocking JS/CSS ~1.7s mobile, ~0.46s desktop.
3. Unused CSS 135-145 KiB on all pages (Squarespace template CSS).
4. Legacy JS 47 KiB (platform polyfills).
5. Third-party apps: remove unused Squarespace integrations/apps (owner action; reduces JS).

## Persistence
Findings JSON (performance category):
{"category":"Performance","source":"local-lighthouse-13.6.0","psi":"429 daily quota","crux":"none","scores":{"mobile":{"home":66,"shop":64,"product":65,"product_rerun":57},"desktop":{"home":95,"shop":83,"product":85}},"blend":73,"baseline_blend":61,"notes":["not 1:1 with PSI","mobile LCP simulated","product mobile unstable"]}

Raw: `pagespeed/local-lh-{mobile,desktop}-{home,shop,product}.json`, `pagespeed/local-lh-mobile-product-rerun.json`, PSI 429 bodies `pagespeed/{mobile,desktop}*.json`.
