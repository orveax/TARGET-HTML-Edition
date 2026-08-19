# ORIGEX — Project HQ V1

Product ID: ORX-P01  
Owner: ORVEAX  
Repository: `orveax/TARGET-HTML-Edition`  
Status: ACTIVE CONTROL DOCUMENT  
Last Updated: 2026-08-19 — M2 / PG01 QA

This is the operational entry point for ORIGEX. If another document conflicts with this HQ, use the authority order below and stop local improvisation.

## 1. Current Project State

```text
M0 — PRODUCT FOUNDATION: PASS / CLOSED
M1 — GLOBAL SYSTEM & COMPONENT FOUNDATION: PASS / CLOSED
M2 — GLOBAL SHELL & HOME FAMILY: IN PROGRESS
PG01 — HOME 01: C7 IMPLEMENTED / AR + EN / QA IN PROGRESS
PG02–PG04: gated by C6 + Design Profile + SEO Contract
M3–M8: NOT STARTED
```

M1 closure authority is `M1-QA-REPORT-V1.md` plus `M1-COMPONENT-IMPLEMENTATION-MAP.md`, `M1-CLOSURE-2026-08-19.md` and `M1-VENDOR-SHA256.txt`.

PG01 source:
- Arabic: `ar/index.html`
- English: `en/index.html`
- Page contract: `page-design-profiles/pg01-home-01-v1.md`

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
5. Domain authorities: technology, design, content, SEO, assets, QA.
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
- V1.1 Content Pack authorities

### Demo / Assets / QA
- `DEMO-VS-PRODUCTION-POLICY-V1.md`
- `ASSET-LICENSE-REGISTER-V1.md`
- `QA-DEFINITION-OF-DONE-V1.md`
- `M1-QA-REPORT-V1.md`
- `M1-COMPONENT-IMPLEMENTATION-MAP.md`
- `DOCUMENTATION-ARCHITECTURE.md`

### Reference Only
- `ABOUT-SOURCE-MAP.md`
- `HOMEPAGE-SOURCE-MAP.md`
- `PAGE-FIDELITY-MATRIX.md`
- `THEMEFOREST-BENCHMARK-2026-08.md`

Reference files inform fidelity/research; they do not define current architecture.

## 6. Active Repository Structure

```text
/
├── README.md
├── CHANGELOG.md
├── ar/
│   └── index.html              # PG01 Arabic — C7 / QA
├── en/
│   └── index.html              # PG01 English — C7 / QA
├── assets/
│   ├── brand/
│   ├── css/
│   │   ├── origex-tokens.css
│   │   ├── origex-foundation.css
│   │   ├── origex-components.css
│   │   └── origex-shell.css
│   ├── fonts/
│   ├── icons/
│   ├── js/
│   │   ├── config.js
│   │   ├── config-engine.js
│   │   └── origex-ui.js
│   ├── patterns/
│   └── vendor/bootstrap/
├── preview/
│   ├── m1-components-ar.html
│   └── m1-components-en.html
└── docs/
```

M1 owns the reusable foundation. M2+ pages consume it and may not create competing local systems.

## 7. Page Entry Gate

A page may enter implementation only when all are true:

- Page ID/filename comes from `SEO-METADATA-PAGE-NAMING-V1.md`.
- V1 Main Features match `SCOPE-FREEZE-V1-FINAL.md`.
- Content reaches C6 — FROZEN.
- Page Design Profile is complete.
- SEO & Page Identity Contract is complete.
- Required components/variants already exist in the registry.
- required assets/licenses are known.

Then implementation proceeds AR + EN together and exits only at Content C8 / Page QA PASS.

PG01 satisfied the entry gate and is now C7 / QA. Its current page-level QA must complete before PG01 is closed.

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
- A filename containing `candidate`, `exploration`, `gate-XX`, `48-hour`, `old`, `final-v2`, or similar temporary lifecycle language must not become a new canonical authority.

## 10. Next Action

Complete PG01 page QA in this order:

1. Arabic RTL responsive QA.
2. English LTR responsive QA.
3. Header / mega menu / mobile drawer / accordion / floating actions interaction QA.
4. Content parity and demo-claim/disclosure scan.
5. SEO/Page Identity contract verification.
6. local asset/runtime reference scan and console/broken-reference review where available.
7. close PG01 at Content C8 only after page QA passes.
8. prepare PG02 through C6 + Page Design Profile + SEO Contract before its code begins.

M1 remains closed unless a verified foundation defect requires a controlled QA fix.

Copyright © ORVEAX.
