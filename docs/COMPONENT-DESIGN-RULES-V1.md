# ORIGEX — Component & Design Rules V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: REVIEW CANDIDATE

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
- Card family mix.
- CTA rhythm.
- Media treatment.
- Motion level.

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
- Never create page-specific decorative colors without design review.
- Accent is for emphasis, not large body backgrounds by default.
- Status colors must communicate state, not decoration.
- Contrast must remain accessible in both themes produced through config customization.

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
- English letter-spacing must not be copied into Arabic.
- Mixed LTR data in RTL pages uses bidi-safe helpers.
- No arbitrary font-size values inside page CSS unless a component token is being added.

## 4. Section Rules

Every section must declare one of four roles:
1. Standard content.
2. Soft contrast.
3. Dark emphasis.
4. Conversion / CTA.

Spacing families:
- Tight.
- Standard.
- Large.

Rules:
- Section spacing is consistent vertically.
- Adjacent sections may intentionally merge only when composition requires it.
- No zero-padding collisions between unrelated sections.
- Section headings use a repeatable anatomy: kicker → title → supporting copy → optional action.

## 5. Hero Rules

Maximum V1 hero families:
1. Split commercial hero.
2. Centered editorial hero.
3. Product / supplier detail hero.
4. Utility hero.

Rules:
- Hero must communicate page purpose within the first viewport.
- One primary CTA; maximum one secondary CTA.
- No decorative sliders unless the page purpose benefits materially.
- Mobile hero order is explicitly defined, never accidental reflow.

## 6. Card System

Card is a system, not a generic box.

Approved card families:
- Feature Card.
- Product Card.
- Supplier / Brand Card.
- Market Card.
- Process Card.
- Metric / Stat Card.
- Certification Card.
- Download / Resource Card.
- Case Study Card.
- Contact / Department Card.
- CTA Card.

Shared card anatomy where applicable:
- optional icon/media.
- eyebrow/category.
- title.
- supporting text.
- metadata.
- action.
- optional status/badge.

Rules:
- Icon and title align consistently.
- One card family uses one radius and one primary border/shadow treatment.
- Cards must not rely only on hover to reveal essential information.
- Hover movement stays restrained.
- Active/selected states are semantic and visible.
- RTL ordering and directional icons are explicitly mirrored when necessary.

## 7. Button Rules

Approved variants:
- Primary.
- Secondary.
- Ghost.
- Text link.
- Icon-only utility.

Approved sizes:
- Small.
- Default.
- Large.

Rules:
- One primary button per local decision area.
- Button copy uses actions, not vague labels.
- Minimum touch target must remain mobile-friendly.
- Focus-visible state is mandatory.
- Directional arrows mirror in RTL.

## 8. Form Rules

Form families:
- Contact.
- RFQ.
- Submit Product.
- Partner / Distributor application.
- Newsletter / simple lead.

Rules:
- Visible labels; placeholder is not a label.
- Required/optional state is explicit.
- Error text appears next to the affected field.
- Success and failure states are designed.
- File upload UI is accessible.
- Telephone/email/SKU fields remain bidi-safe on Arabic pages.
- Backend processing is not implied; documentation explains integration points.

## 9. Tables & Specification Rules

Use tables for:
- Product specifications.
- Compliance matrices.
- Service comparisons.
- SLA / responsibility matrices.

Rules:
- Mobile fallback is defined: scroll, stacked rows, or definition-list layout.
- Header cells are semantic.
- No dense table is left unusable at 360px.

## 10. Tabs, Accordions, Filters & Modals

Rules:
- Keyboard accessible.
- ARIA/state attributes synchronized.
- Deep linking used when materially useful.
- Filter empty states designed.
- Mobile filter drawer available when horizontal controls become crowded.
- Modal/off-canvas focus is controlled.

## 11. Badges & Status

Badge families:
- Category.
- Origin.
- Certification.
- Availability.
- Featured.
- New / Updated.

Rules:
- Do not use color alone to communicate meaning.
- Badge vocabulary is limited and documented.

## 12. Icon Rules

- One primary semantic icon system for V1.
- No mixing multiple icon libraries for the same semantic role.
- Decorative icons are optional and must not be required to understand content.
- Directional icons mirror in RTL.
- Icons must align to the same optical sizing system.

## 13. Image & Media Rules

- Product imagery uses consistent aspect-ratio families.
- Supplier logos use a controlled logo container.
- Preview-only imagery is tracked separately from distributable assets.
- No client/TARGET assets enter the commercial product.
- Lazy loading is default below the fold.
- Alt text required when informative.

## 14. Motion Rules

Motion levels:
- Level 0: utility/legal pages — near-static.
- Level 1: most corporate/product pages — subtle hover/fade/slide.
- Level 2: selected home/landing sections — controlled premium reveals.

Rules:
- No scroll-jacking.
- No motion that hides or delays essential content.
- `prefers-reduced-motion` supported.
- Avoid heavy animation libraries by default.
- Motion duration and easing come from tokens.

## 15. Config Eligibility Rules

Good candidates for `config.js`:
- global colors.
- company name/contact details.
- social links.
- business hours.
- announcement bar.
- global CTA.
- WhatsApp.
- global show/hide switches.

Not suitable for `config.js`:
- complete page copy.
- products.
- suppliers.
- blog content.
- complex page layout.
- large section markup.

Structured data belongs in dedicated JSON files when needed.

## 16. Data Files Planned

- `assets/data/products.json`
- `assets/data/suppliers.json`
- `assets/data/markets.json`

Rules:
- Human-readable.
- Simple schema.
- Documented examples.
- Graceful fallback when JavaScript is unavailable where possible.

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
- Mobile is not a compressed desktop layout.
- Navigation, filters, tables, hero media and CTAs receive explicit mobile behavior.
- No horizontal overflow.
- Content order is checked in Arabic and English independently.

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
- CSS and Vanilla JS only for V1 unless a dependency has a clear measurable benefit.
- Avoid unnecessary runtime frameworks.
- Lazy-load below-fold media.
- Defer non-critical scripts.
- Keep animation lightweight.
- No third-party script required for core layout/navigation.

## 20. Ecommerce / Cart Rule

V1 has no cart or checkout. If a future ecommerce edition is created, it must be a separate product/version scope. Current conversion patterns are RFQ, enquiry, sample request, submit product and partner/distributor applications.

## 21. Page Design Profile Template

Before building a page, record:
- Page ID / name.
- Commercial goal.
- Main features.
- Additional features.
- Hero family.
- Section sequence.
- Primary card families.
- Interaction list.
- Motion level.
- Config values.
- Arabic RTL notes.
- English LTR notes.
- Mobile risks.
- Asset/license requirements.
- Documentation entries.

Copyright © ORVEAX.