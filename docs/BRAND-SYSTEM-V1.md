# ORIGEX — Brand System v1

**Product:** ORX-P01  
**Commercial Brand:** ORIGEX  
**Arabic Rendering:** أوريجكس  
**Author / Product Owner:** ORVEAX  
**Status:** APPROVED FOR V1 BUILD

## Language Priority

ORIGEX is **Arabic-first**.

- Arabic is the default language in previews and the primary presentation language.
- English is always provided as the second language.
- Every preview/review artifact must expose both Arabic and English states.
- Arabic is not a mirrored afterthought; it receives independent typography, spacing, direction, mixed-content and responsive QA.

## Positioning

ORIGEX is a premium Arabic-first bilingual HTML template for B2B food trading, import-export, wholesale, distribution, manufacturers and suppliers.

The visual language must communicate:

- source and origin
- trade routes and movement
- market access
- supply-chain confidence
- product credibility
- international B2B professionalism

It must not resemble a restaurant, grocery shop, organic farm, or generic blue corporate template.

## Logo Direction — Origin Route Mark

The ORIGEX mark combines three ideas:

1. **O / Origin** — the outer circular form represents source and origin.
2. **Route** — a diagonal route moves from source to destination.
3. **X / Exchange** — intersecting route geometry creates a subtle X reference to export, exchange and ORIGEX.

Rules:

- geometric, simple, SVG-first
- must survive monochrome use
- no wheat, fork, spoon, shopping cart, globe cliché, or literal shipping container
- the symbol may appear independently as favicon/app mark
- the public wordmark is ORIGEX; Arabic أوريجكس is a supporting language lockup, not a separate logo identity

## Core Palette

| Token | Hex | Role |
|---|---|---|
| Trade Ink | `#15343B` | Primary brand / headings / dark surfaces |
| Deep Ink | `#0D252B` | Strong primary / footer / high contrast |
| Route Teal | `#3F6F68` | Secondary / supporting states |
| Origin Copper | `#C47A4A` | Accent / route nodes / selective CTA emphasis |
| Warm Sand | `#E8DFD0` | Soft warm neutral / editorial surfaces |
| Paper | `#FAF8F4` | Main background |
| Surface | `#FFFFFF` | Cards / controls |
| Graphite | `#20282C` | Body text |
| Muted | `#667278` | Secondary text |
| Border | `#D8DEDB` | Borders / dividers |

Semantic colors are functional only and must not compete with the brand palette.

## Typography

### Arabic — Primary

**Tajawal**

Approved hierarchy:

- 800 — display / hero emphasis
- 700 — H1/H2 and strong headings
- 600 — H3/H4 and strong UI
- 500 — labels / navigation / controls
- 400 — body copy

Arabic line-height is intentionally more generous than English to protect readability and visual rhythm.

### English — Secondary

**Manrope**

Approved hierarchy:

- 800 — display / hero emphasis
- 700 — H1/H2 and strong headings
- 600 — H3/H4 and strong UI
- 500 — labels / navigation / controls
- 400 — body copy

Canonical family, size, weight and line-height variables live in `assets/css/tokens.css`.

### Packaging Note

Typography is approved as the visual direction. Final downloadable font-file redistribution remains subject to the asset/license registry. Until that audit is closed, development may use safe web-loading or system fallbacks and must not embed unverified font binaries in the commercial ZIP.

## Icon Direction

- outline icons
- consistent optical stroke
- rounded joins where possible
- directional icons must mirror correctly in RTL
- no mixed icon families on the same page
- icons support hierarchy; they do not decorate every text block

## Image Direction

Use editorial B2B imagery focused on:

- manufacturing and packing
- products in trade context
- pallets / cartons / warehouse selectively
- supplier meetings and product review
- distribution and market channels
- origin / sourcing / export context

Avoid:

- restaurant plated-food hero clichés
- excessive produce flat-lays
- generic handshakes
- fake logistics dashboards
- imagery containing client-owned TARGET assets

## Visual Personality

**Premium Trade / Origin / Market Access**

- medium-low corner radius; avoid overly soft SaaS cards
- restrained shadows; borders and surface contrast do most structural work
- strong whitespace and editorial spacing
- high information clarity on product and supplier pages
- subtle motion only; reduced-motion support is mandatory
- Arabic layouts are designed intentionally, not mechanically mirrored after completion

## Preview Rule

Preview infrastructure is review-only and must remain isolated from the production package.

Every preview must provide:

- Arabic as the default state
- English as the secondary state
- a raw page view
- a framed responsive QA view using the common-screen matrix

The preview frame is removed/excluded from the final production/marketplace package.

## Ownership Layer

ORVEAX remains the author, product owner and copyright owner of ORX-P01 / ORIGEX source product.

Required in source package:

- ORVEAX copyright headers in principal source files
- product ID `ORX-P01`
- semantic version
- README / changelog / credits / license notice

Buyer-facing website footer credit to ORVEAX is optional/removable; ownership protection belongs in the product source, documentation and marketplace authorship rather than a forced public footer credit.
