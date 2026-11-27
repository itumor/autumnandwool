# Weglot Free trim — live 2026-11-27

Goal: keep Latvian working on the free plan (2,000 words).

Before: Dashboard URLs list showed `/shop` 1,844 words, each product page about 330, home 415; project 2,704/2,000, translations not served (lv title/H1 stayed English).

Change (Weglot > Settings > Translation Exclusions): rule **Starts with `/shop`**, behavior "URL redirects to Original URL", "Delete translations linked to matching URLs" ON. Matched 23 URLs (shop + all product pages). Deleted 273 automatic + 1 reviewed translation (the reviewed one was not identified before deletion).
A first save picked a single product URL from the autocomplete by mistake; removed it, then saved the correct `/shop` rule.

After (curl, 2026-11-27):
| URL | Result |
|---|---|
| lv `/` | title "Vilnas džemperi un jakas no Rīgas" |
| lv `/contact` | Latvian |
| lv `/wool-hats-and-scarves` | Latvian |
| lv `/shipping-returns` | Latvian ("Piegāde un preču atgriešana") |
| lv `/shop` | redirects to `www.autumnandwool.com/shop` (English) |

Trade-off: shop and product pages are English only. Latvian visitors see translated home, contact, shipping and returns, hats page; checkout/shop remain English.
Rollback: delete the exclusion rule in Weglot. Words limit message in the dashboard may stay until the monthly counter resets.
Open: check exact usage after the counter refreshes; add reviewed LV copy (`lv-money-pages-draft.md`) when native reviewer available.
