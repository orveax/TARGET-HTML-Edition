# ORIGEX — PG12 Suppliers / Brands Directory | Page Design Profile V1

Product ID: ORX-P01  
Milestone: M4 — Product / Supplier / Conversion  
Status: PS6 — FROZEN FOR BUILD  
Canonical file: `suppliers.html`

## Purpose
Provide the primary B2B supplier/brand discovery surface for ORIGEX V1. Buyers can search and narrow the fictional demo supplier dataset by category and origin, review compact supplier profiles and linked product counts, then continue to supplier details, products or a commercial enquiry without implying verified status, representation rights or live commercial relationships.

## Frozen Main Features
1. Search
2. Category filter
3. Origin filter
4. Supplier / brand cards
5. Featured suppliers
6. Commercial CTA

No ratings, reviews, marketplace verification badges, price lists, live availability, territory rights or advanced supplier comparison in V1.

## Canonical Data Contract
- Primary supplier data: `assets/data/suppliers.json`
- Product relation lookup: `assets/data/products.json`
- Supplier schema follows `docs/DATA-SCHEMA-V1.md` without breaking field names.
- V1 demo dataset contains 4 fictional suppliers with stable `productIds`, `categoryIds`, `countryCode`, `featured` and optional demo certification references.
- `logo: ""` renders a neutral text/initials identity frame; the page does not fabricate logos.
- `website: "#"` is not rendered as a live website action.

## Arabic Content Contract
- H1: `موردون وعلامات حسب الفئة والمنشأ.`
- Support: `استعرض ملفات الموردين والمنتجات المرتبطة بهم قبل بدء التواصل التجاري.`
- Search placeholder: `ابحث باسم المورد أو العلامة.`
- Featured title: `موردون مميزون في بيانات الديمو.`
- Directory title: `ابحث في دليل الموردين والعلامات.`
- Empty state: `لا توجد ملفات موردين مطابقة. عدّل الفلاتر أو قدّم منتجك للمراجعة.`
- Primary commercial CTA: `قدّم منتجك`
- Secondary CTA: `تواصل معنا`
- Mandatory disclosure: all suppliers, brands, origins, category coverage, product relations and certification references are fictional/illustrative template content and must be replaced with verified business data before publication.

## English Content Contract
- H1: `Suppliers and brands organized by category and origin.`
- Support: `Explore supplier profiles and their linked products before starting a commercial conversation.`
- Search placeholder: `Search by supplier or brand name.`
- Featured title: `Featured suppliers in the demo dataset.`
- Directory title: `Search the supplier and brand directory.`
- Empty state: `No matching supplier profiles. Adjust the filters or submit your product for review.`
- Primary commercial CTA: `Submit Your Product`
- Secondary CTA: `Contact Us`
- English preserves the Arabic commercial meaning without stronger claims.

## Information Architecture
Hero / Breadcrumb → Featured Suppliers → Search & Filters → Supplier Directory → Demo Disclosure → Commercial CTA.

## Featured Suppliers Contract
- Uses records where `featured === true`.
- Current demo contains four featured fictional suppliers; show all four in a compact featured strip/grid.
- Featured state is editorial demo metadata only, not a quality, certification or commercial endorsement claim.

## Supplier Card Contract
Each supplier card may show only:
- neutral identity initials / supplied logo when a real buyer replaces the demo data
- localized supplier/brand name
- localized summary
- illustrative origin
- category tags from `categoryIds`
- linked product count from `productIds`
- optional Demo certification-reference count (never a verified badge)
- View Supplier Details action → `supplier-details.html?id=<supplier-id>`
- View Products action → `products.html?brand=<brand-id>` using the existing PG10 brand relation

No fake ratings, verification, response rate, years in business, order value, territory rights or representation claims.

## Search / Filter Contract
- Search matches localized supplier/brand name and localized summary.
- Category uses the stable PG09 IDs: `ambient`, `beverages`, `dairy`, `frozen`, `confectionery`, `ingredients`.
- Origin uses supplier `countryCode`.
- Search + category + origin combine with AND logic.
- Reset restores all filters.
- URL query parameters are synchronized for `q`, `category`, `origin`.
- Filtering is Vanilla JS progressive enhancement over the canonical JSON dataset.

## Failure / Progressive Enhancement
If supplier/product JSON loading fails, preserve the shell, page copy and commercial CTA and show a visible data-load error. Never silently fabricate fallback supplier records.

## Visual Direction
- Premium B2B partner directory, not a consumer marketplace.
- Featured supplier strip creates hierarchy without decorative excess.
- Desktop supplier directory: two-column cards for readable B2B profiles.
- Tablet: two columns where practical; mobile: one column.
- Reuse M1 tokens, C03 Supplier Card, form/search primitives and the locked Global Navigation V1.
- RTL/LTR mirroring is systematic.

## SEO / Page Identity Contract
SEO ID: PG12  
Indexability: INDEX candidate

### Arabic
- File: `ar/suppliers.html`
- Title: `الموردون والعلامات التجارية | ORIGEX`
- Meta Description: `استعرض ملفات موردين وعلامات تجارية تجريبية حسب الفئة والمنشأ مع المنتجات المرتبطة ومسارات التواصل التجاري.`
- H1: `موردون وعلامات حسب الفئة والمنشأ.`
- Canonical: `https://example.com/ar/suppliers.html`
- Breadcrumb: `الموردون`

### English
- File: `en/suppliers.html`
- Title: `Suppliers & Brands Directory | ORIGEX`
- Meta Description: `Explore illustrative supplier and brand profiles by category and origin, review linked products and continue to the appropriate commercial route.`
- H1: `Suppliers and brands organized by category and origin.`
- Canonical: `https://example.com/en/suppliers.html`
- Breadcrumb: `Suppliers`

Required: self canonical, AR/EN/x-default hreflang, Open Graph baseline, WebPage + BreadcrumbList JSON-LD. Supplier/Organization detail structured data belongs to PG13, not the directory.

## Navigation Contract
PG12 is the primary Supplier-family directory and is the `Suppliers` top-level current state. Shared mega/mobile navigation remains identical to the locked Global Navigation V1; only current-state attributes vary. PG13 Supplier Details inherits Suppliers as parent current state.

## Responsive / Accessibility
- no horizontal overflow at 390 / 820 / 1366 / 1536
- touch targets >= 24px QA floor and 44px for primary interactive controls on mobile/tablet
- single semantic H1
- visible breadcrumb
- search/select controls have labels
- results count uses `aria-live="polite"`
- featured status is text, not conveyed by color alone
- keyboard-only search/filter/reset/card actions work
- RTL/LTR independently verified

## Exit Gate
PS7 only after AR+EN build and data-schema/source/SEO/assets/icons/search/filter/query-param/featured/card-route/navigation/responsive QA PASS. PS8 remains gated by deployed Cloudflare browser acceptance.
