# ORIGEX — Project HQ V1

Product ID: ORX-P01  
Owner: ORVEAX  
Repository: `orveax/TARGET-HTML-Edition`  
Status: ACTIVE CONTROL DOCUMENT  
Last Updated: 2026-08-19 — M2 / PG01 MARKETPLACE BENCHMARK CLOSED / PG02 C7 CI QA PASS / CLOUDFLARE REVIEW PENDING

This is the operational entry point for ORIGEX. If another document conflicts with this HQ, use the authority order below and stop local improvisation.

## 1. Current Project State

```text
M0 — PRODUCT FOUNDATION: PASS / CLOSED
M1 — GLOBAL SYSTEM & COMPONENT FOUNDATION: PASS / CLOSED
M2 — GLOBAL SHELL & HOME FAMILY: IN PROGRESS
PG01 — HOME 01: C8 / PASS / CLOSED — MARKETPLACE VISUAL BENCHMARK — AR + EN
PG02 — HOME 02: C7 / IMPLEMENTED — CI QA PASS — CLOUDFLARE TEST REVIEW PENDING
PG03–PG04: gated by C6 + Design Profile + SEO Contract
CLOUDFLARE TEST ENVIRONMENT: AVAILABLE VIA MANUAL REBUILD
CLOUDFLARE AUTO-DEPLOY: DEFERRED — PUSH TRIGGER NEEDS CORRECTION
M3–M8: NOT STARTED
```

M1 closure authority is `M1-QA-REPORT-V1.md` plus `M1-COMPONENT-IMPLEMENTATION-MAP.md`, `M1-CLOSURE-2026-08-19.md` and `M1-VENDOR-SHA256.txt`.

PG01 closure authority:
- Arabic: `ar/index.html`
- English: `en/index.html`
- Page contract: `page-design-profiles/pg01-home-01-v1.md`
- Base closure: `PG01-CLOSURE-2026-08-19.md`
- Marketplace visual closure: `PG01-MARKETPLACE-VISUAL-POLISH-2026-08-19.md`
- Final rendered QA: `5ab1edb6fe2a17adc41857790170097dfad57f0f` — 8/8 PASS.
- Final interaction QA: `b3d12beb103492144f4c5fc690ef15eedd49eef4` — PASS.

PG02 current authority:
- Arabic: `ar/home-02.html`.
- English: `en/home-02.html`.
- Page contract: `page-design-profiles/pg02-home-02-v1.md`.
- QA report: `PG02-QA-REPORT-V1.md`.
- Content: C7 / IMPLEMENTED from frozen C6 contract.
- Source/content/SEO/assets QA: `c396b2024bb77ba5d39bd47b756a794ab20431cd` — PASS / failures 0.
- Rendered responsive QA: `f2d25834ac57f2b00c7218cd5bea1376a2ee2d3c` — 8/8 PASS / failures 0.
- Interaction QA: `a6d7488f96c2a3085f90a7ec319dcb2a468be2f0` — PASS / failures 0.
- Visual snapshot evidence: `38d4c851f894a27fc88eb7ad36652d46e46e1beb`.
- Final state: C7 / CI QA PASS; Cloudflare browser review still required before C8.

Deployment authority:
- `STAGING-PREVIEW-GATE-V1.md`.
- GitHub `main` is the source remote.
- Cloudflare Test Environment is the deployed test runtime.
- Manual Rebuild works and is accepted temporarily.
- Automatic deploy after push is currently degraded and explicitly deferred to the next infrastructure session.
- GitHub Pages is not part of the ORIGEX deployment model.

The pre-foundation Build 02–05 implementation was removed from the active tree during the 2026-08-19 hard audit. Git history remains the archive. No removed pre-freeze file is an implementation authority.

## 2. Product Definition

ORIGEX is a premium Arabic-first bilingual HTML template for B2B food trading, import, wholesale, distribution, manufacturers, suppliers and market-access workflows.

V1 ships 32 unique layouts in Arabic and English, with Main Features only. Additional Features remain in the V1.1 backlog.

## 3. Frozen Technology

- HTML5
- CSS3
- Bootstrap **5.3.8** as infrastructure/layout foundation, packaged locally
- Vanilla JavaScript
- ORIGEX Design System
- `config.js` simple customization layer
- JSON structured data where approved
- no React / Vue / Astro runtime / Tailwind / jQuery / mandatory build pipeline

Bootstrap is infrastructure, never the ORIGEX visual identity.

## 4. Authority Order

When documents overlap, use this order:

1. `PROJECT-HQ-V1.md` — operational state and authority map.
2. `PRODUCT-FOUNDATION-COMPLETE-V1.md` — foundation closure authority.
3. `SCOPE-FREEZE-V1-FINAL.md` — V1 page/feature scope.
4. `FOUNDATION-FREEZE-V1.md` — frozen product systems.
5. Domain authorities: technology, design, content, SEO, assets, QA and staging preview.
6. `MILESTONE-PLAN-V1.md` — delivery sequence.
7. Reference/source-map documents — historical evidence only.

No reference document may override a frozen authority.

## 5. Canonical Authority Map

### Product / Governance
- `PRODUCT-FOUNDATION-COMPLETE-V1.md`
- `SCOPE-FREEZE-V1-FINAL.md`
- `MILESTONE-PLAN-V1.md`
- `PROJECT-RULES-V1.md`
- `IMPLEMENTATION-STATUS-V1.md`
- `RELEASE-VERSIONING-POLICY-V1.md`
- `V1.1-ADDITIONAL-FEATURES-BACKLOG.md`

### Technology / Code
- `TECH-STACK-V1.md`
- `CODE-ARCHITECTURE-V1.md`
- `CONFIGURATION.md`
- `DATA-SCHEMA-V1.md`

### Design System
- `BRAND-SYSTEM-V1.md`
- `DESIGN-SYSTEM-HIERARCHY-V1.md`
- `COMPONENT-REGISTRY-V1.md`
- `COMPONENT-DESIGN-RULES-V1.md`
- `PAGE-DESIGN-PROFILE-TEMPLATE-V1.md`
- `ICON-SYSTEM-V1.md`
- `PATTERN-SYSTEM-V1.md`
- `IMAGE-MEDIA-SYSTEM-V1.md`

### Content / SEO
- `CONTENT-SYSTEM-V1.md`
- `MASTER-CONTENT-ARCHITECTURE-V1.md`
- `DEMO-CONTENT-DATASET-V1.md`
- `SEO-METADATA-PAGE-NAMING-V1.md`

### Demo / Assets / QA / Deployment
- `DEMO-VS-PRODUCTION-POLICY-V1.md`
- `ASSET-LICENSE-REGISTER-V1.md`
- `QA-DEFINITION-OF-DONE-V1.md`
- `STAGING-PREVIEW-GATE-V1.md`
- `M1-QA-REPORT-V1.md`
- `M1-COMPONENT-IMPLEMENTATION-MAP.md`
- `PG02-QA-REPORT-V1.md`
- `DOCUMENTATION-ARCHITECTURE.md`

### Reference Only
- `ABOUT-SOURCE-MAP.md`
- `HOMEPAGE-SOURCE-MAP.md`
- `PAGE-FIDELITY-MATRIX.md`
- `THEMEFOREST-BENCHMARK-2026-08.md`

## 6. Active Repository Structure

```text
/
├── index.html                  # Arabic-first language entry
├── README.md
├── CHANGELOG.md
├── ar/
│   ├── index.html              # PG01 Arabic
│   └── home-02.html            # PG02 Arabic — C7
├── en/
│   ├── index.html              # PG01 English
│   └── home-02.html            # PG02 English — C7
├── assets/
│   ├── brand/
│   ├── css/
│   │   ├── origex-tokens.css
│   │   ├── origex-foundation.css
│   │   ├── origex-components.css
│   │   ├── origex-compositions.css
│   │   ├── origex-marketplace-polish.css
│   │   ├── origex-distribution.css
│   │   └── origex-shell.css
│   ├── media/demo/
│   │   ├── hero-trade-scene.svg
│   │   └── hero-distribution-network.svg
│   ├── fonts/
│   ├── icons/
│   ├── js/
│   ├── patterns/
│   └── vendor/bootstrap/
├── preview/
├── qa/
│   ├── pg01-*/
│   └── pg02-*/
└── docs/
    ├── PG02-QA-REPORT-V1.md
    └── page-design-profiles/
        ├── pg01-home-01-v1.md
        └── pg02-home-02-v1.md
```

M1 owns the reusable foundation. M2+ pages consume it and may not create competing local systems.

`origex-shell.css` remains the M1 shell. `origex-compositions.css`, `origex-marketplace-polish.css` and `origex-distribution.css` are M2 composition/refinement layers and may not override the frozen architecture with page-local systems.

## 7. Page Entry and Exit Gate

A page may enter implementation only when all are true:
- Page ID/filename comes from `SEO-METADATA-PAGE-NAMING-V1.md`.
- V1 Main Features match `SCOPE-FREEZE-V1-FINAL.md`.
- Content reaches C6 — FROZEN.
- Page Design Profile is complete.
- SEO & Page Identity Contract is complete.
- Required components/variants already exist in the registry.
- required assets/licenses are known.

Implementation proceeds AR + EN together.

A page reaches C8 only after:
- source/content/SEO/asset QA;
- rendered responsive QA;
- runtime interaction QA where applicable;
- deployed Cloudflare Test Environment smoke/visual review;
- documentation synchronization.

PG01 is **C8 / PASS / CLOSED — MARKETPLACE VISUAL BENCHMARK**.

PG02 is **C7 IMPLEMENTED — CI QA PASS — CLOUDFLARE TEST REVIEW PENDING**. Do not promote it to C8 until the current revision is manually/automatically deployed to Cloudflare and reviewed externally.

Cloudflare auto-deploy degradation is an operational issue, not a code-build blocker while Manual Rebuild remains available.

## 8. Change Classification

After foundation closure, every new request is one of:
1. Bug / defect.
2. Verified content or SEO correction.
3. Formal Design System / Architecture / Product Governance Change Request.
4. V1.1+ backlog.

There is no fifth category called “quick local tweak”.

## 9. Legacy Rule

- Removed legacy remains recoverable through Git history.
- Do not restore deleted pre-freeze HTML/CSS/JS into the active tree.
- Do not recreate superseded planning/candidate documents.
- Historical source maps are reference-only.
- Temporary lifecycle filenames must not become canonical authorities.

## 10. Next Action

1. Use Cloudflare Manual Rebuild to deploy the current `main` revision when external review is performed.
2. Open `/ar/home-02.html` and `/en/home-02.html` through the real Cloudflare Test Environment on mobile + desktop.
3. Verify deployed assets/base paths, layout hierarchy, RTL/LTR and runtime interactions.
4. Fix/retest any deployed-environment defect.
5. Promote PG02 to C8 / PASS / CLOSED only after this review passes.
6. Repair Cloudflare Git auto-deploy in the deferred infrastructure session.
7. PG03 Content/Design/SEO preparation may proceed, but PG02 remains open at C7 until Cloudflare review closes it.

M1 remains closed unless a verified foundation defect requires a controlled QA fix.

Copyright © ORVEAX.
