#!/usr/bin/env python3
from pathlib import Path
import argparse
import re
import sys

ROOT = Path(__file__).resolve().parents[2]

AR_FOOTER = '''<footer class="orx-site-footer" data-orx-global-footer="v1">
  <div class="orx-container orx-container--wide">
    <div class="orx-footer__grid">
      <div class="orx-footer__brand"><a class="orx-brand" href="index.html"><img src="../assets/brand/origex-logo-ar-reverse.svg" alt="ORIGEX" width="178" height="40"></a><p>شركة تجريبية داخل قالب ORIGEX لعرض تجربة تجارة غذائية B2B تربط المنتجات والموردين والمشترين وشركاء التوزيع.</p></div>
      <div><h3 class="orx-footer__title">استكشف</h3><ul class="orx-footer__links"><li><a href="products.html">المنتجات</a></li><li><a href="suppliers.html">الموردون</a></li><li><a href="markets.html">الأسواق</a></li><li><a href="resources.html">الموارد</a></li></ul></div>
      <div><h3 class="orx-footer__title">تواصل</h3><ul class="orx-footer__links"><li><a class="orx-bidi" href="mailto:trade@example.com" data-orx-email="trade">trade@example.com</a></li><li><a class="orx-bidi" href="tel:+97400000000" data-orx-phone>+974 0000 0000</a></li><li><span data-orx-address>الدوحة، قطر — توضيحي</span></li></ul></div>
      <div><h3 class="orx-footer__title">ساعات العمل</h3><div class="orx-business-hours" data-orx-business-hours></div></div>
    </div>
    <div class="orx-footer__bottom"><span>ORIGEX — B2B Food Trading & Distribution HTML Template</span><span>بيانات العرض توضيحية · © ORVEAX</span></div>
  </div>
</footer>'''

EN_FOOTER = '''<footer class="orx-site-footer" data-orx-global-footer="v1">
  <div class="orx-container orx-container--wide">
    <div class="orx-footer__grid">
      <div class="orx-footer__brand"><a class="orx-brand" href="index.html"><img src="../assets/brand/origex-logo-light.svg" alt="ORIGEX" width="178" height="40"></a><p>A fictional company inside the ORIGEX template demonstrating a B2B food-trading experience connecting products, suppliers, buyers and distribution partners.</p></div>
      <div><h3 class="orx-footer__title">Explore</h3><ul class="orx-footer__links"><li><a href="products.html">Products</a></li><li><a href="suppliers.html">Suppliers</a></li><li><a href="markets.html">Markets</a></li><li><a href="resources.html">Resources</a></li></ul></div>
      <div><h3 class="orx-footer__title">Contact</h3><ul class="orx-footer__links"><li><a href="mailto:trade@example.com" data-orx-email="trade">trade@example.com</a></li><li><a href="tel:+97400000000" data-orx-phone>+974 0000 0000</a></li><li><span data-orx-address>Doha, Qatar — illustrative</span></li></ul></div>
      <div><h3 class="orx-footer__title">Business Hours</h3><div class="orx-business-hours" data-orx-business-hours></div></div>
    </div>
    <div class="orx-footer__bottom"><span>ORIGEX — B2B Food Trading & Distribution HTML Template</span><span>Demo data only · © ORVEAX</span></div>
  </div>
</footer>'''

FOOTER_RE = re.compile(r'<footer class="orx-site-footer"(?:\s+[^>]*)?>.*?</footer>', re.S)


def canonical(lang: str) -> str:
    return AR_FOOTER if lang == 'ar' else EN_FOOTER


def process(path: Path, check: bool) -> tuple[bool, str | None]:
    text = path.read_text(encoding='utf-8')
    matches = list(FOOTER_RE.finditer(text))
    rel = str(path.relative_to(ROOT))
    if not matches:
        return False, f'MISSING: {rel}'
    if len(matches) != 1:
        return False, f'MULTIPLE: {rel}:{len(matches)}'
    lang = path.parent.name
    expected = canonical(lang)
    current = matches[0].group(0)
    if current == expected:
        return False, None
    if check:
        return True, f'DRIFT: {rel}'
    new = text[:matches[0].start()] + expected + text[matches[0].end():]
    path.write_text(new, encoding='utf-8')
    return True, f'NORMALIZED: {rel}'


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    changed = False
    errors = False
    for lang in ('ar', 'en'):
        for path in sorted((ROOT / lang).glob('*.html')):
            did_change, message = process(path, args.check)
            changed = changed or did_change
            if message:
                print(message)
                if message.startswith(('MISSING:', 'MULTIPLE:')):
                    errors = True
    if args.check and (changed or errors):
        return 1
    if errors:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
