# ORIGEX — PG03 + PG04 Home Family QA Record

Product ID: ORX-P01  
Milestone: M2 — Global Shell & Home Family  
Date: 2026-08-19  
Status: CI QA PASS — CLOUDFLARE DEPLOYED-BROWSER REVIEW PENDING

## Pages

### PG03 — Home 03 — Manufacturer & Supplier
- Arabic: `ar/home-03.html`
- English: `en/home-03.html`
- Content: C7 — IMPLEMENTED
- C6 authority: `docs/page-design-profiles/pg03-home-03-v1.md`
- Page-family CSS: `assets/css/origex-manufacturer.css`
- Owned hero media: `assets/media/demo/hero-manufacturer-readiness.svg`
- Current state: **C7 / CI QA PASS / CLOUDFLARE REVIEW PENDING**

### PG04 — Landing / One Page
- Arabic: `ar/landing.html`
- English: `en/landing.html`
- Content: C7 — IMPLEMENTED
- C6 authority: `docs/page-design-profiles/pg04-landing-v1.md`
- Page-family CSS: `assets/css/origex-landing.css`
- Page-specific demo form JS: `assets/js/origex-landing.js`
- Owned hero media: `assets/media/demo/hero-commercial-enquiry.svg`
- Current state: **C7 / CI QA PASS / CLOUDFLARE REVIEW PENDING**

## Source / Content / SEO / Asset QA

Evidence: `qa/pg03-pg04-home-family/source-report.json`  
Result: **PASS — failures 0**.

Verified across all four language/page files:
- `lang` / `dir` correctness.
- one canonical H1.
- unique IDs.
- canonical + AR/EN/x-default hreflang.
- Open Graph baseline.
- WebPage structured-data baseline.
- mandatory fictional/demo disclosure.
- no TARGET/client/CDN leakage.
- local Bootstrap + M1 runtime.
- C6 Page Design Profile presence.
- frozen section intents present.
- local linked assets exist.
- canonical internal filenames only.

PG03 additional checks:
- certification cards explicitly demo-labelled.
- export markets explicitly illustrative, not verified export history.
- manufacturer composition layer present.

PG04 additional checks:
- compact form contract present.
- no form endpoint/action.
- demo validation runtime present.

## Rendered Responsive QA

Evidence: `qa/pg03-pg04-home-family/rendered-interaction-report.json`  
Result: **PASS — failures 0**.

Matrix: 16 rendered cases:
- PG03 AR + EN × 390×844 / 820×1180 / 1366×900 / 1536×960.
- PG04 AR + EN × 390×844 / 820×1180 / 1366×900 / 1536×960.

All cases passed:
- RTL/LTR direction.
- zero horizontal overflow/offscreen defects.
- required touch target minimums.
- readable hero/H1.
- local fonts loaded.

Compact visual evidence was captured for AR/EN at 390 and 1536 widths for both pages under `qa/pg03-pg04-home-family/`.

## Interaction QA

Result: **PASS**.

PG03 AR/EN:
- desktop mega menu open + Escape close.
- announcement dismiss.
- mobile drawer open + Escape close.

PG04 AR/EN:
- campaign anchor targets present.
- valid demo form exposes the success/status state without network submission.
- mobile drawer open + Escape close.

## Asset / Licensing

`docs/ASSET-LICENSE-REGISTER-V1.md` registers:
- `ORX-MEDIA-007` — Manufacturer readiness hero — ORVEAX OWNED.
- `ORX-MEDIA-008` — Commercial enquiry hero — ORVEAX OWNED.

No third-party stock or TARGET/client asset entered PG03/PG04.

## C8 Gate

This record does **not** promote PG03 or PG04 to C8.

Before C8 / PASS / CLOSED:
1. deploy current `main` through the Cloudflare Test Environment; Manual Rebuild is temporarily acceptable;
2. open AR + EN routes from the real Cloudflare test URL on mobile and desktop;
3. confirm base paths/assets, responsive layout, RTL/LTR and interactions in the deployed runtime;
4. fix and retest any deployment-only defect;
5. then promote each page from C7 to C8.

M1 remains closed.

Copyright © ORVEAX.
