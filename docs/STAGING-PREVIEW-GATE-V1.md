# ORIGEX — Staging Preview Gate V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED CONTROL GATE  
Adopted: 2026-08-19

## Purpose

This gate separates **page implementation/QA closure** from **externally viewable staging readiness**.

A page may be C8 / PASS / CLOSED after its source, content, SEO, responsive, accessibility, runtime, asset and visual QA pass. That status does **not** by itself mean the page is reachable from a public or access-controlled browser URL.

No page may be described as "viewable on staging", "ready for owner browser review", or used as the visual benchmark that authorizes the next coded page until this Staging Preview Gate passes.

## Required Staging Checks

1. A staging deployment target is configured and enabled.
2. Deployment is generated from the canonical `main` branch.
3. The public artifact contains only intended web-delivery files; internal `docs/`, `qa/` and `.github/` content must not be exposed by the staging artifact.
4. Root `/` resolves successfully and provides a valid language entry/default route.
5. Arabic route resolves successfully.
6. English route resolves successfully.
7. CSS, JavaScript, fonts, icons, patterns and brand assets load correctly from the deployed base path.
8. No broken base-path assumptions appear when the site is hosted under a repository/project subpath.
9. Staging indexability is explicitly controlled; default staging posture is `noindex` unless an approved demo/indexing policy says otherwise.
10. External browser smoke check is completed on at least one mobile viewport and one desktop viewport.
11. Arabic RTL and English LTR are both opened through the deployed URL, not only through a local/CI server.
12. Deployment evidence records the source commit, workflow/run status and resulting URL.

## First-Page Benchmark Rule

For each new page family/milestone batch, the first representative page must pass this gate before the next page in that family enters code implementation.

For M2:

```text
PG01 C8 / PAGE QA PASS
        ↓
STAGING PREVIEW GATE
        ↓
Owner / external browser review
        ↓
PG02 code implementation may begin
```

PG02 content/design/SEO preparation may continue while staging is blocked, but PG02 code must not begin until the PG01 staging preview gate passes.

## Current ORX-P01 State — 2026-08-19

- PG01 page/code QA: **C8 / PASS / CLOSED**.
- Root entry: added at `/index.html`; Arabic-first fallback routes to `./ar/` and provides AR/EN links.
- Deployment workflow: `.github/workflows/deploy-staging-pages.yml`.
- Public artifact scope: `index.html`, `ar/`, `en/`, `assets/` only.
- Deployment evidence: `staging/deployment-status.md`.
- GitHub repository Pages capability: **not enabled** at the time of the first deployment attempt.
- First deployment run: prepare PASS; Configure Pages FAIL; upload/deploy skipped; no page URL generated.
- Deployment state: **BLOCKED — ONE-TIME GITHUB PAGES ENABLEMENT REQUIRED**.

## GitHub Pages Enablement

Repository administrators must configure:

```text
Repository → Settings → Pages
Build and deployment → Source → GitHub Actions
```

After that one-time repository setting is enabled, rerun `Deploy ORIGEX Staging`.

Expected project-site staging base URL after successful GitHub Pages activation:

```text
https://orveax.github.io/TARGET-HTML-Edition/
```

The deployment workflow output remains the final authority for the actual generated URL.

## Status Vocabulary

- `NOT CONFIGURED`
- `BLOCKED`
- `DEPLOYING`
- `STAGING PASS`
- `STAGING REGRESSION`

Do not map these states onto C0–C8; deployment readiness and content/page QA are separate control dimensions.

Copyright © ORVEAX.
