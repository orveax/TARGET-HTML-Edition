# ORIGEX — Component & Design Rules V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: LOCKED FOR V1

This document defines the global rules. Detailed component contracts live in:
- `DESIGN-SYSTEM-HIERARCHY-V1.md`
- `COMPONENT-REGISTRY-V1.md`
- `PAGE-DESIGN-PROFILE-TEMPLATE-V1.md`

## 1. One Global System, Many Page Profiles

ORIGEX uses one global visual/UX system. Individual pages receive a Page Design Profile, not an independent design system.

Global invariants:
- Brand palette.
- Typography hierarchy.
- Spacing scale.
- Border/radius scale.
- Shadow scale.
- Container widths.
- Button language.
- Form language.
- Icon language.
- Motion budget.
- Arabic RTL and English LTR behavior.

Page-level variables:
- Hero pattern.
- Section sequence.
- Density.
- Approved card family mix.
- CTA rhythm.
- Media treatment.
- Motion level.

Pages may compose approved components but may not visually fork them through page-specific CSS.

## 2. Color Rules

Core configurable colors live in `config.js` and CSS variables.

Approved roles:
- Primary / Primary Strong.
- Secondary.
- Accent.
- Background.
- Surface.
- Surface Soft.
- Text.
- Text Muted.
- Border.
- Success / Warning / Danger / Info only when semantically required.

Rules:
- Never create page-specific decorative colors without registry/design review.
- Accent is for emphasis, not large body backgrounds by default.
- Status colors communicate state, not decoration.
- Contrast must remain accessible after documented config customization.

## 3. Typography Rules

Arabic: Tajawal.  
English: Manrope.

Hierarchy:
- Display.
- H1.
- H2.
- H3.
- H4.
- Body Large.
- Body.
- Small.
- Label / Eyebrow.
- Button / UI.

Rules:
- Arabic line-height is independently tuned.
- English letter-spacing is not copied into Arabic.
- Mixed LTR data in RTL pages uses bidi-safe helpers.
- No arbitrary font-size values in page CSS.

## 4. Section Rules

Every section declares a role:
1. Standard content.
2. Soft contrast.
3. Dark emphasis.
4. Data/specification.
5. Directory/grid.
6. Process.
7. Trust/proof.
8. Conversion / CTA.
9. Utility/legal.

Spacing families:
- Tight.
- Standard.
- Large.

Rules:
- Section spacing remains consistent vertically.
- Adjacent sections may merge only by documented composition.
- No zero-padding collisions between unrelated sections.
- Standard section-heading anatomy is controlled by Registry S01.

## 5. Hero Rules

V1 hero families are fixed in the registry:
1. S02 Split Commercial Hero.
2. S03 Centered Editorial Hero.
3. S04 Detail Hero.
4. S05 Utility Hero.

Rules:
- Hero communicates page purpose in the first viewport.
- One primary CTA; maximum one secondary CTA.
- No decorative sliders unless scope explicitly changes.
- Mobile content order is explicitly defined.

## 6. Card System

A card is a registered semantic component, not a generic box.

Approved families are defined as C01–C11 in `COMPONENT-REGISTRY-V1.md`.

Rules:
- A page chooses a registered card family and approved variant.
- A page may not change the component's core radius, padding, shadow, icon/title alignment, or anatomy.
- Content and approved semantic states may change.
- Hover never hides essential information.
- RTL ordering/directional icons are explicitly handled.
- Any new variant is added to the central registry before page use.

## 7. Button Rules

Approved primitives:
- P01 Primary.
- P02 Secondary.
- P03 Text Action.
- P04 Icon Button.

Rules:
- One primary button per local decision area.
- Copy uses explicit actions.
- Touch target remains mobile-friendly.
- Focus-visible is mandatory.
- Directional arrows mirror in RTL.
- No page-specific button shapes/colors.

## 8. Form Rules

Form families:
- Contact.
- RFQ.
- Submit Product.
- Partner / Distributor application.
- Newsletter / simple lead.

All forms are composed from registry primitives/components P06–P09 and C23–C25.

Rules:
- Visible labels; placeholder is not a label.
- Required/optional state explicit.
- Error text associated with field.
- Success/failure states designed.
- File upload accessible.
- Telephone/email/SKU bidi-safe in Arabic.
- Static template does not imply backend processing.

## 9. Tables & Specification Rules

Registry authority: C18 Specification Table.

Use for:
- Product specifications.
- Compliance matrices.
- Service comparisons.
- Responsibility tables.

Rules:
- Mobile fallback defined.
- Header cells semantic.
- No dense unusable 360px table.

## 10. Tabs, Accordions, Filters & Modals

Registry authorities include C13–C17.

Rules:
- Keyboard accessible.
- ARIA/state synchronized.
- Empty states designed.
- Mobile filters use a controlled drawer/pattern when crowded.
- Focus controlled for modal/off-canvas.

## 11. Badges & Status

Registry authority: P05 Badge.

Semantic families:
- Category.
- Origin.
- Certification.
- Availability.
- Featured.
- Updated.

Rules:
- No color-only meaning.
- Vocabulary limited and documented.

## 12. Icon Rules

- One primary semantic icon system for V1.
- No duplicate icon libraries for same roles.
- Decorative icons optional.
- Directional icons mirror in RTL.
- Optical sizing standardized.

## 13. Image & Media Rules

Registry authorities: C26–C28.

- Product imagery uses controlled aspect ratios.
- Supplier logos use C27 Logo Frame.
- Preview-only imagery tracked separately.
- No TARGET/client assets in commercial package.
- Lazy loading below the fold.
- Alt text required when informative.

## 14. Motion Rules

Motion levels:
- Level 0: utility/legal — near-static.
- Level 1: most business/product pages — subtle transitions.
- Level 2: selected home/landing areas — controlled premium reveals.

Rules:
- No scroll-jacking.
- No motion delaying essential content.
- `prefers-reduced-motion` supported.
- No heavy animation library by default.
- Duration/easing come from tokens.

## 15. Config Eligibility Rules

Good `config.js` candidates:
- global colors.
- company/contact details.
- social links.
- business hours.
- announcement bar.
- global CTA.
- WhatsApp.
- global show/hide switches.

Not for `config.js`:
- full page copy.
- products.
- suppliers.
- blog content.
- complex layout.
- large markup.

## 16. Data Files Planned

- `assets/data/products.json`
- `assets/data/suppliers.json`
- `assets/data/markets.json`

Rules:
- Human-readable.
- Simple schema.
- Documented examples.
- Graceful fallback where practical.

## 17. Responsive Rules

Primary QA widths:
- 360.
- 390.
- 412.
- 768.
- 820.
- 1024.
- 1280.
- 1366.
- 1440.
- 1536.
- 1920.

Rules:
- Mobile is not compressed desktop.
- Navigation, filters, tables, hero media and CTAs have explicit mobile behavior.
- No horizontal overflow.
- Arabic and English content order checked independently.

## 18. Accessibility Rules

- Semantic HTML.
- Keyboard navigation.
- Visible focus.
- ARIA only where native HTML is insufficient.
- Contrast checks.
- Reduced motion.
- Form error association.
- Meaningful alt text.
- Skip link.

## 19. Performance Rules

- Static HTML first.
- CSS + Vanilla JS for V1 unless a dependency has measurable benefit.
- Avoid unnecessary runtime frameworks.
- Lazy-load below-fold media.
- Defer non-critical scripts.
- Lightweight motion.
- No third-party script required for core layout/navigation.

## 20. Ecommerce / Cart Rule

V1 has no cart or checkout. Current conversion patterns are RFQ, enquiry, submit product and partner/distributor applications. Ecommerce requires a future separate scope.

## 21. V1 Main-Features Rule

V1 implementation contains only Main Features defined in the frozen scope.

Additional Features are not implemented in V1. They are retained only in the V1.1 Expansion Backlog.

## 22. Page Design Profile Rule

Before coding any page, complete `PAGE-DESIGN-PROFILE-TEMPLATE-V1.md` and declare registry IDs for every major UI building block.

If a required component has no registry ID, stop and review the central registry. Do not create a page-local fork.

Copyright © ORVEAX.