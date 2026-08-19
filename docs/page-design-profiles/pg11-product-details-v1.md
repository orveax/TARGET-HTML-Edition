# ORIGEX — PG11 Product Details | Page Design Profile V1

Product ID: ORX-P01  
Milestone: M4 — Product / Supplier / Conversion  
Status: PS6 — FROZEN FOR BUILD  
Canonical file: `product-details.html`

## Purpose
Provide a reusable B2B product-detail layout that turns one structured product record into a commercial evaluation surface before RFQ. The page must expose decision-relevant product, packaging, storage, supplier and document information without becoming consumer ecommerce or inventing price, stock, ratings, certifications or distribution rights.

## Frozen Main Features
Authority: `docs/SCOPE-FREEZE-V1-FINAL.md`.

1. Product media
2. Product name
3. Brand
4. Category
5. Country of origin
6. Pack size
7. Packaging
8. Shelf life
9. Storage
10. MOQ
11. Availability
12. Certifications
13. Datasheet
14. Brochure
15. RFQ
16. Related products

No price, discount, cart, checkout, wishlist, comparison, rating, review count, live-stock quantity or ecommerce option selectors are added in V1.

## Canonical Data Contract
- Products: `assets/data/products.json`
- Suppliers / brand relationship lookup: `assets/data/suppliers.json`
- Schema authority: `docs/DATA-SCHEMA-V1.md`
- Default demonstration record: `prod-001` — `Concentrated Tomato Sauce — 400 g` / `صلصة طماطم مركزة — 400 جم`.
- `?id=<product-id>` may switch the demonstration record using the same layout and schema.
- Invalid/missing IDs fall back visibly to `prod-001`; no fabricated product object is generated.
- Supplier relationship is resolved from `supplierId`. Current V1 demo uses the supplier display name as the visible brand label because no separate brand dataset exists.
- Availability uses only the frozen vocabulary. Current demo product is `on-request`.
- Certification IDs are displayed strictly as demo references, not verified certification claims.
- `datasheet` / `brochure` values of `#` remain documented placeholders and are never presented as real downloadable files.

## Arabic Content Contract
- H1: `منتجك يحتاج ملفًا تجاريًا واضحًا قبل أن يحتاج عرضًا أكبر.`
- Demo product: `صلصة طماطم مركزة — 400 جم`.
- Core fact baseline: Noura Foods Demo / Italy illustrative / Ambient Foods / 400 g / 24 units / 24 months demo / dry ambient / MOQ on request / availability enquire.
- Primary CTA: `إرسال طلب السعر`
- Mandatory disclosure: all product, origin, supplier, packaging, shelf-life, availability, certification and document values are fictional/illustrative template data and must be replaced with verified buyer data before publication.

## English Content Contract
- H1: `Your product needs a clear commercial profile before it needs a bigger presentation.`
- Demo product: `Concentrated Tomato Sauce — 400 g`.
- Primary CTA: `Request a Quote`
- English preserves the Arabic commercial meaning without stronger claims.

## Information Architecture
Breadcrumb → Product Identity / Media → Commercial Facts → Packaging & Handling → Supplier / Brand Relationship → Certifications & Documents → Related Products → RFQ CTA.

The page uses eight frozen composition blocks:
1. Hero / product identity
2. Commercial facts
3. Packaging & handling
4. Supplier relationship
5. Certifications & documents
6. Related products
7. Demo disclosure
8. RFQ CTA

## Product Identity Contract
The hero may display only data available from the product/supplier contract:
- localized product name
- product media
- brand/supplier display label
- category
- illustrative country of origin
- availability mapped from frozen vocabulary
- pack size
- RFQ action
- back-to-products action

## Commercial Facts Contract
Decision facts are structured as semantic definition-list or equivalent accessible fact groups. Data comes from the selected product record and is never duplicated into a second product object in JavaScript.

## Supplier Relationship Contract
- Resolve supplier through `product.supplierId`.
- Display localized supplier name and summary.
- Link to future `supplier-details.html?id=<supplierId>`.
- The relationship is explicitly fictional/demo.
- Do not claim agency, exclusivity, distribution territory or representation rights.

## Certification / Resource Contract
- Certification IDs are demo references only.
- Datasheet and brochure controls are disabled/placeholders while their schema fields equal `#`.
- A buyer replacing demo data may point these fields to real local resources.
- No fake file size, page count, issue date, regulatory status or downloadable PDF is invented.

## Related Products Contract
- Related products use existing `products.json` records only.
- Priority: same category, then same supplier, excluding the current product.
- Maximum three cards.
- Each card routes back to the same layout using `product-details.html?id=<id>` and may route to RFQ.

## Runtime / Progressive Enhancement
- `assets/js/origex-product-details.js` is Vanilla JS only.
- It loads `products.json` and `suppliers.json`, resolves the selected product, renders the detail blocks and updates the language switch to preserve `?id=`.
- It updates Product JSON-LD for the active demo record without adding price/offers.
- If JSON loading fails, a visible error state is shown while global navigation and RFQ/back-to-products routes remain usable.
- A `noscript` message tells buyers that the demo data renderer requires JavaScript; no false fallback product is invented.

## Visual Direction
- Premium B2B product dossier, not retail ecommerce.
- Hero: large product media + product identity/facts panel.
- Desktop: media and identity split; fact grids and document/supplier blocks use two-column compositions where appropriate.
- Tablet: balanced two-column sections where space permits.
- Mobile: single-column, media first, clear RFQ hierarchy.
- Reuse M1 tokens, shared shell, badges, buttons, cards, definition-list patterns, alerts and product-card language.
- Use only ORVEAX-owned demo media already registered for the selected products.

## SEO / Page Identity Contract
SEO ID: PG11  
Indexability: INDEX candidate for the default demo layout.

### Arabic
- File: `ar/product-details.html`
- Title: `تفاصيل منتج غذائي B2B | ORIGEX`
- Meta Description: `راجع نموذجًا توضيحيًا لتفاصيل منتج غذائي B2B يشمل المنشأ والتعبئة والتخزين والمورد والمستندات قبل بدء طلب سعر.`
- H1: `منتجك يحتاج ملفًا تجاريًا واضحًا قبل أن يحتاج عرضًا أكبر.`
- Canonical: `https://example.com/ar/product-details.html`
- Breadcrumb: `المنتجات / تفاصيل المنتج`

### English
- File: `en/product-details.html`
- Title: `B2B Food Product Details | ORIGEX`
- Meta Description: `Review an illustrative B2B food product profile covering origin, packaging, storage, supplier relationship and document placeholders before starting an RFQ.`
- H1: `Your product needs a clear commercial profile before it needs a bigger presentation.`
- Canonical: `https://example.com/en/product-details.html`
- Breadcrumb: `Products / Product Details`

Required: self canonical, AR/EN/x-default hreflang, Open Graph baseline, WebPage + BreadcrumbList + Product JSON-LD. Product JSON-LD contains no `Offer`, price, rating or availability claim beyond descriptive demo data.

## Navigation Contract
Authority: `docs/GLOBAL-NAVIGATION-CONTRACT-V1.md`.
- PG11 is a Product-family detail page.
- Desktop primary `Products` is current.
- Mega-menu `All Products` is current as parent.
- Mobile `Products` is current.
- Header/menu structure must remain identical to other Standard Pages; only current state and language destination vary.

## Responsive / Accessibility
- no horizontal overflow at 390 / 820 / 1366 / 1536
- touch targets follow shared shell and component minimums
- single semantic H1
- visible breadcrumb
- product media has localized useful alt text
- semantic facts use `dl/dt/dd` where appropriate
- disabled resource placeholders are programmatically clear
- error/loading states are announced
- keyboard navigation works for header, related-product links and RFQ actions
- RTL/LTR independently verified
- reduced-motion rules respected

## Exit Gate
PS7 only after AR+EN build and data/source/SEO/assets/icons/query-param/product-switch/language-switch/supplier-relation/resource-placeholder/related-product/RFQ/navigation/responsive QA PASS. PS8 remains gated by deployed Cloudflare browser acceptance.
