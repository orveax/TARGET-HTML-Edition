# ORIGEX — PG07 Capabilities / Services | Page Design Profile V1

Product ID: ORX-P01  
Page ID: PG07  
Milestone: M3 — Company / Business / Market  
Status: C6 / FROZEN FOR BUILD  
Canonical File: `capabilities.html`

## 1. Purpose

Present the approved ORIGEX V1 capability families as practical B2B food-trading support areas. The page must explain what can be organized or supported around products, suppliers, markets, channels and commercial enquiries without turning the template into a generic consultancy/agency page or promising commercial outcomes.

## 2. Authority

- Frozen V1 scope: `docs/SCOPE-FREEZE-V1-FINAL.md` — PG07.
- Content baseline: `docs/MASTER-CONTENT-ARCHITECTURE-V1.md` — PG07.
- SEO/page identity: `docs/SEO-METADATA-PAGE-NAMING-V1.md`.
- Shared UI foundation: closed M1 components + M2/M3 composition vocabulary.
- Historical TARGET capability page is reference-only and does not define PG07 content; V1 scope/content authorities govern.

## 3. Frozen Main Features / Section Contract

### CAP01 — Hero
- Eyebrow: القدرات والخدمات / Capabilities & Services.
- H1: commercial capabilities from evaluation to market.
- Lead: product data, supplier qualification, market access, distribution channels and commercial enquiries.
- Primary CTA: Explore Capabilities / استعرض القدرات.
- Secondary CTA: See How We Work / تعرف على طريقة العمل.
- No performance, coverage or regulatory claims.

### CAP02 — Capability Grid / Service Families
Five canonical service families:
1. Product & Supplier Assessment.
2. Market Access Support.
3. Distribution & Channel Support.
4. Commercial Documentation.
5. RFQ & Enquiry Structuring.

Each card states the commercial outcome it supports and links to an appropriate canonical route where available.

### CAP03 — Market-Entry Support
Explain the reusable market-entry support role through:
- market/context review;
- product/channel fit;
- route-to-market definition;
- documented next step.

No claim of guaranteed market entry, listing, regulatory approval or sales.

### CAP04 — Product / Supplier Support
Explain support around:
- product information completeness;
- supplier/company context;
- packaging/origin/MOQ/documents where relevant;
- readiness for a structured commercial review.

### CAP05 — Channel / Distribution Support
Explain support around:
- channel type;
- territory/market context;
- product/channel fit;
- RFQ or distribution discussion route.

No invented warehouse, fleet, customer or coverage claims.

### CAP06 — CTA
Three routes:
- Supplier: Submit Your Product.
- Buyer: Request a Quote.
- General: Contact.

Mandatory demo/fictional disclosure remains visible.

## 4. Content Contract

### Arabic H1
`قدرات تجارية تدعم المنتج من التقييم إلى السوق.`

### English H1
`Commercial capabilities supporting products from evaluation to market.`

### Tone
- B2B food trading terminology.
- Operational and commercially specific.
- No generic transformation/consulting language.
- No automatic acceptance, market-entry, distribution, exclusivity, agency, sales or regulatory promises.
- Arabic native RTL; English professionally adapted.

## 5. Design Direction

- Use M1 shell/components; add only a PG07 composition layer.
- Rhythm: hero → 5-service capability grid → market-entry focus → product/supplier focus → channel/distribution focus → conversion CTA.
- Service-family cards must remain scannable and equal-weight; focus sections provide deeper hierarchy without duplicating PG08 Service Details.
- Reuse ORVEAX-owned route/network media only where useful; no new stock dependency.
- No page-local JavaScript beyond shared `origex-ui.js`.

## 6. Responsive / RTL-LTR

- Capability grid: 1 column mobile, 2 tablet, 3/2 desktop composition.
- Focus sections alternate text/support panels but must mirror naturally in RTL using logical properties, not manual left/right hacks.
- No horizontal scrolling at 390 / 820 / 1366 / 1536.
- Touch targets follow M1 baseline.

## 7. Accessibility

- One H1.
- Sequential headings.
- Semantic sections/articles/lists.
- Core content visible without interaction.
- Icons are decorative where text carries meaning.
- M1 focus and reduced-motion rules remain active.

## 8. SEO / Page Identity Contract

SEO ID / Page ID: PG07  
Indexability: INDEX candidate  
Slug/File AR: `/ar/capabilities.html`  
Slug/File EN: `/en/capabilities.html`

Title AR: `قدرات وخدمات تجارة الأغذية B2B | ORIGEX`  
Title EN: `B2B Food Trading Capabilities & Services | ORIGEX`

Meta Description AR: `استعرض قدرات ORIGEX التجريبية حول تقييم المنتجات والموردين، الوصول للسوق، قنوات التوزيع، المستندات التجارية وطلبات RFQ.`  
Meta Description EN: `Explore the ORIGEX demo capability families for product and supplier assessment, market access, distribution channels, commercial documentation and RFQ structuring.`

H1 AR: `قدرات تجارية تدعم المنتج من التقييم إلى السوق.`  
H1 EN: `Commercial capabilities supporting products from evaluation to market.`

Canonical AR: `https://example.com/ar/capabilities.html`  
Canonical EN: `https://example.com/en/capabilities.html`

hreflang AR: AR URL  
hreflang EN: EN URL  
x-default: English URL in demo package

OG Title AR: `قدرات وخدمات تجارة الأغذية B2B | ORIGEX`  
OG Title EN: `B2B Food Trading Capabilities & Services | ORIGEX`  
OG Description AR: `خمس عائلات قدرات تجارية منظمة حول المنتج والمورد والسوق والقناة وطلب الشراء.`  
OG Description EN: `Five structured capability families around products, suppliers, markets, channels and commercial enquiries.`  
OG Image: `https://example.com/assets/media/demo/hero-distribution-network.svg`  
Schema: WebPage + BreadcrumbList  
Breadcrumb AR: الرئيسية → القدرات والخدمات  
Breadcrumb EN: Home → Capabilities & Services

Primary Internal Links:
- `how-we-work.html`
- `market-access.html`
- `submit-product.html`
- `rfq.html`
- `contact.html`
- `service-details.html`

## 9. Build / QA Exit

Before C8:
- AR + EN parity.
- Exactly five service-family cards.
- All six frozen sections present.
- Source/content/SEO/assets/icon references PASS.
- Responsive rendered QA at 390 / 820 / 1366 / 1536.
- Mega-menu/mobile-drawer/language switch PASS.
- No TARGET/client/CDN leakage.
- Cloudflare deployed-browser review at M3 staging acceptance.

Copyright © ORVEAX.
