# ORIGEX — Documentation Architecture V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED STRUCTURE — IMPLEMENTATION IN M8

Documentation is part of the product. V1 documentation must explain the shipped V1 Main Features only; deferred V1.1 Additional Features are not documented as if they ship in V1.

## 1. Documentation Goals

A buyer should be able to:
- open the package locally;
- understand the file structure;
- choose Arabic or English;
- change common company data through `config.js`;
- edit page content safely;
- edit product/supplier/market data where applicable;
- understand forms and backend integration points;
- replace demo assets/data;
- configure SEO metadata/hreflang;
- deploy to standard static hosting;
- understand licenses/credits and support boundaries.

## 2. Planned Buyer Documentation Structure

```text
documentation/
├── index.html
├── getting-started/
│   ├── quick-start.html
│   ├── installation.html
│   ├── file-structure.html
│   └── deployment.html
├── customization/
│   ├── config.html
│   ├── brand.html
│   ├── content.html
│   └── demo-to-production.html
├── languages/
│   ├── arabic-rtl.html
│   ├── english-ltr.html
│   └── mixed-direction-data.html
├── pages/
│   ├── page-index.html
│   ├── home-family.html
│   ├── company-market.html
│   ├── products-suppliers.html
│   ├── conversion.html
│   └── support-utility.html
├── components/
│   ├── overview.html
│   ├── buttons-cards.html
│   ├── forms.html
│   ├── navigation-disclosure.html
│   ├── tables-data.html
│   └── media-icons-patterns.html
├── data/
│   ├── products.html
│   ├── suppliers.html
│   └── markets.html
├── forms/
│   ├── contact.html
│   ├── rfq.html
│   ├── submit-product.html
│   ├── partner.html
│   └── backend-integration.html
├── seo/
│   ├── metadata.html
│   ├── canonical-hreflang.html
│   ├── structured-data.html
│   └── indexing.html
├── accessibility/
│   └── accessibility.html
├── assets-licenses/
│   ├── dependencies.html
│   ├── fonts-icons.html
│   ├── images.html
│   └── credits.html
└── support/
    ├── faq.html
    ├── changelog.html
    └── support-policy.html
```

## 3. Required Guides

### Quick Start
Target: a beginner can get the template open and make first changes quickly.

### File Structure
Explain `/ar`, `/en`, `/assets`, `/documentation` and all distributable support files. Root clutter is prohibited.

### Config Guide
Explain only approved global/repeated settings. Explicitly state that `config.js` is not a CMS/page builder.

### Arabic RTL Guide
Cover `lang="ar" dir="rtl"`, logical properties, mixed LTR data, forms/tables, directional icons and responsive ordering.

### English LTR Guide
Cover counterpart rules and content parity.

### Demo-to-Production Guide
Use `DEMO-VS-PRODUCTION-POLICY-V1.md` as authority and provide a mandatory replacement checklist.

### Product / Supplier / Market Data Guides
Use `DATA-SCHEMA-V1.md` and explain fields, relationships and examples.

### Forms Guide
Static forms are UI templates unless a backend integration is explicitly bundled. Never imply server-side submission exists when it does not.

### SEO Guide
Use `SEO-METADATA-PAGE-NAMING-V1.md` as authority for page names, titles, descriptions, canonical, hreflang, OG, indexing and structured data.

### Deployment Guide
At minimum cover generic shared hosting/static upload and static-host concepts. Do not make a third-party hosting platform a required dependency.

## 4. V1.1 Documentation Boundary

The V1.1 Additional Feature backlog and content packs are internal product-planning assets during V1.

When a V1.1 feature is actually implemented, its buyer documentation must include:
1. purpose;
2. compatible pages;
3. markup/dependencies;
4. Arabic/English behavior;
5. responsive/accessibility behavior;
6. configuration/data requirements;
7. removal/disable instructions.

Do not publish instructions for unshipped Additional Features inside V1 buyer docs.

## 5. Documentation Quality Gate

Documentation must:
- match the actual package tree;
- use exact filenames/API hooks;
- contain no obsolete routes or screenshots;
- distinguish preview-only assets from distributable assets;
- explain licenses/credits;
- be responsive and accessible;
- use copyable examples where useful;
- be reviewed after final packaging, not before only.

## 6. Final Package Support Files

Submission Candidate must include:
- `README.md`
- `CHANGELOG.md`
- `CREDITS.md`
- `LICENSE-NOTICE.txt`
- `documentation/`

These are created/finalized in M8 from the current canonical registers, not copied from old builds.

Copyright © ORVEAX.
