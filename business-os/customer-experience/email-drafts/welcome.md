DRAFT — for owner approval. Not uploaded, not scheduled, not sent. The original
`campaign-assets/welcome-email-draft.md` is left unchanged; W1 below is the proposed replacement (CX-12).

# A1 Welcome flow: 4 emails (CX-12, CX-13, CX-14)

Segment: group "Newsletter". Exit: buys (owner removes), unsubscribes. All links carry
`?utm_source=mailerlite&utm_medium=email&utm_campaign=welcome-2026-11&utm_content=w<n>-<link-position>`, aligned
on 21 Oct (wave 2) with Growth's `business-os/growth/utm-taxonomy.md` s3 (email row: campaign
`<flow>-<yyyy-mm>`, position in `utm_content`) and the two `email-welcome-*` rows in `utm-links.csv`. CX adds the
`w<n>-` prefix so each step can be read separately; the new content values are proposed to Growth for
`utm-links.csv` (Growth owns that file). If activation slips past November, the owner changes `2026-11` to the
activation month in every link. Footer on every email: AUTUMN AND WOOL, SIA, [VERIFY: postal address from the site footer],
unsubscribe link, "You are receiving this because you signed up at autumnandwool.com [or: at <market>]".

---

## W1: Welcome (sends immediately)

Changes from the current draft: one reply promise (1-2 business days, ruling C2; the owner confirms by 7 Nov),
UTM on the links, signed by Kristine, one main CTA, a line on what to expect.

Subject (<=45): Welcome to Autumn & Wool
Preheader (<=90): A note from Kristine in Riga, and how to find your size.

Body:
> Hello [first name | fallback: "Hello"],
>
> Thank you for joining Autumn & Wool. I am Kristine, and I make our knitwear in a small studio in Riga, Latvia:
> cardigans, sweaters, vests and accessories for the cooler months.
>
> Over the next ten days I will send three short letters: how the pieces are made, how to choose your size, and a
> few pieces I would start with. After that, about two letters a month.
>
> If you are unsure about size, the size guide shows how to compare your measurements with each garment:
> [Size guide](https://www.autumnandwool.com/size-guide?utm_source=mailerlite&utm_medium=email&utm_campaign=welcome-2026-11&utm_content=w1-size-guide-link)
>
> And if you have any question at all, just reply to this email. I usually reply within 1-2 business days.
>
> Kristine, Autumn & Wool

CTA button: "See the collection" -> https://www.autumnandwool.com/shop?utm_source=mailerlite&utm_medium=email&utm_campaign=welcome-2026-11&utm_content=w1-shop-link
Facts used: Riga studio, Kristine (brand voice s3; README s2); reply time (live FAQ, ruling C2); `/shop` and
`/size-guide` URLs (existing draft).
[OWNER DECISION]: reply promise (decision 26). [VERIFY]: does the first-name merge field exist on the signup form?
Compliance: consent from the signup form; unsubscribe; sender identity (checklist items 3-5).

---

## W2: How it is made (day 3)

Subject: How a piece leaves the Riga studio
Preheader: Knitted on manual machines, finished by hand, one piece at a time.

Body (story, about 180 words; the owner replaces the brackets with her own words, decision 20):
> Hello [first name],
>
> I promised to tell you how our pieces are made, so here it is, step by step.
>
> Each design starts in my studio in Riga. [VERIFY, Kristine's own words: one sentence on how a design begins,
> e.g. a sketch or a swatch.] The panels are knitted on manual knitting machines. [VERIFY, optional: one line in
> Kristine's words on what working the machine is like.] Then comes the slow part: the pieces are sewn together and finished by hand, washed and
> pressed before they are folded and packed.
>
> Before Autumn & Wool, I sold my knitwear on Etsy as Mareshop for 15 years. It is rated 4.9 stars from 1,400+
> reviews there. This shop is the same work under its own name.
>
> [VERIFY, optional: one concrete studio detail in the owner's words, e.g. a favourite yarn or the view from the
> window. Leave it out if not supplied.]
>
> If you would like to see it, I share the making on Instagram:
> [@autumnandwool](https://www.instagram.com/autumnandwool/)
>
> Kristine

CTA button: "Read our story" -> https://www.autumnandwool.com/about?utm_source=mailerlite&utm_medium=email&utm_campaign=welcome-2026-11&utm_content=w2-story-button [VERIFY: the About page URL slug]
Facts used: manual machines + hand finishing (brand voice s2-3); "sewn, finished, washed and pressed" (live FAQ);
Etsy line (ruling C1); handle (brand voice s5).
Not used on purpose: "handmade", "hand-knitted", "sustainable".
[OWNER DECISION]: Kristine's own words (decision 20); Etsy figure (decision 17). Image: real studio photo (CRE). [VERIFY]

---

## W3: Fit, size and care (day 6)

Subject: Finding your size, and making it last
Preheader: Two measurements, one comparison, and how to wash wool.

Body (about 170 words):
> Hello [first name],
>
> Most questions I get are about size, so here is the quickest way to choose.
>
> 1. Measure your chest around the fullest part, with the tape level under your arms.
> 2. On the product page, find the garment's flat width and double it. That is the garment's chest.
> 3. The difference is the room you will have. As a guide: up to about 5 cm sits close, 8-15 cm feels relaxed,
>    more is roomy.
>
> Easier still: lay a sweater you love flat, measure it armpit to armpit, and compare it with the product page.
> Or send me your measurements and the piece you like, and I will suggest a size.
>
> Caring for wool is simple: hand wash cold with a wool-safe detergent, dry flat, never tumble dry, and store it
> folded. Each product page has the care for that piece.
>
> Kristine

CTA button: "Open the size guide" -> https://www.autumnandwool.com/size-guide?utm_source=mailerlite&utm_medium=email&utm_campaign=welcome-2026-11&utm_content=w3-size-guide-button
Facts used: measuring method and flat x 2 (live `/size-guide`); ease bands are labelled as a guide (CX skill s3);
care (live `/faq`).
[VERIFY]: the owner agrees to publish the ease bands (they also appear in `faq-proposals.md`).

---

## W4: Three pieces to start with (day 10)

### Wave 3: DRAFT-ASSUMPTION version (use this one)

ASSUMPTION: products = Production GREEN (A) list W43 (A-CX-05: Lambswool Crew, Dusty Pink raglan, Hat & Scarf Set
Black; alternate Beanie, photographed colour), prices A-GM-02 (17 Oct export), dispatch A-GM-03, claims A-GM-10;
register: `business-os/customer-experience/assumptions-wave3.md`. GREEN (A) means GREEN on assumed stock and costs,
organic use only (no paid spend). Re-check the GREEN list, prices and each live PDP the week the flow goes live.

Subject (<=45): Three pieces I would start with
Preheader (<=90): A grey crew, a dusty pink raglan, and a hat and scarf set for the cold months.

Body (about 150 words):
> Hello [first name],
>
> If you are new here and wondering where to begin, these are the three pieces I would choose.
>
> **Classic Lambswool Crew, grey.** A crew neck with raglan sleeves, ribbed cuffs and a gently curved hem. A relaxed
> fit, in sizes S to XL. [CLAIM-CHECK: fibre name exactly as on the live PDP] EUR 136.
> [See the crew](https://www.autumnandwool.com/shop/p/p/hand-knitted-lambswool-sweater-womens-grey-knit-jumper?utm_source=mailerlite&utm_medium=email&utm_campaign=welcome-2026-11&utm_content=w4-lambswool-crew)
>
> **Merino Raglan Sweater, Dusty Pink.** An oversized raglan in a soft, muted pink, in two sizes: S/M and L/XL.
> [CLAIM-CHECK: fibre name exactly as on the live PDP] EUR 155.
> [See the sweater](https://www.autumnandwool.com/shop/p/p/hand-knitted-merino-wool-raglan-sweater-dusty-pink-oversized-jumper?utm_source=mailerlite&utm_medium=email&utm_campaign=welcome-2026-11&utm_content=w4-dusty-pink-raglan)
>
> **Hat & Scarf Set, black.** A matching rib-knit beanie and scarf. One size: the beanie fits 54-58 cm heads, the
> scarf is about 190 x 36 cm. [CLAIM-CHECK: fibre name exactly as on the live PDP] EUR 110.
> [See the set](https://www.autumnandwool.com/shop/p/p/merino-wool-hat-scarf-set-extra-fine-rib-knit-soft-on-skin-warm-not-bulky-unisex-gift?utm_source=mailerlite&utm_medium=email&utm_campaign=welcome-2026-11&utm_content=w4-hat-scarf-set)
>
> Each piece is knitted on manual machines and finished by hand in Riga. Pieces in stock are dispatched within
> 2-5 working days, and shipping is free to eligible destinations shown at checkout.
>
> Kristine

CTA button: "See all knitwear" -> https://www.autumnandwool.com/shop?utm_source=mailerlite&utm_medium=email&utm_campaign=welcome-2026-11&utm_content=w4-shop-button

Facts used + source:
| Fact | Source | Status |
|---|---|---|
| The 3 SKUs and max units (6 / 8 / 6) | `knitwear-making/capacity-2026-W43.md` GREEN (A) | ASSUMPTION (A-PRD-12 stock, A-CX-05) |
| Prices 136 / 155 / 110 | A-GM-02 (17 Oct export) | re-check live PDP |
| Crew: raglan sleeves, ribbed cuffs, curved hem, relaxed, S-XL, grey | `seo-marketplace/2026-10-21-pin-batch-w45-draft.md` W5 + `onpage-proposals.md` (read from the PDP); `size-advice.md` fit type | re-check live PDP |
| Dusty Pink: oversized, S/M + L/XL | `size-advice.md` (live, CRO) | re-check live PDP |
| Set: beanie 54-58 cm, scarf about 190 x 36 cm, Black | CRO size-fit standard s2; GREEN Black only | re-check live PDP |
| Process line, dispatch line, free shipping wording | A-GM-10, A-GM-03, aw-brand-voice s3 | ASSUMPTION |
| URLs | existing live slugs (`partnerships/attribution-scheme.md`, `seo-marketplace/2026-10-21-etsy-batch-prep.md`) | product data frozen: slugs not changed |

[CHECK] / [OWNER DECISION] items:
- Fibre wording per piece: copy from the live PDP; no percentages (A-GM-10). Never "RWS", "mulesing-free",
  "extra-fine", "spun in Italy" even though the set's slug contains "extra-fine".
- The Dusty Pink name is written without "Hand-Knitted" (claim gate). Its URL slug and the lambswool crew's slug
  both contain "hand-knitted": visible on hover. Slug change = SEO/CRO proposal for the owner (CX-W3-e).
- No "gift packaging" line (A-GM-22: gift wrap no; CX-W3-d).
- Swap rule: if any of the three drops to AMBER or RED, use the Rib-Knit Beanie in its photographed colour
  (EUR 45, one size, head 54-58 cm; colour name [VERIFY PRD]), and only after the add-to-cart colour bug is fixed.
- No discount code. Images: real photos per colour only (CRE).
Compliance: newsletter sign-ups only (A-GM-14); unsubscribe; sender "Kristine at Autumn & Wool"; footer
`[POSTAL_ADDRESS]` (owner fact).

### Wave 1-2 skeleton (superseded by the wave 3 version above, kept for history)

Subject: Three pieces I would start with
Preheader: [VERIFY after the GREEN list: e.g. "A cardigan, a vest and a beanie for the cold months."]

Body (about 150 words; only SKUs on that week's GREEN list, re-checked the day the flow goes live):
> Hello [first name],
>
> If you are new here and wondering where to begin, these are the three pieces I would choose.
>
> **[GREEN product 1 name]**: [one specific fact from the live PDP: fibre exactly as written, fit type, one
> detail]. EUR [price from the live page]. [Link + UTM utm_content=<slug>]
>
> **[GREEN product 2]**: [same pattern]
>
> **[GREEN product 3]**: [same pattern; ideally a one-size accessory for gift buyers]
>
> In-stock pieces leave Riga in 2-5 working days, and shipping is free to [Latvia, the US and the destinations
> shown at checkout].
>
> Kristine

CTA button: "See all knitwear" -> https://www.autumnandwool.com/shop?utm_source=mailerlite&utm_medium=email&utm_campaign=welcome-2026-11&utm_content=w4-shop-button
Product links: `utm_content=w4-<sku-slug>` (e.g. `w4-hat-scarf-set`).
Facts used: dispatch and free shipping (live `/faq`).
BLOCKED: no SKU is GREEN yet (PRD: every SKU is AMBER, "cost unknown", until G1/G2, the first real GREEN after
4 Nov). Real photo per colour needed (CRE). No discount code.

Wave 2 (21 Oct): provisional candidates, NOT approved for use. Taken from GM's
`business-os/head-of-ecommerce/priority-5-sku-proposal-2026-10-21.md` (owner decides 24 Oct, re-confirms 4 Nov).
Each one goes into W4 only if it is on the GREEN list the week the flow goes live.

| Slot | Candidate | Why it fits W4 | Must be true before use |
|---|---|---|---|
| 1 | Merino Wool Raglan Cardigan | GM hero piece; full cm measurements on the PDP | GREEN; promote only colours with a real photo (Blue has none); fibre wording copied from the live PDP; one size or several [VERIFY owner] |
| 2 | Women's Classic Lambswool Crew Sweater | everyday core sweater, 4 sizes | GREEN; garment measurements on the PDP (CRO size-fit standard s2 shows none); fibre wording from the live PDP |
| 3 | Merino Wool Hat & Scarf Set (Black) | one-size gift option (head 54-58 cm, scarf 190 x 36 cm per CRO s2) | GREEN; Black only until Brown/Gray photos exist; no "RWS / mulesing-free" wording (brand voice s3) |
| alt | Rib-Knit Beanie | gift entry price | GREEN; colour photos; stock confirmed (decision 4); add-to-cart colour bug fixed |

Not proposed for W4: the Dusty Pink raglan, because its title says "Hand-Knitted" (claim gate, decision 16) and
it has only 6 units.

Wave 3 change: Production's W43 capacity file puts the Raglan Cardigan at AMBER (thin CM2, Blue unphotographed) and
the Dusty Pink raglan at GREEN (A), max 6, with the instruction not to repeat "Hand-Knitted". So the cardigan left W4
and the Dusty Pink raglan came in, named without the title claim.
