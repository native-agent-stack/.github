# ADR-0030: `v3.10.2` `22`-Repo Zero-Drift Seal — Zero-Kimi / Zero-Stale Model Hygiene, IEEE-754 & Bitemporal `DF1..DF12` Hardening, and Full `Noesis` Win32 Doctor Parity

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Organization Control Plane, `22`-Repo 40-Char SHA Manifest, Multi-Model Hygiene & Cross-OS Verification (`L0–L13` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (`22/22` Live 40-Char `origin/main` SHA Parity, `9/9` Public GitHub Actions, `13/13` Private `Actions=false`, `6/6` Full `doctor.py` PASS on `Noesis` Win32, `0` Leaks)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-multi-model-workflows, https://github.com/native-agent-stack/cc-sota-harness, https://github.com/native-agent-stack/sota-harness-foundation, https://github.com/native-agent-stack/dsh-sota-harness, https://github.com/native-agent-stack/sota-private-vault
- **Revisit Trigger:** `2026-12-06` (`23/5` SIP cutover) or next `ALPHA_STRATEGY_MINOR` promotion (`t >= 4.1905`, `DSR >= 0.95`)

## Context and Problem Statement

Seals the `v3.10.2` adversarial verification and model-hygiene wave across all `22` organization repositories:
1. Enforces Owner Directives #1 & #2 (`deepseek-v4.1-flash` / `deepseek-flash` superseding `deepseek-v4-pro`, and complete retirement of `kimi-*` / `Moonshot AI` across active routing, presets, and `UPSTREAM.md` catalogs).
2. Remediates all `noesis-cc-lead` `#68`, `#76`, and `#92` empirical findings (`cc-sota-harness` `ADR-0038` cross-OS Win32 `doctor.py` + truthful platform-scoped `goose`/`omniroute`, `sota-multi-model-workflows` `ADR-0025` Mac-pinned broker Orca routing & `worker-release --environment`, and `ADR-0026` IEEE-754 `NaN`/`Inf` fail-closed + `decision_ns` study-wall enforcement + `DF1..DF12` key bijection).

## Decision Outcome

1. **Seal `ECOSYSTEM_ORG_MANIFEST.json` (`v3.10.2`, `30` Org ADRs) With `0` SHA Drift Across All `22` Repositories:**
   - Stamp exact live 40-char `origin/main` `baselineSha` digests across all `9` `PUBLIC`, `9` active `PRIVATE`, and `4` cold-archived repositories (`22/22 MATCH`).

## Alternatives Considered

- **Leaving `ECOSYSTEM_ORG_MANIFEST.json` at pre-`ADR-0026`/`ADR-0038` SHAs:** Rejected — breaks `sota-org-doctor --live` zero-drift invariant.

## Verification Witness

- `python scripts/architecture_catalog.py && python scripts/architecture_catalog.py --check` (`30` ADRs, `0` drift)
- `python scripts/merge_gate.py && python -m unittest discover -s tests -v && gitleaks git --log-opts=HEAD~1..HEAD --no-banner` (`PASS`, `0` leaks)
