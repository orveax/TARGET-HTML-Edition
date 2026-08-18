# ORIGEX — V1 Scope Freeze Candidate

Product ID: ORX-P01  
Owner: ORVEAX  
Status: REVIEW CANDIDATE — NOT YET FROZEN  
Vertical: B2B Food Trading / Import / Distribution / Suppliers  
Language: Arabic-first RTL + English LTR

## 1. Product Strategy

ORIGEX V1 is a premium commercial HTML template, not a generic multipurpose template and not a copy of the TARGET client website. It must be large enough to feel complete, but simple enough for a buyer with limited coding experience to use and customize.

Primary differentiation:
- Arabic-first RTL, full English LTR.
- Vertical-specific B2B food-trading UX.
- Product / supplier / market / RFQ systems.
- One-file simple customization layer (`config.js`).
- Reusable Additional Features library.
- Strong documentation written for beginner users.
- Fast static HTML, CSS and Vanilla JS architecture.

## 2. Scope Rule

Every page is defined before implementation with:
1. Main Features — visible by default.
2. Additional Features — 3 to 10 reusable/manual sections shipped with the template.
3. Page Design Profile — page-specific composition derived from one global ORIGEX design system.
4. Config Eligibility — global settings controlled from `config.js` only when appropriate.
5. RTL/LTR notes.
6. Interaction budget.
7. Documentation entry.

No page implementation starts until these are frozen.

## 3. V1 Page Architecture — 32 Unique Layouts / 64 Ready HTML Pages

### 01 — Home 01 / Food Trading & Importer
**Main Features:** hero, trade route visual, trust row, how-we-work cards, product categories, why ORIGEX, four-step start, featured products, supplier CTA, FAQ preview, final CTA.
**Additional Features:** stats counters; featured brands; market map; certification strip; testimonials; latest insights; newsletter block.

### 02 — Home 02 / Wholesale & Distribution
**Main Features:** distribution-led hero, channels overview, warehouse/coverage story, product categories, distribution process, key metrics, route-to-market blocks, RFQ CTA.
**Additional Features:** logistics timeline; customer logo wall; territory tabs; fleet/warehouse media; service-level stats; channel comparison.

### 03 — Home 03 / Manufacturer & Supplier
**Main Features:** manufacturer-led hero, production capability, product range, certifications, export markets, private-label capability, quality workflow, enquiry CTA.
**Additional Features:** facility gallery; capacity counters; export-document checklist; sample request block; certifications carousel; testimonials.

### 04 — Landing / One Page
**Main Features:** focused hero, benefits, selected categories, proof/trust, process, conversion CTA, compact contact form.
**Additional Features:** lead magnet; video block; stats; logo wall; FAQ; sticky CTA.

### 05 — About
**Main Features:** hero, who we are, facts, vision/mission, commercial role, commercial clarity, final CTA.
**Additional Features:** company history timeline; milestones; leadership preview; values; statistics; certifications; markets served; facilities; affiliations.

### 06 — How We Work
**Main Features:** hero, qualification logic, four-step process, roles/responsibilities, required information, decision flow, next-step CTA.
**Additional Features:** detailed timeline; onboarding checklist; SLA table; RACI-style responsibility matrix; downloadable process PDF; process FAQ; process diagram.

### 07 — Capabilities / Services
**Main Features:** capability grid, service families, market-entry support, product/supplier support, channel/distribution support, CTA.
**Additional Features:** tabbed service view; comparison table; related case study; service FAQ; industry/use-case strip; service stats.

### 08 — Service Details
**Main Features:** service hero, overview, scope, process, deliverables, fit/not-fit guidance, related services, CTA.
**Additional Features:** service checklist; FAQ; stats; download block; case study; timeline.

### 09 — Product Categories
**Main Features:** hero, category grid, category filters, category cards, category facts, CTA.
**Additional Features:** featured categories; category counts; category banner; certification icons; quick links; category FAQ.

### 10 — Products Grid
**Main Features:** search, category filter, brand filter, origin filter, product cards, pagination, RFQ CTA.
**Additional Features:** grid/list switch; sorting; quick-view modal; compare UI; featured products; sticky filter drawer; empty-state component.

### 11 — Product Details
**Main Features:** product media, name, brand, category, country of origin, pack size, packaging, shelf life, storage, MOQ, availability, certifications, datasheet, brochure, RFQ, related products.
**Additional Features:** nutrition facts; ingredients; pallet/shipping data; private-label block; technical tabs; product FAQ; sample request; downloadable specification sheet.

### 12 — Suppliers / Brands Directory
**Main Features:** search, category filter, origin filter, supplier/brand cards, featured suppliers, commercial CTA.
**Additional Features:** alphabet filter; map view; certification filter; category tabs; supplier comparison; logo wall; empty state.

### 13 — Supplier / Brand Details
**Main Features:** supplier profile, origin, categories, featured products, certifications, markets, relationship facts, CTA.
**Additional Features:** company timeline; facilities; documents/downloads; quality facts; gallery; related suppliers; contact card.

### 14 — Market Access
**Main Features:** hero, market-entry model, channel model, fit criteria, route-to-market process, opportunity review, CTA.
**Additional Features:** market map; statistics; regulatory checklist; case study; channel comparison; FAQ.

### 15 — Markets / Countries
**Main Features:** region/country filters, country cards, market map, channel tags, market overview, CTA.
**Additional Features:** region tabs; trade-data placeholders; market-detail modal; distribution-channel comparison; market FAQ; opportunity tags.

### 16 — For Suppliers
**Main Features:** supplier value proposition, qualification criteria, process, required documents, commercial boundaries, CTA, FAQ.
**Additional Features:** supplier testimonial; onboarding timeline; downloadable checklist; sample document list; supplier stats; brand logo wall.

### 17 — Submit Your Product
**Main Features:** company information, product information, category, origin, packaging, MOQ, certifications, file upload UI, consent, validation, submission state.
**Additional Features:** multi-step form; dynamic product rows; downloadable preparation checklist; WhatsApp fallback; product preview summary; save/print summary UI.

### 18 — Request a Quote / RFQ
**Main Features:** buyer details, product selection, quantity, destination, target timing, notes, attachment UI, consent, validation, confirmation state.
**Additional Features:** multi-product rows; print RFQ summary; preferred contact method; quick product search; WhatsApp fallback; RFQ FAQ.

### 19 — Become a Distributor / Partner
**Main Features:** partnership value, qualification criteria, markets/territories, company profile form, portfolio upload UI, CTA.
**Additional Features:** territory interests; portfolio categories; downloadable checklist; FAQ; partner benefits comparison; process timeline.

### 20 — Case Studies
**Main Features:** filters, case-study cards, industry/category tags, result highlights, CTA.
**Additional Features:** featured case study; stats; market filter; supplier filter; testimonial strip; pagination.

### 21 — Case Study Details
**Main Features:** challenge, context, approach, process, result, metrics, related case studies, CTA.
**Additional Features:** timeline; before/after metrics; testimonial; gallery; downloads; key-takeaways box.

### 22 — Downloads / Company Profile / Resources
**Main Features:** resource categories, company profile, brochures, datasheets, certificates, language tags, download actions.
**Additional Features:** search; filters; version labels; featured download; gated-download UI pattern; update date; resource FAQ.

### 23 — Certifications & Compliance
**Main Features:** certification categories, quality framework, storage/handling principles, traceability demo, document types, CTA.
**Additional Features:** compliance matrix; audit timeline; certification logo grid; quality stats; downloadable checklist; FAQ.

### 24 — Insights / Blog
**Main Features:** featured article, category filters, article grid, search, pagination.
**Additional Features:** popular articles; author strip; newsletter; topic tags; related resources; compact list view.

### 25 — Article Details
**Main Features:** article header, metadata, content typography, share links, related articles, CTA.
**Additional Features:** table of contents; author box; inline CTA; downloadable resource; reading progress; next/previous navigation.

### 26 — FAQ
**Main Features:** category navigation, search, accordion, supplier/buyer groups, contact CTA.
**Additional Features:** deep links; print view; feedback UI; popular questions; support links; related downloads.

### 27 — Contact
**Main Features:** contact channels, departments, enquiry form, address, business hours, social links, map placeholder, CTA.
**Additional Features:** appointment request; file upload UI; WhatsApp; contact FAQ; department cards; route/directions block.

### 28 — 404
**Main Features:** branded error state, clear explanation, home link, search/recovery links, contact fallback.
**Additional Features:** suggested pages; popular resources; featured categories; compact newsletter.

### 29 — Coming Soon / Under Construction
**Main Features:** logo, status message, launch date/countdown, subscribe UI, social links, contact link.
**Additional Features:** progress bar; background variants; maintenance mode copy; launch checklist; announcement strip.

### 30 — Privacy
**Main Features:** sample legal structure, table of contents, updated date, contact reference, legal disclaimer.
**Additional Features:** print view; anchor navigation; jurisdiction placeholder; cookie section; download PDF link.

### 31 — Terms
**Main Features:** sample terms structure, table of contents, updated date, contact reference, legal disclaimer.
**Additional Features:** print view; anchor navigation; jurisdiction placeholder; supplier-terms note; download PDF link.

### 32 — Components / Elements Library
**Main Features:** buttons, cards, badges, headings, tabs, accordions, forms, tables, alerts, stats, timelines, CTA blocks, product UI, supplier UI, market UI, utility states.
**Additional Features:** layout snippets; section variants; hero variants; color examples; RTL/LTR examples; config examples; copy/paste insertion examples; accessibility examples.

## 4. Intentional Scope Changes from Earlier Draft

### Removed as standalone V1 pages
- Team.
- Careers.

Reason: useful but weakly tied to the B2B food-trading vertical. They remain available as Additional Features / components and can become full pages in V1.1 without affecting the V1 architecture.

### Added as standalone V1 page
- Certifications & Compliance.

Reason: materially more valuable for food trading, suppliers, importers and distributors than generic Team/Careers pages.

## 5. No Ecommerce Cart in V1

No cart, checkout, payment, customer account or order-management system ships in V1. The template is B2B conversion-led:
- RFQ.
- Product enquiry.
- Sample request.
- Submit product.
- Become distributor / partner.
- Download datasheet / brochure.

## 6. Interaction Strategy

ORIGEX must feel interactive without becoming heavy.

Allowed by default:
- Accessible mega menu / mobile drawer.
- Tabs.
- Accordions.
- Search / filter / sorting.
- Lightweight modals / off-canvas panels.
- Counters when meaningful.
- Form validation.
- Back-to-top / WhatsApp / announcement bar.
- Restrained reveal / hover / transition effects.

Avoid in V1:
- Heavy animation frameworks unless a specific interaction cannot be achieved cleanly otherwise.
- Scroll-jacking.
- Autoplay-heavy media.
- Particle/canvas effects as core UX.
- Animation that delays content access.

## 7. Page Design Profile Rule

ORIGEX has one global design system. Each page gets a Page Design Profile containing:
- Page purpose.
- Hero family.
- Section rhythm.
- Content density.
- Primary card families.
- CTA hierarchy.
- Motion level: 0 / 1 / 2.
- Mobile priority behavior.
- Arabic RTL notes.
- English LTR notes.
- Config-controlled values.

This gives each page identity without fragmenting the product into separate design systems.

## 8. Scope Freeze Condition

This document becomes FROZEN only after explicit approval. After freeze, new V1 pages or feature families require a Scope Change record. Small UX, QA, accessibility, performance and content refinements do not reopen scope.

Copyright © ORVEAX.