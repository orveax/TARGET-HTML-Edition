#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import argparse
import html
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
FEATURED_IDS = ['prod-001', 'prod-003', 'prod-005', 'prod-007']
SECTION_RE = re.compile(
    r'<section class="orx-section orx-section--surface" aria-labelledby="products-title">.*?</section>',
    re.S,
)

ORIGIN_AR = {
    'IT': 'إيطاليا — توضيحي',
    'EG': 'مصر — توضيحي',
    'NL': 'هولندا — توضيحي',
    'PL': 'بولندا — توضيحي',
}
ORIGIN_EN = {
    'IT': 'Italy — illustrative',
    'EG': 'Egypt — illustrative',
    'NL': 'Netherlands — illustrative',
    'PL': 'Poland — illustrative',
}


def esc(value: object) -> str:
    return html.escape(str(value or ''), quote=True)


def load_data():
    products = json.loads((ROOT / 'assets/data/products.json').read_text(encoding='utf-8'))
    suppliers = json.loads((ROOT / 'assets/data/suppliers.json').read_text(encoding='utf-8'))
    product_map = {p['id']: p for p in products}
    supplier_map = {s['id']: s for s in suppliers}
    missing = [pid for pid in FEATURED_IDS if pid not in product_map]
    if missing:
        raise SystemExit(f'Missing canonical featured products: {missing}')
    return product_map, supplier_map


def card(product: dict, supplier: dict | None, lang: str) -> str:
    is_ar = lang == 'ar'
    name = product['nameAr'] if is_ar else product['nameEn']
    supplier_name = ''
    if supplier:
        supplier_name = supplier.get('nameAr' if is_ar else 'nameEn') or supplier.get('name', '')
    origin_map = ORIGIN_AR if is_ar else ORIGIN_EN
    origin = origin_map.get(product.get('originCode'), product.get('originCode', ''))
    packaging = product.get('packagingAr' if is_ar else 'packagingEn', '')
    shelf_life = product.get('shelfLifeAr' if is_ar else 'shelfLifeEn', '')
    storage = product.get('storageAr' if is_ar else 'storageEn', '')
    action = 'عرض المنتج' if is_ar else 'View Product'
    arrow = 'arrow-left' if is_ar else 'arrow-right'
    badge = 'استفسر' if is_ar else 'Enquire'

    summary = ' · '.join(esc(part) for part in (supplier_name, packaging, shelf_life, storage) if part)
    return (
        f'<article class="orx-card orx-product-card" data-product-id="{esc(product["id"])}">'
        f'<div class="orx-product-card__media" aria-hidden="true"></div>'
        f'<div class="orx-product-card__body">'
        f'<div class="orx-card__meta"><span class="orx-badge">{esc(origin)}</span>'
        f'<span class="orx-badge orx-badge--success">{badge}</span></div>'
        f'<h3 class="orx-card__title">{esc(name)}</h3>'
        f'<p class="orx-card__copy">{summary}</p>'
        f'<a class="orx-text-action" href="product-details.html?id={esc(product["id"])}">{action} '
        f'<svg class="orx-icon orx-icon--sm" aria-hidden="true"><use href="../assets/icons/sprite.svg#{arrow}"></use></svg></a>'
        f'</div></article>'
    )


def section(lang: str, product_map: dict, supplier_map: dict) -> str:
    is_ar = lang == 'ar'
    if is_ar:
        eyebrow = 'منتجات مختارة'
        title = 'منتجات ببيانات تجارية واضحة.'
        lead = 'أمثلة توضيحية مرتبطة مباشرة ببيانات المنتج المركزية لعرض المنشأ والتعبئة والتخزين والصلاحية ومسار الاستفسار.'
        notice = 'جميع الأسماء والبيانات التجارية الواردة في العرض التوضيحي أمثلة خيالية لأغراض القالب، ويجب استبدالها ببيانات فعلية قبل النشر.'
        all_products = 'عرض كل المنتجات'
    else:
        eyebrow = 'Featured Products'
        title = 'Products with clear commercial information.'
        lead = 'Illustrative records linked directly to the canonical product dataset for origin, packing, storage, shelf life and enquiry routing.'
        notice = 'All names and commercial data in this demo are fictional template examples and must be replaced with verified business information before publication.'
        all_products = 'View All Products'

    cards = []
    for pid in FEATURED_IDS:
        product = product_map[pid]
        supplier = supplier_map.get(product.get('supplierId'))
        cards.append(card(product, supplier, lang))

    return f'''<section class="orx-section orx-section--surface" aria-labelledby="products-title">
    <div class="orx-container orx-container--wide">
      <header class="orx-section-header"><span class="orx-eyebrow">{eyebrow}</span><h2 id="products-title">{title}</h2><p class="orx-lead">{lead}</p></header>
      <div class="orx-alert orx-alert--info mb-4"><svg class="orx-icon" aria-hidden="true"><use href="../assets/icons/sprite.svg#info"></use></svg><div>{notice}</div></div>
      <div class="orx-grid orx-grid--4">
        {chr(10).join(cards)}
      </div>
      <div class="mt-4"><a class="orx-btn orx-btn--secondary" href="products.html">{all_products}</a></div>
    </div>
  </section>'''


def inspect(path: Path, lang: str, product_map: dict, supplier_map: dict) -> list[str]:
    text = path.read_text(encoding='utf-8')
    match = SECTION_RE.search(text)
    failures: list[str] = []
    if not match:
        return ['missing-featured-products-section']
    block = match.group(0)
    if 'href="product-details.html"' in block:
        failures.append('bare-product-details-link')
    for pid in FEATURED_IDS:
        product = product_map[pid]
        supplier = supplier_map.get(product.get('supplierId'))
        name = product['nameAr'] if lang == 'ar' else product['nameEn']
        supplier_name = ''
        if supplier:
            supplier_name = supplier.get('nameAr' if lang == 'ar' else 'nameEn') or supplier.get('name', '')

        raw_required = [
            f'data-product-id="{pid}"',
            f'product-details.html?id={pid}',
        ]
        for value in raw_required:
            if value not in block:
                failures.append(f'{pid}:missing:{value}')

        text_required = [
            name,
            supplier_name,
            product.get('packagingAr' if lang == 'ar' else 'packagingEn', ''),
            product.get('shelfLifeAr' if lang == 'ar' else 'shelfLifeEn', ''),
            product.get('storageAr' if lang == 'ar' else 'storageEn', ''),
        ]
        for value in text_required:
            if value and esc(value) not in block:
                failures.append(f'{pid}:missing:{value}')

        if block.count(f'data-product-id="{pid}"') != 1:
            failures.append(f'{pid}:card-count')
        if block.count(f'product-details.html?id={pid}') != 1:
            failures.append(f'{pid}:link-count')
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    product_map, supplier_map = load_data()

    drift: list[str] = []
    for lang in ('ar', 'en'):
        path = ROOT / lang / 'index.html'
        text = path.read_text(encoding='utf-8')
        expected_section = section(lang, product_map, supplier_map)
        match = SECTION_RE.search(text)
        if not match:
            raise SystemExit(f'{path}: featured products section not found')
        new = text[:match.start()] + expected_section + text[match.end():]
        if new != text:
            if args.check:
                drift.append(f'{lang}/index.html')
            else:
                path.write_text(new, encoding='utf-8')

    failures: list[str] = []
    if args.check:
        failures.extend(f'drift:{path}' for path in drift)
    page_results = {}
    for lang in ('ar', 'en'):
        path = ROOT / lang / 'index.html'
        checks = inspect(path, lang, product_map, supplier_map)
        page_results[lang] = checks
        failures.extend(f'{lang}:{item}' for item in checks)

    ar_ids = re.findall(r'data-product-id="([^"]+)"', SECTION_RE.search((ROOT/'ar/index.html').read_text(encoding='utf-8')).group(0))
    en_ids = re.findall(r'data-product-id="([^"]+)"', SECTION_RE.search((ROOT/'en/index.html').read_text(encoding='utf-8')).group(0))
    if ar_ids != FEATURED_IDS or en_ids != FEATURED_IDS or ar_ids != en_ids:
        failures.append(f'ar-en-featured-id-parity:{ar_ids}:{en_ids}')

    report = {
        'page': 'PG01 Home 01',
        'gate': 'M7 Featured Products Canonical Data & Routing',
        'featuredIds': FEATURED_IDS,
        'arabicIds': ar_ids,
        'englishIds': en_ids,
        'source': 'assets/data/products.json + assets/data/suppliers.json',
        'failures': sorted(set(failures)),
        'pageFailures': page_results,
    }
    out = ROOT / 'qa/pg01-m7-featured-products'
    out.mkdir(parents=True, exist_ok=True)
    (out/'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    (out/'run-status.txt').write_text(('PASS' if not report['failures'] else 'FAIL')+'\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report['failures'] else 0


if __name__ == '__main__':
    sys.exit(main())
