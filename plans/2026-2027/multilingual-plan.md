# Multilingual storefront (English → Latvian, Russian later) — plan, 25 Nov 2026

DRAFT for owner approval. Author: planning session, 25 Nov 2026. **Nothing here is applied to the live site.**
Every live step is an owner action in the Squarespace admin (Weglot is connected through Squarespace settings,
not through code). Unknown numbers are `TODO` / `[FILL]` — none are forecasts or verified prices.
This plan follows the owner's answers on 25 Nov 2026 and the constraints in `AGENTS.md` and `PROJECT-HANDBOOK.md`.

## 1. Decisions locked with the owner (25 Nov 2026)

| ID | Decision | Consequence |
|---|---|---|
| D1 | Source language English (`en-US`); **Latvian is phase 1**; Russian is a later rollout | Only LV is built now. RU needs its own budget/reviewer gate (§8). |
| D2 | Customer surface = **responsive website only** (desktop + 390 px mobile) | No native app, no PWA, no app-store work. Verify LV at mobile width. |
| D3 | Use **Squarespace's built-in Weglot integration** (7.1 Site Languages) | No Code Injection, no inline `<script>`. The overlay CSS guard stays untouched. |
| D4 | Native Latvian review by owner / named native reader | Weglot drafts; a human fixes LV wording on money pages before launch. Name = `[FILL]` owner input. |
| D5 | Written plan only; **status tables untouched** | Rollup owns the task counts. Proposed `LOC-*` IDs below are for later registration. |

## 2. Starting point (facts, with source)

| Area | Fact | Source |
|---|---|---|
| Current language | English only (`en-US`); `lang` present, no `hreflang` | `GROWTH-PLAN-100-IDEAS.md` S8; `evidence/seo-audit-2026-11-10/findings/technical.md` §hreflang |
| Growth-plan gap | "A Latvian version of the key pages (home, about, shipping, 5 bestsellers)" = idea #31 (Med impact / Low effort) | `GROWTH-PLAN-100-IDEAS.md` §S8, §idea 31 |
| Platform | Squarespace 7.1; Basic assumed (2% store fee); **Code Injection 403**, inline `<script>` gated, waitlists gated | `PROJECT-HANDBOOK.md` §3; `business-os/head-of-ecommerce/assumptions-wave3.md` A-GM-05 |
| Load-bearing guard | `.sqs-widgets-confirmation-overlay` and `.sqs-widgets-confirmation` must keep `pointer-events:none !important;` in Custom CSS | `PROJECT-HANDBOOK.md` §4 |
| Upgrade decision | Decision #24 (plan upgrade) due 4 Nov; memo verdict Case A = stay on Basic through Q4, still ASSUMED pending billing screenshot | `plans/2026-2027/master-plan.md` row 24; `plans/2026-2027/status/OPEN-TASKS.md` GM-13. **Not required for Weglot.** |
| Measurement | GA4 page_view works; ecommerce events absent (plan-gated). Orders come from Squarespace Orders | `PROJECT-HANDBOOK.md` §5.9, §7 |
| Native reader | Native-language review is an open owner item (CRE-23 / form Q12); LV festival copy already waits on it | `campaign-assets/drafts/plan-wave2/december-gift-peak-prep-2026-10-21.md` CO-3; `.../plan-wave3/christmas-order-by-posts-assumed.md` |
| Legal wording | Returns/withdrawal wording awaits EU adviser (PRD-19, due 20 Nov, adviser input pending) | `plans/2026-2027/status/production.md` PRD-19 |
| Official mechanism | Squarespace 7.1 "Site Languages" → Multilingual by Weglot. Header switcher, optional language subdomains, translated customer notification emails on by default | Squarespace Help Center, *Creating a multilingual site with Weglot*, last updated 3 Apr 2026 (checked 25 Nov 2026) |
| Official limits | Free: 1 destination language, ≤2,000 words; 10-day trial ≤10,000 words. Over 2,000 words or 2+ languages → paid Weglot plan. Not translated: Email Campaigns, Acuity, third-party blocks, Member Sites / account login | same official guide |

## 3. Scope and non-goals

**In scope (phase 1):** English source + Latvian destination on the existing Squarespace store; header language switcher;
human-reviewed LV copy on the money pages; LV behaviour verified on desktop and 390 px mobile; LV order-email behaviour
verified; basic language SEO signals checked; Russian held behind a decision gate.

**Out of scope:** native/iOS/Android app, PWA/installable home-screen app, Code Injection or custom scripts, a second
Squarespace site, Russian content, translating Email Campaigns or account screens (platform does not support it),
edits to the Custom CSS overlay guard, and any legal rewrite of returns terms before the adviser answers.

**Money pages for the LV review pass:** home, about, `/shipping-returns`, `/faq`, `/size-guide`, and the 5 priority PDPs
(priority SKU list comes from GM/Production — currently provisional per master-plan C5). Product prices stay EUR, sizes
and brand/product names are locked, and no unverified claim ("handmade", "made in Latvia", "sustainable") may be added
in translation (`GROWTH-PLAN` S8 source; `aw-brand-voice` rules; markets file header).

## 4. Approaches considered (why Weglot won)

| Approach | Trade-off | Verdict |
|---|---|---|
| Built-in Weglot (7.1 Site Languages) | No code injection; covers whole storefront + order emails; editable in Weglot dashboard; recurring cost above 2,000 words / 1 language; machine output needs native review; some surfaces not translated | **Chosen** |
| Manually duplicated LV pages + CSS-only switcher | Free; full wording control; but Squarespace products share one catalog so PDP/cart/checkout stay English, `lang`/`hreflang` not reliable, switcher fragile, and Custom CSS edits risk the overlay guard | Rejected except as a fallback if Weglot is unavailable on this plan |
| Second Squarespace site on an LV subdomain | Native content and separate analytics; but doubles catalog, stock, orders, Merchant Center feed and subscriptions | Rejected at 22 SKUs / current order volume |

## 5. Phase 1 work breakdown

Task IDs are proposals only; they are **not** in the status tables (D5).

### Phase 0 — verify the gate and baseline (owner in admin; assistant reads evidence)

| ID | Task | Owner / role | Done when |
|---|---|---|---|
| LOC-01 | Open Settings → Website → Language & region → **Site Languages**; confirm the "Multilingual by Weglot" Connect control exists on the current plan. If it is absent, stop and escalate (fallback = manual pages, not code injection) | Owner | Screenshot/evidence note under `evidence/` |
| LOC-02 | Start the Weglot trial and record the **actual word count** for the whole site before choosing free vs paid. Do not enter a card without G1 | Owner | Word count written into G1 |
| LOC-03 | Record baseline: current `lang` value, canonicals, absence of `hreflang`, LV-language queries in GSC if any, and the 390 px mobile switcher area (header space) | SEO | Baseline table in this file or `evidence/` |
| LOC-04 | Confirm the overlay guard is still present in Custom CSS before any visual edits | CRO | Live CSS check recorded |

### Phase 1 — connect and translate

| ID | Task | Owner / role | Done when |
|---|---|---|---|
| LOC-05 | Connect Weglot: original English → destination Latvian. Set language visibility public in Site Languages | Owner | LV switcher visible in header |
| LOC-06 | Choose LV URL form (subdomain vs path). **Recommendation: subdomain** for separate Search Console / analytics read; subject to G2 | Owner + SEO | Decision recorded; URLs documented |
| LOC-07 | Style/position the header switcher so it is visible and tappable at 390 px, without custom script | CRO + Owner | Mobile screenshot in `evidence/` |
| LOC-08 | In Weglot dashboard: edit translations for the money pages (§3). Lock brand name, product names, sizes, EUR prices and Etsy/Mareshop trust wording | Owner + native reader | LV copy for each money page saved in Weglot |
| LOC-09 | Native LV review pass: wording, sizing, returns/shipping statements. Keep returns/withdrawal wording aligned with PRD-19 adviser outcome; if adviser has not answered, mark those lines `[PENDING ADVISER]` and do not publish altered legal terms | Owner / named reader (G3) | Reviewer name + date recorded |
| LOC-10 | Decide paid Weglot plan if word count > 2,000 or if RU is added later; price verified on Weglot pricing page, not assumed (G1) | Owner | Plan active or site confirmed at/below free limit |

### QA and launch gate

| ID | Task | Owner / role | Done when |
|---|---|---|---|
| LOC-11 | Functional QA, desktop + 390 px: switcher works; LV persists across ≥5 pages into cart/checkout; prices/stock unchanged; LV product → cart → checkout path works; **failed add-to-cart overlay guard still works**; cookie/consent banner still works | CRO + Owner | QA checklist with screenshots under `evidence/` |
| LOC-12 | Technical QA: verify `lang` on LV URLs, canonical and `hreflang` behaviour, sitemap inclusion, and that no new `<script>`/Code Injection appeared. If `hreflang` cannot be set without code, record it as a known limitation, not a failure to hide | SEO | Findings appended to `evidence/seo-audit-2026-11-10/` or new evidence note |
| LOC-13 | Order-email check: confirm customer notification emails follow the language used (Weglot default), or disable that toggle deliberately; note Email Campaigns remain English-only | Owner + CX | Test-order result recorded |
| LOC-14 | Launch: make LV public, announce to LV followers only after native review is signed off | Owner | Live URL + date in this plan |

### Measurement and the Russian gate

| ID | Task | Owner / role | Done when |
|---|---|---|---|
| LOC-15 | 30–60 day read: Squarespace Analytics + Orders for LV sessions/orders; GSC LV-page clicks/impressions; customer enquiries in LV. Do not attribute revenue from GA4 alone (plan-gated events) | GRO | Readout with observed numbers |
| LOC-16 | Russian go/no-go (§8). Requires 2nd Weglot language (paid plan), native RU reviewer, and observed demand | Owner | Decision logged |

## 6. Owner decision gates / inputs

| ID | Needed from owner | Why it blocks |
|---|---|---|
| G1 | Paid Weglot plan yes/no, with the **actual quoted price and date**; free tier only if ≤2,000 words | Above 2,000 words translations stop displaying on the free plan |
| G2 | LV subdomain vs path (recommendation: subdomain) | Determines URL, GSC property and QA scope |
| G3 | Name of native Latvian reviewer (also closes the open CRE-23 / Q12 item) | Blocks money-page sign-off and launch |
| G4 | Confirm LV returns/withdrawal wording after PRD-19 adviser answer | Legal wording must not be invented by translation |
| G5 | 5 priority PDP list (provisional per master-plan C5) | Defines LOC-08 review scope |
| G6 | Russian go/no-go after LOC-15 | The RU rollout cannot start without budget + RU reviewer |

## 7. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Machine translation of legal/returns copy changes the offer | LOC-09 native review; `[PENDING ADVISER]` until PRD-19 lands; no new claims |
| Word count over free limit → translations silently not displayed | LOC-02 measures before launch; G1 decides plan; LOC-10 confirms |
| Header switcher crowds mobile header or breaks tap targets | LOC-07 with 390 px evidence; no custom script |
| Custom CSS edit reintroduces click-trap overlay | LOC-04 check; overlay guard is never edited; LOC-11 rechecks after failure click |
| `hreflang` / `lang` cannot be controlled on this plan | LOC-12 records the truth; no code injection workaround; accept and document |
| Unsupported surfaces stay English (Email Campaigns, account screens, third-party blocks) | Listed in §3; CX copy tells LV customers support email path; no claim of "fully translated site" |
| Language lost on deep links or checkout | LOC-11 tests persistence into checkout; if broken, raise with Weglot/Squarespace support, do not patch with script |
| Two translation systems drift when products change | Weglot dashboard is the single translation store; re-review money pages when prices/copy change |

## 8. Russian — later rollout criteria (not started)

Start only when **all** are true: (a) G6 approved after LOC-15; (b) paid Weglot plan covers a 2nd destination language;
(c) a native Russian reviewer is named; (d) LV QA checklist is green. Work then repeats LOC-05 → LOC-13 for RU.
Latvian and Russian are separate language × market measurements; do not roll their traffic into one number.
Demand evidence examples: GSC RU queries, customer emails in RU, or LV/RU market-stall feedback (owner-supplied).
Date for the gate: TODO after LV launch date is known.

## 9. What this plan does not do

- No live Squarespace changes are made by this plan; every LOC task is owner-executed.
- No status-table rows added; no rollup counts changed (D5).
- No GA4/GTM or DataForSEO action; no `seo-geo` scripts run — outputs stay drafts/proposals per `AGENTS.md`.
- No PRD-19 legal answer, no new sustainability/handmade/made-in-Latvia claim, no plan-upgrade (#24) dependency.

## 10. Sources

- Squarespace Help Center: *Creating a multilingual site with Weglot* (last updated 3 Apr 2026; checked 25 Nov 2026) and
  *Manually creating a multilingual site* — official integration steps, word limits, unsupported surfaces, subdomains.
- `PROJECT-HANDBOOK.md` §3–§5, §7 — plan gates, overlay guard, measurement baseline.
- `GROWTH-PLAN-100-IDEAS.md` S8 and idea 31; `evidence/seo-audit-2026-11-10/findings/technical.md` (hreflang).
- `plans/2026-2027/master-plan.md` rows 24, 33 and conflict C5; `plans/2026-2027/status/OPEN-TASKS.md` GM-13 / PRD-19.
- `business-os/head-of-ecommerce/assumptions-wave3.md` A-GM-05; `business-os/head-of-ecommerce/plan-upgrade-memo-prep-2026-10-21.md`.
- `campaign-assets/drafts/plan-wave2/december-gift-peak-prep-2026-10-21.md` (CO-3) and wave-3 Christmas posts draft (native reader).
- Owner answers in this session, 25 Nov 2026 (D1–D4 above).
