# ORIGEX — PG02 Home 02 QA Report V1

Product ID: ORX-P01  
Page ID: PG02 — Home 02 — Wholesale & Distribution  
Milestone: M2 — Global Shell & Home Family  
Date: 2026-08-19  
Current State: **C7 IMPLEMENTED — CI QA PASS — CLOUDFLARE TEST REVIEW PENDING**

## Implemented Pair

- Arabic: `ar/home-02.html`
- English: `en/home-02.html`
- Entry authority: `docs/page-design-profiles/pg02-home-02-v1.md`

PG02 implements the eight frozen V1 Main Features only:
1. distribution-led hero;
2. channels overview;
3. warehouse / coverage story;
4. product categories;
5. distribution process;
6. key metrics;
7. route-to-market blocks;
8. RFQ CTA.

## Source / Content / SEO / Asset QA — PASS

Evidence:
- `qa/pg02-source/report.json`
- evidence commit: `c396b2024bb77ba5d39bd47b756a794ab20431cd`

Final result: **failures 0**.

Passed in Arabic and English:
- language and direction;
- one canonical H1;
- unique IDs;
- SEO title;
- canonical URL;
- AR / EN / x-default hreflang;
- Open Graph baseline;
- valid WebPage structured data;
- mandatory fictional demo disclosure;
- all eight frozen section intents;
- explicit Demo metric qualification;
- fictional distributor disclosure;
- no TARGET/client/CDN leakage;
- local Bootstrap/runtime;
- local linked assets;
- canonical internal filenames.

The first source run reported a false JSON-LD failure caused by the QA parser continuing to collect text after the JSON-LD script ended. The QA parser was corrected and rerun; page source did not require a JSON-LD correction.

## Rendered Responsive QA — PASS

Evidence:
- `qa/pg02-rendered/report.json`
- evidence commit: `f2d25834ac57f2b00c7218cd5bea1376a2ee2d3c`

Final result: **8 / 8 PASS — failures 0**.

Matrix:
- AR 390×844 — PASS.
- AR 820×1180 — PASS.
- AR 1366×900 — PASS.
- AR 1536×960 — PASS.
- EN 390×844 — PASS.
- EN 820×1180 — PASS.
- EN 1366×900 — PASS.
- EN 1536×960 — PASS.

Validated:
- RTL / LTR direction;
- zero horizontal/offscreen overflow in the automated matrix;
- touch-target baseline;
- hero/media rendering;
- channel and route-to-market section rendering;
- local font readiness.

## Runtime Interaction QA — PASS

Evidence:
- `qa/pg02-interaction/report.json`
- evidence commit: `a6d7488f96c2a3085f90a7ec319dcb2a468be2f0`

Final result: **failures 0**.

Passed independently in Arabic and English:
- desktop mega menu present/open;
- Escape closes mega menu;
- announcement dismiss;
- channel anchor target exists;
- mobile drawer present/open;
- Escape closes drawer and restores scroll state;
- language link exists in mobile navigation.

No FAQ interaction is required by PG02 V1 scope.

## Visual Review Evidence

Evidence:
- `qa/pg02-visual-review/`
- manifest: `qa/pg02-visual-review/manifest.json`
- evidence commit: `38d4c851f894a27fc88eb7ad36652d46e46e1beb`

Generated review pairs:
- AR Mobile 390 — full + hero.
- EN Mobile 390 — full + hero.
- AR Desktop 1536 — full + hero.
- EN Desktop 1536 — full + hero.

These snapshots confirm browser-rendered evidence exists for the implemented page pair. Final external commercial visual acceptance remains tied to the real Cloudflare Test Environment review.

## Asset / License Record

New PG02 media:
- `assets/media/demo/hero-distribution-network.svg`
- Asset ID: ORX-MEDIA-006
- Owner: ORVEAX
- Status: ORVEAX OWNED / distributable demo media.

Registered in `docs/ASSET-LICENSE-REGISTER-V1.md`.

No TARGET asset, supplier brand, third-party packaging, stock photography or remote runtime dependency entered PG02.

## Architecture

New M2 reusable composition layer:
- `assets/css/origex-distribution.css`

This layer composes existing ORIGEX registered primitives/components for wholesale/distribution contexts. It does not create a parallel design system or reopen M1.

## Deployment Gate

Canonical runtime:

```text
GitHub `main` → Cloudflare Test Environment
```

Current infrastructure condition confirmed by ORVEAX administrator:
- Manual Cloudflare **Rebuild** works.
- GitHub push → Cloudflare automatic deployment is currently degraded.
- Auto-deploy correction is deferred to the next infrastructure session.

PG02 must therefore remain C7 until the current `main` revision is deployed through Cloudflare and reviewed externally on AR/EN Mobile + Desktop.

## Current Decision

**PG02 = C7 IMPLEMENTED — CI QA PASS — CLOUDFLARE TEST REVIEW PENDING.**

Do not promote to C8 / PASS / CLOSED until:
1. current revision is deployed to the Cloudflare Test Environment;
2. `/ar/home-02.html` and `/en/home-02.html` are opened through the real test URL;
3. deployed CSS/fonts/icons/media/base paths are verified;
4. external mobile + desktop visual/smoke review passes;
5. any deployed-environment defects are corrected and retested;
6. documentation is synchronized to C8.

Copyright © ORVEAX.
