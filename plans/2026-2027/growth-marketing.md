# Growth Marketing plan, Q4 2026 and 2027

Status: DRAFT for owner approval. Written 2026-10-21 by aw-growth-marketing. Scope: paid acquisition, CAC,
competitors, UTM/attribution. Nothing here is spend approved or a live change.
Marking: TODO = input missing, [VERIFY] = unconfirmed, [PROPOSED] = my suggested target, not a forecast.
No revenue forecast is given: README section 10 says set revenue targets only after conversion, margin and CAC are measured.

## 1. Starting point (facts from the repo)

| Area | Fact | Source |
|---|---|---|
| Orders | Zero real direct orders. Only orders are tests #00003/#00004 (refunded). Stripe works, PayPal not connected | `weekly-measurement-report-2026-10-19.md`, `business-os/README.md` s2 |
| Traffic | 64 visits / 30 days (19 Sep-18 Oct), 2 from Google, 0 from Instagram/Pinterest, bounce about 96% | `zero-sales-diagnosis-2026-10-18.md` s1 |
| Search | GSC 90d: 11 clicks, 388 impressions, CTR 2.8%, position 14.1. 37 pages discovered, 11 indexed | `weekly-measurement-report-2026-10-19.md` |
| Merchant Center | 98 rows live, all under review (0 approved as of 19 Oct). Variant photos missing: beanie, turtleneck, hat set, blue cardigan. Approval expected from 21 Oct [VERIFY] | `owner-action-pack-2026-10-19.md` A, E |
| Measurement | GA4 `G-7TV8PK060Z` gives sessions only. No purchase events (Code Injection plan-gated). Orders = Squarespace Orders + Etsy | `business-os/README.md` s2, s8 |
| Pixel/conversion tags | Meta Pixel / Google Ads purchase tag likely impossible on current plan [VERIFY] | `business-os/ai-team.md` item 7 |
| Unit economics | `sku-economics.csv`: all 82 rows have blank cost columns and blank `target_cac_eur`. So **no break-even CAC exists for any SKU** | `business-os/sku-economics.csv` |
| Illustrative only | EUR 155 sweater example gives contribution 33.10 = break-even CAC. Not real costs, never use for budget | `business-os/README.md` s9 |
| Capacity | No `capacity-YYYY-Www.md` exists. Status MISSING, so no SKU is GREEN | `business-os/ai-team.md` (hand-offs) |
| KPI sheet | `kpi-weekly.csv` is header-only, no baseline week yet | `business-os/kpi-weekly.csv` |
| Growth folder | `business-os/growth/` (results log, utm-links, competitors) not yet created in this worktree [VERIFY on main checkout] | glob of `business-os/` |
| Budget idea | EUR 200-300 for December, only after GA4/measurement works. Owner has not approved any ceiling | `GROWTH-PLAN-100-IDEAS.md` s6 |
| Proof asset | Mareshop on Etsy: about 8.1-8.2k sales, 4.9 stars, about 1.4-1.5k reviews (figures differ across files). Always attribute to Etsy | `markets-and-gift-guides.md`, `owner-action-pack-2026-10-19.md` D |
| UTM | Bio-link UTMs defined (owner pack C). `campaign-drafts.md` uses `organic_social` and underscores, which conflicts with the taxonomy | `owner-action-pack-2026-10-19.md` C, skill `aw-utm-attribution` |
| Offline/PR | Riga Christmas markets and gift-guide pitches researched, nothing sent. Doma laukums asks for proof of Latvian production | `markets-and-gift-guides.md` |
| Competitors | No profiles yet. Names seen in AI-visibility check: Woolture, PappusStore, Mattilde, Smukilini. Skill seeds: Arela, Babaa, Lisa Yang, Navygrey (all unverified) | `GROWTH-PLAN-100-IDEAS.md` s3, skill `aw-competitor-research` |

Bottom line: the constraint is traffic and measurement, not ad efficiency. With 64 visits a month, paid tests
cannot be read yet. Q4 is mostly gate-clearing, free and organic attribution, competitor and angle work, and at
most one tiny capped test if every gate passes.

## 2. Q4 2026 (21 Oct - 31 Dec)

### Goals
1. Make paid spend *decidable*: costs, capacity list, conversion signal, UTM discipline in place.
2. Establish a measured baseline: first `kpi-weekly.csv` rows, sessions by source, first real orders counted.
3. Know which free channels send visitors (Google free listings, Pinterest, Instagram, Etsy move-to-site, markets, PR).
4. Run at most one capped paid test in December, only if all gates PASS. Otherwise spend EUR 0.

### Gates for any paid test (skill `aw-paid-ads-testing` s0)
| Gate | State 21 Oct | Unblock owner |
|---|---|---|
| SKU costed (`contrib` in `unit_economics.py`) | FAIL (all TODO) | Production / Finance, owner |
| SKU GREEN in owner-approved capacity file | MISSING | Production |
| PDP ready (photo per colour, size guide, delivery time) | FAIL (variant photos missing) | Owner, E-commerce |
| Orders countable | PASS (Squarespace Orders, manual) | n/a |
| Platform conversion signal | UNVERIFIED | E-commerce / owner (plan decision) |
| Owner monthly ceiling | MISSING | Owner |

### KPI targets
| KPI | Q4 target | Basis |
|---|---|---|
| Gates cleared (of 6 above) | 6 of 6 by 30 Nov [PROPOSED] | Needed for a December test |
| Break-even CAC known for priority SKUs | 5 of 5 priority SKUs by 15 Nov [PROPOSED]; the five SKUs are an owner decision (README s12) | `unit_economics.py` output |
| `kpi-weekly.csv` rows proposed | 1 row every Monday from week of 26 Oct (about 10 rows) | Weekly deliverable |
| UTM coverage | 100% of links I draft follow the taxonomy; 5 bio links live by 31 Oct (owner action) | Owner pack C |
| Sessions by source | Report weekly. Numeric traffic target: TODO, set after 3 weekly baselines | No baseline |
| Paid spend | EUR 0 until gates pass. If they pass, December ceiling is the owner's number, suggested EUR 200-300 [owner decision] | `GROWTH-PLAN-100-IDEAS.md` s6 |
| CAC | Report only when at least 1 paid order exists. No target until BE_CAC exists. Target CAC = `target_cac_eur` or 0.6 x BE_CAC | Skill s1 |
| New customers | Count weekly from Squarespace Orders. Numeric target: TODO (no conversion baseline) | n/a |

### Weekly actions (Mon, before business review)
- Pull Squarespace Orders, GA4 sessions by source/medium, GSC clicks, Merchant Center approved count.
- Update `business-os/growth/ads-results-log.csv` (calls HOLD/FIX/TEST/INVESTIGATE; INVESTIGATE overrides while purchase events are missing).
- Propose one `kpi-weekly.csv` row (CAC cell left blank until spend exists).
- Never report a channel as "not working" from GA4 alone.
- 1-2 test briefs or updates, each BLOCKED with an unblock list until gates pass.
- Attribution readout (skill `aw-utm-attribution` s5): "platforms claim N, we can verify M".

### Dated plan
| When | Action | Output |
|---|---|---|
| Week of 21 Oct | Create `growth/` files: `ads-results-log.csv`, `utm-links.csv` (bio links from owner pack C, status draft). Draft correction of `campaign-drafts.md` UTMs for owner | files in `business-os/growth/` |
| By 24 Oct | First weekly readout and baseline KPI row (reads Merchant Center approval, GSC, Squarespace) | readout, proposed row |
| By 31 Oct | Competitor quick scan, 3 profiles (one EU DTC, one Baltic Etsy maker, one aspirational), raw notes dated, `_angles.md` v1. Angles need proof we have (Etsy history attributed, Riga process, label fibre content) | `growth/competitors/` |
| By 31 Oct | Propose UTM/discount-code scheme for markets (QR `utm_source=qr`, `utm_medium=offline`) and for press/gift guides, so market and PR results are visible | `utm-links.csv` rows |
| By 7 Nov | Ask owner for ceiling and SKU shortlist (decision list s5). Draft the December test brief (one SKU, 2-3 concepts, broad EU countries) as BLOCKED or DRAFT | `test-2026-1x-<slug>.md` |
| By 15 Nov | If costs and capacity file exist: compute BE_CAC, set budget = 3 x BE_CAC per concept, kill and scale lines | brief updated |
| Mid-Nov | Check plan-upgrade decision (Code Injection). If upgrade happens: verify Meta/Google tag can fire purchase before any conversion-objective campaign | gate re-check |
| 20 Nov | Owner go/no-go on December test. Last safe launch date depends on carrier cut-offs: TODO from Operations | decision |
| Dec | If APPROVED: no edits for first 3-5 days, weekly readouts, stop at kill line (2 x BE_CAC with 0 orders, or 3 x BE_CAC with CAC > BE_CAC). No scale before 3 orders with positive contribution after CAC | log, readout |
| 31 Dec | Q4 review: what each source sent, what paid cost, per-SKU BE_CAC table, 2027 Q1 budget proposal | `growth/q4-2026-review.md` |

If no conversion signal exists in December, design the test as traffic objective, read through UTMs and Squarespace Orders (skill s0). No pixel changes by me.

### Monthly (Nov, Dec)
- Competitor pass: refresh 3-5 profiles (prices first), update `_angles.md`. Mark data stale after 60 days.
- Creative performance report from whatever ran (organic posts with UTMs if no paid).
- Next-month budget proposal capped by BE_CAC and capacity.

## 3. 2027 by quarter

All paid budgets below are proposals. Rule for every quarter: monthly ceiling = lower of owner budget and
(planned tests x 3 x BE_CAC). Spend amounts are TODO until BE_CAC exists. Targets marked [PROPOSED] are to be reset
after the Q4 baseline.

### Q1 2027 (Jan-Mar): baseline and first real tests
- Goals: first read on CAC; decide which two channels earn a second test (README s12 decision 2).
- KPIs: new customers per week (target TODO after Q4 baseline); CAC vs BE_CAC per SKU; share of orders with a known source (code, UTM, or survey) [PROPOSED: at least 70%, if the checkout question is feasible, otherwise TODO]; sessions by source.
- Initiatives: (1) 2-3 pre-registered Meta concept tests on GREEN priority SKUs. (2) Google: first confirm free listings approved and getting clicks, then Shopping/PMax test at EUR 5-10/day on priority SKUs (idea 52), feed quality first. (3) Post-purchase "How did you hear about us?" question proposed (UNVERIFIED on plan). (4) January sales-lull: use as cheap learning window, no discounts without owner approval and contribution check. (5) Day-90 plan: what to scale, fix or cut, with evidence.
- Budget ask: TODO. Cannot be set until BE_CAC and a GREEN SKU list exist. Initial rule: test budget per concept = 3 x BE_CAC.

### Q2 2027 (Apr-Jun): scale winners, cut losers
- Goals: scale only SKU x creative pairs with contribution after CAC > 0 on at least 3 orders.
- KPIs: CAC <= target CAC on scaled concepts; profitable revenue from paid (Squarespace revenue ex VAT minus variable costs minus ad spend); creative fatigue (frequency) tracked.
- Initiatives: raise budgets about 20% at a time with 3-5 days between raises, within weekly capacity; creator-code attribution with Partnerships (separate codes and links from paid); Pinterest ads test for gift/spring bestsellers (idea 53) if organic Pinterest shows traffic; monthly competitor pass continues.
- Budget ask: TODO, derived from Q1 CAC. Do not carry December numbers forward.

### Q3 2027 (Jul-Sep): pre-peak build
- Goals: prepare Q4 2027 with evidence: which SKUs and angles to fund, what production can ship.
- KPIs: CAC trend by channel; repeat customer rate (with CX/CRM); proven angle list of at most 5.
- Initiatives: build and approve autumn/gift creative from real photos and video (Creative); build prospecting plus retargeting structure only if volume supports it (50 events/week is not reachable at EUR 5-15/day, so keep simple); customer list exclusions once a list exists; first draft of Q4 2027 media plan against Production's capacity forecast; update competitor profiles before the season.
- Budget ask: TODO.

### Q4 2027 (Oct-Dec): peak gift season
- Goals: spend only on GREEN SKUs with proven BE_CAC headroom; last-order dates per country drive the calendar.
- KPIs: new customers, CAC vs BE_CAC, contribution after acquisition, units promoted <= "Max units to promote".
- Initiatives: ramp budgets from Q3 proof; weekly capacity check before each raise; stop-loss line pre-registered; year review and 2028 plan.
- Budget ask: TODO. Guardrail: no promotion beyond published capacity.

### Standing 2027 cadence
Weekly paid readout and results log; monthly competitor pass and creative report; quarterly budget proposal;
UTM audit each quarter (no internal UTMs, no PII, lowercase and hyphens).

## 4. Dependencies on other departments

| Needs from | What | By when | Blocks |
|---|---|---|---|
| Production (`aw-production`) | Real costs for the 22 visible SKUs in `sku-economics.csv` (materials, labour, shipping, packaging, returns); stock truth (turtleneck 360 and beanie 220 look like placeholders); weekly `capacity-YYYY-Www.md` with GREEN/AMBER and max units | Costs by 15 Nov; capacity weekly from now | Any budget, any brief going past BLOCKED |
| Finance (`aw-finance`) | Minimum contribution per order; review of BE_CAC and target CAC; payment fee actuals | 15 Nov | Target CAC |
| E-commerce / CRO | Variant photos bound, delivery times, size info, PayPal, verified Merchant Center approval; plan-upgrade decision (Code Injection) and conversion tag feasibility; landing-page readiness check per test | Photos/PayPal before test launch; plan decision by mid-Nov | PDP gate; conversion signal gate |
| SEO / Marketplace | Merchant Center approval and feed errors (availability hard-coded `in_stock`, 13 items out of stock); GSC data; Etsy move-to-site link | Weekly | Google Shopping test |
| Creative Content | Real photo and video assets per SKU (no AI-altered garments), 2-3 distinct concepts per test; brand-voice review | Before each test | Creative |
| Partnerships | Non-overlapping creator codes and UTMs vs paid links; shared attribution readout | When creators start | Clean attribution |
| Operations | Last order dates per country for Christmas, carrier cut-offs; returns data | 15 Nov | Test end dates, December promo claims |
| CX / CRM | Post-purchase source question, customer list for exclusions, review capture | Q1 2027 | Attribution, exclusions |
| Head of E-commerce / GM | Approvals, weekly review slot, 5 priority SKUs, 2 channels, owner ceiling | 7 Nov | Everything |

## 5. Risks and owner decisions

### Risks
| Risk | Effect | Mitigation |
|---|---|---|
| No cost data | No BE_CAC, so no budget possible (hard rule 5) | Escalate costs as the first dependency; spend EUR 0 |
| Traffic too low to read tests (64 visits/30d) | Tests give no signal, money wasted | Fund free and organic channels first; use big creative swings and pre-registered lines; do not claim significance |
| Purchases not visible to platforms | Platforms cannot optimise; reports can mislead | Traffic-objective tests, Squarespace Orders as truth, never sum platform claims |
| Peak-season timing | A test started too late cannot ship before Christmas | Fix last-order dates (Operations); stop paid gift promos after cut-off |
| Capacity | Handmade, small stock (e.g. vest stock 1) | Promote only GREEN SKUs up to max units |
| Claims | "Handmade", "sustainable", "made in Latvia" unverified; Etsy proof misattributed | Use "knitted on manual machines and finished by hand in Riga" wording per `ai-team.md`; always attribute 4.9 stars and review count to Mareshop on Etsy; figures vary (1.4k / 1.46k / 1.5k), so use one confirmed figure [VERIFY] |
| Asset rights | "ChatGPT Image" files in the store; photo rights unconfirmed | Do not use in ads until owner confirms |
| Conflicting UTM names in drafts | Fragmented GA4 channels | Fix before publishing |
| Trial ends 1 Nov (backup copy) | Store continuity | Owner decision on plan (GM/E-commerce) |
| Competitor data stale or incomplete | Wrong angles | Dated raw notes, "not observed on pages checked" wording, 60-day refresh |

### Owner decisions needed (in this order)
1. Squarespace plan upgrade for Code Injection (GA4 ecommerce, Clarity, conversion tags)? Price it against one month of blind ad spend. By mid-Nov.
2. Provide or approve cost inputs for the 22 visible SKUs, and the minimum contribution per order. By 15 Nov.
3. Which 5 priority SKUs to promote, and which 2 channels to test first.
4. Monthly paid ceiling for December (suggested EUR 200-300, only if gates PASS) and a 2027 Q1 ceiling process. EUR 0 is a valid answer.
5. Approve my UTM scheme and paste the 5 bio links live (owner pack C); approve fixing `campaign-drafts.md` UTMs.
6. Confirm "made in Latvia" status (affects ads and Doma laukums) and photo rights.
7. Whether Etsy stays open this season, and whether Etsy review quotes can appear in ads (with Etsy attribution).
8. Whether a post-purchase "How did you hear about us?" field is feasible and wanted.
9. Any discount or free-returns offer in December (needs contribution check first, per `GROWTH-PLAN-100-IDEAS.md` idea 8).
