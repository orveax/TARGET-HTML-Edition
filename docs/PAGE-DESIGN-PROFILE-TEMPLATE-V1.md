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

## 2. Main Features
List only V1 Main Features approved in the frozen scope.

## 3. Component Map
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

## 4. Section Sequence
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

## 5. Design Profile
- Hero family:
- Density: Compact / Standard / Comfortable
- Section rhythm: Tight / Standard / Large
- Primary card families:
- Surface sequence:
- CTA hierarchy:
- Media treatment:
- Motion level: 0 / 1 / 2

## 6. Interaction Budget
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

## 7. Config Eligibility
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

## 8. Arabic RTL Rules
- Content reading order:
- Arrow/directional behavior:
- Mixed LTR data:
- Number/SKU/phone behavior:
- Mobile ordering:
- Alignment exceptions:

## 9. English LTR Rules
- Content reading order:
- Arrow/directional behavior:
- Mobile ordering:
- Copy-length risks:

## 10. Responsive Contract
For each critical range define behavior, not only breakpoints.

- 360–412 Mobile:
- 768–820 Tablet:
- 1024 Large Tablet:
- 1280–1536 Desktop:
- 1920 Large Desktop:

## 11. Accessibility Contract
- Heading hierarchy.
- Landmark structure.
- Keyboard interactions.
- Focus order.
- ARIA only where required.
- Form error association if relevant.
- Media alt strategy.
- Reduced motion behavior.

## 12. Performance Contract
- Required JS modules:
- Required images/media:
- Lazy-loaded assets:
- No third-party runtime requirement unless explicitly approved.

## 13. Asset & License Record
- Distributable assets:
- Preview-only assets:
- Placeholders:
- License/source registry references:

## 14. Documentation Entries
List documentation that must be updated while building this page.

## 15. QA Exit Gate
A page cannot move to DONE until:
- Main Features complete.
- Registry components used without unauthorized forks.
- Arabic complete.
- English complete.
- RTL/LTR QA complete.
- Responsive QA complete.
- Keyboard/accessibility baseline checked.
- No broken links/assets.
- No console errors.
- Documentation updated.
- Source/rights check complete.

Copyright © ORVEAX.
