# AI Team — hiring plan as Claude Code agents

Each role in `hiring-plan.md` is a project subagent in `../.claude/agents/`, preloaded with skills from
`../.claude/skills/` (frontmatter `skills:` list). Project-local only. Built 21 Oct 2026.

All agents produce **drafts in `business-os/`** for the owner to approve. Hard rules in every agent: no live store /
Etsy / Merchant Center edits (product data frozen), no spending, no sending or publishing, no refunds, no invented
costs, stock, reviews, fibre content or claims (unknowns marked TODO / `[VERIFY]` / `CLAIM-CHECK`).

## Roster

| Agent | Role | Skills | Output folder |
|---|---|---|---|
| `aw-head-of-ecommerce` | GM: weekly review, scale/stop calls, hiring | weekly-business-review, unit-economics, hiring-scorecards, cash-flow | `reviews/`, `hiring/` |
| `aw-finance` | Accountant support, cash, SKU profit | cash-flow, unit-economics, weekly-business-review | `reviews/` |
| `aw-growth-marketing` | Paid tests, CAC, competitors | paid-ads-testing, competitor-research, utm-attribution | `growth/` |
| `aw-partnerships` | Creators, gifting, affiliate codes | creator-outreach, utm-attribution | `partnerships/` |
| `aw-creative-content` | Video scripts, shot lists, calendar | **brand-voice** (shared), short-video-scripts, product-photo-briefs, content-calendar | `campaign-assets/drafts/` |
| `aw-ecommerce-cro` | PDPs, checkout, funnel audits | **cro-audit** (shared), product-page-copy, merchant-feed-qa, ecommerce-seo, brand-voice, unit-economics | `business-os/` |
| `aw-seo-marketplace` | SEO, Pinterest, Etsy, feed | ecommerce-seo, etsy-listing, merchant-feed-qa, cro-audit, product-page-copy, brand-voice, unit-economics | `business-os/` |
| `aw-production` | Costing, capacity, QC, labels | **production-capacity** (shared), qc-and-labelling, unit-economics, brand-voice | `capacity-YYYY-Www.md` |
| `aw-operations` | Fulfilment SOP, returns log | fulfilment-sop, returns-handling, production-capacity, qc-and-labelling, unit-economics, brand-voice | `business-os/` |
| `aw-customer-experience` | Reply drafts, email flows | support-replies, email-lifecycle, returns-handling, brand-voice, production-capacity | `business-os/` |

Tools: all have Read/Grep/Glob/Write/Edit/WebSearch/WebFetch. Only GM + Finance have Bash (to run
`unit_economics.py`; told never to run `init`).

Hand-offs: Production's weekly `capacity-YYYY-Www.md` (GREEN = paid ok, AMBER = organic only) gates Growth,
Partnerships and Creative. Every customer-facing word goes through `aw-brand-voice`.

## Use

Restart Claude Code in `/Users/eramadan/autumnandwool` (agents load at session start), then e.g.:

- "Use aw-head-of-ecommerce to run this week's business review."
- "Use aw-ecommerce-cro to audit the 5 priority product pages."
- "Use aw-production to draft this week's capacity and safe-to-promote list."

## Skill sources (picked by research agents, 2–4 candidates compared per skill)

| Source | License | Used for |
|---|---|---|
| anthropics/knowledge-work-plugins (finance, small-business, HR, customer-support) | Apache-2.0, adapted with attribution | weekly review, cash flow, hiring, support replies |
| coreyhaines31/marketingskills | MIT, adapted with attribution | ads, attribution, competitors, creators, CRO, copy, SEO, email, social |
| rampstackco skills | MIT, ideas only | brand voice, photo-brief structure |
| thatrebeccarae/claude-marketing | MIT | UTM naming, ad-library research |
| nexscope (Etsy scoring) | MIT badge, no per-file line → ideas only | Etsy listing score |
| lyndonkl/claude, Chaser, QA blogs | no license → own words | unit-economics rules, fulfilment SOP, QC |
| Google Merchant Center, Etsy Handbook, TikTok, Pinterest Help, europa.eu, PTAC, Reg. (EU) 1007/2011 | official docs, paraphrased | feed, Etsy, video, Pinterest, labels, returns, influencer disclosure |

Every SKILL.md has a "Sources" section with URLs and what was taken. No scripts were downloaded or run.

## Owner decisions / data the agents need (found during build)

1. **Costs** for the 22 visible SKUs in `sku-economics.csv`. Until then all paid-ad briefs are BLOCKED.
2. **Stock truth**: turtleneck 360 / beanie 220 in export look like made-to-order placeholders. Confirm physical stock.
3. **Feed bug**: `build_google_feed.py` hard-codes `availability=in_stock` on all rows; 13 items are out of stock.
4. **Claims**: "handmade", "sustainable", "made in Riga" need owner evidence; agents use "knitted on manual machines
   and finished by hand in Riga" and avoid "sustainable/organic/certified".
5. **Reply-time conflict**: Contact page says 24 h, welcome email says 1–2 business days. Pick one.
6. **Returns policy** clauses (5-day defects, no sale/made-to-order returns, shipping not refunded) → EU adviser.
7. **Tracking gap**: Meta Pixel / Google Ads purchase tags likely impossible without Code Injection (plan upgrade).
8. **Missing ops data** (TODO in skills): minutes per garment, yarn per lot, supplier lead times, labour rate, carriers,
   return address, HS codes, size table, review platform.
9. **MailerLite Free**: 3 automations × 5 steps, no e-commerce triggers → buyers added to a group by hand.
