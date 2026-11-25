# Owner runbook — Squarespace 7.1 built-in Weglot (English → Latvian)

DRAFT for owner use, 25 Nov 2026. Nothing here has been applied to the live site.
Sources: official Squarespace Help Center and Weglot Help Center, checked 2026-11-25 (URLs at the end).
Items marked **VERIFY** are not confirmed for this store/plan by official docs — check in the admin or with support.

Plan context: `plans/2026-2027/multilingual-plan.md` (design) and `plans/2026-2027/multilingual-implementation-plan.md` (tasks).
Owner gates G1–G6 in the design doc must be resolved at the steps noted below.

## A. Where to go and how to connect

**Admin path (7.1):** Settings → Website → Language & Region → **Site Languages**.
Direct link: `https://account.squarespace.com/settings/website/language-region/site-languages`

1. Open **Site Languages**.
2. Under **Multilingual by Weglot**, click **Connect**, then **Allow**.
3. Create a **new Weglot account**. Squarespace explicitly advises against reusing an account on a free plan or expired trial because the full new-account word allowance would be unavailable. If you already have a **paid** Weglot plan, sign in and choose **Create a new project**.
4. **Original language** = English. **Destination languages** = Latvian. **VERIFY:** Latvian is selectable for this integration.
5. Click **Save**. Squarespace adds a language switcher to the site header.
6. Open the site in an **incognito window**, switch to Latvian, and click through several pages. Squarespace says this populates translations so they can be edited in Weglot.
7. Set up the LV subdomain (section D) before treating the rollout as SEO-ready.

## B. Editing translations later

Translations are **not** editable in Squarespace. In **Site Languages**, click **Edit Translations** — a Weglot tab opens.
Apply the locked glossary and the reviewed drafts in `business-os/localization/lv-money-pages-draft.md` there.

## C. Header switcher — native options only

Fonts and colours follow the site's global styles. **Site Languages → Style your language drop-down → customize → Save**.

| Native setting | Options |
|---|---|
| Language Switch | toggle off to hide the switcher |
| Display | Text Only / Icon & Text / Flag & Text |
| Flag shape (Flag & Text only) | Circle / Rectangle / Square |
| Flag / language icon size | increase / decrease |

Anything else (moving the switcher, custom markup, per-page styling) is **not stated in official docs** and would need code — do not attempt on this plan.
Check the switcher at 390 px: it must be visible and tappable without covering the header links.

## D. Language subdomain (recommended — G2)

URL form: `https://lv.autumnandwool.com` for the Latvian version.

1. A **custom domain must already be connected** to the Squarespace site; otherwise the subdomain setup option is absent.
2. **Site Languages → Setup Subdomains**; Weglot guides the rest.

Why Squarespace recommends it (quoted from the official guide):

- "Offers a faster, fully-translated experience"
- "Automatically adds hreflang tags to make your site searchable in multiple languages"
- "Helps search engines serve the correct language version of your pages in search results"
- "Prevents search engines from flagging your pages as duplicate content"

Without a subdomain, Squarespace warns that "some content (like error messages or button animations) won't appear translated" and translations may load with a lag.

**VERIFY / known limitation:** Weglot's own docs say that for the Squarespace subdomain integration it "can only edit the translated pages" and cannot put full paths in hreflang tags on the **original** pages; their suggested fix uses GitHub/command-line hooks, out of scope on this plan. Record the actual hreflang state in QA rather than assuming it is perfect.

## E. Public / private languages and hiding the switcher

- In language settings, set Latvian **public** so visitors see it in the header drop-down. **Private** means the switcher is still visible while editing but not to visitors.
- If every translated language is private, the drop-down remains with English only.
- To hide the switcher completely: **Style your language drop-down → Language Switch = off**.

## F. Customer notification emails

| Item | Official behaviour |
|---|---|
| Default | Translated customer notification emails are **on by default** when Weglot is connected |
| Language rule | Shoppers receive emails in the language they used while browsing; gift cards use the purchaser's language for both people |
| Preview | Settings → Customer Notifications → email category → email type → **View in** drop-down → language |
| Disable | language settings → **Multilingual Customer Notifications = off** |

The 10-day trial word allowance **includes** translated notification emails — measure before deciding on a paid plan (G1).

## G. Word counts and what happens at the limit

| State | Limit / behaviour |
|---|---|
| Weglot free | 1 destination language, up to **2,000 words** |
| 10-day trial | up to **10,000 words** into one other language (notification emails included) |
| After trial | ≤2,000 words in one language → free plan; >2,000 words or a second language → paid plan, or free with words removed / pages excluded |
| Over free limit | Weglot emails "Words limit reached on Weglot plan"; switcher still shows but **translations stop displaying** |
| Over paid limit | New words pause; already-translated words keep displaying |

Check usage in language settings (current plan + word usage); **Upgrade / Browse Plans** opens Weglot.
Ways to reduce: finish page building before translating; use Weglot's Website Word Count tool; delete demo content; exclude content-heavy or private pages; remove inactive translations.
Weglot exclusions: Dashboard → Project → Settings → Translation Exclusions → Add Rule, using relative URLs (`/page`) with Starts with / Is exactly / Contains. Excluding does not delete existing translations unless "Delete translations linked to matching URLs" is enabled. "Hide switcher on excluded page" is **not available** for the Squarespace integration. Import/export of exclusion rules is a Weglot Advanced feature (Weglot plan tier, not Squarespace plan tier).

## H. What this integration does NOT translate

Squarespace's explicit list: **Email Campaigns; Acuity Scheduling; third-party content blocks such as the map block; Member Sites and customer accounts login screens.**
Squarespace separately states that with Weglot, error messages and the checkout page **can** be translated.
Consequence for CX: do not promise a fully translated site; LV shoppers may still see English in campaigns, account screens and third-party blocks.

## I. SEO statements — official wording and limits

- Squarespace, on subdomains: "Automatically adds hreflang tags…" and "Prevents search engines from flagging your pages as duplicate content" (quotes in D).
- Weglot (secondary, integration-dependent): adds hreflang to the original `<head>` and translated pages; translates meta descriptions, `alt` attributes, page titles and structured data; "does not add canonical tags, but will automatically update your canonical tag if one is already present"; `<html lang>` "must match the hreflang values".
- Weglot warns its **JavaScript integration** "does not offer SEO benefits, as translations are rendered client-side and are not crawlable by search engines". Whether that applies to the built-in Squarespace integration **without** a subdomain is **VERIFY** — another reason to use the subdomain.
- Canonical and `<html lang>` behaviour for Squarespace 7.1 + this integration: **not stated in official Squarespace docs**. QA must inspect the live LV pages and record what is actually there.

## J. Pre-flight checks on this store

0. **VERIFY** native locale option: the live homepage markup contains a Squarespace language-picker hook with
   `"enabled": false` and `i18n_beta_website_locales` in beta flags (evidence:
   `evidence/multilingual-2026-11-25/live-baseline.md`). If Site Languages offers a native locale option in addition
   to Weglot, pause and compare before committing — the approved design chose Weglot, not a beta feature.
1. **VERIFY** Site Languages / Weglot panel is available on the current (assumed Basic) plan — docs state 7.1 only, not a plan tier.
2. **VERIFY** Latvian is a selectable destination language.
3. **VERIFY** a custom domain is connected to this Squarespace site (required for subdomains).
4. **VERIFY** real word count for EN → LV, including notification emails, before entering payment details (G1).
5. **VERIFY** hreflang on original and LV pages after setup; any code-level fix is blocked by Basic-plan Code Injection rules (G2 caveat in D).
6. Confirm the load-bearing overlay CSS guard is unchanged after any header styling (see `PROJECT-HANDBOOK.md` §4).

## Owner gate map

| Gate | Needed at step | Source |
|---|---|---|
| G1 — paid Weglot plan yes/no + quoted price + real word count | A3–A5, G | `multilingual-plan.md` §6 |
| G2 — LV subdomain vs path (recommendation: subdomain) | D | design approval 25 Nov; this runbook D |
| G3 — named native Latvian reviewer | B, before publication | `multilingual-plan.md` §6 |
| G4 — returns/withdrawal wording after adviser (PRD-19) | B, money pages | `status/production.md` PRD-19 |
| G5 — 5 priority PDP list | B | master-plan C5 |
| G6 — Russian go/no-go | after LV measurement | `multilingual-plan.md` §8 |

## Sources

- https://support.squarespace.com/hc/en-us/articles/205809778-Creating-a-multilingual-site-with-Weglot (last updated 3 Apr 2026)
- https://support.squarespace.com/hc/en-us/articles/16552875658765-Manually-creating-a-multilingual-site
- https://support.weglot.com/article/293-how-does-weglot-manage-the-seo
- https://support.weglot.com/article/304-i-have-some-errors-with-the-hreflang-tags
- https://support.weglot.com/article/95-how-to-exclude-urls-blocks-words-from-translation
