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

What's in your parcel: [product], [colour], size [size], [VERIFY: fibre exactly as on the product page].

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
or that it's "made in Latvia" or "hand-knitted" [until G8 changes this]. No discounts other than your
own code, and no "last one" urgency.

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
| Materials + labour EUR | TODO | `sku-economics.csv` `materials_labour_eur`, all empty today |
| Packaging EUR | TODO | `packaging_eur`, empty |
| Shipping EUR (to creator's country) | TODO | OPS carrier rates (due 28 Oct) |
| **Gift cost EUR** | = materials+labour + packaging + shipping = TODO | Logged as creator CAC in `gift_cost_eur` |
| Break-even CAC for this SKU EUR | TODO | `unit_economics.py` `contrib` column, after G1 |
| Code / UTM | [CODE] / [URL] | `attribution-scheme.md` |
| Ship by | [date], not after 30 Nov 2026 | Plan s2; EU cutoff about 3 Dec (ruling C3) |
| Parcel contents | Garment, printed brief (Part A), care card | OPS packaging standard |
| Owner approval | [ ] gift approved [ ] value approved [ ] shipped (date, tracking in owner's records) | Decision rights |

### Candidate gift SKUs (proposal only, pending G1/G2 and decision 4)

| SKU | Price incl. VAT | Ex VAT | Stock in sheet | Note |
|---|---|---|---|---|
| Rib-Knit Merino Beanie, unisex | EUR 45.00 | EUR 37.19 | 220 (looks like a made-to-order placeholder) | Lowest price point, probably the lowest gift cost. Unisex. Variant photos missing |
| Merino Wool Hat & Scarf Set | EUR 110.00 | EUR 90.91 | 6 | Gift-season fit. Small stock: gifting uses real units |
| Merino Turtleneck, lightweight | EUR 110.00 | EUR 90.91 | 360 (looks like a placeholder) | Best styling content, but sizing risk. Variant photos missing |

Prices and stock from `business-os/sku-economics.csv`; ex VAT = price / 1.21. Gift cost per SKU is unknown until
costs are filled. Proposed choice: beanie first, **only if** its cost is confirmed and it is GREEN/AMBER.
