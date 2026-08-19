# ORIGEX — Implementation Status V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: ACTIVE TRACKER  
Last Updated: 2026-08-19 — M1 CLOSED / M2 ACTIVE / PG01 MARKETPLACE BENCHMARK CLOSED / STAGING BLOCKED

This is the repo-level execution tracker. It records actual current implementation state and must match the active code tree.

## Status Vocabulary

- `NOT STARTED`
- `READY`
- `IN PROGRESS`
- `BLOCKED`
- `QA`
- `PASS / CLOSED`
- `REFERENCE ONLY`

Content uses C0–C8 from `CONTENT-SYSTEM-V1.md`. Deployment readiness uses the separate staging vocabulary from `STAGING-PREVIEW-GATE-V1.md`.

## Project Control

| Control Area | Status |
|---|---|
| Product Foundation | PASS / CLOSED |
| Hard Audit / Legacy Cleanup | PASS / CLOSED |
| Canonical Authority Map | PASS / CLOSED |
| Project Rules | PASS / CLOSED |
| Asset/License Register | ACTIVE — M1 baseline + PG01 ORVEAX-owned demo media verified |
| PG01 Page/Code QA | C8 / PASS / CLOSED — MARKETPLACE VISUAL BENCHMARK |
| PG01 Marketplace Visual Polish CR | PASS / CLOSED |
| PG01 Staging Preview | BLOCKED — GitHub Pages not enabled; Configure Pages failed |
| Current Build Baseline | M2 IN PROGRESS — PG01 benchmark closed; PG02 C0; PG02 code blocked until PG01 STAGING PASS |

## Milestones

| Milestone | Status | Exit Gate |
|---|---|---|
| M0 Product Foundation | PASS / CLOSED | Product Foundation Complete |
| M1 Global System & Component Foundation | PASS / CLOSED | Component AR/EN foundation QA |
| M2 Global Shell & Home Family | IN PROGRESS | Home family + shell QA + first-page staging preview gate |
| M3 Company / Business / Market | NOT STARTED | Batch Page QA |
| M4 Product / Supplier / Conversion | NOT STARTED | Data/forms/conversion QA |
| M5 Proof / Resources / Compliance / Content | NOT STARTED | Resource/content QA |
| M6 Support / Utility | NOT STARTED | All 32 layouts exist AR/EN |
| M7 Full QA & Optimization | NOT STARTED | Zero Critical / High defects |
| M8 Docs / Licensing / Marketplace Package | NOT STARTED | Submission Candidate 1.0.0 |

## M1 Foundation Units — CLOSED

| Unit | Status | Evidence / Notes |
|---|---|---|
| Bootstrap 5.3.8 exact baseline | PASS / CLOSED | exact version authority locked |
| Bootstrap local vendor files | PASS / CLOSED | local LTR/RTL CSS + bundle + MIT notice |
| Asset/license register | PASS / CLOSED | M1 vendor/font/icon/pattern baseline verified; remains living register for future assets |
| Design hierarchy / registry normalization | PASS / CLOSED | F01–F07, P01–P11, C01–C28, S01–S06, N01–N04 |
| Tokens / typography / spacing implementation | PASS / CLOSED | central CSS foundation |
| Grid / containers / responsive helpers | PASS / CLOSED | Bootstrap infrastructure + ORIGEX container decisions |
| Radius / border / elevation implementation | PASS / CLOSED | frozen tokens implemented |
| Motion / reduced-motion implementation | PASS / CLOSED | frozen tokens + accessibility fallback |
| Lucide local icon assets/sprite | PASS / CLOSED | selected 1.27.0 subset + combined license |
| ORIGEX PT01–PT06 pattern assets | PASS / CLOSED | six ORVEAX-owned SVGs |
| Primitive code implementation | PASS / CLOSED | P01–P11 mapped |
| Component code implementation | PASS / CLOSED | C01–C28 mapped centrally |
| Config schema/engine normalization | PASS / CLOSED | canonical demo defaults + eligible hooks |
| Config integration with M1 components | PASS / CLOSED | semantic hook integration |
| Global shell | PASS / CLOSED | N01–N04 foundation implemented; mega-menu positioning context corrected centrally |
| Components / Elements M1 foundation view | PASS / CLOSED | AR + EN noindex QA surfaces |
| M1 AR/EN component QA | PASS / CLOSED | structural/component gate; see `M1-QA-REPORT-V1.md` and `M1-CLOSURE-2026-08-19.md` |

## Active Shared Implementation Tree

```text
index.html                         # staging root / Arabic-first language entry
ar/
└── index.html                     # PG01 AR
en/
└── index.html                     # PG01 EN
assets/
├── brand/
├── css/
│   ├── origex-tokens.css
│   ├── origex-foundation.css
│   ├── origex-components.css
│   ├── origex-compositions.css    # M2 composition entry
│   ├── origex-marketplace-polish.css
│   └── origex-shell.css           # M1 shell remains closed
├── media/demo/
│   ├── hero-trade-scene.svg
│   ├── product-tomato-sauce.svg
│   ├── product-hibiscus.svg
│   ├── product-milk.svg
│   └── product-frozen.svg
├── fonts/
│   ├── tajawal/
│   └── manrope/
├── icons/
│   ├── lucide/
│   └── sprite.svg
├── js/
│   ├── config.js
│   ├── config-engine.js
│   └── origex-ui.js
├── patterns/
│   └── pt01–pt06
└── vendor/
    └── bootstrap/
preview/
├── m1-components-ar.html
└── m1-components-en.html
qa/
├── pg01-rendered/
├── pg01-interaction/
└── pg01-visual-review/
staging/
└── deployment-status.md
.github/workflows/
└── deploy-staging-pages.yml
docs/
├── M1-COMPONENT-IMPLEMENTATION-MAP.md
├── M1-QA-REPORT-V1.md
├── M1-CLOSURE-2026-08-19.md
├── PG01-CLOSURE-2026-08-19.md
├── PG01-MARKETPLACE-VISUAL-POLISH-2026-08-19.md
├── STAGING-PREVIEW-GATE-V1.md
├── M1-VENDOR-SHA256.txt
└── canonical authorities
```

`origex-compositions.css` is the M2 composition layer and loads the marketplace polish layer. `origex-shell.css` remains the closed M1 shell. The visual polish therefore does not reopen M1 or create a competing foundation.

The staging deployment artifact intentionally includes only `index.html`, `ar/`, `en/` and `assets/`. Internal governance, QA evidence and workflow files are not part of the public staging artifact.

## 32 V1 Layouts

| PG | Page | Content | Design Profile | Build | QA |
|---|---|---|---|---|---|
| PG01 | Home 01 — Food Trading / Importer | C8 — CLOSED | APPROVED | `ar/index.html` + `en/index.html` | PASS / CLOSED — MARKETPLACE VISUAL BENCHMARK; STAGING BLOCKED |
| PG02 | Home 02 — Wholesale & Distribution | C0 | NOT STARTED | NOT STARTED — CODE BLOCKED UNTIL PG01 STAGING PASS | NOT STARTED |
| PG03 | Home 03 — Manufacturer / Supplier | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG04 | Landing / One Page | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG05 | About | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG06 | How We Work | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG07 | Capabilities / Services | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG08 | Service Details | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG09 | Product Categories | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG10 | Products Grid | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG11 | Product Details | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG12 | Suppliers / Brands Directory | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG13 | Supplier / Brand Details | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG14 | Market Access | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG15 | Markets / Countries | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG16 | For Suppliers | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG17 | Submit Your Product | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG18 | RFQ / Request a Quote | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG19 | Become Distributor / Partner | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG20 | Case Studies | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG21 | Case Study Details | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG22 | Downloads / Resources | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG23 | Certifications & Compliance | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG24 | Insights / Blog | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG25 | Article Details | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG26 | FAQ | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG27 | Contact | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG28 | 404 | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG29 | Coming Soon / Under Construction | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG30 | Privacy | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG31 | Terms | C0 | NOT STARTED | NOT STARTED | NOT STARTED |
| PG32 | Components / Elements Library | C0 | NOT STARTED | NOT STARTED | NOT STARTED |

## PG01 Closure Evidence

PG01 passed the original page/code gate and the approved marketplace visual polish Change Request on 2026-08-19.

Base closure evidence:
- `docs/PG01-QA-REPORT-V1.md`.
- `docs/PG01-CLOSURE-2026-08-19.md`.

Marketplace benchmark closure:
- `docs/PG01-MARKETPLACE-VISUAL-POLISH-2026-08-19.md`.
- final rendered QA: `5ab1edb6fe2a17adc41857790170097dfad57f0f` — 8/8 AR/EN viewport cases PASS, failures 0.
- final interaction QA: `b3d12beb103492144f4c5fc690ef15eedd49eef4` — AR/EN desktop/mobile PASS, failures 0.
- final visual snapshots: `e1c09173757defc6992ac162447990f2ffc76f5a`.
- asset/license register: new demo media registered as ORVEAX OWNED.

QA found a Hero grid overflow after the first marketplace-polish pass. It was fixed in M2 by removing the inherited Hero aspect-ratio constraint and allowing the media to shrink within its grid column (`c7398a00c0db22ba6617c63958606c1a8b326ba1`). Final rendered QA then returned zero failures.

## Staging Preview Control

Authority: `docs/STAGING-PREVIEW-GATE-V1.md`.

Current state:
- root entry `index.html`: IMPLEMENTED.
- deploy workflow `.github/workflows/deploy-staging-pages.yml`: IMPLEMENTED.
- public artifact preparation: PASS.
- GitHub Pages repository capability: NOT ENABLED (`has_pages: false`).
- first deploy workflow run: Configure Pages FAILED; artifact upload/deploy skipped.
- deployment evidence: `staging/deployment-status.md`.
- page URL: NOT AVAILABLE.
- staging state: **BLOCKED**.

Required one-time remediation:

```text
Repository → Settings → Pages
Build and deployment → Source → GitHub Actions
```

After enablement, rerun `Deploy ORIGEX Staging`, verify root/AR/EN and assets on external mobile + desktop browsers, then mark `STAGING PASS`.

## Historical Build Status

Build 02–05 code remains removed from the active tree because it predates the frozen Bootstrap/component/icon/content/SEO architecture.

Historical value remains in Git history and selected reference/source-map files. It is not current implementation progress and must not be restored as active code.

## Page Production Gate

**M1 PASSED / CLOSED.**  
**PG01 page/code = C8 / PASS / CLOSED — MARKETPLACE VISUAL BENCHMARK.**  
**PG01 staging = BLOCKED.**

PG02 remains at C0. Its Content Contract, Arabic/English content work, Design Profile and SEO Contract may be prepared while staging is blocked. PG02 AR/EN code must not begin until:
- PG02 reaches its normal implementation entry gate; and
- PG01 reaches `STAGING PASS`.

Next execution action: enable GitHub Pages → rerun staging deployment → external root/AR/EN smoke review → STAGING PASS → PG02 implementation entry.

## Update Rule

Update this tracker in the same work unit whenever a milestone, foundation unit, page, or staging/deployment state changes.

Copyright © ORVEAX.
