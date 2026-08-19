# ORIGEX — V1 Milestone Plan

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED — PRODUCT FOUNDATION COMPLETE / M1 READY

## Project Brief

Build a premium Arabic-first bilingual HTML template for B2B food trading, import, distribution, suppliers and manufacturers. The product must be marketable on ThemeForest, easy for beginner buyers to customize, fast, responsive, accessible, and structured as an ORVEAX commercial product rather than a one-off client website.

## Success Definition

Submission Candidate 1.0.0 must include:
- Approved/frozen scope and product architecture.
- Frozen foundation/design-system/content/SEO/product-governance architecture.
- 32 unique page layouts delivered in Arabic and English.
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

## Global Content Gate

Authority: `CONTENT-SYSTEM-V1.md`.

No page enters implementation before its content reaches C6 — FROZEN.

Workflow:
C0 Brief → C1 Arabic Draft → C2 Commercial Review → C3 English Adaptation → C4 UI Fit → C5 Demo/Claim Review → C6 FROZEN → C7 Implemented → C8 QA Passed.

Content is prepared batch-by-batch before each implementation milestone. Content is never improvised inside page code.

## Global SEO / Page Identity Gate

Authority: `SEO-METADATA-PAGE-NAMING-V1.md`.

Every page must use its locked PG identity/file naming and complete its SEO & Page Identity Contract before implementation. SEO/metadata QA is part of page closure, not a final cosmetic step.

## M0 — Product Foundation Freeze — CLOSED / COMPLETE
**Purpose:** stop scope and foundation churn before build.

Completed/frozen deliverables:
- Product positioning.
- 32-page architecture and PG01–PG32 identity map.
- Main Features per page.
- V1.1 Additional Features backlog separation.
- Component & Design Rules.
- Design System hierarchy and Component Registry.
- Technology Stack.
- Bootstrap foundation policy.
- Icon System.
- Pattern System.
- Image/Media System.
- Grid/container/responsive rules.
- shape/border/elevation tokens.
- Motion/interaction rules.
- Data schema.
- Code architecture/naming.
- Browser support policy.
- Performance budget principles.
- Content System.
- Master Content Architecture for all 32 layouts.
- Canonical Demo Content Dataset.
- Prepared V1.1 Additional Feature Content Packs.
- SEO, Metadata & Page Naming System.
- Demo vs Production Policy.
- Release & Versioning Policy.
- QA Definition of Done including Content/SEO/Demo/Release Gates.
- Config eligibility rules.
- Page Design Profile template including Content + SEO Contracts.
- V1 exclusions.
- Milestone plan.

Canonical closure authority: `PRODUCT-FOUNDATION-COMPLETE-V1.md`.

Gate: PASSED — APPROVED, FROZEN & COMPLETE on 2026-08-19.

## M1 — Global System & Component Foundation — READY FOR IMPLEMENTATION
**Purpose:** implement the frozen system once and reuse everywhere.

Deliverables:
- Design tokens implemented.
- Bootstrap foundation integrated according to `TECH-STACK-V1.md`.
- Typography hierarchy implemented.
- Grid/container helpers implemented.
- shape/border/elevation tokens implemented.
- Section system.
- Hero families.
- Card families.
- Buttons/badges/forms.
- Lucide local SVG/icon system integration.
- ORIGEX pattern assets PT01–PT06.
- registered media frames/placeholders.
- Tables/specification patterns.
- Tabs/accordions/filters/modals.
- Motion tokens/interactions.
- RTL/LTR helpers.
- `config.js` + engine.
- data file foundations conforming to `DATA-SCHEMA-V1.md`.
- Components/Elements page foundation using realistic canonical demo content, not lorem ipsum.
- reusable metadata/head pattern supporting the frozen SEO contract.

Gate: component QA in Arabic and English using `QA-DEFINITION-OF-DONE-V1.md`.

## M2 — Global Shell & Home Family
**Purpose:** establish the visual benchmark.

### Content / SEO Entry Gate
Home 01 / Home 02 / Home 03 / Landing must each reach Content C6 and complete the SEO/Page Identity Contract before page coding starts.

Deliverables:
- Header / mega menu / mobile drawer.
- Footer.
- Announcement/global CTA behavior.
- Home 01.
- Home 02.
- Home 03.
- Landing / One Page.

Gate: Content C8 + SEO Gate + responsive and RTL/LTR baseline approved.

## M3 — Company, Business & Market Pages

### Content / SEO Entry Gate
About / How We Work / Capabilities / Service Details / Market Access / Markets must reach C6 and complete their SEO/Page Identity Contract before implementation.

Deliverables:
- About.
- How We Work.
- Capabilities / Services.
- Service Details.
- Market Access.
- Markets / Countries.

Gate: Content C8, SEO Gate, page design profiles and documentation entries complete.

## M4 — Product, Supplier & Conversion Core

### Content / SEO Entry Gate
All product, supplier and conversion pages must reach C6, complete their SEO/Page Identity Contract, and align with `DEMO-CONTENT-DATASET-V1.md` + `DATA-SCHEMA-V1.md` before implementation.

Deliverables:
- Product Categories.
- Products Grid.
- Product Details.
- Suppliers / Brands Directory.
- Supplier / Brand Details.
- For Suppliers.
- Submit Product.
- RFQ.
- Become Distributor / Partner.

Gate: Content C8, SEO Gate, frozen data schemas, filters/forms and B2B conversion QA complete.

## M5 — Proof, Resources, Compliance & Content

### Content / SEO Entry Gate
Case Studies, Resources, Compliance and editorial pages reach C6 with demo/factual disclaimers and SEO/Page Identity Contract reviewed before implementation.

Deliverables:
- Case Studies.
- Case Study Details.
- Downloads / Resources.
- Certifications & Compliance.
- Blog / Insights.
- Article Details.

Gate: Content C8, SEO Gate, download/resource patterns and licensing placeholders complete.

## M6 — Support & Utility Pages

### Content / SEO Entry Gate
FAQ / Contact / 404 / Coming Soon / Privacy / Terms / Components reach C6 before implementation; sample legal text must retain explicit template/legal-review disclaimers and each page must have the correct indexability class.

Deliverables:
- FAQ.
- Contact.
- 404.
- Coming Soon / Under Construction.
- Privacy.
- Terms.
- Final Components / Elements page.

Gate: all 32 unique layouts exist in AR/EN with Content C8 and SEO/Page Identity QA complete.

## M7 — Full QA & Optimization
Deliverables:
- Content consistency scan across all pages.
- Arabic/English commercial parity review.
- Demo-claim/disclaimer scan.
- Product/supplier/market dataset consistency scan.
- Page naming/file/slug consistency scan.
- title/meta/canonical/hreflang/Open Graph QA.
- indexability and structured-data review.
- HTML validation.
- CSS/JS integrity.
- Broken link/asset scan.
- Console error scan.
- Arabic RTL QA.
- English LTR QA.
- Responsive matrix.
- Keyboard/accessibility review.
- Reduced-motion review.
- Performance cleanup.
- Cross-browser smoke test.
- Client/TARGET leakage scan.
- Demo vs Production safety scan.

Gate: zero Critical and zero High defects.

## M8 — Documentation, Licensing & Marketplace Package
Deliverables:
- HTML documentation site.
- Getting Started / 5-minute setup.
- File Structure.
- Config guide.
- Arabic/English guide.
- Content customization guide.
- Demo-data replacement guide / Before You Publish checklist.
- Components guide.
- Product/Supplier/Market data guide.
- Forms/RFQ integration guide.
- Deployment guide.
- SEO/hreflang/metadata/page naming guide.
- Credits/license/asset register.
- `CHANGELOG.md`.
- Release version record following `RELEASE-VERSIONING-POLICY-V1.md`.
- Support guide.
- Live preview build governed by `DEMO-VS-PRODUCTION-POLICY-V1.md`.
- Preview screenshots.
- Item title/description/features/tags draft.
- Final downloadable ZIP.
- ThemeForest submission checklist.

Gate: Submission Candidate **1.0.0** approved under the Release Gate.

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