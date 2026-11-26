# Product feeds: what is here and what is safe to upload

One generator owns both feeds: `build_google_feed.py` at the repo root. It is the only
script allowed to write feed files. Never hand-edit a TSV; change the generator and re-run.

## Files

| File | Status | Uploadable? |
|---|---|---|
| `/autumnandwool-google-feed.tsv` (repo root, 98 rows, 19 cols) | Last uploaded to Google Merchant Center 19 Oct 01:31 EET; regenerated 25 Nov to remove promotional text from descriptions. Regeneration is byte-identical only while generator inputs and copy constants are unchanged | Yes, after the owner does the single re-upload pass (C7 photos + claims + colours) |
| `2026-11-25-openai-feed-DRAFT-do-not-upload.tsv` (98 rows, 26 cols) | Draft OpenAI / ChatGPT feed from the same data. `target_countries=LV,EE,LT` is **a starting guess, not an owner decision** | **No.** Blocked on the owner claiming the business in OpenAI Business Hub (GEO-02 owner actions 6) and on eligibility being confirmed |
| `2026-10-21-feed-availability-proposal-wave3.md` + `-diff-wave3.csv` | Proposal only; its stock rule (A-PRD-12/13) is still an assumption | No |
| `2026-10-21-feed-generator-patch-proposal.md` | The problem statement the 25 Nov generator patch implements | n/a, historical |
| `2026-10-21-feed-qa.md` | Read-only QA of the 21 Oct TSV. F1 (hard-coded availability), F9 (generator drift) and F5 (cardigan image) are now fixed in code. F2, F3, F4, F6 need owner input | n/a |

## Commands

```bash
# Google feed only (writes the file Merchant Center reads)
python3 build_google_feed.py products_Oct-17_10-46-00PM.csv autumnandwool-google-feed.tsv

# Google + OpenAI draft; the OpenAI file is the second argument to --openai
python3 build_google_feed.py products_Oct-17_10-46-00PM.csv /tmp/google.tsv \
  --openai business-os/seo-marketplace/feed/2026-11-25-openai-feed-DRAFT-do-not-upload.tsv \
  --targets LV,EE,LT --store-country LV
```

The generator **stops** instead of guessing when a SKU is missing from the export, a stock
value is not a number, or one SKU has two different stock values. That is deliberate: a wrong
`availability` silently hides a product in Shopping.

## What changed on 2026-11-25 (SEO-03 / GEO-02)

- `availability` now reads the `Stock` column of the Squarespace export. `0` writes
  `out_of_stock`; `Unlimited` and any positive integer write `in_stock`.
- The export is the only stock source we have. It disagrees with the old handbook line
  "85 in-stock, 13 out" (all 98 feed SKUs show stock ≥ 1 in the 17 Oct export) — see QA F2.
  When the owner supplies a physical count, update the export, then re-run; do not patch the TSV.
- `VIMG` keeps the 19 Oct cardigan Brown image override (`SQ7601591`) so regeneration does not
  undo it. Per-variant photos still have to be bound in Squarespace for the other ~48 rows.
- Promotional and non-product copy removed from `description` (`Free shipping`, `Ships from Riga`,
  `14-day returns`): Google's product data spec forbids promotional text in descriptions and asks
  for product-only information. Shipping/returns belong in Merchant Center account settings. Both
  feeds were regenerated on 25 Nov; see `2026-11-25-google-feed-conformance-audit.md` G1.
- Output path is passed in, not hard-coded, and both writers emit LF.
- New `--openai` output: 25 OpenAI columns (the two non-schema Google category columns were replaced
  by the spec's `product_category` text-path field on 25 Nov), `variant_dict` as JSON,
  `accepts_returns=true`, `return_deadline_in_days=14`, `shipping_price=0.00 EUR`,
  `listing_has_variations` true only on multi-variant products (14 groups / 91 grouped rows /
  7 single-variant rows).

## Non-negotiables

- No invented GTINs or MPNs. `identifier_exists=no` stays.
- No invented fibre percentages, colour names or stock counts. Those are `[FILL]` until the owner answers.
- Wording stays "knitted on manual machines and finished by hand in Riga". No "handmade",
  "sustainable", "organic", "certified".
