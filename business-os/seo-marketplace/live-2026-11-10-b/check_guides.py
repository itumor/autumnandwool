#!/usr/bin/env python3
"""Checks the rewritten SEO guide pages in html/ against the before/ originals.

Stdlib only. Run: python3 check_guides.py
"""
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
BEFORE = os.path.join(HERE, "before")
AFTER = os.path.join(HERE, "html")
INDEX = os.path.normpath(os.path.join(HERE, "..", "..", "..", "evidence", "seo-reaudit-2026-11-10", "crawl", "index.tsv"))
GUIDES = [
    "how-to-wash-a-wool-sweater.html",
    "merino-vs-lambswool.html",
    "oversized-fit-guide.html",
    "how-to-choose-a-wool-cardigan.html",
]
STYLE_APPEND = ".aw-seo-page table{border-collapse:collapse;width:100%;max-width:760px;margin:0 0 20px;font-size:15px}.aw-seo-page th,.aw-seo-page td{border:1px solid #D9D1C5;padding:8px 10px;text-align:left;vertical-align:top}.aw-seo-page th{background:#EFE9DF;font-weight:600}.aw-seo-page .aw-byline{font-size:14px;color:#6B6258;margin:0 0 20px}.aw-seo-page .aw-tablewrap{overflow-x:auto;max-width:760px}"


class Collect(HTMLParser):
    """Collects h1 text, hrefs, p-blocks, tables, classes and visible text."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.h1 = []
        self.hrefs = []
        self.tables = 0
        self.byline = False
        self.text = []
        self.skip = 0
        self.in_h1 = False
        self.h1_buf = []
        self.classes = []
        self.p_after_byline = None
        self.after_byline_seen = False
        self.in_p = False
        self.p_buf = []
        self.events = []  # ordered: ("byline",) / ("p", text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
        if tag == "h1":
            self.in_h1 = True
            self.h1_buf = []
        if tag == "table":
            self.tables += 1
        if "href" in a:
            self.hrefs.append(a["href"])
        cls = a.get("class", "") or ""
        if tag == "p":
            self.in_p = True
            self.p_buf = []
            if "aw-byline" in cls.split():
                self.events.append(("byline", None))
            else:
                self.events.append(("p", None))
            self._pidx = len(self.events) - 1

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
        if tag == "h1":
            self.in_h1 = False
            self.h1.append("".join(self.h1_buf).strip())
        if tag == "p" and self.in_p:
            self.in_p = False
            kind, _ = self.events[self._pidx]
            self.events[self._pidx] = (kind, "".join(self.p_buf))

    def handle_data(self, data):
        if self.skip:
            return
        self.text.append(data)
        if self.in_h1:
            self.h1_buf.append(data)
        if self.in_p:
            self.p_buf.append(data)


def parse(path):
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    c = Collect()
    c.feed(raw)
    return raw, c


def index_paths():
    paths = set()
    with open(INDEX, encoding="utf-8") as f:
        for line in f:
            url = line.split("\t", 1)[0].strip()
            if url:
                paths.add(urlparse(url).path.rstrip("/") or "/")
    return paths


def main():
    failures = []

    def check(cond, msg):
        if not cond:
            failures.append(msg)

    idx = index_paths()
    for name in GUIDES:
        bpath = os.path.join(BEFORE, name)
        apath = os.path.join(AFTER, name)
        if not os.path.exists(apath):
            failures.append(f"{name}: missing html/{name}")
            continue
        braw, b = parse(bpath)
        araw, a = parse(apath)
        print(f"== {name}")

        # style block: identical except appended rules
        bstyle = braw[: braw.index("</style>")]
        astyle = araw[: araw.index("</style>")].replace(STYLE_APPEND, "")
        check(astyle == bstyle, f"{name}: style block changed before the appended rules")
        check(STYLE_APPEND in araw, f"{name}: appended style rules missing")

        # exactly one h1, same text
        check(len(a.h1) == 1, f"{name}: expected 1 h1, found {len(a.h1)}")
        check(b.h1 == a.h1, f"{name}: h1 text changed: {b.h1!r} -> {a.h1!r}")

        # every before href kept
        for href in b.hrefs:
            check(href in a.hrefs, f"{name}: href dropped: {href}")

        # byline
        check("aw-byline" in araw, f"{name}: no aw-byline class")
        byline_idx = [i for i, e in enumerate(a.events) if e[0] == "byline"]
        check(len(byline_idx) == 1, f"{name}: expected one byline paragraph")
        if byline_idx:
            bl = a.events[byline_idx[0]]
            print("   byline present")
            # first <p> after byline
            nxt = [e for e in a.events[byline_idx[0] + 1:] if e[0] == "p"]
            if nxt:
                words = len(nxt[0][1].split())
                print(f"   first p after byline: {words} words")
                check(40 <= words <= 60, f"{name}: first p after byline is {words} words, need 40-60")
            else:
                failures.append(f"{name}: no p after byline")

        # exactly one table
        check(a.tables == 1, f"{name}: expected 1 table, found {a.tables}")
        check(araw.count('<div class="aw-tablewrap">') == 1, f"{name}: table not wrapped in aw-tablewrap")

        # banned words in visible text (attributes/hrefs excluded; they are kept links)
        visible = " ".join(a.text).lower()
        for banned in ("handmade", "hand-knit"):
            check(banned not in visible, f"{name}: banned word in visible text: {banned}")
        check("<script" not in araw.lower(), f"{name}: <script found")
        check(not re.search(r"\son[a-z]+\s*=", araw, re.I), f"{name}: inline event handler found")

        # internal links exist in crawl index
        for href in a.hrefs:
            if href.startswith("/shop/") or href.startswith("/wool-"):
                check(href.split("?")[0].split("#")[0] in idx, f"{name}: not in index.tsv: {href}")

        # More list unchanged
        bmore = braw[braw.index("<h2>More from"):]
        amore = araw[araw.index("<h2>More from"):]
        check(bmore == amore, f"{name}: 'More from' block changed")

    print()
    if failures:
        print("FAIL")
        for f in failures:
            print(" -", f)
        return 1
    print("PASS: all guides pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
