# ORIGEX — PG13 Supplier / Brand Details | Page Design Profile V1

Product ID: ORX-P01  
Milestone: M4 — Product / Supplier / Conversion  
Status: PS6 — FROZEN FOR BUILD  
Canonical file: `supplier-details.html`

## Purpose
Provide a reusable B2B supplier-detail dossier that resolves one fictional supplier record into a structured commercial profile. The page must show origin, category coverage, linked products, illustrative certification references, demo target markets and relationship facts without implying verification, agency, exclusivity, live representation or territory rights.

## Frozen Main Features
1. Supplier / brand identity
2. Origin
3. Category coverage
4. Linked products
5. Demo certification references
6. Demo target markets
7. Relationship facts
8. Commercial CTA

No ratings, reviews, verification badges, years-in-business claims, revenue, capacity numbers, response rates, exclusivity, territory ownership or live commercial status in V1.

## Canonical Data Contract
- Suppliers: `assets/data/suppliers.json`
- Products: `assets/data/products.json`
- Markets: `assets/data/markets.json`
- Schema authority: `docs/DATA-SCHEMA-V1.md`
- Default demonstration supplier: `supplier-noura` — Noura Foods Demo.
- `?id=<supplier-id>` switches the active supplier using the same layout.
- Invalid/missing IDs visibly fall back to `supplier-noura`; no supplier object is fabricated in JavaScript.
- Products resolve through supplier `productIds` / product `supplierId` relations.
- Markets resolve through supplier `marketIds` / market IDs.
- Certification IDs are rendered strictly as Demo references.
- `logo: ""` renders a neutral initials identity block; the template never fabricates a company logo.
- `website: "#"` remains a disabled/demo placeholder and is not exposed as a live website claim.

## Data Contract Improvement — PG13 Gate
`docs/DATA-SCHEMA-V1.md` already declares `assets/data/markets.json` as a canonical data domain, but the file was absent before PG13. PG13 closes this implementation gap by adding the six illustrative GCC market records already named in the canonical PG15 content and connecting suppliers through existing `marketIds`. This is a backward-compatible data completion, not an architecture change.

## Arabic Content Contract
- Breadcrumb: `الموردون / ملف المورد`
- Eyebrow: `ملف المورد — Demo`
- H1: `اعرف المورد ومنتجاته والأسواق المستهدفة قبل بدء التواصل التجاري.`
- Demo Supplier: `نورا فودز — Demo`
- Intro: `مصنع تجريبي ضمن محتوى القالب لعرض طريقة تقديم بيانات المورد، الفئات، المنتجات، والأسواق المستهدفة. الاسم والبيانات توضيحية وليست لشركة حقيقية.`
- Linked Products title: `منتجات مرتبطة من نفس بيانات الديمو.`
- Markets title: `أسواق مستهدفة توضيحية، وليست حقوق توزيع.`
- Primary CTA: `ابدأ طلبًا تجاريًا`
- Secondary CTA: `العودة إلى الموردين`
- Mandatory disclosure: supplier identity, origin, categories, product relations, certification references and market relations are fictional/illustrative and must be replaced with verified business data before publication.

## English Content Contract
- Breadcrumb: `Suppliers / Supplier Details`
- Eyebrow: `Supplier Profile — Demo`
- H1: `Understand the supplier, linked products and target markets before starting a commercial conversation.`
- Demo Supplier: `Noura Foods Demo`
- Intro: `A fictional demo manufacturer used to demonstrate supplier profile, categories, products and target-market content.`
- Linked Products title: `Linked products from the same demo dataset.`
- Markets title: `Illustrative target markets, not distribution rights.`
- Primary CTA: `Start a Commercial Enquiry`
- Secondary CTA: `Back to Suppliers`
- English preserves Arabic meaning without stronger claims.

## Information Architecture
Breadcrumb → Supplier Identity / Profile → Origin & Relationship Facts → Category Coverage → Linked Products → Demo Certifications → Demo Markets → Disclosure → Commercial CTA.

## Supplier Identity Contract
Hero may show only:
- neutral initials identity / provided logo when buyer replaces demo data
- localized supplier name
- localized summary
- illustrative origin
- category-count badge
- linked-product-count badge
- demo-market-count badge
- back-to-directory and enquiry routes

## Relationship Facts Contract
Relationship facts are derived from canonical data rather than duplicated content:
- Supplier ID
- Origin
- Category count
- Linked product count
- Demo market count
- Demo certification-reference count

The page must explicitly state that these relations demonstrate schema linkage only and do not establish agency, representation, exclusivity or territory rights.

## Category Coverage Contract
- Category labels use the frozen PG09 IDs: `ambient`, `beverages`, `dairy`, `frozen`, `confectionery`, `ingredients`.
- Category tags come directly from `supplier.categoryIds`.
- Category tags may link to `products.html?category=<id>`.

## Linked Products Contract
- Resolve only existing `products.json` records related to the supplier.
- Do not duplicate product data into the supplier record.
- Card may show image, localized name, category, pack size and route to `product-details.html?id=<product-id>`.
- Maximum visible records equals all linked V1 supplier records; current demo maximum is four.
- Product RFQ links may use `rfq.html?product=<product-id>`.

## Certification Contract
- Supplier `certifications` contains reference IDs only.
- Render as `Demo Certification Reference`; never as verified certificate badges.
- Empty state must be explicit where no references exist.

## Market Contract
- Markets resolve from `assets/data/markets.json` using `supplier.marketIds`.
- Market labels and channel tags are illustrative template content.
- Displaying a market never means the supplier has distribution rights, exclusivity, registration or an active partner in that country.
- Market cards may link to `markets.html` without creating country-detail routes in V1.

## Runtime / Progressive Enhancement
- `assets/js/origex-supplier-details.js` is Vanilla JS only.
- Loads supplier, product and market JSON in parallel.
- Resolves `?id=<supplier-id>` and preserves it on language switch.
- Invalid IDs fall back visibly to the default demo supplier.
- Updates an Organization JSON-LD demo record without address, offer, certification, rating or territory-right claims.
- Failure state preserves shell, directory route and contact/RFQ routes.
- No synthetic fallback supplier object is created.

## Visual Direction
- Premium B2B supplier dossier, not marketplace storefront.
- Hero: neutral supplier identity tile + profile copy and concise relationship badges.
- Facts: compact semantic fact grid.
- Categories: restrained tags, not decorative chips overload.
- Products: 2–4 commercial product cards with existing ORVEAX-owned media.
- Markets: compact market cards with explicit `Demo` status.
- Certifications and relationship notes use clear disclosure styling.
- Mobile: single-column information hierarchy with CTA actions full-width where appropriate.
- Reuse M1 tokens, C03 supplier language, product card patterns, badges, alerts, buttons and Global Navigation V1.

## SEO / Page Identity Contract
SEO ID: PG13  
Indexability: INDEX candidate for default demo layout.

### Arabic
- File: `ar/supplier-details.html`
- Title: `ملف مورد وعلامة تجارية B2B | ORIGEX`
- Meta Description: `راجع ملف مورد تجريبي يشمل المنشأ والفئات والمنتجات والأسواق المستهدفة ومراجع الشهادات قبل بدء التواصل التجاري.`
- H1: `اعرف المورد ومنتجاته والأسواق المستهدفة قبل بدء التواصل التجاري.`
- Canonical: `https://example.com/ar/supplier-details.html`

### English
- File: `en/supplier-details.html`
- Title: `B2B Supplier & Brand Profile | ORIGEX`
- Meta Description: `Review an illustrative supplier profile covering origin, category coverage, linked products, target markets and demo certification references before enquiry.`
- H1: `Understand the supplier, linked products and target markets before starting a commercial conversation.`
- Canonical: `https://example.com/en/supplier-details.html`

Required: self canonical, AR/EN/x-default hreflang, Open Graph baseline, WebPage + BreadcrumbList + Organization JSON-LD. Organization schema is explicitly demo-named and contains no offers, ratings, certifications, address, legal identifiers or territory rights.

## Navigation Contract
- PG13 is a Supplier-family detail page.
- Desktop primary `Suppliers` is current.
- Mega-menu `Suppliers & Brands` is current as parent.
- Mobile `Suppliers` is current.
- Language switch preserves active `?id=`.
- Header/menu structure stays identical to Global Navigation V1.

## Responsive / Accessibility
- no horizontal overflow at 390 / 820 / 1366 / 1536
- touch targets follow shared component minimums
- single semantic H1
- visible breadcrumb
- status/error uses live-region semantics
- facts use `dl/dt/dd`
- product images have localized alt text
- demo state is conveyed in text, not color alone
- keyboard navigation works across supplier/product/category/CTA routes
- RTL/LTR independently verified
- reduced-motion rules respected

## Exit Gate
PS7 only after AR+EN build and data/source/SEO/assets/icons/query-param/supplier-switch/language-switch/product-relations/market-relations/certification-reference/navigation/responsive QA PASS. PS8 remains gated by deployed Cloudflare browser acceptance.
