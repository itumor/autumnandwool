# Real test-order + refund checklist — November 2026 run — for the OWNER

Owner: aw-ecommerce-cro wrote it; the OWNER runs it (agents never place orders or enter payment details).
Task CRO-12. Run by 7 Nov (CRO plan) — PayPal runs only after PayPal is connected (decision 14, 31 Oct).
Time: about 45 minutes for 4 orders + refunds. Cost: order values are refunded; payment-provider fees on refunded
test orders may not be returned [VERIFY on Stripe/PayPal fee pages]. Mark every order "TEST" in Squarespace notes and
exclude it from `kpi-weekly.csv` (put the order numbers in the `notes` column).

## A. Before you start (5 min)
- [ ] A1 Custom CSS: screenshot the bottom of the panel showing the two overlay lines (`.sqs-widgets-confirmation-overlay`,
      `.sqs-widgets-confirmation` … `pointer-events:none`). If missing, STOP and tell CRO.
- [ ] A2 Settings → Payments: screenshot showing Stripe connected, Test mode OFF, and PayPal state.
- [ ] A3 Use a private/incognito window on desktop and a normal browser on your phone (not logged into Squarespace).

## B. Runs (fill one row per run)
| Run | Device | Payment | Product(s) | Country at checkout |
|---|---|---|---|---|
| R1 | Desktop | Card | Rib-Knit Beanie, a NON-default colour (e.g. Camel) | Latvia |
| R2 | Phone | Card or Google Pay | One sized garment (size M) + the beanie | Latvia |
| R3 | Desktop | PayPal (once live) | Hat & Scarf Set, Gray | Latvia |
| R4 | Phone | PayPal (once live) | Raglan cardigan, Brown | Latvia |

For each run, tick and note anything odd:
- [ ] B1 PDP loads; price shown; photo shows (note if the chosen colour's photo does NOT show)
- [ ] B2 FIRST press Add To Cart WITHOUT choosing colour/size: write the exact message you see, or "nothing happened"
- [ ] B3 Choose colour/size, Add To Cart: cart count goes up; page still clickable afterwards (no frozen screen)
- [ ] B4 Cart: correct item, colour/size and price; change qty to 2 and back to 1; totals right
- [ ] B5 Checkout: is guest checkout possible without creating an account? (yes/no)
- [ ] B6 Which country is pre-selected? (note it) → choose Latvia
- [ ] B7 Shipping step: price EUR 0.00? Is a delivery time shown? (copy the wording)
- [ ] B8 Tax line: what does it show? (screenshot for FIN/accountant)
- [ ] B9 Payment step: which methods are offered? (card brands, Google Pay, Apple Pay, PayPal) — screenshot
- [ ] B10 Pay. Confirmation page appears with an order number
- [ ] B11 Confirmation email arrives within 10 min: from-name, reply-to address, does it promise tracking/dispatch time? (forward a copy to CRO's evidence folder, or screenshot)
- [ ] B12 Order appears in Squarespace Orders with the right variant name
- [ ] B13 Phone only: any field hard to tap, keyboard covering the button, or zoom needed? (screenshot)

Optional (one run only): before paying R2, open the checkout, enter your email, close the tab, and wait 1 day: does
the abandoned-cart reminder arrive? (Recover abandoned carts is Live.) Then finish or delete.

## C. Refund each order (same day)
- [ ] C1 Squarespace Orders → order → Refund full amount, reason "test"
- [ ] C2 Refund email arrives to the buyer address (screenshot)
- [ ] C3 Stripe / PayPal dashboard shows the refund (screenshot)
- [ ] C4 Stock: refunding may not restock automatically — check the item's stock is back to the earlier number [VERIFY]

## D. Record (paste into the weekly note or send to CRO)
| Run | Order # | B2 message | Guest OK | Default country | Delivery time shown | Tax line | Methods offered | Email OK | Refund OK | Problems |
|---|---|---|---|---|---|---|---|---|---|---|
| R1 | | | | | | | | | | |
| R2 | | | | | | | | | | |
| R3 | | | | | | | | | | |
| R4 | | | | | | | | | | |

Pass = all runs reach B12 and C3 with no frozen screen. Any fail → tell CRO the same day; CRO writes the fix proposal.
December run (CRO-29): repeat R2 (phone, card) only, plus PayPal if it failed in November.
