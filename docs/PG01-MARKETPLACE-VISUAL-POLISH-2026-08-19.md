# ORIGEX — PG01 Marketplace Visual Polish

Product ID: ORX-P01  
Page ID: PG01 — Home 01 — Food Trading / Importer  
Milestone: M2 — Global Shell & Home Family  
Change Type: **APPROVED COMMERCIAL / VISUAL POLISH CHANGE REQUEST**  
Date: 2026-08-19

## Decision

PG01 was already C8 / PASS from the page/code QA gate. It was reopened only for an approved marketplace-quality visual refinement before it becomes the visual benchmark for the rest of the Home family.

This change does **not** reopen M1, change the content architecture, add plugins, alter Bootstrap, or introduce a new runtime dependency.

## Approved Scope

1. Strengthen the split Hero with a B2B trade/logistics visual anchor.
2. Replace pattern-only product placeholders with distributable ORVEAX-owned demo packshots.
3. Improve category-card visual differentiation without stock photography.
4. Improve the trust layer as decision-support information rather than repetitive cards.
5. Create a stronger tonal break for role-based journeys.
6. Refine the supplier CTA surface.
7. Preserve Arabic RTL / English LTR parity and the existing Content/SEO contract.

## Implementation

### Reusable CSS Layer

- `assets/css/origex-marketplace-polish.css`
- loaded after the M2 compositions layer through `assets/css/origex-shell.css`.

The polish layer is scoped to existing semantic section identities and reuses the frozen ORIGEX token system. It does not override Bootstrap as a visual identity or create a parallel design system.

### ORVEAX-Owned Demo Media

- `assets/media/demo/hero-trade-scene.svg`
- `assets/media/demo/product-tomato-sauce.svg`
- `assets/media/demo/product-hibiscus.svg`
- `assets/media/demo/product-milk.svg`
- `assets/media/demo/product-frozen.svg`

These are fictional generic vector compositions created for ORIGEX. They contain no TARGET assets, no third-party brands, no supplier packaging, no people/release risk and no stock-photo dependency.

All five assets are registered in `docs/ASSET-LICENSE-REGISTER-V1.md` as **ORVEAX OWNED**.

## Visual Changes

### Hero

- B2B warehouse / cargo / route scene becomes the visual anchor behind the existing Origin → Route → Market composition.
- Existing information cards remain readable using translucent surfaces and the same component hierarchy.
- No new JavaScript.

### Trust Layer

- five decision inputs retain the same content but receive restrained accent coding and clearer visual separation.
- the section remains information-first rather than metric/claim-heavy.

### Process

- the four-step route receives a stronger sequence cue and top progress accent while preserving the current markup and copy.

### Product Categories

- six category cards receive distinct token-based visual headers and elevated icon treatment.
- no stock imagery is introduced.

### Role-Based Journeys

- the section becomes a dark tonal break using the primary ORIGEX surface, with light cards retained for readability.

### Featured Products

- pattern-only media is replaced visually by four ORVEAX-owned fictional packshots.
- cards use a 4:3 media ratio on larger screens and a 16:10 ratio on small screens to reduce excessive vertical length.

### Supplier CTA

- the CTA gains a restrained network/ring composition with no extra assets or runtime cost.

## Key Commits

- Hero media: `97142bfcbed77a8b80533401bf3f380f8ee58e24`
- Tomato packshot: `abbac24010ae9dc51d164e7e624f6530b0941a9b`
- Hibiscus packshot: `e752e4e183998b62fa778e5a11c2796981d54e83`
- Milk packshot: `89bedf2f9f5a17878a9fd753bbb08829c2f0b33e`
- Frozen packshot: `6cb0e366ea37f465db27aad3dd6703b807076023`
- Marketplace polish CSS: `616b88b33b0fb0bd6eb3532466eba5d069d9fb23`
- Shared shell loading: `2c33a597121b8b7b5d188a52c187ba53142110b8`
- Asset register: `565269fc961e9ad362965d1abd03570899e973ff`
- Visual review rerun trigger: `f605af320cd598eea5bbe94b8181e89f0dedb7e7`
- Updated visual snapshot evidence: `0c2c3a931c790707f7bf70d46677c45ce941777a`

## Visual Evidence

`qa/pg01-visual-review/` was regenerated after the polish. The new snapshot commit updates AR/EN Mobile and Desktop screenshots. Full-page JPEG output sizes increased materially because product/vector media is now present, confirming the browser-rendered output changed.

This snapshot evidence is a visual-review aid, not by itself the complete QA gate.

## QA Gate

PG01 remains in **CHANGE REQUEST QA** until the post-polish reruns confirm:

- rendered responsive matrix: PASS;
- no horizontal overflow: PASS;
- AR RTL / EN LTR: PASS;
- touch target baseline: PASS;
- fonts/runtime: PASS;
- mega menu / Escape: PASS;
- FAQ accordion: PASS;
- announcement dismiss: PASS;
- mobile drawer / Escape / scroll lock: PASS;
- asset/license register: PASS.

After those checks pass, PG01 returns to **C8 / PASS / CLOSED** with this polish as the new M2 visual benchmark.

## Deployment Note

The separate Staging Preview Gate remains BLOCKED until GitHub Pages is enabled in repository Settings → Pages → Source → GitHub Actions. This deployment blocker is independent of the page/code QA state.

Copyright © ORVEAX.
