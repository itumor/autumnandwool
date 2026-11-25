# Live public baseline before Latvian rollout — 2026-11-25

Read-only public reconnaissance via `curl`/HTTP only. No login, no browser, no live edits.
Fetched ~17:55 UTC 2026-11-25. Every fact below has a URL or exact snippet; inference is marked separately.

## Fact table

| Check | Verified result | Source |
|---|---|---|
| `<html lang>` | `en-US` | `https://www.autumnandwool.com/` |
| Canonical | `<link rel="canonical" href="https://www.autumnandwool.com"/>` (no trailing slash) | homepage |
| `hreflang` | 0 in HTML; 0 `xhtml:link` in sitemap | homepage + sitemap.xml |
| `<title>` | `Autumn & Wool \| Wool sweaters and cardigans from Riga` | homepage |
| Meta description | `Oversized sweaters, long cardigans and soft accessories in merino and wool, from our studio in Riga, Latvia. Size guide, care tips and free shipping.` | homepage |
| Weglot present | 0 case-insensitive `weglot` matches in HTML or custom.css | homepage + custom.css |
| Native language picker | markup present, `"enabled": false`, empty `languageFlags` | homepage header section |
| Squarespace i18n flag | `i18n_beta_website_locales` listed in `betaFeatureFlags` | homepage Static context |
| Overlay guard | both selectors present with `pointer-events:none !important;` **in custom.css only** | versioned `custom.css` URL below |
| `robots.txt` | 200; `Sitemap: https://www.autumnandwool.com/sitemap.xml` | robots.txt |
| `sitemap.xml` | 200; 49 `<loc>` total, 30 shop-prefixed (1 `/shop`, 7 subcategories, 22 products: 2 `/shop/p/`, 20 `/shop/p/p/`); no locale-prefixed URLs | sitemap.xml |
| Latvian / Russian copy | 0 Cyrillic on `/`, `/about`, `/shop`, `/size-guide`, `/faq`, `/contact`; footer `Rīga, LV-1035, Latvia`; "Latvian" only in product-tag metadata | those pages |
| Main URL status | `https://www.autumnandwool.com/` → 200, 0 redirects; `http://…` → 200 after 1 hop to https; `https://autumnandwool.com/` → 200 after 1 hop to www | curl -L |

## Exact evidence snippets

Homepage head (`https://www.autumnandwool.com/`):

```html
<html xmlns:og="http://opengraphprotocol.org/schema/" xmlns:fb="http://www.facebook.com/2008/fbml" lang="en-US"  >
<title>Autumn &amp; Wool | Wool sweaters and cardigans from Riga</title>
<link rel="canonical" href="https://www.autumnandwool.com"/>
<meta name="description" content="Oversized sweaters, long cardigans and soft accessories in merino and wool, from our studio in Riga, Latvia. Size guide, care tips and free shipping." />
```

Grep: `weglot` = 0, `hreflang` = 0.

Native language-picker hook (disabled):

```html
data-section-id="header"
data-header-style="dynamic"
data-language-picker="{
  &quot;enabled&quot;: false,
  &quot;iconEnabled&quot;: false,
  &quot;iconType&quot;: &quot;globe&quot;,
  &quot;flagShape&quot;: &quot;shiny&quot;,
  &quot;languageFlags&quot;: [ ]
}"
```

Header/nav hosts for a future switcher: `<header data-test="header" id="header">`, `data-section-id="header"`,
`nav.header-nav-list`, duplicate mobile nav, `data-test="header-menu"`.

Load-bearing CSS guard — `https://static1.squarespace.com/static/custom-css/6908755e4a17f81b7629f4bc/6908755e4a17f81b7629f4c5/24/custom.css` (HTTP 200, line 3):

```css
.sqs-widgets-confirmation-overlay{pointer-events:none !important}.sqs-widgets-confirmation{pointer-events:none !important}
```

Important: versioned `site.css` has the base selectors **without** the guard
(`.sqs-widgets-confirmation-overlay{…z-index:999999}`), and `static.css` has no confirmation selectors.
The click-trap fix lives **only in custom.css**. Verifying `site.css` alone is not sufficient.

Footer (`homepage` line ~3216):

```html
© 2026 AUTUMN AND WOOL, SIA · Reg. no. 40203644965 · Braslas iela 22d, Rīga, LV-1035, Latvia · autumnandwool@gmail.com
```

"Latvian" appears in `/shop` only inside a `data-context` JSON attribute (`latvian ornament(s)` product tags), not visible copy.

## Inference — not verified as intent or capability

- No translation layer and no hreflang/locale URL structure exist today; the public surface is greenfield for EN→LV.
- Squarespace's language-picker markup exists but is disabled, and `i18n_beta_website_locales` appears in beta flags.
  This does **not** prove the feature is enabled, usable on this plan, or configured for Latvian.
- The two-selector Custom CSS guard is load-bearing; any CSS change must preserve both declarations verbatim.
- 20 of 22 products use the legacy `/shop/p/p/…` URL pattern; a locale URL architecture must account for it.

## Not verified here (requires admin or later live state)

- Whether Site Languages → Weglot Connect is available on the current plan.
- Weglot word count and plan price.
- GSC queries by country/language, and LV traffic baseline.
- Switcher styling/behaviour after Weglot is connected.
