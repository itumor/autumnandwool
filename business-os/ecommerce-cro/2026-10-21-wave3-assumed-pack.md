# CRO wave 3 assumed pack — 2026-10-21 — DRAFT-ASSUMPTION, for owner approval

Owner of this file: `aw-ecommerce-cro`. Mode: ASSUMPTION MODE (owner-approved 2026-10-21).
**Every date, lead time, stock status and option below is an ASSUMPTION, not a fact.** Each one cites its A-ID.
Registers: GM `business-os/head-of-ecommerce/assumptions-wave3.md` (its rulings win), Production
`business-os/knitwear-making/assumptions-wave3.md`, Ops `business-os/operations/assumptions-wave3.md`, CRO
`business-os/ecommerce-cro/assumptions-wave3.md`.
Nothing here has been applied. Product data stays frozen (A-GM-19, proposals only). The owner pastes from
`2026-10-21-wave3-pdp-final-copy.csv` once she approves. The feed decisions are in
`2026-10-21-wave3-feed-decisions.csv`. The live TSV, the generator and every shared CSV were left untouched.

Tasks covered: CRO-24 (feed trim/fix decisions), CRO-25 (Christmas banner), CRO-26 (gift options), plus the
apply-ready pack for CRO-27. Applying the pack is a live action, so CRO-27 stays BLOCKED.

## 0. GM rulings W3-5..W3-14 applied (follow-up pass 2026-10-21) — DRAFT-ASSUMPTION

| Ruling | What changed in this pack / the paste CSV | Owner confirms by |
|---|---|---|
| W3-6 | After-cutoff bar (s2.1) no longer offers a gift card. It uses the CX A-CX-03 line instead | 20 Nov |
| W3-7 | "ships in kraft packaging, so it can go straight under the tree" removed from the hat & scarf set (s1.4). G3 no longer offers any packaging line (s3). Only two gift lines are allowed: "add a handwritten gift note" and "prices left off the packing slip" | 14 Nov (decision 31) |
| W3-8 | "100%" removed from every new merino line (cardigan, set, beanie). The wording is now "merino wool [CLAIM-CHECK]". The live lambswool crew line is not new copy, so it stays as live | 31 Oct |
| W3-10 | Cardigan: Black is in stock, Brown/Blue are made to order with 10 working days. Production's 2 per colour are upside only, not a promise. No copy change was needed (s1.1) | 24 Oct (count) |
| W3-11 | A separate made-to-order order-by line now goes on the cardigan, beanie and hat & scarf set PDPs and in the FAQ, with Baltic second-stop dates. Publish by **Mon 9 Nov** (s2.3a). The CSV row is `mto_orderby_line` | **4 Nov** |
| W3-12 | The returns words come out of the delivery line. They go into package **P-RET** (PDP returns line + policy-page change, one proposal). P-RET goes live in full or not at all, and only after the adviser answers (G9). This replaces the old advice to publish the PDP line first (s1.0a) | 3 Nov (adviser pack), then the adviser |
| W3-13 | New shipping-line copy for the assumed zone policy (s1.0b). It goes live only together with the owner's change to the store shipping settings and the Merchant Center shipping settings. Until then, the current line stays | 31 Oct (final 11 Nov) |
| W3-5, W3-9, W3-14 | No CRO change | — |

---

## 1. Final PDP copy for the 5 priority SKUs (A-GM-02) — DRAFT-ASSUMPTION

These replace the open `[OWNER/PRD: X]` slots in `2026-10-21-pdp-copy-proposals.md` and `2026-10-21-wave2-updates.md`
s2/s4. Some gaps are owner-only facts and are **not** assumed: model height/size, fibre %, beanie height, and S/M or L/XL
to EU mapping. For those, the instruction is "omit the line", so the page still reads complete without them.

### 1.0 Shared lines (all 5)

**Delivery line (in stock)**. Dispatch wording follows A-GM-03. Delivery times are the Ops interim line, unchanged.
Free shipping stays because store settings are unchanged (A-GM-18):
> Free shipping to eligible destinations. In-stock items leave Riga in 2–5 working days. Delivery after that:
> Latvia 2–5, EU 5–10, USA, Canada and Australia 7–20 working days.

(W3-12: "14-day returns, see Shipping & Returns." has been taken out of this line. It now lives in package P-RET, s1.0a.)

### 1.0a Package P-RET: PDP returns line + policy-page change (W3-12, A-OPS-23) — HELD until the adviser answers (G9)
This is one proposal. The owner applies both parts on the same day, or neither, so the site never shows two
different returns rules.
- **Part 1, PDP line** (all 5 priority PDPs, under the delivery line):
  > 14-day returns on every piece, including made-to-order colours. See Shipping & Returns.
- **Part 2, Shipping & Returns page:** delete the sentence that says made-to-order pieces are non-returnable
  [OWNER: paste the exact live sentence]. Replace it with:
  > You can return any order within 14 days of delivery, including pieces made to order in a standard design and colour.
  > [ADVISER: confirm the wording, the return-shipping cost rule and any exception for personalised pieces.]
- **Gate:** the adviser has answered (pack sent by 3 Nov) and the owner has approved. If the adviser rules differently,
  CRO rewrites both parts together.
- Until then, neither part goes live. The PDPs carry no returns line and the live policy page stays as it is.
- Rollback: restore the old policy sentence and remove the PDP line, both on the same day.

### 1.0b Shipping line for the assumed zone policy (W3-13, A-GM-18 amended) — goes live only with the settings change
Use this line only on the day the owner changes the Squarespace shipping zones. The Merchant Center account
shipping settings must change at the same time, because feed shipping is set at account level and a price mismatch
gets items disapproved. Until then, keep the s1.0 line.
> Shipping: free to Latvia, Estonia and Lithuania. Other EU countries: free from EUR 150, otherwise EUR 12. USA,
> Canada and Australia: EUR 15. In-stock items leave Riga in 2–5 working days. Delivery after that: Latvia 2–5,
> EU 5–10, USA, Canada and Australia 7–20 working days.

Shipping & Returns page block (same policy):
> | Destination | Shipping | Delivery after dispatch |
> |---|---|---|
> | Latvia, Estonia, Lithuania | Free | Latvia 2–5 working days; Estonia, Lithuania [OPS: confirm row] |
> | Other EU countries | Free from EUR 150, otherwise EUR 12 | 5–10 working days |
> | USA, Canada, Australia | EUR 15 | 7–20 working days |
> | Other countries | Shown at checkout if we ship there. We cannot promise a delivery time | — |

Rules: no "free worldwide" and no "free shipping" without the zone named. US/CA/AU are not promoted (no ad, pin or
bar mentions them). Remove "Free shipping to eligible destinations" from the bar, cart line (P4) and FAQ on the same day.
[OWNER: confirm whether the store ships to Rest of World at all.]

**Made-to-order line** (A-PRD-14 via A-GM-03 / W3-1):
> Made to order: leaves Riga within 10 working days, then the delivery times above. *(garments)*
> Made to order in your colour: leaves Riga within 5 working days, then the delivery times above. *(beanie)*

**Process line**. It replaces the live "Knitted on a manually operated knitting machine and hand-sewn in Latvia" on
every PDP, per A-GM-10, which does not allow "hand-sewn in Latvia":
> Knitted on manual machines and finished by hand in Riga.

**Etsy proof** (A-GM-11 wording). Use it only where the owner approves the placement (form item 17); otherwise leave it out:
> 4.9 stars, 1,400+ reviews on Etsy (Mareshop).

**Returns note (A-GM-16, superseded by W3-12).** The earlier advice ("publish the PDP line, hold the policy page") is
withdrawn. All returns wording is now in package P-RET (s1.0a), which goes live in full or not at all.

### 1.1 Merino Wool Raglan Cardigan (`691050bcb0c4…`, EUR 160) — A-CRO-01, A-PRD-14
Title: no change. Description (new text; DETAILS, MEASUREMENTS and CARE blocks stay as live):
> A relaxed raglan cardigan in merino wool [CLAIM-CHECK]. Slightly oversized, so it sits easily over a shirt or
> a fine knit, and it can be worn open or buttoned.
> Colours: Black, Brown and Blue. Choose your colour below before adding to cart. The main photos show Black; Brown and
> Blue are the same pattern and measurements.
> Black is ready to ship. Brown and Blue are made to order: they leave Riga within 10 working days, then the delivery
> times below.
> Fit: relaxed, slightly oversized, one size. *(Add "Model is __ cm." only when the owner gives it.)*
> Knitted on manual machines and finished by hand in Riga.
> [Delivery line, in stock]

SEO title / meta: unchanged from the wave-1 proposal (60 / 152 chars).
> [MTO order-by line, s2.3a, by 9 Nov]

Remaining owner checks: one size confirmed? (form item 9). W3-10: the customer promise is made to order (10 wd) for
Brown/Blue until the physical count on 24 Oct. Production's 2 per colour are upside only. Black is in stock.

### 1.2 Oversized Merino Wool Raglan Sweater — Dusty Pink (`69105bd9b0c4…`, EUR 155) — A-PRD-12 (6 listed, real)
Title proposal is unchanged from wave 1 (feed rows change in the same pass, feed decision D7). Point edits only:
> Fit: oversized and roomy, easy to layer. Compare the width with a sweater you own (measurements below, Size Guide).
> Knitted on manual machines and finished by hand in Riga.
> [Delivery line, in stock]

"Material: merino wool" stays as live. No % is added (A-GM-10). The EU size mapping and model line are left out
until the owner supplies them.

### 1.3 Women's Classic Lambswool Crew Sweater (`691059dfdc1b…`, EUR 136) — A-CRO-02, A-PRD-12 (16 listed → 8 assumed)
> Colour: Grey.
> Fit: relaxed. Between sizes? Compare the width with a sweater you own (measurement table below, Size Guide).
> Knitted on manual machines and finished by hand in Riga.
> [Delivery line, in stock]

"100% lambswool (pure new wool)" stays as live, [CLAIM-CHECK] (PRD-17). Meta description is unchanged from wave 2.

### 1.4 Merino Wool Hat & Scarf Set (`69105624c6bf…`, EUR 110) — A-CRO-03, A-GM-02 (Black promoted)
> Colours: Black, Gray or Brown. Choose your colour below before adding to cart. The photos show Black.
> Material: merino wool [CLAIM-CHECK].   *(replaces "100% extra-fine merino wool, Italian-spun yarn", A-GM-10, W3-8)*
> Black is ready to ship. Gray and Brown are made to order [OWNER: confirm]: they leave Riga within 5 working days.
> Knitted on manual machines and finished by hand in Riga.
> [Delivery line, in stock]
> [Gift line]
> [MTO order-by line, s2.3a, by 9 Nov]

The sentence "the hat and scarf come in the same colour" is left out until the owner confirms it. The kraft-packaging
gift sentence was removed under W3-7 (no packaging wording at all).

### 1.5 Rib-Knit (Merino) Beanie — Unisex (`69105690dc1b…`, EUR 45) — A-CRO-03, A-PRD-12 (220 → 0 on shelf)
> A unisex merino beanie in a medium-thick rib with a fold-over cuff. The forehead band is knitted smooth and straight,
> so it does not press or leave a line. Suits short or long hair.
> Colours (11): Black, Brown, Navy, Blue, Gray, Light grey, Beige, Camel, Bordeaux, Pink, Melange grey. Choose your
> colour below before adding to cart. The photos show Black; the other colours are the same knit and shape.
> Size: one size with gentle stretch, fits 54–58 cm heads.
> Material: merino wool [CLAIM-CHECK].   *(drops "100%", "extra-fine", "Italian-spun", A-GM-10, W3-8)*
> Made to order in your colour: leaves Riga within 5 working days, then the delivery times below.
> Knitted on manual machines and finished by hand in Riga.
> [Delivery line]
> [Gift line]
> [MTO order-by line, s2.3a, by 9 Nov]

Because the beanie's made-to-order time (5 wd) fits inside the 2–5 wd promise, the shared line is not contradicted.

---

## 2. CRO-25 Christmas banner and lines — DRAFT-ASSUMPTION (dates: A-OPS-16..19, after ruling W3-1)

Dates come from the Ops register, recomputed for W3-1 on 21 Oct. CRO counted the working days independently and got
the same dates. Orders must be placed before 12:00 Riga time (A-OPS-13). Delivery target is Wed 23 Dec. Every date
is internal until the owner approves it (A-GM-28, 20 Nov). All carrier dates are 2025-based estimates.

| Zone | In stock | Made to order: garments (10 wd) | Made to order: beanie / hat set (5 wd) | Promise |
|---|---|---|---|---|
| Latvia | Wed 16 Dec | Fri 4 Dec | Fri 11 Dec | Yes, if carrier confirms |
| Estonia, Lithuania | Tue 15 Dec | Thu 3 Dec | Thu 10 Dec | Yes, if carrier confirms |
| EU (other, main zones) | Mon 7 Dec | **Thu 19 Nov** | Thu 26 Nov | Yes, if carrier confirms (L) |
| US, Canada, Australia | (Thu 26 Nov) | (Fri 13 Nov) | (Mon 23 Nov) | **"Christmas delivery not guaranteed"** (C3). No date is published |
| Rest of world, EU remote zones | — | — | — | No Christmas date (A-OPS-07/20) |

**Finding (urgent for planning).** The EU made-to-order garment date (Thu 19 Nov) and the US garment date
(13 Nov) both fall **before** the 20 Nov publish date (A-GM-28). Proposal A-CRO-07: publish only the made-to-order
lines (cardigan Brown/Blue, beanie, hat & scarf set) by **Mon 9 Nov**. GM ruling W3-11 assumes yes, including the
Baltic second stop (s2.3a). If not, the 20 Nov banner can only say that made-to-order
garments are too late for EU Christmas delivery. Owner decision by 4 Nov.

### 2.1 Announcement bar (from Fri 20 Nov; one line, fits 390px; no countdown, no exclamation marks)
- Until Mon 7 Dec: `Christmas delivery in the EU: order by Mon 7 Dec. Latvia: by Wed 16 Dec. Details in Shipping.`
- Tue 8 – Wed 16 Dec: `Christmas delivery in Latvia: order by Wed 16 Dec, Estonia and Lithuania by Tue 15 Dec.`
- From Thu 17 Dec until 25 Dec (W3-6, A-CX-03, no gift card): `Ordering now? It may arrive after Christmas. Add a handwritten gift note and we will write the delivery date on it.` [CX: align with the A-CX-03 final text]
- Remove on 25 Dec. The dates apply to in-stock pieces. Made-to-order dates are on the PDP and in the Shipping block.

### 2.2 Shipping & Returns / FAQ block
> **Ordering a gift?** For delivery before Christmas, order in-stock pieces by Mon 7 Dec (EU), Tue 15 Dec (Estonia,
> Lithuania) or Wed 16 Dec (Latvia), before 12:00 Riga time. Made-to-order pieces need more time: garments by
> Thu 19 Nov (EU), Thu 3 Dec (Estonia, Lithuania) or Fri 4 Dec (Latvia); beanies and hat & scarf sets by Thu 26 Nov
> (EU), Thu 10 Dec (Estonia, Lithuania) or Fri 11 Dec (Latvia). The Latvia, Estonia and Lithuania dates apply to
> delivery addresses in those countries only. We cannot guarantee Christmas delivery to the US, Canada or Australia.

W3-11: the made-to-order sentences of this block go live in the FAQ by **Mon 9 Nov**, together with the s2.3a PDP lines.
The in-stock sentence follows on 20 Nov. The bar never mentions made-to-order dates.

### 2.3 PDP lines (under the delivery line; the earliest date for each product type governs)
| PDP | Line | Publish |
|---|---|---|
| Cardigan (Black, in stock) | `Christmas: order Black by 7 Dec (EU) or 16 Dec (Latvia).` | 20 Nov |
| Dusty pink, Lambswool crew, Hat & scarf set (Black) | `Christmas: order by 7 Dec for EU delivery, by 16 Dec in Latvia.` | 20 Nov |
| Cardigan Brown/Blue, beanie, set Gray/Brown | Made-to-order order-by line, s2.3a | **9 Nov** (W3-11) |

### 2.3a Made-to-order order-by lines (W3-11, A-CRO-07; Baltic second stop) — publish by Mon 9 Nov
| PDP | Line | After a date passes |
|---|---|---|
| Cardigan | `Brown and Blue are made to order. For Christmas, order by 19 Nov for EU delivery, by 3 Dec for Estonia and Lithuania, or by 4 Dec for Latvia.` | From 20 Nov drop the EU part. From 5 Dec remove the line |
| Beanie | `Made to order in your colour. For Christmas, order by 26 Nov for EU delivery, by 10 Dec for Estonia and Lithuania, or by 11 Dec for Latvia.` | From 27 Nov drop the EU part. From 12 Dec remove the line |
| Hat & scarf set | `Gray and Brown are made to order [OWNER: confirm]. For Christmas, order by 26 Nov for EU delivery, by 10 Dec for Estonia and Lithuania, or by 11 Dec for Latvia.` | Same as beanie |

Baltic dates apply to Baltic delivery addresses only. US/CA/AU: no date, only "We cannot guarantee Christmas delivery
to the US, Canada or Australia" (FAQ). All dates are A-OPS-16..19 assumptions, and the owner confirms by **4 Nov**.
Layer: COPY (PDP description + FAQ). Rollback: delete the line.

Layer: NATIVE (Announcement Bar) plus COPY (page text and PDP description). No script is needed. Rollback: delete
the line or bar. In-stock dates apply only to units the owner has confirmed (Ops rule 3). If stock runs out, the PDP
falls back to the made-to-order date.

---

## 3. CRO-26 Gift options — DRAFT-ASSUMPTION (A-GM-22, A-CRO-04, A-CRO-05)

| Option | Assumed decision (A-GM-22) | How (no script) | Cost (FIN-19) | Customer copy |
|---|---|---|---|---|
| G1 Gift note | **Yes**, short handwritten card | Optional checkout field "Gift message (optional)" [VERIFY that the field exists on the current plan]; fallback is a reply to the order email (A-CRO-04) | EUR 0.70 per gift order (A-CRO-05, L) | "Sending a gift? Add a handwritten gift note: type your message at checkout." (fallback: "…reply to your order confirmation with your message.") |
| G2 Price-free parcel | **Yes** | The owner does not put a priced packing slip in gift parcels [VERIFY whether the Squarespace packing slip shows prices]. Order emails go to the buyer, not the recipient | EUR 0 | "Ship it straight to them: use their address at checkout. Prices are left off the packing slip." |
| G3 Gift wrap | **No** | — | — | Not offered. **No packaging wording at all** (W3-7): no "gift packaging", no "kraft packaging", no "ready to give". The only gift lines are "add a handwritten gift note" and "prices left off the packing slip". [OWNER: the live beanie/set PDPs mention kraft packaging. The new copy replaces those descriptions, so the line disappears when the owner applies them] |
| G4 Extended Christmas exchange | **No**, until the adviser answers | — | — | No wording. Standard 14-day returns only (A-GM-16) |

Where to place it: one FAQ answer ("Can I send it as a gift?") combining G1+G2, the same line under the delivery
line on the hat & scarf set and beanie PDPs, and a CX macro GIFT that reuses the wording. FIN-19 sees a cost of
EUR 0.70 per gift order; at the beanie price (EUR 45) that is under 2% of net. This is an illustrative check, and
FIN owns the margin call. The decision on G1 is reversible, because the field can be removed.

---

## 4. CRO-24 Feed fix and trim decisions — DRAFT-ASSUMPTION (A-GM-24, A-GM-02, A-GM-10, A-PRD-12, A-CRO-08)

Full row list: `2026-10-21-wave3-feed-decisions.csv`. These are decisions for the proposal TSV (CRO-23), which is
built only after the photo deadlines below. Nothing is uploaded, and the owner uploads.

| # | Decision | Rows | Effective | Basis |
|---|---|---|---|---|
| D1 | Trim the turtleneck colour rows if there are no per-colour photos | 33 | 31 Oct | A-GM-24 (turtleneck deadline 31 Oct); alternate SKU only |
| D2 | Trim the hat & scarf set Gray and Brown rows if no photos | 2 | 14 Nov | A-GM-24; A-GM-02 promotes Black only |
| D3 | Trim the beanie rows for the 10 non-Black colours if no photos | 10 | 14 Nov | A-GM-24 |
| D4 | Trim the cardigan Blue row if no photo; keep Brown (it has image_10) | 1 | 14 Nov | A-GM-24 |
| D5 | Cardigan Brown (and Blue if kept) set to `backorder` + `availability_date` = upload date + 14 days; Black stays `in_stock` | 1–2 | next upload | A-CRO-01, A-CRO-08 |
| D6 | Beanie rows stay `in_stock` (made to order in 5 wd fits the 2–5 day handling time) | 1–11 | next upload | A-PRD-12/14, A-CRO-08 |
| D7 | Dusty pink `color` Pink → Dusty Pink (3 rows). The title follows only if the owner applies the PDP title | 3 (+2 title) | next upload | Colour = PDP; A-GM-19 |
| D8 | Exclude the V-neck vest row with the blank colour until the owner names the colour (no colour assumed) | 1 | next upload | Required attribute; never invent |
| D9 | Lambswool crew `color` stays Grey | 4 | — | A-CRO-02 |
| D10 | Descriptions: remove "extra-fine", "Italian-spun"; replace "hand-sewn in Latvia" with "Knitted on manual machines and finished by hand in Riga."; fibre name without % in the changed rows | 14 + 1 + 79 HAND rows | next upload | A-GM-10 |
| D11 | Availability for the other SKUs follows A-PRD-12: listed 0 → `out_of_stock`; 12/16 → in_stock (50% > 0); 220/360 → made-to-order rule (D5/D6); duplicates share one pool (A-PRD-13) | all 98 | next upload | A-PRD-12/13; generator hard-codes in_stock |

Result if no photos arrive: 98 − 46 trimmed − 1 vest = **51 rows**. Every promoted row then shows its own colour.
Re-upload checklist: `2026-10-21-feed-qa.md` (unchanged).

---

## 5. Experiment log update
- EXP-04 (new, Christmas lines): Because gift buyers need an order-by date, adding the Christmas lines (s2) to the
  5 priority PDPs and the bar for all traffic will increase orders placed before 7 Dec. Metric: orders by date,
  "will it arrive" emails (CX). Start: publish date. Read on 8 Dec and 17 Dec. Rollback: remove the bar and lines.
  Qualitative read only (no split test).

## Unverified / owner checks
- Whether the checkout custom field and the packing-slip price setting exist on the current plan (G1, G2).
- Whether the 2 overlay CSS lines are present (CRO-22): this matters before any Christmas traffic. Still BLOCKED.
- Real stock and made-to-order status per variant (form item 8); colour name Grey (item 12).
- Hat & scarf set: whether Gray and Brown are made to order (W3-11 line on the set PDP).
- The exact live sentence about made-to-order returns on the Shipping & Returns page (P-RET part 2).
- Whether the store ships to the Rest of World at all, and which Merchant Center shipping settings must change with W3-13.
