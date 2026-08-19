# ORIGEX — Staging Preview Gate V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED CONTROL GATE  
Adopted: 2026-08-19  
Runtime: **Cloudflare Test Environment**

## Purpose

This gate separates page implementation/QA from deployed browser review.

ORIGEX uses this deployment model:

```text
GitHub `main`
    ↓
Cloudflare Git Integration / Test Environment
    ↓
Cloudflare test domain
```

GitHub is the canonical source remote. Cloudflare is the intended test/deployment runtime.

GitHub Pages is **not** part of the ORIGEX deployment architecture.

## Required Staging Checks

1. Cloudflare test deployment target is configured and reachable.
2. Deployment source is the canonical GitHub repository `orveax/TARGET-HTML-Edition`.
3. Production/test branch mapping uses `main` unless ORVEAX explicitly changes it.
4. Root `/` resolves successfully.
5. Arabic route resolves successfully.
6. English route resolves successfully.
7. CSS, JavaScript, fonts, icons, patterns and media load correctly from Cloudflare.
8. No broken relative/base-path assumptions appear in the deployed environment.
9. Test-environment indexability is controlled appropriately.
10. External browser smoke review is completed on mobile and desktop.
11. Arabic RTL and English LTR are reviewed through the deployed Cloudflare URL.
12. The deployed revision is traceable to a Git commit.

## Deployment Automation vs Preview Availability

These are separate controls.

### Preview Availability
A Cloudflare deployment may be valid even when a deployment is started manually with **Rebuild**.

### Auto-Deploy Automation
Preferred operating mode:

```text
push to GitHub `main`
    ↓
Cloudflare detects commit
    ↓
automatic build/deploy
```

Failure of the Git push trigger is an operational automation issue. It does not invalidate page code or prevent development if the Cloudflare Test Environment can still deploy the current `main` revision through Manual Rebuild.

## Current ORX-P01 State — 2026-08-19

Confirmed by ORVEAX administrator:
- Cloudflare Test Environment exists.
- The deployed site works when **Rebuild** is triggered manually.
- GitHub `main` is receiving ORIGEX commits correctly.
- Current issue: Cloudflare is **not automatically starting a deployment after each push to `main`**.
- Manual Rebuild remains functional.
- Auto-deploy diagnosis/correction is explicitly deferred to the next work session.

Current control states:

```text
Cloudflare Test Environment: AVAILABLE VIA MANUAL REBUILD
Cloudflare Auto-Deploy Trigger: DEFERRED / NEEDS CORRECTION
GitHub Pages: NOT USED
```

The exact Cloudflare test URL is managed in the deployment environment and should be added to canonical documentation when confirmed explicitly.

## Page-Family Rule

The first representative page in a family should be viewed in the actual Cloudflare Test Environment before that family is considered visually validated.

Manual Rebuild is an acceptable temporary deployment path while auto-deploy is being repaired.

Therefore, auto-deploy failure alone does **not** block PG02 implementation. PG02 closure still requires its current source revision to be deployed to Cloudflare and smoke-reviewed before final acceptance.

## Status Vocabulary

Preview state:
- `NOT CONFIGURED`
- `AVAILABLE — MANUAL DEPLOY`
- `DEPLOYING`
- `STAGING PASS`
- `STAGING REGRESSION`

Automation state:
- `AUTO-DEPLOY PASS`
- `AUTO-DEPLOY DEGRADED`
- `AUTO-DEPLOY DEFERRED`

Do not map deployment states onto C0–C8; deployment readiness and page/content QA are separate control dimensions.

## Deferred Operational Item

Next Cloudflare session should verify:
- connected repository = `orveax/TARGET-HTML-Edition`;
- branch = `main`;
- automatic deployments enabled;
- build watch paths do not exclude normal ORIGEX changes;
- latest GitHub commit is detected automatically;
- one test commit produces a Cloudflare deployment without manual Rebuild.

Copyright © ORVEAX.
