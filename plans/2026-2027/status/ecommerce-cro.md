# E-commerce & CRO — status 2026-10-21
Summary: 16 done · 10 blocked · 8 todo

| ID | Task | Due | Status | Output / blocker |
|---|---|---|---|---|
| CRO-01 | Feed QA report incl. availability vs stock check, image-mismatch count, fix list | 2026-10-23 | DONE | [feed QA](../../../business-os/ecommerce-cro/2026-10-21-feed-qa.md), [fix list CSV](../../../business-os/ecommerce-cro/2026-10-21-feed-fix-list.csv). 46 mismatch rows (not 48), 1 blank colour, beanie title ≠ H1; full proposal TSV waits for CRO-23 |
| CRO-02 | Read Merchant Center diagnostics (approved > 0 checkpoint) | 2026-10-23 (approved > 0 by 28 Oct) | BLOCKED | Owner: MC Products → Diagnostics screenshot (no login for agents) |
| CRO-03 | PayPal connected | 2026-10-31 | BLOCKED | Owner: PayPal credentials, Settings → Payments → Connect (decision 14) |
| CRO-04 | Provisional 5 priority PDPs proposed to GM (readiness-based) | 2026-10-24 | DONE | [PDP audits s0](../../../business-os/ecommerce-cro/2026-10-21-pdp-audits.md): raglan cardigan, beanie, hat & scarf set, long shawl-collar cardigan, dusty pink raglan. GM/owner confirm 24 Oct, re-confirm 4 Nov |
| CRO-05 | KPI baseline input for week 2026-10-19 (conversion, AOV, notes text) | 2026-10-24 | DONE | [weekly baseline s3](../../../business-os/ecommerce-cro/2026-10-21-weekly-baseline.md); kpi-weekly.csv not edited (ruling C16) |
| CRO-06 | One shared PDP delivery line + made-to-order variant | 2026-10-28 | DONE | [copy proposals s0](../../../business-os/ecommerce-cro/2026-10-21-pdp-copy-proposals.md); OPS must reconcile with MC 4–10 day service (C8) |
| CRO-07 | Priority PDP 1–2 audits (cardigan, beanie) | 2026-10-31 | DONE | [PDP audits](../../../business-os/ecommerce-cro/2026-10-21-pdp-audits.md) |
| CRO-08 | Priority PDP 1–2 copy diffs | 2026-10-31 | DONE | [copy proposals](../../../business-os/ecommerce-cro/2026-10-21-pdp-copy-proposals.md), [CSV](../../../business-os/ecommerce-cro/2026-10-21-pdp-copy-proposals.csv) |
| CRO-09 | Priority PDP 3–5 audits + copy diffs | 2026-11-07 | DONE | Same two files (provisional set; redo per-SKU copy if GM picks other SKUs) |
| CRO-10 | Size/fit + cm measurement format, one block for all PDPs, gap matrix | 2026-11-07 | DONE | [size-fit standard](../../../business-os/ecommerce-cro/2026-10-21-size-fit-standard.md): 10 sized garments lack measurements, 4 lack fibre % |
| CRO-11 | Scoped unfreeze request for the 5 priority PDPs | 2026-10-31 | DONE | [copy proposals s6](../../../business-os/ecommerce-cro/2026-10-21-pdp-copy-proposals.md); owner decides (decision 19) |
| CRO-12 | November real test-order + refund checklist (desktop + phone, card + PayPal) | 2026-11-07 | DONE | [checklist](../../../business-os/ecommerce-cro/2026-10-21-test-order-checklist-november.md) |
| CRO-13 | November test-order run + refunds | 2026-11-07 | BLOCKED | Owner runs it (agents never order); PayPal runs need CRO-03 |
| CRO-14 | Cart / checkout / mobile audit from repo evidence | 2026-10-21 | DONE | [checkout-mobile audit](../../../business-os/ecommerce-cro/2026-10-21-checkout-mobile-audit.md) |
| CRO-15 | Site-wide buying-copy conflicts (returns wording, reply time, made-to-order, "hand-knitted"/"handmade", FAQ payments) | 2026-10-31 | DONE | [checkout-mobile audit C2–C6](../../../business-os/ecommerce-cro/2026-10-21-checkout-mobile-audit.md); final returns wording waits for adviser (G9) |
| CRO-16 | CSS proposals keeping overlay fix | 2026-10-31 | DONE | [CSS + native proposals](../../../business-os/ecommerce-cro/2026-10-21-css-native-proposals.md); selectors marked [VERIFY] |
| CRO-17 | Cart reassurance line, Shop H1, "No results found" fix proposals | 2026-11-21 | DONE | [CSS + native proposals P4, P5, N2](../../../business-os/ecommerce-cro/2026-10-21-css-native-proposals.md) |
| CRO-18 | Plan-upgrade input (what CRO gains; when worth it) | 2026-11-04 | DONE | [checkout-mobile audit s4](../../../business-os/ecommerce-cro/2026-10-21-checkout-mobile-audit.md); price TODO owner |
| CRO-19 | Weekly note #0 (baseline) + experiment log (EXP-01, EXP-02) | 2026-10-24 | DONE | [weekly baseline](../../../business-os/ecommerce-cro/2026-10-21-weekly-baseline.md) |
| CRO-20 | Weekly site-improvement notes every Friday (24 Oct – 26 Dec) | 2026-10-24 first | TODO | Needs that week's sessions/orders; first note Fri 24 Oct |
| CRO-21 | Weekly 390px smoke + ATC-without-colour retest | weekly from 2026-10-24 | BLOCKED | Owner phone screenshots (WebFetch cannot see JS/overlays); text-level pass done in CRO-14 |
| CRO-22 | Monthly check that overlay CSS is still in Custom CSS | 2026-10-31 | BLOCKED | Owner screenshot of Custom CSS panel (checklist step A1) |
| CRO-23 | Variant photos bound → feed proposal TSV + QA + re-upload checklist | 2026-11-14 | BLOCKED | Owner/Creative: per-colour photos (turtleneck 31 Oct, rest 14 Nov, C7) + confirmed stock (decision 4). Re-upload checklist ready in feed QA |
| CRO-24 | Trim decision for 46 at-risk feed rows if no photos | 2026-11-14 | BLOCKED | Owner decision 29; trim list ready in fix list CSV |
| CRO-25 | Christmas last-order-date banner per country | 2026-11-14 (publish 20 Nov) | BLOCKED | OPS carrier-backed cut-offs (14 Nov) + owner approval; template in CSS + native proposals |
| CRO-26 | Gift options (wrap, note, gift-receipt wording) | 2026-11-14 | BLOCKED | FIN cost check (sku-economics blank) + owner decision 31 |
| CRO-27 | Apply all approved PDP changes | 2026-12-05 | BLOCKED | Owner approval + scoped unfreeze (decision 19); PRD/owner facts: lead times, measurements, fibre %, claims evidence (G8) |
| CRO-28 | Site-change freeze from 12 Dec + defect-watch 12–24 Dec | 2026-12-12 | TODO | Future |
| CRO-29 | December test order (phone, card) + refund | 2026-12-15 | TODO | Future; reuse CRO-12 checklist R2 |
| CRO-30 | Q4 retrospective with before/after table | 2026-12-31 | TODO | Future |
| CRO-31 | Q1 2027: plan-upgrade decision applied, 22 PDPs on one template, category pages with SEO, colour-twin copy, native contact form, adviser returns wording | 2027-03-31 | TODO | Future |
| CRO-32 | Q2 2027: first conversion read, funnel events if upgraded, bundles/threshold after unit economics, spring PDPs, monthly feed refresh | 2027-06-30 | TODO | Future |
| CRO-33 | Q3 2027: on-site reviews, Shop page restructure, A/B only at ~1,000 sessions/week, LV/DE feasibility, gift landing page | 2027-09-30 | TODO | Future |
| CRO-34 | Q4 2027: freeze from mid-Nov, gift flow reused, monthly test orders, retrospective, 2028 input | 2027-12-31 | TODO | Future |

## Blocked on owner
- Merchant Center Diagnostics screenshot today (21 Oct checkpoint) so CRO can read approvals (CRO-02).
- Connect PayPal by 31 Oct, then run the November test-order checklist with refunds by 7 Nov (CRO-03, CRO-13).
- Raglan cardigan: are Brown and Blue in stock (export: 2 each) or made to order? Lead time? Do made-to-order
  colours keep the 14-day return? (CRO-08, CRO-27; adviser G9.)
- Scoped unfreeze of the 5 priority PDPs, or proposals-only (decision 19, 31 Oct) (CRO-11, CRO-27).
- Per-colour photos (turtleneck by 31 Oct; beanie, set, cardigan Blue by 14 Nov) or approve trimming the 46 feed rows
  (CRO-23, CRO-24).
- Confirm physical stock per SKU (beanie 20/colour and turtleneck 10/variant look like placeholders) (CRO-01, CRO-23).
- Facts for PDP copy: fibre % (dusty pink pieces, beige vest, distressed), garment measurements for 10 sized
  garments, model height/size, beanie height, V-neck vest colour name (CRO-10, CRO-27).
- Claims evidence: "hand-sewn in Latvia", "extra-fine", "Italian-spun" by 31 Oct (G8, decisions 16 and 34).
- Screenshots: Custom CSS panel (overlay lines), Contact page at 390px (reply-time CSS line), Shop page at 390px
  ("No results found"), weekly abandoned-cart count (CRO-21, CRO-22).
- Approve or reject the copy, CSS and native proposals in `business-os/ecommerce-cro/` (CRO-27).
