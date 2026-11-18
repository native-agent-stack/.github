# ADR-0031: `v3.10.3` Shared Active `24/5` Lossless Foundation, SOTA GitHub Maintenance Automation & `22`-Repo Zero-Drift Seal

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Organization Control Plane, Reusable GitHub Actions Maintenance, Shared Active `24/5` Foundation & `22`-Repo SHA Manifest (`L0–L13` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (`22/22` Live 40-Char `origin/main` SHA Parity, `9/9` Public GitHub Actions, `13/13` Private `Actions=false`, `sota-harness-foundation@43b51358` `ADR-0040`, `sota-multi-model-workflows@1de975aa` `ADR-0027`/`WF20`, `sota-mover-ranker@a628552b` `ADR-0031`, `native-agent-stack@c06939d1` `ADR-0031`, `0` Leaks)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-harness-foundation, https://github.com/native-agent-stack/sota-multi-model-workflows, https://github.com/alpacahq/alpaca-mcp-server, https://github.com/stablyai/orca
- **Revisit Trigger:** `2026-12-06` (`23/5` SIP cutover) or next `ALPHA_STRATEGY_MINOR` promotion (`t >= 4.1905`, `DSR >= 0.95`)

## Context and Problem Statement

Seals Master Lead Goal `G_SOTA_DUAL_MACHINE_MERIT_TO_LOSSLESS_LIVE_24X5` (`v3.10.3`) across all `22` organization repositories and both workstations (`Mac M5 Max` `<->` `Noesis Win32 64c/RTX4090` + `Noesis-Carbon WSL2`):
1. **Shared Active `24/5` Lossless Foundation (`sota-harness-foundation` `ADR-0040`):** Paper (`3` distinct Alpaca Paper `:8799/:8787/:8797` + `1` IBKR Paper `:4002`) and Stage-5 Live (`:8798`) operate on the same active `24/5` protection foundation built strictly upon our `18` pinned SOTA libraries (upstream-first, zero reinvention).
2. **Never-Gated Merit Sources -> Proven-Only Automated Live (`sota-multi-model-workflows` `ADR-0027`/`WF20`, `sota-mover-ranker` `ADR-0030`/`ADR-0031`):** Sim (`S1/S2`) and all `4` Paper accounts are strictly `NEVER_GATED`; Stage-5 Live (`:8798`) automates proven strategies starting with the Shared Lossless Foundation.
3. **Continuous Org GitHub Actions Maintenance Automation:** Adds weekday pre-open scheduled verification (`cron: "0 13 * * 1-5"`) to `.github/workflows/ci.yml`, adds `UPSTREAM.md` citation gating to `reusable-sota-gate.yml`, and introduces SHA-pinned `reusable-sota-lane-maintenance.yml` (`step-security/harden-runner` + `actions/checkout`, `contents: read`).

## Decision Outcome

- Upgrade `.github/workflows/ci.yml`, `.github/workflows/reusable-sota-gate.yml`, and add `.github/workflows/reusable-sota-lane-maintenance.yml` (all 40-char SHA-pinned, least-privilege).
- Bump `ECOSYSTEM_ORG_MANIFEST.json` to `v3.10.3`, record `stage5ProvenLosslessLivePolicy` and `sotaGithubAutomationLanes`, and seal fresh 40-char `origin/main` SHAs for `native-agent-stack@c06939d1`, `sota-harness-foundation@43b51358`, `sota-multi-model-workflows@1de975aa`, and `sota-mover-ranker@a628552b`.

## Alternatives Considered

- **Allowing `.github` reusable CI to omit scheduled weekday audits and `UPSTREAM.md` citation hygiene:** Rejected — active `24/5` lanes require continuous automated ADR, upstream-pin, and zero-leak verification.

## Verification Witness

- `python3 scripts/architecture_catalog.py --sync-manifest && python3 scripts/architecture_catalog.py --check` (`31` MADR 4.0 ADRs, `0` drift).
- `python3 scripts/merge_gate.py && python3 -m unittest discover -s tests -v && gitleaks git --no-banner` (`PASS`, `0` leaks).
