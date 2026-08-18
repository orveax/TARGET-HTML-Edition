# ORIGEX — Documentation Architecture

**Product:** ORIGEX / ORX-P01  
**Owner:** ORVEAX  
**Goal:** Beginner-friendly, public, buyer-oriented documentation suitable for ThemeForest submission.

## Documentation Principle

Documentation is part of the product, not an afterthought.

A buyer should be able to install, understand, customize, extend, and deploy ORIGEX without needing to inspect the entire source or contact support for routine changes.

## Planned Documentation Structure

```text
documentation/
├── index.html
├── assets/
│   ├── css/
│   ├── js/
│   └── images/
├── getting-started/
│   ├── installation.html
│   ├── file-structure.html
│   ├── choose-language.html
│   └── deployment.html
├── brand/
│   ├── logo.html
│   ├── colors.html
│   ├── typography.html
│   └── icons.html
├── languages/
│   ├── arabic-rtl.html
│   ├── english-ltr.html
│   └── mixed-content.html
├── pages/
│   ├── page-overview.html
│   ├── home-demos.html
│   ├── products.html
│   ├── suppliers.html
│   ├── market-access.html
│   └── utility-pages.html
├── customization/
│   ├── header-footer.html
│   ├── navigation.html
│   ├── forms.html
│   ├── product-data.html
│   ├── supplier-data.html
│   └── optional-sections.html
├── components/
│   ├── overview.html
│   ├── timeline.html
│   ├── stats.html
│   ├── certifications.html
│   ├── logo-wall.html
│   ├── testimonials.html
│   ├── process.html
│   ├── tables.html
│   └── downloads.html
├── forms/
│   ├── contact.html
│   ├── rfq.html
│   ├── submit-product.html
│   └── backend-integration.html
├── seo/
│   ├── metadata.html
│   ├── hreflang.html
│   └── structured-data.html
├── accessibility/
│   └── accessibility.html
├── assets-licenses/
│   ├── fonts.html
│   ├── icons.html
│   ├── images.html
│   └── credits.html
└── support/
    ├── faq.html
    ├── changelog.html
    └── support-policy.html
```

## Required Buyer Guides

### Getting Started
- What ORIGEX is
- Package contents
- Open locally
- Select Arabic or English starting page
- Basic hosting deployment
- Editing workflow

### File Structure
Explain `/ar`, `/en`, `/assets`, `/documentation`, and supporting files. Root-level clutter must be avoided.

### Arabic RTL Guide
- `lang="ar" dir="rtl"`
- Tajawal
- logical spacing properties
- directional icon behavior
- mixed LTR data such as email, SKU, phone and product codes
- forms and tables

### English LTR Guide
- `lang="en" dir="ltr"`
- Manrope
- language counterpart conventions

### Optional Sections Guide
For every Additional Feature:
1. Purpose
2. Compatible pages
3. Copy HTML
4. CSS requirements
5. JS requirements if any
6. Arabic behavior
7. English behavior
8. Responsive behavior
9. Accessibility
10. Removal instructions

### Product System Guide
Explain how to add/edit:
- product name
- brand
- category
- country of origin
- packaging
- pack size
- shelf life
- storage
- MOQ
- availability
- certifications
- datasheet / brochure
- RFQ links

### Supplier System Guide
Explain supplier cards, supplier detail pages, country/category metadata, documents and related products.

### Forms Guide
Static HTML forms are UI templates unless a working backend is explicitly bundled. Documentation must explain integration points clearly and must not imply server-side functionality that is not included.

### SEO Guide
- title / description
- canonical
- hreflang ar/en/x-default
- Open Graph
- structured-data placeholders
- sitemap guidance

### Deployment Guide
At minimum:
- shared hosting / cPanel-style upload
- Cloudflare Pages / static host concept
- Netlify / static host concept
- local relative-path checks

## Documentation UX Standard

The documentation itself must be responsive and bilingual-friendly, but English may be the operational documentation default if needed for marketplace buyers. Arabic guidance must receive a dedicated, first-class RTL section.

Documentation should include:
- left/sidebar navigation on LTR docs
- search-ready heading structure
- copy-code controls where useful
- visual examples
- callouts for warnings and licensing
- Previous / Next navigation

## ThemeForest / Envato Preparation Notes

- Documentation must be publicly accessible online before submission.
- Treat the buyer as a beginner and explain routine customization without assuming advanced coding knowledge.
- Preview-only assets must be explicitly disclosed as not included.
- Downloadable assets must have redistribution-compatible licenses.

## Package Documentation Files

The final item package must also include:
- `README.md`
- `CHANGELOG.md`
- `CREDITS.md`
- `LICENSE-NOTICE.txt`
- `documentation/`

## ORVEAX Standard

Every documentation page footer should identify ORIGEX and ORVEAX without forcing visible ORVEAX credit into buyer websites. Product ownership is carried through documentation, source headers, versioning, package notices, and marketplace authorship.