# ORIGEX — Pattern System V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED & LOCKED  
System: Custom ORIGEX SVG/CSS Pattern Library

## 1. Core Decision

ORIGEX V1 uses a custom pattern system created for the product. Third-party pattern libraries are reference/exploration sources only and are not runtime dependencies and are not shipped as customer-package assets unless separately reviewed and explicitly approved for redistribution.

Reference tools may include Pattern Monster and Haikei for exploration only.

## 2. Pattern Families

### PT01 — Route Lines
Purpose: abstract Origin → Route → Market movement.
Use: selected heroes, market-access sections, conversion areas, logistics storytelling.
Visual language: thin route paths, controlled nodes, directional flow without literal maps.

### PT02 — Trade Grid
Purpose: communicate structure, data, operations and commercial systems.
Use: data/specification sections, resources, compliance, selected utility backgrounds.
Visual language: restrained geometric grid.

### PT03 — Dot Matrix
Purpose: low-noise supporting texture.
Use: hero corners, CTA areas, utility backgrounds, empty-space balancing.
Visual language: consistent optical dot rhythm.

### PT04 — Market Nodes
Purpose: represent suppliers, markets, channels and business relationships.
Use: markets, suppliers, distribution, network-related sections.
Visual language: abstract nodes and links, never a decorative fake network diagram.

### PT05 — Packaging Geometry
Purpose: reference cartons, pallets, packaging and wholesale structure without literal illustration.
Use: product categories, distribution, manufacturer/supplier contexts.
Visual language: modular rectangles/lines derived from packaging geometry.

### PT06 — Flow Lines
Purpose: express logistics movement, continuity and route-to-market flow.
Use: selected home, process and distribution sections.
Visual language: restrained contour/flow lines.

## 3. Pattern Hierarchy & Strategy

Patterns are supporting visual assets, not primary content.

Hierarchy:
Foundation → Pattern Token → Registered Pattern Family → Section Application → Page Design Profile

A page may select an approved PT family but may not invent a new pattern locally.

## 4. Visual Rules

- Default opacity range: approximately 3%–12%, adjusted only when contrast and readability remain strong.
- Patterns use ORIGEX design tokens only.
- No page-specific decorative colors.
- No pattern may reduce text readability or compete with product imagery.
- Pattern density must remain restrained on mobile.
- Patterns must preserve a premium B2B character; avoid playful, food-restaurant or novelty motifs.
- Wheat, forks, chef motifs, generic food doodles and globe clichés are not part of the core ORIGEX pattern language.

## 5. Color Rules

Allowed roles:
- Trade Ink
- Deep Ink
- Route Teal
- Origin Copper
- Warm Sand
- Surface/Soft Surface derived tones

Prefer `currentColor`, CSS variables or tokenized SVG values when practical.

## 6. RTL / LTR Rules

- Non-directional patterns do not mirror merely because the document is RTL.
- Route/flow patterns may have approved RTL/LTR orientation variants only when the visual direction materially supports composition.
- Never use a blanket `scaleX(-1)` on all pattern assets.
- Page Design Profile must state whether a directional pattern uses mirrored, alternate, or identical orientation.

## 7. Responsive Rules

- Pattern density may reduce on smaller screens.
- Decorative nodes/segments may be hidden when they create clutter.
- Patterns must never introduce horizontal overflow.
- Important content order and tap targets always take precedence over decorative pattern visibility.

## 8. Performance Rules

Preferred delivery:
- Inline/local SVG for controlled vector patterns.
- CSS gradients/repeating patterns when simpler and lighter.
- No remote/CDN dependency for core patterns.
- No raster pattern where CSS/SVG can provide the same result cleanly.
- Avoid overly complex SVG paths and excessive DOM nodes.

Planned structure:

```text
assets/patterns/
├── route-lines.svg
├── trade-grid.svg
├── dot-matrix.svg
├── market-nodes.svg
├── packaging-geometry.svg
└── flow-lines.svg
```

## 9. Pattern Usage Contract

Every usage must declare:
- Pattern ID.
- Section/page context.
- Purpose.
- Density: low / medium.
- Token color.
- Opacity.
- RTL/LTR orientation behavior.
- Mobile behavior.

If a required pattern is not in PT01–PT06, stop and review centrally before creating it.

## 10. Components / Elements Library

The buyer-facing Components / Elements page will demonstrate:
- all six pattern families;
- light and dark usage;
- permitted opacity/density examples;
- hero/section examples;
- RTL/LTR orientation behavior;
- CSS/SVG usage examples.

## 11. Licensing Rule

ORIGEX V1 customer-package pattern assets must be ORVEAX/ORIGEX-created assets or assets explicitly cleared for redistribution. Third-party pattern libraries are not copied into the commercial package by default.

Copyright © ORVEAX.