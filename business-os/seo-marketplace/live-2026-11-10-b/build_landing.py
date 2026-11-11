"""Rebuild the 5 /wool-* landing pages: lead (2 sentences) -> product grid with prices -> rest of intro.
Prices come from Product JSON-LD in a fresh fetch of each product page, never typed by hand.
ponytail: prices are static text in a code block; re-run this script after any price change."""
import re, json, sys, pathlib, urllib.request, time
N = pathlib.Path(__file__).parent
UA = {'User-Agent': 'Mozilla/5.0 (Macintosh) Chrome/126 Safari/537.36'}
PAGES = ['wool-sweaters', 'wool-cardigans', 'wool-sweater-vests', 'wool-hats-and-scarves', 'wool-gifts']
CSS = ('.aw-seo-page ul.aw-seo-grid .aw-price{display:block;font-weight:400;color:#6B6258;margin-top:2px}'
       '.aw-seo-page p.aw-lead{font-size:19px}')
cache = {}
def price(path):
    if path in cache: return cache[path]
    h = urllib.request.urlopen(urllib.request.Request('https://www.autumnandwool.com' + path, headers=UA), timeout=30).read().decode('utf-8', 'replace')
    time.sleep(0.6)
    for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        d = json.loads(b)
        if d.get('@type') != 'Product': continue
        o = d['offers']
        assert o['priceCurrency'] == 'EUR', (path, o)
        if o.get('@type') == 'AggregateOffer':
            lo, hi = float(o['lowPrice']), float(o['highPrice'])
            cache[path] = f'€{lo:.0f}' if lo == hi else f'From €{lo:.0f}'
        else:
            cache[path] = f"€{float(o['price']):.0f}"
        return cache[path]
    raise SystemExit(f'no Product JSON-LD: {path}')
report = []
for p in PAGES:
    src = (N / 'before' / f'{p}.html').read_text()
    out = src.replace('</style>', CSS + '\n</style>', 1)
    # prices on tiles
    def tile(m):
        return f'{m.group(0)[:-len("</span></a>")]}</span><span class="aw-price">{price(m.group(1))}</span></a>'
    out, n = re.subn(r'<a href="(/shop/p/[^"]+)"><img [^>]*><span>[^<]*</span></a>', tile, out)
    # lead = first 2 sentences of first <p> after h1; remainder goes after the first grid
    m = re.search(r'(<h1>.*?</h1>\n)<p>(.*?)</p>\n', out, re.S)
    body = m.group(2)
    cut = [x.end() for x in re.finditer(r'\.(?=\s+[A-Z])', body)]
    moved = False
    if len(cut) >= 3 and '<ul class="aw-seo-grid">' in out:
        lead, rest = body[:cut[1]], body[cut[1]:].strip()
        out = out.replace(m.group(0), f'{m.group(1)}<p class="aw-lead">{lead}</p>\n', 1)
        out = out.replace('</ul>\n', f'</ul>\n<p>{rest}</p>\n', 1)
        moved = True
    (N / 'html' / f'{p}.html').write_text(out)
    # self-check: same links, same h1, nothing lost
    assert sorted(re.findall(r'href="([^"]+)"', src)) == sorted(re.findall(r'href="([^"]+)"', out)), p
    strip = lambda s: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s.split('</style>')[1]))
    lost = set(strip(src).split()) - set(strip(out).split())
    assert not lost, (p, lost)
    assert out.count('<h1') == 1
    report.append((p, len(src), len(out), n, moved))
for r in report: print(*r, sep='\t')
print(json.dumps(cache, indent=0, ensure_ascii=False))
