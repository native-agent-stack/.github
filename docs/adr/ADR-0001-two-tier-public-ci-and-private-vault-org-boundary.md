# ADR-0001: Two-Tier Public Unlimited-CI vs Private Vault Organization Boundary

- **Status:** Accepted
- **Date:** 2026-11-17
- **Layer:** Org Governance (`L0–L12` × `P0–P5`)
- **Evidence Grade:** E4 (Live GitHub Org API & CI Enforced)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/step-security/harden-runner
- **Revisit Trigger:** 2027-01-01 or any GitHub Free Org Actions billing/visibility policy change

## Context and Problem Statement

Fragmenting repositories across personal namespaces and private-only tiers either exhausts private GitHub Actions minutes or risks exposing proprietary strategy weights, paper execution manifests, and local machine paths if pushed publicly without a strict boundary.

## Decision Outcome

1. **Public Open-Core & Workflow Tier (Unlimited Free GitHub Actions):** Host zero-secret, path-sanitized harnesses, multi-model workflow DAGs, upstream SHA locks, and MADR 4.0 validators (`native-agent-stack/.github`, `sota-multi-model-workflows`, `sota-compounding-lab`, `sota-harness-foundation`, `sota-upstream-shelf-lock`, `agy-sota-harness`, `dsh-sota-harness`) as `PUBLIC` repositories running SHA-pinned GitHub Actions on every push and pull request.
2. **Private Execution & Continuity Vault Tier (`0` Private Actions Burn):** Host proprietary live radar weights, `24/5` trailing engines, and scrubbed empirical manifests (`sota-mover-ranker`, `sota-dynamic-trail-c`, `cc-sota-harness`, `sota-private-vault`, `ecosystem-records`) as `PRIVATE` repositories gated locally by `scripts/merge_gate.py` and `gitleaks`.

## Alternatives Considered

1. **All-Private Organization:** Rejected — caps monthly GitHub Actions minutes on Free org plans and blocks continuous multi-OS CI fuzzing.
2. **All-Public Organization:** Rejected — exposes proprietary calibrated alpha factors and live paper execution telemetry.

## Verification Witness

- `python3 scripts/architecture_catalog.py --check` -> `6 GitHub-evidenced ADRs valid, 0 drift`
- `python3 scripts/merge_gate.py` -> `PASS (0 secret, account-ID, or home-path leaks)`
