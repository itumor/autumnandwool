# UTM and attribution scheme v1   Status: DRAFT for owner approval (master plan C15: approve by 31 Oct)

Written 2026-10-21 by aw-growth-marketing (skill `aw-utm-attribution`). One taxonomy for every department.
Links live in `utm-links.csv` (status `draft` until the owner pastes them live). Nothing here is live.

## 1. Facts this rests on
- Orders and revenue: **Squarespace Orders** (+ Etsy). GA4 `G-7TV8PK060Z` = sessions and source/medium only,
  no purchase events (Code Injection plan-gated).
- So GA4 can say which link brings visitors, not which link sells. Per-sale credit needs a code, a name match in
  Squarespace Orders, or a customer answer ("How did you hear about us?").
- Discount codes and per-code reports on the current plan: UNVERIFIED (owner decision 11, 28 Oct). Until then
  **no codes are issued** (master ruling C6).

## 2. Rules
1. Lowercase, words joined by hyphens. No spaces, no underscores, no names/emails/order IDs.
2. Always `utm_source`, `utm_medium`, `utm_campaign`. `utm_content` separates variants.
3. Never put UTMs on internal links (site menu, buttons, product grids).
4. Check the landing URL loads and the query string survives any shortener before it goes live.
5. One namespace per department (section 4) so creator, paid and organic never share a link.

## 3. Taxonomy
| Placement | utm_source | utm_medium | utm_campaign | utm_content | GA4 channel (default rules) |
|---|---|---|---|---|---|
| Bio links (keep exactly, owner pack C) | instagram / tiktok / facebook / pinterest | social | bio-link | none | Organic Social |
| Etsy to site | etsy | marketplace | move-to-site | none | Referral/Unassigned [VERIFY in GA4] |
| Organic post or pin | platform | social | `<theme>-<yyyy>` or `<theme>-<yyyy-mm>`; standing series without date. Registered: `autumn-2026`, `gift-2026`, `making-in-riga`, `mareshop-story` | `<format>-<sku-slug>` (e.g. `pin-beanie`) or Creative's script ID (e.g. `vs-2026-10-21-a`) | Organic Social |
| Meta ad | facebook or instagram | paid-social | test slug from the brief | concept letter or `{{ad.name}}` | Paid Social |
| Google Ads | none (auto-tagging gclid on) | | | | Paid Search / Shopping |
| Merchant Center free listings | none | | | | Organic Shopping |
| Creator (Partnerships) | `creator-<handle>` | affiliate | `gifting-<yyyy-mm>` / `affiliate-<yyyy-mm>` | `<platform>-<format>` | Affiliates |
| Email (MailerLite, CX) | mailerlite | email | `<flow-or-issue>-<yyyy-mm>` | `<link-position>` | Email |
| Market / print / parcel QR | qr | offline | `<event-slug>-<yyyy>` | `<card-type>` | Unassigned [VERIFY]; read by campaign |
| Press and gift guides (new, proposed) | `<outlet>` e.g. `neighborhood-lv` | referral | `gift-guide-<yyyy>` or `press-<yyyy>` | `editor-link` | Referral |

Press note: editors often drop UTMs. GA4 still records the referring hostname, so read both the tagged sessions and
`session source` = outlet domain. Pitches stay on hold until G4/G5 clear (master C12).

## 4. Namespaces (so creator and paid tests never share codes or links)
| Owner dept | utm_source / medium it may use | Code prefix (only if codes become possible) |
|---|---|---|
| Growth (paid) | facebook, instagram, google (auto) / paid-social | none planned; paid tests are read by UTM + order timing |
| Partnerships | `creator-<handle>` / affiliate | `HANDLE10` style, one per creator, size set by FIN margin check (PAR plan D5) |
| Creative / SEO (organic) | platform / social | none |
| CX (email) | mailerlite / email | none |
| Markets / OPS | qr / offline | `<EVENT>` code only if owner wants one, after margin check |
| Press | `<outlet>` / referral | none |

If a paid ad and a creator post ever feature the same SKU in the same week, the readout lists both and credits
neither alone.

## 5. Conflicts found (proposals to fix, not edits)
| File | Current | Proposed | Owner of file |
|---|---|---|---|
| `campaign-assets/campaign-drafts.md` | `utm_medium=organic_social`, `winter_knitwear`, `hat_scarf` | Creative's provisional fix adopted as final: `social`, `autumn-2026`, `pin-hat-scarf-set` (`utm-fix-campaign-drafts-2026-10-21.md`) | Creative |
| `campaign-assets/drafts/plan-wave1/captions-2026-10-21.md` | some rows show only `campaign=` and `utm_content=` | add `utm_source=<platform>&utm_medium=social` | Creative |
| `plans/2026-2027/customer-experience.md` row "Growth / SEO" | `utm_campaign=<flow>_<n>` (underscore) | `utm_campaign=<flow>-<yyyy-mm>`, e.g. `welcome-2026-11`; position in `utm_content` | CX |
| `campaign-assets/welcome-email-draft.md` | links to `/shop`, `/size-guide` with no UTM | rows `email-welcome-*` in `utm-links.csv` | CX |

## 6. Post-purchase source question (proposal for Q1 2027, owner decision 8 in growth plan)
Field label: "How did you hear about Autumn & Wool?" Pick-list: Instagram · TikTok · Pinterest · Google search ·
Google Shopping · Etsy / Mareshop · Friend or family · Christmas market · Article or gift guide · Creator or
blogger · Other (text). Feasibility of a checkout field on the current plan: UNVERIFIED (CRO to check). Fallback:
one question in the post-purchase email (CX).

## 7. Readout rule
Source of truth = Squarespace Orders. Show "platforms claim N, we can verify M". Never add platform conversions
together. Never call a channel "not working" from GA4 alone while purchase events are missing. Direct/branded
traffic hides word of mouth, markets and creators; name that blind spot.
