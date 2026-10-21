# SEO & Marketplace — status 2026-10-21
Summary: 13 done · 11 blocked · 10 todo

| ID | Task | Due | Status | Output / blocker |
|---|---|---|---|---|
| SEO-01 | Feed QA of the live TSV (98 rows): structure, ids, attributes, claims, availability, images, category ids | 2026-10-21 | DONE | [feed QA](../../../business-os/seo-marketplace/feed/2026-10-21-feed-qa.md). New finding: the Brown cardigan `image_link` may serve the black photo (F5); 0 SKUs at stock 0 in the 17 Oct export, so "13 out of stock" cannot be reproduced (F2) |
| SEO-02 | Merchant Center Diagnostics summary (21 Oct checkpoint) | 2026-10-23 | BLOCKED | Owner: Diagnostics + disapproved screenshots ([owner checklist](../../../business-os/seo-marketplace/2026-10-21-owner-checklist.md) §1) |
| SEO-03 | `in_stock` bug: written patch proposal for `build_google_feed.py` (not applied) | 2026-10-27 | DONE | [generator patch proposal](../../../business-os/seo-marketplace/feed/2026-10-21-feed-generator-patch-proposal.md): stock read from the product export, fails closed, plus per-variant image map |
| SEO-04 | Feed proposal TSV: set sold-out rows to `out_of_stock` | 2026-10-24 | BLOCKED | Owner decision 4: physical stock per SKU. Repo evidence shows no row at 0; I will not mark rows without inventory evidence |
| SEO-05 | GSC + Bing set-up, sitemap, indexing requests for 5 PDPs + 5 pages, `/home` 301, `/shop/gift` | 2026-10-28 | BLOCKED | Owner (decision 10). Checklist §2–4 written. Already done: GSC URL-prefix verified, sitemap submitted 18 Oct, `/redesign-preview` returns 404 (checked 21 Oct) |
| SEO-06 | Pinterest: business account, rename or new account, claim website, UTM bio link | 2026-10-28 | BLOCKED | Owner decisions 10 and 18; checklist §6; profile text in [Pinterest plan](../../../business-os/seo-marketplace/2026-10-21-pinterest-plan.md) |
| SEO-07 | Etsy baseline: Stats + listings export | 2026-10-28 | BLOCKED | Owner decision 9 (is Mareshop still selling); then export (checklist §7) |
| SEO-08 | Query → page map v1 + keyword sheet | 2026-10-27 | DONE | [query-page map](../../../business-os/seo-marketplace/2026-10-21-query-page-map.md), [keyword sheet](../../../business-os/seo-marketplace/2026-10-21-keyword-sheet.csv). Positions are TODO until the owner sends a GSC export |
| SEO-09 | Rich Results Test request for 5 PDPs (schema check) | 2026-10-27 | DONE | Request written in [owner checklist](../../../business-os/seo-marketplace/2026-10-21-owner-checklist.md) §5; results come from the owner's screenshots |
| SEO-10 | Weekly note #1 | 2026-10-21 | DONE | [weekly note](../../../business-os/seo-marketplace/2026-10-21-weekly.md) |
| SEO-11 | Weekly notes every Monday (GSC movers, map update, 5–10 pin briefs, 3 proposals) | from 2026-10-26 | TODO | Recurring; first one on 26 Oct |
| SEO-12 | Category copy: sweaters, cardigans, vests (intro, H1, meta) | 2026-11-17 | DONE | [on-page proposals](../../../business-os/seo-marketplace/2026-10-21-onpage-proposals.md) §B, §D |
| SEO-13 | Beanies / Sets: hide or merge single-product categories | 2026-11-14 | BLOCKED | Owner decision 29; options (recommend merging into "Hats & scarves") in on-page proposals §D |
| SEO-14 | Shop H1, home second H1, alt text for 5 PDPs | 2026-11-17 | DONE | On-page proposals §A, §C. Alt-text view words are `[VERIFY]`: I could not view the photos |
| SEO-15 | SEO titles and metas: home, shop, 3 categories, size guide, cart, 6 PDPs | 2026-11-17 | DONE | On-page proposals §B + [CSV](../../../business-os/seo-marketplace/2026-10-21-onpage-proposals.csv) |
| SEO-16 | Colour twins: distinct opening lines (side-slit, stand-collar, lambswool) | 2026-11-17 | DONE | On-page proposals §E (input for CRO's PDP copy) |
| SEO-17 | Pinterest: profile, 5 boards, first 10 pin briefs | 2026-11-17 | DONE | [Pinterest plan](../../../business-os/seo-marketplace/2026-10-21-pinterest-plan.md). Posting gated by SEO-06 and the Production GREEN list (G2) |
| SEO-18 | Pinterest: 10 pin briefs per week | weekly from 2026-11-02 | TODO | Needs Creative's weekly content batch |
| SEO-19 | Etsy batch 1: score and rewrite 5 listings (title, 13 tags, attributes, description, photo order) | 2026-11-17 | BLOCKED | Ruling C14: no Etsy rewrite until owner decision 9, then the listings export (SEO-07). Tag candidates prepared in the keyword sheet and [seasonal plan](../../../business-os/seo-marketplace/2026-10-21-seasonal-keyword-plan.md) |
| SEO-20 | Etsy vs site price parity check against contribution | 2026-11-17 | BLOCKED | Production/Finance: SKU costs (G1, 11 Nov) and Etsy prices (SEO-07) |
| SEO-21 | Gift guide page proposal | 2026-11-17 | DONE | [gift guide proposal](../../../business-os/seo-marketplace/2026-10-21-gift-guide-proposal.md); order-by dates wait for Operations (G5) |
| SEO-22 | Seasonal keyword plan Oct–Dec v1 (site, Pinterest, Etsy) | 2026-10-28 | DONE | [seasonal keyword plan](../../../business-os/seo-marketplace/2026-10-21-seasonal-keyword-plan.md); no volumes (no data), each seed has a verification step |
| SEO-23 | `llms.txt` diff against the live site | 2026-11-30 | DONE | [llms.txt diff](../../../business-os/seo-marketplace/2026-10-21-llms-txt-diff.md): live file is already updated; 2 CLAIM-CHECK lines, Etsy proof line (C1), gift category added |
| SEO-24 | Variant photos: bind check, regenerated feed QA, single re-upload, Diagnostics 24–72 h later | 2026-11-14 | BLOCKED | Owner/Creative: photos per ruling C7 (turtleneck by 31 Oct; beanie, set, cardigan Blue by 14 Nov) |
| SEO-25 | Feed claims clean-up ("hand-sewn in Latvia" 79 rows, "Italian-spun" 14, "extra-fine" 15) | 2026-10-31 | BLOCKED | Owner decision 16 / G8 (claims evidence); yarn spec sheets, decision 34 (30 Nov) |
| SEO-26 | Christmas: cut-off pins per zone; push only GREEN, in-stock SKUs in pins and gift content | 2026-11-20 | BLOCKED | Operations G5 (cut-off table, published 20 Nov) and Production G2 (GREEN list) |
| SEO-27 | Re-baseline Q4 KPIs after 4 weeks of data | 2026-11-23 | TODO | Ruling C9 date |
| SEO-28 | Monthly SEO review, November (indexation, on-page, schema, llms.txt, feed QA) | 2026-11-30 | TODO | Future date |
| SEO-29 | Monthly SEO review, December | 2026-12-31 | TODO | Future date |
| SEO-30 | Etsy batch 2 (5 listings) | 2026-12-15 | TODO | Future date; same gate as SEO-19 |
| SEO-31 | Q1 2027: indexation ≥ 90%, category landing pages, care/fibre/fit guides, Etsy 5 listings per month, LV page proposals, slug clean-up only with an approved redirect list | 2027-03-31 | TODO | Future quarter |
| SEO-32 | Q2 2027: Pinterest catalog (after photos), Mother's Day page and pins, MC return/shipping extras, monthly AI-visibility test, Google Business Profile check | 2027-06-30 | TODO | Future quarter |
| SEO-33 | Q3 2027: seasonal keyword plan v2, autumn pages indexed by 31 Aug, Etsy second pass, SEO/Pinterest freelancer decision | 2027-09-30 | TODO | Future quarter |
| SEO-34 | Q4 2027: gift guides live by 1 Oct, cut-off pins per zone, year-on-year review against contribution | 2027-12-31 | TODO | Future quarter |

## Blocked on owner
- Merchant Center Diagnostics screenshots from the 21 Oct checkpoint, plus a 2-minute check of which image URL shows the brown cardigan (SEO-02, feed QA F5).
- Physical stock per SKU / made-to-order status (decision 4, 24 Oct) before any `availability` change (SEO-04); approve the generator patch (SEO-03).
- GSC Performance export (Queries + Pages) and indexing-reasons screenshot; request indexing for 10 URLs; Bing import; `/home` 301; `/shop/gift` hide or merge (SEO-05, decision 10).
- Rich Results Test screenshots for the 5 working-set PDPs (SEO-09 follow-up).
- Pinterest: rename `mmareshop` or new account, business account, claim domain, UTM bio link (SEO-06, decisions 10/18).
- Is Etsy/Mareshop still selling? Then the listings export + Stats (SEO-07, SEO-19, decision 9).
- Claims evidence for "made in Latvia/Riga", "handmade", "extra-fine", "Italian-spun" (SEO-25, decision 16 / G8).
- Hide or merge Beanies and Sets categories (SEO-13, decision 29).
- Variant photos per ruling C7 and a single feed re-upload pass (SEO-24, decision 29).
- Provisional 5 priority SKUs (decision 2, 24 Oct). My working set (cardigan, beanie, striped sweater, vest, hat and scarf set) gets swapped for the GM's list.
- Etsy proof line 1,400+ vs 1,500+ (decision 17) for `llms.txt` and the Pinterest About text.
