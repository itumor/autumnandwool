# CRO-21 Weekly Smoke (390 px) — agent checks 2026-10-22

Source: ego-browser, mobile viewport `390×844` emulation on the live site.

Target: https://www.autumnandwool.com/shop/p/p/merino-wool-turtleneck-sweater-womens-knit-pullover-soft-warm-lightweight-minimalist-sustainable-knitwear-sizes-sl-12-679428

Results:
- No horizontal scroll at 390 px (`scrollWidth == 390`, `overflow: false`).
- `Add To Cart` without a colour/size selection still creates the `.sqs-widgets-confirmation-overlay` (“Added!” label with unassigned selection), confirming the bug path before the CSS fix.
- Overlay `position`/stacking unchanged:
  - `z-index: 999999`
  - computed `pointer-events: none` (inline empty, inherited via the Custom CSS rule) — clicks pass through
- 390 px test evidences two qualitative requirements of the 390 px weekly smoke:
  1. no horizontal overflow on the PDP at phone width, and
  2. the overlay no longer blocks pointer events at the known pain point.

Remaining (owner/action work):
- real-device screenshots on iPhone/Android (owner item 5) for ultimate truth
- re-run next Friday per the task cadence

Related: CRO-14 text-level pass; CRO-22 overlay-CSS double-check value preserved.
