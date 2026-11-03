# Owner unblock — first sale (2026-11-02)

Status: store sellable, 0 real orders. Problem = no buyers reach site. Free Google channels maxed out by agent; next lift needs owner logins or ad budget.

## Facts (2026-11-02)
- Real traffic ~5-15 visits/day. Oct 17-19 spike (~850) = our own audit sessions.
- Merchant Center: 99/99 approved, 52 product impressions / 28d, 0 product clicks.
- GSC 3 mo: 17 clicks, 614 impressions, avg pos 14.7. 30 pages indexed.
- Your existing audience points to **Etsy, not site**: Etsy 16,644 admirers / 8,153 sales, Facebook 866, Instagram 638, Pinterest 261, TikTok 94. Only Instagram links to site.

## Do these (ranked by chance of first sale)
1. **Swap profile links to site** (5 min each, you log in):
   - TikTok > Edit profile > Website: `https://www.autumnandwool.com/shop?utm_source=tiktok&utm_medium=social&utm_campaign=bio-link`
   - Facebook page > Edit page info > Website: `https://www.autumnandwool.com/shop?utm_source=facebook&utm_medium=social&utm_campaign=bio-link`
   - Pinterest mmareshop > Edit profile > Website: `https://www.autumnandwool.com/shop?utm_source=pinterest&utm_medium=social&utm_campaign=bio-link`
2. **Log into Instagram, Facebook, Pinterest, TikTok inside ego lite once.** Agent can't type passwords. After login, daily agent run posts product content from `campaign-assets/drafts/` and checks links.
3. **One "our own shop is open" post** on Instagram + Facebook + TikTok, link in bio. Draft: `campaign-assets/drafts/social-batch-2026-10-28.md`.
4. **Ad budget decision** (fastest paid path): Google Shopping / Performance Max on the 99 approved products, test €5-10/day for 14 days, hard cap €140. Needs your card + OK in Merchant Center > Ad campaigns. Agent will not spend money without it.
5. **Google Business Profile** for Autumn & Wool, Riga: business.google.com, website = `https://www.autumnandwool.com/shop?utm_source=google&utm_medium=organic&utm_campaign=gbp`. Verification (postcard/phone) = you only.
6. **PayPal connect**: Squarespace > Selling Tools > Payments. Still pending since 10-19.

## Done by agent today
- Merchant Center: automatic image improvements on; customer service website + email (`autumnandwool@gmail.com`) set. Phone `+371 29838090` was prefilled, left as-is — confirm OK.
- GSC: indexing requested for 6 category pages + hat-and-scarf set. Sitemap OK.
- Daily scheduled task `aw-first-sale-daily` (09:14): checks orders, traffic, MC/GSC, one safe action, logs to `daily-log.md`, pushes notification on first real order.

## Flags
- MC delivery times (Europe 7-15 days) ≠ shipping page (5-10 days). Pick one.
- 47 products missing description attributes in MC — product data frozen; unfreeze to let agent fill. List: `merchant-center-report.md`.
- Category pages canonical → `/shop` = Squarespace default, not fixable in settings.
