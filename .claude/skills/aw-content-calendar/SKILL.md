---
name: aw-content-calendar
description: Use when planning the Autumn & Wool weekly or monthly social content calendar (Instagram, TikTok, Pinterest, email tie-ins), choosing content pillars, batching a week of posts, or reviewing which content drove visits and orders.
---

# Autumn & Wool content calendar

Purpose: a realistic weekly plan that one creative lead plus Kristine can film in one session, tied to products
that can actually ship, measured by UTM visits and orders (README s4, s9).

Read first: `.claude/skills/aw-brand-voice/SKILL.md`, then `aw-short-video-scripts` and `aw-product-photo-briefs`
for the individual pieces.

## Pillars (share of weekly posts)

| Pillar | Share | Examples |
|---|---|---|
| Making in Riga | 30% | Machine knitting, hand-sewing seams, yarn arriving, parcel packing |
| Product truth (fit, texture, colour) | 30% | Try-ons with size on screen, rib close-ups, every colour of the beanie |
| Styling / everyday wear | 20% | One piece three ways, layering a vest, office to weekend |
| Kristine and the Mareshop story | 10% | 15 years on Etsy, why Autumn & Wool, studio life |
| Offer / gift / seasonal | 10% | Gift set, Riga Christmas markets (`markets-and-gift-guides.md`), restocks |

Promotional content stays near 10%. Every post still links to a product or the shop with a UTM.

## Inputs (gather before planning)

1. Production's weekly safe-to-promote list and capacity (README s6). No list = plan only pillars 1 and 4.
2. Live prices, colours, stock for chosen SKUs (read-only check).
3. Last week's results: UTM visits per post (GA4), orders (Squarespace Orders), saves/shares.
4. Season and dates: Christmas markets, gift-guide deadlines, shipping cut-offs [VERIFY with Operations].
5. Photo backlog status (variant photos).

## Weekly cadence (default, review monthly)

| Day | Instagram | TikTok | Pinterest | Other |
|---|---|---|---|---|
| Mon | — | — | 2 pins (product flat lays) | Plan + scripts to owner for approval |
| Tue | Reel: making-of | Same, TikTok text | — | Stories: behind the scenes |
| Wed | Carousel: colours / fit | — | 2 pins | — |
| Thu | Reel: texture or fit | Same | — | Stories: Q&A sticker |
| Fri | — | Styling video | 2 pins | — |
| Sat | Reel: styling or founder | Same | — | Optional email tie-in |
| Sun | Off | Off | — | — |

3-5 videos a week total (hiring-plan target). Batch: one filming session, one editing session.

## Output template (`business-os/content-calendar-YYYY-Www.md`)

```
# Content calendar — week [YYYY-Www] — DRAFT for owner approval
Safe-to-promote SKUs: [list + source/date]   Capacity note: [...]
Last week: [post] -> [UTM visits] -> [orders] ; keep / change / drop
| Day | Channel | Pillar | Format | Product + colour | Hook / title | Asset (script/photo id) | UTM content | Status |
|-----|---------|--------|--------|------------------|--------------|-------------------------|-------------|--------|
| Tue | IG+TT   | Making | Reel   | Merino Raglan Cardigan, Black | ... | vs-2026-10-28-a | making-cardigan | draft |
Filming list (one session): [shots across all scripts]
Owner decisions needed: [...]
Claim check: all pieces passed aw-brand-voice s6 [yes/no + VERIFY list]
```

UTM pattern: `utm_source=[instagram|tiktok|pinterest|facebook]&utm_medium=social&utm_campaign=[campaign]&utm_content=[post-id]`
(bio links: `owner-action-pack-2026-10-19.md` C).

## Scoring ideas (when more ideas than slots)

Score 1-10, weighted: customer/sales impact 40% (safe-to-promote, margin, photo-ready) · brand fit 30% · reuse
across channels 20% · effort 10% (inverse). Keep the top items; park the rest in the backlog.

## Monthly review

- Table per format and pillar: posts, UTM visits, orders, revenue. Drop formats with zero visits after 4 posts.
- Never judge by views or followers alone (hiring-plan interview rule).
- Note which SKU x creative pairs to hand to Growth for paid tests.

## Guardrails

- Plans and drafts only. Never post, schedule, or connect a scheduler. Buffer/native scheduling is done by the
  owner after approval.
- Do not promote SKUs off the safe-to-promote list or with missing variant photos for the colour shown.
- Social account ownership: Instagram `@autumnandwool` confirmed; Facebook/Pinterest still Mareshop, confirm with
  owner before planning posts there.

## Sources

- coreyhaines31/marketingskills `social` (MIT), https://github.com/coreyhaines31/marketingskills
  : adapted pillar mix idea, weekly batching, repurposing one asset across platforms, "drafts first, never
  auto-publish".
- coreyhaines31/marketingskills `content-strategy` (MIT), same repo
  : adapted weighted idea scoring (impact/fit/potential/effort) and 60/30/10 style split.
- rampstackco/claude-skills `content-strategy` (MIT), https://github.com/rampstackco/claude-skills
  : compared; blog/SEO-oriented, less fit for a social calendar. Not used beyond confirming structure.
- Business inputs: `business-os/README.md` s4, s6, s9; `business-os/hiring-plan.md`; `GROWTH-PLAN-100-IDEAS.md`.
