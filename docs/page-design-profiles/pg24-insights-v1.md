# ORIGEX — PG24 Insights / Blog | Page Design Profile V1

Product ID: ORX-P01  
Milestone: M5 — Proof / Resources / Compliance / Content  
Status: PS6 — FROZEN FOR BUILD  
Canonical file: `insights.html`

## Purpose
Provide a practical B2B editorial hub for product, buyer, supplier, market and distribution topics without introducing a CMS or inventing live market intelligence.

## Canonical Content Authority
Arabic Master:
- H1: `رؤى عملية حول المنتج والسوق والتوزيع.`

English Adaptation:
- H1: `Practical insights on products, markets and distribution.`

## Frozen Main Features
Authority: `docs/SCOPE-FREEZE-V1-FINAL.md`.
1. Featured article
2. Category filters
3. Article grid
4. Search
5. Pagination

## Editorial / Demo Contract
- All V1 articles are fictional ORIGEX Demo editorial content.
- No live market-data, legal/regulatory advice, investment advice, price forecast, client claim or measured commercial result is presented.
- Editorial article records remain semantic HTML. No new `articles.json` domain is introduced in V1.
- PG24 ships 9 Demo article records: one featured article and eight grid articles.
- Canonical PG25 route is `article-details.html?id=<article-id>`; PG24 may link to it before PG25 implementation because it is the frozen next detail layout.
- Article dates are Demo publication metadata, not evidence of live intelligence.

## Categories
- `all`
- `buying`
- `product`
- `market`
- `distribution`
- `supplier`

## Runtime Contract
Runtime: `assets/js/origex-insights.js`.
Allowed:
- client-side text search over title/excerpt/keywords;
- category filtering;
- pagination at 6 grid articles per page;
- `?category=`, `?q=` and `?page=` hydration;
- valid state preservation across AR/EN language switch;
- keyboard-operable filters;
- accessible visible-count and zero-result state.

Prohibited:
- remote API/CMS fetch;
- local/session storage;
- analytics dependency;
- fabricated popularity/view counts;
- dynamic SEO mutation intended to emulate server rendering.

## Information Architecture
Breadcrumb → Hero → Featured Article → Search / Category Toolbar → Article Grid → Pagination → Editorial Boundary → CTA.

## Visual Direction
Premium B2B editorial journal: strong featured-story hierarchy, compact metadata, restrained category badges, high reading clarity, and no generic lifestyle-blog styling. Mobile is one-column; tablet/desktop increase density without shrinking touch targets.

## Navigation / Footer
- Standard Global Navigation V1.
- Explore current; Insights current in Mega Menu and Mobile Drawer.
- Global Footer V1 exact.
- Language switch preserves valid category/search/page state.

## SEO / Page Identity
### Arabic
- File: `ar/insights.html`
- Title: `رؤى التجارة والتوزيع | ORIGEX`
- Description: `مكتبة Demo عملية حول معلومات المنتج، جاهزية المورد، احتياجات المشتري، الوصول إلى السوق والتوزيع في سياق تجارة الأغذية B2B.`
- H1: `رؤى عملية حول المنتج والسوق والتوزيع.`
- Canonical: `https://example.com/ar/insights.html`

### English
- File: `en/insights.html`
- Title: `Trade & Distribution Insights | ORIGEX`
- Description: `A practical Demo editorial library covering product information, supplier readiness, buyer needs, market access and B2B food distribution.`
- H1: `Practical insights on products, markets and distribution.`
- Canonical: `https://example.com/en/insights.html`

Required: self canonical, AR/EN/x-default hreflang, Open Graph baseline, `CollectionPage` + `BreadcrumbList` JSON-LD only. No Article schema is emitted on the listing page.

## Accessibility / Responsive
- one H1;
- search has visible label or accessible label;
- filters use buttons + `aria-pressed`;
- result count is in `aria-live=polite` context;
- pagination uses semantic nav and buttons/links with current state;
- hidden cards use `hidden`;
- no horizontal overflow at 390/820/1366/1536;
- touch-target baseline applies;
- Arabic RTL / English LTR tested independently.

## Exit Gate
PS7 only after source/editorial-safety/runtime/navigation/footer/icon/client-leak QA + rendered AR/EN 390/820/1366/1536 + search/filter/pagination/query/language-preservation/empty-state interaction QA all PASS. PS8 remains gated by deployed Cloudflare browser acceptance.

## QA Rerun Note — 2026-08-20
Initial PG24 rendered and interaction QA passed, but the first source gate detected a canonical Global Footer V1 drift in `en/insights.html`. The shared footer normalizer was rerun centrally; this profile update intentionally retriggers PG24 QA against the normalized footer before any PS7 promotion.

Copyright © ORVEAX.