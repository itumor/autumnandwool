# lv subdomain live — 2026-11-27

- DNS: Squarespace DNS Settings, CNAME `lv` -> `2e2862a6.translate-cf.weglot.io` (registrar GoDaddy, DNS provider Squarespace).
- `dig CNAME lv.autumnandwool.com` @1.1.1.1 and @8.8.8.8 returned the target. HTTPS 200 about 2 min after saving.
- Weglot wizard: Check DNS = "Your DNS are ready!", Next reached Setup finished.
- `https://lv.autumnandwool.com/`: `<html lang="lv" data-wg-translated="lv">`, canonical self, hreflang alternates en (www) and lv present.
- Caveat: `<title>` still English there; Weglot Free is 2,704/2,000 words so new translations are not served. Owner decision on plan.
- EN `www` page: no hreflang tags (known Weglot/Squarespace limit, runbook D).
- Not done: footer Latviešu link still `#Weglot-lv`; not switched to the subdomain.
