# ADR-0028: `v3.10.0` Quality-Directive `3`-Powerhouse + `DSH` + `Pi/OMP` (`gpt-6.2-sol`), Claude `1:1` `claude-fable-5-2` Mix & 22-Repo Zero-Drift Seal

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Organization Control Plane, Frontier Model Quality Governance, 22-Repo 40-Char SHA Manifest & 3-Surface Parity (`L0–L13` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (`22/22` Exact 40-Char `origin/main` SHA Parity, `9/9` Public GitHub Actions `SUCCESS`, `1:1` `claude-fable-5-2` Mix & `54/54` Synced Checkouts)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-private-vault, https://github.com/native-agent-stack/sota-multi-model-workflows, https://github.com/native-agent-stack/cc-sota-harness, https://github.com/native-agent-stack/agy-sota-harness, https://github.com/native-agent-stack/sota-harness-foundation
- **Revisit Trigger:** 2026-12-06 (`23/5` SIP cutover) or next `ALPHA_STRATEGY_MINOR` promotion (`t >= 4.1905`, `DSR >= 0.95`)

## Context and Problem Statement

Sealing the `v3.10.0` Quality-Directive multi-model routing upgrade (`3` frontier powerhouses + `DSH` + `Pi/OMP` on `gpt-6.2-sol` `high` / `gpt-6.2-astra` `xhigh`, `0%` `haiku`/free-model sprawl, and `~1:1` `claude-fable-5-2` mix on Claude Code CLI) across all `22` organization repositories and `54` 3-surface workstation checkouts.

## Decision Outcome

1. **Seal `ECOSYSTEM_ORG_MANIFEST.json` at `schemaVersion = "3.10.0"` (`28` Org ADRs) Across All `22` Repositories:**
   - Stamp all `21` sibling live 40-char `origin/main` `baselineSha` digests (`total_mismatches = 0`).

## Alternatives Considered

1. **Leave `ECOSYSTEM_ORG_MANIFEST.json` at `v3.9.9` after `DEFAULT_ECOSYSTEM_SEMVER` advances to `"3.10.0"`:** Rejected — `22/22` zero-drift SHA and SemVer parity is mandatory across all 3 surfaces.

## Verification Witness

- `python3 scripts/architecture_catalog.py --sync-manifest` + `python3 scripts/merge_gate.py` + `python3 -m unittest discover -s tests -v` -> `PASS` (`28` ADRs, `0` drift, `0` leaks).
- `sota-org-doctor --live` -> `22/22` `MATCH` (`0` violations, `0` SHA drift).
