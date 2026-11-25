# GEO roadmap: get Autumn & Wool named by AI assistants

Sprint: 2026-11-25 19:24–19:54 EET. Manager: main session. Workers: subagents (Sonnet/Haiku).
Plan page: https://claude.ai/artifact/R4PZ14BcBuVGGMHnWQKJ7N · Context: `geo-2026-11-25/CONTEXT.md`
Status: `todo` · `running` · `review` · `done` · `blocked (owner)`. Only the manager edits this file.

| ID | Step | Task | Worker | Output | Status |
|---|---|---|---|---|---|
| GEO-01 | 1 Index | Bing Webmaster Tools (import from GSC) + GSC request-indexing guide for owner | Haiku | `geo-2026-11-25/01-bing-gsc-indexing-guide.md` | done (draft) |
| GEO-02 | 1 Index | ChatGPT / Perplexity / Google merchant-feed programmes: eligibility + steps | Sonnet | `geo-2026-11-25/02-ai-shopping-feeds.md` | done (draft) |
| GEO-03 | 2 Entity | Brand consistency pack: Etsy Mareshop announcement/About, social bios, Business Info name, `sameAs` list | Sonnet | `geo-2026-11-25/03-brand-entity-pack.md` | done (draft) |
| GEO-04 | 2 Entity | Marketplaces + Baltic press/gift guides shortlist with pitch drafts | Sonnet | `geo-2026-11-25/04-marketplaces-press.md` | done (draft) |
| GEO-05 | 2 Entity | 60-second YouTube script + title/description; Reddit answer guidelines | Haiku | `geo-2026-11-25/05-youtube-reddit.md` | done (draft) |
| GEO-06 | 3 Citable | Home + About answer-first copy, `/shop` H1 + intro block with text links | Sonnet | `geo-2026-11-25/06-home-about-shop-copy.md` | done (draft) |
| GEO-07 | 3 Citable | Product facts first-line sheet (22 products), fibre-% gaps, "hand-knitted" wording fixes | Sonnet | `geo-2026-11-25/07-product-facts.md` | done (draft) |
| GEO-08 | 3 Citable | Guide refresh drafts: byline/date, answer-first, merino vs lambswool table, product links | Sonnet | `geo-2026-11-25/08-guide-refresh.md` | done (draft) |
| GEO-09 | 4 Measure | Prompt-panel tracker + baseline via web search | Haiku | `geo-2026-11-25/09-prompt-panel.md` | done (draft) |
| GEO-10 | 2 Entity | Latvian-language press, gift guides, Riga concept stores (gap found in GEO-04) | Haiku | `geo-2026-11-25/10-latvian-press.md` | done (draft) |
| GEO-11 | All | One deduplicated owner checklist from all task files | Haiku | `geo-2026-11-25/00-OWNER-ACTIONS.md` | done (draft) |

## Log
- 19:24 Roadmap created; 9 tasks queued.
- 19:25 All 9 workers launched in parallel (Sonnet ×6, Haiku ×3).
- 19:27 GEO-09 reviewed: baseline 0/8 prompts surface autumnandwool.com; Mareshop in 2/8 (web-search proxy). Done.
- 19:27 GEO-06 reviewed: no invented numbers; Etsy figures left as [FILL]; uses machine-knitted wording. Done. Worker had no shell, so "before" text partly from 11 Nov copies; verbatim live text saved to `geo-2026-11-25/live-text-2026-11-25.md`.
- 19:27 GEO-08 reviewed: banned words absent from copy (only in URL slugs, left alone). Woolmark claims marked [VERIFY]. Done.
- 19:27 GEO-03 reviewed: Etsy policy bars pointing buyers off Etsy, so version A (no URL) recommended. Live sameAs checked by manager (see below). Done.
- 19:27 GEO-01 reviewed: GSC import + sitemap + 11 request-indexing URLs + 1-week check (2 Dec). Bing help pages 404 → some menu names from guides. Done.
- 19:27 GEO-02 reviewed: Google free listings = only confirmed route (unblock 98 queued items first). ChatGPT Business Hub feed possible, eligibility unconfirmed; TSV needs seller_name, target_countries, store_country, group_id. Perplexity/Copilot parked. Done.
- 19:27 GEO-04 reviewed: apply first to Not Just A Label (30% commission) and Wolf & Badger (owner checks fee). Skip ethics-proof marketplaces for now. No Latvian-language search done, so GEO-10 added and launched. Done.
- 19:27 GEO-05 reviewed: 60s script + YouTube metadata + Reddit rules (sub rules from mirrors, unverified). Done. Manager synced repo `llms.txt` to the live file (repo copy was stale: said "by hand or on a machine"; live already says manual knitting machine).
- 19:28 GEO-07 reviewed: the 10 Nov edits are live, and visible product text has no "hand-knitted". Manager scanned titles, meta, alt text and JSON-LD on all 22 pages: the only hits are 3 offer.url slugs, which stay as they are. Fibre % is missing on 4 products and colours on 7 (owner). Done.
- 19:28 GEO-10 reviewed: 8 Riga targets (M50, RIIJA, JO, Gift Shop Riga, LSM, Svinam, Latvian Design Award…), plus a pitch in Latvian. Done.
- 19:28 GEO-11 launched to merge the owner actions.
- 19:30 GEO-11 reviewed: 45-item owner checklist (A this week 12, B facts 13, C approve 8, D decide 12). Sprint complete: 11/11 done as drafts, nothing live. Next: owner works through `00-OWNER-ACTIONS.md` section A; re-run prompt panel 2026-12-01.

## Implementation phase (owner said implement, no drafts), 19:39
- Committed and pushed sprint drafts (5ec3dbe).
- GSC: all 9 GEO pages already "URL is on Google". No request needed.
- Bing WMT: site already verified; resubmitted sitemap.xml; submitted 39 URLs (Success). AI Performance baseline: 36 Copilot citations in 3 months. Log: `geo-2026-11-25/live/2026-11-25-live-log.md`.
- Squarespace copy (Home, About, /shop): final text with no placeholders in `geo-2026-11-25/live/apply-copy-final.md`. BLOCKED: admin logged out; owner must finish the Google sign-in pop-up in Chrome.
- 19:47 LIVE: About page Q&A section (4 questions: origin, Mareshop link, machine-knitted, fibres) published and verified on the public page; Google indexing requested for /about. /shop H1 section discarded unsaved (block resize failed); open item for a manual resize.
- 19:53 LIVE: /shop H1 + intro + 5 crawlable /wool-* links (Custom CSS widens the Fluid Engine block). Verified at 390px and 1440px.
- 19:57 SEO round: guides already answer-first and bylined (10 Nov), no change. /shop + /about resubmitted to Bing.
