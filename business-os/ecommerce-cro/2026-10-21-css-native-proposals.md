# CSS and native-setting proposals — 2026-10-21 — DRAFT for owner approval

Owner: aw-ecommerce-cro. Tasks CRO-15 (CSS proposals), CRO-18 (cart line, Shop H1, "No results found"), and the
copy template for CRO-17 (Christmas banner, dates blocked on OPS).
Plan gate: everything here works with Custom CSS or native settings. Nothing needs Code Injection or `<script>`.
Nothing is applied. Apply one change per page per 2 weeks (sequential before/after) and log the date.

## P0. Overlay click-trap guard — MUST STAY (handbook s4)
Every CSS change below is appended AFTER these two lines. Never delete, edit or reorder them. After any CSS paste,
the owner screenshots the bottom of the Custom CSS panel showing both lines still present.
```css
.sqs-widgets-confirmation-overlay{pointer-events:none !important;}
.sqs-widgets-confirmation{pointer-events:none !important;}
```

## P1. How to verify a selector before pasting (owner or QA, 2 min)
Selectors marked `[VERIFY]` are Squarespace 7.1 class names I could not see (WebFetch strips classes rendered by
JS). On desktop Chrome: right-click the element → Inspect → confirm the class exists. If it does not, do not paste.

## P2. Footer tap targets at phone width (QA s4: links 22px, icons 20–25px) — CSS, ICE 2/5/5
```css
/* AW-P2 footer tap targets — rollback: delete this block */
@media (max-width: 767px) {
  #footer-sections a { display: inline-block; min-height: 24px; padding-top: 4px; padding-bottom: 4px; } /* [VERIFY #footer-sections] */
}
```
Check after: footer at 390px, links not overlapping, no horizontal scroll.

## P3. Contact reply-time line (ruling C2: public promise 1–2 business days) — CSS text edit, ICE 3/3/5
Handbook s5.5 says a CSS-rendered line reads "Email us at autumnandwool@gmail.com — we reply within 24 hours."
The page text now says 1–2 business days, so the two may contradict on screen.
Owner: in Custom CSS press Ctrl/Cmd+F, search `24 hours`. If found, change only the text inside `content:"..."` to:
`Email us at autumnandwool@gmail.com — we reply within 1–2 business days.`
Rollback: put the old text back. If not found: nothing to do (screenshot the Contact page for the record).

## P4. Shop page "No results found" (only if a 390px screenshot shows it) — CSS, ICE 2/2/4
The text "No results found / No results match your search. Try removing a few filters." is in the Shop HTML next to 22
products. It may already be hidden by Squarespace's script. Screenshot first. If visible:
```css
/* AW-P4 hide empty-state when products are listed — rollback: delete this block */
.product-list:has(.product-list-item) .product-list-empty-state { display: none !important; } /* [VERIFY all three class names] */
```
`:has()` works in current Chrome, Safari and Firefox; on older browsers the rule is ignored (no harm).

## P5. Cart reassurance line near Checkout (by 21 Nov) — CSS, ICE 2/3/4
Text (all facts already published on /shipping-returns):
"Free shipping to eligible destinations · 14-day returns · Secure checkout"
```css
/* AW-P5 cart reassurance — rollback: delete this block */
.cart-container .cart-checkout::after { /* [VERIFY selector on /cart with an item in the cart] */
  content: "Free shipping to eligible destinations · 14-day returns · Secure checkout";
  display: block; margin-top: 12px; font-size: 13px; line-height: 1.4; color: #24201C; text-align: center;
}
```
Accessibility note: CSS `content` is not reliably read by screen readers. If Squarespace offers a native cart text
field on this plan, prefer it [VERIFY]. Add "PayPal" to the line only after PayPal is live.

## Native settings (owner clicks, no code)
| ID | Where | Change | Why | ICE |
|---|---|---|---|---|
| N1 | Settings → Payments | Connect PayPal | Second payment route (decision 14) | 4/4/4 |
| N2 | Shop page → header text block | Set "The collection" to Heading 1 | Shop has no H1 | 2/5/5 |
| N3 | Navigation | Add "Size guide" → /size-guide to header | QA s2; sizing is the top apparel objection | 2/4/5 |
| N4 | Commerce → checkout / store location | Default country Latvia if available [VERIFY option] | Defaults to US today | 2/3/5 |
| N5 | Announcement bar | Christmas order-by line (template below), only on 20 Nov after approval | Gift buyers need dates (G5) | 4/4/5 |
| N6 | Product → Related products | Show beanie / hat & scarf set on cardigan PDPs if manual selection exists on plan [VERIFY] | AOV | 2/3/3 |

## Christmas order-by template (CRO-17; dates come only from OPS, ruling C3)
Announcement bar (one line, phone-safe, ≤ 90 chars per variant):
"Christmas delivery: order by [OPS date] (Latvia) or [OPS date] (EU). Details in Shipping."
FAQ / Shipping page block:
"Ordering a gift? Order by [OPS date] for Latvia and [OPS date] for the rest of the EU and the UK [OPS: confirm UK/NO/CH
cut-off]. For the US, Canada and Australia we cannot guarantee delivery before Christmas. Made-to-order colours need
[PRD: X] extra working days."
Rules: no countdown, no "last chance"; publish only after OPS carrier-backed dates (14 Nov) and owner approval
(20 Nov); remove on 25 Dec.
