# ADR-0024: `v3.9.7` Scrubbed `95`-Trial / `80`-Lesson Vault Sync (`ADR-0019`), ADIA #19 `MinTRL` Law & 22-Repo Zero-Drift SHA Seal

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Organization Control Plane, 22-Repo 40-Char SHA Manifest & 3-Surface Parity (`L0–L13` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (`22/22` Exact 40-Char `origin/main` SHA Parity, `9/9` Public GitHub Actions, `95` HLZ Trials, `80` Lessons & `54/54` Synced Checkouts)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-private-vault, https://github.com/native-agent-stack/sota-multi-model-workflows, https://github.com/native-agent-stack/cc-sota-harness
- **Revisit Trigger:** 2026-12-06 (`23/5` SIP cutover) or next `ALPHA_STRATEGY_MINOR` promotion (`t >= 4.1882`, `DSR >= 0.95`)

## Context and Problem Statement

Completing `v3.9.7` full-ecosystem convergence following Mac's scrubbed `95`-trial `HYPOTHESIS_LEDGER.md` + `80`-lesson `LESSONS.md` sync into `sota-private-vault` (`ADR-0019`), ADIA Lab #19 `MinTRL` power-law codification (`Lesson 6dab48d65a104306`), and `native-agent-stack` (`ADR-0024`).

## Decision Outcome

1. **Seal `ECOSYSTEM_ORG_MANIFEST.json` at `schemaVersion = "3.9.7"` (`24` Org ADRs) Across All `22` Repositories:**
   - Stamp all `21` sibling live 40-char `origin/main` `baselineSha` digests (`total_mismatches = 0`).

## Alternatives Considered

1. **Leave `ECOSYSTEM_ORG_MANIFEST.json` pointing at pre-wiki-sync `sota-private-vault` / `native-agent-stack` SHAs:** Rejected — `22/22` exact live `origin/main` SHA parity is mandatory.

## Verification Witness

- `python3 scripts/architecture_catalog.py --sync-manifest` + `python3 scripts/merge_gate.py` + `python3 -m unittest discover -s tests -v` -> `PASS` (`24` ADRs, `0` drift, `0` leaks).
- `sota-org-doctor --live` -> `22/22` `MATCH` (`0` violations, `0` SHA drift).
