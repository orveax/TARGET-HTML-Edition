# ORIGEX — SEO, Metadata & Page Naming System V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED & LOCKED  
Approval Date: 2026-08-19

This document is the canonical authority for page identity, file naming, metadata and SEO structure across ORIGEX V1.

## 1. Governing Principle

Every page is defined in one controlled chain:

Page ID → Canonical Page Name → File/Slug → Content Contract → H1 → SEO Title → Meta Description → Canonical URL → hreflang → Open Graph → Structured Data → Internal Links → SEO QA.

No page may invent these values independently during implementation.

## 2. Page Identity

Every unique V1 layout uses a stable `PG##` identifier. The ID does not change when marketing copy changes.

Canonical mapping:

- PG01 — Home 01 — `index.html`
- PG02 — Home 02 — `home-02.html`
- PG03 — Home 03 — `home-03.html`
- PG04 — Landing / One Page — `landing.html`
- PG05 — About — `about.html`
- PG06 — How We Work — `how-we-work.html`
- PG07 — Capabilities / Services — `capabilities.html`
- PG08 — Service Details — `service-details.html`
- PG09 — Product Categories — `product-categories.html`
- PG10 — Products Grid — `products.html`
- PG11 — Product Details — `product-details.html`
- PG12 — Suppliers / Brands Directory — `suppliers.html`
- PG13 — Supplier / Brand Details — `supplier-details.html`
- PG14 — Market Access — `market-access.html`
- PG15 — Markets / Countries — `markets.html`
- PG16 — For Suppliers — `for-suppliers.html`
- PG17 — Submit Your Product — `submit-product.html`
- PG18 — RFQ / Request a Quote — `rfq.html`
- PG19 — Become Distributor / Partner — `become-partner.html`
- PG20 — Case Studies — `case-studies.html`
- PG21 — Case Study Details — `case-study-details.html`
- PG22 — Downloads / Resources — `resources.html`
- PG23 — Certifications & Compliance — `certifications-compliance.html`
- PG24 — Insights / Blog — `insights.html`
- PG25 — Article Details — `article-details.html`
- PG26 — FAQ — `faq.html`
- PG27 — Contact — `contact.html`
- PG28 — 404 — `404.html`
- PG29 — Coming Soon — `coming-soon.html`
- PG30 — Privacy — `privacy.html`
- PG31 — Terms — `terms.html`
- PG32 — Components / Elements — `components.html`

Home 01 is the only canonical `index.html`. Do not create duplicate `home-01.html` content without an explicit reason.

## 3. File / Slug Rules

- lowercase only.
- kebab-case only.
- English semantic slugs for package clarity.
- Arabic and English folders mirror the same file names.
- No page-number filenames, temporary names, `final-v2`, underscores or mixed casing.

Recommended bilingual structure:

```text
/ar/products.html
/en/products.html
```

Language is declared by `lang` and `dir`, not by filename language.

## 4. Page Name vs H1 vs SEO Title

These are related but not identical.

- Canonical Page Name = internal product/navigation identity.
- Menu Label = concise navigation wording.
- H1 = user-facing page proposition.
- SEO Title = concise search-result title aligned with page purpose.

They must describe the same intent without being forced to use identical copy.

## 5. SEO Title Rules

Default patterns:

Standard page:
```text
[Primary Topic] | ORIGEX
```

Detail page:
```text
[Entity Name] — [Commercial Context] | ORIGEX
```

Article:
```text
[Article Title] | ORIGEX Insights
```

Rules:
- unique per page.
- descriptive and concise.
- no keyword stuffing.
- no meaningless boilerplate.
- aligned with visible H1 and actual page content.
- Arabic title written natively; English is adapted professionally.

## 6. Meta Description Rules

Each indexable page requires a unique description.

Rules:
- one or two concise sentences.
- communicate page purpose and useful commercial context.
- use relevant B2B terminology naturally.
- no keyword stuffing.
- no copied descriptions across multiple pages.
- no unsupported claims.

## 7. Canonical / hreflang

For bilingual production deployment, each language page declares:
- self-referencing canonical.
- `hreflang="ar"` alternate.
- `hreflang="en"` alternate.
- `x-default` according to buyer deployment strategy.

Canonical/hreflang URLs remain placeholders in the commercial package until the buyer defines the production domain.

## 8. Open Graph Metadata

Every public content page provides:
- `og:type`
- `og:title`
- `og:description`
- `og:url`
- `og:image`

Article pages use article-appropriate type where relevant.

OG imagery follows the Image/Media System and asset/licensing policy.

## 9. Structured Data Policy

Structured data is only added when the visible page contains matching data.

Approved candidate mappings:
- Home: WebSite / Organization where appropriate.
- Internal pages: BreadcrumbList where appropriate.
- Product Details: Product only when data is present and valid for that implementation.
- Supplier/Brand Details: Organization where appropriate.
- Article Details: Article where appropriate.

Prohibited:
- fake ratings.
- fake reviews.
- fake prices.
- fake stock/availability claims.
- fake awards/certifications.
- structured data not represented in visible content.

## 10. Indexability Classes

Every page/environment receives one explicit state:

- INDEX
- NOINDEX
- ENVIRONMENT-DEPENDENT

Typical production candidates: commercial content pages.
Typical environment-dependent/noindex candidates: preview utilities, components library, coming-soon variants, internal developer/demo utilities.

ThemeForest live demo indexability is governed separately by `DEMO-VS-PRODUCTION-POLICY-V1.md`.

## 11. Internal Link Naming

Anchor copy should describe the destination or action.

Prefer:
- Explore Products
- Review Supplier Requirements
- Request a Quote
- View Product Details

Avoid generic `Click Here` / `Read More` where a descriptive action is possible.

## 12. Meta Keywords

`meta name="keywords"` is not part of the ORIGEX SEO strategy and is not required.

SEO focus remains on:
- useful content.
- clear titles/headings.
- semantic HTML.
- logical URLs.
- internal linking.
- canonical/hreflang.
- image alt text.
- structured data where appropriate.
- performance/accessibility.

## 13. Mandatory Page SEO Contract

Every Page Design Profile must include:

```text
SEO ID / Page ID
Indexability
Slug/File AR
Slug/File EN
Title AR
Title EN
Meta Description AR
Meta Description EN
H1 AR
H1 EN
Canonical AR
Canonical EN
hreflang AR
hreflang EN
x-default strategy
OG Title AR/EN
OG Description AR/EN
OG Image
Schema Type
Breadcrumb Label AR/EN
Primary Internal Links
```

## 14. Change Control

A page naming/SEO convention change after this lock requires a documented SEO/Product Architecture Change Request. Normal page implementation may populate page-specific values but may not redesign this system.

Copyright © ORVEAX.