---
name: aw-multilingual-weglot
description: Use when touching the Latvian (lv.) site, Weglot, the language switcher or footer language links, the PageSpeed "Agentic Browsing / accessibility tree is not well-formed / listbox" failure, Weglot word-limit or exclusions, or adding DNS records for autumnandwool.com.
---

# aw-multilingual-weglot — Squarespace 7.1 + Weglot Free (EN / LV)

Live facts verified 2026-11-27 (PR #144). Evidence in `evidence/multilingual-2026-11-27/`.

## State
- Languages: English `www.autumnandwool.com`, Latvian `lv.autumnandwool.com` (Weglot subdomain mode, project `autumn-wool`).
- DNS: registrar GoDaddy, **DNS provider = Squarespace** (nameservers `dns1-4.p01.nsone.net` are Squarespace's NS1, not a separate account). Edit records at Squarespace > Domains > DNS Settings. Record: CNAME `lv` -> `2e2862a6.translate-cf.weglot.io`. Adding a record needs Google re-verification (human step).
- Header: Squarespace Language Switch is **off**. It renders `div[role=listbox]` with no `option` children, which fails Lighthouse `aria-required-children` and the Agentic Browsing category. Do not turn it on.
- Footer Code block (global, right cell): `<p class="aw-lang-links"><a href="https://www.autumnandwool.com/" lang="en" hreflang="en">English</a> | <a href="https://lv.autumnandwool.com/" lang="lv" hreflang="lv">Latviešu</a></p>`. Plain links, no script. They go to each home page (footer is global, path is lost).
- Weglot Free = 2,000 words. Exclusion rule **Starts with `/shop`** (redirect to original URL, translations deleted) keeps usage under the limit. So `/shop` and all products stay English; home, contact, hats page, shipping-returns are Latvian.

## Gotchas
- Over the word limit Weglot stops serving new translations (title/H1 stay English, API 403). Words are translated lazily on request; after freeing words, a page fills in on its next visit.
- `#Weglot-lv` hooks work only on click (Weglot rewrites them to `#`); hash navigation does nothing. Prefer real URLs now.
- Weglot translates the English link label to "Angļu" in LV view if the link is not marked notranslate.
- Subdomain EN pages carry no hreflang (Weglot limitation); LV pages have hreflang en+lv and a self canonical.
- Weglot setup wizard defaults to Subdirectories: pick Subdomains before Next. Use "Set DNS manually", not Entri Quick Connect.
- Weglot exclusion URL field is an autocomplete: typing `/shop` then clicking elsewhere can select a product URL instead. Click the exact `/shop` suggestion, check the "N URLs will be excluded" line (expect 23), then Save twice (second Save confirms the delete warning).
- Never print the Weglot project API key.

## Do not
- Pay for a Weglot plan or enter card details: owner decision.
- Add script/Code Injection (plan-gated) or another language switcher widget.

## Verify after any change
1. `curl -sL https://lv.autumnandwool.com/ | grep -E '<html|<title|hreflang'` shows `lang="lv"` and a Latvian title.
2. `grep -c 'role="listbox"'` is 0 on `www` and `lv`.
3. PageSpeed Accessibility 100 and Agentic Browsing 3/3, desktop and mobile.
4. Overlay guard `pointer-events:none !important` on `.sqs-widgets-confirmation-overlay` still in `/site.css`.

## Rollback
Weglot > Translation Exclusions: delete the `/shop` rule. Footer: restore `#Weglot-en` / `#Weglot-lv` hrefs. Header: Language Switch on (reintroduces the listbox failure). DNS: delete the `lv` CNAME.
