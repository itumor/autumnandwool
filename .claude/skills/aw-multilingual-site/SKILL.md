---
name: aw-multilingual-site
description: Run and troubleshoot the English→Latvian (later Russian) Squarespace/Weglot rollout for autumnandwool.com. Use when asked to set up, edit, QA or explain the multilingual storefront, language switcher, Weglot glossary/translations, word limits, subdomains/hreflang, or to brief a native reviewer.
---

# Autumn & Wool multilingual storefront (Squarespace 7.1 + Weglot)

Operational knowledge verified live on 2026-11-25/26. Design source of truth:
`plans/2026-2027/multilingual-plan.md`; executable tasks: `plans/2026-2027/multilingual-implementation-plan.md`;
live evidence: `evidence/multilingual-2026-11-25/`. Nothing here authorizes publishing unreviewed copy.

## 1. Platform facts (verified live)

- Squarespace 7.1, Basic plan assumed (A-GM-05). **Site Languages → "Multilingual by Weglot" IS available on this plan.**
- Correct admin path: click **Settings** → **Website** → **Site Languages**, i.e.
  `https://rose-tarpon-ld9w.squarespace.com/config/settings/website/language-region/site-languages`.
  Guessing `/config/website/language-region/...` (no `/settings/`) silently lands in site preview.
- Panel shows: site language English (United States); "Multilingual by Weglot", free ≤2,000 words / 1 destination
  language; promo code `WELOVESQSP` (20% off) shown in admin.
- Weglot account was created with `autumnandwool@gmail.com`; project "Autumn & Wool" in workspace `w-c5647a5b67`.
- Latvian row is **Public** (checkbox checked); Multilingual Customer Notifications is **on** by default.
- The switcher is injected client-side: `curl` of the public HTML shows **no** `weglot` string, but the browser shows
  `listbox "language picker"` with `Latviešu` / `English`. Verify in a browser, not with curl.
- Selecting `Latviešu` translates the page **on the same URL** — no `lv.` subdomain, no `hreflang` yet.
- The admin "SETUP SUBDOMAINS" link (`dashboard.weglot.com/getting-started/Connect?isSwitchingIntegration=true`)
  landed on a generic "Setup finished" page. No DNS change was made; do not claim subdomain/hreflang is configured.

## 2. Word count is the hard limit

- After switching **only the homepage** to Latvian: Squarespace admin showed **396 / 2,000** words; Weglot dashboard
  showed 270 translated words, 0% manually translated, and a separate **"2,000 AI words left until December 01"**.
  These counters differ — quote them with their source.
- 49 URLs / 22 products are in the sitemap, so the free tier cannot cover the site. Stop generating translations by
  browsing many pages: translations stop displaying when the free limit is exceeded (paid plans pause new words only).
- Owner gate G1 = paid plan yes/no (with real quote) or page exclusions. Never enter a card or buy a plan yourself.

## 3. Glossary and locked terms (live)

Added 9 Weglot "Never translate" rules (all language pairs, case-insensitive) — check before editing:
`Autumn & Wool`, `Mareshop`, `Kristine`, `autumnandwool@gmail.com`,
`Merino Wool Raglan Cardigan`, `Merino Wool Raglan Sweater`, `Women's Classic Lambswool Crew Sweater`,
`Merino Wool Hat & Scarf Set`, `Merino Rib-Knit Beanie`.
Full locked glossary and LV drafts: `business-os/localization/lv-money-pages-draft.md` §2.
Original evidence of the live state: `evidence/multilingual-2026-11-25/live-setup.md`.

## 4. How a native reviewer edits Latvian text (official Weglot UI)

Two supported paths (verified against Weglot help docs 2026-11-24/25):

1. **Visual Editor (best in context).** `dashboard.weglot.com` → project → Translations → Visual Editor →
   **Start editing** → choose Latviešu → open a page via the editor's URL bar → click the **blue pencil** next to text
   (Option+click on Mac if it does not appear) → edit in the left panel → **OK**. The label becomes
   "Manual translation" with a green saved confirmation. Refresh the live site; if stale, hard refresh (Cmd+Shift+R)
   or incognito.
2. **Translations List (best for exact strings).** Direct URL:
   `https://dashboard.weglot.com/workspaces/w-c5647a5b67/projects/autumn-wool/translations?languages=en_lv`
   → **Search a translation** (or URL list on the left) → click the Latvian text in the right column → type; changes
   save automatically with "Translation successfully edited". Optional spellcheck = "Mark as reviewed".
   "Search and replace" (right-hand Quick links) for repeated strings — check the preview first.

Known rough machine output (homepage, before manual fixes): title became "Rudens un vilna …" (brand translated),
stray `„”` in the heading, "oversized" → "Pārmērīgi liela izmēra". Fix via glossary + manual edits, not by claiming
the automatic translation is publication-ready.

## 5. Content gates (do not bypass)

- Native Latvian reviewer name is gate G3 — still `[FILL]`. Owner brief: `business-os/localization/lv-native-review-brief.md`.
- Returns/withdrawal/refund wording is gate G4 (PRD-19 EU adviser). Lines in the LV draft carry `[PENDING ADVISER]`.
  Never publish altered legal terms or translate a draft still marked `translation-draft`.
- G5 priority PDP list is provisional (C5). No unverified claims: no sustainable/organic/eco/hand-knitted;
  approved process phrase: "knitted on manual machines and finished by hand in Riga".
- On 2026-11-26 an instruction email was sent from `ebrahim@cast.ai` to `autumnandwool@gmail.com` with the reviewer steps
  and task list. Do not resend without being asked.

## 6. Load-bearing live guard

`.sqs-widgets-confirmation-overlay` and `.sqs-widgets-confirmation` must keep `pointer-events:none !important;`.
It exists **only in `custom.css`** (versioned URL recorded in `evidence/multilingual-2026-11-25/live-baseline.md`);
`site.css` has the base selectors without the guard. Checking `site.css` alone is NOT verification. Any Custom CSS edit
must preserve both declarations; QA must re-check a failed add-to-cart afterwards.

## 7. Tooling gotchas hit during this rollout

- `ego-browser` lives at `~/.local/bin/ego-browser` (symlink to Ego Lite); `command -v ego` finds nothing.
  Always run `ego-browser skill` before a browser task; use TaskSpaces/pages (`p1`), not ad-hoc new tabs.
- At a Google login chooser, Ego may hand control to the user ("Control of this task space is with the user") — that is
  a hard stop. Wait for the user to reply "continue", then `takeOverTaskSpace(id)`. Never take back control unprompted.
- `browse` (Chrome relay) was offline until the user ran `curl -fsSL https://opencode.ai/browse/install | bash`.
  `browse status` reports connected browsers; close tabs you open with `browse.tabs({action:"close", group:...})`.
- GitHub remote is `itumor/autumnandwool`. `gh` active account `ebrahim-castai` is NOT a collaborator — `gh pr create`
  fails with "must be a collaborator". Use `gh auth switch -u itumor`, create the PR, then switch back.
  Cutting a branch from local `main` carries other agents' unpushed commits into the PR — say so in the PR body.
- Gmail new compose from a URL (`?view=cm&fs=1&to=…&su=…`) prefills To/Subject; paste a prepared body with
  `pbcopy < file` + focus `div.Am[contenteditable="true"][aria-label="Message Body"]` + `Meta+v`; verify "Message sent".
- Do not push edits to status tables — `rollup.py`/the task counts own them.
