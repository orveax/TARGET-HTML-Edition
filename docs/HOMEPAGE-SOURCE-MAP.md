# Homepage Source Map — Fidelity Baseline

Source authority: `orveax/target/src/components/HomePremium.astro`

This document freezes the complete homepage composition before conversion. No item below may disappear silently.

## Global shell

1. Header
2. Desktop navigation
3. Mega menu
4. Language switch
5. Primary commercial CTA
6. Mobile offcanvas navigation
7. Footer
8. Footer contact/resource/legal hierarchy

## Homepage composition

### H01 — Hero
- Eyebrow
- H1
- Lead copy
- Primary CTA
- Secondary CTA
- Media panel
- Media tag
- Commercial route visual
  - Manufacturer / Supplier node
  - Fit-review / center node
  - Market node

### H02 — Trust strip
Four trust/fact items:
1. Local-market context
2. Trading/import role
3. Manufacturers/suppliers/brands
4. Product-fit-before-commitment

### H03 — How We Work
- Section kicker
- H2
- Intro copy
- Four feature cards
  1. Import & Trading
  2. Working with Manufacturers & Suppliers
  3. Sales & Distribution Channels
  4. Product Opportunity Development
- Explore/full-process link

### H04 — Products & Categories
- Section kicker
- H2
- Intro copy
- Editorial image
- Five category cards
- Portfolio explore link

### H05 — Why / Differentiation
- Section kicker
- H2
- Intro copy
- Four differentiation items
  1. Market focus
  2. Product fit first
  3. Direct commercial discussion
  4. Clear agreement before execution

### H06 — How to Start
- Section kicker
- H2
- Intro copy
- Four-step ordered journey
  1. Share the Product
  2. Review the Fit
  3. Agree How to Work
  4. Move to Next Steps
- Full-process link

### H07 — Homepage FAQ
- Section kicker
- H2
- Three accordion items
- First item open by default
- Accessible `aria-expanded`, `aria-controls`, panel relationship
- View-all-FAQ link

### H08 — Final Conversion CTA
- Kicker
- H2
- Lead copy
- Commercial disclaimer
- Primary CTA
- Secondary contact CTA

## Fidelity acceptance rule

Homepage conversion is not `MATCHED` until:

- all H01–H08 sections exist;
- header, navigation, language and footer systems work;
- Arabic/English text switching works;
- RTL/LTR flips correctly;
- mobile navigation works;
- homepage FAQ works;
- responsive hierarchy is verified;
- no client-only identity/content ships unintentionally.

## Commercial generalization rule

The product may change names, geography, demo assets and copy, but it must preserve each section's UX purpose and feature density.
