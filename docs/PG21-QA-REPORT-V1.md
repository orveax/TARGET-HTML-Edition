# ORIGEX — PG21 Case Study Details QA Report V1

Product ID: ORX-P01  
Page: PG21 — Case Study Details  
Canonical file: `case-study-details.html`  
Status: **PS7 / IMPLEMENTED / CI QA PASS — AR+EN**  
Date: 2026-08-20

## 1. Scope

Frozen V1 features verified:
- challenge;
- context;
- objective;
- approach;
- three-step process;
- illustrative result;
- qualitative metrics / review signals;
- metrics disclaimer;
- related cases;
- CTA.

## 2. Implementation Evidence

- `ar/case-study-details.html`
- `en/case-study-details.html`
- `assets/css/origex-case-study-details.css`
- `assets/js/origex-case-study-details.js`
- `docs/page-design-profiles/pg21-case-study-details-v1.md`
- `.github/workflows/pg21-case-study-details-qa.yml`

## 3. Editorial / Demo Safety

- Six fictional Demo case-detail records are embedded in HTML `<template>` elements.
- No new `cases.json` data domain was created.
- No client identity, testimonial, rating, revenue, ROI, sales volume, percentage uplift, distribution appointment, pricing, stock, regulatory approval or measured business outcome is claimed.
- Qualitative metrics are explicitly labelled as review signals / illustrative workflow outcomes.
- Production buyers are instructed to replace Demo evidence with verified, permissioned content.

## 4. Query / Runtime Contract

- `?id=case-001` through `?id=case-006` hydrate the matching Demo record.
- No ID defaults to `case-001`.
- Invalid ID safely falls back to `case-001` and displays a visible status notice.
- Language switch preserves the resolved case ID.
- Previous/next links remain inside the six-case set.
- Related cases exclude the current case and render two alternatives.
- Runtime uses no `fetch`, `XMLHttpRequest`, `localStorage` or `sessionStorage`.

## 5. Source QA

Final `qa/pg21-case-study-details/source-report.json`:
- global failures: **0**;
- Arabic failures: **0**;
- English failures: **0**;
- runtime failures: **0**;
- six case records in AR;
- six case records in EN;
- canonical sections confirmed: hero / notice / detail / navigation / related / CTA;
- canonical/hreflang/JSON-LD baseline PASS;
- client-leak scan PASS;
- Global Navigation V1 check PASS;
- Global Footer V1 check PASS;
- icon-reference check PASS.

## 6. Rendered / Responsive QA

Viewport matrix:
- AR 390 — PASS
- AR 820 — PASS
- AR 1366 — PASS
- AR 1536 — PASS
- EN 390 — PASS
- EN 820 — PASS
- EN 1366 — PASS
- EN 1536 — PASS

Result: **8/8 PASS** with no horizontal overflow.

## 7. Interaction QA

- AR valid `case-004`: PASS.
- EN valid `case-004`: PASS.
- AR invalid `case-999` fallback: PASS.
- EN invalid `case-999` fallback: PASS.
- Language switch ID preservation: PASS.
- Previous/next case navigation: PASS.
- Related-case count/exclusion: PASS.
- Desktop Mega Menu open/Escape: PASS.
- Mobile drawer open/close: PASS.
- Minimum interactive touch-target scan: PASS.

## 8. Shared System State

After PG21 addition:
- Global Footer V1 includes the new AR/EN detail pages with 0 failures.
- F05 Icon Integrity scans **44 AR/EN pages** with **0 missing sprite references**.
- Global Navigation V1 maps `case-study-details.html` to `case-studies.html` as the Explore parent without adding a new mobile route.

## 9. Final Decision

**PG21 is approved at PS7 / IMPLEMENTED / CI QA PASS — AR+EN.**

PS8 remains pending deployed Cloudflare browser acceptance under the project-wide final-acceptance gate.

## 10. Next Production Action

**PG22 — Downloads / Resources**.

Proceed through canonical content review → PS6 Page Design Profile + SEO/Page Identity contract → AR/EN build → resource/download-state/licensing QA.

Final QA evidence commit: `7b5be6b72985026d003f48da5f7b3674fb84fcf6`.

Copyright © ORVEAX.