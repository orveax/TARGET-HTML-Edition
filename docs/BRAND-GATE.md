# ORX-P01 — Demo Brand & Visual Identity Gate

**Gate:** 02  
**Status:** CLOSED — APPROVED  
**Closed:** 2026-08-19  
**Next Gate:** 03 — Design System Foundation

## Approved Brand

### Marketplace / Demo Product Brand

**ORIGEX**  
Arabic rendering: **أوريجكس**  
Internal shorthand: **RGX**  
Product code: **ORX-P01**

### Brand Relationship

- **ORVEAX** = Author / Product Owner / Copyright Owner
- **ORX-P01** = Internal product code
- **ORIGEX** = Commercial template / demo brand

ORIGEX is independent from TARGET client identity while preserving the reusable UX and layout DNA extracted from the mature TARGET project.

## Approved Language Priority

- **Arabic = primary/default presentation language**
- **English = secondary language**
- every preview/review artifact must include both Arabic and English states
- Arabic receives first-class RTL, typography, mixed-content and responsive QA

## Approved Logo Direction

**Origin Route Mark**

- O / Origin outer form
- route from source to destination
- intersecting route geometry creates a subtle X / exchange reference
- SVG-first
- monochrome-capable geometry
- compact mark suitable for favicon/app use
- public wordmark: ORIGEX
- Arabic أوريجكس is a supporting language lockup

Current source assets:

- `assets/brand/origex-mark.svg`
- `assets/brand/origex-logo.svg`

## Approved Core Palette

- Trade Ink — `#15343B`
- Deep Ink — `#0D252B`
- Route Teal — `#3F6F68`
- Origin Copper — `#C47A4A`
- Warm Sand — `#E8DFD0`
- Paper — `#FAF8F4`
- Surface — `#FFFFFF`
- Graphite — `#20282C`
- Muted — `#667278`
- Border — `#D8DEDB`

Canonical variables live in `assets/css/tokens.css`.

## Approved Typography Direction

### Arabic — Primary

**Tajawal**

Hierarchy:

- 800 — display / hero
- 700 — major headings
- 600 — subheadings / strong UI
- 500 — labels / navigation / controls
- 400 — body

Arabic-specific line-height tokens are required.

### English — Secondary

**Manrope**

Hierarchy:

- 800 — display / hero
- 700 — major headings
- 600 — subheadings / strong UI
- 500 — labels / navigation / controls
- 400 — body

Typography is approved for design/build direction. Commercial ZIP font-file redistribution remains a separate licensing/asset-registry check before marketplace packaging; no unverified font binaries are to be embedded in deliverables.

## Approved Icon Direction

- single outline icon family
- consistent optical stroke
- directional icons mirror in RTL
- no mixed icon packs
- icons are functional/hierarchical rather than decorative clutter

## Approved Image Direction

Focus on:

- manufacturing and packing
- product review and sourcing
- B2B supplier context
- warehouse/distribution selectively
- route-to-market and export context

Avoid restaurant imagery, grocery-store clichés, generic handshakes and all TARGET-owned/client-specific assets.

## Approved Visual Personality

**Premium Trade / Origin / Market Access**

- medium-low radius
- restrained shadows
- borders/surface contrast for structure
- strong whitespace
- high information density only where products/suppliers require it
- subtle motion
- reduced-motion support mandatory
- Arabic is designed and QA'd as a first-class system

## Preview Rule

Until final production packaging, each preview must provide:

- Arabic default state
- English secondary state
- raw page preview
- reusable device-frame preview using the common-screen matrix in `docs/PREVIEW-POLICY.md`

The preview frame is review infrastructure and is excluded/removed from the final production/marketplace package.

## Ownership Rule

ORVEAX attribution is mandatory in product source headers, README, documentation, changelog, credits/license notice and marketplace authorship.

Buyer-facing footer attribution may be removed by the licensed buyer and is not the primary ownership mechanism.

## Exit Criteria

- [x] demo brand name — ORIGEX
- [x] Arabic rendering — أوريجكس
- [x] logo direction — Origin Route Mark
- [x] final core palette
- [x] Arabic typography — Tajawal
- [x] English typography — Manrope
- [x] Arabic-first language priority
- [x] icon direction
- [x] image direction
- [x] visual personality statement

## Gate Result

**GATE 02 PASSED.**

Proceed to **Gate 03 — Design System Foundation** and then the first production page build.
