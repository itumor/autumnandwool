#!/usr/bin/env python3
"""Per-SKU order economics for Autumn & Wool. Stdlib only.

  python3 unit_economics.py init      # seed sku-economics.csv from the Squarespace product export
  python3 unit_economics.py           # report contribution per SKU (rows with blank costs are listed as TODO)
  python3 unit_economics.py --selftest
"""
import csv
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXPORT = HERE.parent / "products_Oct-17_10-46-00PM.csv"
SHEET = HERE / "sku-economics.csv"
COSTS = ["materials_labour_eur", "shipping_eur", "payment_eur", "packaging_eur", "returns_allowance_eur"]
COLS = ["product_id", "title", "visible", "stock", "price_eur", "vat_rate", *COSTS, "target_cac_eur"]


def economics(price, vat_rate, costs, cac):
    """Return (net revenue ex VAT, contribution before acquisition, contribution after CAC)."""
    net = price / (1 + vat_rate)
    before = net - sum(costs)
    return net, before, before - cac


def init():
    if SHEET.exists():
        sys.exit(f"{SHEET.name} exists; delete it first to re-seed (your cost entries would be lost)")
    products, current = [], None
    with EXPORT.open(encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if r["Product ID [Non Editable]"]:  # first row of a product; following rows are its variants
                current = {"product_id": r["Product ID [Non Editable]"], "title": r["Title"].strip(),
                           "visible": r["Visible"], "stock": 0, "price_eur": r["Price"],
                           "vat_rate": "0.21", "target_cac_eur": ""}
                current.update(dict.fromkeys(COSTS, ""))
                products.append(current)
            current["stock"] += int(r["Stock"]) if r["Stock"].isdigit() else 0  # ponytail: "Unlimited" counts as 0
    products.sort(key=lambda p: (p["visible"] != "Yes", p["title"]))
    with SHEET.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, COLS)
        w.writeheader()
        w.writerows(products)
    print(f"wrote {len(products)} products to {SHEET.name}; fill the cost columns, then run without args")


def report():
    rows = list(csv.DictReader(SHEET.open(encoding="utf-8")))
    todo = []
    print(f"{'title':44} {'price':>7} {'net':>7} {'contrib':>8} {'margin':>7} {'after CAC':>9}")
    for r in rows:
        if any(r[c] == "" for c in COSTS):
            todo.append(r)
            continue
        net, before, after = economics(float(r["price_eur"]), float(r["vat_rate"]),
                                       [float(r[c]) for c in COSTS], float(r["target_cac_eur"] or 0))
        flag = "  <- loses money" if after < 0 else ""
        print(f"{r['title'][:44]:44} {float(r['price_eur']):7.2f} {net:7.2f} {before:8.2f} "
              f"{before / net:7.0%} {after:9.2f}{flag}")
    # "contrib" is also the break-even CAC: spend more than that per new customer and the first order loses money.
    print(f"\n{len(rows) - len(todo)} costed, {len(todo)} TODO "
          f"({sum(r['visible'] == 'Yes' for r in todo)} of them visible on the store)")


def selftest():
    # The illustrative €155 sweater from README section 8 must come out at ~€33 / ~€15.
    net, before, after = economics(155, 0.21, [70, 12, 5, 3, 5], 18)
    assert round(net, 2) == 128.10, net
    assert round(before, 2) == 33.10, before
    assert round(after, 2) == 15.10, after
    assert economics(121, 0.21, [100], 0) == (100, 0, 0)
    print("selftest ok")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "report"
    {"init": init, "report": report, "--selftest": selftest}.get(arg, lambda: sys.exit(__doc__))()
