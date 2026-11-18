# ADR-0006: Least-Privilege SHA-Pinned GitHub Actions & Reusable Org Gate

- **Status:** Accepted
- **Date:** 2026-11-17
- **Layer:** CI/CD & Supply-Chain Security (`L9`)
- **Evidence Grade:** E4 (Live GitHub Actions Verified)
- **GitHub Evidence:** https://github.com/step-security/harden-runner, https://github.com/actions/checkout, https://github.com/gitleaks/gitleaks
- **Revisit Trigger:** 2027-01-01 or upstream action security advisory

## Context and Problem Statement

Mutable action tags (`@v4`, `@main`) and default write-scoped `GITHUB_TOKEN` permissions expose public CI workflows to supply-chain tag hijacking and credential exfiltration.

## Decision Outcome

1. **40-Char Commit-SHA Pinning & Empty Default Permissions:** Pin all third-party GitHub Actions to immutable 40-character commit SHAs (`step-security/harden-runner@e14015d583714f6e62063499dc959a02595150a1`, `actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1`), set top-level `permissions: {}`, and disable credential persistence (`persist-credentials: false`).
2. **Reusable Org Gate (`reusable-sota-gate.yml`):** Centralize MADR 4.0 catalog verification, secret/home-path regex tripwires, and test execution in `native-agent-stack/.github` so every public repository inherits identical fail-closed checks.

## Alternatives Considered

1. **Floating major-version tags (`actions/checkout@v4`):** Rejected — vulnerable to upstream tag mutation.

## Verification Witness

- `python3 scripts/merge_gate.py` -> `PASS (all workflow uses: lines 40-char SHA pinned)`
