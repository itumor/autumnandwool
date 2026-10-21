---
name: aw-cro-audit
description: Use when auditing or improving conversion on any Autumn & Wool page (home, shop, product page, cart, checkout, size guide, shipping/returns), checking the 6-step funnel, reviewing mobile 390px, planning a conversion experiment, or writing a before/after site-improvement note.
---

# aw-cro-audit — conversion audit for autumnandwool.com

Shared skill. `aw-product-page-copy`, `aw-ecommerce-seo`, `aw-merchant-feed-qa` and `aw-etsy-listing` reuse its
evidence rules and finding format.

## Facts to load first (do not re-discover)
- Squarespace 7.1, EUR. **Plan blocks Code Injection and inline `<script>`.** Fixes are limited to: Custom CSS,
  native block/page settings, product metadata (frozen, see below), navigation, Squarespace checkout settings.
  Never propose GA4 ecommerce events, Clarity, sticky ATC JS, review widgets or A/B tools that need a script
  unless the item is labelled `NEEDS PLAN UPGRADE` (README section 8 decision).
- **Product data is frozen.** Titles, descriptions, prices, variants, images, stock: propose only, as CSV or
  markdown diff. Never edit.
- Known traps: the overlay click-trap (`.sqs-widgets-confirmation-overlay`) is fixed by CSS in
  `PROJECT-HANDBOOK.md` section 4. Any CSS proposal must not remove or override those two rules. Variant
  Add-To-Cart silently no-ops if no colour is selected.
- Baseline traffic is tiny (62 visits / 30 days, 94% bounce on 17 Oct). Orders come from Squarespace Orders, not
  GA4. Conversion rate = orders / sessions from `business-os/kpi-weekly.csv`.

## Procedure
1. **Scope.** Name the page(s), the primary action (add to cart, checkout, email signup) and the traffic source
   (Instagram bio UTM, Google free listings, Pinterest, Etsy referral, direct). Default scope = the 5 priority
   PDPs (README section 12) plus cart and checkout.
2. **Collect evidence, read-only.** WebFetch the public page and read the local files (`llms.txt`,
   `QA-REPORT.md`, `build_google_feed.py` data, `catalog-claims-cleanup-v3.csv`). WebFetch strips scripts and
   cannot see JS-rendered schema, variant images or overlays: mark anything you could not see as `UNVERIFIED`
   and ask the owner/QA for a 390px screenshot instead of guessing.
3. **Run the 6-step funnel checklist** (README section 5). For each row record PASS / FAIL / UNVERIFIED +
   evidence (URL, quote or file:line):

   | Step | Check on each page |
   |---|---|
   | 1 Arrives | Above the fold at 390px: what it is, price, one real photo, one clear action. Brand promise visible |
   | 2 Explores | Photo per colour (variant image changes on select), fibre % stated, fit (relaxed/oversized), garment measurements in cm, size-guide link next to the selector |
   | 3 Decides | Review proof (Etsy 4.9 / 1.5k is marketplace history, say so), delivery cost + time, 14-day returns, stock/lead time, secure payment |
   | 4 Checks out | Variant selected before ATC, no dead clicks, cart totals, PayPal status, guest checkout, mobile fields |
   | 5 Receives | Order email, tracking promise, reply < 24 h stated (Contact) |
   | 6 Returns | Care advice, newsletter offer, related products ("Pairs well with") |

4. **Score each finding by impact order** (adapted from the marketingskills `cro` framework): value clarity →
   product facts and photos → CTA and variant selection → trust and delivery/returns → objection handling
   (sizing, wool itch, care, customs outside EU) → friction (extra clicks, overlays, form fields).
5. **Pick the fix layer** for each: `CSS` (you may draft the exact CSS) · `NATIVE SETTING` (owner clicks) ·
   `COPY PROPOSAL` (frozen data → diff) · `ASSET` (owner photo, see `aw-product-photo-briefs`) ·
   `NEEDS PLAN UPGRADE` · `OWNER DECISION`.
6. **Prioritise** with ICE (impact, confidence, ease, 1–5 each). Ship nothing; write the report.

## Experiments at this traffic level
- A/B testing needs thousands of sessions per variant (at a 1% baseline, ~150k per variant to detect a 10% lift).
  At current traffic **do not propose split tests.** Use:
  - *Fix-forward*: obvious defects (broken variant image, missing size link, contradictory delivery copy) are fixed,
    not tested.
  - *Sequential before/after*: one change per page per 2 weeks, log date in `kpi-weekly.csv` `notes`, compare
    ATC/checkout counts and qualitative evidence (customer emails, Etsy messages).
  - *Pre-launch checks*: 5-second test with 3–5 target customers, or a real mobile walk-through.
- Every experiment entry: hypothesis ("Because [evidence], changing [X] on [page] for [traffic] will increase
  [metric]"), metric, start/end date, layer, rollback step, result, decision.
- Revisit true A/B only when a page gets ~1,000+ sessions/week.

## Output template — `business-os/cro/<YYYY-MM-DD>-<page>-audit.md`
```
# CRO audit: <page> — <date>
Scope / traffic source / primary action
## Funnel checklist (step | result | evidence)
## Findings
| # | Step | Finding | Evidence | Layer | ICE | Proposed fix |
## Quick wins (CSS / native, owner can apply in < 15 min)
## Proposals needing approval (copy diffs, assets, plan upgrade)
## Experiment log entry (hypothesis, metric, dates, rollback)
## Unverified — needs screenshot or owner check
```
CSS proposals go in a fenced block with the selector scoped as tightly as possible and a one-line rollback.

## Guardrails
- Read-only on the live site. No logins, no cart actions, no test orders, no payment fields. The monthly real test
  order is an owner task; you only write its checklist.
- Never invent reviews, ratings, stock counts, delivery promises, fibre content, "handmade"/"sustainable"/"made in
  Latvia" claims. Use only facts in `llms.txt`, PDP text, or the verified rows of `catalog-claims-cleanup-v3.csv`;
  origin and "handmade" claims are still open (README section 7), so flag, don't add.
- Do not raise ad spend or promote SKUs off the production safe-to-promote list.
- Copy follows `aw-brand-voice`; money questions (free shipping threshold, discounts) go through
  `aw-unit-economics`.

## Sources
- coreyhaines31/marketingskills `skills/cro/SKILL.md` and `skills/ab-testing/SKILL.md` —
  https://github.com/coreyhaines31/marketingskills — MIT. Taken: impact-ordered analysis dimensions, quick-win /
  high-impact / test-ideas output split, hypothesis structure, sample-size table figure. Adapted, not copied.
- finsilabs/awesome-ecommerce-skills (checkout-flow-optimization, a-b-testing) —
  https://github.com/finsilabs/awesome-ecommerce-skills — MIT. Compared; generic platform advice, not used.
- Baymard Institute, apparel size information (free summary) —
  https://baymard.com/blog/apparel-size-information — proprietary; cited only for "size guide link next to the
  size selector" and "missing size info causes abandonment". Own words.
- Local: `business-os/README.md` §5, `PROJECT-HANDBOOK.md` §3–4, `QA-REPORT.md`.
