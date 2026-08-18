# ORIGEX — Design System Hierarchy V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: LOCKED FOR V1  
Scope: Main Features only

## 1. Purpose

ORIGEX uses one controlled design system. Pages compose approved building blocks; they do not redesign those building blocks locally.

Core principle:

> Define once → reuse everywhere → change centrally.

A page may choose an approved component or variant, change its content, and change documented semantic states. A page may not create a visual fork of an existing component through page-specific CSS.

## 2. System Hierarchy

### Level 0 — Foundations
Global visual and behavioral constants.

Includes:
- Brand colors and semantic colors.
- Typography families and type scale.
- Spacing scale.
- Container widths.
- Grid rules.
- Radius scale.
- Border scale.
- Shadow scale.
- Icon sizing.
- Motion duration/easing.
- Breakpoints.
- RTL/LTR direction rules.
- Focus/accessibility tokens.

Strategy: foundations never belong to one page. They are centrally defined and inherited.

Sample:
```css
:root {
  --orx-primary: #15343B;
  --orx-accent: #C47A4A;
  --orx-space-4: 1rem;
  --orx-radius-md: .75rem;
  --orx-duration-fast: 160ms;
}
```

### Level 1 — Primitives
Small reusable UI atoms that carry no page-specific business meaning.

Includes:
- Button.
- Icon button.
- Text link.
- Badge.
- Label.
- Input.
- Select.
- Checkbox.
- Radio.
- Textarea.
- Divider.
- Avatar/logo holder.
- Media frame.
- Tooltip trigger.

Strategy: primitives have few variants, strong states, and no page-specific overrides.

Sample:
```html
<a class="orx-btn orx-btn--primary" href="rfq.html">اطلب عرض سعر</a>
```

### Level 2 — Components
Reusable semantic UI units built from primitives.

Includes:
- Feature Card.
- Product Card.
- Supplier Card.
- Market Card.
- Process Card.
- Certification Card.
- Resource Card.
- Case Study Card.
- Contact Card.
- CTA Card.
- Search control.
- Filter group.
- Accordion item.
- Tab set.
- Pagination.
- Form field.
- File upload.
- Stat block.
- Breadcrumb.

Strategy: each component has a documented anatomy, allowed variants, states, responsive behavior, RTL behavior, and sample markup.

### Level 3 — Patterns
Compositions of several components that solve a repeated UX task.

Includes:
- Product filter bar.
- Supplier directory toolbar.
- RFQ form group.
- Process flow.
- Specification table.
- Trust strip.
- Resource/download grid.
- FAQ group.
- Contact-channel group.
- CTA cluster.
- Navigation group.

Strategy: patterns may rearrange approved components, but may not alter their internal visual contract.

### Level 4 — Sections
Page-level content blocks composed from patterns/components.

Section families:
- Hero.
- Standard content.
- Soft contrast.
- Dark emphasis.
- Data/specification.
- Directory/grid.
- Process.
- Trust/proof.
- Conversion/CTA.
- Utility/legal.

Strategy: sections control composition and rhythm. They do not redefine button, card, form or badge styling.

### Level 5 — Page Design Profiles
A page profile selects and sequences approved sections and components.

Each profile defines:
- Commercial goal.
- Hero family.
- Main section sequence.
- Content density.
- Allowed card families.
- CTA hierarchy.
- Interaction budget.
- Motion level.
- Mobile behavior.
- Arabic RTL notes.
- English LTR notes.
- Config-controlled values.

Strategy: a page gets identity through composition, not through creating a separate design language.

## 3. Component Immutability Rule

When an approved component is used inside a page:

Allowed:
- Replace content.
- Change image/data.
- Apply an approved modifier/variant.
- Apply semantic state: active, unavailable, featured, selected, error, success.
- Change placement and grid span if documented.

Not allowed:
- New border radius only for one page.
- New shadow only for one page.
- Different icon/title alignment only for one page.
- Different padding only because a page needs to 'look different'.
- Page CSS that rewrites core component anatomy.
- Duplicating the component under a new class with minor visual changes.

If a legitimate new requirement appears:
1. Check whether an approved variant already solves it.
2. If not, propose a new variant.
3. Add the variant to the central registry.
4. QA Arabic, English, responsive, accessibility.
5. Only then use it in a page.

## 4. Naming Strategy

Base component:
```text
.orx-card
```

Semantic family:
```text
.orx-product-card
.orx-supplier-card
.orx-process-card
```

Approved modifier:
```text
.orx-product-card--featured
.orx-product-card--compact
```

Semantic state:
```text
.is-active
.is-selected
.is-unavailable
.has-error
```

Page-specific selectors may control layout placement only:
```css
.products-page__grid .orx-product-card { /* placement/grid only */ }
```

They must not redefine the visual contract of `.orx-product-card`.

## 5. Documentation Contract for Every Component

Every component entry must contain exactly these headings:
1. Name / ID.
2. Purpose.
3. Hierarchy level.
4. Strategy.
5. Anatomy.
6. Approved variants.
7. Approved states.
8. Content rules.
9. RTL/LTR rules.
10. Responsive rules.
11. Accessibility rules.
12. Config eligibility.
13. Do / Don't.
14. HTML sample.
15. Pages using it.

## 6. Change Control

V1 pages consume the registry. They do not expand it casually.

A proposed new component/variant must answer:
- Is the use case repeated?
- Can an existing component solve it?
- Is it vertical-specific and commercially useful?
- Does it preserve performance and simplicity?
- Does it work in Arabic and English?
- Does it justify long-term maintenance?

If not, it does not enter V1.

## 7. Components Page Relationship

The future `Components / Elements` page is not a separate design experiment. It is a visual rendering of this registry and serves as:
- buyer reference,
- developer reference,
- QA reference,
- documentation examples source.

Copyright © ORVEAX.
