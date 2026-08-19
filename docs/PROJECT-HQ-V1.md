# ORIGEX — Project HQ V1

Product ID: ORX-P01  
Owner: ORVEAX  
Repository: `orveax/TARGET-HTML-Edition`  
Status: ACTIVE CONTROL DOCUMENT  
Last hard audit: 2026-08-19

This is the operational entry point for ORIGEX. If another document conflicts with this HQ, use the authority order below and stop local improvisation.

## 1. Current Project State

```text
M0 — PRODUCT FOUNDATION: CLOSED / COMPLETE
M1 — GLOBAL SYSTEM & COMPONENT FOUNDATION: CLEAN START / IMPLEMENTATION NEXT
M2–M8 — NOT STARTED
```

The pre-foundation Build 02–05 implementation was removed from the active tree during the 2026-08-19 hard audit. Git history remains the archive. No removed pre-freeze file is an implementation authority.

## 2. Product Definition

ORIGEX is a premium Arabic-first bilingual HTML template for B2B food trading, import, wholesale, distribution, manufacturers, suppliers and market-access workflows.

V1 ships 32 unique layouts in Arabic and English, with Main Features only. Additional Features remain in the V1.1 backlog.

## 3. Frozen Technology

- HTML5
- CSS3
- Bootstrap **5.3.8** as infrastructure/layout foundation
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
- `DOCUMENTATION-ARCHITECTURE.md`

### Reference Only
- `ABOUT-SOURCE-MAP.md`
- `HOMEPAGE-SOURCE-MAP.md`
- `PAGE-FIDELITY-MATRIX.md`
- `THEMEFOREST-BENCHMARK-2026-08.md`

Reference files inform fidelity/research; they do not define current architecture.

## 6. Active Repository Structure

Current clean-start structure before M1 implementation:

```text
/
├── README.md
├── CHANGELOG.md
├── assets/
│   ├── brand/          # approved ORIGEX brand SVG assets
│   └── js/             # config seed only until M1 normalization
└── docs/               # canonical product authorities and references
```

M1 is responsible for creating the compliant implementation structure:

```text
assets/
├── vendor/bootstrap/   # Bootstrap 5.3.8 local distribution
├── icons/              # local Lucide subset/sprite + license note
├── patterns/           # ORIGEX PT01–PT06
├── brand/
├── css/
├── js/
├── data/
└── media/

ar/
en/
preview/                # development-only QA infrastructure
```

No page code is reintroduced before the M1 global foundation is implemented.

## 7. Page Entry Gate

A page may enter implementation only when all are true:

- Page ID/filename comes from `SEO-METADATA-PAGE-NAMING-V1.md`.
- V1 Main Features match `SCOPE-FREEZE-V1-FINAL.md`.
- Content reaches C6 — FROZEN.
- Page Design Profile is complete.
- Required components/variants already exist in the registry.
- required assets/licenses are known.

Then implementation proceeds AR + EN together and exits only at Content C8 / Page QA PASS.

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

Implement M1 in this order:

1. Bootstrap 5.3.8 local vendor baseline + notices.
2. ORIGEX tokens / typography / grid / shape / motion.
3. Icon and pattern assets.
4. primitives and components.
5. config engine normalization.
6. global shell.
7. Components/Elements foundation page.
8. AR/EN component QA.

Only after the M1 Gate passes does PG01 Home 01 enter page-by-page production.

Copyright © ORVEAX.
