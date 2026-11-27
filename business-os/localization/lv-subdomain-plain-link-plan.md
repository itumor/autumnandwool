# LV subdomain + plain link (replaces the built-in switcher)

Why: PageSpeed "Agent accessibility → Accessibility tree is not well-formed". Failing element = Squarespace/Weglot
header switcher `div#multilingual-language-picker-desktop[role=listbox]` with no `option` children. Markup is
Squarespace-owned; Custom CSS cannot change roles and Code Injection is plan-gated (`PROJECT-HANDBOOK.md`).
Fix = drop the generated switcher, link to a real language URL with an ordinary `<a>`.

Status: **Steps 2-4 done live 2026-11-27** (lv CNAME added, `https://lv.autumnandwool.com/` serves `lang=lv`, hreflang en+lv present on LV page, EN page has none). Footer still uses `#Weglot-*` hooks; LV title still English (free-plan word limit). Steps marked OWNER need the owner's login, DNS or money.

## Steps

| # | Step | Who | Notes |
|---|---|---|---|
| 1 | Decide Weglot plan (G1). Free = 2,000 words, already 396 after the home page only. Over limit = translations stop displaying. | OWNER | No card entered by the agent. |
| 2 | Site Languages → Multilingual SEO → **Setup Subdomains**. Weglot shows a project-specific CNAME target. | OWNER | Earlier attempt (2026-11-25) landed on a generic "Setup finished" page — retry, record what Weglot shows. |
| 3 | DONE 2026-11-27. Added in **Squarespace DNS Settings** (registrar GoDaddy, DNS = Squarespace): CNAME, host `lv`, value `2e2862a6.translate-cf.weglot.io`, TTL 4 hrs. Public resolvers return it; HTTPS cert live within ~2 min. | OWNER (done) | Weglot "Check DNS" = ready, wizard reached Setup finished. |
| 4 | Back in Weglot, verify DNS. Open `https://lv.autumnandwool.com/` in incognito; confirm Latvian renders and prices/checkout still work. | agent (ego-browser) | Record hreflang on EN and LV pages (runbook section J.5). |
| 5 | Add plain link in footer code block: `<a href="https://lv.autumnandwool.com/" hreflang="lv" lang="lv">Latviešu</a>` (and a matching "English" link on the LV side if Weglot exposes one). | agent, after step 4 passes | HTML link only, no script (inline script is a hard gate). |
| 6 | Language Switch = **off** (Style your language drop-down). Re-run PageSpeed; the `listbox` failure should be gone. | agent / OWNER | Do this LAST so there is no window with no switcher at all. |
| 7 | Confirm the overlay guard `pointer-events:none !important` on `.sqs-widgets-confirmation-overlay` is unchanged. | agent | Load-bearing (2026-10-19 incident). |

## Rollback
Language Switch back to on; remove the footer `<a>`; delete the `lv` CNAME. Nothing else depends on them.

## Unverified
- That Weglot's free plan allows subdomain setup (docs not confirmed).
- That the built-in LV site stays translated after Language Switch = off (should: switcher is cosmetic).
- Whether the LV page keeps a link back to English once the switcher is off; add a plain `<a>` in the footer if not.

Sources: third-party guide https://www.sqspthemes.com/blog/how-to-set-up-weglot-on-squarespace-and-which-options-to-choose ;
Squarespace DNS records help https://support.squarespace.com/hc/en-us/articles/360002101888 ;
runbook `weglot-owner-runbook.md` section D.
