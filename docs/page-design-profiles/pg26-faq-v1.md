# ORIGEX — PG26 FAQ | Page Design Profile V1

Product ID: ORX-P01  
Milestone: M6 — Support / Utility / Components  
Status: **PS7 — IMPLEMENTED / CI QA PASS**  
Canonical file: `faq.html`

## Purpose
Provide a searchable, category-led FAQ surface for buyers, suppliers, products, RFQ, distribution and Demo/integration questions. The page must clarify how the ORIGEX template works without converting Demo content into business guarantees, live commercial facts or legal/regulatory advice.

## Canonical Content Authority
Arabic Master explicitly freezes these groups:
- Buyers
- Suppliers
- Products
- RFQ
- Distribution
- Demo & Integration

Arabic Master explicitly freezes:
- Q: `هل إرسال المنتج يعني قبوله؟`
- A: `لا. التقديم يتيح مراجعة المعلومات فقط، ولا يعني قبول المنتج أو تمثيله أو توزيعه.`
- Q: `هل الأسعار موجودة داخل القالب؟`
- A: `يمكن إضافتها حسب نموذج العمل، لكن Demo يركز على RFQ لأن الأسعار التجارية تعتمد غالبًا على الكمية والسوق والشروط.`

English Adaptation freezes the same Buyer / Supplier / Product / RFQ / Distribution / Demo & Integration grouping and requires consistent answers/disclosure.

Supporting FAQ copy for the remaining questions is a content refinement inside the approved FAQ feature and is derived only from existing frozen ORIGEX rules: PG10/11 product information, PG15 market disclaimer, PG17 submit-product boundaries, PG18 RFQ fields and Demo form state, PG19 partner qualification, PG22 resource states, PG23 certification/claim boundaries and global Demo/config behavior. It does not add new product facts.

## Frozen Main Features
Authority: `docs/SCOPE-FREEZE-V1-FINAL.md`.
1. Category navigation
2. Search
3. Accordion
4. Supplier / buyer groups
5. Contact CTA

## Content Model
V1 uses semantic page-local HTML; no `faq.json`, CMS or remote API is introduced.

Six groups × three questions = 18 Demo/support FAQ records:
- Buyers: RFQ information, price presentation, availability/confirmation boundary.
- Suppliers: submission acceptance boundary, required supplier/product information, representation/distribution boundary.
- Products: product facts shown by the template, certification/document status, product filtering behavior.
- RFQ: request inputs, Demo form integration boundary, attachment UI.
- Distribution: partnership qualification, distributor information, market/opportunity boundary.
- Demo & Integration: fictional Demo content, configurable contact values, production replacement/integration checklist.

## Search / Category Contract
Runtime: `assets/js/origex-faq.js`.

Query parameters:
- `?category=buyers|suppliers|products|rfq|distribution|demo`
- `?q=<search term>`

Rules:
- Missing category → `all`.
- Invalid category → normalize to `all`.
- Search is local, case-insensitive and checks question + answer + keywords.
- Search and category combine as AND filters.
- Result count uses an `aria-live="polite"` region.
- Zero results expose a visible empty state with a reset action.
- Category buttons expose `aria-pressed` and remain keyboard-native buttons.
- URL state may be updated with `history.replaceState`; no reload is required.
- AR/EN language switch preserves the normalized category and non-empty search query.
- Escape while focused in the search field clears the search term.
- No network request, storage or analytics.

## Accordion Contract
Use registered C14 markup and `assets/js/origex-ui.js` behavior.
- native `<button>` triggers;
- `aria-expanded` + `aria-controls`;
- controlled panel uses `role="region"` and `aria-labelledby`;
- Enter/Space activation is inherited from native button behavior;
- FAQ runtime must not duplicate accordion open/close logic.

## Demo / Claim Boundaries
- Product submission never implies acceptance, representation or distribution.
- Partner/distributor submission never guarantees partnership.
- Demo market content is illustrative and must be replaced/verified before production use.
- Demo certificates/documents are placeholders unless replaced with verified owned/authorized evidence.
- Demo contact values and business information are configurable examples.
- Demo forms require production integration before real submission handling.
- Price/availability/market opportunity are not represented as live guaranteed values.

## Information Architecture
Breadcrumb → FAQ Hero → Search + category navigation → grouped accordions → Demo/production boundary → Contact/RFQ CTA.

## Visual Direction
Premium support utility rather than a generic help center: compact hero, prominent search field, desktop sticky category rail, clearly separated group headings, calm accordion cards, high-contrast search/result state and a restrained final CTA. Mobile collapses to one column with wrapping category navigation and full-width accordion triggers.

## Navigation / Footer
- Standard Global Navigation V1.
- Explore = current.
- FAQ = current in Mega Menu and Mobile Drawer.
- Global Footer V1 exact.
- No page-local shell fork.

## SEO / Page Identity
### Arabic
- File: `ar/faq.html`
- Title: `الأسئلة الشائعة | المنتجات والموردون وطلبات RFQ | ORIGEX`
- Description: `أسئلة Demo منظمة حول المشترين والموردين والمنتجات وطلبات RFQ والتوزيع وتخصيص قالب ORIGEX لتجارة الأغذية B2B.`
- H1: `إجابات أوضح قبل أن تبدأ المحادثة التجارية.`
- Canonical: `https://example.com/ar/faq.html`

### English
- File: `en/faq.html`
- Title: `FAQ | Products, Suppliers & RFQ | ORIGEX`
- Description: `Structured Demo FAQs for buyers, suppliers, products, RFQ, distribution and ORIGEX template integration in B2B food trading.`
- H1: `Clearer answers before the commercial conversation starts.`
- Canonical: `https://example.com/en/faq.html`

Required:
- self canonical;
- AR / EN / x-default hreflang;
- Open Graph baseline;
- `WebPage` + `BreadcrumbList` JSON-LD.

No Product, Offer, Review, Rating, AggregateRating, certification or commercial-result schema is permitted on PG26.

## Accessibility / Responsive
- one H1;
- search has a visible label;
- category state is not color-only;
- accordion buttons retain visible focus and accessible expanded state;
- each panel is associated with its trigger;
- result count announced politely;
- reset action keyboard accessible;
- no horizontal viewport overflow at 390 / 820 / 1366 / 1536;
- AR RTL and EN LTR tested separately;
- minimum practical touch targets inherited from global foundation.

## QA Closure — 2026-08-20
Final authority: `docs/PG26-QA-REPORT-V1.md`.

- Source/content/SEO/runtime failures: **0**.
- Arabic FAQ records: **18 / 6 groups / PASS**.
- English FAQ records: **18 / 6 groups / PASS**.
- Canonical Arabic submission and pricing Q/A: PASS.
- AR/EN 390 / 820 / 1366 / 1536: **8/8 PASS**.
- Search + category filter + URL hydration + invalid-category normalization + reset + Escape clear: PASS.
- AR/EN desktop/mobile language-state preservation: PASS.
- C14 Enter/Space accordion interaction: PASS.
- Global Navigation V1 / Global Footer V1: PASS.
- Global F05 Icon Integrity: **54 AR/EN pages / 0 missing references**.
- Final QA evidence commit: `26a2a72870b3506f098a3dd95e38c56756575e10`.
- PS8 remains pending deployed Cloudflare browser acceptance.

## Exit Gate
**PS7 PASS / CLOSED FOR PAGE PRODUCTION.**

Next sequential production action: **PG27 — Contact**.

Copyright © ORVEAX.
