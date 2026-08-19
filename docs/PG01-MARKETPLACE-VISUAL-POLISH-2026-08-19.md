# ORIGEX — PG01 Marketplace Visual Polish

Product ID: ORX-P01  
Page ID: PG01 — Home 01 — Food Trading / Importer  
Milestone: M2 — Global Shell & Home Family  
Change Type: **APPROVED COMMERCIAL / VISUAL POLISH CHANGE REQUEST**  
Date: 2026-08-19  
Final Result: **PASS / CLOSED — MARKETPLACE VISUAL BENCHMARK**

## Decision

PG01 was already C8 / PASS from the page/code QA gate. It was reopened only for an approved marketplace-quality visual refinement before becoming the visual benchmark for the rest of the Home family.

This change did **not** reopen M1, change the content architecture, add plugins, alter Bootstrap, or introduce a new runtime dependency.

## Approved Scope

1. Strengthen the split Hero with a B2B trade/logistics visual anchor.
2. Replace pattern-only product placeholders with distributable ORVEAX-owned demo packshots.
3. Improve category-card visual differentiation without stock photography.
4. Improve the trust layer as decision-support information rather than repetitive cards.
5. Create a stronger tonal break for role-based journeys.
6. Refine the supplier CTA surface.
7. Preserve Arabic RTL / English LTR parity and the existing Content/SEO contract.

## Implementation

### Reusable M2 CSS Layer

- `assets/css/origex-marketplace-polish.css`
- loaded by `assets/css/origex-compositions.css`.
- `assets/css/origex-shell.css` remains the closed M1 shell and imports only the M2 compositions layer.

This preserves the lifecycle boundary: M1 remains closed while M2 owns the commercial page-composition refinement.

### ORVEAX-Owned Demo Media

- `assets/media/demo/hero-trade-scene.svg`
- `assets/media/demo/product-tomato-sauce.svg`
- `assets/media/demo/product-hibiscus.svg`
- `assets/media/demo/product-milk.svg`
- `assets/media/demo/product-frozen.svg`

These are fictional generic vector compositions created for ORIGEX. They contain no TARGET assets, third-party brands, supplier packaging, people/release risk, or stock-photo dependency.

All five assets are registered in `docs/ASSET-LICENSE-REGISTER-V1.md` as **ORVEAX OWNED**.

## Visual Changes

### Hero

- B2B warehouse / cargo / route scene is the visual anchor behind the Origin → Route → Market composition.
- translucent route cards preserve information readability.
- no new JavaScript.

### Trust Layer

- the five decision inputs retain the same content with restrained accent coding and clearer separation.

### Process

- the four-step route receives a stronger sequence cue and progress accent.

### Product Categories

- six category cards receive distinct token-based visual headers and elevated icon treatment.

### Role-Based Journeys

- the section becomes a dark tonal break using the primary ORIGEX surface, with light cards retained for readability.

### Featured Products

- four pattern-only placeholders are replaced visually by ORVEAX-owned fictional packshots.
- media uses 4:3 on larger screens and 16:10 on small screens.

### Supplier CTA

- the CTA gains a restrained network/ring composition with no extra dependency.

## Defect Found During QA

The first post-polish rendered gate detected four Laptop/Desktop failures. Root cause: the new Hero `min-block-size` combined with the inherited `aspect-ratio: 3/2`, forcing the media box wider than its CSS grid column.

Resolution in M2 only:
- `inline-size: 100%`;
- `min-inline-size: 0`;
- `aspect-ratio: auto`;
- retained responsive block-size behavior.

Fix commit: `c7398a00c0db22ba6617c63958606c1a8b326ba1`.

M1 was not reopened.

## Key Commits

- Hero media: `97142bfcbed77a8b80533401bf3f380f8ee58e24`
- Tomato packshot: `abbac24010ae9dc51d164e7e624f6530b0941a9b`
- Hibiscus packshot: `e752e4e183998b62fa778e5a11c2796981d54e83`
- Milk packshot: `89bedf2f9f5a17878a9fd753bbb08829c2f0b33e`
- Frozen packshot: `6cb0e366ea37f465db27aad3dd6703b807076023`
- Marketplace polish CSS: `616b88b33b0fb0bd6eb3532466eba5d069d9fb23`
- Asset register: `565269fc961e9ad362965d1abd03570899e973ff`
- M1/M2 boundary correction: `9999dcd3a153202da1ebcf56090aaacefbad4810` + `63afdcdfeabaa6efa8634ed895ecab955b8b014d`
- Hero overflow defect fix: `c7398a00c0db22ba6617c63958606c1a8b326ba1`
- Final rendered QA evidence: `5ab1edb6fe2a17adc41857790170097dfad57f0f`
- Final visual benchmark snapshots: `e1c09173757defc6992ac162447990f2ffc76f5a`
- Final interaction QA evidence: `b3d12beb103492144f4c5fc690ef15eedd49eef4`

## Final QA — PASS

### Rendered Responsive Gate

Evidence: `qa/pg01-rendered/report.json` generated `2026-08-19T04:15:00Z`.

Result: **8/8 viewport/language cases PASS — failures: 0**.

Validated:
- AR 390 / 820 / 1366 / 1536.
- EN 390 / 820 / 1366 / 1536.
- correct RTL/LTR direction.
- no horizontal overflow or offscreen layout defect.
- touch-target baseline.
- readable Hero.
- local fonts loaded.

### Runtime Interaction Gate

Evidence: `qa/pg01-interaction/report.json` generated `2026-08-19T04:18:36Z`.

Result: **AR Desktop + AR Mobile + EN Desktop + EN Mobile PASS — failures: 0**.

Validated:
- mega menu open + Escape close.
- FAQ toggle.
- announcement dismiss.
- mobile drawer open + Escape close.

### Visual Benchmark Evidence

`qa/pg01-visual-review/` was regenerated after the overflow fix.

Final snapshot commit: `e1c09173757defc6992ac162447990f2ffc76f5a`.

### Asset / License Gate

PASS. All new demo media is ORVEAX-owned and registered. No stock image, third-party product packaging, trademark, client asset or external runtime dependency was introduced.

## Closure Decision

**PG01 Marketplace Visual Polish Change Request = PASS / CLOSED.**

PG01 returns to:

> **C8 / PASS / CLOSED — MARKETPLACE VISUAL BENCHMARK**

This is now the reference quality level for subsequent ORIGEX Home layouts, while page-specific compositions must still be designed for their own user/commercial intent rather than cloned blindly.

## Deployment Note

The separate Staging Preview Gate remains **BLOCKED** until GitHub Pages is enabled in repository Settings → Pages → Source → GitHub Actions. This deployment blocker is independent of the page/code QA closure.

Copyright © ORVEAX.
