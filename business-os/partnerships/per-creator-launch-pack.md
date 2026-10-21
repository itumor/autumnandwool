# Per-creator launch pack (PAR-14 prep) - DRAFT template

Status: DRAFT, prepared 2026-10-21. Copy this block once per creator who says yes. No creator has agreed yet.
Nothing is sent, created or shipped by the agent. Growth owns `business-os/growth/utm-links.csv` (ruling C15):
the UTM row is handed to Growth, which already holds a creator template row (status `template`, code
`HELD-per-master-C6-until-owner-decision-11`).

```
## <handle> - <platform> - agreed <yyyy-mm-dd> - DRAFT

1. Tracker: status agreed -> row in creator-tracker.csv (deal_model, sku_gifted, size_colour, code, utm_url)
2. Deal model: gift, no obligation | gift + code   (commission: none in Q4 unless owner D5)
3. Gift spec (creator-brief-gifting.md Part B):
   SKU: <priority-5 SKU, G8-cleared>  colour/size: <..>  real unit confirmed by owner: [ ]
   Gift cost EUR: <from gift-budget-worksheet.md>   max CAC EUR: <..>   ship by: <date, after G4, not after 30 Nov>
4. Code (only case A/C of attribution-scheme.md s1): <HANDLE + % from D5>, end <date>, limit <..>
   Owner creates it in Marketing > Discounts. Agent does not.
5. UTM link:
   <landing_url>?utm_source=creator-<handle>&utm_medium=affiliate&utm_campaign=gifting-2026-11&utm_content=<ig-reel|ig-story|tt-video>
   Check: URL returns 200, query string survives any shortener, no personal data.
6. Row for Growth (append to growth/utm-links.csv, status draft):
   <yyyy-mm-dd>,aw-partnerships,creator-<handle>-<platform>,<landing_url>,creator-<handle>,affiliate,gifting-2026-11,<platform>-<format>,<full_url>,<CODE or none>,draft
7. Brief: creator-brief-gifting.md Part A with fields filled, LV version if native-checked
8. Usage rights: separate written ask (usage-rights-template.md), only if owner approved terms
9. Owner approvals: [ ] gift [ ] value [ ] code [ ] brief [ ] shipped (date)
```

Landing URLs: `attribution-scheme.md` s3 (beanie, hat & scarf set, /shop). [VERIFY] each loads before use.

## Wave-3 pre-fill on assumptions (2026-10-21)

ASSUMPTION: case B attribution (no code), beanie gift EUR 19.83 LV / 20.83 EE-LT, ship by 27 Nov after G4; register:
`business-os/partnerships/assumptions-wave3.md` (A-PAR-01, -03, -09, -10; A-GM-06, A-GM-17). Only `<handle>`,
`<platform>`, `<format>` and the owner's tick boxes stay open once a creator says yes:

```
2. Deal model: gift, no obligation (no code, no commission, no cash fee in Q4)
3. Gift spec: Rib-Knit Beanie, photographed colour [VERIFY], one size [VERIFY]; real unit made W47: [ ]
   Gift cost EUR 19.83 (LV) / 20.83 (EE-LT) ASSUMED; max per gift EUR 22; ship by Fri 27 Nov, after G4
   Payback needed: 2 attributed orders within 60 days (blended CM2 18.92 LV, ASSUMED)
4. Code: none (case B). Manual weekly check of Squarespace Orders by the owner
5. UTM: https://www.autumnandwool.com/shop/p/p/merino-beanie-100-wool-soft-warm-breathable-rib-knit-hat-for-men-women-1?utm_source=creator-<handle>&utm_medium=affiliate&utm_campaign=gifting-2026-11&utm_content=ig-<reel|story|post>
6. Growth row: <yyyy-mm-dd>,aw-partnerships,creator-<handle>-instagram,<beanie PDP>,creator-<handle>,affiliate,gifting-2026-11,ig-<format>,<full_url>,none,draft
8. Usage rights: 3 months, organic only; ads only on a separate written yes (A-GM-17)
```
Creators are LV/EE/LT only in Q4 (A-PAR-04). This block is a draft: no creator has agreed, and nothing is shipped.
