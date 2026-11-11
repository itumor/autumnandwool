# AI Search Readiness re-audit: autumnandwool.com (after, 2026-11-10)

Scope: seo-geo + seo-agentic pass, evidence first. Sources: `after/crawl/pages.tsv` (59 rows), `after/crawl/html/*.html` (52 rendered HTML pages, live `/llms.txt`, `/robots.txt`, sitemap). Text and JSON-LD were extracted from the captures into scratch files (not in the repo). Live requests were limited to: one `agent_ux_check.py` run on `/`, 4 `/.well-known` probes, 1 `/index.md` probe, 1 `Accept: text/markdown` probe on `/`, `/llms.txt` headers, and a `/robots.txt` hash comparison. The root HTML capture (`crawl/html/https-www-autumnandwool-com.html`, 175,903 bytes) is now populated; the first audit had it empty.

## Score: 78 / 100 (AI Search Readiness), was 64

Analyst judgement, same five sub-scores and rubric as the first audit.

| Area | First audit | Now | Change |
|---|---|---|---|
| AI crawler access | 20 / 20 | 20 / 20 | 0. Unchanged |
| llms.txt | 12 / 20 | 16 / 20 | +4 |
| Citability | 14 / 25 | 19 / 25 | +5 |
| Entity clarity | 9 / 20 | 12 / 20 | +3 |
| Agent readiness | 9 / 15 | 11 / 15 | +2 |
| **Total** | **64** | **78** | **+14** |

### Point-by-point reasons

**Crawler access, 20 / 20, no change.** `after/crawl/html/...robots-txt.html` is byte-identical (md5 `20c415ee...`) to the live `/robots.txt` fetched now. The single `User-agent: *` group has no `Disallow: /`. The named AI bots carry no own Disallow. Nothing blocks content pages.

**llms.txt, 12 to 16.**
- Gains: internal notes gone (G-03). The "since 2011" line is gone (G-04). Prices are gone (G-15). Imprint, privacy, cookie and both gift pages are listed (G-14). The nine new guides are listed. All 48 links return 200 in the crawl and are in the sitemap, except the home URL, which is not listed in llms.txt (intended).
- Losses: "Pieces are knitted by hand or on a manually operated knitting machine" contradicts the site (N-01): -1. Nine guide labels differ from live titles (N-02): -1.
- The `X-Robots-Tag: noindex` header is still served (G-13), a platform limit, so the file is not capped beyond the two deductions above.

**Citability, 14 to 19.**
- Gains: the nine new pages are self-contained and quotable. Each has one H1 and a meta description. Facts are stated plainly: fibre per style, the wash steps, the S to XL and EU/UK/US size mapping, the free shipping to Latvia and the US, 14-day unworn-and-unused returns, who designs and makes the pieces, and the Riga studio address. Examples: `wool-gifts` "Under EUR 50: a rib-knit beanie ... costs EUR 45"; `oversized-fit-guide` "S is 84 to 90 cm around the chest ... Sizes S to XL convert to EU 36 to 42, UK 8 to 14 and US 6 to 12". Prices quoted on those pages match the Product JSON-LD (EUR 136, 110, 145, 25).
- Losses: the eight `/shop/*` category pages and `/cart` still have no H1 and no meta description (G-10, pages.tsv `h1_count` 0, `desc_len` 0): -2. FAQ says "unworn, unwashed items" while the shipping page says "Unworn, unused items" (G-11): -2. Product JSON-LD still has no material, colour or size (G-09): -1. The About figures are now labelled "on Etsy" with a link, but still undated: 0 (partly fixed).

**Entity clarity, 9 to 12.**
- Gains: the conflicting contact is gone. Organization `email` is `autumnandwool@gmail.com` on all 52 pages, the same as the imprint, shipping page and llms.txt. `info@autumnandwool.com` and `+37129838090` do not appear anywhere in `after/crawl` (grep, 0 hits). The Etsy history is now stated the same way in the footer ("Formerly Mareshop on Etsy"), About, and llms.txt ("previously Mareshop on Etsy, about 15 years").
- Losses: Organization still has no `name`, `url` or `logo` (G-02): -2. LocalBusiness `name` is still "AUTUMN AND WOOL, SIA" (legal form). `sameAs` is unchanged and still points to legacy `facebook.com/AccessoriesMareshop` and `pinterest.com/mmareshop`, with no Etsy profile (G-16): -2. LocalBusiness `image` is a Squarespace folder URL, not an image (N-03): -1. `telephone` is an empty string on every page (N-05): -1.

**Agent readiness, 9 to 11.**
- Gains: all 20 home images carry an `alt` attribute (`pages.tsv` `img_no_alt` 0, was 4) (G-08). The newsletter email field now has a `<label class="newsletter-form-field-label">` (G-06). All new pages have one H1. Static HTML: 0 anchors without an accessible name on all 52 pages.
- Live `agent_ux_check.py` on `/` (this run): score 97, `unnamed_interactive: 1`, `inputs_without_aria: 1`, 515 a11y nodes, 0 `div onclick` widgets (first audit: 505 nodes, same score). One unnamed interactive control remains, so G-07 is only partly fixed.
- No change: `/.well-known/api-catalog`, `/.well-known/agent-card.json`, `/.well-known/ai-catalog.json`, `/.well-known/oauth-protected-resource`, `/index.md` all return 404 live (G-17). `Accept: text/markdown` on `/` returns `text/html`.
- Losses: the 199 of 203 images on `/shop` (96 of 100 on `/shop/sweaters`) have `alt=""` (N-04): -1. The PSI link-name failure was not re-run.

## Status of first-audit findings G-01 to G-18

Counts: FIXED 6, PARTLY FIXED 4, OPEN 6, NOT FIXABLE ON PLATFORM 2.

| ID | Status | Fresh evidence |
|---|---|---|
| G-01 | FIXED | Organization JSON-LD on 52 pages: `"email":"autumnandwool@gmail.com","telephone":""`. Zero hits for `info@autumnandwool` or `29838090` in `crawl/html`. |
| G-02 | OPEN | Organization keys still `legalName, address, email, telephone, sameAs, @type` (no `name`, `url`, `logo`). LocalBusiness `"name":"AUTUMN AND WOOL, SIA"`. |
| G-03 | FIXED | Live `llms.txt` contains no "do not describe", "Check the actual fibre", "as checked on", "not guaranteed" or "gift-wrap" text. Structure is link lists and "Key facts" lines. |
| G-04 | FIXED | No "2011" in llms.txt. Now "previously Mareshop on Etsy (about 15 years)", matching About: "15years as Mareshop on Etsy". |
| G-05 | PARTLY FIXED | About now reads "8,000+orders on Etsy", "4.9★from 1,400+ reviews on Etsy" with link to `etsy.com/shop/mareshop`. Figures still not dated. |
| G-06 | PARTLY FIXED | Label now present (`newsletter-form-field-label`). The status text "This newsletter signup form needs a storage option" is still in the DOM of 53 pages inside `newsletter-form-banner--hidden`. Sign-up not tested. |
| G-07 | PARTLY FIXED | Static HTML: 0 unnamed anchors. Live `agent_ux_check` on `/`: `unnamed_interactive: 1`. PSI not re-run, so the 6-of-6 PSI failure is unverified. |
| G-08 | FIXED | Home `img` 20, no `alt` attribute on any (`pages.tsv` `img_no_alt` 0). |
| G-09 | OPEN | Product JSON-LD keys across 22 products: `@context, @type, brand, description, image, name, offers` only. No material, colour, size, gtin or url. 15 of 15 AggregateOffers have no `url`. |
| G-10 | OPEN | `/shop` and `/shop/beanies--hats, cardigans, gift, sets, sweaters, vests, winter-wool-gifts`: `h1_count` 0, `desc_len` 0 in pages.tsv. `/cart` `desc_len` 0. The nine new pages do have H1 and descriptions. |
| G-11 | OPEN | faq: "Returns are accepted within 14 days of delivery for unworn, unwashed items". shipping-returns: "Unworn, unused items can be returned within 14 days of delivery." llms.txt: "unworn, unused". |
| G-12 | PARTLY FIXED | `/home` canonical is now `https://www.autumnandwool.com` (pages.tsv). `/home` is still in `sitemap.xml` (1 entry). |
| G-13 | NOT FIXABLE ON PLATFORM | Live `curl -sI /llms.txt`: `x-robots-tag: noindex`. |
| G-14 | FIXED | llms.txt lists `/imprint`, `/privacy-policy`, `/cookie-policy`, `/shop/gift`, `/shop/winter-wool-gifts`, and all nine guides. |
| G-15 | FIXED | llms.txt product lines have titles and links only, no prices. |
| G-16 | OPEN | `sameAs` unchanged: Instagram, TikTok, `facebook.com/AccessoriesMareshop`, `pinterest.com/mmareshop`. No Etsy URL. No new off-site search run. |
| G-17 | NOT FIXABLE ON PLATFORM | Live 404 for `/.well-known/api-catalog`, `/.well-known/agent-card.json`, `/.well-known/ai-catalog.json`, `/.well-known/oauth-protected-resource`, `/index.md`. No markdown negotiation. |
| G-18 | OPEN (not re-tested) | Checkout and add-to-cart not run (would change a cart). Beanie colour-default behaviour unverified. Prior project memory only. |

## New findings

| ID | Severity | Finding | Evidence | Fix | Layer |
|---|---|---|---|---|---|
| N-01 | Medium | llms.txt says pieces are "knitted by hand or on a manually operated knitting machine". The site says machine-knitted: footer "Machine-knitted, hand-finished knitwear by Kristine", About "Knitted on a manual knitting machine", guides "knitted on a manual knitting machine and finished by hand". "By hand" is not stated on any page text. | `after/crawl/html/...llms-txt.html` blockquote; footer on `...wool-sweaters.html` | In llms.txt, replace with "Pieces are knitted on a manual knitting machine in Latvia, then hand-finished, washed and pressed before shipping." (same wording as About). | (g) |
| N-02 | Low | Nine guide labels in llms.txt do not match the live `<title>` (for example llms "Wool sweaters" vs live "Wool Sweaters, Oversized and Relaxed \| Autumn & Wool"). The first audit's wording check asked for titles to match. | Compared in the llms.txt check against pages.tsv `title` | Use the live title text for those nine lines, or keep short labels and state that. | (g) |
| N-03 | Low | LocalBusiness JSON-LD `image` is `https://static1.squarespace.com/static/.../t/6925818ed87343383b55e7bc/1794322646867/`, a folder path, not a file. Organization and WebSite use a different asset. | JSON-LD on all 52 pages | Set the logo and a real image in Business Information. This is a settings field, not code. | (a) |
| N-04 | Low | Category and shop grids: 199 of 203 `img` on `/shop`, 96 of 100 on `/shop/sweaters`, 22 of 26 on `/shop/vests`, 40 of 44 on `/shop/winter-wool-gifts` have `alt=""`. Product names are present as link text, so the link is named, but photos carry no colour or style text. | `after/crawl/html/...shop*.html`, attribute count | Add product image alt text (colour and style) in product image settings. Product names already cover the link. | (d) |
| N-05 | Low | Organization `telephone` is `""` and WebSite `description` is `""` on all 52 pages. Empty strings add noise and give no contact-by-phone. Visible site has no phone number, so this is consistent with the page but is an empty field. | JSON-LD on all 52 pages | Remove the empty phone field if no phone is published. Set the WebSite description to the one-line summary from the About page. | (a) |

## Not checked or limited

- PSI / Lighthouse not re-run (G-07 unverified). `lighthouse_agentic.py` was not run.
- Checkout, add-to-cart and the beanies colour default not tested (G-18). No cart changes made.
- Newsletter storage and sign-up not tested (G-06). No form submitted.
- Off-site brand presence (G-16) not re-searched.
- Squarespace AI-crawler toggle not read from the UI. Inferred from robots.txt.
- `agentic_check.py`, `ucp_check.py`, `lighthouse_agentic.py` and the full `--ua-matrix` markdown test not run. Markdown negotiation tested only with one `Accept` header on `/`.
- Quantity inputs on product pages carry a group `aria-label="Quantity"`; not logged as a finding.
- Claims on the nine new pages (for example "Every order is packed by hand in our Riga studio") were checked against the shipping page and are present there. Claims that appear on one page only were not checked against an external source.
