# GEO-03 Brand entity pack (2026-11-25)

DRAFT — for owner approval. Nothing here has been posted or changed. Brand name everywhere: **Autumn & Wool**.

Goal: tell AI search and people that Mareshop (Etsy, since 2011) and Autumn & Wool (autumnandwool.com) are the same maker, Kristine in Riga.

## 0. Brand fact block (reuse everywhere)

Paste-ready (about 60 words):

> Autumn & Wool is a small knitwear studio in Riga, Latvia, run by designer and maker Kristine. She makes women's wool cardigans, sweaters, vests, beanies and scarves in merino wool, lambswool and pure new wool (the exact fibre is on each product page). Pieces are knitted on manual knitting machines and finished by hand in Riga. Before autumnandwool.com, the same maker sold as Mareshop on Etsy, since 2011, with a 4.9 rating from 1,400+ reviews on Etsy.

Short version (one line): "Autumn & Wool, knitwear made in Riga by Kristine. Formerly Mareshop on Etsy."

Fact sources: studio, Kristine, fibres, "since 2011": `llms.txt` (repo root). Machine-knitted, hand-finished, 15 years, 8,000+ orders, 4.9 from 1,400+ Etsy reviews: live https://www.autumnandwool.com/about (read 2026-11-25) and aw-brand-voice s3. Etsy shop stats (4.9, 1.5k reviews, 8,153 sales): `evidence/first-sale-2026-11-02/social-recon.md`.

Open items:
- [VERIFY: owner OK that "since 2011" (llms.txt) and "15 years" (About) are both true. 2011 to 2026 = 15 years, so they agree.]
- [VERIFY: `llms.txt` line 3 says "knitted by hand or on a manually operated knitting machine". The About page says manual machine, hand-finished. Use the machine wording above; the "by hand" wording clashes with the brand-voice rule.]
- Add [FILL: year Autumn & Wool launched as a brand] only if the owner wants it stated. Not on file.
- "Family knitting tradition" appears on the live About page, in Kristine's words. Not used above; reuse only with owner OK.

## 1. Etsy (Mareshop)

### 1.1 Policy check (cited)

What I could confirm (Etsy pages themselves returned 403 to my fetch, so wording comes from search summaries of Etsy help and the Seller Policy):
- Etsy's help says the About section Links field is for a website, blog or social profile (https://help.etsy.com/hc/en-us/articles/115015628487).
- Etsy's Seller Policy bars directing shoppers to another online venue to buy the same items you sell on Etsy, including posting links/URLs or giving details sufficient to find that venue (https://www.etsy.com/legal/sellers/; off-platform page https://www.etsy.com/legal/policy/off-platform-transactions/1254654515806).
- A 2016 Etsy staff forum post treated a link to your own selling site as risky, but a blog or social link as fine (https://www.etsy.com/forums_thread.php?thread_id=6547379). Old; not current policy.
- Announcement links reportedly are not clickable (AWeber guide, third party).

Conclusion: Autumn & Wool sells the same knitwear. A link to autumnandwool.com, or the URL as text, is a real risk to a 15-year, 4.9-star shop. A plain-language rebrand note with no URL and no "buy there" push is much lower risk. Social links (Instagram) are already in the Mareshop About, per the 2 Nov recon.
[VERIFY: current Seller Policy wording. Owner to read https://www.etsy.com/legal/sellers/ or ask Etsy Seller Support before using version B.]

### 1.2 Version A: complies even if URLs are not allowed (recommended)

No URL, no website name, no "buy elsewhere". Says who the maker is and where to follow her.

Shop announcement (short):

> Mareshop is knitted in Riga by Kristine. We are also growing a new brand, Autumn & Wool, with the same maker and the same machines. Questions about sizing or care? Send a message here, I answer every one.

About paragraph:

> Mareshop has been my Riga studio on Etsy since 2011. I am Kristine. I knit each piece on a manual knitting machine and finish it by hand: seams, washing and pressing. My newer brand name is Autumn & Wool. Same maker, same studio, same way of working. You can follow the studio on Instagram at @autumnandwool.

### 1.3 Version B: names the website (only if the owner confirms it is allowed)

Use only after Seller Support or the Seller Policy confirms a link to an own site is allowed. Keep it as information. Never write "buy here", "cheaper", "discount" or "order directly".

Announcement:

> Mareshop is now also Autumn & Wool, the same maker in Riga. Our website: autumnandwool.com. Shopping on Etsy works exactly as before.

About paragraph:

> Mareshop has been my Riga studio on Etsy since 2011. I am Kristine. I knit each piece on a manual knitting machine and finish it by hand. My newer brand name is Autumn & Wool (autumnandwool.com). Same maker, same studio.

Put the site in the About "Links" field only under B.

## 2. Social bios

Handles on file (`social-recon.md`, logged-out view 2026-11-02, live site footer): Instagram @autumnandwool (638 followers), TikTok @autumnandwool (94), Facebook page AccessoriesMareshop (named "Mareshop", 866), Pinterest mmareshop (261). `pinterest.com/autumnandwool` returned an error on 2 Nov, so the handle looked free [VERIFY].

Display name on all four: **Autumn & Wool**. Facebook and Pinterest still show Mareshop; renaming is an owner action (Facebook may limit name changes).

| Platform | Limit | Bio (paste-ready) |
|---|---|---|
| Instagram | 150 chars | Knitwear made in Riga by Kristine. Manual knitting machines, finished by hand. Formerly Mareshop on Etsy. |
| TikTok | 80 chars | Knitwear made in Riga by Kristine. Formerly Mareshop. |
| Pinterest | 160 chars | Autumn & Wool: knitwear made in Riga, Latvia by Kristine. Merino wool, lambswool and pure new wool. Formerly Mareshop on Etsy. |
| Facebook (Intro 101 chars; About longer) | | Intro: Knitwear made in Riga by Kristine. Formerly Mareshop on Etsy.<br>About: use the fact block in section 0. |

Website field on each: `https://www.autumnandwool.com/shop?utm_source=[instagram|tiktok|pinterest|facebook]&utm_medium=social&utm_campaign=bio-link` (from social-recon and owner-action-pack C). Facebook and TikTok currently point to etsy.com/shop/mareshop; Etsy-policy risk does not apply to links placed on those platforms.
Counts are approximate; check the character limit in the app. No hashtags, no claim words.

## 3. Squarespace Business Information

Proposal: Business name field = **Autumn & Wool**. The legal name stays on the imprint page: AUTUMN AND WOOL, SIA, reg. no. 40203644965 (source: `llms.txt`; live /imprint).

Current state: the Business Information name is "AUTUMN AND WOOL, SIA" and is what Organization/LocalBusiness JSON-LD reads (re-audit finding A-04, `evidence/seo-reaudit-2026-11-10/findings-1111/geo-agentic.md`). The WebSite name is already the trade name.

Check first, before the owner changes it:
1. Where this field prints: order confirmation emails, invoices and receipts, email footers, the checkout page, the legal footer. If the legal name must appear on invoices (Latvian rules) [VERIFY with the accountant], keep it there another way.
2. Squarespace "Legal name" or "Imprint" fields, if shown separately. Leave legal name unchanged.
3. Payment provider and Merchant Center business name: they should not conflict with the trade name. Do not change either from this task.
4. Send a test order or preview email after the change and compare it to before.
5. Re-run the JSON-LD check on the home page. Expected: `name` = Autumn & Wool, `legalName` = AUTUMN AND WOOL, SIA.

Owner decision: whether the field change is worth the invoice risk. If it is, the JSON-LD gains a clean brand name.

## 4. Proposed Organization `sameAs`

Live now (re-audit A-03, 2026-11-10; I could not re-fetch the page JSON-LD in this task): `["https://www.instagram.com/autumnandwool","https://www.tiktok.com/@autumnandwool"]`. [VERIFY: unchanged on 2026-11-25]

| URL | Status | Note |
|---|---|---|
| https://www.instagram.com/autumnandwool | Real, in live JSON-LD | Keep |
| https://www.tiktok.com/@autumnandwool | Real, in live JSON-LD | Keep |
| https://www.etsy.com/shop/mareshop | Real, seen 2026-11-02 and in CONTEXT | Add: this is the link that connects the 15-year reputation. Owner decision: it is an entity link, not a sales push (re-audit S-02) |
| https://www.facebook.com/AccessoriesMareshop | Real, linked in live footer | Add; unverified admin rights. Replace after a rename |
| https://www.pinterest.com/mmareshop | Real, linked in live footer | Add; unverified. Replace if an autumnandwool account is created |
| https://www.pinterest.com/autumnandwool | Not found (error on 2 Nov) | Do not add until it exists |
| Google Business Profile, YouTube, LinkedIn, Wikipedia, Reddit | None found | Do not add. Add GBP link after owner creates and verifies it |

How to apply: this is a Squarespace settings/social-links change, owner only. No code injection.

## Owner actions

1. Decide Etsy wording: send Version A now, or ask Etsy Seller Support whether Version B (website name) is allowed. Etsy edits are owner-only.
2. Confirm "since 2011" and "15 years", and which Etsy numbers may be quoted (1,400+ is on the site; Etsy shows 1.5k).
3. Update bios and display names on Instagram, TikTok, Pinterest, Facebook (section 2). Confirm admin rights on Facebook and Pinterest first.
4. Decide the Business Information rename after the invoice/email check in section 3.
5. Approve the `sameAs` list; add Etsy, Facebook, Pinterest in Squarespace social links.
6. Reconcile `llms.txt` line 3 ("by hand or on a manually operated knitting machine") with the About wording, then reuse the fact block in section 0.

## Claim check

Brand voice checklist run: no banned words (sustainable, organic, certified, luxurious), no "hand-knitted", "handmade" not used, fibre only as general product lines already on `llms.txt`/About with "exact fibre on each product page", no invented numbers. Review quotes: none. Pass, with the [VERIFY] items above.

## Sources

- Repo: `llms.txt`; `PROJECT-HANDBOOK.md` (lines 4, 92); `evidence/first-sale-2026-11-02/social-recon.md`; `evidence/seo-reaudit-2026-11-10/findings-1111/geo-agentic.md` (A-03, A-04); `evidence/seo-reaudit-2026-11-10/findings-1111/schema-ecommerce.md` (S-02); `business-os/seo-marketplace/geo-2026-11-25/CONTEXT.md`; `.claude/skills/aw-brand-voice/SKILL.md`
- Live: https://www.autumnandwool.com/about (read 2026-11-25)
- Etsy Seller Policy https://www.etsy.com/legal/sellers/ and off-platform page https://www.etsy.com/legal/policy/off-platform-transactions/1254654515806 (not fetchable, 403; read via search summary)
- Etsy Help, About section: https://help.etsy.com/hc/en-us/articles/115015628487
- Etsy forum, off-site linking (2016): https://www.etsy.com/forums_thread.php?thread_id=6547379
- AWeber, announcement links: https://docs.aweber.com/integrations/integrations/how-do-i-put-my-landing-page-on-my-etsy-store
