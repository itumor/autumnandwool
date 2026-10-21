# Creator attribution scheme: codes + UTM links (DRAFT, PAR-09)

Status: DRAFT for owner approval. Per `aw-utm-attribution` s2-s3 and GM rulings C6 and C15. No code is created and
no link is pasted anywhere. Growth owns `business-os/growth/utm-links.csv` (ruling C15), so the rows below are
**handed to Growth to append**, not written there by Partnerships.

## 1. Which key we use (ruling C6)

| Case | Primary key | Secondary |
|---|---|---|
| A. Decision 11 shows Squarespace discounts + per-code order view work on the current plan | `HANDLE10` code per creator, counted weekly in Squarespace Orders | UTM link (GA4 sessions only) |
| B. Discounts are plan-locked (CRO's reading) | **No codes in Q4.** UTM link per creator + weekly manual check of Orders for the creator's name/handle in order notes, plus the "how did you hear" answer if added | GA4 sessions |
| C. Plan upgraded (decision 24, 4 Nov) | As A, and GA4 purchase events become possible later | — |

GA4 has no purchase events today, so GA4 can show visits from a creator link, never sales. We never call a creator
"not working" from GA4 alone.

## 2. Discount code format (case A/C only)

- `HANDLE` + discount %, uppercase, letters and digits only: dots, underscores and hyphens removed. Example
  pattern: `@first.last_lv` gives `FIRSTLASTLV10`. If over [VERIFY: Squarespace max code length], shorten and log it.
- `10` is a **placeholder**. Discount size is the owner's margin decision (D5) after Finance gives min contribution
  (decision 23, 4 Nov): price ex VAT - discount - variable costs must stay >= min contribution.
- One code per creator. Proposed limits: end date [season end], usage limit [VERIFY plan support]. Owner creates it
  in Marketing > Discounts.

## 3. UTM pattern (creators)

| Param | Value |
|---|---|
| utm_source | `creator-<handle>` (lowercase, `.` and `_` become `-`) |
| utm_medium | `affiliate` (GA4 sorts it into the Affiliates channel) |
| utm_campaign | `gifting-2026-11` (or `affiliate-yyyy-mm` later) |
| utm_content | `<platform>-<format>`, e.g. `ig-reel`, `ig-story`, `tt-video` |

Landing page: the product page of the gifted SKU, or `/shop` for a mixed post. Check the URL returns 200 and the
query string survives any shortener. No personal data in any URL.

### Ready-made base URLs (append the UTM string)

| SKU | Landing URL (from `llms.txt`, [VERIFY] it loads before use) |
|---|---|
| Rib-Knit Merino Beanie | https://www.autumnandwool.com/shop/p/p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1 |
| Merino Wool Hat & Scarf Set | https://www.autumnandwool.com/shop/p/p/merino-wool-hat-scarf-set-extra-fine-rib-knit-soft-on-skin-warm-not-bulky-unisex-gift |
| Merino Turtleneck, lightweight | https://www.autumnandwool.com/shop/p/p/merino-wool-turtleneck-sweater-womens-knit-pullover-soft-warm-lightweight-minimalist-sustainable-knitwear-sizes-sl-12-679428 |
| Shop all | https://www.autumnandwool.com/shop |

Example (placeholder handle, not a real creator):
`https://www.autumnandwool.com/shop/p/p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1?utm_source=creator-examplehandle&utm_medium=affiliate&utm_campaign=gifting-2026-11&utm_content=ig-reel`

## 4. Rows for Growth to append to `business-os/growth/utm-links.csv` (one per agreed creator)

```
created,owner,placement,landing_url,utm_source,utm_medium,utm_campaign,utm_content,full_url,discount_code,status
<yyyy-mm-dd>,partnerships,creator-<handle>-<platform>,<landing_url>,creator-<handle>,affiliate,gifting-2026-11,<platform>-<format>,<full_url>,<CODE or none>,draft
```
No rows yet: no creator has agreed.

## 5. Weekly creator attribution readout (template)

```
# Creator attribution readout <date>
Question / decision:
Source of truth: Squarespace Orders (n = __), Etsy (n = __)
| Creator | Sessions (GA4, creator-<handle>) | Orders with their code | Orders naming them (notes / survey) | Platform claims | Notes |
Platforms claim N, we can verify M.
Confidence: low / medium / high, and why
Blind spots: direct/branded visits after a post, Etsy purchases by their followers
Gaps / MISSING:
Recommendation + one test that would settle it:
```

## 6. Owner decision proposed: "How did you hear about us?"
A pick-list (Instagram creator, Google, Etsy, friend, market, other + text) at checkout or in the order confirmation.
Squarespace checkout form field support on this plan: **UNVERIFIED** (CRO to check with decision 11).
