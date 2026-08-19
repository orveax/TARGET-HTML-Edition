# ORIGEX — Release & Versioning Policy V1

Product ID: ORX-P01  
Owner: ORVEAX  
Status: APPROVED & LOCKED  
Approval Date: 2026-08-19

This document governs ORIGEX product releases after the first submission candidate.

## 1. Version Format

ORIGEX uses semantic-style version numbers:

```text
MAJOR.MINOR.PATCH
```

Example:
```text
1.0.0
1.0.1
1.1.0
2.0.0
```

## 2. Release Classes

### PATCH — x.y.Z
Use for backward-compatible corrections that do not introduce a new product feature family.

Examples:
- bug fixes.
- RTL/LTR corrections.
- accessibility fixes.
- responsive fixes.
- browser compatibility fixes.
- performance improvements.
- documentation corrections.
- small content corrections.
- security/safety fixes without architectural change.

Example: `1.0.0 → 1.0.1`.

### MINOR — x.Y.0
Use for backward-compatible product expansion.

Examples:
- approved V1.1 Additional Features.
- new reusable components/variants approved through governance.
- new page layout that does not fundamentally change product architecture.
- new documented configuration capability.
- new demo/data capability compatible with existing buyer structure.

Example: `1.0.0 → 1.1.0`.

### MAJOR — X.0.0
Use when buyer-facing compatibility or core product architecture changes materially.

Examples:
- primary framework/runtime replacement.
- breaking file structure changes.
- breaking configuration schema.
- removal/renaming of core public components without compatibility path.
- major page architecture change requiring buyer migration.

Example: `1.x → 2.0.0`.

## 3. Pre-1.0 Milestone Labels

Before the first approved public release, internal work uses milestone/build status rather than pretending incomplete builds are market releases.

Examples:
- M1 Foundation Implementation
- M2 Home Family
- Submission Candidate 1.0.0

The first market-ready approved package becomes `1.0.0`.

## 4. Changelog Requirement

Every public package release must update `CHANGELOG.md` with:

```text
Version
Release Date
Added
Changed
Fixed
Deprecated
Removed
Security
Migration Notes (when applicable)
```

Empty categories may be omitted.

## 5. Release Gate

A version may be published only when:
- applicable milestone/QA gates pass.
- zero Critical defects.
- zero High defects for Submission Candidate/public release.
- changed assets/licenses are reviewed.
- documentation matches the shipped package.
- demo and buyer package are synchronized where required.
- version number is updated consistently in package metadata/docs.
- changelog is updated.

## 6. V1.1 Backlog Rule

Deferred Additional Features do not change V1 scope by merely existing in the backlog.

When selected for implementation after V1, they are grouped into a defined MINOR release plan, normally beginning with `1.1.0`, unless the actual change is breaking and therefore requires MAJOR review.

## 7. Deprecation

When a buyer-facing component/configuration pattern must eventually be replaced:
- document the replacement.
- keep compatibility where practical for at least the current minor line.
- mark deprecation in changelog/documentation before removal.
- removal that breaks existing buyer customization normally requires a MAJOR release.

## 8. Hotfixes

Urgent critical production/package defects may be released as PATCH versions after focused QA. Hotfix status does not bypass documentation, licensing or changelog requirements.

## 9. Source Control Rule

The commercial repository continues to use the approved `main` branch policy unless explicitly changed by ORVEAX governance. Release tags/version packaging are created only from a QA-approved repository state.

## 10. Change Control

Changing the meaning of MAJOR/MINOR/PATCH or the release gate requires a Product Governance Change Request.

Copyright © ORVEAX.