# ORIGEX — Project HQ V1

Product ID: ORX-P01  
Owner: ORVEAX  
Repository: `orveax/TARGET-HTML-Edition`  
Status: ACTIVE CONTROL DOCUMENT  
Last Updated: 2026-08-19 — M2 / PG01 CLOSED / STAGING BLOCKED

This is the operational entry point for ORIGEX. If another document conflicts with this HQ, use the authority order below and stop local improvisation.

## 1. Current Project State

```text
M0 — PRODUCT FOUNDATION: PASS / CLOSED
M1 — GLOBAL SYSTEM & COMPONENT FOUNDATION: PASS / CLOSED
M2 — GLOBAL SHELL & HOME FAMILY: IN PROGRESS
PG01 — HOME 01: C8 / PASS / CLOSED — AR + EN
PG01 STAGING PREVIEW: BLOCKED — GitHub Pages not enabled
PG02 — HOME 02: C0 / ENTRY GATE REQUIRED / CODE BLOCKED UNTIL PG01 STAGING PASS
PG03–PG04: gated by C6 + Design Profile + SEO Contract
M3–M8: NOT STARTED
```

M1 closure authority is `M1-QA-REPORT-V1.md` plus `M1-COMPONENT-IMPLEMENTATION-MAP.md`, `M1-CLOSURE-2026-08-19.md` and `M1-VENDOR-SHA256.txt`.

PG01 closure authority:
- Arabic: `ar/index.html`
- English: `en/index.html`
- Page contract: `page-design-profiles/pg01-home-01-v1.md`
- Source/SEO QA: `PG01-QA-REPORT-V1.md`
- Closure: `PG01-CLOSURE-2026-08-19.md`
- Rendered evidence: `../qa/pg01-rendered/`
- Interaction evidence: `../qa/pg01-interaction/`
- Visual review: `../qa/pg01-visual-review/`

PG01 staging authority:
- Root language entry: `../index.html`
- Deployment workflow: `../.github/workflows/deploy-staging-pages.yml`
- Staging gate: `STAGING-PREVIEW-GATE-V1.md`
- Deployment evidence: `../staging/deployment-status.md`
- Current deployment state: **BLOCKED — repository GitHub Pages capability is not enabled**.

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
- V1.1 Content Pack authorities

### Demo / Assets / QA / Staging
- `DEMO-VS-PRODUCTION-POLICY-V1.md`
- `ASSET-LICENSE-REGISTER-V1.md`
- `QA-DEFINITION-OF-DONE-V1.md`
- `STAGING-PREVIEW-GATE-V1.md`
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
├── index.html                  # staging root / Arabic-first language entry
├── README.md
├── CHANGELOG.md
├── ar/
│   └── index.html              # PG01 Arabic — C8 / CLOSED
├── en/
│   └── index.html              # PG01 English — C8 / CLOSED
├── assets/
│   ├── brand/
│   ├── css/
│   │   ├── origex-tokens.css
│   │   ├── origex-foundation.css
│   │   ├── origex-components.css
│   │   ├── origex-compositions.css
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
├── qa/
│   ├── pg01-rendered/
│   ├── pg01-interaction/
│   └── pg01-visual-review/
├── staging/
│   └── deployment-status.md
├── .github/workflows/
│   └── deploy-staging-pages.yml
└── docs/
```

M1 owns the reusable foundation. M2+ pages consume it and may not create competing local systems.

`origex-compositions.css` is an M2 reusable F07 media-composition layer built on top of the frozen M1 foundation; it does not reopen M1 or create an unregistered component family.

The staging workflow publishes only `index.html`, `ar/`, `en/` and `assets/`; internal `docs/`, `qa/` and `.github/` content are excluded from the public artifact.

## 7. Page Entry Gate

A page may enter implementation only when all are true:

- Page ID/filename comes from `SEO-METADATA-PAGE-NAMING-V1.md`.
- V1 Main Features match `SCOPE-FREEZE-V1-FINAL.md`.
- Content reaches C6 — FROZEN.
- Page Design Profile is complete.
- SEO & Page Identity Contract is complete.
- Required components/variants already exist in the registry.
- required assets/licenses are known.

Then implementation proceeds AR + EN together and exits page QA only at Content C8 / Page QA PASS.

C8 is separate from deployment readiness. For the first representative page in a milestone/page family, `STAGING-PREVIEW-GATE-V1.md` must also pass before the next page in that family enters code implementation.

PG01 has completed its page lifecycle and is **C8 / PASS / CLOSED**, but its independent **Staging Preview Gate is BLOCKED** because GitHub Pages is not enabled at repository level.

PG02 has not entered implementation. It remains at **C0**. Its content/design/SEO preparation may proceed, but PG02 code is blocked until PG01 staging reaches `STAGING PASS`.

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

Resolve the **PG01 Staging Preview Gate** before PG02 code begins:

1. Repository administrator enables GitHub Pages: `Settings → Pages → Build and deployment → Source → GitHub Actions`.
2. Rerun `Deploy ORIGEX Staging`.
3. Confirm the workflow reaches Configure → Upload → Deploy PASS and records the generated Page URL.
4. Open root `/` externally and verify Arabic-first routing.
5. Open AR and EN through the deployed URL on mobile and desktop.
6. Confirm deployed assets and base-path behavior.
7. Mark PG01 `STAGING PASS`.
8. Continue PG02 Content Contract → Arabic master → English adaptation → C6 → Design Profile → SEO Contract.
9. Begin PG02 AR+EN code only after both its entry gate and PG01 staging gate pass.

M1 remains closed unless a verified foundation defect requires a controlled QA fix.

PG01 is the current M2 implementation benchmark for shell behavior and QA discipline only after its staging gate passes; page/code C8 remains valid independently.

Copyright © ORVEAX.
