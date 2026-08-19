# PG05 — About | Page Design Profile V1

Product: ORIGEX — ORX-P01  
Milestone: M3 — Company / Business / Market  
Page: PG05 — About  
Content State: C6 / FROZEN FOR BUILD  
Languages: Arabic + English  
Direction: AR RTL / EN LTR

## Canonical Authority

- Structural source map: `docs/ABOUT-SOURCE-MAP.md`
- Reference composition: `orveax/target/src/components/AboutCanonical.astro`
- Generalization rule: preserve section purpose, hierarchy and content density; remove TARGET/client-specific identity, assets, facts and Qatar-only claims.
- Demo policy: `docs/DEMO-VS-PRODUCTION-POLICY-V1.md`
- Shared system: M1 closed components + M2 shared navigation/runtime.

## Page Intent

Present a credible fictional B2B food-trading company profile that explains who the business is, how it thinks about commercial fit, its role between source and market, and the boundaries of any commercial discussion.

The page must feel suitable for a real importer/distributor/manufacturer template while remaining reusable and free from client-specific claims.

## Content Contract — C6

### A01 — Hero
- Eyebrow: About ORIGEX / عن أوريجكس
- H1 AR: `تجارة غذائية B2B تربط المنتج والمورد ومسار السوق بوضوح.`
- H1 EN: `B2B food trading that connects products, suppliers and market routes with clarity.`
- Lead: explain that ORIGEX Trading Demo is a fictional commercial model for selected food categories and structured supplier/product opportunities.
- Primary resource action: Company Profile / Resources → `resources.html`
- Commercial media using ORVEAX-owned existing demo asset.
- Two factual/demo-safe highlights: Food Trading & Distribution; Manufacturers, Suppliers & Brands.

### A02 — Who We Are
- Explain selected food categories, supplier/manufacturer relationships, structured product information and suitable channel/market routes.
- State that the role is commercial and opportunity-based, not generic consulting.
- State that starting a discussion does not mean automatic product acceptance, import, representation or distribution commitment.
- Four fact items: B2B Food Trading; Selected Categories; Supplier & Brand Relationships; Market-Route Focus.

### A03 — Vision & Mission
- Vision: build trusted, structured commercial routes around suitable products and transparent information.
- Mission: review company/product/category/opportunity information, assess fit, then define the next commercial step on clear terms.
- Two full content cards.

### A04 — Commercial Role
- Explain ORIGEX as a commercial bridge between source and market.
- Three-node flow: Manufacturer / Brand / Supplier → ORIGEX → Market / Channel / Buyer.
- No claim that every submitted product will be accepted or represented.

### A05 — Commercial Clarity
Four trust cards:
1. Clear Information
2. No Automatic Commitment
3. Agree Before Execution
4. No Agency or Exclusivity Without Documentation

Include a visible commercial-boundary note.

### A06 — Final Conversion
- Resource panel: Company Profile / Resources.
- Opportunity panel: Explore Products + Submit Your Product.
- No unsupported performance, market-share, customer-count or certification claims.

## Demo Disclosure

AR: `جميع الأسماء والبيانات التجارية الواردة في العرض التوضيحي أمثلة خيالية لأغراض القالب، ويجب استبدالها ببيانات فعلية قبل النشر.`

EN: `All names and commercial data in this demo are fictional template examples and must be replaced with verified business information before publication.`

## SEO / Page Identity Contract

AR title: `عن شركة تجارة أغذية B2B | ORIGEX`  
EN title: `About a B2B Food Trading Company | ORIGEX`

AR canonical: `https://example.com/ar/about.html`  
EN canonical: `https://example.com/en/about.html`

Required:
- one H1 only
- canonical + AR/EN/x-default hreflang
- Open Graph baseline
- WebPage + BreadcrumbList JSON-LD
- semantic section headings
- local assets only
- no TARGET/client identifiers

## Component / System Mapping

- Global: N01–N04 shell/navigation
- Hero: S02 split hero + C01/C02/C05
- Who We Are: S01 + C08/C20 + media composition
- Vision/Mission: C11 card foundation
- Commercial Role: C11 cards + F07 composition
- Commercial Clarity: C11/C20 trust cards + note
- Final Conversion: S06 / CTA composition
- Runtime: `config.js`, `config-engine.js`, `origex-ui.js`
- Page composition CSS: `assets/css/origex-about.css`

## Responsive Contract

- Mobile: single-column content; flow nodes stack; arrows rotate/resolve with direction; CTAs full-width where needed.
- Tablet: two-column where readability permits.
- Laptop/Desktop: balanced editorial layouts; no oversized empty media fields.
- Arabic RTL and English LTR are first-class layouts.

## Exit Gate

C6 → Build AR+EN together → Source/SEO/asset QA → Rendered responsive QA → Interaction/navigation regression → Cloudflare deployed browser review → C8.
