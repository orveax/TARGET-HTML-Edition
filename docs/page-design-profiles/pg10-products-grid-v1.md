# ORIGEX — PG10 Products Grid | Page Design Profile V1

Product ID: ORX-P01  
Milestone: M4 — Product / Supplier / Conversion  
Status: C6 — FROZEN FOR BUILD  
Canonical file: `products.html`

## Purpose
Provide the primary B2B product-discovery surface for ORIGEX V1. The page must let buyers search and narrow a fictional demo catalogue by category, brand and origin, then continue to product details or a structured RFQ without presenting fake prices, ratings, stock or commercial rights.

## Frozen Main Features
1. Search
2. Category filter
3. Brand filter
4. Origin filter
5. Product cards
6. Pagination
7. RFQ CTA

No sort control, comparison, wishlist, cart, pricing, ratings or advanced filter drawer is added in V1.

## Canonical Data Contract
- Primary data: `assets/data/products.json`
- Brand/supplier lookup: `assets/data/suppliers.json`
- Product schema follows `docs/DATA-SCHEMA-V1.md` without breaking field names.
- Demo catalogue: 12 fictional/illustrative products across the six PG09 categories.
- Brand relationships use fictional demo suppliers only.
- Availability vocabulary stays within the frozen schema. PG10 demo products use `on-request` to avoid fake stock claims.

## Arabic Content Contract
- H1: `منتجات ببيانات تساعدك قبل إرسال الطلب.`
- Support: `ابحث وفلتر حسب الفئة، العلامة، وبلد المنشأ ثم افتح المنتج لمراجعة بياناته التجارية.`
- Search placeholder: `ابحث بالمنتج أو العلامة أو بلد المنشأ.`
- Empty state: `لا توجد منتجات مطابقة. عدّل الفلاتر أو أرسل طلبًا بفئتك المطلوبة.`
- Primary CTA: `أرسل طلب عرض سعر`
- Mandatory disclosure: all catalogue entities, origins, packaging, availability labels and commercial relationships are fictional/illustrative template data and must be replaced with verified buyer data before publication.

## English Content Contract
- H1: `Products presented with the information you need before enquiring.`
- Search placeholder: `Search by product, brand or origin.`
- Empty state: `No matching products. Adjust filters or submit an enquiry for the category you need.`
- Primary CTA: `Request a Quote`
- English preserves Arabic commercial meaning without stronger claims.

## Information Architecture
Hero / Breadcrumb → Search & Filter Controls → Results Summary → Product Grid → Pagination → Empty State → RFQ CTA.

## Product Card Contract
Each card uses the registered C02 Product Card and may show only:
- product image
- product name
- fictional demo brand
- category label
- illustrative origin
- pack size
- availability label mapped from the frozen controlled vocabulary
- View Product Details action
- Request Quote action

No fake price, discount, rating, review count, stock quantity or unsupported certification badge.

## Search / Filter Contract
- Search matches localized product name, localized brand name and localized origin label.
- Category uses the six stable IDs established by PG09: `ambient`, `beverages`, `dairy`, `frozen`, `confectionery`, `ingredients`.
- Brand uses stable `brandId` values from `suppliers.json`.
- Origin uses two-letter `originCode` values.
- Filters combine with AND logic.
- PG09 links such as `products.html?category=beverages` pre-apply the matching category.
- Clear/Reset restores all filters and page 1.
- Search/filter interaction is client-side Vanilla JS only.

## Pagination Contract
- 6 products per page in V1 demo.
- Pagination is generated from filtered result count.
- Changing any search/filter returns to page 1.
- Pagination uses semantic buttons/links with current-page state and accessible labels.

## Failure / Progressive Enhancement
If JSON loading fails, the page displays a visible data-load error and preserves navigation, filter labels, RFQ CTA and category route. No hidden failure or fabricated fallback data.

## Visual Direction
- Premium B2B catalogue, not consumer ecommerce.
- Desktop: filter rail / toolbar + three-column product grid where space permits.
- Tablet: two-column product grid.
- Mobile: one-column controls and cards.
- Reuse M1 tokens, C02 Product Card, C15 Pagination, C16 Search, P06/P07 form primitives and shared shell.
- Product media uses ORVEAX-owned demo SVG assets only.

## SEO / Page Identity Contract
SEO ID: PG10  
Indexability: INDEX candidate

### Arabic
- File: `ar/products.html`
- Title: `المنتجات الغذائية B2B | ORIGEX`
- Meta Description: `استعرض منتجات غذائية تجريبية منظمة حسب الفئة والعلامة والمنشأ مع بيانات تجارية تساعد على بدء طلب سعر منظم.`
- H1: `منتجات ببيانات تساعدك قبل إرسال الطلب.`
- Canonical: `https://example.com/ar/products.html`
- Breadcrumb: `المنتجات`

### English
- File: `en/products.html`
- Title: `B2B Food Products | ORIGEX`
- Meta Description: `Explore illustrative B2B food products by category, brand and origin with structured commercial information before starting an RFQ.`
- H1: `Products presented with the information you need before enquiring.`
- Canonical: `https://example.com/en/products.html`
- Breadcrumb: `Products`

Required: self canonical, AR/EN/x-default hreflang, Open Graph baseline, WebPage + BreadcrumbList JSON-LD. Product structured data belongs to PG11 detail pages, not this listing.

## Navigation Contract
PG10 is the primary Product-family listing. Shared Product IA exposes `Product Categories` + `All Products`; PG10 is current. PG11 Product Details inherits `All Products` as parent current state.

## Responsive / Accessibility
- no horizontal overflow at 390 / 820 / 1366 / 1536
- touch targets >= 44px on mobile/tablet
- single semantic H1
- visible breadcrumb
- all form controls have labels
- search has accessible name
- result count uses `aria-live="polite"`
- empty/error state is announced
- keyboard-only filtering and pagination must work
- RTL/LTR independently verified

## Exit Gate
C7 only after AR+EN build and data-schema/source/SEO/assets/icons/search/filter/query-param/pagination/navigation/responsive QA PASS. C8 remains gated by deployed Cloudflare browser acceptance.
