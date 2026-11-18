# ADR-0018: `v3.9.2` 3-Surface Dual-Desktop Coexistence (`ADR-0018` & `ADR-0015`), `18/18` `UPSTREAM.md` (`Canon 0180`) & 22-Repo Zero-Drift SHA Seal

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Organization Control Plane, 22-Repo 40-Char SHA Manifest & 3-Surface Workstation Parity (`L0–L13` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (`22/22` Exact 40-Char `origin/main` SHA Parity, `9/9` Public GitHub Actions `SUCCESS`, `54/54` 3-Surface Synced Checkouts, `93` HLZ Trials & `69` Compiled Lessons)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-mover-ranker, https://github.com/native-agent-stack/sota-dynamic-trail-c, https://github.com/native-agent-stack/canon, https://github.com/native-agent-stack/sota-multi-model-workflows, https://github.com/native-agent-stack/agy-sota-harness
- **Revisit Trigger:** 2027-01-02

## Context and Problem Statement

Following `ADR-0017` (`v3.9.1`), final multi-peer and dual-workstation reconciliation across `Mac M5 Max`, `Noesis Win32`, and `* Noesis-Carbon` `ext4` landed six final closures:
1. **`sota-mover-ranker @ 31907e95999d` (`ADR-0018`, `18` ADRs, `89/89` `pytest` PASS, `ty@0.0.104` `0` diagnostics)** and **`sota-dynamic-trail-c @ 7fb92138931e` (`ADR-0015`, `15` ADRs):** Dual TradingView Desktop zero-WS-conflict coexistence, Win32 computer-use & `msvcrt` singleton daemon locks, `--read-only-radar`, and static type narrowing.
2. **`canon @ b12968e125b1` (`0180`, `154` ADRs), `sota-multi-model-workflows @ a6c71a4a4d0f` (`ADR-0017`), `agy-sota-harness @ 6c4073d9f36a` (`ADR-0023`), `sota-private-vault @ 4de294b6daf5` (`ADR-0014`), and `native-agent-stack @ b6ad7dae8a14` (`ADR-0018`):** Completing `18/18` (`100%`) `UPSTREAM.md` + `orca.yaml` coverage across all active repositories.

## Decision Outcome

1. **Seal `ECOSYSTEM_ORG_MANIFEST.json` at `schemaVersion = "3.9.2"` (`18` Org ADRs) Across All `22` Repositories:**
   - Lock all `21` sibling 40-char `origin/main` `baselineSha` digests (`total_mismatches = 0`), maintaining `9` public repos (`completed/success`), `9` active private repos (`actionsEnabled = false`), and `4` cold-archived repos (`archived = true`, `actionsEnabled = false`).

## Alternatives Considered

1. **Leave `ECOSYSTEM_ORG_MANIFEST.json` at `v3.9.1` prior to locking `ADR-0018`, `ADR-0015`, `Canon 0180`, `ADR-0017`, and `ADR-0023`:** Rejected — zero SHA drift (`22/22` `MATCH`) across all `3` workstation surfaces is mandatory.

## Verification Witness

- `python3 scripts/architecture_catalog.py --sync-manifest` + `python3 scripts/merge_gate.py` + `python3 -m unittest discover -s tests -v` -> `PASS` (`18` ADRs, `0` drift, `0` leaks).
- `22/22` live `origin/main` SHA `MATCH` (`total_mismatches = 0`) & `9/9` public GitHub Actions `completed / success`.
