# ORVEAX Product 01 — TARGET HTML Edition

## V1 Scope Lock

**Status:** LOCKED  
**Product ID:** ORX-P01  
**Owner:** ORVEAX  
**Repository:** `orveax/TARGET-HTML-Edition`  
**Primary vertical:** B2B Food Trading / Import-Export / Wholesale / Distribution / Suppliers  
**Languages:** Arabic-first RTL + English LTR  

## Product Positioning

A premium bilingual HTML template for food trading companies, importers, exporters, distributors, wholesalers, manufacturers, suppliers and brand owners.

The product is intentionally vertical-first. It must not be diluted into a generic multipurpose corporate template.

## V1 Page Architecture

### Home Demos
1. Home 01 — Food Trading / Importer
2. Home 02 — Wholesale & Distribution
3. Home 03 — Manufacturer / Supplier

### Company
4. About
5. Team
6. Careers

### Business
7. Services / Capabilities
8. Service Details
9. How We Work

### Products
10. Product Categories
11. Products Grid
12. Product Details

### Suppliers / Brands
13. Suppliers / Brands Directory
14. Supplier / Brand Details

### Market
15. Market Access
16. Markets / Countries

### Conversion
17. For Suppliers
18. Submit Your Product
19. Request a Quote / RFQ
20. Become a Distributor / Partner

### Proof
21. Case Studies
22. Case Study Details

### Resources
23. Downloads / Company Profile / Certificates
24. Insights / Blog
25. Article Details

### Support
26. FAQ
27. Contact

### Utility
28. 404
29. Privacy
30. Terms

## Language Delivery

Each unique layout must ship as a ready-to-use Arabic and English page:

- `/ar/...` using `lang="ar" dir="rtl"`
- `/en/...` using `lang="en" dir="ltr"`
- shared assets and component styles

Target: approximately 30 unique layouts / approximately 60 ready HTML pages.

## Core Product Systems

- Arabic-first RTL design system
- English LTR system
- Shared design tokens
- Header / Mega Menu / Mobile Navigation
- Product system
- Supplier / Brand system
- Market access system
- RFQ / enquiry conversion system
- Resources / downloads system
- Certifications / compliance components
- Case study system
- Component / elements showcase
- SEO-ready bilingual structure
- Accessibility baseline
- Performance baseline
- Documentation and licensing register

## V1 Non-Goals

The following are excluded from V1 unless explicitly reopened:

- Ecommerce cart / checkout / payment
- User account / authentication
- Admin dashboard
- React / Vue runtime dependency
- Page builder integration
- Dark mode
- excessive animation systems
- large multipurpose demo count

## Build Gates

1. Scope Lock — CLOSED
2. Demo Brand & Visual Identity — OPEN
3. Design Tokens — PENDING
4. Arabic RTL System — PENDING
5. Global Components — PENDING
6. Header / Footer — PENDING
7. Home 01 Fidelity Build — PENDING
8. Home 01 Arabic QA — PENDING
9. Home 01 English QA — PENDING
10. TARGET Baseline Pages — PENDING
11. Commercial Expansion Pages — PENDING
12. Home 02 / Home 03 — PENDING
13. Component Library — PENDING
14. Documentation — PENDING
15. Full QA — PENDING
16. Demo / Deployment — PENDING
17. Envato Package — PENDING

## ORVEAX Ownership

ORVEAX ownership is foundational to the product.

Every principal source file should carry a lightweight ORVEAX product header containing:

- Product name
- Product ID `ORX-P01`
- Version
- Designed & Developed by ORVEAX
- Copyright notice

The package must include:

- `README.md`
- `CHANGELOG.md`
- `CREDITS.md`
- `LICENSE-NOTICE.txt`
- `documentation/`

Frontend credit such as “Designed by ORVEAX” may appear in the demo but must remain removable by a licensed buyer. Source ownership and marketplace authorship remain ORVEAX-controlled.

## Change Control

After this lock, any new V1 page, framework, feature family, or major dependency requires an explicit Scope Change entry before implementation.

Small UX refinements and accessibility/performance improvements do not reopen scope when they remain inside an already-approved component or page.
