# ORIGEX — Data Schema V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED & FROZEN  
Approval Date: 2026-08-19

This document defines the stable V1 structured-data contract used by listings, filters and detail pages. It is not a CMS specification.

## 1. Data Domains

Canonical files when data-driven behavior is used:
- `assets/data/products.json`
- `assets/data/suppliers.json`
- `assets/data/markets.json`

Editorial page copy remains in HTML. Global company/contact settings remain in `config.js`.

## 2. Product Schema

Required/standard fields:
- `id`
- `slug`
- `nameAr`
- `nameEn`
- `brandId`
- `categoryId`
- `originCode`
- `packSizeAr`
- `packSizeEn`
- `packagingAr`
- `packagingEn`
- `shelfLifeAr`
- `shelfLifeEn`
- `storageAr`
- `storageEn`
- `moq`
- `availability`
- `certifications`
- `images`
- `datasheet`
- `brochure`
- `supplierId`
- `featured`

Optional fields may be added only when required by an approved Main Feature and must remain backward-compatible where practical.

Sample:
```json
{
  "id": "prod-001",
  "slug": "premium-tomato-paste",
  "nameAr": "معجون طماطم فاخر",
  "nameEn": "Premium Tomato Paste",
  "brandId": "brand-001",
  "categoryId": "ambient-food",
  "originCode": "TR",
  "packSizeAr": "12 × 400 جم",
  "packSizeEn": "12 × 400 g",
  "packagingAr": "علب معدنية",
  "packagingEn": "Cans",
  "shelfLifeAr": "24 شهرًا",
  "shelfLifeEn": "24 months",
  "storageAr": "مكان جاف وبارد",
  "storageEn": "Cool, dry place",
  "moq": "1 pallet",
  "availability": "available",
  "certifications": ["demo-cert-01"],
  "images": ["product-001.webp"],
  "datasheet": "#",
  "brochure": "#",
  "supplierId": "supplier-001",
  "featured": true
}
```

## 3. Supplier / Brand Schema

Standard fields:
- `id`
- `slug`
- `name`
- `nameAr` when localized display differs
- `nameEn` when localized display differs
- `countryCode`
- `logo`
- `summaryAr`
- `summaryEn`
- `categoryIds`
- `productIds`
- `marketIds`
- `certifications`
- `featured`
- `website` optional placeholder/demo field

## 4. Market Schema

Standard fields:
- `id`
- `slug`
- `countryCode`
- `nameAr`
- `nameEn`
- `region`
- `summaryAr`
- `summaryEn`
- `channelTagsAr`
- `channelTagsEn`
- `featured`

## 5. IDs and Relations

- IDs are stable lowercase kebab-case identifiers.
- Relations use IDs, not duplicated full objects.
- Slugs are URL-friendly lowercase kebab-case.
- Country codes use a consistent two-letter convention throughout the demo data.
- Display labels are bilingual where user-facing language differs.

## 6. Availability Vocabulary

V1 controlled values:
- `available`
- `limited`
- `on-request`
- `unavailable`

UI maps these values to documented labels/badges. Pages do not invent additional availability vocabulary.

## 7. Demo Data Integrity

- Demo data must not impersonate real commercial rights, certifications or distribution relationships.
- Fictional/demo values are clearly safe for template demonstration.
- Real brand/supplier data is used only when rights and purpose are appropriate.

## 8. JavaScript Fallback

Where practical, core page meaning remains understandable without JavaScript. Data-driven filters/search are progressive enhancements; failure states are designed and documented.

## 9. Governance

Schema changes that break Product Card, Product Details, Supplier Directory, Supplier Details, Markets or filters require an Architecture Change Request. Content/data additions that conform to this schema do not reopen architecture.

Copyright © ORVEAX.