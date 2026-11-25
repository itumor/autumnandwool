# AGENT-CONTEXT.md — orientation for a new session

Written 2026-11-25. Read this after `AGENTS.md`; it does not repeat the working rules or the repo map.
It answers: what is authoritative where, what is currently true, and what is actually unblocked.

## 1. The business in five lines

Autumn & Wool (autumnandwool.com) is a one-owner knitwear label in Riga, Latvia: merino and lambswool
garments knitted on manual machines and finished by hand. Store is Squarespace 7.1, prices in EUR,
plus an Etsy shop under the older name **Mareshop**. It has effectively **zero real sales** — the
zero-sales cause was a page-wide `.sqs-widgets-confirmation-overlay` click trap, fixed live on
2026-10-19. Everything else (traffic, feed, ads, retention) is being built from that baseline.

Baselines that keep being re-quoted: ~62 visits/30 days, 94% bounce; Search Console 90 days 11 clicks /
388 impressions / 2.8% CTR / average position 14.1; 11 of 37 pages indexed; Merchant Center feed 98 rows
and 0 approved at the 21 Oct checkpoint; `sku-economics.csv` 0 of 82 SKUs costed; `kpi-weekly.csv` empty
(C16 sets the first `week_start` to 2026-10-19).

## 2. What is authoritative where

| Question | Source of truth | Not this |
|---|---|---|
| What should be done, in what order, behind which gate | `plans/2026-2027/master-plan.md` (gates G0–G9, rulings C1–C16) | plan due dates — most Oct/Nov dates are already past |
| What is left right now | `plans/2026-2027/status/OPEN-TASKS.md` (generated) | any hand-written task list |
| Live-site facts, history, open owner items | `PROJECT-HANDBOOK.md` | the handbook's stock numbers (see §6) |
| Product data | `products_Oct-17_10-46-00PM.csv` (Squarespace export, 207 rows / 160 SKUs) | the Google TSV, which is derived |
| The feed Merchant Center reads | `autumnandwool-google-feed.tsv` + `build_google_feed.py` | hand-edited TSVs — never |
| Assumed values pending owner confirmation | `business-os/**/assumptions-wave3.md` | narrative documents |
| What each agent may do | `business-os/ai-team.md` | agent names in old plans |

The repo is the decision record. The live store is the only place orders happen. There is no test
suite, no lint, no CI: verification is a Markdown diff, a regenerated CSV, or a paste of live output
under `evidence/`.

## 3. Hard constraints (these do not expire)

- Squarespace plan gates: **no Code Injection, no inline `<script>`, no waitlists.** Working surface is
  Custom CSS, product metadata, Merchant Center, and the checkout/CSS patches already shipped.
- Custom CSS must keep `pointer-events:none !important;` on the `.sqs-widgets-confirmation-overlay`
  selectors. This is load-bearing; removing it re-breaks checkout.
- Wording: "knitted on manual machines and finished by hand in Riga". Never "handmade", "sustainable",
  "organic", "certified", "hand-knitted", or "made in Latvia" without owner evidence. Three live URL
  slugs contain "hand-knitted" — leave them, do not propagate.
- No invented GTINs/MPNs (`identifier_exists=no` stays), no invented fibre percentages, colour names,
  stock counts, review ratings or cost figures. Use `[FILL]` and an `ASSUMED` task instead.
- Never spend money, send a message, or change a live setting. All live actions need the owner logged in
  and ego-browser running from an ordinary Terminal — not from this sandboxed shell.

## 4. Where the work actually stands (2026-11-25)

- **GEO sprint** (`business-os/seo-marketplace/2026-11-25-geo-roadmap.md`): GEO-01…GEO-11 produced as
  drafts; two items went live that evening (About Q&A, /shop H1 + crawlable `/wool-*` links). The
  consolidated owner checklist is `geo-2026-11-25/00-OWNER-ACTIONS.md` (45 items, groups A–D). The
  prompt-panel/visibility re-run is not due before 2026-12-01.
- **Feed (SEO-03 / GEO-02), done code-side 2026-11-25:** `build_google_feed.py` no longer hard-codes
  `in_stock`; it reads `Stock` from the export and stops on a missing, non-numeric or conflicting SKU.
  It also emits an opt-in 26-column OpenAI feed (`--openai`). Google output is byte-identical to the
  committed TSV. Details and commands: `business-os/seo-marketplace/feed/README.md`.
- **OpenAI feed draft** `feed/2026-11-25-openai-feed-DRAFT-do-not-upload.tsv` is deliberately named
  un-uploadable: `target_countries=LV,EE,LT` is a guess, and the business is not claimed/verified in
  OpenAI Business Hub yet.
- **Most other plan work is owner-blocked, not agent-blocked.** Blocked means a number, a login or a
  decision is missing; do not "unblock" it by inventing one.

## 5. The owner is the bottleneck: gates in one table

| Gate | Missing | Blocks |
|---|---|---|
| G0 | timed production runs, yarn grams, labour rate, physical stock | every cost, capacity and cash number |
| G1 | SKU cost confirmation → `sku-economics.csv` | break-even CAC, any budget |
| G2 | GREEN capacity per SKU (needs G1) | any promotion, content product posts, pins, ads |
| G3 | cash balance, fixed costs, 13-week forecast | any spend, hire, yarn buy |
| G4 | PayPal live, delivery times, size info, returns wording, bound variant photos, claims wording | creator gifts, PR, paid traffic |
| G5 | carrier-backed delivery ranges + Christmas order-by dates | gift content, banner, MTO stop date |
| G6 | Merchant Center clean approval | Google free listings, Shopping/PMax, Pinterest catalog |
| G7 | Squarespace plan decision, attribution method | conversion ads, per-creator codes |
| G8 | claims evidence | first creator DM, ads, PDP copy, feed |
| G9 | legal review of returns/consent/label wording | final returns page, lifecycle emails |

## 6. Data traps found the hard way

- **"85 in stock / 13 out of stock"** in `PROJECT-HANDBOOK.md` §5 item 4 is not reproducible: every one
  of the 98 feed SKUs shows stock ≥ 1 in the 17 Oct export. QA F2 says so. The export wins until the
  owner counts physically.
- **Feed rows ≠ visible products.** The feed has 98 rows / 15 groups over 160 SKUs because hidden
  variants are included; only 21 SKUs are `Visible=Yes`. A per-product row count from the export will
  not match the feed.
- **Turtleneck 360 and beanie 220** look like made-to-order placeholders, not stock.
- **~48 rows ship the wrong or no variant photo**, and `VIMG` in the generator cannot fix that — the
  photos must be bound in Squarespace. Only the cardigan Brown override is safe in code.
- **12 rows have an empty `color`** and `material` carries no fibre %. Both are owner answers.
- **AI shopping feeds are not live**: no ChatGPT/Perplexity merchant programme is confirmed for this
  store. Treat eligibility claims as unconfirmed unless read on an official page in-session.

## 7. Status machinery

`plans/2026-2027/status/*.md` holds one table per department plus two generated files.
`python3 plans/2026-2027/status/rollup.py` rewrites `STATUS.md` and `OPEN-TASKS.md` (it also reorders
departments by blocked count, so expect churn). After any status-table edit, run it — do not hand-edit
the generated pair. The header line `42 assumed · 42 blocked · 90 to do · 122 done` must always equal
the sum of the department tables; `rollup.py --selftest` checks the parser.

Status words mean: `DONE` finished; `ASSUMED` finished on proposed values and awaiting owner
confirmation; `BLOCKED` waiting on owner or another department; `TODO` scheduled later.

## 8. Sensible next moves for a new session

1. Run `python3 plans/2026-2027/status/rollup.py` and read `OPEN-TASKS.md`. Pick work that is `TODO`,
   not `BLOCKED`.
2. Prefer repo-side work that does not need a login: feed/QA/data quality, plan and assumption
   registers, copy drafts, owner question packs.
3. If a task needs a live store, confirm the owner is logged in and ego-browser is available from an
   ordinary Terminal before planning it; otherwise write the exact click-path into
   `geo-2026-11-25/00-OWNER-ACTIONS.md`.
4. Add new assumptions to the matching `assumptions-wave3.md` with an `A-*` ID and mark the task
   `ASSUMED`, with `[FILL]` where a number is missing.
5. Do not commit another agent's or the owner's in-flight changes. Check `git status` and stage paths
   explicitly; `.claude/agents/aw-*.md`, `.claude/skills/**` and `skills-lock.json` are the owner's
   2026-11-25 skills wiring.

## 9. Commands

```bash
python3 build_google_feed.py products_Oct-17_10-46-00PM.csv autumnandwool-google-feed.tsv   # Google only
python3 business-os/unit_economics.py                                                      # useless until G1
python3 plans/2026-2027/status/rollup.py                                                   # STATUS + OPEN-TASKS
```

Gate sequence for money: G0 → G1 → min contribution → break-even CAC → G2 GREEN → G3 cash check →
owner sets ceiling → capped test at 3× break-even CAC per concept. Traffic chain: G6 + G4 + G8 → free
channels first.
