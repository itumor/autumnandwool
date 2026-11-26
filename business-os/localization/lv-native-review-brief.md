# Native Latvian review brief — Autumn & Wool storefront

DRAFT, 25 Nov 2026. For the owner or the named native Latvian reader (gate G3 in
`plans/2026-2027/multilingual-plan.md`). No live page may be published from a draft.

## 1. Source lock and scope

- Source language: English (`en-US`), previewed 2026-11-25. If a source page changes after that date, mark its LV
  translation `outdated` and review again before use.
- English source map and draft LV copy: `business-os/localization/lv-money-pages-draft.md`.
- Admin steps and Weglot limits: `business-os/localization/weglot-owner-runbook.md`.
- In scope for review: home, about, `/shipping-returns`, `/faq`, `/size-guide`, and the 5 priority PDPs (gate G5).
  The rest of the storefront can stay as Weglot output until a later review pass.

## 2. Risk tiers

| Tier | Content | Review required |
|---|---|---|
| High | Returns, withdrawal, delivery promises, sizing and care claims | Native reader **plus** the EU adviser outcome (PRD-19). Keep `[PENDING ADVISER]` until answered; do not rewrite legal effect by translation. |
| Medium | PDP copy, prices, product names, fibre wording, stock/scarcity phrases | Native reader; verify every number and product fact against the live page. |
| Low | Navigation, section headings, general marketing copy | Native reader; natural Latvian, calm tone. |

## 3. What the reviewer checks

1. **Meaning, not literal words.** Natural Latvian grammar, register and punctuation; no machine-translation artefacts.
2. **Locked glossary.** Brand "Autumn & Wool", Etsy shop "Mareshop", product names, sizes, EUR values and contact
   email are unchanged. The only approved proof line is "Formerly Mareshop on Etsy, 4.9★ from 1,400+ customers".
3. **Claims.** Do not introduce sustainable/eco/ethical/organic/certified/RWS/mulesing-free/carbon claims, "hand-knitted",
   "itch-free", "hypoallergenic", "machine-washable" or invented reviews. Prefer the precise process phrase
   "knitted on manual machines and finished by hand in Riga".
4. **Facts.** Fibre wording copied exactly from each live product page; delivery promises only dispatch 2–5 working days,
   Europe about 5–10, US/CA/AU 7–20; "14-day returns" only as currently stated, pending legal review.
5. **Links and UI.** Links keep working, EUR and sizes readable, no text overflow in the header or at 390 px.
6. **Metadata.** Page title and meta description in Latvian should match the page intent, not be word-for-word copies.

Full claim rules: `.claude/skills/aw-brand-voice/SKILL.md` §3 (read it before signing off).

## 4. Workflow states

`translation-draft` → `review` → `localized-ready` → (on source change) `outdated`.
Use the state column in `lv-money-pages-draft.md`. A page is `localized-ready` only after the reviewer signs the row.

## 5. Sign-off record

Reviewer name: `[FILL]` (gate G3) · Review date: `[FILL]` · Source version reviewed: 2026-11-25 preview

| Page | Tier | State | Reviewer initials / date | Notes or unresolved items |
|---|---|---|---|---|
| Home | Medium | translation-draft | | |
| About | Medium | translation-draft | | |
| /shipping-returns | High | translation-draft | | `[PENDING ADVISER]` |
| /faq | High | translation-draft | | `[PENDING ADVISER]` where returns are described |
| /size-guide | High | translation-draft | | |
| Priority PDP 1–5 (`[FILL]` list, gate G5) | Medium | translation-draft | | Fibre wording from each live PDP |

## 6. The reviewer does not

- Publish, enable a public language, or change returns/withdrawal terms.
- Invent sizes, prices, stock, delivery dates, certifications or reviews.
- Approve a page whose source has changed since the source lock without re-checking the affected text.
