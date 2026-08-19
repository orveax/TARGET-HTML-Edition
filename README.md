# ORIGEX — B2B Food Trading & Distribution HTML Template

**Product ID:** ORX-P01  
**Owner / Author:** ORVEAX  
**Status:** M1 closed — M2 active — PG01 C8 / PASS / MARKETPLACE VISUAL BENCHMARK — Staging Preview BLOCKED

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
PG01 MARKETPLACE VISUAL POLISH CR: PASS / CLOSED
PG01 STAGING PREVIEW: BLOCKED — GitHub Pages not enabled
PG02 — HOME 02: C0 / ENTRY GATE REQUIRED / CODE BLOCKED UNTIL STAGING PASS
PG03–PG32: gated by their own content/design/SEO entry requirements
```

M1 closure authority:
- [`docs/M1-QA-REPORT-V1.md`](docs/M1-QA-REPORT-V1.md)
- [`docs/M1-COMPONENT-IMPLEMENTATION-MAP.md`](docs/M1-COMPONENT-IMPLEMENTATION-MAP.md)
- [`docs/M1-CLOSURE-2026-08-19.md`](docs/M1-CLOSURE-2026-08-19.md)
- [`docs/M1-VENDOR-SHA256.txt`](docs/M1-VENDOR-SHA256.txt)

PG01 authority, implementation and closure:
- [`docs/page-design-profiles/pg01-home-01-v1.md`](docs/page-design-profiles/pg01-home-01-v1.md)
- [`docs/PG01-QA-REPORT-V1.md`](docs/PG01-QA-REPORT-V1.md)
- [`docs/PG01-CLOSURE-2026-08-19.md`](docs/PG01-CLOSURE-2026-08-19.md)
- [`docs/PG01-MARKETPLACE-VISUAL-POLISH-2026-08-19.md`](docs/PG01-MARKETPLACE-VISUAL-POLISH-2026-08-19.md)
- [`ar/index.html`](ar/index.html)
- [`en/index.html`](en/index.html)
- [`qa/pg01-rendered/`](qa/pg01-rendered/)
- [`qa/pg01-interaction/`](qa/pg01-interaction/)
- [`qa/pg01-visual-review/`](qa/pg01-visual-review/)

Staging authority:
- [`index.html`](index.html) — Arabic-first root language entry
- [`docs/STAGING-PREVIEW-GATE-V1.md`](docs/STAGING-PREVIEW-GATE-V1.md)
- [`.github/workflows/deploy-staging-pages.yml`](.github/workflows/deploy-staging-pages.yml)
- [`staging/deployment-status.md`](staging/deployment-status.md)

A hard audit on 2026-08-19 removed pre-foundation Build 02–05 implementation and superseded planning files from the active tree. Git history remains the archive.

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

- [`PROJECT-HQ-V1.md`](docs/PROJECT-HQ-V1.md) — current state and authority map
- [`PROJECT-RULES-V1.md`](docs/PROJECT-RULES-V1.md) — implementation rules
- [`IMPLEMENTATION-STATUS-V1.md`](docs/IMPLEMENTATION-STATUS-V1.md) — live execution tracker
- [`PRODUCT-FOUNDATION-COMPLETE-V1.md`](docs/PRODUCT-FOUNDATION-COMPLETE-V1.md) — M0 closure
- [`MILESTONE-PLAN-V1.md`](docs/MILESTONE-PLAN-V1.md) — delivery sequence
- [`QA-DEFINITION-OF-DONE-V1.md`](docs/QA-DEFINITION-OF-DONE-V1.md) — page/milestone/release gates
- [`STAGING-PREVIEW-GATE-V1.md`](docs/STAGING-PREVIEW-GATE-V1.md) — deployed browser-preview gate
- [`ASSET-LICENSE-REGISTER-V1.md`](docs/ASSET-LICENSE-REGISTER-V1.md) — dependencies/assets/licensing

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
9. close page QA only after full page QA and Content C8;
10. for the first representative page in a page family, pass the Staging Preview Gate before coding the next page in that family.

## PG01 Marketplace Benchmark

PG01 passed the original page gate and the approved Marketplace Visual Polish Change Request on 2026-08-19.

Final benchmark includes:
- stronger B2B trade/logistics Hero visual;
- differentiated category presentation;
- clearer trust/process hierarchy;
- dark role-based tonal break;
- four ORVEAX-owned fictional product packshots;
- refined supplier CTA;
- no stock-photo dependency or new runtime plugin.

Final QA:
- source/content/SEO/asset QA — PASS;
- rendered responsive QA — **8/8 PASS** across AR/EN at 390, 820, 1366 and 1536 widths;
- runtime interaction QA — **PASS** for AR/EN desktop/mobile mega menu, Escape behavior, FAQ, announcement and mobile drawer;
- final rendered evidence: `5ab1edb6fe2a17adc41857790170097dfad57f0f`;
- final interaction evidence: `b3d12beb103492144f4c5fc690ef15eedd49eef4`;
- final visual snapshots: `e1c09173757defc6992ac162447990f2ffc76f5a`;
- all new demo media is registered as ORVEAX-owned.

The QA cycle caught a Hero grid overflow caused by the inherited aspect ratio; it was corrected in the M2 polish layer before closure. M1 remained closed.

PG01 is now **C8 / PASS / CLOSED — MARKETPLACE VISUAL BENCHMARK** at page/code level.

Its independent Staging Preview Gate is currently **BLOCKED** because GitHub Pages is not enabled for the repository. The deployment workflow successfully prepares the public artifact but cannot configure/deploy Pages yet, so no public Page URL exists.

## Current Next Action

Resolve PG01 staging before PG02 code begins:

1. enable GitHub Pages once at `Repository → Settings → Pages`;
2. set `Build and deployment → Source → GitHub Actions`;
3. rerun `Deploy ORIGEX Staging`;
4. verify root + AR + EN externally on mobile and desktop;
5. mark `STAGING PASS`;
6. continue PG02 Content Contract → C6 → Design Profile → SEO Contract;
7. begin PG02 AR+EN code only after its entry gate and PG01 staging gate both pass.

PG02 content/design/SEO preparation may continue while staging is blocked; its code may not.

## Repository Rule

Current branch policy is `main` only unless ORVEAX explicitly changes it.

Historical TARGET-derived source maps may inform fidelity, but client identity, contacts, proprietary data, client assets and unsupported claims must never enter ORIGEX.

Copyright © ORVEAX.
