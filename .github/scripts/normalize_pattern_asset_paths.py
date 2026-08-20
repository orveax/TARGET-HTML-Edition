#!/usr/bin/env python3
"""Normalize inline ORIGEX pattern custom-property URLs for stylesheet resolution.

`--orx-pattern-image` is consumed by assets/css/origex-foundation.css. Relative URLs
inside the custom property therefore resolve from the stylesheet context in Chromium.
Shipped AR/EN pages must use ../patterns/... rather than ../assets/patterns/... to
resolve to /assets/patterns/... without duplicating the assets directory.
"""
from pathlib import Path

R = Path(__file__).resolve().parents[2]
OLD_SINGLE = "url('../assets/patterns/"
NEW_SINGLE = "url('../patterns/"
OLD_DOUBLE = 'url("../assets/patterns/'
NEW_DOUBLE = 'url("../patterns/'

changed = []
replacements = 0

for lang in ("ar", "en"):
    for path in sorted((R / lang).glob("*.html")):
        text = path.read_text(encoding="utf-8")
        count = text.count(OLD_SINGLE) + text.count(OLD_DOUBLE)
        if not count:
            continue
        text = text.replace(OLD_SINGLE, NEW_SINGLE).replace(OLD_DOUBLE, NEW_DOUBLE)
        path.write_text(text, encoding="utf-8")
        changed.append(str(path.relative_to(R)))
        replacements += count

print(f"pattern-path normalization: {replacements} replacements across {len(changed)} files")
for path in changed:
    print(path)
