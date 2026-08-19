# ORIGEX — Page Design Profile Template V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: LOCKED TEMPLATE

Use this record before implementing every V1 page.

## 1. Page Identity
- Page ID:
- Page Name AR:
- Page Name EN:
- Page Family:
- Commercial Goal:
- Primary Audience:

## 2. Content Contract — Mandatory

Authority: `CONTENT-SYSTEM-V1.md` and `MASTER-CONTENT-ARCHITECTURE-V1.md`.

No page may enter implementation without Content Status C6 — FROZEN.

Complete:
- Content ID:
- Funnel Role:
- Primary User Question:
- Primary Message:
- Required Facts/Data:
- Arabic Master Copy status:
- English Adaptation status:
- Primary CTA:
- Secondary CTA:
- Labels/Microcopy:
- Empty State:
- Success/Error/Validation states where applicable:
- Demo/Legal Disclaimer:
- SEO Title Intent:
- SEO Description Intent:
- Data Source / Owner:
- Content Status: C0 / C1 / C2 / C3 / C4 / C5 / C6 / C7 / C8

Rules:
- Arabic is the master commercial copy.
- English is a professional adaptation, not literal translation.
- Facts and commercial promises must match in both languages.
- Demo entities must use `DEMO-CONTENT-DATASET-V1.md` unless a reviewed new entity is added.
- No lorem ipsum in commercial preview pages.
- Additional Features use the same Content Contract when activated.

## 2A. SEO & Page Identity Contract — Mandatory

Authority: `SEO-METADATA-PAGE-NAMING-V1.md`.

Complete before page implementation:
- SEO/Page ID:
- Indexability: INDEX / NOINDEX / ENVIRONMENT-DEPENDENT
- Canonical Page Name:
- File/Slug AR:
- File/Slug EN:
- H1 AR:
- H1 EN:
- SEO Title AR:
- SEO Title EN:
- Meta Description AR:
- Meta Description EN:
- Canonical URL AR placeholder:
- Canonical URL EN placeholder:
- hreflang AR:
- hreflang EN:
- x-default strategy:
- OG Type:
- OG Title AR/EN:
- OG Description AR/EN:
- OG Image strategy:
- Structured Data candidate/type:
- Breadcrumb Label AR/EN:
- Primary Internal Links / Anchor Copy:

Rules:
- page file/slug follows the locked PG01–PG32 naming registry.
- Canonical Page Name, H1 and SEO title may differ in wording but must communicate the same page intent.
- Each indexable page requires unique title/description content.
- No fake ratings/reviews/prices/certifications/availability in structured data.
- Demo canonical/hreflang values must not hard-code buyer production domains.
- ThemeForest/demo indexability follows `DEMO-VS-PRODUCTION-POLICY-V1.md`.

## 3. Main Features
List only V1 Main Features approved in the frozen scope.

## 4. Component Map
Declare registry IDs only.

Example:
```text
Hero: S03 Centered Editorial Hero
Section Header: S01
Primary Cards: C05 Process Card
Trust: C20 Trust Item
Accordion: C14
Primary CTA: P01
Secondary Action: P03
Final CTA: S06
Global Navigation: N01 + N02 + N03 + N04
```

Rule: if a required UI unit has no registry ID, stop and review the registry before coding. Do not invent a page-local component.

## 5. Section Sequence
Document exact page order.

Example:
```text
01 Hero
02 Qualification
03 Four-Step Process
04 Roles / Responsibilities
05 Required Information
06 Decision Flow
07 Final CTA
```

## 6. Design Profile
- Hero family:
- Density: Compact / Standard / Comfortable
- Section rhythm: Tight / Standard / Large
- Primary card families:
- Surface sequence:
- CTA hierarchy:
- Media treatment:
- Motion level: 0 / 1 / 2

## 7. Interaction Budget
Only list interactions required by the Main Features.

Examples:
- Mega menu.
- Mobile drawer.
- Accordion.
- Tabs.
- Search/filter.
- Form validation.
- Modal/offcanvas.

No decorative interaction is added without UX value.

## 8. Config Eligibility
List only global recurring values from `config.js`.

Example:
```text
Contact email: config
Phone: config
Business hours: config
Page H1: HTML
Page body copy: HTML
Product data: JSON/data source
```

## 9. Arabic RTL Rules
- Content reading order:
- Arrow/directional behavior:
- Mixed LTR data:
- Number/SKU/phone behavior:
- Mobile ordering:
- Alignment exceptions:

## 10. English LTR Rules
- Content reading order:
- Arrow/directional behavior:
- Mobile ordering:
- Copy-length risks:

## 11. Responsive Contract
For each critical range define behavior, not only breakpoints.

- 360–412 Mobile:
- 768–820 Tablet:
- 1024 Large Tablet:
- 1280–1536 Desktop:
- 1920 Large Desktop:

## 12. Accessibility Contract
- Heading hierarchy.
- Landmark structure.
- Keyboard interactions.
- Focus order.
- ARIA only where required.
- Form error association if relevant.
- Media alt strategy.
- Reduced motion behavior.

## 13. Performance Contract
- Required JS modules:
- Required images/media:
- Lazy-loaded assets:
- No third-party runtime requirement unless explicitly approved.

## 14. Asset & License Record
- Distributable assets:
- Preview-only assets:
- Placeholders:
- License/source registry references:

## 15. Documentation Entries
List documentation that must be updated while building this page.

## 16. QA Exit Gate
A page cannot move to DONE until:
- Content Contract complete and status reached C8 after implementation QA.
- SEO & Page Identity Contract complete and QA-passed.
- Main Features complete.
- Registry components used without unauthorized forks.
- Arabic complete.
- English complete.
- Commercial meaning/facts/CTA parity checked across AR/EN.
- Demo/factual disclaimers present where required.
- RTL/LTR QA complete.
- Responsive QA complete.
- Keyboard/accessibility baseline checked.
- No broken links/assets.
- No console errors.
- Documentation updated.
- Source/rights check complete.

Copyright © ORVEAX.