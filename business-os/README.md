# Autumn & Wool — Business Operating System

Local working copy of the A-to-Z company plan, turned into things the team can run: decisions, owners, checklists,
a KPI sheet and a per-SKU profit calculator. Nothing here touches the live store (product data is frozen; see
`../PROJECT-HANDBOOK.md`).

| File | Use |
|---|---|
| `README.md` | The plan: positioning, org, channels, funnel, ops, AI rules, tools, KPIs, 90 days, legal review |
| `hiring-plan.md` | Roles, job descriptions, 90-day scorecards, hiring order |
| `sku-economics.csv` | One row per product (82, from the 17 Oct export). Fill the cost columns |
| `unit_economics.py` | `python3 unit_economics.py` → contribution and break-even CAC per SKU. `init` re-seeds, `--selftest` checks the maths |
| `kpi-weekly.csv` | Weekly dashboard, one row per week. Paste into Google Sheets |
| `ai-team.md` | Hiring plan as 10 Claude Code agents + 23 skills (`../.claude/`) |

Principle: every activity must move **revenue, profit, product quality or retention**. Videos, site tweaks and
software are means, not goals.

---

## 1. Business model

```
Brand, product & customer research  →  what to sell, to whom, why they buy
Marketing                           →  social, creators, SEO/Pinterest, ads
Sales                               →  website conversion, checkout, Etsy
Production, fulfilment & CX         →  QC, stock, delivery, returns, support
Retention & profitable growth       →  reviews, email, repeat orders, referrals
        AI, data, finance and management support every stage
```

## 2. Starting point (facts, 21 Oct 2026)

Assets: made in Riga, manual-machine knitting + hand finishing, founder story, Mareshop/Etsy history
(~8.2k sales, ~1.5k reviews, 4.9★, 15 years). Historical marketplace proof, **not** direct-store sales.

Store state (from `../PROJECT-HANDBOOK.md`):

| Area | State |
|---|---|
| Direct sales | Zero real orders to date. Root cause (invisible click-trap overlay) fixed 19 Oct |
| Payments | Stripe proven with test orders #00003/#00004 (refunded). PayPal **not connected** (owner) |
| Analytics | GA4 `G-7TV8PK060Z` pageviews OK. **No ecommerce events** (Code Injection plan-gated) → count orders from Squarespace Orders, not GA4 |
| Google | Merchant Center rebuilt: 98 rows, approval expected from 21 Oct. Variant photos missing for beanie, turtleneck, hat set, cardigan blue |
| Catalog | 82 products, 22 visible |

Positioning:

- **Customer:** women 25–45 who value natural fibres, understated design, quality, comfort, distinctive knitwear.
- **Promise:** thoughtfully made knitwear from Riga, designed for comfort, longevity and timeless everyday style.
- **Channels:** autumnandwool.com = brand home; Etsy/Mareshop = marketplace discovery; Instagram, TikTok, Pinterest,
  Google = qualified traffic.
- **Order of work:** validate strongest products → buying confidence + conversion → steady acquisition → scale
  production and repeat purchase.

Do not re-platform or hire a tech team first. Prove the current store acquires customers profitably.

## 3. Organisation

```
CEO / Owner (strategy, investment, profitability; keeps creative direction + brand authenticity)
└── Head of E-commerce / GM (all commercial results, weekly P&L review)
    ├── Marketing & Growth      — Growth Marketing Manager, Creative Content Lead, Partnerships
    ├── E-commerce & Sales      — E-commerce & CRO Specialist (later: Marketplace Manager)
    ├── Product & Production    — Product & Production Manager
    └── Operations & CX         — Fulfilment Coordinator, CX & CRM Specialist
Shared: Finance (outsourced accountant) · Analytics · AI automation · Legal/compliance (EU consumer-law adviser)
```

Roles ≠ salaries. Founder likely covers product/production; one strong growth marketer can run ads + creators at
first. Detail and hiring order: `hiring-plan.md`.

## 4. Marketing — attract customers

| Channel | Job | Owner | Starting rule |
|---|---|---|---|
| Instagram + TikTok | Awareness: real people wearing it, making-of, fabric close-ups, styling, founder | Creative Content Lead | 3–5 short videos/week, review monthly |
| Pinterest + Google | Intent discovery: searchable imagery, titles/metadata, Merchant Center free listings | E-commerce Specialist → SEO hire | Fix variant photos first (Merchant Center) |
| Meta + Google Ads | Acquisition | Growth Marketing Manager | Small controlled tests on proven SKUs; scale only when contribution after CAC > 0 |
| Creators | Trust | Partnerships Specialist | Small relevant fashion creators, gifting/affiliate; measure orders + profit, not views |
| Etsy | Marketplace sales | E-commerce → Marketplace Manager | Listing quality, relevance, titles/tags, service |

UTM bio links for every social profile: `../owner-action-pack-2026-10-19.md` section C. Idea backlog:
`../GROWTH-PLAN-100-IDEAS.md`.

## 5. Sales — visitors into buyers

| Step | Must be true | Check |
|---|---|---|
| 1 Arrives | Clear brand + product message above the fold | Mobile 390px screenshot review |
| 2 Explores | Real photos per colour, material, fit, measurements, size guide | Every visible PDP |
| 3 Decides | Reviews, delivery cost + time, return policy, stock shown | Every visible PDP |
| 4 Checks out | Reliable payments (add PayPal), mobile, low friction | Monthly real test order + refund |
| 5 Receives | Tracking, careful packaging, support reply < 24 h | Ops log |
| 6 Returns | Care advice, useful email, new drops, recommendations | Repeat rate |

First project: perfect the **5 priority product pages** before raising ad spend.

## 6. Operations — after payment

| Stage | Do | Control |
|---|---|---|
| Order received | Validate payment, product, address | No missed/duplicate orders |
| Stock / production | Reserve stock or schedule making | Reliable lead time, shown on PDP |
| Quality check | Sizing, stitching, finish, **fibre-composition + care label** | Defect rate |
| Packaging | Care card, branding, protection | Consistent presentation |
| Shipping | Carrier, dispatch, tracking sent | On-time dispatch |
| After-sales | Questions, returns, feedback request | CSAT, review rate |
| Reporting | Update stock, actual cost, SKU profit (`sku-economics.csv`) | Accurate margins |

Capacity is a commercial constraint for handmade knitwear. **Production Manager publishes weekly capacity and the
list of SKUs safe to promote.** Marketing promotes only from that list.

## 7. AI across the company

| Dept | AI does | Human owns |
|---|---|---|
| Marketing | Scripts, caption variants, keyword research, ideas | Brand accuracy, decisions |
| Creative | Concepts, background cleanup, resizing, variations | Authentic product representation |
| E-commerce | Descriptions, SEO, translations, site analysis | Product truth, live changes |
| Customer service | Draft replies, FAQ, categorisation | Refunds, sensitive cases |
| Inventory | Forecast help, reorder suggestions | Real stock, purchasing |
| Finance | Reports, anomaly flags, margin maths | Reconciliation, accounting |
| Management | Weekly KPI summary, prioritisation | Strategy, spend approval |

First three workflows:

1. **Content:** product facts + real photos → AI drafts → creative review → scheduled post.
2. **Customer service:** inquiry → classify + draft reply → human approval when needed → send.
3. **Reporting:** orders, traffic, costs, campaigns → `kpi-weekly.csv` → AI summary → Monday decisions.

Hard rules: AI never invents reviews, specs, stock, fibre content or sustainability claims; never publishes ads or
issues refunds on its own (initially). Open item: the catalog claims cleanup (`../catalog-claims-cleanup-v3.csv`)
is only partly verified, and Shipping & Returns still says "handmade" and "sustainable fashion" without supplier
evidence (`../implementation-report.md`).

Automate only after the team has run a process by hand and knows it works.

## 8. Tools — low recurring cost

| Function | Tool | Cost | Note |
|---|---|---|---|
| E-commerce | Squarespace (existing) | Existing | Current plan blocks Code Injection |
| Analytics | GA4 + Search Console | Free | Ecommerce events blocked by plan |
| Behaviour | Microsoft Clarity | Free | **Needs a script tag → blocked on current plan** |
| Discovery | Google Merchant Center | Free listings | Live, approval pending |
| Email | MailerLite | Free ≤250 subs / 2,500 emails/mo | Verify current limits before signup |
| Social scheduling | Buffer or native | Free (3 channels) | |
| PM | Google Sheets/Drive | Free | |
| Design | Canva, CapCut | Free tiers | |
| AI | Shared platform/API budget | Usage-based | |
| Finance | Sheets + accountant's software | Minimal | |

Illustrative cap **€100–250/month** (example €150: store €45, AI €75, misc €30). Excludes salaries, ads,
payment fees, production, shipping, tax. Not a quote.

Decision to make: upgrading the Squarespace plan would unlock Code Injection → GA4 ecommerce events + Clarity +
more contributors (Core lists unlimited, Basic two — verify on current pricing page). Without it the funnel cannot
be measured past pageviews. Price the upgrade against one month of blind ad spend.

## 9. Finance — sales into profit

Illustrative €155 sweater (not real costs; `python3 unit_economics.py --selftest` reproduces it):

| Line | € |
|---|---|
| Price incl. 21% VAT | 155.00 |
| Revenue ex VAT | 128.10 |
| Materials + labour | −70 |
| Shipping | −12 |
| Payment processing | −5 |
| Packaging | −3 |
| Returns allowance | −5 |
| **Contribution before acquisition** | **33.10** (= break-even CAC) |
| Acquisition cost | −18 |
| **Contribution after acquisition** | **15.10** → still has to cover salaries + overhead |

So marketing never gets an unlimited budget. Track CAC, AOV, contribution margin and repeat rate together.

To do with real numbers: fill `sku-economics.csv` for the 22 visible products, run `python3 unit_economics.py`.
Its `contrib` column is the most you can pay to acquire a customer on that SKU's first order.

### KPI dashboard (`kpi-weekly.csv`, weekly; monthly cash + payroll review)

| KPI | Definition | Owner |
|---|---|---|
| Net revenue | Sales ex tax, net of returns | GM / Finance |
| Gross margin | Revenue after product cost | Production Manager |
| Contribution margin | Revenue after variable cost + acquisition | GM / Finance |
| Conversion rate | Orders ÷ sessions | E-commerce |
| AOV | Net order revenue ÷ orders | E-commerce |
| CAC | Acquisition spend ÷ new customers | Growth |
| Repeat purchase rate | Customers with 2+ orders ÷ customers | CRM |
| On-time dispatch | Dispatched within promised lead time ÷ orders | Operations |
| Sell-through | Units sold ÷ units available | Production Manager |

Sources: orders/revenue/AOV from Squarespace Orders + Etsy (GA4 has no purchase events); sessions from GA4;
spend from ad accounts.

## 10. 90-day plan

### Days 1–30 — Foundation and conversion readiness
- [ ] Hire GM, Growth Marketing Manager, E-commerce Specialist
- [ ] Fill costs for 22 visible SKUs in `sku-economics.csv`; agree minimum contribution per order
- [ ] Connect PayPal; run one real test order + refund
- [ ] Upload missing variant photos (owner action pack A); confirm Merchant Center approved > 0
- [ ] Decide Squarespace plan upgrade (section 8)
- [ ] Legal review of Shipping & Returns (section 11)
- [ ] Write order-to-delivery SOP from section 6; add fibre labels to QC checklist
- [ ] Start `kpi-weekly.csv` with a baseline week

Milestone: reliable store, measurable funnel, financial baseline.

### Days 31–60 — Acquisition experiments
- [ ] Creative Content Lead + CX owner in place
- [ ] 3–5 videos/week; UTM links everywhere
- [ ] 5–10 small creators gifted, tracked by code/link
- [ ] Small Meta + Google tests on the 5 priority SKUs only, capped by break-even CAC
- [ ] MailerLite welcome flow (`../campaign-assets/welcome-email-draft.md`)

Milestone: first evidence of which channels and products acquire customers economically.

### Days 61–90 — Optimise and scale selectively
- [ ] Scale winning SKU × creative pairs within weekly capacity
- [ ] Fix or cut losing pages/channels
- [ ] Retention: post-purchase care email, review request, new-drop email
- [ ] Automate one workflow from section 7 that has run manually for 4+ weeks
- [ ] Capacity review vs demand

Milestone: repeatable sales process with known costs and a defensible growth plan. Set revenue targets only after
real conversion, margin and CAC are measured.

## 11. Legal review — Shipping & Returns (for EU consumer-law adviser)

Not legal advice. Wording below comes from the plan's review of `/shipping-returns`. Re-check the live page before
sending it to the adviser:

| Current wording | EU general rule to check against |
|---|---|
| Discounted items excluded from returns | 14-day withdrawal right generally applies to discounted goods too |
| Made-to-order items broadly excluded | Exception covers goods made to the consumer's specifications or clearly personalised, not standard items made after order |
| Refunds exclude shipping | Original standard delivery cost normally refunded on withdrawal |
| Faults must be reported within 5 days | Legal guarantee for faulty goods is far longer (at least 2 years EU minimum); confirm Latvian notice rules |
| (QC) | Textile fibre-composition labelling (Reg. (EU) 1007/2011) on every garment |

Sources to give the adviser: europa.eu "Your Europe" (consumer rights, guarantees, textile labelling) and PTAC
(ptac.gov.lv). Product data and site copy are frozen; adviser output becomes a proposal for the owner.

## 12. First management meeting

Owner appoints one commercially experienced Head of E-commerce who has grown a DTC fashion/accessories brand,
with ownership of hiring, acquisition, product profitability and weekly performance.

Agenda — three decisions:

1. Which **5 products** to prioritise (input: `sku-economics.csv` contribution × stock × photo readiness).
2. Which **2 acquisition channels** to test first.
3. Minimum **contribution per order** each sale must generate.

Target state: know what sells, why customers buy, what each sale costs, and how to deliver more orders profitably.
