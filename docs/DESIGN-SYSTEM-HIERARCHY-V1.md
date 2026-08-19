# ORIGEX — Design System Hierarchy V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED & LOCKED  
Scope: V1 Main Features only  
Normalized: 2026-08-19 Hard Audit

ORIGEX uses one controlled design system. Pages compose registered building blocks; they do not redesign those blocks locally.

Core principle:

> Define once → register → reuse everywhere → change centrally.

## 1. Architecture Stack

```text
Infrastructure Layer — Bootstrap 5.3.8
        ↓
F — ORIGEX Foundations
        ↓
P — Primitives
        ↓
C — Components
        ↓
PT / N — Reusable Patterns & Global Navigation
        ↓
S — Sections
        ↓
PG — Page Design Profiles
```

Bootstrap is below the ORIGEX Design System. It provides infrastructure; it is not a branded hierarchy level and cannot bypass the registry.

## 2. Infrastructure Layer — Bootstrap 5.3.8

Allowed roles:
- grid;
- containers;
- breakpoints;
- selected layout/display/spacing utilities;
- selected behavior primitives when approved centrally.

Not allowed:
- using default Bootstrap cards/buttons/forms/navigation styling as ORIGEX design language;
- page-by-page mixing of Bootstrap behavior with different custom implementations for the same interaction.

Exact technology authority: `TECH-STACK-V1.md`.

## 3. F — Foundations

Global constants and systems that never belong to one page.

Registered in `COMPONENT-REGISTRY-V1.md`:
- F01 Color System
- F02 Typography System
- F03 Spacing, Grid & Layout
- F04 Shape, Border & Elevation
- F05 Icon System
- F06 Motion & Interaction
- F07 Media & Pattern Foundations

Strategy: foundations are inherited by every primitive/component/page. A page cannot create an alternative foundation.

## 4. P — Primitives

Small reusable UI atoms with minimal business meaning.

Current primitive registry:
- P01 Primary Button
- P02 Secondary Button
- P03 Text Action
- P04 Icon Button
- P05 Badge
- P06 Form Input
- P07 Select
- P08 Textarea
- P09 Checkbox / Radio
- P10 Divider
- P11 Icon Container

Strategy: few variants, strong states, consistent accessibility and no page-local overrides.

## 5. C — Components

Reusable semantic UI units composed from foundations/primitives.

Current registered families C01–C28 include:
- Feature / Product / Supplier / Market / Process / Metric / Certification / Resource / Case Study / Contact / CTA cards;
- Breadcrumb / Tabs / Accordion / Pagination / Search / Filters;
- Specification / Trust / Empty / Alert;
- Form Field / File Upload / Form Status;
- Product Media / Logo Frame / Editorial Media.

Detailed IDs and contracts live only in `COMPONENT-REGISTRY-V1.md`.

Strategy: a component keeps the same core anatomy across pages. Content, approved variant/state and placement may change; its visual contract may not.

## 6. PT / N — Patterns

Patterns solve repeated UX/composition tasks using registered components.

### Visual pattern families
Authority: `PATTERN-SYSTEM-V1.md`.

- PT01 Route Lines
- PT02 Trade Grid
- PT03 Dot Matrix
- PT04 Market Nodes
- PT05 Packaging Geometry
- PT06 Flow Lines

### Global navigation patterns
- N01 Site Header
- N02 Mega Menu
- N03 Mobile Drawer
- N04 Footer

Other repeated UX compositions may be documented as patterns during implementation only if they reuse registered components and pass change control.

## 7. S — Sections

Registered section families:
- S01 Section Header
- S02 Split Hero
- S03 Centered Editorial Hero
- S04 Detail Hero
- S05 Utility Hero
- S06 Final CTA

Sections control page composition/rhythm and may combine components. They do not redefine components.

## 8. PG — Page Design Profiles

Every page receives a Page Design Profile before implementation.

A profile defines:
- Page ID / SEO identity;
- commercial goal and audience;
- Content Contract / C6 status;
- Main Features;
- component/section IDs;
- section sequence;
- density and media treatment;
- interaction budget;
- config eligibility;
- AR RTL / EN LTR behavior;
- responsive/accessibility/performance contracts;
- assets/licenses;
- QA exit conditions.

A page gets identity through **content + composition**, not a private design system.

## 9. Component Immutability Rule

Allowed at page level:
- change content/data;
- select approved variant;
- select semantic state;
- change documented grid span/placement;
- compose registered units.

Not allowed:
- new radius/shadow/padding just for one page;
- page-specific icon grammar;
- different button/form/card anatomy;
- duplicate component class with minor visual changes;
- hidden hotfix override layer.

If a real repeated need appears:

```text
Check existing registry
→ confirm gap
→ define central variant/component
→ document/register
→ AR/EN/mobile/accessibility QA
→ reuse
```

## 10. Naming

ORIGEX-owned classes:
```text
.orx-component
.orx-component__part
.orx-component--variant
```

State classes:
```text
.is-active
.is-selected
.is-unavailable
.has-error
```

JavaScript hooks use `data-orx-*`; CSS styling must not depend on JS-only hook names.

Page selectors may control placement/composition only, never shared component internals.

## 11. Documentation Contract

The registry is intentionally concise. A component/primitive entry must define the information needed for implementation without duplicating global rules already owned by companion authorities.

Minimum required where applicable:
- ID / name;
- hierarchy level;
- purpose;
- anatomy/strategy;
- approved variants/states;
- critical rule(s);
- dependency/authority reference when needed.

Global RTL, accessibility, icon, media, shape and motion rules may be referenced rather than repeated in every entry.

The implementation itself and Components/Elements page provide executable/visual examples during M1/M6.

## 12. Change Control

A new component/variant must answer:
- Is the need repeated?
- Can an existing registered unit solve it?
- Is it commercially useful for this vertical?
- Does it preserve static simplicity/performance?
- Does it work AR/EN and mobile?
- Does it justify maintenance?

If not, it does not enter V1.

## 13. Components Page Relationship

PG32 Components / Elements is a rendering of the same registry, not an independent design experiment. It serves buyer reference, developer reference and QA evidence.

Current implementation status is tracked in `IMPLEMENTATION-STATUS-V1.md`.

Copyright © ORVEAX.
