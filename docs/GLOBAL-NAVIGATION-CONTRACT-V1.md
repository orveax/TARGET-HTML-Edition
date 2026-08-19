# ORIGEX — Global Navigation Contract V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED & LOCKED  
Adopted: 2026-08-19

## Purpose

Define one stable navigation architecture for every standard ORIGEX page. Header/menu structure must not change from page to page. Only current/active state and the language-switch destination may change.

## UX Rule

A user must be able to move between Company, Products, Suppliers and Market pages without relearning the header.

Page-specific navigation variants are prohibited unless the Page Design Profile explicitly defines a conversion/utility exception.

## Approved Standard Desktop Header

Primary navigation order:

### Arabic
1. `الرئيسية` → `index.html`
2. `المنتجات` → `products.html`
3. `الموردون` → `suppliers.html`
4. `الوصول إلى السوق` → `market-access.html`
5. `استكشف` → canonical mega menu trigger

### English
1. `Home` → `index.html`
2. `Products` → `products.html`
3. `Suppliers` → `suppliers.html`
4. `Market Access` → `market-access.html`
5. `Explore` → canonical mega menu trigger

Header actions remain:
- language switch;
- RFQ primary CTA;
- mobile drawer trigger.

## Canonical Mega Menu

### Company
- About → `about.html`
- How We Work → `how-we-work.html`
- Capabilities → `capabilities.html`
- Company Profile → `company-profile.html`

### Products
- Product Categories → `product-categories.html`
- All Products → `products.html`

### Suppliers
- Suppliers & Brands → `suppliers.html`
- For Suppliers → `for-suppliers.html`
- Submit Your Product → `submit-product.html`

### Market & Partnership
- Market Access → `market-access.html`
- Markets & Countries → `markets.html`
- Become Distributor / Partner → `become-partner.html`

### Resources & Support
- Case Studies → `case-studies.html`
- Downloads / Resources → `resources.html`
- Certifications & Compliance → `certifications-compliance.html`
- Insights → `insights.html`
- FAQ → `faq.html`
- Contact → `contact.html`

### Home Demos
- Home 01 → `index.html`
- Home 02 → `home-02.html`
- Home 03 → `home-03.html`
- Landing / One Page → `landing.html`

Detail and utility layouts such as Product Details, Supplier Details, Service Details, Article Details, Case Study Details, Privacy, Terms, 404, Coming Soon and Components are intentionally reached contextually and do not receive top-level mega-menu entries.

## Canonical Mobile Drawer

Mobile uses the same information architecture in a simplified flat order. It must not expose a different business structure from desktop.

Required primary order:
1. Home
2. Products
3. Product Categories
4. Suppliers
5. For Suppliers
6. Market Access
7. Markets
8. About
9. How We Work
10. Capabilities
11. Company Profile
12. Submit Product
13. Become Partner
14. Resources
15. Insights
16. FAQ
17. Contact
18. language switch

## Current-State Mapping

Only current state changes between pages.

Parent mapping:
- `product-details.html` → Products
- `supplier-details.html` → Suppliers
- `service-details.html` → Capabilities inside Explore
- `case-study-details.html` → Case Studies inside Explore
- `article-details.html` → Insights inside Explore
- `company-profile.html` → Company Profile inside Explore

## Approved Exception

**PG04 — Landing / One Page** retains its compact conversion header and does not use the full mega menu. This is an intentional UX exception defined by its page contract, not navigation drift.

All other standard pages use the canonical global header/menu.

## Implementation Rule

- Header/mega-menu/mobile-drawer markup is static semantic HTML in each distributed page.
- `origex-ui.js` controls interaction only; it must not inject/reorder business navigation groups.
- Future pages must start from the canonical shell.
- A permanent navigation regression gate must fail if standard pages diverge in structure/order.

## Change Control

Any change to primary navigation order, mega-menu groups or the Landing exception requires an explicit IA/Navigation Change Request and synchronized AR/EN update.

Copyright © ORVEAX.