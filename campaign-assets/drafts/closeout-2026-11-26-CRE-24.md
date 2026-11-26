# CRE-24 — closeout check 2026-11-26

## Task
Re-baseline content KPI targets after 4 weeks of data (C9); owner approves targets — due 23 Nov (status: TODO).

## What the deliverable requires
- 4 weeks of posted content (W44-W47) with UTM-tagged sessions to compute median UTM sessions per post.
- GA4 export (`G-7TV8PK060Z`) filtered by `utm_campaign` / `utm_content` for median visits, product-page sessions, saves/shares.
- Squarespace Orders export for orders attributed to content UTM sessions (GA4 has no purchase events).
- Photo backlog count (colours photographed and bound of 24).
- Owner approval of proposed targets (GM-17 alignment).
- Output file `business-os/content-review-2026-MM.md` (or `business-os/content-kpi-rebaseline-2026-11.md`) finalised from the prep template.

## Repo evidence found
- Prepared draft exists: `campaign-assets/drafts/plan-wave2/content-measurement-prep-2026-10-21.md` Part 2 (KPI re-baseline table template, method rows).
- No GA4 export CSV in repo (grep for `ga4*.csv` / `utm*.csv` returned nothing).
- No Squarespace Orders export in repo (accountant packs for Oct/Nov both mark row 1 "MISSING").
- No photo-backlog tick list beyond the plan's 0 of 24 at 21 Oct assumption; no evidence of shipped flat lays (no product image files in `campaign-assets/`).
- `business-os/growth/owner-inputs-wave2.md` row 1 still lists the Monday data batch as owner-supplied; nothing landed.

## Verdict
HELD — owner/live data not in repo

## Missing inputs
- Owner GA4 traffic-acquisition export (sessions by `utm_campaign`/`utm_content`) for W44-W47.
- Owner Squarespace Orders export for the same 4 weeks, excluding test orders #00003/#00004.
- Confirmed count of colours photographed and bound (photo backlog tick list).
- Owner approval of the proposed targets (GM-17).

## Next action
Owner runs the Monday data batch and pastes the GA4 + Squarespace Orders exports into the prep template; agent then fills the Part 2 table and routes targets for approval.