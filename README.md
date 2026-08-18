# TARGET HTML Edition

Commercial HTML productization track derived from the TARGET website experience.

## Repository purpose

This repository is the clean-room HTML edition. It is intentionally separated from the client implementation in `orveax/target`.

## Source authority

- Client implementation reference: `orveax/target`
- Commercial implementation authority: this repository
- Project/product decisions and conversion gates: TARGET Productization records in Notion

## Conversion rule

The HTML edition must preserve the approved website experience **section-by-section and feature-by-feature** before marketplace generalization.

Removing a framework does not mean removing a feature.

### Preserve

- Page structure and section order
- Visual hierarchy and spacing logic
- Responsive behavior
- RTL/LTR behavior
- Arabic/English switching
- Header, mega menu and mobile navigation behavior
- Card systems
- Product/company interaction pattern
- Forms and validation UX
- FAQ and utility interactions
- Accessibility behavior where applicable

### Replace / generalize

- TARGET logo and client identity
- Client emails, phone numbers, addresses and domains
- Supplier/company names and proprietary product data
- Client PDFs and company-profile files
- Client-specific legal and commercial claims
- Any asset without redistribution rights

## Target stack

- HTML5
- CSS3
- Vanilla JavaScript
- RTL + LTR
- Arabic + English
- No Astro runtime
- No Vue/Pinia runtime unless an explicit product decision later requires it

## Delivery sequence

1. M0 — Productization Gate
2. M1 — Fidelity Baseline / Design System Extraction
3. M2 — Full HTML Conversion
4. M3 — Commercial Generalization
5. M4 — Marketplace Components & Variants
6. M5 — Licensing & Assets
7. M6 — Documentation
8. M7 — Demo & Presentation
9. M8 — ThemeForest QA
10. M9 — Ready-to-Upload Package

## Current status

`M1 — Fidelity Baseline: STARTED`

First implementation target: `index.html` / Homepage 1:1 baseline.
