# Autumn & Wool — Squarespace implementation gate

Updated 18 October 2026. A native Squarespace draft was saved to **Redesign Preview (Hidden)**. The page remains **Disabled** and unpublished; the live homepage and commerce settings remain untouched.

## Implementation status

- Duplicated Home into **Redesign Preview (Hidden)** under **Not Linked**, URL slug `/redesign-preview`.
- The duplicate remains under **Not Linked**. It had been enabled during preview troubleshooting, which made the current homepage copy reachable at `/redesign-preview`. Disabled it again; settings show **Enable Page = off**, and a fresh public load returns Squarespace’s not-found page.
- Editor canvas now loads in the authenticated browser. Saved native edits: hero H1 “Warmth in every detail.”, supplied supporting copy, “Shop Knitwear” → `/shop`, “Our Story” → `/about`, story heading/body copy, and a “Shop by category” row with Cardigans → `/shop/cardigans`, Sweaters → `/shop/sweaters`, and Beanies & Hats → `/shop/beanies--hats`.
- Save is disabled after save; editor identifies the page as **Page · Disabled**. Publish was not used. Live homepage and checkout remain unchanged.
- Preview evidence: [desktop hero](/Users/eramadan/autumnandwool/evidence/redesign-preview-after-desktop.png), [mobile hero](/Users/eramadan/autumnandwool/evidence/redesign-preview-after-mobile.png), [desktop category row](/Users/eramadan/autumnandwool/evidence/redesign-preview-final-category.jpg), [mobile category stack](/Users/eramadan/autumnandwool/evidence/redesign-preview-final-mobile-category.jpg).
- Next: review the preview, then verify product-block selection and stock before any featured-product change. Keep the preview disabled until owner review.

## Access and current state

- Authenticated Squarespace editor is open for Autumn & Wool.
- Editor identifies the site as **Squarespace 7.1**. Website Pages, Site Styles, Products & Services, and Preview controls are available.
- The current Home page remains **Published** and unchanged. The **Redesign Preview (Hidden)** duplicate is in **Not Linked** and disabled; its public URL remains unavailable to visitors.
- Public pages checked: `/`, `/shop`, `/about`, `/shipping-returns`, `/faq`, `/size-guide`, `/contact`, and the three featured product pages.
- Current live baseline captured after responsive layout settled: [390×844 mobile](/Users/eramadan/autumnandwool/evidence/live-home-before-390.png) and [1440×900 desktop](/Users/eramadan/autumnandwool/evidence/live-home-before-1440.png). Both show the published “Wool Knitwear for Cooler Days” hero. Disabled-preview after views are above; mobile/desktop inspection was visual only, not a full viewport test suite.
- Shop page visibly lists products and also displays **“No results found”**. Reproduced on the public page.
- Current catalog contains repeated public titles, including two Pure Wool Side-Slit Sweaters and two Lambswool Raglan Crew listings. Product IDs/SKUs and full variant history were not compared, so no catalog merge is proposed.
- Existing featured prices verified on public pages: Long Wool Cardigan €145, Black Merino Wool Raglan Cardigan €160, Rib-Knit Beanie €45. Live inventory was not independently checked for these featured items in this pass.
- Product detail pages already use native Squarespace purchase controls, genuine color/size controls, and multiple product images. The Black Merino page has the requested four measurements plus an extra collar measurement. Long cardigan copy contains duplicated content and sustainability/certification claims whose evidence was not checked.
- Delivery page says Latvia shipping is free and international options appear at checkout. FAQ says returns are available for 14 days and exchanges require a new order; the full policy adds sale/custom-item exclusions and describes exchanges differently. Do not restate or change legal terms before owner/legal review.

## Proposed change table

| ID | Native setting/editor block or scoped CSS | Current value | Proposed change | URL | Before/after evidence | Test | Status / risk |
|---|---|---|---|---|---|---|---|
| H1 | Hidden preview hero blocks | Existing “Wool Knitwear for Cooler Days” | H1 “Warmth in every detail.”; supplied subtitle; CTAs “Shop Knitwear” → `/shop`, “Our Story” → `/about`; retained site image | `/redesign-preview` | [Desktop](/Users/eramadan/autumnandwool/evidence/redesign-preview-after-desktop.png), [mobile](/Users/eramadan/autumnandwool/evidence/redesign-preview-after-mobile.png) | Visual desktop/mobile check; exact text and CTA targets confirmed in editor | Saved in disabled preview. Theme renders the H1 uppercase. Eyebrow not added. |
| NAV | Site header / navigation | Shop, About, Contact, Home; native cart visible | Shop, Our Story, Delivery & Returns, Contact; keep Squarespace cart and logo-home link | Site-wide | Before captured in editor; after requires preview | Verify all targets and cart at desktop/mobile | Proposed for hidden preview. Not applied; editor canvas is blank. |
| CAT | Hidden preview native section | No category links | Add native buttons: Cardigans → `/shop/cardigans`, Sweaters → `/shop/sweaters`, Beanies & Hats → `/shop/beanies--hats` | `/redesign-preview` | [Category row](/Users/eramadan/autumnandwool/evidence/redesign-preview-final-category.jpg) | Link paths checked against existing Squarespace categories; collection results not audited | Saved in disabled preview. Existing Beanies & Hats category represents the prototype’s accessories shortcut. |
| SKU | Native product blocks | Vest (€126), hat/scarf set (€110), cardigan (€145) in first group; beanie (€45) below story | Prototype calls for Long Wool Cardigan, Black Merino Cardigan, Beanie; verify catalog/stock and block selection before changing | `/redesign-preview` | Product blocks unchanged | Confirm title, price, image, URL, stock before block edits | Not changed. Avoid catalog or listing mutations. |
| STORY | Hidden preview section | Existing story heading/body | “Behind every stitch.”, factual craftsmanship description, “Meet Autumn & Wool →” → `/about` | `/redesign-preview` | [Desktop preview](/Users/eramadan/autumnandwool/evidence/redesign-preview-after-story.png) | Copy and link confirmed in editor | Saved. |
| PDP | Native product detail content | Black cardigan has verified measurements but only a short summary; all three PDPs have native purchase controls. Long cardigan has duplicated content and sustainability/certification claims. | Use supplied concise Black Merino description; organize accurate content under Details & Materials, Size & Fit, Delivery & Returns, Care Instructions; add neutral delivery/returns/sizing links near native purchase control; keep native variants and cart behavior | Three featured product URLs | Product text inspected; no screenshot file saved | Confirm options, measurements and link destinations; keyboard access; no order submission | Proposed in preview only. Claims need factual review; no checkout/variant changes. |
| TRUST | Native text/link blocks | No homepage trust strip; shop has shipping, returns, response-time claims | Add neutral shipping, sizing and policy links only after checking exact policy wording; no refund-rule edits | `/`, `/shipping-returns` | No after screenshot | Compare text against live checkout settings and policy | Blocked on owner/legal confirmation of returns wording. |
| POLICY | Native page content | Shipping & Returns and FAQ differ on exchange process and item exclusions; About and Size Guide include sustainability/certification/handmade claims | Reconcile only after merchant/legal decision and supplier evidence; make no policy or certification edits in this pass | `/shipping-returns`, `/faq`, `/about`, `/size-guide` | Public copy inspected | Cross-check statements against approved policy and supplier records | Blocked on owner/legal and supplier confirmation. |
| NEWS | Existing footer signup | “Sign up to receive news and updates.” Native email field and Sign Up | Keep existing native signup; update copy only after verifying consent, privacy notice, list integration, and success state | Site-wide | No after screenshot | Submit only in a controlled test list; verify consent and confirmation | Blocked on newsletter integration/consent verification. |
| SHOP | Native store page | Real products plus a visible “No results found” message | Reproduce on a clean public load, then correct with supported Squarespace controls if possible | `/shop` | Public page captured by web inspection | Reload unfiltered shop; apply/remove a category; confirm state follows results | Defect reproduced; fix not attempted pending confirmation of safe editor workflow. |

## Not in this change

- No checkout, price, stock, product IDs, variants, shipping rules, or return conditions changes.
- No duplicate products removed or renamed without SKU/photo/variant comparison.
- No production publication, order, newsletter submission, or payment was made.
- Site Styles controls are available; existing style values and Custom Code contents were not inspected.
- The supplied ZIP remains an offline visual/behavior reference; its SVGs and demo bag/newsletter are not production assets or commerce controls.

## Rollback and release

Before edits: establish a duplicate/unlinked preview page or another verified rollback path and capture the current 390px/1440px views. If Squarespace offers no isolated preview, get approval for each live page save. Keep the native cart, product data, and checkout untouched. Do not publish or deploy until the owner approves the completed preview and the policy/newsletter checks pass.
