# ORIGEX — Project HQ V1

Product ID: ORX-P01  
Owner: ORVEAX  
Repository: `orveax/TARGET-HTML-Edition`  
Status: ACTIVE CONTROL DOCUMENT  
Last Updated: 2026-08-19 — M2 HOME FAMILY IMPLEMENTED / PG02–PG04 C7 CI QA PASS / CLOUDFLARE REVIEW PENDING

This is the operational entry point for ORIGEX. If another document conflicts with this HQ, use the authority order below and stop local improvisation.

## 1. Current Project State

```text
M0 — PRODUCT FOUNDATION: PASS / CLOSED
M1 — GLOBAL SYSTEM & COMPONENT FOUNDATION: PASS / CLOSED
M2 — GLOBAL SHELL & HOME FAMILY: IN PROGRESS
PG01 — HOME 01: C8 / PASS / CLOSED — MARKETPLACE VISUAL BENCHMARK — AR + EN
PG02 — HOME 02: C7 / IMPLEMENTED — CI QA PASS — CLOUDFLARE TEST REVIEW PENDING
PG03 — HOME 03: C7 / IMPLEMENTED — CI QA PASS — CLOUDFLARE TEST REVIEW PENDING
PG04 — LANDING / ONE PAGE: C7 / IMPLEMENTED — CI QA PASS — CLOUDFLARE TEST REVIEW PENDING
CLOUDFLARE TEST ENVIRONMENT: AVAILABLE VIA MANUAL REBUILD
CLOUDFLARE AUTO-DEPLOY: DEFERRED — PUSH TRIGGER NEEDS CORRECTION
M3–M8: NOT STARTED
```

M1 closure authority is `M1-QA-REPORT-V1.md` plus `M1-COMPONENT-IMPLEMENTATION-MAP.md`, `M1-CLOSURE-2026-08-19.md` and `M1-VENDOR-SHA256.txt`.

### PG01 authority
- Arabic: `ar/index.html`.
- English: `en/index.html`.
- Page contract: `page-design-profiles/pg01-home-01-v1.md`.
- Base closure: `PG01-CLOSURE-2026-08-19.md`.
- Marketplace visual closure: `PG01-MARKETPLACE-VISUAL-POLISH-2026-08-19.md`.
- Final rendered QA: 8/8 PASS.
- Final interaction QA: PASS.
- State: C8 / PASS / CLOSED.

### PG02 authority
- Arabic: `ar/home-02.html`.
- English: `en/home-02.html`.
- Page contract: `page-design-profiles/pg02-home-02-v1.md`.
- QA report: `PG02-QA-REPORT-V1.md`.
- Source/content/SEO/assets: PASS / failures 0.
- Rendered responsive: 8/8 PASS.
- Interaction: PASS.
- State: C7 / CI QA PASS; Cloudflare deployed-browser review required before C8.

### PG03 authority
- Arabic: `ar/home-03.html`.
- English: `en/home-03.html`.
- Page contract: `page-design-profiles/pg03-home-03-v1.md`.
- Manufacturer composition: `assets/css/origex-manufacturer.css`.
- Owned media: `assets/media/demo/hero-manufacturer-readiness.svg`.
- Combined QA authority: `PG03-PG04-HOME-FAMILY-QA-2026-08-19.md`.
- Source/content/SEO/assets: PASS / failures 0.
- Rendered responsive: AR/EN × 390/820/1366/1536 = 8/8 PASS.
- Interaction: desktop mega/announcement + mobile drawer PASS.
- Demo certification and illustrative export-market safeguards: PASS.
- State: C7 / CI QA PASS; Cloudflare deployed-browser review required before C8.

### PG04 authority
- Arabic: `ar/landing.html`.
- English: `en/landing.html`.
- Page contract: `page-design-profiles/pg04-landing-v1.md`.
- Landing composition: `assets/css/origex-landing.css`.
- Demo-form runtime: `assets/js/origex-landing.js`.
- Owned media: `assets/media/demo/hero-commercial-enquiry.svg`.
- Combined QA authority: `PG03-PG04-HOME-FAMILY-QA-2026-08-19.md`.
- Source/content/SEO/assets: PASS / failures 0.
- Rendered responsive: AR/EN × 390/820/1366/1536 = 8/8 PASS.
- Interaction: anchors + validation-only demo form + mobile drawer PASS.
- Form has no endpoint/network submission.
- State: C7 / CI QA PASS; Cloudflare deployed-browser review required before C8.

Deployment authority:
- `STAGING-PREVIEW-GATE-V1.md`.
- GitHub `main` is the source remote.
- Cloudflare Test Environment is the deployed test runtime.
- Manual Rebuild works and is accepted temporarily.
- Automatic deploy after push is currently degraded and explicitly deferred.
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
5. Domain authorities: technology, design, content, SEO, assets, QA and deployment preview.
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
- `PG03-PG04-HOME-FAMILY-QA-2026-08-19.md`
- `DOCUMENTATION-ARCHITECTURE.md`

### Reference Only
- `ABOUT-SOURCE-MAP.md`
- `HOMEPAGE-SOURCE-MAP.md`
- `PAGE-FIDELITY-MATRIX.md`
- `THEMEFOREST-BENCHMARK-2026-08.md`

## 6. Active Repository Structure

```text
/
├── index.html
├── README.md
├── CHANGELOG.md
├── ar/
│   ├── index.html              # PG01
│   ├── home-02.html            # PG02
│   ├── home-03.html            # PG03
│   └── landing.html            # PG04
├── en/
│   ├── index.html              # PG01
│   ├── home-02.html            # PG02
│   ├── home-03.html            # PG03
│   └── landing.html            # PG04
├── assets/
│   ├── brand/
│   ├── css/
│   │   ├── origex-tokens.css
│   │   ├── origex-foundation.css
│   │   ├── origex-components.css
│   │   ├── origex-compositions.css
│   │   ├── origex-marketplace-polish.css
│   │   ├── origex-distribution.css
│   │   ├── origex-manufacturer.css
│   │   ├── origex-landing.css
│   │   └── origex-shell.css
│   ├── media/demo/
│   │   ├── hero-trade-scene.svg
│   │   ├── hero-distribution-network.svg
│   │   ├── hero-manufacturer-readiness.svg
│   │   └── hero-commercial-enquiry.svg
│   ├── fonts/
│   ├── icons/
│   ├── js/
│   │   ├── config.js
│   │   ├── config-engine.js
│   │   ├── origex-ui.js
│   │   └── origex-landing.js
│   ├── patterns/
│   └── vendor/bootstrap/
├── preview/
├── qa/
│   ├── pg01-*/
│   ├── pg02-*/
│   └── pg03-pg04-home-family/
└── docs/
    ├── PG02-QA-REPORT-V1.md
    ├── PG03-PG04-HOME-FAMILY-QA-2026-08-19.md
    └── page-design-profiles/
        ├── pg01-home-01-v1.md
        ├── pg02-home-02-v1.md
        ├── pg03-home-03-v1.md
        └── pg04-landing-v1.md
```

M1 owns the reusable foundation. M2+ pages consume it and may not create competing local systems.

`origex-shell.css` remains the M1 shell. M2 page-family composition layers may assemble registered systems without reopening M1.

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

Current states:
- PG01 = **C8 / PASS / CLOSED — MARKETPLACE VISUAL BENCHMARK**.
- PG02 = **C7 / CI QA PASS — CLOUDFLARE REVIEW PENDING**.
- PG03 = **C7 / CI QA PASS — CLOUDFLARE REVIEW PENDING**.
- PG04 = **C7 / CI QA PASS — CLOUDFLARE REVIEW PENDING**.

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

1. Use Cloudflare Manual Rebuild to deploy current `main`.
2. Open PG02, PG03 and PG04 AR + EN through the real Cloudflare Test Environment on mobile + desktop.
3. Verify deployed assets/base paths, hierarchy, RTL/LTR and runtime interactions.
4. Fix/retest any deployed-environment defect.
5. Promote each page individually to C8 only after deployed review passes.
6. When PG01–PG04 all meet the M2 exit criteria, close M2 and open M3.
7. Repair Cloudflare Git auto-deploy in the deferred infrastructure session.

M1 remains closed unless a verified foundation defect requires a controlled QA fix.

Copyright © ORVEAX.
