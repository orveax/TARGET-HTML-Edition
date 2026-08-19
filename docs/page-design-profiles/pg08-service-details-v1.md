# ORIGEX — PG08 Service Details | Page Design Profile V1

Product ID: ORX-P01  
Page ID: PG08  
Milestone: M3 — Company / Business / Market  
Status: C6 / FROZEN FOR BUILD  
Canonical File: `service-details.html`

## 1. Purpose

Explain one concrete B2B food-trading support service in enough detail for a qualified manufacturer or supplier to understand the review scope, process, outputs and fit before starting an enquiry. PG08 is a service-detail layout, not a generic agency-services page.

Demo service: **Product Market-Readiness Review / مراجعة جاهزية المنتج للسوق**.

## 2. Authority

- Frozen V1 scope: `docs/SCOPE-FREEZE-V1-FINAL.md` — PG08.
- Content baseline: `docs/MASTER-CONTENT-ARCHITECTURE-V1.md` — PG08.
- SEO/page identity: `docs/SEO-METADATA-PAGE-NAMING-V1.md`.
- Parent capability page: PG07 — `capabilities.html`.

No V1.1 deferred service feature is enabled in this page.

## 3. Frozen Main Features / Section Contract

### SD01 — Service Hero
- Eyebrow identifies the capability family: Product & Supplier Assessment.
- H1 names the demo service.
- Intro states that the review checks whether core product information is sufficient for an initial commercial evaluation.
- Primary CTA: Start Product Review / ابدأ مراجعة المنتج.
- Secondary CTA: Back to Capabilities / العودة إلى القدرات.
- Visible demo/service-boundary note.

### SD02 — Overview
Explain the commercial purpose of the review:
- organize product facts before the commercial discussion;
- identify information gaps;
- distinguish information readiness from market acceptance;
- prepare a clearer next step.

### SD03 — Scope
Review areas:
- product/category identity;
- origin/manufacturer context;
- pack/packaging details;
- storage and shelf-life information where relevant;
- MOQ/commercial information where available;
- available specifications/documents;
- proposed market/channel context.

Explicitly out of scope:
- legal or regulatory approval;
- laboratory testing;
- guaranteed listing, distribution or sales;
- contractual due diligence.

### SD04 — Process
Four stages:
1. Share the product information.
2. Review completeness and commercial context.
3. Identify gaps and initial readiness.
4. Define the appropriate next step.

### SD05 — Deliverables
Demo output structure:
- readiness snapshot;
- information-gap checklist;
- commercial clarification points;
- next-step recommendation.

Outputs are demo/template examples and are not certificates, approvals or professional legal/regulatory opinions.

### SD06 — Fit / Not Fit Guidance
**Fit:** manufacturers or suppliers with a defined product plus core origin, pack and commercial information.

**Not Fit:** concepts with no defined product specification, origin, packaging or meaningful commercial data yet.

### SD07 — Related Services
Link to:
- Market Access Support — `market-access.html`.
- Distribution & Channel Support — `home-02.html`.
- RFQ & Enquiry Structuring — `rfq.html`.
- Parent Capabilities — `capabilities.html`.

### SD08 — Final CTA
Supplier/manufacturer route: `submit-product.html`.
General clarification route: `contact.html`.
Mandatory fictional/demo disclosure remains visible.

## 4. Content Contract

### Arabic
H1: `مراجعة جاهزية المنتج للسوق.`  
Intro: `خدمة منظمة لمراجعة المعلومات الأساسية للمنتج وتحديد ما إذا كانت البيانات الحالية كافية لبدء تقييم تجاري أولي.`

### English
H1: `Product Market-Readiness Review.`  
Intro: `A structured review of core product information to determine whether the current data is sufficient for an initial commercial evaluation.`

### Tone
- operational B2B food-trading language;
- concise and commercially useful;
- no consultancy-style transformation claims;
- no promise of regulatory approval, listing, distribution, demand, sales or exclusivity;
- Arabic is native RTL; English is a professional adaptation.

## 5. Design Direction

- Use the closed shared shell and component system.
- Detail-page rhythm: hero → overview → scope matrix → four-step process → outputs → fit guidance → related services → conversion.
- Use information architecture and contrast rather than decorative complexity.
- Reuse existing ORVEAX-owned route/product media only; no new stock asset is required.
- No page-local JavaScript is required.

## 6. Responsive / RTL-LTR Rules

- Hero: two-column desktop, single-column mobile.
- Scope: two-column Included / Out of Scope matrix; stack mobile.
- Four-step process: 4/2/1 responsive progression.
- Deliverables: 2×2 desktop/tablet where space permits; single-column mobile.
- Fit/Not Fit: two columns desktop; stack mobile.
- No horizontal scrolling.

## 7. Accessibility

- one H1 only;
- semantic heading order;
- scope and deliverables readable without icons/color;
- icons decorative where text already conveys meaning;
- visible shared focus state;
- no interaction required to access core content.

## 8. SEO / Page Identity Contract

SEO ID / Page ID: PG08  
Indexability: INDEX candidate  
Slug/File AR: `/ar/service-details.html`  
Slug/File EN: `/en/service-details.html`

Title AR: `مراجعة جاهزية المنتج للسوق — خدمة تجارية | ORIGEX`  
Title EN: `Product Market-Readiness Review — B2B Service | ORIGEX`

Meta Description AR: `صفحة خدمة تجريبية توضح نطاق مراجعة جاهزية المنتج للسوق، خطوات المراجعة، المخرجات ومعايير الملاءمة قبل التقييم التجاري الأولي.`  
Meta Description EN: `A demo service page explaining the scope, process, outputs and fit criteria of a product market-readiness review before initial commercial evaluation.`

H1 AR: `مراجعة جاهزية المنتج للسوق.`  
H1 EN: `Product Market-Readiness Review.`

Canonical AR: `https://example.com/ar/service-details.html`  
Canonical EN: `https://example.com/en/service-details.html`

hreflang AR: AR URL  
hreflang EN: EN URL  
x-default: English URL in demo package

OG Image: `https://example.com/assets/media/demo/hero-trade-scene.svg`  
Schema: WebPage + BreadcrumbList  
Breadcrumb AR: الرئيسية → القدرات والخدمات → مراجعة جاهزية المنتج للسوق  
Breadcrumb EN: Home → Capabilities & Services → Product Market-Readiness Review

Primary Internal Links:
- `capabilities.html`
- `submit-product.html`
- `market-access.html`
- `home-02.html`
- `rfq.html`
- `contact.html`

## 9. Build / QA Exit

Before C8:
- AR + EN parity;
- all eight frozen sections present;
- Source/content/SEO/assets/icons PASS;
- responsive rendered QA at 390 / 820 / 1366 / 1536;
- parent navigation, language switch and mobile drawer PASS;
- no horizontal overflow;
- no TARGET/client/CDN leakage;
- Cloudflare deployed-browser review in the M3 batch before final C8 promotion.

Copyright © ORVEAX.
