# lv subdomain live — 2026-11-27

- DNS: Squarespace DNS Settings, CNAME `lv` -> `2e2862a6.translate-cf.weglot.io` (registrar GoDaddy, DNS provider Squarespace).
- `dig CNAME lv.autumnandwool.com` @1.1.1.1 and @8.8.8.8 returned the target. HTTPS 200 about 2 min after saving.
- Weglot wizard: Check DNS = "Your DNS are ready!", Next reached Setup finished.
- `https://lv.autumnandwool.com/`: `<html lang="lv" data-wg-translated="lv">`, canonical self, hreflang alternates en (www) and lv present.
- Caveat: `<title>` still English there; Weglot Free is 2,704/2,000 words so new translations are not served. Owner decision on plan.
- EN `www` page: no hreflang tags (known Weglot/Squarespace limit, runbook D).
- Not done: footer Latviešu link still `#Weglot-lv`; not switched to the subdomain.

## Footer switched to real URLs (live 2026-11-27)
Footer Code block now: `<p class="aw-lang-links"><a href="https://www.autumnandwool.com/" lang="en" hreflang="en">English</a> | <a href="https://lv.autumnandwool.com/" lang="lv" hreflang="lv">Latviešu</a></p>`
Plain crawlable links, no `#Weglot-*` hooks. Both go to the home page of each language (footer is global, so the current page path is not kept).
Rollback: restore the `#Weglot-en` / `#Weglot-lv` hrefs in the same block. PageSpeed re-run not done yet.
