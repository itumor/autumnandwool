# Language switcher ARIA fix — live 2026-11-27

Problem: PageSpeed "Agent accessibility → Accessibility tree is not well-formed". Failing element was the
Squarespace/Weglot header switcher `div#multilingual-language-picker-desktop[role=listbox]` with no `option` children.
Markup is Squarespace-owned; CSS cannot change roles and Code Injection is plan-gated.

## What changed (live, no DNS, no subdomain, no plan change)

1. **Footer Code block** added in Site Footer (global), moved to the empty right-hand footer cell:
   `<p class="aw-lang-links"><a href="#Weglot-en" lang="en" hreflang="en">English</a> | <a href="#Weglot-lv" lang="lv" hreflang="lv">Latviešu</a></p>`
   Weglot rewrites these to `a.weglot-link-en` / `a.weglot-link-lv` and handles the click itself.
2. **Site Header → Add Elements → Language Switch = off.** Built-in listbox no longer rendered.
Latvian stays Public; translations untouched.

## Observed before the change (read-only test on the live site)
Injecting `<a href="#Weglot-lv">` in the page and clicking it switched to Latvian (`html lang` en-US → lv, title translated)
on the same URL. A hash-only navigation does NOT trigger it; a click does.

## Validation (live, ego-browser, 2026-11-27)

| Check | Result |
|---|---|
| `[role=listbox]` elements on `/` and `/cart` | 0 |
| Footer link → Latviešu from fresh load | `html lang` = lv, LV title |
| Footer link → English | `html lang` = en, EN title |
| `site.css` overlay guard `pointer-events:none !important` on `.sqs-widgets-confirmation-overlay` | present |
| `/cart` loads | yes |
| PageSpeed desktop (`pagespeed.web.dev/analysis/https-www-autumnandwool-com/9b2lprtv2pyjz50g8hoe1j?form_factor=desktop`) | Accessibility 100, **Agentic Browsing 3/3**, no failing agent audit |
| PageSpeed mobile (same run) | Accessibility 100, Agentic Browsing 3/3 |

## Known quirks (not fixed)
- On the Latvian view the English link label is machine-translated to "Angļu". Cosmetic.
- A quick EN→LV→EN toggle in one session once missed a click; a fresh load always switched. Re-check after any Weglot change.
- Footer links are plain white text without underline in the code block; other footer links are underlined.

## Rollback
Site Header → Add Elements → Language Switch = on, Save. Footer → delete the Code block, Save.

## Not done / still open
No subdomain, hreflang, paid Weglot plan or native Latvian review (G1–G3 in `live-setup.md`). Not committed.
