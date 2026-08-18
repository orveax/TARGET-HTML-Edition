# ORIGEX — Page Build Rules

Product: ORX-P01  
Owner / Author: ORVEAX  
Status: LOCKED WORKING RULES

These rules are reviewed before building or expanding any page in ORIGEX.

## 1. Arabic-first bilingual rule

- Arabic is the primary/default presentation language.
- English is the secondary language and must be complete, not partial.
- Every page, component and preview must support both Arabic and English.
- RTL/LTR behavior is a first-class architecture requirement, not a final CSS patch.
- Directional icons, arrows, breadcrumbs, drawers, forms, mixed Arabic/English content, numbers, SKUs, emails and product codes must be QA-reviewed in both directions.

## 2. Fidelity-first rule

- Preserve the purpose, hierarchy, content density and commercial logic of the approved source page before adding marketplace improvements.
- No core section may be removed silently.
- Any intentional change must be documented as a Marketplace Improvement or Generalization.

## 3. Core Sections + Optional Feature Slots

Each page is designed in two layers:

1. **Core Sections** — the default commercial page experience. These remain concise, focused and suitable for most buyers.
2. **Optional Feature Slots** — ready-to-use sections/components that are not necessarily shown in the main demo page, but are included so the buyer can extend the page without redesigning from scratch.

Optional features must use the same ORIGEX design system, RTL/LTR rules, responsiveness and documentation standards as core sections.

## 4. Feature discovery before every page

Before implementation, audit the page for:

- Essential sections for the page type.
- Useful sections missing from the TARGET baseline.
- Additions that increase marketplace value without bloating the default page.
- Classification of every candidate as **Core**, **Optional**, or **Not in V1**.

## 5. About page example — optional features

The default About page can stay focused while ORIGEX still ships reusable optional About components such as:

- Company History / Timeline — e.g. 2020 → 2026 milestones.
- Key milestones / achievements.
- Leadership / management preview.
- Certifications & compliance.
- Markets / countries served.
- Company statistics / counters.
- Values / principles.
- Office / warehouse / facility block.
- Partners / memberships / affiliations.

These features do not need to appear simultaneously in the default About demo. They should exist as documented optional building blocks so a buyer can activate the right combination.

## 6. No feature dumping

- More features do not automatically mean a better template.
- Do not overload the main page with every available component.
- Default demos must remain commercially coherent and premium.
- Optional sections belong in the component library, alternative demo, or documented insertion patterns when they are not essential to the primary page story.

## 7. Reusability rule

A new optional feature should be built as a reusable pattern whenever practical, not page-specific one-off markup.

Examples:

- Timeline.
- Stats / counters.
- Certification cards.
- Team strip.
- Download block.
- Market map.
- Testimonials.
- Logo wall.
- CTA variants.

## 8. Simple Config eligibility rule

Before every page/component build, identify which values belong in the global `assets/js/config.js` customization layer.

**Good config candidates:**

- Brand/theme colors.
- Repeated company contact data.
- Social URLs.
- Business hours.
- Announcement/top bar content and visibility.
- Global header CTA.
- Sticky header / mega-menu visibility.
- Floating WhatsApp / Back-to-top controls.
- Other small global on/off switches that genuinely reduce buyer editing effort.

**Do not put in global config:**

- Long page copy.
- Entire About/Services sections.
- Product, supplier or blog records.
- Layout construction.
- Large per-page content structures.

The goal is a simple buyer customization layer, not a CMS or page builder.

Every global/contact/footer component should use documented config hooks where practical while preserving a valid HTML fallback.

## 9. Progressive enhancement rule

- Pages must remain structurally usable if the config engine is unavailable.
- Essential content must exist in HTML; config may replace/reuse repeated values but must not become the only source of page meaning.
- JavaScript enhancements must not break navigation or reading when disabled.

## 10. Pre-build decision record

Before implementation of every new page, record:

- Page goal.
- Core sections.
- Optional feature candidates.
- Config-eligible global values.
- Arabic-specific UX considerations.
- English counterpart.
- Responsive risks.
- Required interactions.
- Asset/licensing requirements.
- Final V1 inclusion decision.

## 11. Gate condition

No new page moves into implementation until this rule set has been reviewed and the page-specific Core / Optional / Not-in-V1 / Config-eligible decisions are recorded.

Copyright © ORVEAX.
