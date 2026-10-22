# Squarespace plan upgrade memo (decision 24, due 4 Nov): PREPARED DRAFT, not final

Author: GM (agent), 2026-10-21. Task GM-13. **Status: BLOCKED on owner.** The current plan name and billing term
are unknown. The memo is pre-written for both cases and is finished the day the owner's Billing and Discounts
screenshots arrive (unblock pack row 17, due 28 Oct). No purchase, no store change.

**One line (provisional):** on Basic with zero orders, the upgrade only pays for itself as measurement. Buy it the
week a paid test is approved, not before.

## Facts available now
| Fact | Value | Source |
|---|---|---|
| Plan prices (EUR/mo, annual / monthly billing) | Basic 11.00 / 15.00, Core 17.00 / 24.00, Advanced 29.00 / 42.00 | `finance/spend-checks-q4-2026.md` s1, public page read 2026-10-21; VAT inclusion `[VERIFY]` |
| Store transaction fee | Basic 2%, Core and Advanced 0% | same |
| Extra cost Basic -> Core | EUR 6.00/mo annual, EUR 9.00/mo monthly | FIN computed |
| Break-even store sales (fee saving = extra cost) | EUR 300.00/mo annual, EUR 450.00/mo monthly | FIN: 6.00 / 0.02, 9.00 / 0.02 |
| Real orders to date | 0 (test #00003/#00004 refunded, excluded) | handbook, FIN |
| Code Injection (GA4 purchase events, Meta Pixel, Clarity) | Not on Basic | README s8, Growth gate 5 |
| Discount codes / per-code reports on current plan | Unknown | decision 11 screenshot |
| Current plan, billing term, renewal date | **TODO owner** | Settings > Billing screenshot |

## Decision by case (owner picks after the screenshot)
| Case | GM recommendation | Why | KPI effect | Cost | Reversible |
|---|---|---|---|---|---|
| A. Current plan is Basic, no paid test approved for Dec (decision 33 = EUR 0) | Stay on Basic now. Re-decide when a paid test is approved or monthly store sales near EUR 300 | Below EUR 300/mo sales the upgrade is a net cost; with no paid traffic, purchase events add little that the Squarespace Orders export does not already show | None now | EUR 0 | Yes |
| B. Basic, and the owner intends a paid test (Dec or Q1) | Upgrade before the test starts, then Growth/CRO run the conversion-signal checklist (`growth/paid-test-gates.md`) | A paid test without a purchase signal cannot be read (Growth gate 5). FIN: EUR 72/yr difference (annual) is less than a single suggested EUR 200-300 test | Gate 5 can pass; CAC readable per channel | EUR 6.00/mo annual or 9.00/mo monthly, plus any mid-term switching terms `[VERIFY on billing page]` | Downgrade terms `[VERIFY]` |
| C. Basic, discount codes unavailable on Basic | Same as A or B; creators run on UTM + manual check (ruling C6), not codes, in Q4 | Codes alone do not justify the upgrade at zero sales | Attribution weaker but workable | EUR 0 | Yes |
| D. Current plan is already Core or Advanced | No purchase decision. Growth/CRO run the conversion-signal checklist now | Code Injection already available | Gate 5 testable this week | EUR 0 | n/a |

## To finish (GM, on receipt of screenshots)
1. Pick the case, put the plan name, term and renewal date in the facts table.
2. Check the pricing page again the same day (prices change) and whether the price shown includes VAT.
3. Add Growth's gate status and decision 33 intent; final recommendation in one line; hand to the owner on 4 Nov.

DRAFT for owner. Not a purchase. Not sent.
