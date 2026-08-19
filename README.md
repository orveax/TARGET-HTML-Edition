# ORIGEX — B2B Food Trading & Distribution HTML Template

**Product ID:** ORX-P01  
**Owner / Author:** ORVEAX  
**Status:** M1 closed — M2 active — PG01 C8 Marketplace Visual Benchmark — PG02 C7 CI QA PASS — Cloudflare review pending

ORIGEX is a premium Arabic-first bilingual HTML template product for B2B food trading, import, wholesale, distribution, manufacturers, suppliers and market-access workflows.

This repository is the commercial ORIGEX product. It is intentionally separated from the original TARGET client implementation.

## Start Here

**Canonical project control:** [`docs/PROJECT-HQ-V1.md`](docs/PROJECT-HQ-V1.md)

Do not start implementation from historical commits or reference/source-map files.

## Current State

```text
M0 — PRODUCT FOUNDATION: CLOSED / COMPLETE
M1 — GLOBAL SYSTEM & COMPONENT FOUNDATION: CLOSED / COMPLETE
M2 — GLOBAL SHELL & HOME FAMILY: IN PROGRESS
PG01 — HOME 01: C8 / PASS / CLOSED — MARKETPLACE VISUAL BENCHMARK — AR + EN
PG02 — HOME 02: C7 / IMPLEMENTED — CI QA PASS — CLOUDFLARE TEST REVIEW PENDING
PG03–PG32: gated by their own content/design/SEO entry requirements
CLOUDFLARE TEST ENVIRONMENT: AVAILABLE VIA MANUAL REBUILD
CLOUDFLARE AUTO-DEPLOY: DEFERRED — PUSH TRIGGER NEEDS CORRECTION
```

## Frozen V1 Stack

- HTML5
- CSS3
- Bootstrap 5.3.8 — infrastructure/layout foundation, packaged locally
- Vanilla JavaScript
- ORIGEX Design System
- `config.js` customization layer
- JSON structured data where approved
- Arabic RTL + English LTR

No React, Vue, Astro runtime, Tailwind, jQuery, mandatory Node/build process or heavy animation framework in the V1 buyer package.

## Scope

- 32 unique layouts
- Arabic + English ready pages
- V1 Main Features only
- Additional Features preserved in V1.1 backlog
- static-first, responsive, accessible and SEO-ready architecture

See [`docs/SCOPE-FREEZE-V1-FINAL.md`](docs/SCOPE-FREEZE-V1-FINAL.md).

## Core Control Files

- [`docs/PROJECT-HQ-V1.md`](docs/PROJECT-HQ-V1.md) — current state and authority map
- [`docs/IMPLEMENTATION-STATUS-V1.md`](docs/IMPLEMENTATION-STATUS-V1.md) — live execution tracker
- [`docs/PROJECT-RULES-V1.md`](docs/PROJECT-RULES-V1.md) — implementation rules
- [`docs/QA-DEFINITION-OF-DONE-V1.md`](docs/QA-DEFINITION-OF-DONE-V1.md) — page/milestone/release gates
- [`docs/STAGING-PREVIEW-GATE-V1.md`](docs/STAGING-PREVIEW-GATE-V1.md) — Cloudflare deployed-browser gate
- [`docs/ASSET-LICENSE-REGISTER-V1.md`](docs/ASSET-LICENSE-REGISTER-V1.md) — dependencies/assets/licensing

## M1 Closure

M1 closure authority:
- [`docs/M1-QA-REPORT-V1.md`](docs/M1-QA-REPORT-V1.md)
- [`docs/M1-COMPONENT-IMPLEMENTATION-MAP.md`](docs/M1-COMPONENT-IMPLEMENTATION-MAP.md)
- [`docs/M1-CLOSURE-2026-08-19.md`](docs/M1-CLOSURE-2026-08-19.md)
- [`docs/M1-VENDOR-SHA256.txt`](docs/M1-VENDOR-SHA256.txt)

M1 is frozen unless a verified foundation defect requires a controlled fix.

## PG01 Marketplace Benchmark

PG01 authority:
- [`docs/page-design-profiles/pg01-home-01-v1.md`](docs/page-design-profiles/pg01-home-01-v1.md)
- [`docs/PG01-CLOSURE-2026-08-19.md`](docs/PG01-CLOSURE-2026-08-19.md)
- [`docs/PG01-MARKETPLACE-VISUAL-POLISH-2026-08-19.md`](docs/PG01-MARKETPLACE-VISUAL-POLISH-2026-08-19.md)
- [`ar/index.html`](ar/index.html)
- [`en/index.html`](en/index.html)

Final PG01 QA:
- rendered responsive — 8/8 PASS;
- interaction — PASS;
- marketplace visual polish — PASS;
- no TARGET client data/assets or untracked buyer-package assets.

PG01 is **C8 / PASS / CLOSED — MARKETPLACE VISUAL BENCHMARK**.

## PG02 — Wholesale & Distribution

PG02 authority:
- [`docs/page-design-profiles/pg02-home-02-v1.md`](docs/page-design-profiles/pg02-home-02-v1.md)
- [`docs/PG02-QA-REPORT-V1.md`](docs/PG02-QA-REPORT-V1.md)
- [`ar/home-02.html`](ar/home-02.html)
- [`en/home-02.html`](en/home-02.html)

Implemented V1 scope:
- distribution-led hero;
- channels overview;
- warehouse / coverage story;
- product categories;
- distribution process;
- Demo metrics;
- route-to-market blocks;
- RFQ CTA.

PG02 QA completed in CI:
- source/content/SEO/assets — PASS / failures 0;
- rendered responsive — **8/8 PASS** at 390 / 820 / 1366 / 1536 in AR+EN;
- runtime interaction — PASS / failures 0;
- visual-review snapshots — generated for AR/EN Mobile + Desktop;
- new distribution media — ORVEAX-owned and registered.

Current state:

> **PG02 = C7 IMPLEMENTED — CI QA PASS — CLOUDFLARE TEST REVIEW PENDING.**

It is not C8 yet because final deployed-browser review must use the real Cloudflare Test Environment.

## Deployment Model

Canonical test flow:

```text
GitHub `main`
    ↓
Cloudflare Test Environment
```

Cloudflare currently works with **Manual Rebuild**. Automatic deployment after every GitHub push is degraded and has been explicitly deferred to the next infrastructure session.

GitHub Pages is **not** used by ORIGEX.

Manual Rebuild is temporarily acceptable for page review. The active revision must still be tested through the Cloudflare URL before a page closes at C8.

## Implementation Rule

Before a page is built:
1. confirm PG ID / filename;
2. confirm V1 Main Features;
3. freeze content at C6;
4. complete the Page Design Profile;
5. complete the SEO & Page Identity Contract;
6. use registered components only;
7. identify asset/license needs;
8. build Arabic and English together;
9. run source/rendered/runtime QA;
10. review the current revision through Cloudflare;
11. close only at C8 / PASS.

## Current Next Action

For PG02 closure:
1. deploy current `main` with Cloudflare Manual Rebuild when ready for external review;
2. open `/ar/home-02.html` and `/en/home-02.html` through the test domain on mobile + desktop;
3. verify deployed assets/base paths, RTL/LTR, layout and interactions;
4. correct/retest any environment defect;
5. promote PG02 to C8 only after that review passes.

Cloudflare auto-deploy repair remains deferred to the next infrastructure session.

## Repository Rule

Current branch policy is `main` only unless ORVEAX explicitly changes it.

Historical TARGET-derived source maps may inform fidelity, but client identity, contacts, proprietary data, client assets and unsupported claims must never enter ORIGEX.

Copyright © ORVEAX.
