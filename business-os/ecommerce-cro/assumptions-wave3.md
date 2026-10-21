# E-commerce & CRO assumptions register, wave 3 — DRAFT for owner

Agent `aw-ecommerce-cro`, 2026-10-21. ASSUMPTION MODE (owner-approved 2026-10-21). **Every value is an ASSUMPTION,
not a fact.** These rows only fill gaps that the shared registers leave open. Shared registers come first, in this
order: GM `business-os/head-of-ecommerce/assumptions-wave3.md` (its rulings win), then Production
`business-os/knitwear-making/assumptions-wave3.md`, then Operations `business-os/operations/assumptions-wave3.md`.
No row here permits a live edit, an upload or any spend. The owner applies everything herself.

Never assumed (these stay `[OWNER]` / CLAIM-CHECK): model height and size worn, fibre %, beanie height in cm,
S/M and L/XL to EU size mapping, physical stock counts, the return address, and any colour name that is not
already on the live page or in the feed.

| A-ID | Value | Basis | Range | Conf. | Task IDs | Owner confirms by |
|---|---|---|---|---|---|---|
| A-CRO-01 | **Raglan cardigan:** Black = in stock (2 listed, real under A-PRD-12). **Brown and Blue = made to order**, garment lead time 10 working days (A-PRD-14) | The live PDP says Brown/Blue are knitted "to order". The 17 Oct export lists 2 of each. Where the two sources disagree, the less risky promise wins | Brown/Blue may be in stock (2 each) | M | CRO-24, CRO-25, CRO-27 | 24 Oct (form item 9) |
| A-CRO-02 | **Lambswool crew colour name = "Grey"** | Feed `color` column (rows SQ8973335 etc.). The PDP names no colour | Light grey / Melange grey | L | CRO-24, CRO-27 | 31 Oct (form item 12) |
| A-CRO-03 | **Beanie: all 11 colours made to order, leave Riga within 5 working days.** **Hat & scarf set Black: in stock** (6 listed, so 1–8 counts as real units) | Derived from A-PRD-12 (220 listed = 0 on shelf, made to order) and A-PRD-14 (accessories 5 wd). The set is promoted in Black only (A-GM-02) | Beanie colours could have shelf units | L | CRO-24, CRO-25, CRO-27 | 24 Oct (form item 8) |
| A-CRO-04 | **Gift note collection:** an optional site-wide checkout form field, "Gift message (optional)". This is a native setting, not a script. **Fallback** if the plan does not offer the field: "Reply to your order confirmation with your gift message" | A-GM-22 says the gift note is offered. Checkout custom fields are described in third-party guides; plan availability is not confirmed on Squarespace help [VERIFY in Commerce → Checkout] | field available / not available | L | CRO-26 | 14 Nov (form item 16) |
| A-CRO-05 | **Cost of one gift note: EUR 0.70 per gift order** (blank card EUR 0.30 plus 2 minutes of handwriting at EUR 0.20/min, A-PRD-01) | No supplier quote. Packaging in A-OPS-10 already includes a printed care card | 0.40–1.50 | L | CRO-26, FIN-19 | 14 Nov |
| A-CRO-06 | **No CRO-owned date.** Christmas copy uses the Ops dates in A-OPS-16..19 exactly as written (recomputed for W3-1 on 21 Oct). **Which date applies to which product:** in-stock priority SKUs (cardigan Black, dusty pink, crew, hat & scarf set Black) use the in-stock column. Cardigan Brown/Blue use the made-to-order garment column. The beanie uses the made-to-order beanie/hat set column. Orders before 12:00 Riga time (A-OPS-13) | CRO cross-check of the arithmetic agrees with Ops on every date (pack s2). Product mapping comes from A-CRO-01/03 | as Ops | L | CRO-25 | 14 Nov (OPS-09), 20 Nov approval |
| A-CRO-07 | **Christmas made-to-order line is published by Mon 9 Nov** on the cardigan and beanie PDPs, ahead of the 20 Nov banner (A-GM-28). **This is a proposal, not a default.** If the owner says no, the EU made-to-order garment date (19 Nov) passes before any customer is told | The arithmetic in pack s2: 19 Nov comes before 20 Nov | 2–16 Nov | L | CRO-25 | 4 Nov |
| A-CRO-08 | **Feed availability for made-to-order rows:** made-to-order garments (10 wd, longer than the 5-day Merchant Center handling time) = `backorder` with `availability_date` = upload date + 14 calendar days, refreshed at each upload. Made-to-order accessories (5 wd fits the handling time) = `in_stock` | Google says backorder needs an availability_date (the ship date, max 1 year ahead, no ranges): https://support.google.com/merchants/answer/6324470 , https://support.google.com/merchants/answer/6324448 . Rule for long handling times not confirmed [VERIFY] | alt: raise the handling time in the MC shipping service | M | CRO-23, CRO-24 | 31 Oct |

Inputs used from the shared registers: A-GM-02, -03, -05, -10, -11, -16, -18, -19, -22, -24, -28; A-PRD-01, -12,
-13, -14, -22; A-OPS-07, -12..-19, -22.

DRAFT. Nothing sent or applied. When the owner answers `owner-inputs-wave2.md`, the answer replaces the matching row.
