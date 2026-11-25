# Bing and Google indexing: step-by-step guide (DRAFT, GEO-01)

Date: 2026-11-25. Owner: Kristine. Time needed: about 30 minutes today, 2 minutes in one week.

**Why it matters:** Copilot uses Bing's index, ChatGPT search draws partly on Bing, and Gemini and Google AI Overviews use Google's index. If a page is not indexed, AI tools cannot quote it.

Before you start: you need the Google account that owns Search Console for autumnandwool.com. Do not share the login with anyone. Do not enter the Google password into any site other than Google's own sign-in page.

---

## Part 1. Set up Bing Webmaster Tools by import (no code)

Bing can copy your verified sites from Google Search Console. You do not add a meta tag or DNS record.

1. Open https://www.bing.com/webmasters in your browser.
2. Sign in with a Microsoft, Google or Facebook account. Use the same Google account as Search Console, so the import is simple.
3. On the start page, choose **Import** under the Google Search Console option. If you are already signed in, you may see **Add a site** first. Click it, then choose **Import**.
4. Sign in to Google when asked. Choose the Google account that owns Search Console.
5. Google shows a permission screen. Read it, then click **Allow**. Bing asks for access to your list of verified sites and sitemaps. It does not ask for your Search Console performance data.
6. Tick **https://www.autumnandwool.com/** (or the property name you see, `autumnandwool.com` if it is a Domain property). Click **Import**, then **Done**.
7. Check that the site appears in **My Sites** with a sitemap count.

Notes:
- Bing re-checks ownership by syncing with Search Console. If you remove Bing's access in your Google account, the Bing site stops working. You would then need to verify by another method.
- If the site does not appear in the list, first check Search Console: Settings > Ownership verification must show the site as verified.

Source: [Bing Webmaster Tools import from Google Search Console (Bing blog, 2019)](https://blogs.bing.com/webmaster/september-2019/Import-sites-from-Search-Console-to-Bing-Webmaster-Tools). Import steps checked on Bing's page on 2026-11-25; button names can change, so use the nearest match.

### 1b. Submit the sitemap in Bing

1. In Bing Webmaster Tools, click your site (autumnandwool.com).
2. In the left menu, click **Sitemaps**.
3. Click **Submit sitemap** (or the add button on that page).
4. Type exactly: `https://www.autumnandwool.com/sitemap.xml`
5. Click **Submit**. Bing tries to fetch it straight away and re-checks it at least once a day.
6. Wait a few minutes, then refresh the page. Check that the sitemap shows no error. Note the "discovered" and "indexed" counts for later.

Source: [Keeping Content Discoverable with Sitemaps in AI Powered Search (Bing blog, July 2025)](https://blogs.bing.com/webmaster/July-2025/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search). The button name was not in the article; check the page.

### 1c. Check the home page in Bing URL Inspection

1. In the left menu, click **URL Inspection**.
2. Type `https://www.autumnandwool.com/` and press Enter.
3. Read the result. Write down what it says: indexed, not indexed, or an error. Take a screenshot and save it to `business-os/seo-marketplace/geo-2026-11-25/` (name it `bing-home-inspection-2026-11-25.png`).
4. If there is a "Submit" or "Request indexing" option, click it once. Do not click it again the same day.

Note for owner: the sitemap you submit lists `/home` and does not list `/`. This is a known platform limit (see `business-os/seo-marketplace/2026-11-10-seo-reaudit.md`, finding 9). Do not change it yourself.

---

## Part 2. Ask Google to index key pages (Google Search Console)

Do this in Google Search Console for the property autumnandwool.com.

1. Open https://search.google.com/search-console and select the property.
2. At the top, paste the full page address into the search bar (for example `https://www.autumnandwool.com/wool-sweaters`). Press Enter. This opens **URL Inspection**.
3. Wait for the check to finish.
4. If it says **URL is on Google**, the page is already indexed. Do not request again. Go to the next URL.
5. If it says **URL is not on Google**, click **Request indexing**. Wait for the message "Indexing requested" or a similar confirmation. Then go to the next URL.
6. If it shows an error (for example "Blocked by robots" or "Not found 404"), do not request. Write the URL and the error in your notes and send them to the team.

Requests in this order (one at a time, same steps each):

| # | URL to paste | Type |
|---|---|---|
| 1 | https://www.autumnandwool.com/ | Home |
| 2 | https://www.autumnandwool.com/wool-sweaters | Category landing |
| 3 | https://www.autumnandwool.com/wool-cardigans | Category landing |
| 4 | https://www.autumnandwool.com/wool-sweater-vests | Category landing |
| 5 | https://www.autumnandwool.com/wool-hats-and-scarves | Category landing |
| 6 | https://www.autumnandwool.com/wool-gifts | Category landing |
| 7 | https://www.autumnandwool.com/how-to-wash-a-wool-sweater | Guide |
| 8 | https://www.autumnandwool.com/merino-vs-lambswool | Guide |
| 9 | https://www.autumnandwool.com/oversized-fit-guide | Guide |
| 10 | https://www.autumnandwool.com/how-to-choose-a-wool-cardigan | Guide |
| 11 | https://www.autumnandwool.com/about | About |

Daily quota:
- Google does not publish a number for the **Request indexing** button. The help page says there is "a daily limit to how many index requests you can submit."
- If you hit the limit, Search Console shows a quota message. Stop, and continue the next day from the first URL that was not done.
- Unverified: the URL Inspection API allows 2,000 inspections per property per day. That is a different tool and does not set the button limit.
- Plan: 11 URLs fit in one session. If the limit appears early, split the list over two days.

Sources: [About the URL Inspection tool, Google Search Console Help](https://support.google.com/webmasters/answer/9012289) (request indexing steps, daily-limit wording, timing "typically a day or so, but can take much longer"). [Google Search Console usage limits](https://developers.google.com/webmaster-tools/limits) (API figures only).

Do not request indexing for `/shop/...` pages in this round. The team is moving menu and page links to the `/wool-*` pages first (see the re-audit, SEO-51).

---

## Part 3. The 2-minute check (one week later, about 2 December 2026)

Do this once. Write the numbers in the table below and send them to the team.

**Google (2 minutes):**
1. In Search Console, open **Indexing > Pages**.
2. Read the number next to **Indexed**. Write it down. Baseline on 19 October was 11 of 37 known pages indexed.
3. Under **Why pages aren't indexed**, check for new reasons for the 11 URLs in Part 2. Note any with "Crawled – currently not indexed" or "Discovered – currently not indexed".

**Bing (2 minutes):**
1. Open https://www.bing.com and type: `site:autumnandwool.com`
2. Note the approximate result count shown at the top. Note which pages appear.
3. In Bing Webmaster Tools, open **Sitemaps** and note the indexed count for the sitemap.
4. Open the **Pages** or **Index** report (name may differ) and note the number of indexed pages.

Expected: some growth on both. Bing may show few or no results at first; that is normal for a new site. Do not panic; record and recheck in a month.

| Date | GSC indexed pages | GSC not indexed (top reason) | Bing site: count | Bing sitemap indexed | Notes |
|---|---|---|---|---|---|
| 2026-11-25 (today) | [FILL] | [FILL] | [FILL] | [FILL] | Before any request |
| 2026-12-02 | [FILL] | [FILL] | [FILL] | [FILL] | One week check |

---

## Owner actions
1. Import the site into Bing Webmaster Tools from Search Console (Part 1, steps 1–7).
2. Submit `https://www.autumnandwool.com/sitemap.xml` in Bing > Sitemaps.
3. Run URL Inspection in Bing on the home page; save the screenshot.
4. In Search Console, request indexing for the 11 URLs in Part 2, one at a time. Stop if the daily limit appears.
5. Send the results (which URLs said "already on Google", "requested", or error) to the team.
6. On 2 December, fill the table in Part 3 with the numbers.
7. Confirm the Search Console property type (Domain or URL prefix) so the team knows the exact site name to use.

## Sources
- Bing import from Google Search Console: https://blogs.bing.com/webmaster/september-2019/Import-sites-from-Search-Console-to-Bing-Webmaster-Tools
- Bing sitemaps, fetch timing and lastmod: https://blogs.bing.com/webmaster/July-2025/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search
- Google URL Inspection and Request indexing: https://support.google.com/webmasters/answer/9012289
- Google usage limits (API only): https://developers.google.com/webmaster-tools/limits
- Local: `business-os/seo-marketplace/2026-11-10-seo-reaudit.md` (finding 9, SEO-51), `business-os/seo-marketplace/geo-2026-11-25/CONTEXT.md`
