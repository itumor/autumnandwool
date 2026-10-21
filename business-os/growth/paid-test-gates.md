# Paid-test gate tracker   Status: DRAFT, updated 2026-10-21 by aw-growth-marketing

Rule (skill `aw-paid-ads-testing` s0, master ruling C10): no brief leaves BLOCKED and no euro is spent until all 6
gates PASS. Default December spend = EUR 0. Last owner go/no-go: 20 Nov (master decision 33).

| # | Gate | State 21 Oct | Evidence | Unblocks when | Who | Master gate / decision | Due |
|---|---|---|---|---|---|---|---|
| 1 | SKU costed (`contrib` in `unit_economics.py`) | FAIL | `sku-economics.csv`: cost columns blank on all 82 rows, `target_cac_eur` blank | Owner times 3 units per priority SKU, PRD proposes costs, owner confirms, script run | Owner, PRD, FIN | G0, G1; decisions 5, 28 | 5 SKUs 4 Nov, 22 by 11 Nov |
| 2 | SKU GREEN in owner-approved `capacity-YYYY-Www.md` | MISSING | No capacity file in `business-os/` | PRD publishes Friday file; SKU GREEN needs G1 | PRD, owner | G2 | first real GREEN after 4 Nov |
| 3 | PDP ready (photo per colour, size info, delivery time, price) | FAIL | Variant photos missing: beanie (10 colours), turtleneck (11), hat set (2), cardigan Blue (owner pack A). Delivery line present on beanie PDP ("ship from Riga within 2-5 working days", checked 21 Oct); other PDPs not checked | Photos bound, CRO landing check PASS (see `landing-brief-2026-10-21-dec-first-signal.md`) | Owner, CRE, CRO | G4, C7; decision 29 | 14 Nov |
| 4 | Orders countable | PASS (manual) | Squarespace Orders; test orders #00003/#00004 refunded | n/a. Weekly export by owner | Owner | n/a | weekly |
| 5 | Platform conversion signal (Meta Pixel / Google Ads purchase tag) | UNVERIFIED | Code Injection plan-gated (README s8) | Plan decision; if upgraded, run checklist below | Owner, CRO | G7; decision 24 | 4 Nov |
| 6 | Owner monthly ceiling | MISSING | No approved ceiling. Suggested EUR 200-300 Dec, EUR 0 valid | Owner names a number after gates 1-5 and FIN cash check (G3) | Owner, FIN | G3; decision 33 | 20 Nov |

Extra checks (not gates, but block launch): claims evidence G8 (31 Oct) for any "Riga" / "finished by hand" ad line;
Christmas order-by dates G5 (OPS, carrier-backed 14 Nov) for test end date; photo rights for "ChatGPT Image" files
(decision 16).

## Conversion-signal checklist (run only after a plan upgrade; owner/CRO click, I read the evidence)
1. Squarespace plan page shows Code Injection available. Screenshot.
2. Native integrations: does Squarespace offer a built-in Meta Pixel / Google Ads conversion field on this plan?
   [VERIFY on Settings > Marketing / Advanced]. Prefer native over pasted code.
3. One real test order + refund (owner, monthly CRO task). Check in Meta Events Manager "Test events" that
   `Purchase` fired once with value and EUR currency. Check Google Ads conversion action status.
4. GA4 DebugView shows `purchase` once (no duplicate).
5. Record in `ads-results-log.csv` note: date, which tags verified. Until all pass, any test is traffic objective,
   read through UTMs and Squarespace Orders.

I do not add, edit or remove any tag. Pixel/tag changes are owner-approved CRO work.

## Change log
- 2026-10-21: tracker created. 1 PASS, 2 FAIL, 2 MISSING, 1 UNVERIFIED.
