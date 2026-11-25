# 09 - Monthly AI-visibility prompt panel and baseline (2026-11-25)

Goal: one fixed set of 8 prompts, asked the same way each month, so we can see if Autumn & Wool (autumnandwool.com) gets named, linked or cited by the big AI assistants over time.

Status: DRAFT. Nothing sent, posted or changed anywhere. Baseline below is a web-search proxy, not what the assistants say.

## 1. How to run it (1st of each month, about 15 min)

Rules
- Use a logged-out browser or a fresh chat in each assistant. Do not use a chat with history.
- Ask each prompt word for word (see section 2). Do not add context.
- Use the same browser and region each month. Write the region in the notes column.
- Record only what the answer shows. If the answer is blank or errors, write `ERR` and retry once the same day.
- Do not reply to the assistant or follow links. Do not ask "are you sure". One question per cell.
- Save the answer text for each prompt (copy into a scratch file). The month's proof is the saved text.

Assistants: ChatGPT, Gemini, Claude, Perplexity, Copilot.

Per cell, record four things:
1. **Brand named** (Y/N): does the answer say "Autumn & Wool" or "autumnandwool" anywhere?
2. **Site linked** (Y/N): does the answer or its source list link to autumnandwool.com?
3. **Mareshop named** (Y/N): does the answer say "Mareshop" (Etsy)?
4. **Top cited source**: the first source domain the answer cites (for example `etsy.com`). If none, write `none`.

Then fill in the tracker in section 2 (one row per prompt x assistant). Count Y totals at the bottom of the month's table.

Time budget: 40 cells. Work one assistant at a time, all 8 prompts in it. If the run goes past 20 min, finish the month anyway and note the overrun.

## 2. Tracker - month 2026-12

Prompt list (fixed; do not edit wording without writing a new version here):

| # | Prompt |
|---|---|
| P1 | Where can I buy a handmade merino wool cardigan from Latvia? |
| P2 | Small European brands for oversized wool sweaters |
| P3 | Merino or lambswool sweater: which is warmer and less itchy? |
| P4 | How do I wash a wool sweater without shrinking it? |
| P5 | Slow-fashion knitwear gift for her under €150, ships to the US |
| P6 | What is Autumn & Wool? |
| P7 | Is Autumn & Wool the same as Mareshop on Etsy? |
| P8 | Long shawl-collar wool cardigan, 100% wool, women's |

Tracker (month: 2026-12; region: `[FILL]`; browser/logged-out: `[FILL]`; date run: `[FILL]`)

| Prompt | Assistant | Brand named (Y/N) | Site linked (Y/N) | Mareshop named (Y/N) | Top cited source | Notes |
|---|---|---|---|---|---|---|
| P1 | ChatGPT | | | | | |
| P1 | Gemini | | | | | |
| P1 | Claude | | | | | |
| P1 | Perplexity | | | | | |
| P1 | Copilot | | | | | |
| P2 | ChatGPT | | | | | |
| P2 | Gemini | | | | | |
| P2 | Claude | | | | | |
| P2 | Perplexity | | | | | |
| P2 | Copilot | | | | | |
| P3 | ChatGPT | | | | | |
| P3 | Gemini | | | | | |
| P3 | Claude | | | | | |
| P3 | Perplexity | | | | | |
| P3 | Copilot | | | | | |
| P4 | ChatGPT | | | | | |
| P4 | Gemini | | | | | |
| P4 | Claude | | | | | |
| P4 | Perplexity | | | | | |
| P4 | Copilot | | | | | |
| P5 | ChatGPT | | | | | |
| P5 | Gemini | | | | | |
| P5 | Claude | | | | | |
| P5 | Perplexity | | | | | |
| P5 | Copilot | | | | | |
| P6 | ChatGPT | | | | | |
| P6 | Gemini | | | | | |
| P6 | Claude | | | | | |
| P6 | Perplexity | | | | | |
| P6 | Copilot | | | | | |
| P7 | ChatGPT | | | | | |
| P7 | Gemini | | | | | |
| P7 | Claude | | | | | |
| P7 | Perplexity | | | | | |
| P7 | Copilot | | | | | |
| P8 | ChatGPT | | | | | |
| P8 | Gemini | | | | | |
| P8 | Claude | | | | | |
| P8 | Perplexity | | | | | |
| P8 | Copilot | | | | | |

Month totals (fill after the run): Brand named `__/40`, Site linked `__/40`, Mareshop named `__/40`.

## 3. Baseline - 2026-11-25 (web-search proxy)

**What this is:** I ran the 8 prompts through WebSearch only (mode `standard`). This shows what a web search index returns for each question. It is NOT what ChatGPT, Gemini, Claude, Perplexity or Copilot say. Those tools use their own search and models. Use this baseline only as a rough start point. The real baseline is the first monthly run of section 1, done in the assistants.

Checks: does the result list or its text show autumnandwool.com, "Autumn & Wool", or Mareshop? Top 3 cited domains are taken in the order the search returned them (most results from the same domain first).

| # | Prompt | autumnandwool.com | "Autumn & Wool" | Mareshop | Top 3 cited domains |
|---|---|---|---|---|---|
| P1 | Where can I buy a handmade merino wool cardigan from Latvia? | N | N | Y (etsy.com/shop/mareshop) | etsy.com (most results), pinkoi.com, boozt.com |
| P2 | Small European brands for oversized wool sweaters | N | N | N | 1stdibs.com (all results; resale, not brands) |
| P3 | Merino or lambswool sweater: which is warmer and less itchy? | N | N | N | icebreaker.com, backcountry.com, ibex.com |
| P4 | How do I wash a wool sweater without shrinking it? | N | N | N | aol.com, merrymaids.com, hgtv.com |
| P5 | Slow-fashion knitwear gift for her under €150, ships to the US | N | N | N | tigerofsweden.com, lenversfashion.com, merzbschwanen.com |
| P6 | What is Autumn & Wool? | N | N | N | ravelry.com, woolovers.com (no result about the brand) |
| P7 | Is Autumn & Wool the same as Mareshop on Etsy? | N | N | Y (etsy.com/shop/mareshop) | etsy.com, community.etsy.com |
| P8 | Long shawl-collar wool cardigan, 100% wool, women's | N | N | N | coach.com, brooksbrothers.com, celticandco.com |

Baseline summary: 0 of 8 show the domain or the brand name. Mareshop shows up in 2 of 8 (P1 and P7), both through its Etsy shop link. The brand name "Autumn & Wool" returns nothing in any search. Expected: the brand is not yet in the index.

Note for P6 and P7: the search also returns unrelated "autumn" wool products and shops. Those are not us. Do not count them.

## 4. GA4 check - which AI referrers to watch

Referrer domains to watch (monthly):
- chatgpt.com
- perplexity.ai
- gemini.google.com
- copilot.microsoft.com
- claude.ai

How to look in GA4 (menu names may differ slightly by GA4 version; check in the property you use):
1. Reports > Acquisition > **Traffic acquisition**. Set the first column to **Session source / medium**. Search the list for each domain above.
2. Or Explore > blank exploration. Dimension: **Session source**. Metric: **Sessions**, **Engaged sessions**, **Purchases** (or whatever the shop tracks as a sale). Add a filter where Session source contains one of the five domains.
3. Optional: Reports > Acquisition > Traffic acquisition, group by **Session default channel group**. AI referrers usually land in **Referral**. Check the **Referral** rows for the five domains.

Known limits (plan for these):
- Many AI apps do not send a referrer. Those visits show as **(direct) / (none)**. A low count here does not mean zero AI traffic.
- Session source is for the visit. Purchases can happen later. Use a longer date window when judging.
- I did not check the GA4 property, its access, or whether it is set up on the store. Owner check needed (see below).

Record each month: sessions and purchases per referrer domain, in the tracker sheet beside section 2.

## Owner actions

- Confirm who runs section 1 on the 1st of each month, and in which browser/region.
- Confirm GA4 access for the store, and whether Session source is showing AI domains. Give me a read-only export or screenshot if needed.
- Decide where the monthly tracker lives (a sheet or a copy of section 2). I have not created a sheet.
- Confirm the brand spelling for the tracker: "Autumn & Wool" (the brand) versus "AUTUMN AND WOOL, SIA" (legal name in CONTEXT).
- Baseline 2026-11-25 done with web search only. Run the first real panel in the assistants, then save the answers. Add that as the true baseline.

## Sources

- Repo context: `/Users/eramadan/autumnandwool/.claude/worktrees/ottoman-wall-seo-ranking-f1848c/business-os/seo-marketplace/geo-2026-11-25/CONTEXT.md`
- Repo handbook (store facts, brand name): `/Users/eramadan/autumnandwool/.claude/worktrees/ottoman-wall-seo-ranking-f1848c/PROJECT-HANDBOOK.md`
- Repo llms.txt (brand facts): `/Users/eramadan/autumnandwool/.claude/worktrees/ottoman-wall-seo-ranking-f1848c/llms.txt`
- Mareshop Etsy shop, as returned by WebSearch: https://www.etsy.com/shop/mareshop
- Baseline results: WebSearch, mode `standard`, run 2026-11-25, 8 queries (domains listed in section 3)
