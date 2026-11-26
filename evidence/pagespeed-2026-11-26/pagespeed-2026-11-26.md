# PageSpeed Insights scan — autumnandwool.com — 2026-11-26

Collection: browser-driven `https://pagespeed.web.dev/analysis?url=...&form_factor=<mobile|desktop>` in the
connected Chrome relay, one run per cell, 26 Nov 2026 12:49–12:52 EET. The PSI v5 REST API returned
HTTP 429 (`RESOURCE_EXHAUSTED`, keyless quota 0) for every request from this environment, and WebFetch
on pagespeed.web.dev returns only the JS shell — all numbers below were read from the rendered report.
All runs: Lighthouse 13.6.0, HeadlessChromium 157.0.8103.38; mobile = Moto G Power / Slow 4G,
desktop = emulated desktop / custom throttling. **No field (CrUX) data** for any URL ("No data") —
low-traffic site, so these are lab results only. Values are single runs; PSI varies run to run.

## Scores and lab metrics

| Page | Strategy | Perf | A11y | BP | SEO | Agentic | FCP | LCP | TBT | CLS | SI |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `/` | Mobile | 74 | 100 | 100 | 100 | 3/3 | 2.9 s | 2.9 s | 390 ms | 0 | 7.4 s |
| `/` | Desktop | 89 | **95** | 100 | 100 | **2/3** | 0.6 s | 1.8 s | 130 ms | 0.002 | 1.0 s |
| `/shop` | Mobile | 66 | 100 | 100 | 100 | 3/3 | 3.2 s | 3.2 s | 510 ms | 0 | 9.5 s |
| `/shop` | Desktop | 97 | **95** | 100 | 100 | **2/3** | 0.6 s | 0.9 s | 80 ms | 0.001 | 1.6 s |
| PDP vest | Mobile | 60 | 100 | 100 | 100 | 3/3 | 2.7 s | **15.3 s** | 240 ms | 0 | 6.7 s |
| PDP vest | Desktop | 78 | **95** | 100 | 100 | **2/3** | 0.6 s | 2.6 s | 210 ms | 0.001 | 1.3 s |

PDP = `https://www.autumnandwool.com/shop/p/oversized-merino-wool-v-neck-sweater-vest`.

## Issues found (exact evidence)

1. **Desktop A11y 95 + Agentic 2/3 — one root cause.** Failing element from the Lighthouse audit:
   `<div aria-controls="language-picker-menu" aria-expanded="false" aria-label="language picker" class="language-picker language-picker-desktop" id="multilingual-language-picker-desktop" role="listbox" tabindex="0">`
   — a `listbox` with no required `option` children. Injected client-side by the Weglot switcher
   (enabled 25–26 Nov), which is why mobile is unaffected (desktop-only picker). Audit text:
   "Elements with an ARIA [role] that require children to contain a specific [role] are missing some or all
   of those required children"; Agentic: "Accessibility tree is not well-formed".
2. **PDP mobile LCP 15.3 s.** Render-blocking requests (est. savings 1,760 ms): Squarespace Hosting HTML
   159.2 KiB / 5,410 ms, `static.css` 41.5 KiB / 1,350 ms, `site.css?nocustom=true` 110.4 KiB / 1,800 ms,
   `custom.css` 3.5 KiB / 750 ms. Image delivery est. savings 205 KiB: `IMG_3347.JPEG?format=750w`
   264.3 KiB (1536×2048 served for 634×846; compression saving 142.2 KiB, responsive saving 75.1 KiB)
   and `IMG_3336.JPEG?format=750w` 97.5 KiB (saving 27.7 KiB). Also "Image elements do not have explicit
   width and height".
3. **Platform-level on every page:** unused JS 672–883 KiB, unused CSS 134–145 KiB, legacy JS 34 KiB,
   render-blocking 1,110–1,760 ms mobile vs 370–390 ms desktop, long main tasks 5–12. These are
   Squarespace core bundles and template CSS; Basic plan has no Code Injection, so not editable here.
4. **Shop mobile:** image delivery est. saving 1,278 KiB; total payload 3,547 KiB; JS execution 1.7 s,
   main-thread work 3.1 s. Biggest single lever is product grid images.
5. **No Core Web Vitals field data** — cannot claim a real-user pass/fail; all ratings above are lab.

## Out-of-band SEO/product checks (read-only, subagent)

- Titles, meta descriptions, H1s, canonicals and Product JSON-LD on `/`, `/shop` and the PDP are present
  and valid; PDP schema has name/image/price/availability/brand; `/` has no Product schema (correct).
- `robots.txt` reachable, points at sitemap; sitemap has 49 URLs, no `noindex`.
- `autumnandwool-google-feed.tsv`: 12 rows with empty `color`; 14 duplicate `link` URLs (variants share
  one PDP). Google's `item_group_id` minimum requirements say variants must have **different landing
  page URLs** — a real violation, but Squarespace cannot deep-link a variant, so no fake query string
  was added. Owner/platform decision.
- `/shop`: 202/203 images have non-empty alt. Home H1 renders as `Wool knitwearfor cooler days`
  (missing space) — live copy edit in Squarespace, not a code fix.

## Rescan (goal loop, 12:58 EET)

| Cell | First run | Rescan | Verdict |
|---|---|---|---|
| `/` desktop | Perf 89, A11y 95, Agentic 2/3, LCP 1.8 s | Perf 94, A11y 95, Agentic 2/3, LCP 1.6 s | Perf noise; ARIA/Agentic issues stable and reproducible |
| PDP mobile | Perf 60, A11y 100, Agentic 3/3, LCP 15.3 s | Perf 60, A11y 100, Agentic 3/3, LCP 15.0 s | LCP issue stable; no fix applied (admin/assets gated) |

No other cell was rescanned: both blocker fixes require Squarespace or Weglot admin login, and neither
is available in this session. See `FIX-PLAN.md` for the prioritised fixes and the rescan checklist.

## Fix applied 2026-11-26

Squarespace admin was made available via browser handoff. A subagent appended to Custom CSS:

```css
/* PSI 2026-11-26: Weglot desktop language picker (Squarespace integration) renders
   role="listbox" with no role="option" children -> desktop Accessibility 95 and
   Agentic 2/3. display:contents keeps it visible and clickable while
   removing the broken box from the accessibility tree. */
#multilingual-language-picker-desktop{display:contents !important;}
```

- Saved in Squarespace Custom CSS; original 18,038-char stylesheet and the load-bearing
  `.sqs-widgets-confirmation-overlay{pointer-events:none !important;}` rule are intact.
- Verified live: `https://www.autumnandwool.com/site.css` serves the new rule, and the live DOM
  reports `getComputedStyle(#multilingual-language-picker-desktop).display === 'contents'` with the
  switcher's current-language child still visible (87×23 px).
- Weglot's own Custom CSS field was tried first and persisted in the dashboard but did **not** reach
  the Squarespace-native picker — do not rely on it for this fix.
- **REVERTED the same day.** Rescan with the rule live showed mobile Accessibility had regressed
  from 100 / 3-of-3 to **95 / 2-of-3** on all three pages, and the ARIA failures were still present.
  `display:contents` did not remove the listbox from Chrome's accessibility tree and also overrode
  the mobile `display:none`, exposing the broken picker on mobile. Custom CSS was restored to the
  exact original 18,038 characters; `curl https://www.autumnandwool.com/site.css` no longer contains
  the rule, and the overlay guard is intact. Do not retry this rule.

## Goals / loop status

- Goal A — all four non-performance categories at 100 on both form factors: **blocked only by the Weglot
  listbox** (desktop). Fix by changing the switcher markup/style, not by hiding it.
- Goal B — Performance 90+ on mobile: **not achievable on Basic plan** while platform JS/CSS is
  render-blocking; lab scores 60–74 mobile. Owner levers: smaller product images, fewer apps, no
  platform upgrade. 100/100 is not a realistic target here.
- Goal C — no fake evidence: no API numbers invented; 429 and JS-shell failures recorded verbatim.
