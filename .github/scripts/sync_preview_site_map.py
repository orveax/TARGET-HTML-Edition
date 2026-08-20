#!/usr/bin/env python3
"""Synchronize the internal ORIGEX preview site map with the approved PS7 registry state.

Update the constants below only after the Page Registry has approved a new PS7 page.
This utility is internal QA infrastructure and does not change product scope.
"""
from pathlib import Path
import re

R = Path(__file__).resolve().parents[2]
PATH = R / "site-map.html"

IMPLEMENTED_COUNT = 31
PENDING_COUNT = 2
LINKED_LANGUAGE_PAGES = 62
THROUGH_LABEL = "PG30"
PROMOTED_PG = "PG30"
PROMOTED_TITLE = "Privacy"
PROMOTED_FILE = "privacy.html"
NEXT_PG = "PG31"
NEXT_TITLE = "Terms"
NEXT_FILE = "terms.html"

text = PATH.read_text(encoding="utf-8")

replacements = [
    (r'<strong>\d+</strong><span>Implemented through PG\d+</span>', f'<strong>{IMPLEMENTED_COUNT}</strong><span>Implemented through {THROUGH_LABEL}</span>'),
    (r'<strong>\d+</strong><span>Implemented AR \+ EN pages</span>', f'<strong>{LINKED_LANGUAGE_PAGES}</strong><span>Implemented AR + EN pages</span>'),
]

for pattern, replacement in replacements:
    text, count = re.subn(pattern, replacement, text, count=1)
    if count != 1:
        raise SystemExit(f"site-map sync failed: expected exactly one match for {pattern!r}, got {count}")

promoted_pattern = rf'<article class="card" data-status="(?:pending|implemented)"><span class="pg">{PROMOTED_PG}</span>.*?</article>'
promoted_html = (
    f'<article class="card" data-status="implemented"><span class="pg">{PROMOTED_PG}</span>'
    f'<div><div class="title">{PROMOTED_TITLE} <span class="status done">PS7</span></div>'
    f'<div class="file">{PROMOTED_FILE}</div></div><div class="actions">'
    f'<a class="btn" href="ar/{PROMOTED_FILE}">AR</a><a class="btn" href="en/{PROMOTED_FILE}">EN</a>'
    f'</div></article>'
)
text, count = re.subn(promoted_pattern, promoted_html, text, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f"site-map sync failed: {PROMOTED_PG} card match count {count}")

next_pattern = rf'<article class="card" data-status="pending"><span class="pg">{NEXT_PG}</span>.*?</article>'
next_html = (
    f'<article class="card" data-status="pending"><span class="pg">{NEXT_PG}</span>'
    f'<div><div class="title">{NEXT_TITLE} <span class="status pending">NEXT</span></div>'
    f'<div class="file">{NEXT_FILE}</div></div><div class="actions"></div></article>'
)
text, count = re.subn(next_pattern, next_html, text, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f"site-map sync failed: {NEXT_PG} card match count {count}")

PATH.write_text(text, encoding="utf-8")
print(f"site-map synced: {IMPLEMENTED_COUNT} implemented / {PENDING_COUNT} pending / {LINKED_LANGUAGE_PAGES} language pages / next {NEXT_PG}")
