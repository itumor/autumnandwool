---
name: aw-utm-attribution
description: Use when building or checking any tracked link for Autumn & Wool (social post, bio, ad, creator, email, Etsy), creating a creator discount code scheme, or reconciling which channel or creator drove Squarespace orders.
---

# aw-utm-attribution

One taxonomy, one source of truth for orders, and honest readouts. Attribution is directional, not proof.

## 1. Facts this store runs on (21 Oct 2026)

- **Source of truth for orders and revenue: Squarespace Orders** (and Etsy for marketplace sales).
- GA4 `G-7TV8PK060Z` records sessions and their source/medium, but **no purchase events** (Code Injection is
  plan-gated). So GA4 can say which links bring visitors, not which ones sell.
- So for anything that needs per-sale credit (creators, affiliates), the **discount code is the primary
  attribution key**. UTMs are the secondary key.

## 2. UTM rules

- All lowercase, words joined by **hyphens**. No spaces, no underscores, no personal data, never on internal links.
- Always set `utm_source`, `utm_medium` and `utm_campaign`. `utm_content` tells variants apart.
- Mediums are picked so GA4's default channel groups sort traffic correctly (GA4 docs, see Sources).

| Placement | utm_source | utm_medium | utm_campaign | utm_content |
|---|---|---|---|---|
| Bio links (owner-action-pack section C, keep exactly) | instagram / tiktok / facebook / pinterest | social | bio-link | (none) |
| Etsy → site | etsy | marketplace | move-to-site | (none) |
| Organic post / pin | platform | social | `<theme>-<yyyy-mm>` e.g. `winter-knitwear-2026-11` | `<sku-slug>-<format>` e.g. `beanie-reel` |
| Meta ad | facebook (or instagram) | paid-social | test slug from the brief | `{{ad.name}}` dynamic, or the concept letter |
| Google Ads | none, keep **auto-tagging (gclid)** on | none | none | none |
| Merchant Center free listings | none, Google labels it "Shopping Free Listings" when linked | none | none | none |
| Creator (gifted or affiliate) | `creator-<handle>` | affiliate | `gifting-<yyyy-mm>` or `affiliate-<yyyy-mm>` | `<platform>-<format>` e.g. `ig-reel` |
| Email (MailerLite) | mailerlite | email | `<flow-or-issue>-<yyyy-mm>` | `<link-position>` |
| Market / print QR code | qr | offline | `<event-slug>-<yyyy>` | `<card-type>` |

Why creators use `affiliate`: GA4 sorts medium=affiliate into its own Affiliates channel, so creator traffic
stays separate from organic social. `paid-social` matches GA4's paid regex `paid.*`. `social` matches Organic Social.

**Known inconsistency:** `campaign-assets/campaign-drafts.md` uses `organic_social` and underscores
(`winter_knitwear`). Propose correcting those drafts to this table before anything is published. Don't edit live links.

Base landing URLs: a PDP for single-SKU content, `/shop` for bio links. Check that the URL loads (HTTP 200) and
that the query string survives any shortener.

## 3. Creator discount codes

- Format: `HANDLE10` (uppercase handle + percent), one code per creator, so you can see who drove each order in Squarespace Orders.
- Discount size is a margin decision. Check it with `aw-unit-economics`: price ex VAT − discount − variable
  costs must stay above the minimum contribution per order. Propose; the owner creates the code in Squarespace.
- Whether Squarespace on the current plan supports per-code usage limits and reports orders by code is
  UNVERIFIED. Check in Marketing → Discounts before promising a creator a report.

## 4. Link builder output (append to `business-os/growth/utm-links.csv`)

```
created,owner,placement,landing_url,utm_source,utm_medium,utm_campaign,utm_content,full_url,discount_code,status
```
Status is `draft` until the owner pastes it live. Never invent click or order numbers.

## 5. Attribution readout (weekly or per campaign)

```
# Attribution readout <date>
Question / decision:
Source of truth: Squarespace Orders (n = __), Etsy (n = __)
| Channel or creator | Sessions (GA4) | Orders with their code | Orders after their UTM visit (if visible) | Platform claims | Notes |
Survey answers ("How did you hear about us?"), if collected:
Confidence: low / medium / high, and why
Gaps / MISSING:
Recommendation + one test that would settle it:
```

Rules: never add platform conversions together. Show "platforms claim N, we can verify M". Direct and branded
traffic often hide creator or word-of-mouth effects, so name that blind spot instead of crediting "direct".
Propose a post-purchase "How did you hear about us?" question (pick-list + other) as an owner decision. On
Squarespace it may need a checkout form field, which is UNVERIFIED on this plan.

## Guardrails

- Never put an email, name or order ID in a URL.
- Never paste links into live profiles, ads or the store. Drafts only.
- Never report a channel as "not working" from GA4 alone while purchase events are missing.

## Sources

- thatrebeccarae/claude-marketing `skills/utm-attribution-strategy/SKILL.md`, MIT
  (https://github.com/thatrebeccarae/claude-marketing). Adapted: lowercase and hyphens, required params,
  governance checklist (no internal UTMs, check redirects, no PII).
- coreyhaines31/marketingskills `skills/attribution/SKILL.md`, MIT
  (https://github.com/coreyhaines31/marketingskills). Adapted: one source of truth, never sum platforms,
  "claim N, verify M", self-reported survey, direct/branded blind spots, readout outline.
- Google Analytics Help, "[GA4] Default channel group" (https://support.google.com/analytics/answer/9756891).
  Facts only: the medium rules for Organic Social, Paid Social and Affiliates.
- Compared but not chosen as base: coreyhaines `analytics` and `conversion-tracking` (they assume pixel/code
  access this plan lacks).
