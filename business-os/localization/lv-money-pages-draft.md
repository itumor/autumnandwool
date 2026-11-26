# DRAFT — native Latvian review required before publication

English → Latvian copy pack for the Weglot money-page pass (LOC-08 / LOC-09 prep).
Compiled 2026-11-25 from repo sources only. **Nothing here is applied to the live site.** No native Latvian reviewer has been named (gate G3 / CRE-23) and the EU adviser answer on returns wording has not landed (PRD-19 / G4). Do not paste any block below into Weglot as a published translation until both gates close.

Claim rules applied from `.claude/skills/aw-brand-voice/SKILL.md` §3 (hard gate). Status key: **LIVE** = text captured from the public site and stored in `evidence/`; **DRAFT** = repo proposal, not published; **UNVERIFIED** = no source text available.

Lifecycle values in §3 start at `translation-draft`; the native reviewer moves each row to `review` and then `localized-ready`. A row carrying `[PENDING ADVISER]` or `[VERIFY: …]` cannot be promoted past `translation-draft` until that gate closes.

---

## 1. Source map — where each English block came from

| Page / block | Exact repo source | Status | Note |
|---|---|---|---|
| Home `/` | `evidence/seo-audit-2026-11-10/after/crawl/html/https-www-autumnandwool-com.html` | LIVE | Public-site crawl snapshot, 2026-11-10, post-audit state |
| About `/about` | `evidence/seo-audit-2026-11-10/after/crawl/html/https-www-autumnandwool-com-about.html` | LIVE | Held origin claim (§4) |
| Shipping & returns `/shipping-returns` | `evidence/seo-audit-2026-11-10/after/crawl/html/https-www-autumnandwool-com-shipping-returns.html` | LIVE | Legal lines flagged `[PENDING ADVISER]` |
| FAQ `/faq` | `evidence/seo-audit-2026-11-10/after/crawl/html/https-www-autumnandwool-com-faq.html` | LIVE | Returns Q&As flagged `[PENDING ADVISER]` |
| Size guide `/size-guide` | `evidence/seo-audit-2026-11-10/after/crawl/html/https-www-autumnandwool-com-size-guide.html` | LIVE | Chart numbers reproduced unchanged |
| P1 Merino Wool Raglan Cardigan | `evidence/seo-audit-2026-11-10/after/crawl/html/*black-merino-wool-cardigan-*cardigan-1.html` | LIVE | Filename glob used deliberately; full name locked in §2 |
| P2 Merino Wool Raglan Sweater – Dusty Pink | `evidence/seo-audit-2026-11-10/after/crawl/html/*merino-wool-raglan-sweater-dusty-pink-oversized-jumper.html` | LIVE | Filename glob used; full name locked in §2 |
| P3 Women's Classic Lambswool Crew Sweater | `evidence/seo-audit-2026-11-10/after/crawl/html/*lambswool-sweater-womens-grey-knit-jumper.html` | LIVE | Filename glob used; full name locked in §2 |
| P4 Merino Wool Hat & Scarf Set | `evidence/seo-audit-2026-11-10/after/crawl/html/https-www-autumnandwool-com-shop-p-p-merino-wool-hat-scarf-set-extra-fine-rib-knit-soft-on-skin-warm-not-bulky-unisex-gift.html` | LIVE | |
| P5 Merino Rib-Knit Beanie – Unisex | `evidence/seo-audit-2026-11-10/after/crawl/html/https-www-autumnandwool-com-shop-p-p-merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1.html` | LIVE | |
| Priority-PDP list (P1–P5) | `business-os/head-of-ecommerce/min-contribution-assumed-2026-10-21.md` (P1–P5 table); `plans/2026-2027/status/head-of-ecommerce.md` GM-12 ("keep the 5, no swap") | DRAFT | Provisional per master-plan C5 / gate G5; assumed costs |
| Site-wide fact sheet | `llms.txt` (lines 1–14) | LIVE | Repo copy of public `/llms.txt`; cross-check only |
| Claim rules | `.claude/skills/aw-brand-voice/SKILL.md` §3 | LIVE | Hard gate applied to every LV row |
| Replacement returns wording | `business-os/operations/returns-wording-draft-wave3.md` | DRAFT | Assumption-based; not publishable |
| PRD-19 adviser answer | — | UNVERIFIED | Legal lines stay `[PENDING ADVISER]` |
| Native LV reviewer name | — | UNVERIFIED | `[FILL]` owner gate G3 |
| Live text as of 2026-11-25 | — | UNVERIFIED | Snapshots dated 2026-11-10; re-read before publication |

---

## 2. Locked glossary — do not machine-translate or alter these values

| Term | Exact source / approved value | Handling in Latvian copy |
|---|---|---|
| Brand | `Autumn & Wool` | Keep verbatim, including `&` |
| Trading entity | `AUTUMN AND WOOL, SIA`, reg. `40203644965` | Keep verbatim if used |
| Etsy shop | `Mareshop`; `etsy.com/shop/Mareshop` | Keep verbatim |
| Etsy proof — only approved line | `Formerly Mareshop on Etsy, 4.9★ from 1,400+ customers` | Use this rendering only; `4.9★` and `1,400+` locked; "customers", not "reviews"; label as marketplace history. No other proof phrasing is approved. |
| Etsy sales line | `8,000+ orders over 15 years on Etsy` | Numerals locked; never imply direct-store volume |
| Contact email | `autumnandwool@gmail.com` | Keep verbatim |
| Social handle | `@autumnandwool` | Keep verbatim |
| Maker's name | `Kristine` | Keep source spelling (do not convert to `Kristīne`) |
| Process — only approved phrase | `knitted on manual machines and finished by hand in Riga` | LV: `adīts uz manuālām adāmmašīnām un pabeigts ar rokām Rīgā`. Bare process variants are restricted — see §4. |
| Fibre content | Exact wording on **that** product's live page, e.g. `100% merino wool`, `100% pure new wool`, `100% lambswool`, `100% extra-fine merino wool, Italian-spun yarn` | Copy per PDP; never generalise ("all our knits are merino/wool") |
| Product names | `Merino Wool Raglan Cardigan`; `Merino Wool Raglan Sweater - Dusty Pink`; `Women's Classic Lambswool Crew Sweater`; `Merino Wool Hat & Scarf Set`; `Merino Rib-Knit Beanie - Unisex` | Locked proper names; do not translate |
| Sizes | `S`, `M`, `L`, `XL`, `S/M`, `L/XL`, `one size`; `EU 36–42`, `UK 8–14`, `US 6–12` | Labels and numerals locked |
| Prices | `€160.00`, `€155.00`, `€136.00`, `€110.00`, `€45.00`, `€145`, `€126` | Keep exact string (do not convert to `160,00 €`); from live page on publication day |
| Delivery — only approved promises | dispatch `2–5 working days`; Europe `about 5–10 working days`; US/CA/AU `7–20`; `Free shipping to eligible destinations`; `14-day returns` | No other delivery or return promise; legal lines `[PENDING ADVISER]` |
| Measurements | e.g. `61 cm / 24.02 in`, `54–58 cm`, `190 × 36 cm` | Numerals, units and separators unchanged |

---

## 3. Draft Latvian copy (blocks actually sourced)

`[PENDING ADVISER]` = returns/withdrawal/legal wording, do not publish. `[VERIFY: …]` = fact missing or conflicting with the approved brand line. `[HOLD]` = held source claim, see §4.

### 3.1 Home `/`

| EN source (snapshot) | LV draft | Lifecycle |
|---|---|---|
| `Knitted in Riga, Latvia` | `Adīts Rīgā, Latvijā` | translation-draft |
| `Wool knitwear for cooler days` | `Vilnas trikotāža vēsākām dienām` | translation-draft |
| `Oversized sweaters, long cardigans and soft accessories in merino and wool — each piece knitted on a manual machine and finished by hand.` | `Oversized svīteri, gari kardigāni un mīksti aksesuāri no merino un vilnas — katrs izstrādājums ir adīts uz manuālām adāmmašīnām un pabeigts ar rokām Rīgā.` [VERIFY: live page says "in Riga"/"Latvia" inconsistently; approved process phrase fixes Riga] | translation-draft |
| `Shop the collection →` / `Our story` | `Skatīt kolekciju →` / `Mūsu stāsts` | translation-draft |
| `4.9 ★★★★★ from 1,400+ reviews on Etsy` | `Bijusi Mareshop vietnē Etsy, 4.9★ no 1,400+ klientiem.` [VERIFY: live strip says "reviews"; approved line says "customers"] | translation-draft |
| `Machine-knitted, hand-finished` / `Manual machine knit, hand-sewn in Riga` | `Adīts uz manuālām adāmmašīnām un pabeigts ar rokām Rīgā` (one approved phrase replaces both source chips) | translation-draft |
| `Free shipping — Latvia, US & many more countries` | `Bezmaksas piegāde uz atbalstītajiem galamērķiem` [VERIFY: exact eligible-destination list from checkout] | translation-draft |
| `14-day returns — Easy, no-fuss exchanges` | `Atgriešana 14 dienu laikā [PENDING ADVISER] — Vienkārša apmaiņa [PENDING ADVISER]` | translation-draft |
| `Loved since Mareshop — 4.9 from 1,400+ reviews on Etsy` | `Iecienīti kopš Mareshop — 4.9★ no 1,400+ klientiem` [VERIFY: align to approved proof line] | translation-draft |
| `Bestsellers` / `View all pieces` | `Labākie pārdošanā` / `Skatīt visus izstrādājumus` | translation-draft |
| `Long Wool Cardigan €145` / `Oversized Wool Raglan Sweater €155` / `Merino Wool Raglan Sweater €155` / `Oversized Merino V-Neck Vest €126` | Nosaukumi un cenas nemainīti (§2); tulko tikai virsrakstu `Bestsellers`. | translation-draft |
| `Made slowly, by one pair of hands` | `Veidots lēnām — viena cilvēka rokās` [VERIFY: founder line needs owner's own words per §3] | translation-draft |
| `Every Autumn & Wool piece is designed by Kristine, knitted on a manual knitting machine and hand-sewn in our small studio in Riga, Latvia.` | `Katru Autumn & Wool izstrādājumu izstrādā Kristine; tas ir adīts uz manuālām adāmmašīnām un pabeigts ar rokām Rīgā.` | translation-draft |
| `For 15 years you may have known us as Mareshop on Etsy — 8,000+ orders and 4.9 from 1,400+ reviews on Etsy.` | `15 gadus jūs, iespējams, pazināt mūs kā Mareshop vietnē Etsy — 8,000+ pasūtījumi 15 gados vietnē Etsy un 4.9★ no 1,400+ klientiem.` | translation-draft |
| `Meet the maker` / `Worn on cooler days` / `FOLLOW US ON INSTAGRAM` | `Iepazīstiet radītāju` / `Valkāts vēsākās dienās` / `SEKOJIET MUM INSTAGRAMĀ` | translation-draft |

### 3.2 About `/about`

| EN source (snapshot) | LV draft | Lifecycle |
|---|---|---|
| `Every stitch tells a story of patience and purpose` | `Katrs dūriens stāsta par pacietību un mērķi` | translation-draft |
| `Autumn & Wool is a small knitwear studio in Riga, Latvia. Kristine designs every piece, inspired by a family tradition of knitting.` | `Autumn & Wool ir maza trikotāžas studija Rīgā, Latvijā. Kristine izstrādā katru izstrādājumu, iedvesmojoties no ģimenes adīšanas tradīcijas.` [VERIFY: family-history claim needs owner's own words per §3] | translation-draft |
| `15 years as Mareshop on Etsy` / `8,000+ orders on Etsy` | `15 gadi kā Mareshop vietnē Etsy` / `8,000+ pasūtījumi 15 gados vietnē Etsy` | translation-draft |
| `4.9★ from 1,400+ reviews on Etsy` | `Bijusi Mareshop vietnē Etsy, 4.9★ no 1,400+ klientiem` | translation-draft |
| EN stat line 4 (origin claim) | `[HOLD]` — exact held phrase in §4; no LV version until brand/adviser verification. | translation-draft |
| `How each piece is made` | `Kā top katrs izstrādājums` | translation-draft |
| EN process paragraph (held origin claim + fibre generalisation) | `[HOLD]` — see §4. First sentence only: `Šeit nekas nenāk no konveijera.` [VERIFY: fibre wording must be copied per PDP] | translation-draft |
| `1 Designed by Kristine in the Riga studio` | `1 Izstrādājusi Kristine Rīgas studijā` | translation-draft |
| `2 Knitted on a manual knitting machine` | `2 Adīts uz manuālām adāmmašīnām` | translation-draft |
| `3 Hand-sewn and finished, seam by seam` | `3 Pabeigts ar rokām, šuve pa šuvei` [VERIFY: source "hand-sewn" → approved "finished by hand"] | translation-draft |
| `4 Washed and pressed before it ships to you` | `4 Mazgāts un gludināts pirms nosūtīšanas` | translation-draft |
| `What we promise` | `Mūsu solījumi` | translation-draft |
| `Quiet design — Understated colours and relaxed shapes you'll wear for many autumns.` | `Kluss dizains — Atturīgas krāsas un brīvas formas, ko valkāsi daudzos rudenī.` | translation-draft |
| `Honest information — Clear details on materials, measurements and care for every product.` | `Godīga informācija — Skaidras ziņas par materiāliem, izmēriem un kopšanu katram izstrādājumam.` | translation-draft |
| `Natural yarns — Merino, lambswool and pure new wool — the exact fibre listed on each page.` | `Dabīgas dzijas — precīzs šķiedru sastāvs norādīts katras preces lapā.` [VERIFY: do not generalise fibre; no site-wide fibre claim] | translation-draft |
| `Find a knit for cooler days` / `Explore the collection` / `Say hello` | `Atrodi adījumu vēsākām dienām` / `Skatīt kolekciju` / `Sveiki` | translation-draft |

### 3.3 Shipping & returns `/shipping-returns`

| EN source (snapshot) | LV draft | Lifecycle |
|---|---|---|
| `Shipping & returns` | `Piegāde un atgriešana` | translation-draft |
| `Every order is packed by hand in our Riga studio and sent with tracking.` | `Katrs pasūtījums tiek iepakots ar rokām mūsu Rīgas studijā un nosūtīts ar izsekošanu.` | translation-draft |
| `Shipping cost: Free — Latvia, the US & destinations shown at checkout` | `Piegādes izmaksas: bezmaksas uz atbalstītajiem galamērķiem` [VERIFY: eligible-destination list] | translation-draft |
| `Leaves Riga in: 2–5 days — Working days, in-stock items` | `Nosūtīšana no Rīgas: 2–5 darba dienas — noliktavā esošās preces` | translation-draft |
| `Europe: 5–10 days — Estimated working days` | `Eiropa: aptuveni 5–10 darba dienas` | translation-draft |
| `USA, Canada, Australia: 7–20 days — Estimated delivery` | `ASV, Kanāda, Austrālija: 7–20 dienas` | translation-draft |
| `Delivery times are estimates, not guarantees. Taxes and duties for orders outside the EU are explained in the FAQs.` | `Piegādes laiki ir aplēses, nevis garantijas. Nodokļi un muitas maksājumi pasūtījumiem ārpus ES ir skaidroti bieži uzdotajos jautājumos. [PENDING ADVISER]` | translation-draft |
| `Returns & exchanges` | `Atgriešana un apmaiņa [PENDING ADVISER]` | translation-draft |
| `Unworn, unused items can be returned within 14 days of delivery.` | `Nevalkātus, neizmantotus izstrādājumus var atgriezt 14 dienu laikā no piegādes. [PENDING ADVISER]` | translation-draft |
| `1 Email us — Send your order number and reason to autumnandwool@gmail.com.` | `1 Rakstiet mums — Nosūtiet pasūtījuma numuru un iemeslu uz autumnandwool@gmail.com. [PENDING ADVISER]` | translation-draft |
| `2 Send it back — Original condition and packaging, by a tracked method.` | `2 Nosūtiet atpakaļ — Sākotnējā stāvoklī un iepakojumā, ar izsekojamu sūtījumu. [PENDING ADVISER]` | translation-draft |
| `3 Get your refund — Within 7 business days after we receive and approve it. Shipping costs not included.` | `3 Saņemiet atmaksu — 7 darba dienu laikā pēc apstiprināšanas. Piegādes izmaksas netiek iekļautas. [PENDING ADVISER]` | translation-draft |
| `Prefer an exchange? Place a new order for the size or colour you prefer, return the original within 14 days, and we refund the first purchase.` | `Vēlaties apmainīt? Veiciet jaunu pasūtījumu vēlamajā izmērā vai krāsā, atgrieziet sākotnējo izstrādājumu 14 dienu laikā, un mēs atmaksāsim pirmo pirkumu. [PENDING ADVISER]` | translation-draft |
| `Non-returnable items: Custom or made-to-order pieces; Gift cards; Sale or discounted items, unless faulty` | `Neatgriežami: pēc pasūtījuma izgatavoti izstrādājumi; dāvanu kartes; preces ar atlaidi, ja vien tās nav bojātas. [PENDING ADVISER]` | translation-draft |
| `Return shipping — You cover return postage unless the item arrived damaged or incorrect. Please use a tracked service — parcels lost in transit can't be refunded.` | `Atgriešanas piegāde — postu apmaksājat jūs, ja vien izstrādājums nav ieradies bojāts vai nepareizs. Izmantojiet izsekojamu sūtījumu. [PENDING ADVISER]` | translation-draft |
| `Damaged or faulty? Contact us within 5 days of delivery with photos. We'll offer a replacement, repair or refund.` | `Bojāts vai ar defektu? Sazinieties ar mums 5 dienu laikā no piegādes, pievienojot foto. [PENDING ADVISER]` | translation-draft |
| `Each piece is machine-knitted and hand-finished, so slight variations in texture or colour are normal and part of its character.` | `Katrs izstrādājums ir adīts uz manuālām adāmmašīnām un pabeigts ar rokām Rīgā, tāpēc nelielas tekstūras vai krāsas atšķirības ir normālas.` | translation-draft |
| `Need help with an order? We're in Riga, Latvia, and reply within 1–2 business days.` / `Contact us` | `Vajadzīga palīdzība ar pasūtījumu? Mēs esam Rīgā, Latvijā, un atbildam 1–2 darba dienu laikā.` / `Sazinieties ar mums` | translation-draft |

### 3.4 FAQ `/faq`

| EN source (snapshot) | LV draft | Lifecycle |
|---|---|---|
| `Questions, answered` | `Atbildes uz jautājumiem` | translation-draft |
| `What payment methods do you accept? … All major credit and debit cards through our secure checkout. You will receive an order confirmation by email.` | `Kādus maksāšanas veidus pieņemat? Visas galvenās kredīt- un debitkartes caur mūsu drošo norēķinu sistēmu. Apstiprinājumu saņemsiet pa e-pastu.` | translation-draft |
| `How long does it take to process my order? In-stock items leave Riga, Latvia within 2–5 working days. Made-to-order items ship within the time shown on the product page.` | `Noliktavā esošās preces izceļo no Rīgas 2–5 darba dienu laikā. Pēc pasūtījuma izgatavotās — preces lapā norādītajā laikā.` | translation-draft |
| `What are your shipping times? Europe: about 5–10 working days. USA, Canada and Australia: 7–20 days. … Shipping is free to Latvia, the US and other destinations offered at checkout.` | `Eiropa: aptuveni 5–10 darba dienas. ASV, Kanāda, Austrālija: 7–20 dienas. Piegāde bez maksas uz atbalstītajiem galamērķiem.` [VERIFY: eligible destinations] | translation-draft |
| `Do I have to pay customs or taxes? … VAT included for EU … duties may apply outside the EU.` | `ES klientiem PVN ir iekļauts cenā. Ārpus ES var tikt piemēroti muitas vai importa nodokļi. [PENDING ADVISER]` | translation-draft |
| `What is your return policy? … 14 days … unworn, unwashed … Return shipping is paid by the customer unless the item is faulty.` | `Atgriešana 14 dienu laikā no piegādes nevalkātiem, nemazgātiem izstrādājumiem sākotnējā stāvoklī. [PENDING ADVISER]` | translation-draft |
| `Do you offer exchanges? Yes. Place a new order … return the original. We refund the first purchase once the return arrives.` | `Jā. Veiciet jaunu pasūtījumu vēlamajā izmērā vai krāsā un atgrieziet sākotnējo izstrādājumu. [PENDING ADVISER]` | translation-draft |
| `What materials do you use? Merino wool, lambswool or pure new wool. The exact fibre is listed on each product page.` | `Precīzs šķiedru sastāvs ir norādīts katras preces lapā.` [VERIFY: site-wide fibre list not approved; quote per PDP] | translation-draft |
| `How are your pieces made? Kristine designs each piece in Riga. It is knitted on a manual knitting machine in Latvia, then hand-sewn, finished, washed and pressed before shipping.` | `Kristine katru izstrādājumu izstrādā Rīgā. Tas ir adīts uz manuālām adāmmašīnām un pabeigts ar rokām Rīgā, pēc tam mazgāts un gludināts.` | translation-draft |
| `How should I care for my knitwear? Hand wash in cold water with a wool-safe detergent. Do not tumble dry — lay flat to dry. Store folded …` | `Mazgāt ar rokām aukstā ūdenī ar vilnai piemērotu līdzekli. Nelikt žāvētājā — žāvēt, izklājot plakani. Glabāt salocītu.` | translation-draft |
| `How do I choose the right size? … garment measurements … size guide … Email autumnandwool@gmail.com.` | `Katras preces lapā ir izstrādājuma izmēri, un izmēru ceļvedis paskaidro, kā tos salīdzināt ar ķermeņa izmēriem. Rakstiet uz autumnandwool@gmail.com.` | translation-draft |
| `Do you offer custom sizing? Not at the moment. Many of our pieces have relaxed silhouettes …` | `Pašlaik nē. Daudziem izstrādājumiem ir brīvas siluetes dažādiem ķermeņa tipiem.` | translation-draft |
| `How can I contact you? Email autumnandwool@gmail.com or @autumnandwool on Instagram. We usually reply within 1–2 business days.` | `Rakstiet uz autumnandwool@gmail.com vai @autumnandwool Instagramā. Parasti atbildam 1–2 darba dienu laikā.` | translation-draft |

### 3.5 Size guide `/size-guide`

| EN source (snapshot) | LV draft | Lifecycle |
|---|---|---|
| `Find your fit` | `Atrodi savu izmēru` | translation-draft |
| `Our knits are made in relaxed and oversized shapes. Use your body measurements to pick a size, then check the garment measurements on each product page.` | `Mūsu adījumi ir brīvās un oversized formās. Izvēlieties izmēru pēc ķermeņa izmēriem, pēc tam pārbaudiet izstrādājuma izmērus katras preces lapā.` | translation-draft |
| `01 Measure your body — Chest, waist and hips, over thin fitted clothing.` | `01 Izmēriet ķermeni — krūtis, viduklis un gurni pār plānu, pieguļošu apģērbu.` | translation-draft |
| `02 Find your size — Match your numbers to the body size chart below.` | `02 Atrodiet izmēru — Salīdziniet skaitļus ar tabulu zemāk.` | translation-draft |
| `03 Check the garment — Compare with the garment measurements on the product page …` | `03 Pārbaudiet izstrādājumu — Salīdziniet ar izmēriem preces lapā.` | translation-draft |
| Body size chart header + S–XL rows | `Ķermeņa izmēru tabula — cm / collas — Izmērs \| ES · Lielbritānija · ASV \| Krūtis \| Viduklis \| Gurni`; visi skaitļi un `S/M/L/XL`, `EU/UK/US` kodi nemainīti. | translation-draft |
| `EU, UK and US sizes match the labels on product pages. The chart is a general guide — always check the garment measurements …` | `ES, Lielbritānijas un ASV izmēri atbilst etiķetēm. Tabula ir vispārīgs ceļvedis — vienmēr pārbaudiet izstrādājuma izmērus.` | translation-draft |
| `Chest / bust`, `Waist`, `Hips` measurement instructions | `Krūtis — ap pilnāko daļu zem rokām, turot mērlenti līdzenu.` / `Viduklis — ap dabīgo vidukļa līniju, nepievelkot cieši.` / `Gurni — ar kopām kājām, ap pilnāko daļu.` | translation-draft |
| `Body vs garment … width armpit to armpit, length shoulder to hem, sleeve armpit to cuff.` | `Izstrādājuma izmēri mērīti plakani: platums no paduses līdz padusei, garums no pleca līdz apmalei, piedurknes garums no paduses līdz manžetei.` | translation-draft |
| `Tip — Double the garment width … The difference is the ease …` | `Padoms — Divkāršojiet platumu, lai iegūtu apkārtmēru; starpība ir brīvība izstrādājumā.` | translation-draft |
| `Example: Pure Wool Side-Slit Sweater, size S — 50 cm flat ≈ 100 cm (39.4 in) around.` | `Piemērs: Pure Wool Side-Slit Sweater, izmērs S — 50 cm plakani ≈ 100 cm (39.4 in) apkārt.` | translation-draft |
| `Fit types: Close-fitting / Relaxed / Oversized / One size` | `Pieguluma veidi: pieguļošs / brīvs / oversized / viens izmērs` | translation-draft |
| `Between sizes? … Send us your measurements and the piece you like.` / `Email Kristine` | `Starp izmēriem? Nosūtiet mums savus izmērus un izvēlēto izstrādājumu.` / `Rakstiet Kristine` | translation-draft |

### 3.6 Priority PDPs (P1–P5, list DRAFT per §1)

Titles, prices, size labels and fibre strings are locked (§2). Every `DELIVERY & RETURNS` line is `[PENDING ADVISER]`.

| SKU / EN source (snapshot) | LV draft | Lifecycle |
|---|---|---|
| P1 `Merino Wool Raglan Cardigan`, `€160.00` — `A relaxed raglan cardigan in 100% merino wool, machine-knitted and hand-finished in Riga.` | `Brīvs raglan kardigāns no 100% merino wool; adīts uz manuālām adāmmašīnām un pabeigts ar rokām Rīgā.` | translation-draft |
| P1 `Available in three colours: Black (shown in the photos), Brown and Blue. Brown and Blue are machine-knitted and hand-finished to order…` | `Pieejams trīs krāsās: Black (attēlos), Brown un Blue. Brown un Blue adīti uz manuālām adāmmašīnām un pabeigti ar rokām pēc pasūtījuma.` [VERIFY: MTO returns exception pending adviser] | translation-draft |
| P1 `DETAILS — Material: 100% merino wool; Style: Raglan cardigan; Fit: Relaxed, slightly oversized (one size)` | `DETAĻAS — Materiāls: 100% merino wool; Stils: Raglan kardigāns; Piegulums: brīvs, nedaudz oversized (viens izmērs)` | translation-draft |
| P1 `MEASUREMENTS — Width: 61 cm / 24.02 in; Front length: 67 cm / 26.37 in; Sleeve length from neck: 82 cm / 32.28 in; Sleeve length from armpit: 49 cm / 19.29 in; Collar width: 4 cm / 1.57 in` | `IZMĒRI` — visi skaitļi un vienības nemainīti; tulko tikai nosaukumus. | translation-draft |
| P1 `CARE — Hand wash cold or use a gentle wool cycle. Lay flat to dry.` | `KOPŠANA — Mazgāt ar rokām aukstā ūdenī vai maigā vilnas ciklā. Žāvēt plakani.` | translation-draft |
| P1 `Free shipping. In-stock items ship from Riga within 2–5 working days. 14-day returns.` | `Bezmaksas piegāde. Nosūtīšana no Rīgas 2–5 darba dienu laikā. Atgriešana 14 dienu laikā. [PENDING ADVISER]` | translation-draft |
| P2 `Merino Wool Raglan Sweater - Dusty Pink`, `€155.00` — `Oversized raglan sweater in dusty pink … Knitted on a manually operated knitting machine and hand-sewn in Latvia. Washed and pressed, ready to wear.` | `Oversized raglan svīteris putekļaini rozā; adīts uz manuālām adāmmašīnām un pabeigts ar rokām Rīgā. Mazgāts un gludināts.` [VERIFY: source "hand-sewn in Latvia" → approved phrase] | translation-draft |
| P2 `Material: merino wool; Fit: Oversized; roomy and easy to layer.` | `Materiāls: merino wool; Piegulums: oversized, plašs, viegli kombinējams slāņos.` | translation-draft |
| P2 `S/M: width 54 cm, front length 62 cm, back length 66 cm, sleeve from neck 75 cm; L/XL: width 60 cm, front length 63 cm, back length 69 cm, sleeve from neck 80 cm` | Skaitļi un `S/M`, `L/XL` nemainīti; tulko tikai nosaukumus. | translation-draft |
| P2 `CARE … Do not wring. Lay flat on a towel, reshape and dry flat.` / `DELIVERY & RETURNS` | `KOPŠANA — Negriezt. Izklāties uz dvieļa, piešķirt formu un žāvēt plakani.` / `Bezmaksas piegāde; nosūtīšana 2–5 darba dienu laikā; atgriešana 14 dienu laikā. [PENDING ADVISER]` | translation-draft |
| P3 `Women's Classic Lambswool Crew Sweater`, `€136.00` — `Classic lambswool crew-neck sweater with raglan sleeves … hand-sewn in Latvia.` | `Klasisks lambswool svīteris ar apaļu kaklu un raglan piedurknēm; adīts uz manuālām adāmmašīnām un pabeigts ar rokām Rīgā.` [VERIFY: source "hand-sewn in Latvia" → approved phrase] | translation-draft |
| P3 `Material: 100% lambswool (pure new wool); Fit: Relaxed.` + S–XL measurement rows | `Materiāls: 100% lambswool (pure new wool); Piegulums: brīvs.`; visi `S/M/L/XL`, `EU/US/UK` kodi un skaitļi nemainīti. | translation-draft |
| P3 `CARE …` / `DELIVERY & RETURNS` | Kā P2. [PENDING ADVISER] | translation-draft |
| P4 `Merino Wool Hat & Scarf Set`, `€110.00` — `Matching rib-knit beanie and scarf. Soft on the skin and warm without bulk. The beanie has a smooth, straight knit at the forehead so it does not press or leave lines.` | `Saskaņots ribainis cepure un šalle. Mīksta ādai un silta bez apjoma. Cepures pieres daļa ir gluda, lai nespiestu un neatstātu nospiedumus.` | translation-draft |
| P4 `Material: 100% extra-fine merino wool, Italian-spun yarn; Sizes: beanie one size, fits 54–58 cm heads; scarf approx. 190 × 36 cm` | `Materiāls: 100% extra-fine merino wool, itāļu vērptā dzija; Izmēri: cepure — viens izmērs, 54–58 cm galvai; šalle aptuveni 190 × 36 cm` | translation-draft |
| P4 `CARE …` / `DELIVERY & RETURNS` | `KOPŠANA — Mazgāt ar rokām aukstā ūdenī vai vilnas ciklā; žāvēt plakani; glabāt salocītu.` / kā P2. [PENDING ADVISER] | translation-draft |
| P5 `Merino Rib-Knit Beanie - Unisex`, `€45.00` — `Unisex rib-knit beanie with a fold-over cuff. A smooth, straight knit at the forehead means it won't press or leave lines. Suits short or long hair. Available in 11 colours.` | `Uniseksa ribainīša cepure ar locītu manžeti. Gluds adījums pieres daļā nespiež un neatstāj nospiedumus. Piemērota īsiem un gariem matiem. Pieejama 11 krāsās.` | translation-draft |
| P5 `Material: 100% extra-fine merino wool, Italian-spun yarn; Size: one size, medium-thick rib with gentle stretch; fits 54–58 cm heads` | `Materiāls: 100% extra-fine merino wool, itāļu vērptā dzija; Izmērs: viens izmērs, vidēji bieza riba ar maigu elastību; 54–58 cm galvai` | translation-draft |
| P5 `CARE …` / `DELIVERY & RETURNS` | Kā P4. [PENDING ADVISER] | translation-draft |

---

## 4. Do not use / held source claims (brand-voice §3 hard gate)

These strings appear in English sources or older drafts. They must **not** be introduced or strengthened in Latvian copy. This is the only section where they are written out.

- **Banned claims:** `sustainable`, `eco`, `ethical`, `green`, `conscious`, `slow fashion`, `organic`, `RWS`, `mulesing-free`, `certified`, `zero-waste`, `plastic-free`, `carbon`, and the held origin claim `made in Latvia` (including About's `100% made in Latvia`). No supplier evidence on file; removed by owner on 18 Oct. Do not translate into LV as active claims, even as hashtags.
- **Restricted:** bare `handmade` only in the owner-approved live line; **never** `hand-knitted` / `hand-knit` for machine pieces. Use the approved process phrase in §2.
- **Hype (avoid):** `luxurious`, `elevate`, `must-have`, `obsessed`, `game-changer`, `iconic`, `timeless` (max once), `unlock`, `curated`. Calm tone, no exclamation headlines.
- **Performance (banned unless the live PDP states it):** `itch-free`, `hypoallergenic`, `machine-washable`, `never pills`, `lasts forever`, `warmest`.
- **Proof:** only `Formerly Mareshop on Etsy, 4.9★ from 1,400+ customers`; `8,000+ orders over 15 years on Etsy`. Inflated `1,500+` is not live; never paraphrase a review into a quote.
- **Delivery/returns:** only the promises in §2. No "free returns", "hassle-free", "no questions asked"; no extra return promise while legal review is pending.
- **Fibre:** no site-wide generalisation; copy the exact string from each live PDP.
- Replacement returns wording in `returns-wording-draft-wave3.md` is DRAFT on assumptions — not publishable LV legal text.

---

## 5. Gaps / blockers to close before publication

1. `[FILL]` Native Latvian reviewer name (G3 / CRE-23). No §3 row is approved until a human reads it and moves its Lifecycle to `review` → `localized-ready`.
2. `[PENDING ADVISER]` PRD-19 / G4 — every returns, withdrawal, exchange, customs/duties and 14-day line. Do not publish altered legal terms.
3. `[FILL]` Gate G5 — confirm the P1–P5 list is final (provisional/assumed; GM-12 says keep the 5).
4. `[VERIFY]` Live-vs-approved drift: proof line ("reviews" → "customers"), process phrase ("hand-sewn in Latvia" → "finished by hand in Riga"), eligible shipping destinations, founder/family-history lines, and per-PDP fibre strings. Resolve each before promoting its row.
5. Source freshness: §1 snapshots are 2026-11-10; re-read each live URL on publication day. Prices and fibre strings must come from the live PDP that day.
6. Not sourced here, therefore not translated: contact page, privacy/cookie policy, imprint, category pages, guide pages, order/notification emails, and PDP FAQ blocks beyond §3.6 — route through the same reviewer when Weglot scope widens.
7. Weglot word count, plan choice and URL form (G1/G2) are owner gates outside this file; unsupported surfaces stay English per the spec.
