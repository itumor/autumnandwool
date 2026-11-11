# Images and visual findings — autumnandwool.com — 2026-11-10 re-audit

Source: the seo-visual specialist captured the 20 screenshots in `../screenshots/` (desktop 1440 and mobile 390, fold and full page, first visit, cookie banner not dismissed) and then hit its turn limit before reporting. The alt-text counts and the screenshot review below were done by the manager session from the shared crawl (`../crawl/`, 49 pages, 17:10 EET).

## Image alt text (all 49 pages, raw HTML)

| Measure | Morning | Now |
|---|---|---|
| `<img>` tags | not recorded | 1,462 |
| Missing alt attribute | not recorded | 0 |
| Empty alt | not recorded | 9 |
| Alt that is a file name (`image_1.jpg`, `ChatGPT Image…`) | 115 | 0 |
| Alt over 125 characters | 84 | 0 |
| Repeated alt within a page | not recorded | 721 (mostly the same gallery image at several sizes, plus header/footer logos) |
| `loading="lazy"` | not recorded | 497 of 1,462 |

Social preview image (home `og:image`): still 1024 × 1536 portrait PNG, served over `http://`.

## Screenshot review (mobile 390 px, first visit)

| ID | Severity | Finding | Evidence |
|---|---|---|---|
| V-01 | High | Cookie banner is about 150 px tall at the bottom of the screen on every page. On the product page it covers the lower part of the product title; price and Add To Cart are below the first screen regardless, because the photo fills it. | `product-mobile-fold.png` |
| V-02 | Medium | `/wool-sweaters` on mobile: the first screen is the heading plus one long paragraph. No product, photo or price is visible before scrolling. | `wool-sweaters-mobile-fold.png` |
| V-03 | Info | Home mobile first screen is clear: label, heading, one sentence, two buttons. No horizontal overflow seen on the four mobile pages viewed. | `home-mobile-fold.png` |
| I-01 | Medium | Social preview image is portrait; link previews crop it. | home `og:image` tags |
| I-02 | Low | 721 repeated alts within pages. Low risk: same image, several renditions. | crawl count |

Not done: tap-target measurement, desktop screenshot review, per-image file size (see `performance.md` for image weight per page).

Images score: 78 / 100 (manager's judgement: alt text fixed sitewide; preview image and mobile banner remain).
