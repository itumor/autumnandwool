Decision needed 20 Nov (#33): December paid test GO or NO-GO (default NO-GO, EUR 0). Pre-drafted 2026-10-21; filled 20 Nov.

# December test go/no-go + run sheet   Status: DRAFT (prep for GRO-18, GRO-19)

aw-growth-marketing. Brief: `test-2026-10-21-dec-first-signal.md`. Gates: `paid-test-gates.md`.
Rule: GO only if all 6 gates PASS **and** the owner names a ceiling. Any FAIL/MISSING = NO-GO (ruling C10).

## Part 1. Go/no-go (fill on 20 Nov)
| # | Check | Evidence to link | State 20 Nov |
|---|---|---|---|
| 1 | Chosen SKU costed: BE_CAC in `be-cac-worksheet-priority-skus.md` | `unit_economics.py` output | TODO |
| 2 | Chosen SKU GREEN in the latest owner-approved capacity file; max units | `capacity-2026-W47.md` | TODO |
| 3 | PDP ready: CRO landing brief PASS | `landing-brief-2026-10-21-dec-first-signal.md` | TODO |
| 4 | Orders countable (Squarespace Orders) | weekly export | PASS (manual) since 21 Oct |
| 5 | Conversion signal: plan upgraded + checklist passed, or accept a traffic objective | `paid-test-gates.md` checklist | TODO |
| 6 | Owner ceiling EUR ___ and FIN cash above buffer (G3) | owner note, FIN forecast | TODO |
| x | G8 claims evidence (concept A), photo rights (#16), Etsy proof line (#17) | owner evidence list | TODO |
| x | OPS order-by dates carrier-backed (G5) | `../operations/christmas-cutoffs-2026.md` v2 | TODO |

Numbers once 1, 2 and 6 are known:
| Line | Formula | Value |
|---|---|---|
| Concepts live | 2 (B, C) or 3 if G8 clears A | TODO |
| Test total | concepts x 3 x BE_CAC | TODO |
| Ceiling | lower of owner ceiling and test total | TODO |
| Daily | ceiling / working days in window (launch to last order-by) | TODO |
| Max orders the SKU may take | PRD "Max units to promote" | TODO |

Decision: [ ] NO-GO, EUR 0   [ ] GO, EUR ___, SKU ___, launch ___   Owner initials + date: ___

## Part 1b. Pre-filled on assumptions (2026-10-21, wave 3, GRO-18 ASSUMED)
ASSUMPTION: A-GM-08 December paid = NO-GO, EUR 0; A-GM-05 Basic plan; P2 BE_CAC 24.82 (A-GRO-01/02); register:
`business-os/growth/assumptions-wave3.md` and `business-os/head-of-ecommerce/assumptions-wave3.md`. Not an owner decision.

| # | Check | State on assumption |
|---|---|---|
| 1 | Costed | ASSUMED: P2 BE_CAC 24.82 EE/LT (not confirmed) |
| 2 | GREEN + max units | ASSUMED: P2 max 6 from stock (DRAFT capacity W43) |
| 3 | PDP / CRO PASS | MISSING |
| 4 | Orders countable | PASS |
| 5 | Conversion signal | FAIL (Basic plan); traffic objective only |
| 6 | Owner ceiling + cash > buffer | MISSING (no ceiling assumed; A-GM-09 buffer EUR 460 planning case, balance unknown) |

| Line | Value (ASSUMPTION) |
|---|---|
| Concepts live | 2 |
| Test total | 2 x 3 x 24.82 = EUR 148.92 |
| Ceiling | lower of owner ceiling (none) and 148.92 = **EUR 0** |
| Daily | n/a at EUR 0 (would be about EUR 8.76 over 17 working days, 23 Nov-15 Dec) |
| Max orders | 6 (P2 stock) |

**Assumed decision: NO-GO, EUR 0.** Reasons: gates 3, 5, 6 not passing; expected CAC about EUR 40 vs BE_CAC 24.82 on
illustrative CPC/CVR (A-GRO-05/06, L). The owner can still choose GO on 20 Nov; then Part 1 is re-filled with real values.

## Part 2. Run sheet (only if GO; owner clicks, agent never touches the ad account)
| Day | Who | Action |
|---|---|---|
| Launch -1 | Growth | Final UTM URLs in `utm-links.csv` (concept rows), check that each URL loads and the query string survives |
| Launch -1 | Owner | Builds 1 campaign, 1 ABO ad set, objective per check 5, countries in window only, budget = Daily |
| Launch | Owner | Publish; screenshot settings into `business-os/growth/exports/` |
| Days 1-5 | All | No edits (learning). Exception: a kill line is hit, a policy rejection, or the SKU sells out |
| Daily | Owner | Spend per concept + Squarespace orders on the SKU (2 numbers) |
| Daily | Growth | Kill-line check: spend >= 2 x BE_CAC with 0 orders -> stop concept; spend >= 3 x BE_CAC with CAC > BE_CAC -> stop |
| Any day | Growth | Stop all if units sold reach PRD max units, or capacity turns AMBER/RED |
| Last order-by date | Owner | Stop all (no gift promise after the cutoff) |
| Monday | Growth | Readout + `ads-results-log.csv` rows; "Meta claims N, we verify M" |
| End + 7 days | Growth | Close-out readout -> input to `budget-proposal-2027-01.md` |

No scaling in December (needs >= 3 orders with contribution after CAC > 0).
