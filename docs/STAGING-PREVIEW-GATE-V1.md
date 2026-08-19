# ORIGEX — Staging Preview Gate V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED CONTROL GATE — R1 ALIGNED  
Adopted: 2026-08-19  
Runtime: **Cloudflare Test Environment**

## Purpose

This gate controls deployed browser acceptance before **PS8 — Final Page Acceptance**.

ORIGEX uses this deployment model:

```text
GitHub `main`
    ↓
Cloudflare Git Integration / Test Environment
    ↓
Cloudflare test domain
```

GitHub is the canonical source remote. Cloudflare is the test/deployment runtime.

GitHub Pages is **not** part of the ORIGEX deployment architecture.

## Canonical Repository

Repository: `orveax/origex-html-template`  
Branch: `main`

Historical references to `orveax/TARGET-HTML-Edition` are superseded and must not be used as the deployment authority.

## Canonical Cloudflare Test URL

`https://origex-html-template.targetftcom.workers.dev/`

This URL was explicitly confirmed by the ORVEAX administrator on 2026-08-19 and is the canonical ORIGEX test-runtime address until changed through deployment control.

## Required Staging Checks Before PS8

1. Cloudflare test deployment target is configured and reachable.
2. Deployment source is `orveax/origex-html-template`.
3. production/test branch mapping uses `main` unless ORVEAX explicitly changes it.
4. root `/` resolves successfully.
5. applicable Arabic routes resolve successfully.
6. applicable English routes resolve successfully.
7. CSS, JavaScript, fonts, icons, patterns, media and structured data files load correctly from Cloudflare.
8. no broken relative/base-path assumptions appear in the deployed environment.
9. test-environment indexability is controlled appropriately.
10. external browser smoke review is completed on representative mobile and desktop viewports.
11. Arabic RTL and English LTR are reviewed through the deployed Cloudflare URL.
12. deployed revision is traceable to a Git commit.

## Deployment Automation vs Preview Availability

These are separate controls.

### Preview Availability

A Cloudflare deployment may be valid when it is started manually with **Rebuild**.

### Auto-Deploy Automation

Preferred operating mode:

```text
push to GitHub `main`
    ↓
Cloudflare detects commit
    ↓
automatic build/deploy
```

Failure of the Git push trigger is an operational automation issue. It does not invalidate valid PS7 page code/CI evidence when Manual Rebuild still deploys the current `main` revision.

## Current ORX-P01 State — 2026-08-19

Confirmed operating state:
- Cloudflare Test Environment exists.
- canonical test URL is `https://origex-html-template.targetftcom.workers.dev/`.
- deployed site works when **Rebuild** is triggered manually.
- GitHub `main` receives ORIGEX commits correctly.
- current issue: Cloudflare does not automatically start a deployment after each push to `main`.
- Manual Rebuild remains functional.
- auto-deploy diagnosis/correction remains deferred to the dedicated infrastructure session.

Current control states:

```text
Cloudflare Test Environment: AVAILABLE VIA MANUAL REBUILD
Cloudflare Test URL: CONFIRMED / RECORDED
Cloudflare External Smoke Verification: PENDING
Cloudflare Auto-Deploy Trigger: DEFERRED / NEEDS CORRECTION
GitHub Pages: NOT USED
```

The assistant-side external runtime check could not resolve the workers.dev host from the available verification environment, so this record confirms the administrator-supplied URL but does not by itself grant `STAGING PASS` or PS8.

## Parallel Page-Production Rule

Cloudflare review is a **PS8/final-acceptance gate**, not a PS7 implementation gate.

Therefore:
- PS6 preparation and PS7 implementation may continue while Cloudflare review is pending.
- Manual Rebuild is acceptable temporarily.
- a page cannot advance from PS7 to PS8 until the applicable deployed Cloudflare checks pass.
- a milestone cannot close while its required Cloudflare acceptance remains pending.

This rule supersedes earlier wording that implied the next page in a family must be code-blocked while the representative staging review was pending.

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

Page stage remains PS0–PS8 and is tracked separately from deployment automation state. PS8, however, requires the applicable deployed-browser acceptance defined by this gate.

## Deferred Operational Item

Next Cloudflare infrastructure session should verify:
- connected repository = `orveax/origex-html-template`;
- branch = `main`;
- automatic deployments enabled;
- build watch paths do not exclude normal ORIGEX changes;
- latest GitHub commit is detected automatically;
- one harmless test commit produces a Cloudflare deployment without Manual Rebuild.

Copyright © ORVEAX.
