# SXO / search-intent findings — autumnandwool.com — 2026-11-10 re-audit

Source: seo-sxo specialist (Haiku), crawl snapshot 17:10 EET, 9 web searches as a proxy for Google (not live SERP, no positions).
Manager note: the specialist's X-03 suggested HowTo/FAQ schema; dropped. HowTo is deprecated and FAQ rich results were retired 2026-05-07. Article schema is the only relevant gap, and it needs code injection (platform limit).

## Intent match per page

| Page | Intent match | Top gap |
|---|---|---|
| /wool-sweaters | partial | no prices or filters in the grid (X-01) |
| /wool-cardigans | partial | 4 SKUs, no prices (X-01) |
| /wool-sweater-vests | partial | 2 SKUs, 224 words (X-01) |
| /wool-hats-and-scarves | partial | 2 SKUs, no prices (X-01) |
| /wool-gifts | yes (gift guide) | no December delivery cut-off (X-06) |
| /how-to-wash-a-wool-sweater | yes | no visuals; no Article schema (platform limit) (X-03) |
| /merino-vs-lambswool | yes | no durability/allergy section, no table (X-05) |
| /oversized-fit-guide | yes | no size table (X-04) |
| /how-to-choose-a-wool-cardigan | yes | no price band or comparison table; SERP is thin |
| Home | no, for head terms | H1 "Wool knitwear for cooler days" has no product or fibre term (X-09) |
| /shop | partial | no H1, boilerplate meta (X-08) |
| Product (oversized merino vest) | yes (PDP) | no product review text; delivery sits below images (X-07) |

Head-term SERPs ("wool sweater women", "merino wool cardigan women", "merino wool hat and scarf set") are retailer listing pages with prices, filters and ratings (Lands' End, L.L.Bean, Falke, M&S, Ralph Lauren). Guide pages match SERP type.

## Findings

| ID | Severity | Finding |
|---|---|---|
| X-01 | High | /wool-* landing pages list product names only: no price, no filters, unlike every ranking listing page |
| X-02 | High | Cannibalisation: /wool-gifts vs /shop/winter-wool-gifts and /shop/gift (worst); /wool-sweaters vs /shop/sweaters; /wool-cardigans vs /shop/cardigans; /wool-sweater-vests vs /shop/vests; /wool-hats-and-scarves vs /shop/beanies--hats and /shop/sets |
| X-03 | Medium | Guides carry only WebSite / Organization / LocalBusiness data, no Article (platform limit) and no visuals |
| X-04 | Medium | /oversized-fit-guide has no size table |
| X-05 | Medium | /merino-vs-lambswool lacks durability/allergy section and a comparison table |
| X-06 | High | /wool-gifts has no December delivery cut-off |
| X-07 | Medium | PDP: no review text; delivery info below images |
| X-08 | Low | /shop has no H1, boilerplate meta |
| X-09 | Low | Home H1 has no product or fibre term |

## Long-tail opportunities (specialist's judgement, no volume data)

1. "hand-finished merino cardigan made in Latvia"
2. "oversized merino sweater vest women" (PDP already has garment measurements)
3. "how to hand wash merino sweater" (guide matches; SERP has weak domains)
4. "oversized wool sweater size chart" (needs X-04)
5. "merino or lambswool which is warmer"

Head terms: under about 5% page-1 chance for a new low-authority domain (specialist's estimate, not measured).

## Persona scores (0-10, judgement, not user tests)

| Page | Gift buyer (Dec) | Quality buyer | Mobile IG | Biggest friction |
|---|---|---|---|---|
| Home | 5 | 6 | 6 | no gift route in the hero |
| /wool-gifts | 7 | 5 | 5 | no December cut-off, 4 SKUs |
| Product vest | 6 | 8 | 5 | no product reviews; delivery below images |

## Limits

Web search proxy only; titles and snippets, not full competitor pages. Static crawl snapshot. No GSC data for the five new pages yet.
