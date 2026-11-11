# Backlink Profile: autumnandwool.com (2026-11-10)

Tier: 0 (Common Crawl + verify crawler only). No Moz, Bing or Keywords Everywhere keys.
Backlink Health Score: **INSUFFICIENT DATA** (fewer than 4 scoring factors have data; no numeric score issued).

## Source coverage

| Source | Status | Result |
|---|---|---|
| Common Crawl web graph (cc-main-2026-jan-feb-mar, fetched 2026-11-10) | Ran | Domain **not in Common Crawl graph** (too new / too few links). No PageRank, harmonic centrality, host count or referring hosts. Confidence 0.50. |
| Referring domain count | Not available | Not in CC graph; no paid source configured |
| Backlink verification crawler | Not run | No known backlink list supplied |
| Moz (DA, PA, spam score, anchors) | Not configured | Skipped |
| Bing Webmaster inbound links | Not configured | Skipped |
| Anchor text, toxicity, velocity, follow ratio, geo relevance | Not available | Skipped |

Result: not in Common Crawl graph (too new / too few links). No referring-domain count, rank, or referring hosts can be reported.

## Outbound brand links (on-disk HTML, no re-crawl)

Source files: `crawl/_root.html` (homepage) and `crawl/about.html`. Parsed (confidence 0.95).

| Platform | URL in HTML | Owner | Rating |
|---|---|---|---|
| Instagram | https://www.instagram.com/autumnandwool | Autumn & Wool | Pass |
| TikTok | https://www.tiktok.com/@autumnandwool | Autumn & Wool | Pass |
| Etsy | https://www.etsy.com/shop/mareshop | **Mareshop** | Warn |
| Pinterest | https://www.pinterest.com/mmareshop/ | **Mareshop** | Warn |
| Facebook | https://www.facebook.com/AccessoriesMareshop | **Mareshop** | Warn |
| Company registry | https://company.lursoft.lv/en/autumn-and-wool/40203644965 | Business registry listing (not a social profile) | Info |

Finding (High): three of six outbound brand links (Etsy, Pinterest, Facebook) point to the legacy "Mareshop" profiles, not Autumn & Wool. Visitors and any crawler reading these links see a different brand. Owner decision needed: repoint to Autumn & Wool profiles or confirm the Mareshop accounts are intentional. Do not change without owner input.

Each profile URL appears in both saved files (raw HTML hrefs; placement on the page not checked).

## Realistic link sources for a small handmade-knitwear shop (no volume estimates)

1. **Etsy shop profile**: the Etsy shop link exists only as the Mareshop shop. Owner-controlled Etsy listing or shop-about page linking to autumnandwool.com would be a first-party link, if the Etsy shop is the same business.
2. **Pinterest**: pin product and fit-guide images with links to autumnandwool.com pages (shop, size guide, merino-vs-lambswool). Repoint the existing Mareshop Pinterest profile or create a branded one.
3. **Maker and craft directories**: handmade and small-business directories with a free business profile (for example, a country maker directory or a craft marketplace profile). Verify each listing exists before counting it.

## Next steps

- Owner: decide whether Etsy, Pinterest and Facebook should point to Autumn & Wool or stay Mareshop.
- Re-run Common Crawl after the next quarterly web graph release (source: https://commoncrawl.org/web-graphs). Absence is expected for a new domain.
- Re-check with Moz or Bing once a key is configured (`"$HOME/.claude/skills/seo/scripts/claude-seo" run backlinks_auth.py --check --json`).
