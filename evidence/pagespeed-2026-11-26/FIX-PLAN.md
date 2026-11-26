# PageSpeed fix plan — 2026-11-26

Scan data and collection method: `pagespeed-2026-11-26.md` in this folder.
Rescan at 12:58 EET confirmed stability: home desktop Perf 89 → 94 (lab noise), A11y **95** and
Agentic **2/3** unchanged; PDP mobile Perf **60** both runs, LCP 15.3 s → **15.0 s**, other three
categories 100 / 100 / 3-of-3 both runs. No change was applied because every remaining fix needs
either Squarespace/Weglot admin login or owner-supplied assets; both are unavailable in this session.

## Goal state and what is achievable

| Goal | Target | Current | Achievable here? |
|---|---|---|---|
| Accessibility 100 on desktop | 100 | 95 (Weglot `role="listbox"`) | **No** — Weglot dashboard login required |
| Agentic browsing 3/3 on desktop | 3/3 | 2/3 (same root cause) | **No** — same |
| SEO 100 / Best Practices 100 | 100 | 100 everywhere | Already met |
| Performance 90+ mobile | 90 | 60–74 | **No** — platform render-blocking JS/CSS on Basic plan |
| Performance 100 | 100 | 60–97 | **Not realistic** on Squarespace Basic with third-party widgets |

"Zero issues / 100% everywhere" is not reachable from this environment: three of the five blockers
are platform- or vendor-owned, and two need credentials. No number below was invented to close a gap.

## Fixes, in priority order

1. **Weglot switcher ARIA (desktop A11y 95 + Agentic 2/3) — owner, Weglot dashboard.**
   Offending markup, read from the live DOM:
   `<div aria-controls="language-picker-menu" aria-expanded="false" aria-label="language picker" class="language-picker language-picker-desktop" id="multilingual-language-picker-desktop" role="listbox" tabindex="0">`
   with no `role="option"` children. Loaded by `https://cdn.weglot.com/weglot_squarespace-12.5.0.min.js?api_key=…`.
   Fix: in Weglot → switcher settings, use an accessible style (native select or a list of real
   links) so required child roles exist; **do not hide the switcher** — that would break the LV
   rollout. Re-run the desktop scan on `/`, `/shop` and the PDP; expect A11y 100 and Agentic 3/3.
   CSS cannot add ARIA roles, so Custom CSS is not a fix. Confirmed against official W3C ARIA/APG and
   axe `aria-required-children`: `listbox` requires `option` (or `group` of `option`) children; CSS has no
   mechanism to create role-bearing DOM children, and `::before`/`::after` are not role-bearing.
   Squarespace Basic offers Custom CSS (styling only), HTML/Markdown blocks (cannot reach an injected
   widget), and no site-wide Code Injection — so no allowed Squarespace layer can patch this widget.
   The fix must be made in Weglot's own dashboard/settings (login gate) or by the vendor.
   **Tried and rejected 2026-11-26:** `#multilingual-language-picker-desktop{display:contents!important}`
   was applied and saved in Custom CSS. It did not remove the listbox from Chrome's accessibility tree,
   regressed mobile A11y 100→95 and Agentic 3/3→2/3 on all three pages, and was fully reverted (CSS
   restored to the original 18,038 chars; live `/site.css` no longer contains the rule). Weglot's own
   Custom CSS field persists but does not reach the Squarespace-native picker; Squarespace header
   "Display" settings are cosmetic and expose no ARIA control. Do not retry the `display:contents` rule.

2. **PDP mobile LCP 15.0 s — owner, image assets + Squarespace.**
   LCP chain: render-blocking suggestions 1,760–1,770 ms (Squarespace Hosting HTML 159 KiB / 5.4 s,
   `static.css` 41.5 KiB / 1.35 s, `site.css?nocustom=true` 110.4 KiB / 1.8 s, `custom.css` 3.5 KiB).
   Image suggestions 205 KiB: `IMG_3347.JPEG?format=750w` 264 KiB (1536×2048 served at 634×846;
   142 KiB compression + 75 KiB responsive) and `IMG_3336.JPEG?format=750w` 97.5 KiB (27.7 KiB).
   Fix: re-export/uploads at target display size with higher compression, and set explicit
   width/height on gallery images. Platform CSS cannot be deferred on Basic plan.

3. **Shop mobile performance 66 — owner, product grid imagery.**
   Image delivery saving 1,278 KiB, payload 3,547 KiB, JS execution 1.7 s, main-thread work 3.1 s.
   Reduce thumbnail upload dimensions/quality; check whether hover-swap doubles images per card;
   remove unused Squarespace apps/integrations.

4. **Feed variant links — owner/platform decision.**
   14 duplicate `link` URLs across 98 rows. Google's `item_group_id` minimum requirements say
   variants must have different landing page URLs. Squarespace cannot deep-link a variant (accepted
   repo limitation), and a fake `?variant=` query would not select the variant — do **not** add one.
   Either accept limited variant visibility or change platform. Also 12 empty `color` rows need the
   owner's exact colour names; no guessing from photos.

5. **Small live copy issues — owner, Squarespace editor.**
   Home H1 renders `Wool knitwearfor cooler days` (missing space); one `/shop` image of 203 lacks a
   non-empty alt. Both are content edits, not code fixes.

6. **Platform-level, not fixable here:** unused JS 655–883 KiB, unused CSS 134–145 KiB, legacy JS
   34 KiB, long main-thread tasks. No Code Injection on Basic plan; no code change can remove
   Squarespace core bundles.

## Rescan loop (owner, after each fix batch)

```sh
# Browser (PSI API is keyless-quota-blocked with HTTP 429 in this environment):
for url in https://www.autumnandwool.com/ https://www.autumnandwool.com/shop \
  'https://www.autumnandwool.com/shop/p/oversized-merino-wool-v-neck-sweater-vest'; do
  for ff in mobile desktop; do
    open "https://pagespeed.web.dev/analysis?url=<urlencoded>&form_factor=$ff"
  done
done
```

Record Perf/A11y/BP/SEO/Agentic plus FCP/LCP/TBT/CLS/SI in a new dated file next to this one.
Treat ±5 Perf points and LCP changes inside the reported range as lab noise; PSI is single-run here.
Stop the loop when A11y/Agentic/SEO/BP are 100/3-of-3/100/100 and no new vendor audit appears;
mobile Perf 90+ needs the platform levers above, so do not claim it from CSS alone.
