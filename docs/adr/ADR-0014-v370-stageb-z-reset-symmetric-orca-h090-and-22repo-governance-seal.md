# ADR-0014: `v3.7.0` Stage-B `Noesis-Carbon` Closure, Symmetric `:6770` Orca Mesh, `Trial #90` (`H090`) & `09:30` ET 22-Repo Governance Seal

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Organization-Wide Control Plane, 3-Surface Workstation Mesh & `24/5` Paper Execution Governance (`L0–L12` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (`9/9` Public GitHub Actions `SUCCESS`, `22/22` `sota-org-doctor --live` `PASS`, `12/12` `sota-doctor` `PASS`, `90` Trials, `59` Lessons & Symmetric `:6770` Orca Verified)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-harness-foundation, https://github.com/native-agent-stack/agy-sota-harness, https://github.com/native-agent-stack/sota-compounding-lab, https://github.com/native-agent-stack/astrolabe, https://github.com/stablyai/orca
- **Revisit Trigger:** 2027-01-02

## Context and Problem Statement

Following `ADR-0013` (`v3.6.0` universal workflow/DataFeed/template/engine governance), coordinated multi-peer execution across `Mac M5 Max`, `Noesis` Win32, and `* Noesis-Carbon` (`Ubuntu 26.04.1 LTS` `ext4`) closed the Stage-B `Z:` reset (`2.85 TB` free on `Z:`, `Meridian` `0055`/`0056` holds closed `@ f8483af9`), paired symmetric `:6770` Orca E2EE servers, seeded the `1.57 GB` (`29,500`-file) `<= 2026-10-15` pre-wall Parquet lake on `Noesis`, completed `Trial #90` (`H090`: `+20.84 bps` 1x, `+15.43 bps` 2x, `5/5` `CPCV` positive paths; `N = 90 -> t*(91) = 4.1760`, `59` lessons), and sealed MADR 4.0 ADRs across every execution, research, and harness repository (`sota-harness-foundation` `ADR-0028`+, `cc-sota-harness` `ADR-0026`+, `agy-sota-harness` `ADR-0020`, `sota-compounding-lab` `ADR-0009`, `sota-mover-ranker` `ADR-0013`, `sota-dynamic-trail-c` `ADR-0011`, `astrolabe` `ADR-0006`+, `tsl` `ADR-0020`+, `canon` `0177`, and `sota-private-vault` `ADR-0010`).

## Decision Outcome

1. **Seal `ECOSYSTEM_ORG_MANIFEST.json` (`v3.7.0`, `14` Org ADRs) Across All `22` Repositories:**
   - Synchronize all `21` sibling `baselineSha` commits and converged ADR counts across `publicUnlimitedActionsTier` (`9` repos), `privateExecutionAndVaultTier` (`9` repos, `actionsEnabled = false`), and `coldArchivedSupersededTier` (`4` repos, `archived = true`, `actionsEnabled = false`).
2. **Enforce `09:30` ET Single-Writer Paper Protection & Zero Private CI Burn:**
   - Maintain `singleActiveBrokerHostOnly = true` on `Mac M5 Max` (`:8787`, `:8799`, `:4002` `HTTP 200` / `8/8` landscape planes ready) while routing `56`-thread `CPCV` and pre-wall research onto `Noesis` / `Noesis-Carbon`, keeping `13/13` private repositories at `0` GitHub Actions minute burn.

## Alternatives Considered

1. **Defer org-wide `v3.7.0` manifest synchronization until after RTH close:** Rejected — locking exact pre-open `baselineSha` provenance before `09:30` ET guarantees deterministic attribution for today's live Paper cohort.
2. **Expose private execution or vault telemetry in public repositories:** Rejected — enforced fail-closed by `merge_gate.py` and `sota-org-doctor --live`.

## Verification Witness

- `python3 scripts/architecture_catalog.py --sync-manifest` + `python3 scripts/merge_gate.py` -> `PASS` (`14` GitHub-evidenced MADR 4.0 ADRs & `ECOSYSTEM_ORG_MANIFEST.json` `v3.7.0` verified, `0` drift, `0` leaks).
- `python3 -m unittest discover -s tests -v` -> `PASS`.
- `sota-org-doctor --live` (`22/22 PASS`, `0` violations) & `sota-doctor` (`12/12 PASS`).
