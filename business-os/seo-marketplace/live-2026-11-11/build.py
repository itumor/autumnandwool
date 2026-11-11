"""2026-11-11 batch: exact-string replacements on page code blocks. Each needle must occur exactly once.
Owner decisions: Etsy numbers confirmed (as of November 2026); return wording = 'unworn, unwashed ... original condition'."""
import pathlib
N = pathlib.Path(__file__).parent
RET_OLD = 'Unworn, unused items can be returned within 14 days of delivery'
RET_NEW = 'Unworn, unwashed items in their original condition can be returned within 14 days of delivery'
EDITS = {
 'home.html': [
  ('8,000+ orders and 4.9 from 1,400+ reviews <a href="https://www.etsy.com/shop/mareshop" target="_blank" rel="noopener">on Etsy</a>.</p>',
   '8,000+ orders and 4.9 from 1,400+ reviews <a href="https://www.etsy.com/shop/mareshop" target="_blank" rel="noopener">on Etsy</a>, as of November 2026.</p>\n'
   '<p>Every garment is made in Latvia from merino wool, lambswool or pure new wool, and each product page lists the exact fibre, garment measurements and care steps. Our <a href="/size-guide">size guide</a> shows how to measure, and unworn, unwashed items in their original condition can be returned within 14 days of delivery.</p>'),
 ],
 'about.html': [
  ('Kristine designs every piece, inspired by a family tradition of knitting.</p>',
   'Kristine designs every piece, inspired by a family tradition of knitting. Each one is knitted on a manual knitting machine and finished by hand in our Riga studio.</p>'),
  ('<span><b>Washed and pressed</b> before it ships to you</span></li></ol>',
   '<span><b>Washed and pressed</b> before it ships to you</span></li></ol>'
   '<p>Each product page lists the exact fibre, fit and care steps. Before opening this shop we sold as Mareshop on Etsy for 15 years: more than 8,000 orders and a 4.9 rating from 1,400+ reviews <a href="https://www.etsy.com/shop/mareshop" target="_blank" rel="noopener">on Etsy</a>, as of November 2026. Those reviews are on Etsy, not on this website.</p>'
   '<p>Browse the <a href="/shop">shop</a> for current styles, or read <a href="/shipping-returns">Shipping &amp; returns</a> for delivery times and our 14-day returns.</p>'),
 ],
 'faq.html': [
  ('Returns are accepted within 14 days of delivery for unworn, unwashed items in original condition. Return shipping is paid by the customer unless the item is faulty. See Shipping &amp; returns for full terms.',
   RET_NEW + '. You pay return postage unless the item arrived damaged or incorrect. See <a href="/shipping-returns">Shipping &amp; returns</a> for full terms.'),
 ],
 'shipping-returns.html': [(RET_OLD, RET_NEW)],
 'wool-sweaters.html': [(RET_OLD, RET_NEW)],
 'wool-sweater-vests.html': [('nworn, unused items', 'nworn, unwashed items in their original condition')],
 'wool-hats-and-scarves.html': [('nworn, unused items', 'nworn, unwashed items in their original condition')],
 'wool-gifts.html': [(RET_OLD, RET_NEW)],
 'llms.txt': [
  ('unworn, unused items within 14 days of delivery; you pay return postage unless the item is faulty.',
   'unworn, unwashed items in their original condition within 14 days of delivery; you pay return postage unless the item arrived damaged or incorrect.'),
 ],
}
for f, edits in EDITS.items():
    s = (N / 'before' / f).read_text()
    for old, new in edits:
        assert s.count(old) == 1, (f, s.count(old), old[:50])
        s = s.replace(old, new)
    # llms.txt lists product URLs whose slugs contain 'handmade'
    assert f == 'llms.txt' or 'handmade' not in s.lower() and 'hand-knit' not in s.lower().replace('/hand-knitted-', '/').replace('-hand-knitted-', '-'), f
    (N / 'html' / f).write_text(s)
    print(f, len((N / 'before' / f).read_text()), '->', len(s))
