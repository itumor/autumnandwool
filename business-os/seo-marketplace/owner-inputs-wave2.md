# Owner inputs: SEO, Merchant Center, Pinterest, Etsy (wave 2, 2026-10-21), DRAFT

From aw-seo-marketplace. This is the **one form** for everything SEO & Marketplace needs from you. It replaces the
open items in `2026-10-21-owner-checklist.md` (that file keeps the click-by-click steps; the § numbers below point
into it). Fill the "Your answer" column, or send a screenshot/export, and say the row number. Every step is a login
step only you can do; agents never log in, edit or upload.

Rows that are the same question as another team's form are marked **SHARED**: answer once, in the place named,
and I read it from there.

| # | Question / input | Why I need it | Due | Unblocks | Your answer |
|---|---|---|---|---|---|
| 1 | Merchant Center → Products → Diagnostics: screenshot of counts (approved / limited / disapproved / pending) and the item-issues table. Plus the first page of "Disapproved" products (checklist §1) | The 21 Oct approval checkpoint. I can't see the account. Without it I can't say why free listings are or aren't live | 23 Oct | SEO-02 (also CRO-02) | |
| 2 | Which of the two image URLs in checklist §1 shows the **brown** cardigan? (open both, about 2 min) | The live feed may show the black photo on the Brown row (feed QA F5). Pin brief P4 waits on this too | 23 Oct | SEO-02, pin P4 | URL 1 / URL 2 / neither |
| 3 | **SHARED, decision 4:** physical stock per SKU, or "made to order, X working days". Answer in the stock form in `business-os/head-of-ecommerce/owner-decision-pack-2026-10-24.md` | Feed `availability` is hard-coded `in_stock` for all 98 rows. I won't change a row without your count | 24 Oct (22 SKUs by 31 Oct) | SEO-04, SEO-24, SEO-26 | (answer in GM pack) |
| 4 | Approve the generator patch proposal (`feed/2026-10-21-feed-generator-patch-proposal.md`): yes / no / changes. You or a developer apply it; I don't run the script | Stops the feed claiming stock that doesn't exist on every future regeneration | 24 Oct | SEO-04, SEO-24 | |
| 5 | **SHARED, decision 2:** the provisional 5 priority SKUs (GM proposal: raglan cardigan, Dusty Pink raglan sweater, Classic lambswool crew, hat & scarf set, beanie). Answer in the GM pack | Sets which 5 PDPs go into indexing requests (row 8), Rich Results tests (row 12), pins (row 15) and Christmas pins (row 22). My wave-2 drafts already use the GM's 5 | 24 Oct | SEO-05, SEO-09, SEO-18, SEO-26 | (answer in GM pack) |
| 6 | Search Console → Performance → last 3 months → Export: Queries + Pages (checklist §2) | The only source for positions and the 8–20 "quick win" band; all positions in the query map are TODO until then | 28 Oct | SEO-05, SEO-08 update, SEO-11, SEO-27 | |
| 7 | Search Console → Pages: screenshot of "Why pages aren't indexed" | 11 of 37 pages indexed; I need the reasons to target fixes | 28 Oct | SEO-05, SEO-28 | |
| 8 | Request indexing for 10 URLs (checklist §2; swap PDPs 3–4 for the Dusty Pink sweater and Lambswool crew if you approve the GM's 5, URLs in `2026-10-26-weekly-draft.md` §3). Tick when done | Gets the priority pages crawled before the gift season | 28 Oct | SEO-05 | done / not done |
| 9 | Bing Webmaster Tools: import from Google Search Console, submit sitemap (checklist §3). Tick when done | Bing powers ChatGPT search results | 28 Oct | SEO-05 | done / not done |
| 10 | Squarespace URL Mappings: add `/home -> / 301` (checklist §4). Tick when done | `/home` duplicates the home page in the sitemap | 28 Oct | SEO-05 | done / not done |
| 11 | `/shop/gift`: hide, or merge into `/shop/winter-wool-gifts`? (gift guide proposal, option A) | Two thin gift pages compete for "wool gifts" | 28 Oct | SEO-05, SEO-21 follow-up | hide / merge / keep |
| 12 | Rich Results Test (search.google.com/test/rich-results) on the 5 priority PDPs, one screenshot each (checklist §5) | A page fetch can't see script-injected schema; this confirms Product + price + availability | 28 Oct | SEO-09 follow-up, SEO-28 | |
| 13 | Pinterest: rename legacy `mmareshop` to Autumn & Wool (keeps followers) **or** open a new account? (decisions 10 and 18) | Every pin and the profile text wait on which account | 28–31 Oct | SEO-06, SEO-17, SEO-18 | rename / new |
| 14 | Pinterest: convert to business account, claim `autumnandwool.com`, paste bio link `https://www.autumnandwool.com/shop?utm_source=pinterest&utm_medium=social&utm_campaign=bio-link` (checklist §6). Tick when done | Analytics, rich pins, tracked profile clicks | 31 Oct | SEO-06 | done / not done |
| 15 | **SHARED, decision 18 / ruling C15:** approve one pin UTM pattern. I propose Growth's registered pattern `utm_source=pinterest&utm_medium=social&utm_campaign=autumn-2026&utm_content=pin-<product>` (replaces my earlier board-slug campaign) | One taxonomy across teams; GA4 groups all pins under one campaign | 31 Oct | SEO-18, SEO-26 | yes / change |
| 16 | **SHARED, decision 9:** is Etsy/Mareshop still selling, and do both channels stay open this season? | Ruling C14: no Etsy listing work until you answer | 28 Oct | SEO-07, SEO-19, SEO-20, SEO-30 | active / paused / closing |
| 17 | If Etsy is active: Shop Manager → Settings → Options → Download data → Listings CSV, plus Stats → last 30 days screenshot of the listing table (checklist §7) | Baseline before any rewrite; Etsy prices for the parity check | 28 Oct (after row 16) | SEO-07, SEO-19, SEO-20 | |
| 18 | **SHARED, decision 16 / G8:** evidence for "knitted on a manually operated knitting machine and hand-sewn in Latvia" (79 feed rows), "extra-fine" (15), "Italian-spun" (14), "handmade". Spec sheets / invoices per yarn by 30 Nov (decision 34) | Feed and listing descriptions keep only claims with evidence; I propose plain "100% merino wool" if none | 31 Oct (spec sheets 30 Nov) | SEO-25, SEO-19 | |
| 19 | **SHARED, decision 17:** one Etsy proof line (1,400+ or 1,500+ reviews) and whether verbatim Etsy quotes may be used | Needed in `llms.txt`, the Pinterest About text and Etsy-to-site wording | 31 Oct | SEO-23 follow-up, SEO-06, SEO-19 | 1,400+ / 1,500+; quotes yes/no |
| 20 | **SHARED, decision 29:** Beanies and Sets categories (1 product each): merge into one "Hats & scarves" category, hide, or keep? | Thin pages drag on indexing | 14 Nov | SEO-13 | merge / hide / keep |
| 21 | **SHARED, decision 29 / ruling C7:** variant photos uploaded and bound in Squarespace per colour, or "trim this row". Tick per colour in `2026-10-21-variant-bind-check.csv` (turtleneck by 31 Oct; beanie, set, cardigan Blue by 14 Nov) | 48 feed rows show the wrong colour; one re-upload pass after binding | 31 Oct / 14 Nov | SEO-24 (also CRO-23/24, CRE-12/13) | (tick in CSV) |
| 22 | Approve the approach for Christmas cut-off pins (`2026-10-21-christmas-cutoff-pins-draft.md`): one pin per zone, dates filled only from the Operations table you approve on 20 Nov, pins edited/archived the day after each cut-off | Gift pins must not promise delivery dates the carriers don't back | 20 Nov | SEO-26 | yes / change |
| 23 | **SHARED, G1 (Finance/Production form):** confirmed SKU costs in `sku-economics.csv`. Answer in `business-os/finance/cost-collection-request-2026-10-21.md` | The Etsy vs site price parity check needs the contribution per SKU | 11 Nov | SEO-20 | (answer in Finance form) |

## What I do once you answer
- Rows 1–2 → Diagnostics summary within 1 working day (SEO-02).
- Rows 3–4 → feed proposal TSV with `availability` from your counts (SEO-04).
- Rows 6–7 → query→page map v2 with real positions, weekly note (SEO-08, SEO-11).
- Rows 16–17 → Etsy batch 1 proposals using `2026-10-21-etsy-batch-prep.md` (SEO-19).
- Row 21 → bind check, regenerated-feed QA and a re-upload checklist (SEO-24).

DRAFT: nothing sent, no live change.
