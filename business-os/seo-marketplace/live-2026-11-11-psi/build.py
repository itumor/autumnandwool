"""PageSpeed fixes 2026-11-11: logo link name (Custom CSS) + responsive images (home Code block).
Run: python3 build.py   (asserts act as the self-check)"""
import re, pathlib
D = pathlib.Path(__file__).parent

# 1. Custom CSS: keep logo <img> in the accessibility tree (was display:none -> link had no name)
css = (D / "before/custom.css").read_text()
OLD = ".header-title a picture img,.header-title a picture source{display:none!important}"
NEW = (".header-title a picture source{display:none !important}\n"
       "/* PageSpeed 2026-11-11: logo image visually hidden, not display:none, so the logo link keeps its alt text as a name */\n"
       ".header-title a picture img:not(#_){position:absolute !important;width:1px !important;height:1px !important;"
       "max-height:1px !important;opacity:0 !important;clip-path:inset(50%) !important;pointer-events:none}")
# empty alt for the CSS wordmark text, placed AFTER the original content rules so it wins; older browsers drop it and keep the original
ANCHOR = "@media (max-width:799px){.header-title a::before,.header-title a picture::before,.header-title a picture::after{font-size:26px}}"
ALT = ("\n/* PageSpeed 2026-11-11: decorative wordmark text gets empty alt so the logo link is read once */\n"
       ".header-title a::before{content:~\"'Autumn' / ''\"}\n"
       ".header-title a picture::before{content:~\"'&' / ''\"}\n"
       ".header-title a picture::after{content:~\"'Wool' / ''\"}")
assert css.count(ANCHOR) == 1
css_in = css
css = css.replace(ANCHOR, ANCHOR + ALT)
assert css.count(OLD) == 1, css.count(OLD)
out = css.replace(OLD, NEW)
for guard in (".sqs-widgets-confirmation-overlay{pointer-events:none !important;}", ".sqs-widgets-confirmation{pointer-events:none !important;}"):
    assert out.count(guard) == 1, guard
(D / "html/custom.css").write_text(out)

# 2. Home Code block: srcset + sizes so browsers pick 500w/750w instead of always 750w/1000w
html = (D / "before/home.html").read_text()
def rep(m):
    base, w, rest = m.group(1), int(m.group(2)), m.group(3)
    if w == 1000:  # hero (LCP)
        widths, sizes = (500, 750, 1000), "(max-width:800px) 100vw, 50vw"
    else:          # cards and grids
        widths, sizes = (300, 500, 750), "(max-width:800px) 92vw, 25vw"
    srcset = ", ".join(f"{base}?format={x}w {x}w" for x in widths)
    return f'<img src="{base}?format={w}w" srcset="{srcset}" sizes="{sizes}"{rest}'
new, n = re.subn(r'<img src="([^"?]+)\?format=(\d+)w"([^>]*>)', rep, html)
assert n == html.count("<img ") == 16, (n, html.count("<img "))
strip = lambda s: re.sub(r' srcset="[^"]*" sizes="[^"]*"', "", s)
assert strip(new) == html          # nothing else changed
assert new.count("<h1") == 1
(D / "html/home.html").write_text(new)
print("ok css", len(css_in), "->", len(out), "| home", len(html), "->", len(new), "| imgs", n)
