# ORIGEX — Asset & License Register V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: ACTIVE REGISTER — M1 BASELINE VERIFIED  
Last Updated: 2026-08-19

No third-party asset or dependency may enter the distributable package without a row in this register.

## Status Vocabulary

- `APPROVED — DISTRIBUTABLE`
- `APPROVED — PREVIEW ONLY`
- `PENDING VERIFICATION`
- `PROHIBITED`
- `ORVEAX OWNED`

## Dependencies

| Asset ID | Asset | Version / Snapshot | Source / Owner | License | Package Use | Status | Notes |
|---|---|---:|---|---|---|---|---|
| DEP-001 | Bootstrap | 5.3.8 | Bootstrap / twbs | MIT | local CSS/RTL CSS/JS bundle | APPROVED — DISTRIBUTABLE | `assets/vendor/bootstrap/`; MIT notice included; checksum record in `M1-VENDOR-SHA256.txt` |
| DEP-002 | Lucide semantic icons | 1.27.0 selected subset | Lucide Icons and Contributors | ISC; Feather-derived subset retains MIT notice | selected local SVG subset + generated sprite | APPROVED — DISTRIBUTABLE | `assets/icons/lucide/` + `assets/icons/sprite.svg`; upstream combined license included |

### M1 Lucide Subset

`arrow-left`, `arrow-right`, `arrow-up`, `menu`, `x`, `search`, `package`, `truck`, `factory`, `earth`, `shield-check`, `file-text`, `download`, `chevron-down`, `chevron-up`, `mail`, `phone`, `map-pin`, `external-link`, `check`, `info`, `triangle-alert`, `upload`, `layers`, `boxes`, `handshake`, `clock`, `building-2`, `badge-check`, `route`, `circle-question-mark`.

`globe-2` is a local registry compatibility alias generated from the selected `earth` icon; it does not introduce a separate third-party source.

## ORVEAX-Owned Assets

| Asset ID | Asset | Path | Status | Notes |
|---|---|---|---|---|
| ORX-BRAND-001 | ORIGEX primary logo | `assets/brand/origex-logo.svg` | ORVEAX OWNED | active |
| ORX-BRAND-002 | ORIGEX light logo | `assets/brand/origex-logo-light.svg` | ORVEAX OWNED | active |
| ORX-BRAND-003 | ORIGEX mark | `assets/brand/origex-mark.svg` | ORVEAX OWNED | active |
| ORX-PATTERN-001 | PT01 Route Lines | `assets/patterns/pt01-route-lines.svg` | ORVEAX OWNED | implemented M1 |
| ORX-PATTERN-002 | PT02 Trade Grid | `assets/patterns/pt02-trade-grid.svg` | ORVEAX OWNED | implemented M1 |
| ORX-PATTERN-003 | PT03 Dot Matrix | `assets/patterns/pt03-dot-matrix.svg` | ORVEAX OWNED | implemented M1 |
| ORX-PATTERN-004 | PT04 Market Nodes | `assets/patterns/pt04-market-nodes.svg` | ORVEAX OWNED | implemented M1 |
| ORX-PATTERN-005 | PT05 Packaging Geometry | `assets/patterns/pt05-packaging-geometry.svg` | ORVEAX OWNED | implemented M1 |
| ORX-PATTERN-006 | PT06 Flow Lines | `assets/patterns/pt06-flow-lines.svg` | ORVEAX OWNED | implemented M1 |
| ORX-MEDIA-001 | Trade logistics hero scene | `assets/media/demo/hero-trade-scene.svg` | ORVEAX OWNED | PG01 marketplace preview + distributable demo media; abstract warehouse, route, cargo and market composition |
| ORX-MEDIA-002 | Tomato sauce demo packshot | `assets/media/demo/product-tomato-sauce.svg` | ORVEAX OWNED | fictional generic packaging; no third-party brand/trademark |
| ORX-MEDIA-003 | Hibiscus drink demo packshot | `assets/media/demo/product-hibiscus.svg` | ORVEAX OWNED | fictional generic packaging; no third-party brand/trademark |
| ORX-MEDIA-004 | UHT milk demo packshot | `assets/media/demo/product-milk.svg` | ORVEAX OWNED | fictional generic packaging; no third-party brand/trademark |
| ORX-MEDIA-005 | Frozen vegetables demo packshot | `assets/media/demo/product-frozen.svg` | ORVEAX OWNED | fictional generic packaging; no third-party brand/trademark |
| ORX-MEDIA-006 | Distribution network hero scene | `assets/media/demo/hero-distribution-network.svg` | ORVEAX OWNED | PG02 wholesale/distribution demo media; abstract warehouse, inventory, route and channel nodes; no real fleet/property/coverage claim |
| ORX-MEDIA-007 | Manufacturer readiness hero scene | `assets/media/demo/hero-manufacturer-readiness.svg` | ORVEAX OWNED | PG03 manufacturer/supplier demo media; abstract factory, packaging, documents and market route; no real capacity/certification/factory claim |
| ORX-MEDIA-008 | Commercial enquiry hero scene | `assets/media/demo/hero-commercial-enquiry.svg` | ORVEAX OWNED | PG04 landing demo media; abstract product-information-enquiry route; no client, brand, performance or conversion claim |
| ORX-MEDIA-009 | Confectionery demo packshot | `assets/media/demo/product-confectionery.svg` | ORVEAX OWNED | PG10 fictional generic confectionery packaging; no third-party brand/trademark |
| ORX-MEDIA-010 | Ingredients demo packshot | `assets/media/demo/product-ingredients.svg` | ORVEAX OWNED | PG10 fictional generic B2B ingredient packaging; no third-party brand/trademark |
| ORX-MEDIA-011 | Company Profile demo cover | `assets/media/demo/company-profile-cover.svg` | ORVEAX OWNED | PG33 fictional digital company-profile cover; distributable; no client document, logo, trademark, person or verified-file claim |

## Fonts

Pinned source snapshot for M1: Google Fonts repository commit `e1118da94a8cb00cf6d06cdac9ef13eb1e5c6ab7`.

| Asset ID | Font | Local Delivery | License / Source | Status | Rule |
|---|---|---|---|---|---|
| FONT-001 | Tajawal | Regular / Medium / Bold / ExtraBold TTF | SIL Open Font License 1.1 / Google Fonts | APPROVED — DISTRIBUTABLE | `assets/fonts/tajawal/`; `OFL.txt` shipped with binaries |
| FONT-002 | Manrope | variable TTF | SIL Open Font License 1.1 / Google Fonts | APPROVED — DISTRIBUTABLE | `assets/fonts/manrope/`; `OFL.txt` shipped with binary |

## M1 Vendor Integrity

Authoritative checksum file: `docs/M1-VENDOR-SHA256.txt`.

Verified local groups:
- Bootstrap CSS + RTL CSS + bundle JS.
- Tajawal selected weights.
- Manrope variable font.
- Lucide generated sprite.

The vendor packaging commit is `9fd274d0ca5ce0fd7760285e103f2f779ef6f334`.

## Photography / Images

Primary demo sourcing strategy:
- Pexels: preview candidate only after per-asset source/license logging.
- Unsplash: secondary preview candidate only after per-asset source/license logging.
- Pixabay: special-case preview candidate only after per-asset source/license logging.

Default buyer ZIP rule: no third-party stock photography unless redistribution rights for that exact asset are verified and logged.

**M2 Home decision:** PG01–PG04 use ORVEAX-owned vector demo media instead of third-party stock photography. These files are distributable, self-contained, fictional, and intentionally free from supplier packaging, trademarks, people/release risk or external attribution requirements.

Image rows must include:
- Asset ID
- filename
- page/section
- source URL
- creator/photographer if applicable
- license
- acquisition date
- preview-only yes/no
- trademark/person/release risk
- notes

## Brand / Social Marks

Semantic icons are Lucide. Brand/social logos must come from official or separately licensed sources and are logged independently. Brand marks are never treated as Lucide icons.

## Preview-Only Rule

Preview-only assets must:
- never enter the buyer ZIP;
- be disclosed in marketplace documentation;
- be replaceable by ORVEAX-owned placeholders in the distributable package.

## Prohibited Until Verified

- random web images;
- copied supplier/product packaging images;
- third-party logos without permission/valid brand-use basis;
- untracked PDFs;
- AI-generated assets inside the buyer download when marketplace policy prohibits that use;
- font binaries without their verified redistribution basis;
- icon packs not approved by the Icon System.

## M1 Closure Record

The M1 vendor/license baseline is complete:
1. Bootstrap 5.3.8 local files + MIT license — verified.
2. Lucide selected subset + combined ISC/MIT notice — verified.
3. Tajawal and Manrope local binaries + OFL notices — verified.
4. ORIGEX PT01–PT06 — implemented and ORVEAX-owned.
5. Vendor checksums — recorded.

Future page imagery and any additional icon/font/brand asset remain subject to this register before entering the buyer package.

Copyright © ORVEAX.