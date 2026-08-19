# ORIGEX — V1 Foundation Freeze

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED, FROZEN & COMPLETE  
Approval Date: 2026-08-19  
Normalized: 2026-08-19 Hard Audit

This is the consolidated frozen-system authority for ORIGEX V1. Implementation consumes these systems; normal page work does not reopen them.

Operational entry point: `PROJECT-HQ-V1.md`.

## 1. Technology Foundation

Exact authority: `TECH-STACK-V1.md`.

V1 uses:
- HTML5;
- CSS3;
- Bootstrap **5.3.8** as infrastructure/layout foundation;
- Vanilla JavaScript;
- ORIGEX Design System;
- `config.js` simple global customization;
- approved JSON data domains where useful.

Explicit exclusions:
- React;
- Vue;
- Astro runtime in buyer package;
- Tailwind;
- jQuery;
- mandatory Node/build pipeline;
- heavy animation framework.

Bootstrap is infrastructure, never ORIGEX visual identity.

## 2. Design-System Hierarchy

Authorities:
- `DESIGN-SYSTEM-HIERARCHY-V1.md`
- `COMPONENT-REGISTRY-V1.md`
- `COMPONENT-DESIGN-RULES-V1.md`

```text
Bootstrap 5.3.8 Infrastructure
→ ORIGEX Foundations
→ Primitives
→ Components
→ Patterns / Global Navigation
→ Sections
→ Page Design Profiles
```

Pages compose registered units. Shared components are changed centrally, never forked through page-local CSS.

## 3. Grid / Container / Responsive

Bootstrap grid is structural infrastructure.

ORIGEX container profiles:
- Narrow: max 840px;
- Standard: max 1140px;
- Wide: max 1320px;
- Full Bleed: viewport width with controlled inner content.

Horizontal gutters:
- Mobile: 20px;
- Tablet: 24px;
- Desktop: 32px.

Primary QA widths:
360 / 390 / 412 / 768 / 820 / 1024 / 1280 / 1366 / 1440 / 1536 / 1920.

Rules:
- mobile is intentionally composed, not compressed desktop;
- logical properties are preferred;
- AR and EN ordering is independently verified;
- horizontal overflow is a defect.

## 4. Shape / Border / Elevation

Radius:
- XS 8px;
- SM 12px;
- MD 16px;
- LG 24px;
- Pill 999px.

Border:
- Subtle: 1px soft border;
- Default: 1px standard border;
- Strong: 2px only where state/hierarchy justifies it.

Elevation:
- E0 none;
- E1 subtle separation;
- E2 featured/interactive emphasis;
- E3 overlay/drawer/dropdown/modal only.

No page-local shape/shadow language.

## 5. Motion / Interaction

Durations:
- Fast 150ms;
- Standard 250ms;
- Slow 400ms.

Levels:
- L0 utility/legal;
- L1 normal business/product UI;
- L2 selected home/landing emphasis.

Allowed: restrained state transitions, directional micro-motion, disclosure/navigation transitions.  
Prohibited: scroll-jacking, bouncing, continuous decorative loops, essential-content delay, page-specific motion libraries.

`prefers-reduced-motion` is mandatory.

## 6. Icon System

Authority: `ICON-SYSTEM-V1.md` / Registry F05.

- Lucide = single semantic icon family;
- outline;
- 24×24 base grid;
- default stroke 2;
- sizes 14 / 16 / 20 / 24 / 32 / 40px;
- selected local SVGs / local sprite;
- brand/social marks separate;
- only directional icons swap/mirror in RTL;
- text/glyph placeholders are prohibited production icon substitutes;
- icon-only controls require accessible names.

## 7. Pattern System

Authority: `PATTERN-SYSTEM-V1.md`.

Approved ORIGEX-owned families:
- PT01 Route Lines;
- PT02 Trade Grid;
- PT03 Dot Matrix;
- PT04 Market Nodes;
- PT05 Packaging Geometry;
- PT06 Flow Lines.

External pattern libraries are reference/exploration only unless an exact asset is separately approved and logged.

## 8. Image / Media System

Authority: `IMAGE-MEDIA-SYSTEM-V1.md`.

Direction: **Natural Industrial Premium**, B2B food trading / wholesale / distribution / manufacturing / sourcing / market access.

Approved frame families:
- Hero: 3:2 or 16:10; mobile editorial crop 4:5;
- Product: 1:1;
- Supplier/brand media: 4:3; logos use controlled contain frame;
- Blog: 16:9;
- Case/facility: 16:10 or 3:2;
- Avatar: 1:1 when used.

Third-party stock is preview-only by default. Buyer ZIP uses ORVEAX-owned placeholders/graphics or explicitly redistributable assets only.

## 9. Asset / License Governance

Authority: `ASSET-LICENSE-REGISTER-V1.md`.

No dependency/image/font/icon/logo/PDF/third-party asset enters the distributable package before source and redistribution status are logged.

M1 must close Bootstrap/Lucide/font/pattern delivery records before component foundation closes.

## 10. Data Architecture

Authority: `DATA-SCHEMA-V1.md`.

Canonical structured domains:
- Products;
- Suppliers/Brands;
- Markets/Countries.

`config.js` is not a CMS. Editorial page copy remains HTML; structured repeated business records use documented data structures when data-driven behavior is required.

## 11. Code Architecture / Naming

Authority: `CODE-ARCHITECTURE-V1.md`.

- ORIGEX classes use `orx-`;
- CSS variables use `--orx-*`;
- JS hooks use `data-orx-*`;
- files use lowercase kebab-case;
- BEM-like block/element/modifier naming;
- no hidden hotfix layer;
- no `final-final`, `fix2`, `new-copy`, or other temporary canonical filenames.

## 12. Configuration Contract

Authority: `CONFIGURATION.md`.

`config-engine.js` enhances existing semantic HTML through registered data hooks. It does not construct core UI/components or become the source of essential page meaning.

Global/repeated settings may enter config; page editorial content and structured catalogs do not.

## 13. Content System

Authorities:
- `CONTENT-SYSTEM-V1.md`;
- `MASTER-CONTENT-ARCHITECTURE-V1.md`;
- `DEMO-CONTENT-DATASET-V1.md`;
- V1.1 Content Pack authorities.

Rules:
- Arabic master;
- English professional adaptation;
- same facts/promise/CTA intent;
- no page/feature implementation before C6 — FROZEN;
- final implemented content reaches C8 after QA;
- no lorem ipsum in commercial demo pages;
- no fake customers/certifications/performance claims;
- demo facts that may look real are disclosed as illustrative;
- future Additional Feature requires a full Content Contract/Pack before design/development.

## 14. SEO / Metadata / Page Naming

Authority: `SEO-METADATA-PAGE-NAMING-V1.md`.

Every page uses:
- registered PG ID;
- canonical filename/slug;
- H1 intent;
- unique title/meta description;
- canonical URL contract;
- AR/EN hreflang + x-default strategy where applicable;
- Open Graph contract;
- indexability class;
- structured-data mapping where appropriate.

SEO is part of page identity and QA, not a final afterthought.

## 15. Demo vs Production

Authority: `DEMO-VS-PRODUCTION-POLICY-V1.md`.

- fictional demo entities remain clearly demo/illustrative;
- no private/client credentials or proprietary data;
- preview-only assets never enter buyer ZIP;
- buyer documentation includes a Demo → Production replacement checklist;
- demo indexability is intentionally controlled.

## 16. Browser / Performance

V1 targets modern evergreen desktop/mobile browsers; no Internet Explorer support.

Performance rules:
- no duplicate UI/icon libraries;
- local core dependencies;
- no unnecessary scripts;
- below-fold media lazy-loaded;
- image dimensions declared where practical;
- modern compressed formats preferred;
- no unoptimized multi-megabyte media;
- core navigation/content does not require a third-party runtime;
- CSS/JS duplication is a QA defect.

## 17. QA Definition of Done

Authority: `QA-DEFINITION-OF-DONE-V1.md`.

A page/component/content unit closes only after applicable Content / Design / AR / EN / Responsive / Accessibility / SEO / Asset / Performance / Runtime checks pass.

Submission Candidate requires zero Critical and zero High defects.

## 18. Release / Versioning

Authority: `RELEASE-VERSIONING-POLICY-V1.md`.

Product releases use semantic `MAJOR.MINOR.PATCH` governance. Code comments/schema labels are not release claims. Release number, changelog, package contents and marketplace version must agree.

## 19. V1 / V1.1 Boundary

Authority: `SCOPE-FREEZE-V1-FINAL.md` and `V1.1-ADDITIONAL-FEATURES-BACKLOG.md`.

V1 = approved Main Features only.  
Additional Features remain V1.1+ unless a formal scope change is approved.

## 20. Governance Lock

Frozen for V1:
- scope/page architecture;
- stack/version-family baseline;
- design-system hierarchy;
- grid/shape/motion;
- component registry governance;
- icon/pattern/media systems;
- asset/license process;
- data/config architecture;
- code naming;
- content-writing mechanism;
- bilingual adaptation;
- SEO/page naming;
- demo/production policy;
- browser/performance principles;
- QA/release/change control.

Normal page implementation cannot reopen these decisions.

Valid post-freeze classifications:
1. verified bug/defect;
2. verified content/SEO correction;
3. formal Design System / Architecture / Product Governance Change Request;
4. V1.1+ backlog.

Current implementation state is tracked only in `IMPLEMENTATION-STATUS-V1.md`.

Copyright © ORVEAX.
