# ORIGEX — PG09 Product Categories | Page Design Profile V1

Product ID: ORX-P01  
Milestone: M4 — Product / Supplier / Conversion  
Status: C6 — FROZEN FOR BUILD  
Canonical file: `product-categories.html`

## Purpose
Provide a category-first B2B browsing entry point before the denser PG10 product grid. The page must help buyers and trade users understand the commercial product families without inventing live stock, pricing, buyer relationships or performance claims.

## Frozen Main Features
1. Product-category hero
2. Category filters
3. Six-category grid
4. Category cards
5. Category facts
6. Final CTA

No search, brand filter, origin filter, pagination or product-level filtering in PG09; those belong to PG10.

## Canonical Categories
- Ambient Foods
- Beverages
- Dairy
- Frozen
- Confectionery
- Ingredients

## Arabic Content Contract
- H1: `استعرض المنتجات حسب الفئة التجارية.`
- Support: `انتقل مباشرة إلى الفئة المناسبة ثم راجع المنتجات حسب المنشأ، العلامة، التعبئة، والتوفر.`
- Primary CTA: `استعرض كل المنتجات`
- Mandatory disclosure: all categories, counts, availability references and commercial examples are demo/illustrative template content and must be replaced with verified buyer data before publication.

## English Content Contract
- H1: `Explore products by commercial category.`
- Support preserves Arabic meaning without stronger claims.
- Primary CTA: `Explore All Products`
- Same mandatory demo disclosure.

## Information Architecture
Hero → Category Overview / Facts → Filter Chips → Category Cards → Buyer Guidance → CTA.

## Category Card Contract
Each card contains only:
- category name
- short commercial positioning line
- 2–3 illustrative fact labels
- route to `products.html` using a category query/hash placeholder
No fabricated SKU counts, live availability, ratings, sales data or market share.

## Visual Direction
- Reuse M1 tokens, shell, icons and buttons.
- Premium B2B directory feel; not grocery/ecommerce styling.
- Category identity through iconography, restrained tone and facts rather than decorative product photography.
- Mobile-first one-column → tablet two-column → desktop three-column category grid.
- Arabic RTL and English LTR treated independently.

## SEO / Page Identity
### Arabic
- Title: `فئات المنتجات الغذائية B2B | ORIGEX`
- Canonical: `https://example.com/ar/product-categories.html`

### English
- Title: `B2B Food Product Categories | ORIGEX`
- Canonical: `https://example.com/en/product-categories.html`

Required: canonical, AR/EN/x-default hreflang, Open Graph baseline, WebPage + BreadcrumbList JSON-LD.

## Interaction Contract
Category filter chips use the existing C17 filter behavior plus a minimal PG09 vanilla-JS adapter to show/hide category cards by family. `All` resets the six-card grid. No external data/API.

## Navigation Contract
PG09 is part of the Product family. Desktop mega menu must expose Product Categories + All Products and mark Product Categories current. Mobile drawer must expose both routes and mark PG09 current.

## Responsive / Accessibility
- no horizontal overflow at 390 / 820 / 1366 / 1536
- minimum touch target baseline 44px on mobile/tablet
- semantic single H1
- visible breadcrumb
- keyboard-operable filter buttons
- aria-pressed state from shared filter primitive
- reduced-motion safe; no required animation

## Exit Gate
C7 only after AR+EN build and source/SEO/assets/icons/filter/navigation/responsive QA PASS. C8 remains gated by deployed Cloudflare browser acceptance.
