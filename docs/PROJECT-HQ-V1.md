# ORIGEX — Project HQ V1

Product ID: ORX-P01  
Owner: ORVEAX  
Repository: `orveax/TARGET-HTML-Edition`  
Status: ACTIVE CONTROL DOCUMENT  
Last Updated: 2026-08-19 — M2 / PG01 MARKETPLACE BENCHMARK CLOSED / PG02 C6 READY / CLOUDFLARE AUTO-DEPLOY DEFERRED

This is the operational entry point for ORIGEX. If another document conflicts with this HQ, use the authority order below and stop local improvisation.

## 1. Current Project State

```text
M0 — PRODUCT FOUNDATION: PASS / CLOSED
M1 — GLOBAL SYSTEM & COMPONENT FOUNDATION: PASS / CLOSED
M2 — GLOBAL SHELL & HOME FAMILY: IN PROGRESS
PG01 — HOME 01: C8 / PASS / CLOSED — MARKETPLACE VISUAL BENCHMARK — AR + EN
PG02 — HOME 02: C6 / FROZEN — DESIGN + SEO APPROVED — READY FOR AR+EN BUILD
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
- Source/SEO QA: `PG01-QA-REPORT-V1.md`
- Base closure: `PG01-CLOSURE-2026-08-19.md`
- Marketplace visual closure: `PG01-MARKETPLACE-VISUAL-POLISH-2026-08-19.md`
- Final rendered QA: `5ab1edb6fe2a17adc41857790170097dfad57f0f` — 8/8 PASS.
- Final interaction QA: `b3d12beb103492144f4c5fc690ef15eedd49eef4` — PASS.
- Visual snapshots: `e1c09173757defc6992ac162447990f2ffc76f5a`.

PG02 entry authority:
- Page contract: `page-design-profiles/pg02-home-02-v1.md`.
- Content: C6 / FROZEN.
- SEO/Page Identity Contract: APPROVED.
- Component map: APPROVED registered V1 units only.
- Build: NOT STARTED / READY.

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
│   └── index.html              # PG01 Arabic
├── en/
│   └── index.html              # PG01 English
├── assets/
│   ├── brand/
│   ├── css/
│   │   ├── origex-tokens.css
│   │   ├── origex-foundation.css
│   │   ├── origex-components.css
│   │   ├── origex-compositions.css
│   │   ├── origex-marketplace-polish.css
│   │   └── origex-shell.css
│   ├── media/demo/
│   ├── fonts/
│   ├── icons/
│   ├── js/
│   ├── patterns/
│   └── vendor/bootstrap/
├── preview/
├── qa/
└── docs/
    └── page-design-profiles/
        ├── pg01-home-01-v1.md
        └── pg02-home-02-v1.md
```

M1 owns the reusable foundation. M2+ pages consume it and may not create competing local systems.

`origex-shell.css` remains the closed M1 shell. `origex-compositions.css` is the M2 composition entry and may load approved M2 refinements without reopening M1.

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

PG01 has completed its page lifecycle and is **C8 / PASS / CLOSED — MARKETPLACE VISUAL BENCHMARK**.

PG02 has completed its entry preparation and is now **C6 / DESIGN + SEO APPROVED / READY FOR AR+EN BUILD**.

Cloudflare auto-deploy degradation is an operational issue, not a page-entry blocker while Manual Rebuild remains available. Final browser acceptance still requires the current revision to be deployed through the real Cloudflare Test Environment.

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

1. Build PG02 Arabic and English together from `page-design-profiles/pg02-home-02-v1.md`.
2. Create and register the required ORVEAX-owned distribution hero media.
3. Run source, rendered responsive and interaction QA.
4. Deploy the current `main` revision to the Cloudflare Test Environment; Manual Rebuild is acceptable temporarily.
5. Perform external AR/EN mobile + desktop smoke review.
6. Close PG02 only at C8 / PASS.
7. In the deferred infrastructure session, repair Cloudflare Git auto-deploy so push to `main` deploys automatically.

M1 remains closed unless a verified foundation defect requires a controlled QA fix.

Copyright © ORVEAX.
