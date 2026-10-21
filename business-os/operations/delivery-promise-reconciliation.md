DRAFT — for owner approval

# Delivery promise reconciliation (master plan ruling C8)

OPS-12, agent `aw-operations`, 2026-10-21. For CRO (PDP delivery line) and SEO (Merchant Center). Proposal only:
the agent changes no setting, page or feed. All values below are as recorded in repo files; re-check live pages
before acting [VERIFY].

Sources: `implementation-report.md` (shipping recheck 18 Oct; FAQ / Shipping & Returns / homepage / Merchant
Center rows; feed-country fix); `.claude/skills/aw-brand-voice` s3; `.claude/skills/aw-fulfilment-sop`;
`plans/2026-2027/master-plan.md` C8; `zero-sales-diagnosis-2026-10-18.md` (as cited in C8).

## 1. Where delivery promises appear today

| Place | Dispatch | Latvia | EU | US / CA / AU | Other | Price |
|---|---|---|---|---|---|---|
| Squarespace shipping settings | none | no time | (Rest of World) no time | US zone + Rest of World, no time | Rest of World = every other country | EUR 0 all three zones |
| Merchant Center shipping policy | 2-5 business days handling | 2-5 transit | 18 named countries, 5-10 transit | 7-20 transit | none | Free |
| Merchant Center feed countries | — | yes | only the 12 euro countries (Czechia, Denmark, Hungary, Poland, Romania, Sweden excluded: non-EUR) | excluded (non-EUR) | — | EUR |
| Live FAQ (per 18-19 Oct update) | 2-5 working days | in "Europe" | about 5-10 working days | 7-20 days ("working" not stated) [VERIFY] | — | — |
| Older FAQ recheck (same report, earlier pass) | 1-2 business days | — | 2-4 days; UK/Ireland 3-5 | worldwide 5-10 | — | — | 
| Brand-voice rule | 2-5 working days | in "Europe" | about 5-10 working days | 7-20 | — | "Free shipping to eligible destinations" |
| Handbook (per C8) | — | — | "EU-19 + UK/NO/CH 4-10 days" | — | — | — |
| Announcement bar / homepage | — | — | — | — | — | "Free shipping · 14-day returns" |

## 2. Gaps found

| # | Gap | Risk | Proposal (owner decides) |
|---|---|---|---|
| 1 | **Estonia and Lithuania are not in the Merchant Center EU-18 list**, yet ship free under Squarespace "Rest of World" | Nearest export markets get no Google free listing and no stated delivery time | SEO adds EE/LT to the MC EU policy (both use EUR, so the feed can include them) once a carrier time is known; dry-run T3 |
| 2 | Squarespace "Rest of World" ships **free to every country**, incl. UK, NO, CH and countries with no promise, no carrier price and customs exposure | Margin loss, customs surprises, untested checkout | Owner decision 21: restrict Rest of World to priced, promised countries, or add paid zones, after carrier rates |
| 3 | Handbook lists UK/NO/CH; Merchant Center does not | Conflicting promise to partners and press | Drop UK/NO/CH from all copy until priced and customs-checked |
| 4 | FAQ says "7-20 days" for US/CA/AU (unit unclear); MC says business days | Customer counts calendar days, expects earlier delivery | Use "working days" everywhere |
| 5 | Two FAQ versions recorded in the same report (1-2 / 2-4 vs 2-5 / 5-10) | One may still be live somewhere (FAQ vs Shipping & Returns page) | CRO re-checks both pages live before any new line |
| 6 | No range is carrier-verified; only Latvia checkout-tested | Late deliveries vs promise | Dry run 6 Nov + carrier rates; then confirm or tighten |
| 7 | Squarespace checkout shows no delivery time | Diagnosis issue #2 (conversion) | CRO adds the line below to PDP/checkout notes after owner OK |

## 3. Proposed single source of truth (interim, no new range)

Uses only the ranges already submitted to Merchant Center (the interim ceiling per C8):

> Dispatch in 2-5 working days. Delivery after dispatch: Latvia 2-5 working days; EU 5-10 working days;
> USA, Canada and Australia 7-20 working days. Free shipping to these destinations.

Owner: approve, edit, or wait for dry-run data (6 Nov). OPS owns this table; CRO/SEO/CX/Creative copy it unchanged.
Next revision: after OPS-11 dry run and OPS-06 carrier rates (target 14 Nov, G5).

## TODO / missing data

- Live re-check of FAQ, Shipping & Returns, PDP delivery line, announcement bar (CRO).
- Owner decisions 3 (dispatch promise) and 21 (free-shipping regions).
- Carrier transit times per region (OPS-06).
