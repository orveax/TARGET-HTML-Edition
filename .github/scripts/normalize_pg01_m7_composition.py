#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import argparse
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
PAGES = [ROOT / 'ar/index.html', ROOT / 'en/index.html']

REDUNDANT_INLINE_STYLES = (
    ' style="color:var(--orx-sand)"',
    ' style="color:#fff;border-color:rgba(255,255,255,.45)"',
)


def normalize(text: str) -> str:
    for style in REDUNDANT_INLINE_STYLES:
        text = text.replace(style, '')
    return text


def inspect(path: Path) -> list[str]:
    text = path.read_text(encoding='utf-8')
    failures: list[str] = []

    for style in REDUNDANT_INLINE_STYLES:
        if style.strip() in text:
            failures.append(f'redundant-inline-style:{style.strip()}')

    final_cta = re.search(r'<section class="orx-final-cta">.*?</section>', text, re.S)
    if not final_cta:
        failures.append('missing-final-cta')
    else:
        block = final_cta.group(0)
        if block.count('orx-btn--primary') != 1:
            failures.append('final-cta-primary-count')
        if block.count('orx-btn--secondary') != 1:
            failures.append('final-cta-secondary-count')
        if 'style="color:' in block or 'style="border-color:' in block:
            failures.append('final-cta-local-color-override')

    supplier_cta = re.search(r'<section class="orx-section orx-section--soft" aria-labelledby="supplier-cta-title">.*?</section>', text, re.S)
    if not supplier_cta:
        failures.append('missing-supplier-cta')
    elif 'style="color:' in supplier_cta.group(0):
        failures.append('supplier-cta-local-color-override')

    product_section = re.search(r'<section class="orx-section orx-section--surface" aria-labelledby="products-title">.*?</section>', text, re.S)
    if not product_section:
        failures.append('missing-products-section')
    elif 'href="product-details.html"' in product_section.group(0):
        failures.append('bare-product-details-link')

    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()

    drift: list[str] = []
    for path in PAGES:
        current = path.read_text(encoding='utf-8')
        expected = normalize(current)
        if current != expected:
            if args.check:
                drift.append(str(path.relative_to(ROOT)))
            else:
                path.write_text(expected, encoding='utf-8')

    failures: list[str] = []
    if args.check:
        failures.extend(f'drift:{path}' for path in drift)

    page_failures = {}
    for path in PAGES:
        checks = inspect(path)
        page_failures[str(path.relative_to(ROOT))] = checks
        failures.extend(f'{path.relative_to(ROOT)}:{item}' for item in checks)

    report = {
        'page': 'PG01 Home 01',
        'gate': 'M7 Composition & CSS Ownership',
        'pagesChecked': len(PAGES),
        'rules': [
            'CTA colors/states owned by shared component CSS',
            'No redundant local CTA foreground/border overrides',
            'One primary + one secondary action in final CTA',
            'Featured product cards use contextual Product Details routes',
        ],
        'failures': sorted(set(failures)),
        'pageFailures': page_failures,
    }
    out = ROOT / 'qa/pg01-m7-composition'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (out / 'run-status.txt').write_text(('PASS' if not report['failures'] else 'FAIL') + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report['failures'] else 0


if __name__ == '__main__':
    sys.exit(main())
