# ORIGEX — Route 3 Premium Mark | Brand Production Specification V1

**Product:** ORIGEX / ORX-P01  
**Owner:** ORVEAX  
**Marketplace:** ThemeForest  
**Decision:** Route 3 — Premium Mark APPROVED  
**Production status:** Identity assets V1 implemented; website integration remains gated.

## 1. Brand role

ORIGEX is a premium Arabic-first bilingual B2B HTML template for food trading, import, wholesale, distribution, manufacturers, suppliers and market-access workflows.

**Positioning:** From source to market, through a clearer commercial route.  
**Arabic:** من المصدر إلى السوق، بمسار تجاري أوضح.

## 2. Route 3 creative principle

The identity must communicate three ideas in one controlled mark:

1. **Global market** — simplified globe structure.
2. **Source-to-market movement** — one continuous commercial route.
3. **Opportunity / progress** — upward directional arrow at the route exit.

The mark must remain premium, structured, B2B and commercially credible. It must not become a generic logistics icon, delivery badge, shopping symbol or consumer-food mark.

## 3. Symbol construction

**Canonical asset:** `assets/brand/origex-mark.svg`

- Base artboard: 64 × 64.
- Outer globe diameter: 46 units.
- Primary structural stroke: 4.5 units.
- Secondary globe geometry: 2–2.2 units.
- Route stroke: 4.4 units.
- Route begins at a copper origin node in the lower-left quadrant.
- Route travels through the globe and exits toward the upper-right.
- Arrow is integrated into the route, not added as a detached icon.
- Internal globe detail remains subordinate to the route.

## 4. Logo system

| Asset | Purpose |
|---|---|
| `origex-mark.svg` | Primary full-color symbol |
| `origex-mark-mono.svg` | One-color / CSS-currentColor mark |
| `origex-logo.svg` | Primary English horizontal lockup |
| `origex-logo-light.svg` | Dark-background horizontal lockup |
| `origex-logo-ar.svg` | Arabic-facing lockup |
| `origex-logo-bilingual.svg` | Arabic + English combined lockup |
| `origex-brand-field.svg` | Reusable low-contrast brand background |

### Primary wordmark
- English wordmark: **ORIGEX**.
- Typeface basis: Manrope ExtraBold / 800.
- Letter spacing: controlled positive tracking for a premium technical feel.
- `BY ORVEAX` is a small author provenance device and must remain visually secondary.

### Arabic-facing wordmark
- Arabic form: **أوريجكس**.
- Typeface basis: Tajawal ExtraBold / 800.
- Arabic descriptor: **من المصدر إلى السوق، بمسار تجاري أوضح**.
- Do not force Latin tracking behavior onto Arabic lettering.

## 5. Color system

The Route 3 identity inherits the frozen ORIGEX design tokens; no parallel palette is introduced.

| Token | Role | Hex |
|---|---|---|
| Trade Ink | Primary identity | `#15343B` |
| Deep Ink | Maximum contrast / dark surfaces | `#0D252B` |
| Route Teal | Secondary globe / supporting UI | `#3F6F68` |
| Origin Copper | Route, node, directional accent | `#C47A4A` |
| Warm Sand | Light supporting accent | `#E8DFD0` |
| Base | Main light background | `#FAF8F4` |
| Surface | Cards / neutral surface | `#FFFFFF` |

### Color governance
- Copper is an accent, not a large-area brand fill.
- The globe structure should normally use Trade Ink / Deep Ink.
- Route Teal may support secondary globe geometry or system patterns.
- Light logo uses Warm Base / Sand with Copper route accent.
- No gradients are required for the core identity.

## 6. Typography

- Arabic: **Tajawal**.
- English: **Manrope**.
- Logo files reference the same font families already distributed within the template.
- Body typography remains governed by the ORIGEX design system; this specification does not fork typography tokens.

## 7. Clear space and minimum size

### Clear space
Use the origin-node diameter as the minimum exclusion unit **x**.

- Mark-only clear space: minimum `2x` around all sides.
- Horizontal logo clear space: minimum `2x` around the mark and wordmark boundary.
- Do not place route patterns directly behind the logo when contrast drops below a clean reading threshold.

### Minimum digital size
- Mark only: 24 px minimum; 32 px preferred.
- Horizontal logo: 132 px minimum width; 160 px preferred.
- Bilingual lockup: 220 px minimum width.

## 8. Background and pattern behavior

`origex-brand-field.svg` is the primary website identity field.

Rules:
- Use at low opacity only.
- Keep route lines thin and visually secondary to content.
- Copper nodes may be used sparingly as navigation or journey cues.
- Large mark watermark should remain below approximately 8% visual opacity on light surfaces.
- Existing PT01–PT06 remain valid. Route 3 does not replace them; it becomes the brand-level identity layer above the pattern system.

## 9. Bilingual behavior

- Arabic page layouts remain RTL and Arabic-first.
- English page layouts remain LTR.
- The symbol never mirrors in RTL; the source-to-market arrow remains upward/rightward as a fixed brand asset.
- Horizontal lockups may reposition the symbol according to the prepared Arabic/English asset; do not CSS-mirror the SVG.
- Use the bilingual lockup only when both languages need equal brand presence in the same visual frame.

## 10. Contrast and accessibility

- Primary dark logo on `#FAF8F4` / white surfaces.
- Light logo on `#0D252B` or similarly dark approved surfaces.
- Avoid placing Copper wordmarks on Warm Sand or low-contrast photography.
- Do not use opacity on the main logo below normal readable contrast.
- Decorative brand fields must never carry semantic information.

## 11. Prohibited modifications

Do not:
- rotate or mirror the mark;
- detach or reposition the route arrow;
- recolor with arbitrary template colors;
- stretch the globe into an ellipse;
- replace the typography ad hoc;
- add shadows, bevels, 3D effects or gradients to the master logo;
- use the mark as a food, delivery or ecommerce cart icon;
- merge the mark with third-party supplier logos.

## 12. Website integration gate

The new Route 3 assets may exist in the repository before runtime integration. Runtime replacement is allowed only after this production specification and visual QA are accepted.

Integration targets after acceptance:
- Global navigation / header brand.
- Footer brand.
- Favicon / compact mark surfaces.
- Hero and high-value brand fields where appropriate.
- Component and documentation previews.

No page-local logo substitutions are permitted.

## 13. Acceptance criteria

Route 3 V1 passes when:
- primary, light, Arabic-facing, bilingual and monochrome assets render without clipping;
- mark remains legible at 24–32 px;
- Arabic/English lockups render correctly with local Tajawal/Manrope;
- light/dark contrast passes visual review;
- background field stays subordinate to content;
- no client/TARGET assets or third-party marks are present;
- licensing provenance remains ORVEAX-owned;
- website integration occurs centrally, not page-by-page.

## 14. Current execution record

Implemented on `main` on 2026-08-19 as the first Route 3 production identity pass. This replaces the earlier temporary circular-X sample mark as the canonical asset candidate. Runtime synchronization remains the next controlled gate.
