#!/usr/bin/env python3
from pathlib import Path
import argparse
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
EXCLUDED = {'landing.html'}

PRIMARY_FAMILIES = {
    'home': {'index.html', 'home-02.html', 'home-03.html'},
    'products': {'product-categories.html', 'products.html', 'product-details.html'},
    'suppliers': {'suppliers.html', 'supplier-details.html', 'for-suppliers.html', 'submit-product.html'},
    'market': {'market-access.html', 'markets.html', 'become-partner.html'},
}

DETAIL_PARENT = {
    'product-details.html': 'products.html',
    'supplier-details.html': 'suppliers.html',
    'service-details.html': 'capabilities.html',
    'case-study-details.html': 'case-studies.html',
    'article-details.html': 'insights.html',
}

AR = {
    'primary': [('home','index.html','الرئيسية'),('products','products.html','المنتجات'),('suppliers','suppliers.html','الموردون'),('market','market-access.html','الوصول إلى السوق')],
    'explore': 'استكشف',
    'cta': 'اطلب عرض سعر',
    'nav_label': 'التنقل الرئيسي',
    'mobile_label': 'قائمة الهاتف',
    'open': 'فتح القائمة',
    'close': 'إغلاق القائمة',
    'groups': [
        ('الشركة', [('about.html','عن الشركة'),('how-we-work.html','كيف نعمل'),('capabilities.html','القدرات والخدمات'),('company-profile.html','الملف التعريفي')]),
        ('المنتجات', [('product-categories.html','فئات المنتجات'),('products.html','كل المنتجات')]),
        ('الموردون', [('suppliers.html','الموردون والعلامات'),('for-suppliers.html','للموردين'),('submit-product.html','قدم منتجك')]),
        ('السوق والشراكات', [('market-access.html','الوصول إلى السوق'),('markets.html','الأسواق والدول'),('become-partner.html','كن موزعًا / شريكًا')]),
        ('الموارد والدعم', [('case-studies.html','دراسات الحالة'),('resources.html','الموارد والتنزيلات'),('certifications-compliance.html','الشهادات والامتثال'),('insights.html','الرؤى والمقالات'),('faq.html','الأسئلة الشائعة'),('contact.html','تواصل معنا')]),
        ('نماذج الرئيسية', [('index.html','الرئيسية 01'),('home-02.html','الرئيسية 02'),('home-03.html','الرئيسية 03'),('landing.html','Landing / One Page')]),
    ],
    'mobile': [('index.html','الرئيسية'),('products.html','المنتجات'),('product-categories.html','فئات المنتجات'),('suppliers.html','الموردون'),('for-suppliers.html','للموردين'),('market-access.html','الوصول إلى السوق'),('markets.html','الأسواق والدول'),('about.html','عن الشركة'),('how-we-work.html','كيف نعمل'),('capabilities.html','القدرات والخدمات'),('company-profile.html','الملف التعريفي'),('submit-product.html','قدم منتجك'),('become-partner.html','كن موزعًا / شريكًا'),('resources.html','الموارد'),('insights.html','الرؤى'),('faq.html','الأسئلة الشائعة'),('contact.html','تواصل معنا')],
}

EN = {
    'primary': [('home','index.html','Home'),('products','products.html','Products'),('suppliers','suppliers.html','Suppliers'),('market','market-access.html','Market Access')],
    'explore': 'Explore',
    'cta': 'Request a Quote',
    'nav_label': 'Primary navigation',
    'mobile_label': 'Mobile menu',
    'open': 'Open menu',
    'close': 'Close menu',
    'groups': [
        ('Company', [('about.html','About'),('how-we-work.html','How We Work'),('capabilities.html','Capabilities & Services'),('company-profile.html','Company Profile')]),
        ('Products', [('product-categories.html','Product Categories'),('products.html','All Products')]),
        ('Suppliers', [('suppliers.html','Suppliers & Brands'),('for-suppliers.html','For Suppliers'),('submit-product.html','Submit Your Product')]),
        ('Market & Partnership', [('market-access.html','Market Access'),('markets.html','Markets & Countries'),('become-partner.html','Become Distributor / Partner')]),
        ('Resources & Support', [('case-studies.html','Case Studies'),('resources.html','Downloads / Resources'),('certifications-compliance.html','Certifications & Compliance'),('insights.html','Insights'),('faq.html','FAQ'),('contact.html','Contact')]),
        ('Home Demos', [('index.html','Home 01'),('home-02.html','Home 02'),('home-03.html','Home 03'),('landing.html','Landing / One Page')]),
    ],
    'mobile': [('index.html','Home'),('products.html','Products'),('product-categories.html','Product Categories'),('suppliers.html','Suppliers'),('for-suppliers.html','For Suppliers'),('market-access.html','Market Access'),('markets.html','Markets & Countries'),('about.html','About'),('how-we-work.html','How We Work'),('capabilities.html','Capabilities & Services'),('company-profile.html','Company Profile'),('submit-product.html','Submit Your Product'),('become-partner.html','Become Distributor / Partner'),('resources.html','Resources'),('insights.html','Insights'),('faq.html','FAQ'),('contact.html','Contact')],
}

def family_for(filename: str) -> str:
    for key, values in PRIMARY_FAMILIES.items():
        if filename in values:
            return key
    return 'explore'

def current_target(filename: str) -> str:
    return DETAIL_PARENT.get(filename, filename)

def current_attr(condition: bool) -> str:
    return ' aria-current="page"' if condition else ''

def canonical_header(lang: str, filename: str) -> str:
    t = AR if lang == 'ar' else EN
    family = family_for(filename)
    current = current_target(filename)
    mega_id = f'global-mega-{lang}'
    brand_label = 'ORIGEX — الرئيسية' if lang == 'ar' else 'ORIGEX — Home'
    other_lang = 'en' if lang == 'ar' else 'ar'
    other_label = 'EN' if lang == 'ar' else 'AR'

    primary = []
    for key, href, label in t['primary']:
        primary.append(f'      <a class="orx-nav-link" href="{href}"{current_attr(family == key)}>{label}</a>')
    primary.append(f'      <button class="orx-nav-link" type="button" aria-expanded="false" aria-controls="{mega_id}" data-orx-mega-trigger{current_attr(family == "explore")}>{t["explore"]} <svg class="orx-icon orx-icon--sm" aria-hidden="true"><use href="../assets/icons/sprite.svg#chevron-down"></use></svg></button>')

    groups = []
    for title, items in t['groups']:
        links = ''.join(f'<a href="{href}"{current_attr(href == current)}>{label}</a>' for href, label in items)
        groups.append(f'        <div class="orx-mega-menu__group"><span class="orx-mega-menu__title">{title}</span>{links}</div>')

    return f'''<header class="orx-site-header" data-orx-site-header data-orx-global-nav="v1">
  <div class="orx-container orx-container--wide orx-site-header__inner">
    <a class="orx-brand" href="index.html" aria-label="{brand_label}"><img src="../assets/brand/origex-logo.svg" alt="ORIGEX" width="140" height="40"></a>
    <nav class="orx-primary-nav" aria-label="{t['nav_label']}">
{chr(10).join(primary)}
    </nav>
    <div class="orx-site-header__actions">
      <a class="orx-lang-switch" href="../{other_lang}/{filename}" lang="{other_lang}" hreflang="{other_lang}">{other_label}</a>
      <a class="orx-btn orx-btn--primary orx-btn--sm" href="rfq.html" data-orx-header-cta>{t['cta']}</a>
      <button class="orx-icon-btn orx-mobile-toggle" type="button" aria-label="{t['open']}" aria-expanded="false" data-orx-drawer-open><svg class="orx-icon" aria-hidden="true"><use href="../assets/icons/sprite.svg#menu"></use></svg></button>
    </div>
    <div class="orx-mega-menu" id="{mega_id}" data-orx-mega-menu hidden>
      <div class="orx-mega-menu__grid">
{chr(10).join(groups)}
      </div>
    </div>
  </div>
</header>'''

def canonical_drawer(lang: str, filename: str) -> str:
    t = AR if lang == 'ar' else EN
    current = current_target(filename)
    other_lang = 'en' if lang == 'ar' else 'ar'
    other_label = 'English' if lang == 'ar' else 'العربية'
    links = ''.join(f'<a href="{href}"{current_attr(href == current)}>{label}</a>' for href, label in t['mobile'])
    links += f'<a href="../{other_lang}/{filename}" lang="{other_lang}">{other_label}</a>'
    return f'''<div class="orx-mobile-drawer" data-orx-mobile-drawer aria-hidden="true" data-orx-global-nav="v1">
  <div class="orx-mobile-drawer__backdrop" data-orx-drawer-backdrop></div>
  <aside class="orx-mobile-drawer__panel" aria-label="{t['mobile_label']}">
    <div class="orx-mobile-drawer__head"><img src="../assets/brand/origex-logo.svg" alt="ORIGEX" width="128" height="37"><button class="orx-icon-btn" type="button" aria-label="{t['close']}" data-orx-drawer-close><svg class="orx-icon" aria-hidden="true"><use href="../assets/icons/sprite.svg#x"></use></svg></button></div>
    <nav class="orx-mobile-nav">{links}</nav>
  </aside>
</div>'''

def normalize_html(path: Path, check: bool) -> bool:
    if path.name in EXCLUDED:
        return False
    text = path.read_text(encoding='utf-8')
    if 'data-orx-site-header' not in text:
        return False
    lang = path.parent.name
    expected_header = canonical_header(lang, path.name)
    expected_drawer = canonical_drawer(lang, path.name)
    new = re.sub(r'<header class="orx-site-header" data-orx-site-header(?: [^>]*)?>.*?</header>', expected_header, text, count=1, flags=re.S)
    new = re.sub(r'<div class="orx-mobile-drawer" data-orx-mobile-drawer aria-hidden="true"(?: [^>]*)?>.*?(?=<main id="main">)', expected_drawer + '\n\n', new, count=1, flags=re.S)
    if new == text:
        return False
    if check:
        print(f'DRIFT: {path.relative_to(ROOT)}')
        return True
    path.write_text(new, encoding='utf-8')
    print(f'NORMALIZED: {path.relative_to(ROOT)}')
    return True

def normalize_runtime(check: bool) -> bool:
    path = ROOT / 'assets/js/origex-ui.js'
    text = path.read_text(encoding='utf-8')
    marker_start = '  // Controlled global-navigation layer:'
    marker_end = '  // Mobile drawer — N03'
    if marker_start not in text:
        return False
    start = text.index(marker_start)
    end = text.index(marker_end)
    replacement = '''  // N01/N02/N03 global navigation structure is canonical static HTML.
  // JS owns behavior only; it must not inject, remove, reorder or relabel business navigation routes.
  // Authority: docs/GLOBAL-NAVIGATION-CONTRACT-V1.md

'''
    new = text[:start] + replacement + text[end:]
    if check:
        print('DRIFT: assets/js/origex-ui.js still contains structural navigation hydration')
        return True
    path.write_text(new, encoding='utf-8')
    print('NORMALIZED: assets/js/origex-ui.js')
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    drift = False
    for lang in ('ar', 'en'):
        for path in sorted((ROOT / lang).glob('*.html')):
            drift = normalize_html(path, args.check) or drift
    drift = normalize_runtime(args.check) or drift
    if args.check and drift:
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
