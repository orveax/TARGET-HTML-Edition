# ORIGEX — PG06 How We Work | Page Design Profile V1

Product ID: ORX-P01  
Page ID: PG06  
Milestone: M3 — Company / Business / Market  
Status: C6 / FROZEN FOR BUILD  
Canonical File: `how-we-work.html`

## 1. Purpose

Explain the reusable B2B commercial qualification and execution route from initial product/company information to a documented next step. The page must clarify what ORIGEX demo does, what the supplier/brand provides, how fit is reviewed, and that discussion does not create automatic import, distribution, agency, exclusivity or market-success commitments.

## 2. Authority & Fidelity

- Frozen V1 scope: `docs/SCOPE-FREEZE-V1-FINAL.md` — PG06.
- Source experience reference: `orveax/target/src/components/HowWeWorkCanonical.astro`.
- Source fidelity authority: `docs/PAGE-FIDELITY-MATRIX.md`.
- SEO/page identity authority: `docs/SEO-METADATA-PAGE-NAMING-V1.md`.

The historical TARGET source contains six operational steps. ORIGEX V1 is explicitly frozen to a four-step process, so the source logic is consolidated into four commercial stages rather than copied 1:1.

## 3. Frozen Main Features / Section Contract

### HWW01 — Hero
- Eyebrow: How We Work / كيف نعمل.
- Commercial H1 focused on information → qualification → decision → next step.
- Lead explains case-by-case review and no automatic commitment.
- Primary CTA: Submit Your Product / قدم منتجك.
- Secondary CTA: Explore Products / استعرض المنتجات.
- Route visual: Information → Review → Decision → Next Step.

### HWW02 — Qualification Logic
Four qualification dimensions:
1. Company / brand context.
2. Product & technical information.
3. Market / channel fit.
4. Commercial readiness.

Each dimension explains what is reviewed without promising acceptance.

### HWW03 — Four-Step Process
1. Share the opportunity.
2. Review the fit.
3. Agree roles and commercial route.
4. Move to the documented next step and review continuity.

This is the only canonical PG06 process count in V1.

### HWW04 — Roles & Responsibilities
Three responsibility columns:
- Supplier / Brand.
- ORIGEX Trading Demo.
- Buyer / Market Channel.

The section must separate responsibilities and avoid implying ORIGEX controls regulatory approval, buyer demand or commercial results.

### HWW05 — Required Information
Required-information checklist:
- Company / brand.
- Product / category.
- Origin, pack, storage and shelf-life data where relevant.
- MOQ / commercial terms where available.
- Certificates / documents where available.
- Proposed market or channel opportunity.
- Product materials / files.

### HWW06 — Decision Flow
Three possible review outcomes:
- Proceed to commercial discussion.
- Clarify / request more information.
- Not a fit at this stage.

No rejection reason or acceptance state may be presented as automated.

### HWW07 — Next-Step CTA
- Supplier route: Submit Your Product.
- Buyer route: Request a Quote.
- General route: Contact.

Mandatory fictional/demo disclosure remains visible.

## 4. Content Contract

### Arabic H1
`من المعلومة إلى القرار، ثم إلى خطوة تجارية مناسبة.`

### English H1
`From information to a decision, then to the right commercial next step.`

### Tone
- B2B food trading terminology.
- Clear, operational and non-consulting.
- No promises of import, distribution, exclusivity, regulatory approval, sales volume, coverage or growth.
- Arabic is native RTL copy; English is a professional adaptation, not literal translation.

## 5. Design Direction

- Use the closed M1 shell/components and M2 shared composition vocabulary.
- Page rhythm: decisive hero → qualification grid → numbered process → responsibility matrix → information checklist → decision states → final CTA.
- Visual hierarchy should favor process clarity over decoration.
- Reuse ORVEAX-owned route/network media and patterns where useful; no new stock dependency is required.
- No page-local JavaScript required beyond shared `origex-ui.js`.

## 6. Responsive / RTL-LTR Rules

- Four-step process stacks 1-column mobile, 2-column tablet, 4-column desktop where space permits.
- Responsibility matrix stacks on mobile and must remain readable without horizontal scrolling.
- Decision states must not depend on color alone.
- Direction-sensitive arrows use existing icon/runtime direction rules.
- Minimum touch targets follow M1 foundation.

## 7. Accessibility

- One H1 only.
- Sequential heading order.
- Semantic sections/articles/lists.
- Decorative route media hidden from assistive technology when it carries no unique content.
- Visible focus states from M1.
- No interaction is required to access core content.

## 8. SEO / Page Identity Contract

SEO ID / Page ID: PG06  
Indexability: INDEX candidate  
Slug/File AR: `/ar/how-we-work.html`  
Slug/File EN: `/en/how-we-work.html`

Title AR: `كيف نعمل في تجارة الأغذية B2B | ORIGEX`  
Title EN: `How We Work in B2B Food Trading | ORIGEX`

Meta Description AR: `تعرّف على مسار ORIGEX التجريبي لتأهيل فرص المنتجات الغذائية، مراجعة الملاءمة، تحديد الأدوار والوصول إلى خطوة تجارية واضحة.`  
Meta Description EN: `See the ORIGEX demo process for qualifying food-product opportunities, reviewing fit, defining responsibilities and reaching a clear commercial next step.`

H1 AR: `من المعلومة إلى القرار، ثم إلى خطوة تجارية مناسبة.`  
H1 EN: `From information to a decision, then to the right commercial next step.`

Canonical AR: `https://example.com/ar/how-we-work.html`  
Canonical EN: `https://example.com/en/how-we-work.html`

hreflang AR: AR URL  
hreflang EN: EN URL  
x-default: English URL in demo package

OG Image: `https://example.com/assets/media/demo/hero-distribution-network.svg`  
Schema: WebPage + BreadcrumbList  
Breadcrumb AR: الرئيسية → كيف نعمل  
Breadcrumb EN: Home → How We Work

Primary Internal Links:
- `submit-product.html`
- `products.html`
- `rfq.html`
- `contact.html`

## 9. Build / QA Exit

Before C8:
- AR + EN parity.
- Source/content/SEO/assets PASS.
- Responsive rendered QA at 390 / 820 / 1366 / 1536.
- Navigation and language-switch interaction PASS.
- No horizontal overflow.
- No TARGET/client/CDN leakage.
- Cloudflare deployed-browser review when the M3 batch reaches staging acceptance.

Copyright © ORVEAX.
