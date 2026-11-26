# Multilingual storefront (EN → LV) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use a subagent-driven or executing-plans workflow to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a native-reviewed Latvian version of autumnandwool.com through Squarespace 7.1's built-in Weglot integration, verified on desktop and 390 px mobile, with Russian held behind a later decision gate.

**Architecture:** Squarespace 7.1 Site Languages → Weglot translates the storefront at the platform layer; no custom code. Repo-side work supplies public-site evidence, an exact owner runbook, and reviewed Latvian copy drafts. Live admin steps are owner-executed because this agent has no Squarespace editing session in the sandbox.

**Tech Stack:** Squarespace 7.1 (Basic assumed), built-in Weglot integration, Squarespace Custom CSS (read-only verification), public HTML/CSS via `curl`, Markdown/CSV repo artifacts.

**Spec:** `plans/2026-2027/multilingual-plan.md` (read both documents).

## Global Constraints

- No Code Injection, no inline `<script>`, no new scripts on the live site (Squarespace plan gate; 403).
- Load-bearing guard `.sqs-widgets-confirmation-overlay` and `.sqs-widgets-confirmation` must keep `pointer-events:none !important;` in Custom CSS / `site.css`; never edit it.
- Current plan assumption A-GM-05 = Basic; decision #24 (upgrade) is separate and not required here.
- Money pages for LV review: home, about, `/shipping-returns`, `/faq`, `/size-guide`, 5 priority PDPs (list provisional per C5).
- Prices stay EUR; sizes, brand/product names, Etsy/Mareshop trust wording and the verified "4.9 stars, 1,400+ reviews" figure stay unchanged.
- No invented "handmade", "sustainable", "organic" or "made in Latvia" claims in any language.
- Returns/withdrawal wording stays `[PENDING ADVISER]` until PRD-19 lands; no legal terms rewritten by translation.
- Native Latvian review (owner or named reader) is required before any LV page is made public.
- Status tables are owned by `rollup.py`; do not edit them or their four counts for this work.
- No GA4/GTM live changes, no `seo-geo` scripts / DataForSEO calls; all outputs stay drafts/proposals.
- Owner-facing copies live under `business-os/`; generated evidence under `evidence/`.

## File Structure

| File | Responsibility |
|---|---|
| `evidence/multilingual-2026-11-25/live-baseline.md` | Verified public HTML/CSS facts before any LV change; baseline for later QA. |
| `business-os/localization/weglot-owner-runbook.md` | Exact admin click-path and settings for the owner, from official docs. |
| `business-os/localization/lv-money-pages-draft.md` | English source map, locked glossary, LV drafts flagged for native review. |
| `plans/2026-2027/multilingual-plan.md` | Design/spec (already committed, `85944f5`). |
| `plans/2026-2027/multilingual-implementation-plan.md` | This file. |

---

### Task 1: Capture the public-site baseline (LOC-03, LOC-04)

**Files:** Create `evidence/multilingual-2026-11-25/live-baseline.md`

- [ ] **Step 1:** Fetch the live homepage into a temp file and extract the language/SEO/header facts:

```bash
TMP="${TMPDIR:-/tmp}/aw-lv-baseline"
mkdir -p "$TMP"
curl -sSL -D "$TMP/home.headers" https://www.autumnandwool.com/ -o "$TMP/home.html"
grep -io '<html[^>]*>' "$TMP/home.html"
grep -io '<link[^>]*rel="canonical"[^>]*>' "$TMP/home.html"
grep -io '<link[^>]*hreflang[^>]*>' "$TMP/home.html" | head -20
grep -io '<title>[^<]*</title>' "$TMP/home.html"
grep -in 'weglot' "$TMP/home.html" | head -20
head -1 "$TMP/home.headers"
```

Expected: `<html lang="en">` (or equivalent), one canonical, zero `hreflang`, no Weglot markup. If any differ, record the actual value — do not normalize it.

- [ ] **Step 2:** Verify the overlay guard. Baseline finding: it lives **only in `custom.css`**, not in `site.css`
      (`site.css` has the base selectors without the guard). Use the exact versioned URL recorded in evidence:

```bash
curl -sSL 'https://static1.squarespace.com/static/custom-css/6908755e4a17f81b7629f4bc/6908755e4a17f81b7629f4c5/24/custom.css' -o "$TMP/custom.css"
grep -n 'sqs-widgets-confirmation-overlay\|sqs-widgets-confirmation' "$TMP/custom.css" | head -20
```

Expected: both selectors with `pointer-events:none !important;`. If that URL changes, find `custom.css` in the
stylesheet links of `home.html` and record the new URL. Checking `site.css` alone is not sufficient.

- [ ] **Step 3:** Write the evidence file with a fact table (URL, verified value, exact snippet), a baseline section for language/SEO/header, a separate overlay-guard section, and an explicit "not verified" list for anything requiring admin (Custom CSS panel contents, GSC data, word count).

- [ ] **Step 4:** Self-check: every claim in the file has a snippet or URL; nothing from `PROJECT-HANDBOOK.md` §3–§5 is restated as newly verified without a live snippet.

- [ ] **Step 5:** Commit only this file:

```bash
git add evidence/multilingual-2026-11-25/live-baseline.md
git commit -m "evidence: public baseline before Latvian rollout"
```

---

### Task 2: Write the owner runbook (LOC-01, LOC-05–LOC-10)

**Files:** Create `business-os/localization/weglot-owner-runbook.md`

- [ ] **Step 1:** From official Squarespace 7.1 Weglot documentation, extract: Site Languages path, connect flow, switcher customization, language subdomain setup, public/private language visibility, customer-notification-email toggle/preview, word-count thresholds and over-limit behaviour, and the unsupported-surface list.

- [ ] **Step 2:** Write numbered steps with exact menu labels. Anything not explicitly stated in official docs must be labelled `VERIFY` — never presented as fact. Quote the official wording for SEO/hreflang/canonical/`lang` claims, or state "not stated in official docs".

- [ ] **Step 3:** Add a pre-flight checklist mapping owner gates G1–G6 from the spec to the step where each is needed, with `[FILL]` slots for the quoted price, reviewer name, and launch date.

- [ ] **Step 4:** Verify with a read-back: every step has a source URL and a date checked (2026-11-25); no invented price or plan entitlement.

- [ ] **Step 5:** Commit only this file:

```bash
git add business-os/localization/weglot-owner-runbook.md
git commit -m "docs: owner runbook for Weglot LV setup"
```

---

### Task 3: Prepare Latvian money-page copy for review (LOC-08, LOC-09 prep)

**Files:** Create `business-os/localization/lv-money-pages-draft.md` (already assigned to a subagent; review before accepting).

- [ ] **Step 1:** Confirm the file contains: source map with LIVE/DRAFT/UNVERIFIED status per page, locked glossary, and LV drafts headed "DRAFT — native Latvian review required before publication".

- [ ] **Step 2:** Scan for banned claims (`handmade`, `sustainable`, `organic`, `made in Latvia`), inflated trust figures, changed EUR prices, and any returns/legal line missing `[PENDING ADVISER]`:

```bash
grep -in 'handmade\|sustainable\|organic\|made in latvia\|1,500' business-os/localization/lv-money-pages-draft.md
grep -in 'PENDING ADVISER' business-os/localization/lv-money-pages-draft.md
```

Expected: banned claims appear only inside a "do not use" note; every returns/legal line carries `[PENDING ADVISER]`.

- [ ] **Step 3:** Fix any violation inline; do not "improve" the translation without a native reviewer.

- [ ] **Step 4:** Commit only this file:

```bash
git add business-os/localization/lv-money-pages-draft.md
git commit -m "docs: draft Latvian money-page copy for native review"
```

---

### Task 4: Owner executes the live setup (LOC-01, LOC-02, LOC-05–LOC-10)

This task is **owner-only** in the Squarespace admin and Weglot dashboard. The agent cannot perform it from this sandbox. Each step produces evidence the agent can then verify.

- [ ] **Step 1 (owner):** Confirm Site Languages → "Multilingual by Weglot" Connect exists. Evidence: screenshot or short note. If absent → stop; use the manual-pages fallback from the spec, not code injection.
- [ ] **Step 2 (owner):** Start the Weglot trial, record the site's actual word count. Evidence: number + date in owner gate G1.
- [ ] **Step 3 (owner):** Decide paid plan vs free (G1), LV URL form (G2 — spec recommends subdomain), and native reviewer name (G3). Evidence: written decisions.
- [ ] **Step 4 (owner):** Connect English → Latvian, set LV public, style/position the header switcher for 390 px, and confirm the switcher is tappable. Evidence: desktop + mobile screenshots.
- [ ] **Step 5 (owner):** In Weglot, apply the locked glossary and reviewed money-page copy from Task 3; keep `[PENDING ADVISER]` lines out of publication. Evidence: saved translation IDs/screenshots.
- [ ] **Step 6 (owner):** Confirm order-notification email behaviour; leave default on if verified, or turn it off deliberately. Evidence: test-order result.
- [ ] **Step 7:** Agent verifies the evidence pack exists before Task 5 begins. If any gate is unresolved, report it as a blocker with the exact gate ID — do not guess.

---

### Task 5: QA the live LV storefront (LOC-11–LOC-14)

Requires Task 4 to be complete. All checks are read-only against the live site plus the evidence pack.

- [ ] **Step 1:** Switcher works on desktop and 390 px; LV persists across ≥5 pages and into cart/checkout; no English fallback on reviewed money pages except locked terms.
- [ ] **Step 2:** EUR prices, stock and sizes unchanged; LV product → cart → checkout completes (test order, refunded by owner).
- [ ] **Step 3:** Click-trap regression: deliberately fail an add-to-cart, then confirm the next click still works and the overlay guard is present in Custom CSS / `site.css`.
- [ ] **Step 4:** Technical: record `lang`, canonical and `hreflang` behaviour on LV URLs; confirm sitemap inclusion; confirm no `<script>`/Code Injection appeared. If `hreflang` cannot be set without code, record the limitation rather than hiding it.
- [ ] **Step 5:** Write results into `evidence/multilingual-2026-11-25/launch-qa.md` with screenshots, then commit that file.

---

### Task 6: Measurement and the Russian gate (LOC-15, LOC-16)

- [ ] **Step 1:** 30–60 days after LV launch, record Squarespace Analytics sessions, Squarespace Orders count, GSC LV clicks/impressions, and LV-language customer enquiries. Use `business-os/kpi-weekly.csv` only if the owner has populated it; otherwise keep a standalone table. Do not attribute revenue from GA4 alone.
- [ ] **Step 2:** Apply the Russian entry criteria from spec §8: G6 approved, paid Weglot plan covering a 2nd language, native RU reviewer named, LV QA green. Record evidence per criterion.
- [ ] **Step 3:** If any criterion fails, hold RU and log the failed criterion with date. No partial RU launch.

## Execution status (2026-11-25)

| Task | State | Note |
|---|---|---|
| Task 1 — public baseline | DONE | `evidence/multilingual-2026-11-25/live-baseline.md`; `en-US`, no hreflang, no Weglot, guard in `custom.css` only. |
| Task 2 — owner runbook | DONE | `business-os/localization/weglot-owner-runbook.md`, commit `e7898fd`. Subdomain SEO facts added. |
| Task 3 — LV copy draft | DONE (draft only) | `business-os/localization/lv-money-pages-draft.md`, commit `2266b79`. 94 rows, `translation-draft`; 28 `[PENDING ADVISER]`, 17 `[VERIFY]`. Native review (G3) and adviser (G4) still required before publication. |
| Task 4 — live admin setup | PARTIAL, then BLOCKED | Via ego-browser: Weglot connected with store email, LV enabled Public, 9 glossary rules added, word count measured (396/2,000 after 1 page). Evidence: `evidence/multilingual-2026-11-25/live-setup.md`. Blocked at G1 (paid plan; free tier cannot cover site), G2 (subdomain/hreflang), G3/G4 (reviewer/adviser), G5 (PDP list). |
| Task 5 — QA | BLOCKED (partial) | Switcher and LV homepage verified live; full QA needs reviewed translations + paid-plan decision + no subdomain yet. |
| Task 6 — measurement / RU gate | BLOCKED | Needs LV launch date and LOC-15 readout. |

## Self-Review (completed before handoff)

- Spec §1–§10 coverage: decisions → global constraints; phase 0 → Task 1+4; phase 1 → Tasks 2–4; QA/launch → Task 5; measurement/RU → Task 6; risks → global constraints + Task 4/5 gates; non-goals → global constraints.
- No TBD/TODO placeholders except deliberate owner-input slots `G1`, `G3`, launch date and the provisional priority-SKU list inherited from the spec.
- Owner gates G1–G6 are consistent with `multilingual-plan.md` §6; `LOC-*` IDs match §5.
