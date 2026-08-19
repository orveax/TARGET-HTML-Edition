# ORIGEX — Project Rules V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED & LOCKED  
Effective Date: 2026-08-19

These are the operating rules for implementation after Product Foundation closure.

## R01 — Canonical Authority First
Before editing code, identify the canonical authority that governs the change. Do not implement from memory, old build files, or a superseded document.

## R02 — Main Branch Only
Current project policy: work directly on `main` unless ORVEAX explicitly changes the branch policy.

## R03 — No Legacy Restoration
Deleted pre-foundation HTML/CSS/JS is historical evidence only. Do not restore it into the active tree. Reuse an idea only after translating it into the frozen ORIGEX system.

## R04 — Define Once, Reuse Everywhere
Shared visual/interaction behavior belongs to the Design System and Component Registry.

```text
Bootstrap Infrastructure
→ ORIGEX Tokens
→ Primitives
→ Components
→ Patterns
→ Sections
→ Page Design Profile
```

A page cannot locally fork shared radius, shadow, padding, icon grammar, button anatomy, form anatomy, card anatomy, navigation behavior, or motion language.

## R05 — Page Entry Gate
No page implementation starts until:
- the Page ID and filename are approved;
- its Main Features are in frozen V1 scope;
- Content Status is C6 — FROZEN;
- Page Design Profile is complete;
- required components/variants exist;
- asset/license requirements are known.

## R06 — Arabic Master / English Complete
Arabic is the master commercial copy. English is a professional adaptation with the same facts, promise and CTA intent. AR and EN implementation move in the same page milestone.

## R07 — No Content Inside Code Discovery
Page implementation does not invent copy. Missing copy blocks implementation of that unit until the Content Contract is completed.

## R08 — SEO Is Page Identity
Every page must use its registered:
- PG ID;
- canonical filename/slug;
- H1 intent;
- title/meta description;
- canonical/hreflang contract;
- OG contract;
- indexability class;
- structured-data mapping where applicable.

## R09 — Assets Are Licensed Before Use
No image, font, icon, logo, PDF, illustration, library or third-party asset enters the distributable package unless its source and redistribution status are logged.

Preview-only stock remains preview-only.

## R10 — Bootstrap Boundary
Bootstrap 5.3.8 is infrastructure. ORIGEX owns the branded visual language.

Allowed: grid, containers, responsive utilities and selected behavior primitives when justified.

Not allowed: substituting default Bootstrap cards/buttons/forms/navigation styling for registered ORIGEX components.

## R11 — Icon Boundary
Lucide is the primary semantic icon family. Brand marks are separate. No second semantic icon library may be added for convenience.

## R12 — Static-First
Core content, navigation and page meaning must remain understandable without optional JavaScript. No mandatory build process, SPA runtime, or server dependency is introduced in V1.

## R13 — Config Is Not a CMS
`config.js` controls approved global/repeated settings only. Long editorial content and large page structures stay in HTML; structured repeated business data uses approved JSON schemas.

## R14 — File Naming
- lowercase kebab-case for project files;
- `orx-` prefix for ORIGEX CSS classes;
- `--orx-*` for CSS custom properties;
- `data-orx-*` for JavaScript hooks;
- no `final-final`, `new`, `copy`, `v2-final`, `test2`, or temporary names in the canonical tree.

## R15 — No Hidden Hotfix Layer
A fix must be applied at the correct architecture level. Do not append unexplained CSS overrides or duplicate scripts to make one page pass.

## R16 — RTL/LTR Independently Tested
Do not assume LTR mirroring proves RTL correctness. Arabic and English are independently QA-reviewed for ordering, arrows, mixed-direction data, forms, tables, filters, drawers and responsive composition.

## R17 — Accessibility Is Definition of Done
Keyboard behavior, focus, labels, heading hierarchy, native semantics, ARIA/state sync where needed, contrast and reduced-motion behavior are not optional polish.

## R18 — Performance Is Architecture
No duplicate UI/icon libraries, unnecessary runtime script, oversized raw media or page-specific dependency. Below-fold media is lazy-loaded and dimensions are declared where practical.

## R19 — Demo Is Not Production
Fictional demo data is never presented as a real company claim. Production buyers must replace demo identity/contact/data before deployment.

## R20 — Page Exit Gate
A page closes only after the full `QA-DEFINITION-OF-DONE-V1.md` gate, including Content C8, AR/EN, responsive, accessibility, SEO, assets/licenses, no console errors and documentation updates.

## R21 — Reopen Control
A closed item reopens only for:
- verified defect;
- accessibility/RTL/responsive/performance regression;
- verified factual/SEO correction;
- approved formal change request.

Preference alone does not reopen a closed page.

## R22 — V1.1 Boundary
Additional Features remain deferred. If an Additional Feature is proposed during V1, record it in V1.1 rather than silently implementing it.

## R23 — Documentation Changes With Code
If buyer behavior, configuration, data structure, dependency, component API, file structure or deployment behavior changes, documentation changes in the same unit of work.

## R24 — Implementation Status Is Explicit
Every page/component/milestone has an explicit state in `IMPLEMENTATION-STATUS-V1.md`. “Almost done” is not a status.

## R25 — Source Fidelity Without Client Leakage
TARGET-derived reference material may inform purpose/hierarchy/content density. Client identity, contacts, proprietary data/assets and unsupported claims never enter ORIGEX.

Copyright © ORVEAX.
