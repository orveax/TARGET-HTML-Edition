# ORIGEX — Asset & License Register V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: ACTIVE REGISTER  
Last Updated: 2026-08-19

No third-party asset or dependency may enter the distributable package without a row in this register.

## Status Vocabulary

- `APPROVED — DISTRIBUTABLE`
- `APPROVED — PREVIEW ONLY`
- `PENDING VERIFICATION`
- `PROHIBITED`
- `ORVEAX OWNED`

## Dependencies

| Asset ID | Asset | Version | Source / Owner | License | Package Use | Status | Notes |
|---|---|---:|---|---|---|---|---|
| DEP-001 | Bootstrap | 5.3.8 | Bootstrap / twbs | MIT code license | local vendor CSS/JS | APPROVED — DISTRIBUTABLE | exact local files to be added in M1 |
| DEP-002 | Lucide semantic icons | M1 lock pending exact package snapshot | Lucide | ISC; Feather-derived icons may retain MIT notices | selected local SVG subset/sprite | PENDING VERIFICATION | verify exact selected icon files/names and notices before commit |

## ORVEAX-Owned Assets

| Asset ID | Asset | Path | Status | Notes |
|---|---|---|---|---|
| ORX-BRAND-001 | ORIGEX primary logo | `assets/brand/origex-logo.svg` | ORVEAX OWNED | active |
| ORX-BRAND-002 | ORIGEX light logo | `assets/brand/origex-logo-light.svg` | ORVEAX OWNED | active |
| ORX-BRAND-003 | ORIGEX mark | `assets/brand/origex-mark.svg` | ORVEAX OWNED | active |
| ORX-PATTERN-001..006 | ORIGEX Pattern System PT01–PT06 | `assets/patterns/` | ORVEAX OWNED | implementation pending M1 |

## Fonts

| Asset ID | Font | Delivery | License / Source | Status | Rule |
|---|---|---|---|---|---|
| FONT-001 | Tajawal | pending M1 packaging decision | verify official source/license before local packaging | PENDING VERIFICATION | no font file committed until redistribution terms are verified |
| FONT-002 | Manrope | pending M1 packaging decision | verify official source/license before local packaging | PENDING VERIFICATION | no font file committed until redistribution terms are verified |

## Photography / Images

Primary demo sourcing strategy:
- Pexels: preview candidate only after per-asset source/license logging.
- Unsplash: secondary preview candidate only after per-asset source/license logging.
- Pixabay: special-case preview candidate only after per-asset source/license logging.

Default buyer ZIP rule: no third-party stock photography unless redistribution rights for that exact asset are verified and logged.

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
- font binaries with unverified redistribution rights;
- icon packs not approved by the Icon System.

## M1 Action

Before M1 closes:
1. add local Bootstrap 5.3.8 files and license notice;
2. verify/package the selected Lucide subset and notices;
3. resolve font delivery/licensing;
4. create ORIGEX pattern assets;
5. log every shipped asset.

Copyright © ORVEAX.
