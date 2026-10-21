# Patch proposal: `build_google_feed.py` availability bug, 2026-10-21 (DRAFT, not applied)

Author: aw-seo-marketplace. Task SEO-03. **Not applied.** `build_google_feed.py` is a shared file and was not edited
or run. The owner (or whoever owns the generator) applies this patch after approval.

## Problem
1. **Availability is hard-coded.** Line 108 writes the literal `'in_stock'` for every row. When a SKU sells out,
   the feed keeps advertising it as available. Google treats an availability mismatch with the landing page as
   inaccurate product data: the item is disapproved and repeated mismatches can put the account at risk.
2. **Per-variant images are impossible.** Line 107 uses `imgs[0]` for every variant, so the 19 Oct manual fix
   (Brown cardigan image, SQ7601591) is undone on the next run, and owner photos bound per colour (ruling C7) can
   never reach the feed.
3. **Output path is outside the repo.** Line 109 writes `/mnt/user-data/outputs/...`. This is why the agents do not
   run the script.

## Proposed diff
```diff
--- a/build_google_feed.py
+++ b/build_google_feed.py
@@ -1,4 +1,40 @@
-import csv, re
+import csv, re, sys
+
+# Usage: python3 build_google_feed.py <squarespace-products-export.csv> <out.tsv>
+# Availability comes from the Squarespace product export (Stock column), never from a constant.
+# Unknown SKU, unreadable stock or conflicting duplicate rows -> stop. No default to in_stock.
+if len(sys.argv) != 3:
+    sys.exit('usage: build_google_feed.py <products-export.csv> <out.tsv>')
+EXPORT, out = sys.argv[1], sys.argv[2]
+STOCK = {}
+with open(EXPORT, newline='', encoding='utf-8') as f:
+    for r in csv.DictReader(f):
+        sku = (r.get('SKU') or '').strip()
+        if not sku:
+            continue
+        s = (r.get('Stock') or '').strip()
+        if sku in STOCK and STOCK[sku] != s:
+            sys.exit(f'STOP: {sku} has two stock values in {EXPORT}: {STOCK[sku]!r} vs {s!r}')
+        STOCK[sku] = s
+
+def availability(sku):
+    if sku not in STOCK:
+        sys.exit(f'STOP: {sku} not in {EXPORT}; refusing to guess availability')
+    s = STOCK[sku]
+    if s.lower() == 'unlimited':
+        return 'in_stock'
+    if not s.isdigit():
+        sys.exit(f'STOP: {sku} stock {s!r} is not a number')
+    return 'in_stock' if int(s) > 0 else 'out_of_stock'
+
+# Per-variant image overrides: SKU -> asset path under P. Fill only with photos the owner has
+# bound in Squarespace and confirmed by eye (feed QA F4, F5). Empty = gallery image 1.
+VIMG = {
+    # 'SQ7601591': '1762677181680-ROINLJPXW23F9IBWGYYN/image_10.jpg',  # cardigan Brown, [VERIFY] photo is brown
+}
 B='https://www.autumnandwool.com'
@@ -104,9 +140,11 @@ for pid,title,url,color,gender,kind,desc,imgs,vars_ in D:
         c=a.get('Primary color') or color
         sz=a.get('Size') or "One size"
         vt=', '.join(x for x in (a.get('Primary color'),a.get('Size')) if x)
-        rows.append([sku, pid if len(vars_)>1 else '', (title+(f' ({vt})' if vt else ''))[:150], desc+' '+SHIP, B+url, P+imgs[0]+'?format=1500w', ','.join(P+i+'?format=1500w' for i in imgs[1:]),
-            'in_stock', price+' EUR','Autumn & Wool','new','no',CAT[kind][0],CAT[kind][1],gender,'adult',c,sz,mat,''])
-out='/mnt/user-data/outputs/autumnandwool-google-feed.tsv'
+        main=VIMG.get(sku, imgs[0])
+        rows.append([sku, pid if len(vars_)>1 else '', (title+(f' ({vt})' if vt else ''))[:150], desc+' '+SHIP, B+url, P+main+'?format=1500w', ','.join(P+i+'?format=1500w' for i in imgs[1:]),
+            availability(sku), price+' EUR','Autumn & Wool','new','no',CAT[kind][0],CAT[kind][1],gender,'adult',c,sz,mat,''])
 with open(out,'w',newline='') as f:
     w=csv.writer(f,delimiter='\t'); w.writerow(cols[:-1]); [w.writerow(r[:-1]) for r in rows]
-print(len(rows),'rows', sum(1 for r in rows if not r[16]),'no color')
+print(len(rows),'rows', sum(1 for r in rows if not r[16]),'no color',
+      sum(1 for r in rows if r[7]=='out_of_stock'),'out_of_stock')
```

`additional_image_link` is unchanged (`imgs[1:]`). Only `image_link`, `availability`, the output path and the summary
line change.

## Why this design
- Stock source = the same Squarespace export the owner already downloads (Products → Export). One file, one truth,
  matching master-plan ruling C14 ("one stock list").
- It fails closed: a SKU missing from the export stops the build instead of defaulting to `in_stock`.
- `Unlimited` (gift card SQ4128122 in the export) maps to `in_stock`; the gift card is not in the feed today.
- Out-of-stock rows stay in the feed as `out_of_stock` rather than being dropped, so they come back without a new
  review when restocked. If the owner prefers to drop them, filter `rows` before writing (owner decision).

## Expected result on today's data (dry reasoning, not a run)
- With `products_Oct-17_10-46-00PM.csv`: 98 rows, 12 with no colour, **0 out_of_stock** (all 98 feed SKUs have
  stock ≥ 1 in that export; see feed QA F2).
- **Duplicate-row check will stop the build** if hidden duplicates carry different stock: SQ7004700 (beige vest),
  SQ3776585, the turtleneck SKUs and the stand-collar SKUs each appear twice in the 17 Oct export. In that export the
  duplicate values are equal (1/1, 1/1, 10/10, 4/4, 3/3), so it passes. After the dedupe decision (master plan
  decision 20) this check stays as a guard.
- Diff against the live TSV: only SQ7601591 `image_link` differs, unless `VIMG` carries the owner-confirmed photo.

## Test plan for whoever applies it
1. Run with the latest export into a scratch path, not the live TSV.
2. Diff the new TSV against `autumnandwool-google-feed.tsv`: expect changes only in `availability` (rows with stock 0)
   and in `image_link` for SKUs listed in `VIMG`.
3. Edit one stock value to 0 in a copy of the export and re-run: that SKU must read `out_of_stock`.
4. Delete one SKU row from a copy of the export: the build must stop with `STOP: ... not in ...`.
5. Send me the new TSV; I QA it (`aw-merchant-feed-qa`) before the owner uploads.

## Rollback
Keep the current script as `build_google_feed.py.bak-2026-10-21`. To roll back, restore it. Merchant Center keeps the last
uploaded file until a new upload.
