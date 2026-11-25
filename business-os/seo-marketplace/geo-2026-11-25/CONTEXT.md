# GEO sprint context (2026-11-25) — read before working

Goal: get Autumn & Wool (autumnandwool.com, Squarespace 7.1, Riga knitwear studio, maker Kristine, formerly Mareshop on Etsy) named and cited by ChatGPT, Gemini, Claude, Perplexity, Copilot.

## Findings (live checks 2026-11-25)
- AI search crawlers allowed (robots.txt `*` group). Text server-rendered. `/llms.txt` live and clean. On-site AI readiness ~63/100 (audits 2026-11-10/11).
- Web search for "Autumn & Wool" Riga knitwear: zero brand results. Search for autumnandwool.com: zero pages from the domain.
- Query "best handmade merino cardigan Latvia/Baltic": AI answer names Mareshop on Etsy (https://www.etsy.com/shop/mareshop, since 2011) first; also cites Project Cece, Wolf & Badger, Pinkoi, Gather & See. No link from Mareshop to new site.
- `/shop` raw HTML: 0 product links (JS grid), no H1. `/wool-sweaters` 13 product links, `/wool-gifts` 7, `/wool-cardigans` 4. Sitemap 49 URLs.
- Home ~343 words, About ~364 words (only ~170 words of real copy each). Product JSON-LD: no material/colour/SKU/GTIN/rating.
- Wording clash: 12 product URLs say "hand-knitted"; pages say machine-knitted, hand-finished. Some products say only "wool", no fibre %.
- Business Information name = "AUTUMN AND WOOL, SIA" (legal); brand should read "Autumn & Wool".

## Rules (hard)
- DRAFTS ONLY. Never edit the live site, Etsy, Merchant Center, social accounts, or send anything. No JavaScript / code injection proposals (Squarespace plan gate).
- Never invent owner numbers (stock, costs, fibre %, sales, ratings, dates). Use `[FILL: what]` placeholders. Only quote facts found in this repo or on the live site, and cite where.
- No fake reviews, no mention-farming, no undisclosed self-promotion.
- Read first: `AGENTS.md`, `PROJECT-HANDBOOK.md`, `llms.txt` (repo root), `business-os/seo-marketplace/2026-11-10-seo-reaudit.md`. Brand voice: `.claude/skills/aw-brand-voice/SKILL.md`.
- Write only your own output file(s) under `business-os/seo-marketplace/geo-2026-11-25/`. Do NOT edit `ROADMAP.md` (manager owns it).
- Plain English, short sentences, paste-ready. End your file with a `## Owner actions` list and a `## Sources` list.
- Final reply to manager: ≤8 lines: file path(s), what's done, what needs owner, anything you could not verify.
