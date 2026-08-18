# ORIGEX — V1 Milestone Plan

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED — M0 CLOSED / M1 READY

## Project Brief

Build a premium Arabic-first bilingual HTML template for B2B food trading, import, distribution, suppliers and manufacturers. The product must be marketable on ThemeForest, easy for beginner buyers to customize, fast, responsive, accessible, and structured as an ORVEAX commercial product rather than a one-off client website.

## Success Definition

Submission Candidate 1.0.0 must include:
- Approved/frozen scope and product architecture.
- Frozen foundation/design-system/content architecture.
- 32 unique page layouts delivered in Arabic and English.
- V1 Main Features only; Additional Features remain in V1.1 Expansion Backlog.
- Complete Content Contract for every V1 page.
- Arabic master + English professional adaptation.
- One coherent fictional Demo Dataset across products, suppliers, markets, cases and resources.
- `config.js` simple customization layer.
- Product/supplier/market data patterns conforming to frozen schemas.
- Beginner-friendly HTML documentation.
- Asset/license registry.
- Live preview package.
- Marketplace screenshots/listing copy.
- Clean final ZIP and submission checklist.

## Global Content Gate

Authority: `CONTENT-SYSTEM-V1.md`.

No page enters implementation before its content reaches C6 — FROZEN.

Workflow:
C0 Brief → C1 Arabic Draft → C2 Commercial Review → C3 English Adaptation → C4 UI Fit → C5 Demo/Claim Review → C6 FROZEN → C7 Implemented → C8 QA Passed.

Content is prepared batch-by-batch before each implementation milestone. Content is never improvised inside page code.

## M0 — Scope & Product Architecture Freeze — CLOSED
**Purpose:** stop scope and foundation churn before build.

Completed/frozen deliverables:
- Product positioning.
- 32-page architecture.
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
- QA Definition of Done including Content Gate.
- Config eligibility rules.
- Page Design Profile template including Content Contract.
- V1 exclusions.
- Milestone plan.

Canonical foundation authority: `FOUNDATION-FREEZE-V1.md`.

Gate: PASSED — APPROVED & FROZEN on 2026-08-19.

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

Gate: component QA in Arabic and English using `QA-DEFINITION-OF-DONE-V1.md`.

## M2 — Global Shell & Home Family
**Purpose:** establish the visual benchmark.

### Content Entry Gate
Home 01 / Home 02 / Home 03 / Landing must each reach Content C6 before page coding starts.

Deliverables:
- Header / mega menu / mobile drawer.
- Footer.
- Announcement/global CTA behavior.
- Home 01.
- Home 02.
- Home 03.
- Landing / One Page.

Gate: Content C8 + responsive and RTL/LTR baseline approved.

## M3 — Company, Business & Market Pages

### Content Entry Gate
About / How We Work / Capabilities / Service Details / Market Access / Markets must reach C6 before implementation.

Deliverables:
- About.
- How We Work.
- Capabilities / Services.
- Service Details.
- Market Access.
- Markets / Countries.

Gate: Content C8, page design profiles and documentation entries complete.

## M4 — Product, Supplier & Conversion Core

### Content Entry Gate
All product, supplier and conversion pages must reach C6 and align with `DEMO-CONTENT-DATASET-V1.md` + `DATA-SCHEMA-V1.md` before implementation.

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

Gate: Content C8, frozen data schemas, filters/forms and B2B conversion QA complete.

## M5 — Proof, Resources, Compliance & Content

### Content Entry Gate
Case Studies, Resources, Compliance and editorial pages reach C6 with demo/factual disclaimers reviewed before implementation.

Deliverables:
- Case Studies.
- Case Study Details.
- Downloads / Resources.
- Certifications & Compliance.
- Blog / Insights.
- Article Details.

Gate: Content C8, download/resource patterns and licensing placeholders complete.

## M6 — Support & Utility Pages

### Content Entry Gate
FAQ / Contact / 404 / Coming Soon / Privacy / Terms / Components reach C6 before implementation; sample legal text must retain explicit template/legal-review disclaimers.

Deliverables:
- FAQ.
- Contact.
- 404.
- Coming Soon / Under Construction.
- Privacy.
- Terms.
- Final Components / Elements page.

Gate: all 32 unique layouts exist in AR/EN with Content C8.

## M7 — Full QA & Optimization
Deliverables:
- Content consistency scan across all pages.
- Arabic/English commercial parity review.
- Demo-claim/disclaimer scan.
- Product/supplier/market dataset consistency scan.
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

Gate: zero Critical and zero High defects.

## M8 — Documentation, Licensing & Marketplace Package
Deliverables:
- HTML documentation site.
- Getting Started / 5-minute setup.
- File Structure.
- Config guide.
- Arabic/English guide.
- Content customization guide.
- Demo-data replacement guide.
- Components guide.
- Product/Supplier/Market data guide.
- Forms/RFQ integration guide.
- Deployment guide.
- SEO/hreflang guide.
- Credits/license/asset register.
- Changelog.
- Support guide.
- Live preview build.
- Preview screenshots.
- Item title/description/features/tags draft.
- Final downloadable ZIP.
- ThemeForest submission checklist.

Gate: Submission Candidate 1.0.0 approved.

## Change Control

After M0 closure:
- New page or Main Feature family = Scope Change or V1.1+.
- Foundation/technology/component/content-system change = Architecture/Design System/Content-System Change Request.
- Additional Features remain V1.1 backlog and are not silently introduced into V1.
- A future Additional Feature must have a complete bilingual Content Pack before design/development.
- QA/accessibility/performance/responsive/RTL fixes do not reopen scope.
- Normal page implementation must conform to `FOUNDATION-FREEZE-V1.md`.

Copyright © ORVEAX.
