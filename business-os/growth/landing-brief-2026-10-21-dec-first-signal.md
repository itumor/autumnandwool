# Landing-page brief: dec-first-signal   Status: DRAFT, for aw-ecommerce-cro (`aw-cro-audit`)

From aw-growth-marketing, 2026-10-21. Read-only checks; product data is frozen, so every fix is a proposal for the
owner. Test brief: `test-2026-10-21-dec-first-signal.md`.

## Scope
- Page: PDP of the ONE SKU the owner picks for the test (TODO, decision 2). Also `/shop` (bio-link landing).
- Traffic source: Meta paid-social, mobile-first (390 px), cold visitors who have never heard of A&W.
- Primary action: add to cart, then checkout. Order counted in Squarespace Orders.

## What the ad promises (the page must confirm each within one scroll on mobile)
| Ad concept | Promise | PDP must show |
|---|---|---|
| A making-of | Knitted on a manual machine, finished by hand in Riga (after G8) | Same wording in description or a process line |
| B proof | 4.9 stars, 1,400+ reviews on Etsy (Mareshop) | Same Etsy line, attributed, near price or ATC |
| C product truth | Exact fibre, free shipping to eligible destinations, 2-5 working day dispatch | Fibre line, delivery line, 14-day returns |

## Pass criteria (CRO marks PASS / FAIL / UNVERIFIED with evidence)
1. Real photo for every colour sold; variant image changes on select (owner pack A).
2. Variant must be selected before ATC, or a visible message; known silent no-op on variant ATC (memory note).
3. Size info: garment measurements in cm and size-guide link next to the selector.
4. Delivery line present (beanie PDP has it, checked 21 Oct: "Free shipping. In-stock items ship from Riga within
   2-5 working days. 14-day returns.") and consistent with OPS ranges (C8).
5. Price shown and identical to the ad.
6. Etsy proof line visible (C1 wording), not only "Formerly Mareshop on Etsy" in the footer.
7. PayPal live (G4, decision 14) or a stated reason to launch without it.
8. Stock state true (no `in_stock` for sold-out items; 13 sold-out vs feed per SEO).
9. No visible errors. **Found 21 Oct:** hat & scarf set PDP shows newsletter text "This newsletter signup form needs a
   storage option..." Please check all candidate PDPs and route the fix (native setting, owner).
10. Load and tap test at 390 px: no overlay click-trap regression (PROJECT-HANDBOOK s4 CSS stays).

## Output requested
`business-os/cro/<date>-<sku>-audit.md` per `aw-cro-audit` template, with overall PASS/FAIL for gate 3 in
`paid-test-gates.md`. Needed by 14 Nov.
