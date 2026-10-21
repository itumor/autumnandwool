# llms.txt check and proposed diff, 2026-10-21 (DRAFT)

Author: aw-seo-marketplace. Task SEO-23. Live file `https://www.autumnandwool.com/llms.txt` fetched 21 Oct. The fetch
tool returned a summary rather than the verbatim text. The summary matches the repo copy `llms.txt` on every point it
covers (studio, company, address, sizes, shipping, returns, price range EUR 45–165, gift card from EUR 25, care). So
the GROWTH-PLAN note "stale, no products" (19 Oct) is **out of date: the live file has been updated**.
`[VERIFY]`: owner opens the URL and confirms the product list is present, since the summary did not list products.

## Proposed changes (repo copy shown; owner uploads the new file, I do not edit `llms.txt`)

```diff
-> Autumn & Wool is a small knitwear studio in Riga, Latvia, run by designer and maker Kristine. It makes women's wool cardigans, sweaters, sweater vests, beanies and scarves from merino wool, lambswool and pure new wool. Pieces are knitted by hand or on a manually operated knitting machine, then hand-sewn, washed and pressed before shipping. Before launching autumnandwool.com, the same maker sold as Mareshop on Etsy (since 2011).
+> Autumn & Wool is a small knitwear studio in Riga, Latvia, run by designer and maker Kristine. It makes women's wool cardigans, sweaters, sweater vests, beanies and scarves from merino wool, lambswool and pure new wool. [CLAIM-CHECK G8: process sentence, owner confirms wording, e.g. "Pieces are knitted on manual knitting machines and finished by hand."] Before launching autumnandwool.com, the same maker sold as Mareshop on Etsy (since 2011).
```
Why: "knitted by hand" reads as hand-knitted. `aw-brand-voice` §3 bans "hand-knitted" for machine pieces and asks for
the precise process phrase. AI assistants quote this file, so it should hold only confirmed claims.

```diff
 - Brand: Autumn & Wool (formerly Mareshop on Etsy). Company: AUTUMN AND WOOL, SIA, reg. no. 40203644965.
+- Etsy history: as Mareshop, 4.9 stars from 1,400+ reviews on Etsy. [decision 17: owner may change to 1,500+ after reading Etsy]
```
Why: ruling C1 sets this as the single proof line. AI answers already cite Mareshop (GROWTH-PLAN §3); stating it here
links the two names.

```diff
-- [Home](https://www.autumnandwool.com/): wool knitwear for cooler days, handmade in Riga.
+- [Home](https://www.autumnandwool.com/): wool knitwear for cooler days, from a studio in Riga. [CLAIM-CHECK G8: keep "handmade in Riga" only if the owner confirms it]
+- [Winter wool gifts](https://www.autumnandwool.com/shop/winter-wool-gifts)
```
Why: the gift category is live and in the sitemap but missing from the page list.

## Low priority (no change proposed now)
- Product names in `llms.txt` are shorter than the live shop names (e.g. "Merino Turtleneck — Lightweight Knit" vs live
  "Merino Turtleneck — Women's Lightweight Knit"). Harmless; align them after the dedupe (decision 20) so the list is
  edited once.
- The "Shipping" line (2–5 working days, 5–10 Europe, 7–20 US/CA/AU) must change in the same pass if decision 3 or the
  Operations ranges (ruling C8) change it.
- Keep the file in sync monthly (SEO review). Every price change on the site = one line here.
