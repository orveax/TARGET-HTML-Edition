# ORIGEX — V1 Milestone Plan

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED — M0/M1 CLOSED / M2–M4 IN PROGRESS  
Last Alignment: 2026-08-19 — R1 Direction & Compliance Review

## Project Brief

Build a premium Arabic-first bilingual HTML template for B2B food trading, import, distribution, suppliers and manufacturers. The product must be marketable on ThemeForest, easy for beginner buyers to customize, fast, responsive, accessible, and structured as an ORVEAX commercial product rather than a one-off client website.

## Success Definition

Submission Candidate 1.0.0 must include:
- Approved/frozen scope and product architecture.
- Frozen foundation/design-system/content/SEO/product-governance architecture.
- 33 unique page layouts delivered in Arabic and English after approved CR-001 (PG33 Company Profile).
- V1 Main Features only; Additional Features remain in V1.1 Expansion Backlog.
- Complete Content Contract for every V1 page.
- Complete SEO & Page Identity Contract for every V1 page.
- Arabic master + English professional adaptation.
- One coherent fictional Demo Dataset across products, suppliers, markets, cases and resources.
- `config.js` simple customization layer.
- Product/supplier/market data patterns conforming to frozen schemas.
- Beginner-friendly HTML documentation.
- Asset/license registry.
- Live preview package governed by Demo vs Production policy.
- Marketplace screenshots/listing copy.
- Clean final ZIP, changelog/version record and submission checklist.

## Page Stage Lifecycle

Authority: `CONTENT-SYSTEM-V1.md`.

`PS0–PS8` is the canonical page-production lifecycle. `C01–C28` is reserved for Component IDs. Historical C0–C8 references remain historical evidence only.

No page enters implementation before reaching **PS6 — FROZEN**.

Workflow:

`PS0 Brief → PS1 Arabic Draft → PS2 Commercial Review → PS3 English Adaptation → PS4 UI Fit → PS5 Demo/Claim Review → PS6 FROZEN → PS7 Implemented / CI QA → PS8 Final Page Acceptance.`

PS8 requires the applicable page QA and deployed Cloudflare browser acceptance defined in `QA-DEFINITION-OF-DONE-V1.md`, `PS8-CLOSURE-MATRIX-V1.md` and `STAGING-PREVIEW-GATE-V1.md`.

Cloudflare review is a **parallel final-acceptance gate**. It does not block continued PS6/PS7 production of subsequent pages when the test environment remains available through Manual Rebuild.

Content is prepared batch-by-batch before each implementation milestone. Content is never improvised inside page code.

## Global SEO / Page Identity Gate

Authority: `SEO-METADATA-PAGE-NAMING-V1.md`.

Every page must use its locked PG identity/file naming and complete its SEO & Page Identity Contract before implementation. SEO/metadata QA is part of page closure, not a final cosmetic step.

## M0 — Product Foundation Freeze — CLOSED / COMPLETE

**Purpose:** stop scope and foundation churn before build.

Completed/frozen deliverables include product positioning, 32-page architecture, V1/V1.1 separation, Design System, Component Registry, technology stack, responsive/RTL rules, data schema, content system, demo dataset, SEO/page naming, Demo vs Production policy, release policy, QA DoD and milestone plan.

Canonical closure authority: `PRODUCT-FOUNDATION-COMPLETE-V1.md`.

Gate: **PASSED — APPROVED, FROZEN & COMPLETE on 2026-08-19.**

## M1 — Global System & Component Foundation — CLOSED / COMPLETE

**Purpose:** implement the frozen system once and reuse everywhere.

Completed deliverables:
- Design tokens and Bootstrap 5.3.8 local foundation.
- Local Tajawal / Manrope typography.
- Grid/container helpers, shape/border/elevation and section systems.
- Hero/card/button/badge/form/table/filter/navigation foundations.
- Lucide local subset + sprite + license.
- ORIGEX patterns PT01–PT06.
- RTL/LTR and reduced-motion foundations.
- `config.js` + config engine.
- global shell and reusable component/head-ready architecture.
- M1 asset/license baseline + vendor checksums.

Gate: **PASSED / CLOSED on 2026-08-19**. Authority: `M1-QA-REPORT-V1.md` + `M1-COMPONENT-IMPLEMENTATION-MAP.md`.

## M2 — Global Shell & Home Family — IN PROGRESS

**Purpose:** establish the visual benchmark.

Deliverables:
- Header / mega menu / mobile drawer.
- Footer.
- Announcement/global CTA behavior.
- PG01 Home 01.
- PG02 Home 02.
- PG03 Home 03.
- PG04 Landing / One Page.

Current state:
- PG01 — **PS8 / PASS / CLOSED — Marketplace Visual Benchmark**.
- PG02–PG04 — **PS7 / IMPLEMENTED / CI QA PASS**.
- Cloudflare deployed-browser review remains open for PG02–PG04 before PS8.

Gate: all M2 pages PS8 + SEO/RTL/responsive/browser acceptance + zero Critical/High milestone defects.

## M3 — Company, Business & Market Pages — IN PROGRESS

Deliverables:
- PG05 About.
- PG06 How We Work.
- PG07 Capabilities / Services.
- PG08 Service Details.
- PG14 Market Access.
- PG15 Markets / Countries.

Current state:
- PG05 / PG06 / PG07 / PG08 / PG14 / PG15 — **PS7 / IMPLEMENTED / CI QA PASS**.
- M3 page production is code/CI complete.
- Cloudflare M3 batch browser acceptance remains before PS8 / milestone closure.

Gate: all listed pages PS8 + SEO/Page Identity + documentation alignment + zero Critical/High milestone defects.

## M4 — Product, Supplier & Conversion Core — IN PROGRESS

Deliverables:
- PG09 Product Categories.
- PG10 Products Grid.
- PG11 Product Details.
- PG12 Suppliers / Brands Directory.
- PG13 Supplier / Brand Details.
- PG16 For Suppliers.
- PG17 Submit Product.
- PG18 RFQ.
- PG19 Become Distributor / Partner.

Current state:
- PG09 — **PS7 / IMPLEMENTED / CI QA PASS**.
- PG10 — **PS7 / IMPLEMENTED / DATA + SOURCE + RENDERED/INTERACTION CI QA PASS**.
- PG11 — **NEXT BUILD** after R1 governance alignment.
- PG12/PG13/PG16/PG17/PG18/PG19 — NOT STARTED.
- Cloudflare M4 browser acceptance remains a parallel PS8 gate and does not block PS7 page production.

Gate: all listed pages PS8 + frozen data schemas + filters/forms/conversion QA + zero Critical/High milestone defects.

## M5 — Proof, Resources, Compliance & Content — NOT STARTED

Deliverables:
- Case Studies.
- Case Study Details.
- Downloads / Resources.
- Certifications & Compliance.
- Blog / Insights.
- Article Details.

Gate: all listed pages PS8 + SEO + download/resource/licensing controls.

## M6 — Support & Utility Pages — NOT STARTED

Deliverables:
- FAQ.
- Contact.
- 404.
- Coming Soon / Under Construction.
- Privacy.
- Terms.
- Final Components / Elements page.

Gate: all 32 unique layouts exist in AR/EN and reach applicable PS8 / SEO/Page Identity QA.

## M7 — Full QA & Optimization — NOT STARTED

Deliverables:
- Content consistency and AR/EN parity review.
- Demo-claim/disclaimer scan.
- Product/supplier/market dataset consistency scan.
- Page naming/slug/SEO metadata QA.
- HTML validation and CSS/JS integrity.
- Broken link/asset and console-error scans.
- RTL/LTR and full responsive matrix.
- Keyboard/accessibility/focus/reduced-motion review.
- Performance cleanup and duplicate-code/component-promotion review.
- Cross-browser smoke testing.
- TARGET/client leakage and Demo vs Production safety scan.
- final marketplace visual polish.

Gate: zero Critical and zero High defects.

## M8 — Documentation, Licensing & Marketplace Package — NOT STARTED

Deliverables:
- HTML documentation site and Getting Started.
- File structure/config/AR-EN/content customization guides.
- Demo-data replacement / Before You Publish checklist.
- Components and structured-data guides.
- Forms/RFQ integration and deployment guides.
- SEO/hreflang/metadata/page naming guide.
- Credits/license/asset register.
- `CHANGELOG.md` + release version record.
- Support guide and live preview package.
- Marketplace preview screenshots/listing copy.
- Final downloadable ZIP and ThemeForest submission checklist.

Gate: Submission Candidate **1.0.0** approved under the Release Gate.

## R1 — Direction & Compliance Review — 2026-08-19

R1 is a control review, not a new milestone.

Result:
- Product direction: PASS.
- Architecture/stack/reusability/RTL-LTR/demo safety/licensing direction: PASS.
- Corrective actions: lifecycle naming alignment, stale deployment-governance wording correction, PS8 closure matrix creation, repository-name correction in staging governance.
- No redesign, rollback or V1 scope change required.
- PG11 may proceed after R1 documentation alignment; Cloudflare PS8 acceptance remains parallel.

## Change Control

After Product Foundation closure:
- New page or Main Feature family = Scope Change or V1.1+.
- Foundation/technology/component/content/SEO/product-governance change = formal Change Request.
- Additional Features remain V1.1 backlog and are not silently introduced into V1.
- A future Additional Feature must have a complete bilingual Content Pack before design/development.
- QA/accessibility/performance/responsive/RTL fixes do not reopen scope.
- verified SEO/content defects may be corrected without reopening architecture.
- Normal implementation must conform to `PRODUCT-FOUNDATION-COMPLETE-V1.md` and its canonical authorities.

Copyright © ORVEAX.


## CR-001 Scope Addendum — 2026-08-19
- Added PG33 — Company Profile / الملف التعريفي under M3.
- Active V1 scope is now **33 unique layouts / approximately 66 AR+EN HTML pages**.
- `GLOBAL-NAVIGATION-CONTRACT-V1.md` is the canonical N01/N02/N03 IA for all Standard Pages.
- PG04 Landing retains its compact conversion navigation as the documented exception.
- Historical 32-layout statements in frozen closure evidence describe the pre-CR baseline and are superseded for active delivery by CR-001.
