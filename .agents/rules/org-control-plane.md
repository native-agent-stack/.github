---
trigger: model_decision
description: Enforce Native Agent Stack organization control-plane governance when editing ECOSYSTEM_ORG_MANIFEST.json, docs/adr/*, UPSTREAM.md, orca.yaml, or .github/workflows/*.yml.
---

# Organization Control-Plane Governance Rules

1. **Manifest Invariants:** Preserve `schemaVersion: "4.0.0"` and `repositories.nextEraActiveTier` keys `{".github", "tier0-quant"}` in `ECOSYSTEM_ORG_MANIFEST.json`. Never mutate immutable `archivedLegacyTier` SHAs.
2. **GitHub-Evidenced MADR 4.0 ADRs:** Every `docs/adr/ADR-XXXX-*.md` record must include all 6 required metadata bullets (`Status`, `Date`, `Layer`, `Evidence Grade`, `GitHub Evidence` with `>=1` `https://github.com/owner/repo` URL, `Revisit Trigger`) and all 4 required sections (`## Context and Problem Statement`, `## Decision Outcome`, `## Alternatives Considered`, `## Verification Witness`). Always regenerate `docs/adr/CATALOG.md` (LF line endings) and `adrGovernance` with `python3 scripts/architecture_catalog.py --sync-manifest`.
3. **Supply-Chain & Workflow Hardening:** Pin every external GitHub Action to a 40-char commit SHA, include `step-security/harden-runner` (`egress-policy: audit`), declare top-level `permissions: {}` with job-level `contents: read`, pass workflow inputs strictly via `env:` (never raw `${{ inputs.* }}` inside `run:`), and verify `zizmor --offline .github/workflows/` returns `0` findings.
4. **Zero-Leak & Hygiene Checks:** Keep `UPSTREAM.md` free of retired wrappers, keep `orca.yaml` free of `defaultTabs`, and run `python3 scripts/merge_gate.py`, `python3 -m unittest discover -s tests -v`, and `gitleaks` before committing.
