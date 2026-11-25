# Google feed conformance audit — 2026-11-25

## Verdict
The file is structurally clean (98 data rows, exactly 19 columns each, LF endings, no BOM, no duplicate IDs) and all required attributes are present with correct value formats. It is **not ready to re-upload**: two content issues can trigger disapprovals (promotional text — "Free shipping" — in all 98 descriptions, and unverifiable fibre/origin claims in up to 93 rows), and the variant-image problem (F4) still needs owner-bound photos. One new structural issue is `additional_image_link`: we put all extra images comma-separated in one cell, while Google documents including the attribute multiple times. The generator-side availability bug (F1) is now closed.

Counts below come from a fresh read of `autumnandwool-google-feed.tsv` on 2026-11-25; commands are in `## Counting method`.

## Blocking issues

| ID | Issue | Affected rows | Spec source | Fix |
|---|---|---|---|---|
| G1 | Description contains promotional text "Free shipping" plus shipping/returns details. Google says: "Don't include promotional text like 'free shipping' …" and "Include only information about the product." | 98 | OFFICIAL Product data specification, Basic product data → Description [description] (`https://support.google.com/merchants/answer/7052112`) | Remove the `SHIP` constant appended in `build_google_feed.py` line 51 from `description`. Shipping/returns belong in Merchant Center shipping settings and `return_policy`, not the product description. Regenerate both feeds. Needs owner approval because it changes public feed copy. |
| G2 | Unverifiable claims in `description`/`title`: "100%" (93 desc, 4 title), "Knitted on a manually operated knitting machine and hand-sewn in Latvia." (79), "extra-fine" (15), "Italian-spun" (14), "pure new wool" (25), "pure wool" (1 desc, 16 title), "kraft gift packaging" (14). Our policy allows only "knitted on manual machines and finished by hand in Riga" and forbids fibre % until supplier specs land. | up to 93 | OFFICIAL spec requires accurate product data and "incorrect, inaccurate, or missing product information can cause disapprovals" (`https://support.google.com/merchants/answer/7052112`); our brand-voice gate (repo) | Hold for G8 claims evidence / decision 16. If unproven, replace with the allowed wording and drop fibre/origin claims. Same owner gate as October F3. |
| G3 | Wrong or missing variant photos. `image_link` is byte-identical across many rows of one product (e.g. 36 turtleneck rows, 11 beanie rows, 4+ per size range); October F4 estimated ~48 rows with `variant.imageIds=[]`. Google requires the image to "accurately display the product" and flags conflicting variant attributes. | ~48 (owner estimate, not re-counted today) | OFFICIAL spec, Basic product data → Image link (`https://support.google.com/merchants/answer/7052112`) | Bind real variant photos in Squarespace, then regenerate. `VIMG` override already fixes SQ7601591 only. Do not guess photos from the CDN. |

## Warnings

| ID | Issue | Affected rows | Spec source | Fix |
|---|---|---|---|---|
| W1 | `additional_image_link` holds several comma-separated URLs in one cell. Google says: "Submit up to 10 additional product images by including this attribute multiple times." Our single-cell form is not the documented text-feed form; it may be read as one invalid URL. | 90 (8 rows have no additional images) | OFFICIAL spec, Basic product data → Additional image link (`https://support.google.com/merchants/answer/7052112`) | Emit repeated `additional_image_link` columns (one column per extra image, up to 10) in the generator; keep one `image_link`. Verify with Merchant Center after upload. |
| W2 | Empty `color` on apparel rows. October F6 lists these SKUs; Google flags missing variant attributes as a common issue. | 12 | OFFICIAL spec intro, "missing or incorrect variant attributes (such as … color [color] or size [size])" (`https://support.google.com/merchants/answer/7052112`) | Owner supplies the colour name exactly as on the PDP; add to generator `D` data. Do not guess from photos. |
| W3 | Colour spelling inconsistent across rows: `Gray` (2), `Grey` (4), `Light grey` (1), `Light Grey` (4), `Melange grey` (1), `Melange Grey` (3). Free-text values should be consistent for the same colourway. | 15 | OFFICIAL spec, "use the same language for all attributes in a data source" and accurate variant attributes (`https://support.google.com/merchants/answer/7052112`) | Normalise to one spelling per colourway after owner confirmation (Grey vs Gray is a market choice). |
| W4 | No `shipping` column in the feed. Google's spec includes Shipping and returns; account-level shipping settings in Merchant Center are an accepted alternative but we have no in-repo evidence they are configured. | 98 | OFFICIAL spec, "Shipping and returns" section and "Shipping rate data requirements" (`https://support.google.com/merchants/answer/7052112`) | Owner confirms Merchant Center account-level shipping is active for Latvia/EU. If not, add `shipping` to the feed. Not verifiable from repo files. |
| W5 | Title-vs-H1 mismatch on the vest PDP (October F8, SQ2078364). Feed title matches the PDP H1, but the PDP SEO `<title>` differs. | 1 | OFFICIAL spec, title must "match the title from your landing page" (`https://support.google.com/merchants/answer/7052112`) | Fix the PDP SEO title (on-page proposal exists). No feed change needed. |
| W6 | `size=One size` on garments with no size selector. Accepted in October F7; still present. | 24 | OFFICIAL spec, size is a free-text label; not disallowed | Reconsider only if CRO adds size variants; feed must follow in the same pass. |

## Claim-wording inventory

Counts are case-insensitive substring counts in the `description` column (and `title` where shown), from the committed TSV on 2026-11-25.

| Phrase | Column | Rows | Allowed by our policy? |
|---|---|---|---|
| `100%` | description | 93 | No — fibre % needs supplier spec sheet (decision 34) |
| `100%` | title | 4 | No — same reason |
| `Knitted on a manually operated knitting machine and hand-sewn in Latvia.` | description | 79 | Partly — "knitted on manual machines and finished by hand in Riga" is allowed; "hand-sewn" and "in Latvia" are not the approved wording |
| `extra-fine` | description | 15 | No — needs yarn spec |
| `Italian-spun` | description | 14 | No — needs yarn spec |
| `pure new wool` | description | 25 | No — "pure wool" claims need evidence (gate G8) |
| `pure wool` (exact substring, not "pure new wool") | description | 1 | No — same |
| `pure wool` | title | 16 | No — same |
| `kraft gift packaging` | description | 14 | No — packaging claim needs evidence |
| `Free shipping` | description | 98 | No — promotional text, explicitly forbidden by Google for descriptions |
| `Ships from Riga` | description | 98 | Content, not promotional; verify factual |
| `14-day returns` | description | 98 | Content, not promotional; verify factual |
| `handmade`, `sustainable`, `organic`, `certified`, `hand-knitted`, `hand-sewn` as literal words in `description` | description | 0 (all 98 use the longer "manually operated … hand-sewn" sentence, counted above) | The standalone banned words do not appear; the long sentence still needs the approved wording |

## October QA F1–F6 status

| # | Finding | Status on 2026-11-25 | Evidence |
|---|---|---|---|
| F1 | Availability hard-coded `in_stock` | **Closed code-side.** `build_google_feed.py` now reads `Stock` from the export, fails closed on missing/conflicting/non-numeric values, and writes `in_stock`/`out_of_stock`. Current TSV still has 98/98 `in_stock` because the 17 Oct export shows stock ≥ 1 for those SKUs. | `build_google_feed.py` lines 26–40; commit `800caec` |
| F2 | "13 out of stock" not reproducible | **Still needs owner.** Export remains truth; handbook §5 item 4 still contains the disputed line. | F2 text; repo export |
| F3 | Claims evidence | **Open**, escalated as G2 above. | Claim counts in this audit |
| F4 | Wrong variant photos | **Open.** One SKU (SQ7601591) fixed by `VIMG`; the rest need owner photo binding. | G3 above; generator `VIMG` |
| F5 | Brown cardigan possibly serving Black photo | **Partially closed.** Generator override points SQ7601591 at the asset the 19 Oct hand-edit used; owner eyes still required to confirm the photo is brown. | `VIMG` in generator |
| F6 | 12 empty colours | **Open.** | W2 above |

## New findings not in the October QA

- **G1 (blocking):** "Free shipping" and shipping/returns copy in all 98 descriptions — promotional text explicitly forbidden by Google's description rules. This is the highest-priority new fix and needs only a generator constant change plus owner copy approval.
- **W1:** all extra images in one comma-separated `additional_image_link` cell instead of repeated columns.
- **W3:** Grey/Gray spelling split across 15 rows.
- **W4:** no in-repo evidence that account-level shipping is configured (not a feed defect, but an unverified prerequisite).
- Note: October QA reported the feed as structurally PASS; this audit agrees on structure and differs only on the content/formatting findings above.

## Counting method

Read-only commands run from the repo root on 2026-11-25, Python 3 `csv` module, delimiter `\t`:

```
python3 - <<'PY'
import csv, collections, re
raw = open('autumnandwool-google-feed.tsv','rb').read()
# BOM: raw[:3] == b'\xef\xbb\xbf' -> False; CRLF count -> 0; LF count -> 99
rows = list(csv.reader(open('autumnandwool-google-feed.tsv',newline='',encoding='utf-8'),delimiter='\t'))
hdr, data = rows[0], rows[1:]
# len(hdr)=19; len(data)=98; Counter(len(r) for r in data) -> {19: 98}
# duplicate ids: Counter(r[0] for r in data) entries with value>1 -> none
# empty counts per column, then Counter per column for availability, gender, color, size, material, category, price
# title lengths: max 65, count>150 = 0; description max 312, count>5000 = 0
# price pattern: r'\d+\.\d{2} EUR' -> 98/98
# claims: case-insensitive substring over description/title
# images: urlparse -> scheme https, host endswith squarespace-cdn.com, suffix '?format=1500w'
# group ids: 91 rows with, 7 without; 14 distinct, none reused across different id sets
PY
```

All numbers in this document are from those reads. The ~48 wrong-variant-photo estimate is inherited from October F4 and is explicitly labelled as an owner estimate, not re-counted today.

## Sources
- OFFICIAL — Google Merchant Center, Product data specification: `https://support.google.com/merchants/answer/7052112` — read 2026-11-25. Covers required/optional attributes, title and description rules (no promotional "free shipping", ≤150/≤5000 chars), image link and repeated additional image link, price/availability values, identifier_exists/GTIN, product category ID or full path, and the intro warning about inaccurate data and missing variant attributes.
- REPO — `business-os/seo-marketplace/feed/2026-10-21-feed-qa.md` — read 2026-11-25 for F1–F6 status and the 21 Oct taxonomy check (`212` = Apparel & Accessories > Clothing > Shirts & Tops; `173` = Clothing Accessories > Hats). The taxonomy IDs were checked on 21 Oct, not re-fetched today.
- REPO — `build_google_feed.py`, `products_Oct-17_10-46-00PM.csv`, `autumnandwool-google-feed.tsv` — read 2026-11-25.
