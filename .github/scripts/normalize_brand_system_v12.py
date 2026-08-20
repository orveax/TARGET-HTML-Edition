#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
THEME_COLOR = '#082A2F'
FAVICON = '../assets/brand/favicon.svg'
HEADER_LOGO = {
    'ar': '../assets/brand/origex-logo-ar.svg',
    'en': '../assets/brand/origex-logo.svg',
}
FOOTER_LOGO = {
    'ar': '../assets/brand/origex-logo-ar-reverse.svg',
    'en': '../assets/brand/origex-logo-light.svg',
}
MOBILE_LOGO = '../assets/brand/origex-mark.svg'
LEGACY_BRAND_COLORS = {
    '#15343b', '#0d252b', '#3f6f68', '#c47a4a',
    '#e8dfd0', '#faf8f4', '#f3efe8', '#667278',
}
ACTIVE_BRAND_ASSETS = [
    'assets/brand/origex-logo.svg',
    'assets/brand/origex-logo-light.svg',
    'assets/brand/origex-logo-ar.svg',
    'assets/brand/origex-logo-ar-reverse.svg',
    'assets/brand/origex-mark.svg',
    'assets/brand/origex-mark-mono.svg',
    'assets/brand/origex-mark-reverse.svg',
    'assets/brand/favicon.svg',
    'assets/brand/origex-brand-field.svg',
]

HEADER_RE = re.compile(r'(<header class="orx-site-header[^>]*data-orx-site-header[^>]*>)(.*?)(</header>)', re.S)
DRAWER_HEAD_RE = re.compile(r'<div class="orx-mobile-drawer__head">.*?</div>', re.S)
FOOTER_RE = re.compile(r'(<footer class="orx-site-footer"[^>]*>)(.*?)(</footer>)', re.S)
BRAND_IMG_RE = re.compile(r'<img src="\.\./assets/brand/[^"]+" alt="ORIGEX"[^>]*>')
THEME_RE = re.compile(r'<meta name="theme-color" content="[^"]+">')


def normalized_page(path: Path) -> tuple[str, list[str]]:
    lang = path.parent.name
    text = path.read_text(encoding='utf-8')
    notes: list[str] = []

    new, n = THEME_RE.subn(f'<meta name="theme-color" content="{THEME_COLOR}">', text, count=1)
    if n == 0:
        notes.append('missing-theme-color')
    text = new

    if 'rel="icon"' not in text:
        marker = f'<meta name="theme-color" content="{THEME_COLOR}">'
        if marker in text:
            text = text.replace(marker, marker + f'\n  <link rel="icon" href="{FAVICON}" type="image/svg+xml">', 1)
        else:
            notes.append('favicon-not-inserted')

    header = HEADER_RE.search(text)
    if header:
        body = header.group(2)
        replacement = f'<img src="{HEADER_LOGO[lang]}" alt="ORIGEX" width="178" height="40">'
        body, count = BRAND_IMG_RE.subn(replacement, body, count=1)
        if count != 1:
            notes.append('header-brand-img')
        text = text[:header.start()] + header.group(1) + body + header.group(3) + text[header.end():]
    else:
        notes.append('missing-header')

    drawer = DRAWER_HEAD_RE.search(text)
    if drawer:
        block, count = BRAND_IMG_RE.subn(
            f'<img src="{MOBILE_LOGO}" alt="ORIGEX" width="40" height="40">',
            drawer.group(0),
            count=1,
        )
        if count != 1:
            notes.append('drawer-brand-img')
        text = text[:drawer.start()] + block + text[drawer.end():]
    else:
        notes.append('missing-drawer-head')

    footer = FOOTER_RE.search(text)
    if footer:
        body = footer.group(2)
        replacement = f'<img src="{FOOTER_LOGO[lang]}" alt="ORIGEX" width="178" height="40">'
        body, count = BRAND_IMG_RE.subn(replacement, body, count=1)
        if count != 1:
            notes.append('footer-brand-img')
        text = text[:footer.start()] + footer.group(1) + body + footer.group(3) + text[footer.end():]
    else:
        notes.append('missing-footer')

    return text, notes


def expected_checks(path: Path, text: str) -> list[str]:
    lang = path.parent.name
    failures: list[str] = []
    if f'<meta name="theme-color" content="{THEME_COLOR}">' not in text:
        failures.append('theme-color')
    if f'<link rel="icon" href="{FAVICON}" type="image/svg+xml">' not in text:
        failures.append('favicon')
    header = HEADER_RE.search(text)
    if not header or HEADER_LOGO[lang] not in header.group(0):
        failures.append('header-logo')
    drawer = DRAWER_HEAD_RE.search(text)
    if not drawer or MOBILE_LOGO not in drawer.group(0) or 'width="40" height="40"' not in drawer.group(0):
        failures.append('mobile-logo')
    footer = FOOTER_RE.search(text)
    if not footer or FOOTER_LOGO[lang] not in footer.group(0):
        failures.append('footer-logo')
    return failures


def audit_assets() -> list[str]:
    failures: list[str] = []
    for rel in ACTIVE_BRAND_ASSETS:
        path = ROOT / rel
        if not path.exists():
            failures.append(f'missing-asset:{rel}')
            continue
        try:
            ET.parse(path)
        except ET.ParseError as exc:
            failures.append(f'invalid-svg:{rel}:{exc}')
            continue
        lower = path.read_text(encoding='utf-8').lower()
        for color in LEGACY_BRAND_COLORS:
            if color in lower:
                failures.append(f'legacy-color:{rel}:{color}')
    return failures


def audit_css() -> list[str]:
    failures: list[str] = []
    for path in sorted((ROOT / 'assets/css').glob('*.css')):
        lower = path.read_text(encoding='utf-8').lower()
        for color in LEGACY_BRAND_COLORS:
            if color in lower:
                failures.append(f'legacy-css:{path.relative_to(ROOT)}:{color}')
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()

    pages = [p for lang in ('ar', 'en') for p in sorted((ROOT / lang).glob('*.html'))]
    normalization_notes: list[str] = []
    changed: list[str] = []

    for path in pages:
        current = path.read_text(encoding='utf-8')
        expected, notes = normalized_page(path)
        normalization_notes.extend(f'{path.relative_to(ROOT)}:{note}' for note in notes)
        if expected != current:
            if args.check:
                changed.append(str(path.relative_to(ROOT)))
            else:
                path.write_text(expected, encoding='utf-8')

    failures: list[str] = []
    if args.check:
        failures.extend(f'drift:{p}' for p in changed)

    page_results = {}
    for path in pages:
        checks = expected_checks(path, path.read_text(encoding='utf-8'))
        page_results[str(path.relative_to(ROOT))] = checks
        failures.extend(f'{path.relative_to(ROOT)}:{check}' for check in checks)

    failures.extend(audit_assets())
    failures.extend(audit_css())
    failures.extend(normalization_notes)

    ar_names = {p.name for p in (ROOT / 'ar').glob('*.html')}
    en_names = {p.name for p in (ROOT / 'en').glob('*.html')}
    if ar_names != en_names:
        failures.append('ar-en-filename-parity')

    report = {
        'standard': 'ORIGEX Brand System v1.2',
        'themeColor': THEME_COLOR,
        'pagesChecked': len(pages),
        'arabicPages': len(ar_names),
        'englishPages': len(en_names),
        'filenameParity': ar_names == en_names,
        'activeBrandAssetsChecked': len(ACTIVE_BRAND_ASSETS),
        'failures': sorted(set(failures)),
        'pageFailures': page_results,
    }
    out = ROOT / 'qa/brand-system-v12'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (out / 'run-status.txt').write_text(('PASS' if not report['failures'] else 'FAIL') + '\n', encoding='utf-8')

    print(json.dumps({k: report[k] for k in ('pagesChecked','arabicPages','englishPages','filenameParity','activeBrandAssetsChecked')}, indent=2))
    if report['failures']:
        print('\n'.join(report['failures']))
        return 1
    print('Brand System v1.2 PASS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
