# December paid test go/no-go memo (decision 33, due 20 Nov): PREPARED DRAFT, finish 20 Nov

Author: GM (agent), 2026-10-21. Task GM-18. Default answer is **no-go, EUR 0** (ruling C10). The memo turns
into "go" only if all 6 Growth gates pass by 20 Nov with evidence. No spend, no account change.

## Gate status (copy of `growth/paid-test-gates.md`, 21 Oct; GM re-reads it on 20 Nov)
| # | Gate | 21 Oct | Needs (owner rows in `owner-unblock-pack.md`) | 20 Nov |
|---|---|---|---|---|
| 1 | SKU costed (`contrib` in `unit_economics.py`) | FAIL (0 of 82) | rows 5, 9, 12, 32, 40 | TODO |
| 2 | SKU GREEN in capacity file | MISSING (no file; PRD writes blocked by `prod-guard`) | rows 2, 8, 32 | TODO |
| 3 | PDP ready (photo per colour, size, delivery time, price) | FAIL | rows 21, 41, 42, 27 | TODO |
| 4 | Orders countable | PASS (manual, Squarespace Orders) | row 10 weekly | TODO |
| 5 | Platform conversion signal | UNVERIFIED (Code Injection plan-gated) | rows 17, 35; see `plan-upgrade-memo-prep-2026-10-21.md` | TODO |
| 6 | Owner monthly ceiling | MISSING | rows 13, 33, then this memo | TODO |
Extra launch checks: G8 claims (row 26), G5 carrier-backed cutoffs (OPS, 14 Nov), photo rights (row 26).

## Decision rule (from master plan s3 and ruling C10)
- Any gate not PASS on 20 Nov -> **no-go, EUR 0**. Free channels continue (Google free listings, Pinterest, creators).
- All 6 PASS -> owner may approve a capped test: per concept cap = 3 x BE_CAC of the SKU it promotes; total
  ceiling = owner's number after FIN cash check (G3). Only GREEN SKUs. Stop at Growth's kill lines.
- Test window: from approval to the earliest regional gift cutoff (about 3 Dec EU per ruling C3, unverified until
  OPS publishes carrier-backed dates on 14-20 Nov). After the cutoff, only in-stock SKUs with confirmed dispatch.

## Memo shape for 20 Nov (fill-in)
| Field | Value |
|---|---|
| Gates passed | __ of 6 |
| Recommendation | go / no-go |
| SKUs (GREEN only) and BE_CAC each | __ |
| Ceiling proposed (EUR, total) | __ (EUR 0 valid) |
| Per-concept cap (3 x BE_CAC) | __ |
| Window | __ to __ |
| Lowest cash balance with the ceiling spent (FIN) | __ |
| Kill lines (Growth brief) | __ |
| Reversible | yes, stop any day |

Status 21 Oct: 1 of 6 gates PASS, so the memo would say no-go today. Not a forecast of 20 Nov.

DRAFT for owner. Not sent. No spend.
