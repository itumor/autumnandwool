# Creator gifting brief + gift spec: DRAFT (PAR-07, PAR-10)

Status: DRAFT for owner approval. The brief goes in the parcel (printed card) or by email after a creator agrees.
Per-creator fields in `[brackets]`. Facts from `llms.txt`, `aw-brand-voice` and `business-os/README.md`. Unverified
claims are marked.

## Part A: brief to the creator (EN; LV version after native check)

```
Hi [first name],

Thank you for trying Autumn & Wool. Here's everything in one place.

Why we exist: knitwear from a small studio in Riga, made for comfort and everyday wear,
season after season. Before this site, I sold as Mareshop on Etsy (4.9 stars, 1,400+ reviews on Etsy).

What's in your parcel: [product], [colour], size [size], merino wool [CLAIM-CHECK].

If you'd like to talk about it, a few true things (use your own words, or none):
- Fit: [VERIFY: fit line from the product page, e.g. relaxed / true to size]. Measurements: [PDP link]
- Feel: how it feels to you. Your honest opinion is what matters to us.
- Care: hand wash cold with a wool-safe detergent, don't tumble dry, lay flat to dry.

Link for your followers: [UTM link from attribution-scheme.md]
[ONLY IF decision 11 + D5: Your personal code: [CODE], [X]% off, valid until [date].]

Disclosure, please: this is a gift, so any post about it is an ad under EU and Latvian rules.
Please label it clearly at the start: use the platform's "Paid partnership" label and #reklama
(or "Advertisement / gifted by @autumnandwool" in the caption's first line). "Thanks @autumnandwool"
or #collab on its own is not enough.

Please don't say: that it's sustainable, eco, organic, hypoallergenic, itch-free or machine-washable,
"extra-fine" or a fibre percentage (e.g. "100% merino"), or that it's "made in Latvia" or "hand-knitted"
[until G8 changes this]. Please don't mention a gift card or gift packaging (we don't offer either).
No discounts other than your own code, and no "last one" urgency.

Everything else is up to you: no scripts, no approval needed, and no obligation to post.
If you'd like us to share your photos on our own pages, we'll ask separately, in writing.

Thank you, Kristine
Autumn & Wool, autumnandwool.com, Instagram @autumnandwool
```

## Part B: gift spec (one per agreed creator; the owner ships)

| Field | Value | Source / rule |
|---|---|---|
| Creator handle | [handle] | tracker |
| SKU (product title) | [title] | Must be GREEN/AMBER in latest owner-approved `capacity-YYYY-Www.md`. **MISSING: no capacity file yet** |
| Colour / size | [colour] / [size] | Creator's choice, checked against real stock (decision 4) |
| Materials + labour EUR | ASSUMED beanie 13.33 / hat set 55.51 (A-PRD-20/21) | `sku-economics.csv` `materials_labour_eur` replaces it when filled |
| Packaging EUR | ASSUMED 1.50 (A-OPS-10) | `packaging_eur` when quoted |
| Shipping EUR (to creator's country) | ASSUMED LV 5.00 / EE-LT 6.00 (A-OPS-02/03), +7% Nov-Dec (A-OPS-09). No EU-other gifts in Q4 (A-PAR-04) | OPS carrier rates |
| **Gift cost EUR** | ASSUMED beanie **LV 19.83 / EE-LT 20.83**; hat set Black LV 62.01 (A-PAR-01). Max EUR 22 per gift (A-PAR-05) | Logged as creator CAC in `gift_cost_eur` |
| Break-even CAC for this SKU EUR | ASSUMED beanie 13.09 LV / hat set 18.82 LV; programme payback on blended 18.92 (A-PAR-06) | `unit_economics.py` `contrib` column, after G1 |
| Code / UTM | Q4: **no code** (A-GM-06, A-PAR-10) / UTM per `attribution-scheme.md` (beanie PDP) | `attribution-scheme.md` |
| Ship by | ASSUMED make W47, ship by Fri 27 Nov, after G4 (A-PAR-09); never after 30 Nov 2026 | Plan s2; EU cutoff about 3 Dec (ruling C3) |
| Parcel contents | Garment, printed brief (Part A), care card. Optional handwritten note. **No gift card, no gift wrap / "gift packaging"** (W3-6/W3-7, A-GM-22) | OPS packaging standard |
| Owner approval | [ ] gift approved [ ] value approved [ ] shipped (date, tracking in owner's records) | Decision rights |

### Candidate gift SKUs (proposal only, pending G1/G2 and decision 4)

| SKU | Price incl. VAT | Ex VAT | Stock in sheet | Note |
|---|---|---|---|---|
| Rib-Knit Merino Beanie, unisex | EUR 45.00 | EUR 37.19 | 220 (looks like a made-to-order placeholder) | Lowest price point, probably the lowest gift cost. Unisex. Variant photos missing |
| Merino Wool Hat & Scarf Set | EUR 110.00 | EUR 90.91 | 6 | Gift-season fit. Small stock: gifting uses real units |
| Merino Turtleneck, lightweight | EUR 110.00 | EUR 90.91 | 360 (looks like a placeholder) | Best styling content, but sizing risk. Variant photos missing |

Prices and stock from `business-os/sku-economics.csv`; ex VAT = price / 1.21. Gift cost per SKU is unknown until
costs are filled. Proposed choice: beanie first, **only if** its cost is confirmed and it is GREEN/AMBER.

Wave-2 update (2026-10-21): the GM decision pack (#12) says gift only from the priority 5, G8-cleared
(`head-of-ecommerce/priority-5-sku-proposal-2026-10-21.md`). So the candidates are the beanie and the hat & scarf
set (Black only until Brown/Gray have real photos). The turtleneck is an alternate, not a gift candidate unless the GM
swaps it in on 4 Nov. Costing: `gift-budget-worksheet.md`.

Wave-3 update (2026-10-21, ASSUMPTION): gift = **Rib-Knit Beanie, the one photographed colour [VERIFY which], one size
[VERIFY on PDP]**, GREEN (A) in `knitwear-making/capacity-2026-W43.md`. Hat & scarf set Black only as an owner-approved
per-creator swap (A-PAR-03). Register: `business-os/partnerships/assumptions-wave3.md`.

GM rulings applied 2026-10-21: W3-8 (fibre = "merino wool [CLAIM-CHECK]", no "extra-fine", no %; product titles in
the table above are store titles for reference, not brief copy), W3-6/W3-7 (no gift card, no "gift packaging"), W3-5
(EUR 110 programme, max EUR 22 per gift, LV/EE/LT, owner approves each gift, nothing ships before G4).
