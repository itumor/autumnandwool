DRAFT — for owner approval. Nothing here is sent.

# Size-advice method and macros (CX-07), size data staging (CX-08)

Written 2026-10-21 by the aw-customer-experience agent. Size questions are P2: draft the same day (a slow answer
can cost the sale).

## Facts used (and source)

| Fact | Source | Status |
|---|---|---|
| Body size chart below | Live `/size-guide`, read 2026-10-21 (web fetch; the page also lists inches, which the fetch did not return) | Owner confirms: decision 8 in the CX plan |
| Garment measurements are taken flat: width (armpit to armpit), length (shoulder to hem), sleeve (armpit to cuff), listed on each product page | Live `/size-guide` | Read the PDP of the piece every time |
| Flat width x 2 = garment chest. Garment chest minus body chest = ease. Example on the page: Side-Slit Sweater S, 50 cm flat, about 100 cm around | Live `/size-guide` | OK |
| Fit types: close (e.g. lightweight merino turtleneck), relaxed (side-slit, stand-collar, lambswool crew), oversized (most one size), one size (vests, some cardigans) | Live `/size-guide` | OK |
| No custom sizing | Live `/faq` | OK |
| Some garments have no size selector, and the PDP measurement format varies (cm vs cm + in) | `zero-sales-diagnosis-2026-10-18.md` A4 | CRO fix; check the PDP before advising |
| Ease guide: close about 0-5 cm over chest, relaxed 8-15 cm, oversized 15+ cm | `aw-support-replies` s3 | **Guidance, not a fact.** Say "as a guide" |

### Body chart (cm), staged from the live page, not owner-confirmed

| Size | EU / UK / US | Chest | Waist | Hips |
|---|---|---|---|---|
| S | 36 / 8 / 6 | 84-90 | 62-70 | 90-96 |
| M | 38 / 10 / 8 | 90-96 | 70-78 | 96-104 |
| L | 40 / 12 / 10 | 96-104 | 78-88 | 104-112 |
| XL | 42 / 14 / 12 | 104-110 | 88-100 | 112-118 |

### Garment measurements per SKU (CX-08, BLOCKED: owner confirms or pastes from the PDPs)

| Product (visible) | Sizes | Flat width cm | Length cm | Sleeve cm | Fit type | Source |
|---|---|---|---|---|---|---|
| [VERIFY: one row per visible garment, copied from the live PDP; owner confirms] | | | | | | |

Until this table is filled, every size reply reads that product's live page on the day and quotes it exactly.

## Method (one recommendation, one reason, one alternative)

1. Collect: chest (bust) measurement in cm, preferred fit (close / relaxed / oversized), height (sleeve and
   length), usual size, and if possible a knit they like, measured flat (width and length).
2. Garment chest = flat width x 2. Ease = garment chest minus body chest.
3. Compare with the ease guide for the fit they want. Pick one size. If two sizes are both within range, give
   the one that matches their preferred fit and name the other as the alternative.
4. Check length and sleeve against height, if the PDP gives them.
5. Close with the return or exchange line, only in approved wording (see `support-macros.md` facts table).
6. Never guess a measurement that is not on the page. If it is missing, write
   `[VERIFY: ask Kristine to measure size X flat]`.

Worked example (from the live page's own example, for the method only): chest 86 cm and wants relaxed. Side-Slit
Sweater S is 50 cm flat, so 100 cm around and 14 cm of ease. As a guide that is relaxed, so recommend S.

## Macros

### SIZE_HELP_ASK (they have not given measurements)
```
Hello [first name],

Happy to help you choose. Could you send me:
1. your chest measurement in cm (around the fullest part, tape level under the arms),
2. how you like it to fit: close, relaxed or roomy,
3. your height and the size you usually buy.
If you have a sweater you love, lay it flat and measure across from armpit to armpit; that helps
most of all.
I will reply the same day with one clear recommendation.

Kristine, Autumn & Wool
```

### SIZE_HELP_RECOMMEND (measurements given)
```
Hello [first name],

For [product] I would choose size [X]. It measures [flat width] cm across, so about [x2] cm around:
that is [ease] cm more than your chest, which (as a guide) gives the [close/relaxed/roomy] fit you
described. The length is [length] cm from shoulder to hem [and the sleeve [sleeve] cm from armpit].
[If between sizes: size [Y] would feel [closer/roomier]; choose it if you like to layer / prefer
it neater.]
If it does not fit as hoped, you can [approved returns/exchange line: VERIFY current wording].

Kristine, Autumn & Wool
```

### SIZE_HELP_ONE_SIZE (vests, some cardigans, oversized)
```
Hello [first name],

[Product] comes in one size. It measures [flat width] cm across ([x2] cm around), so with your
[chest] cm chest it gives about [ease] cm of room, a [relaxed/oversized] fit. [Length note.]
If you prefer something closer to the body, [alternative product with sizes: VERIFY on the GREEN
list] may suit you better.

Kristine, Autumn & Wool
```

### SIZE_HELP_GIFT (size unknown)
```
Hello [first name],

Choosing for someone else is tricky, so here is the safest way: if you can, borrow a sweater of
theirs that fits well and measure it flat, armpit to armpit. If not, their usual size is enough
for a guess, and a one-size piece such as [beanie / hat and scarf set: VERIFY on the GREEN list] is
the no-risk choice. [Exchange after Christmas: OWNER DECISION 31.]

Kristine, Autumn & Wool
```

### DM version (Instagram, 1-3 sentences)
"Happy to help with size. Send me your chest measurement in cm and how you like it to fit (close, relaxed or
roomy), and I will recommend one. Measurements for each piece are on its product page. — Kristine"

## Feedback loop
Every size case and every return with a SIZE_SMALL or SIZE_LARGE reason is counted in the weekly CX summary.
Two or more on one SKU in a month means a PDP or size-guide proposal goes to CRO. Product data stays frozen;
these are proposals only.
