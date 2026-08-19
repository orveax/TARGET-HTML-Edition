# ORIGEX — PG33 Company Profile — Page Design Profile V1

Product ID: ORX-P01  
Page ID: PG33  
Milestone: M3 — Company / Business / Market  
Status: **PS6 / FROZEN FOR BUILD**  
Change Authority: `CR-001-PG33-COMPANY-PROFILE-2026-08-19.md`

## Page Identity

- Arabic filename: `ar/company-profile.html`
- English filename: `en/company-profile.html`
- Page purpose: focused B2B company-profile experience that complements About with a document/resource-oriented trust layer.
- Primary audience: buyers, suppliers, manufacturers, distributors and commercial partners.
- Primary action: continue into the relevant commercial route.
- Secondary action: review company/profile information and resource integration point.

## Reference Fidelity

Validated reference pattern: `orveax/target/src/pages/company-profile.astro`.

Preserve:
- focused profile hero;
- quick company snapshot;
- routes to deeper site sections;
- document/resource presentation panel;
- document metadata/trust layer;
- final commercial CTA.

Do not transfer:
- TARGET identity;
- Qatar-specific claims;
- real client/company facts;
- verified PDF metadata;
- proprietary preview assets or documents;
- contact details or legal/business claims.

## Frozen Section Contract

### CP01 — Profile Hero
- eyebrow;
- one H1;
- concise B2B overview;
- actions to page content / About / Products;
- owned profile-cover visual;
- explicit demo disclosure.

### CP02 — At a Glance
Four reusable demo facts:
1. B2B Food Trading & Distribution
2. Manufacturers, Suppliers & Brands
3. Product / Supplier / Market workflows
4. Commercial route focus

### CP03 — Explore the Business
Four route cards:
1. About
2. How We Work
3. Products
4. Market Access

### CP04 — Profile Resource Pattern
- preview panel;
- profile-resource status;
- explanation of downloadable-PDF integration point;
- no fake downloadable PDF;
- buyer can replace/connect their approved company profile asset later.

### CP05 — Document / Trust Information
Four metadata items:
- resource type;
- language readiness;
- replacement status;
- version/demo status.

Must state that document metadata is illustrative until the buyer connects a verified file.

### CP06 — Final CTA
Primary: Products / RFQ route.  
Secondary: Contact / About route.

## Content Rules

- ORIGEX is a fictional trading demo identity.
- No agency, exclusivity, import, distribution, certification, coverage or performance claim may be presented as verified fact.
- No fake PDF size/page count presented as verified business metadata.
- Template integration language must remain clear where a document/resource slot is demonstrated.

## Visual Contract

- Uses M1 tokens, shell, cards, buttons, icon system and media frames.
- Page-specific CSS is composition only.
- Premium editorial/document feel; no brochure gimmicks.
- Strong document-preview hierarchy with restrained metadata and route cards.
- Arabic RTL and English LTR must remain first-class.

## Responsive Contract

- Mobile: single-column hero; preview follows copy; route cards stack; resource panel stacks.
- Tablet: two-column where space permits.
- Desktop: hero/resource split layouts with stable reading order.
- No horizontal overflow.

## Accessibility

- semantic headings;
- unique H1;
- meaningful image alt text;
- anchors for navigation;
- no fake download control;
- visible focus states inherited from shared system.

## SEO / Page Identity

### Arabic
- Title: `الملف التعريفي لشركة تجارة أغذية B2B | ORIGEX`
- Description: `استعرض الملف التعريفي الرقمي لنموذج ORIGEX لتجارة وتوزيع الأغذية B2B، مع نظرة على النشاط والمسارات التجارية والمنتجات والوصول إلى السوق.`
- H1: `ملف تعريفي رقمي يختصر الشركة، النشاط والمسارات التجارية في تجربة واحدة.`

### English
- Title: `B2B Food Trading Company Profile | ORIGEX`
- Description: `Explore the ORIGEX digital company-profile demo for B2B food trading and distribution, including business routes, products and market-access context.`
- H1: `A digital company profile that brings the business, its role and commercial routes into one focused experience.`

Indexability: ENVIRONMENT-DEPENDENT / demo policy applies.

## Asset Contract

New ORVEAX-owned distributable demo media:
- `assets/media/demo/company-profile-cover.svg`

No third-party photography or document asset required.

## Exit Gate

PS7 requires:
- AR + EN builds;
- canonical Global Navigation Contract;
- source/SEO/assets/icon QA;
- responsive rendered QA;
- route/link checks;
- no TARGET/client leakage;
- asset register update.

PS8 remains subject to Cloudflare deployed acceptance.

Copyright © ORVEAX.