# ORIGEX — PG20 Case Studies | Page Design Profile V1

Product ID: ORX-P01  
Milestone: M5 — Proof / Resources / Compliance / Content  
Status: PS7 — IMPLEMENTED / CI QA PASS — PS8 CLOUDFLARE REVIEW PENDING  
Canonical file: `case-studies.html`

## Purpose

Present a reusable library of fictional, clearly labelled B2B food-trading Demo cases that show how a commercial challenge can be organized into a practical next step. PG20 is a proof-pattern page, not a portfolio of real ORIGEX clients and not evidence of live commercial performance.

## Canonical Content Authority

Arabic Master:
- H1: `حالات توضيحية من تحدٍ تجاري إلى خطوة قابلة للتنفيذ.`
- Core intent: illustrate structured commercial problem solving without presenting fictional content as real client work.

English Adaptation:
- H1: `Illustrative cases from commercial challenge to actionable next step.`

## Frozen Main Features

Authority: `docs/SCOPE-FREEZE-V1-FINAL.md`.

1. Filters
2. Case-study cards
3. Industry / category tags
4. Result highlights
5. CTA

No testimonials, client logos, star ratings, revenue claims, percentage improvements, ROI figures, awards, live project evidence, CRM integration or CMS behavior are included in V1.

## Content / Data Contract

PG20 remains editorial HTML. `docs/DATA-SCHEMA-V1.md` defines canonical structured JSON only for products, suppliers and markets, so PG20 must not introduce a new `cases.json` domain without a formal architecture/schema change.

Six fictional Demo cases are embedded in each language page with stable case IDs and matching AR/EN meaning:
- `case-001` — Ambient Foods / Market Access
- `case-002` — Beverages / Distribution
- `case-003` — Dairy / Supplier Readiness
- `case-004` — Frozen / RFQ & Buying
- `case-005` — Confectionery / Distribution
- `case-006` — Ingredients / Product Information

Every card must visibly carry a Demo / illustrative label.

## Filter Contract

Approved filter values:
- `all`
- `market-access`
- `distribution`
- `supplier-readiness`
- `rfq-buying`

Runtime: `assets/js/origex-case-studies.js`.

Allowed behavior:
- filter cards by `data-case-focus`;
- update visible-result count;
- use `aria-pressed` on filter buttons;
- update `?focus=<value>` without reload;
- hydrate a valid query value on load;
- preserve a valid focus value on AR/EN language switching;
- show an accessible empty state if future editorial changes create a zero-result filter.

Prohibited:
- network requests;
- local/session storage;
- remote analytics dependency;
- fabricated sorting/ranking logic;
- client or performance data injection.

## Demo Cases

### Case 001 — Market Access / Ambient Foods
Challenge: product information exists but market/channel readiness is unclear.  
Action: organize pack, origin, category, channel and market-review inputs.  
Illustrative result highlight: a clearer market-review path and defined next-information requirements.

### Case 002 — Distribution / Beverages
Challenge: a beverage range needs a clearer channel route.  
Action: map practical retail, wholesale and foodservice contexts.  
Illustrative result highlight: a clearer channel shortlist for commercial discussion.

### Case 003 — Supplier Readiness / Dairy
Challenge: manufacturer information is fragmented before buyer review.  
Action: structure company, capability, products, packaging and Demo compliance references.  
Illustrative result highlight: a more reviewable supplier profile.

### Case 004 — RFQ & Buying / Frozen
Challenge: a buyer shortlist lacks enough information for a useful RFQ.  
Action: structure product, quantity, destination and target-timing inputs.  
Illustrative result highlight: a more complete RFQ starting point without generating price or availability claims.

### Case 005 — Distribution / Confectionery
Challenge: channel fit is unclear across wholesale and foodservice opportunities.  
Action: organize category, packaging and channel assumptions for review.  
Illustrative result highlight: clearer channel-fit questions before distributor discussion.

### Case 006 — Product Information / Ingredients
Challenge: technical and commercial product information is difficult to compare.  
Action: organize specification, pack, origin, MOQ and documentation references.  
Illustrative result highlight: a more consistent initial product-evaluation view.

## Commercial / Proof Boundaries

Visible disclosure must state:
- all cases are fictional Demo scenarios created for the template;
- they are not real client engagements;
- result highlights are qualitative workflow examples, not measured outcomes;
- no case implies guaranteed market entry, sales, distribution appointment, pricing, availability or regulatory approval;
- buyers must replace Demo cases with verified, permissioned evidence before production publication.

## Information Architecture

Breadcrumb → Hero / Proof Boundary → Filter Toolbar → Case Study Grid → Demo Evidence Note → Final CTA.

## Visual Direction

- Premium B2B editorial/proof page, not agency portfolio styling.
- Strong content hierarchy over decorative imagery.
- Cards use restrained category/focus tags, challenge statement, action summary and highlighted illustrative result.
- Grid: 1 column mobile, 2 columns tablet, 3 columns desktop where content remains readable.
- Filter toolbar horizontally scrolls inside its own bounded container on narrow screens without creating page overflow.
- Result highlight uses the existing accent/surface vocabulary; no success-green visual that could imply verified achievement.
- Reuse M1 tokens/components; page CSS is composition-only.

## Navigation / Footer Contract

- Standard Global Navigation V1.
- `Explore` is the current desktop top-level state.
- `Case Studies` is current in the canonical Mega Menu.
- The locked Global Navigation V1 mobile drawer intentionally does **not** include Case Studies; PG20 preserves the canonical flat mobile order without introducing a page-local navigation variant or current marker.
- Language switch preserves a valid `focus` query parameter.
- Footer consumes N04 Global Footer V1 exactly; no local footer variant.

## SEO / Page Identity Contract

SEO ID: PG20.  
Indexability: INDEX candidate.

### Arabic
- File: `ar/case-studies.html`
- Title: `دراسات حالة تجارة غذائية B2B | ORIGEX`
- Meta Description: `حالات تجريبية توضح كيف يمكن تنظيم تحديات الوصول للسوق والتوزيع وتأهيل المورد وطلبات الشراء إلى خطوات تجارية أوضح.`
- H1: `حالات توضيحية من تحدٍ تجاري إلى خطوة قابلة للتنفيذ.`
- Canonical: `https://example.com/ar/case-studies.html`
- Breadcrumb: `الرئيسية / دراسات الحالة`

### English
- File: `en/case-studies.html`
- Title: `B2B Food Trading Case Studies | ORIGEX`
- Meta Description: `Illustrative B2B food-trading cases showing how market access, distribution, supplier-readiness and buying challenges can be organized into clearer next steps.`
- H1: `Illustrative cases from commercial challenge to actionable next step.`
- Canonical: `https://example.com/en/case-studies.html`
- Breadcrumb: `Home / Case Studies`

Required: self canonical, AR/EN/x-default hreflang, Open Graph baseline, WebPage + BreadcrumbList JSON-LD. No Review, Rating, Offer or performance-result structured claims.

## Accessibility / Responsive

- one semantic H1;
- filter buttons are keyboard accessible and expose `aria-pressed`;
- result count uses `aria-live=polite`;
- hidden cards use the `hidden` attribute;
- case-detail actions have descriptive labels;
- all interactive controls meet the global touch-target baseline;
- no horizontal overflow at 390 / 820 / 1366 / 1536;
- Arabic RTL and English LTR verified independently;
- reduced-motion inherited globally.

## Final PS7 Evidence — 2026-08-20

- Source/runtime report: `qa/pg20-case-studies/source-report.json` — failures 0.
- Rendered/interaction report: `qa/pg20-case-studies/rendered-report.json` — failures 0; AR/EN × 390/820/1366/1536 = 8/8 PASS.
- Filter query hydration, language preservation, keyboard reset and empty-state behavior PASS in both languages.
- Global Footer V1 PASS and F05 Icon Integrity PASS across the active AR/EN page set.
- Initial rendered run found horizontal overflow only at 390px in AR/EN. The filter row was constrained with logical-size-safe flex/grid rules and a bounded horizontal-scroll filter group in commit `020097b889ec04df899e414647fcf3d89181d7d4`; final QA evidence commit `d559056fe2b6b6bd88b7d0debf371f19525e0d80` passed.

## Exit Gate

PS7 PASSED. PS8 remains gated by deployed Cloudflare browser acceptance.

Copyright © ORVEAX.
