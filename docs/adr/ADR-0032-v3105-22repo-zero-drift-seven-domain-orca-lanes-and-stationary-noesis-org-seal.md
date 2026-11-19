# ADR-0032: `v3.10.5` Full-Ecosystem 7-Domain Orca Lane Hubs, Stationary `Noesis` Primary `24/5` Host, Dedicated `:8796` Live Guardian & `22`-Repo Zero-Drift Org Seal

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Organization Control Plane, Dual-Machine Stationary Workstation Sovereignty, 7-Domain Orca Lane Hubs & `22`-Repo 40-Char SHA Manifest (`L0–L13` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (`22/22` Live 40-Char `origin/main` SHA Parity, `9/9` Public GitHub Actions, `13/13` Private `Actions=false`, `18` Live Dual-Machine Orca Folder Hubs (`9` Noesis + `9` Mac), `14` Active Orca Automations (`7` + `7`), `native-agent-stack@d6ed68bb`, `sota-multi-model-workflows@938decb2`, `sota-mover-ranker@2010a9e1`, `0` Leaks)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-harness-foundation, https://github.com/native-agent-stack/sota-multi-model-workflows, https://github.com/native-agent-stack/agy-sota-harness, https://github.com/native-agent-stack/sota-compounding-lab, https://github.com/stablyai/orca
- **Revisit Trigger:** `2026-12-06` (`23/5` SIP cutover) or next `ALPHA_STRATEGY_MINOR` promotion (`t >= 4.1928`, `DSR >= 0.95`)

## Context and Problem Statement

Seals the `v3.10.5` full-ecosystem dual-machine convergence across all `22` organization repositories (`Mac M5 Max` `<->` `Noesis Win32 64c/128GB/RTX4090` + `Noesis-Carbon WSL2`):
1. **Stationary `Noesis` Primary `24/5` Host & Portable `Mac` Cockpit/Failover (`sota-harness-foundation@0629fd82` `ADR-0041`, `sota-dynamic-trail-c@2e3d96b5` `ADR-0026`, `sota-mover-ranker@2010a9e1` `ADR-0033`):** `stationary_noesis_win32` is promoted as primary always-on `24/5` host for the Main Framework Foundation and Trading Engine (`P1:8799`, `P2:8787`, `P3:8797`, `P4:4002`, `L5:8798`, `:8796` Live EXT Guardian, `S1`/`S2`, 4K TradingView) with symmetric `singleActiveBrokerHostOnly = true` firewall and cross-OS Win32 Credential Manager (`advapi32.CredReadW`) + `CrossOsJsonRpcPipe` parity.
2. **All 7 Full-Ecosystem Domain Orca Lane Hubs + Named Lane Leads (`sota-multi-model-workflows@938decb2` `ADR-0029` + `CANONICAL_ORCA_LANE_LEADS`):** Physically manifests `01-sim-backtest`, `02-paper-4acct-farm`, `03-stage5-lossless-live` (strictly read-only `T5` Lane Lead with zero broker credentials or order write path), `04-research-all-market`, `05-non-market-incentives`, `06-framework-and-harness`, and `07-beyond-convergence-skillopt` across BOTH `Noesis` and `Mac` (`18` total folder hubs + `14` enabled scheduled Orca Automations).
3. **Dedicated `:8796` Extended-Hours Live Guardian Isolation (`sota-mover-ranker@2010a9e1` `ADR-0034`):** Fail-closes Extended-Hours Stage-5 Live entries unless a dedicated `:8796` Live Guardian explicitly confirms `account_mode == "LIVE"`, eliminating Paper/Live guardian conflation while preserving native RTH atomic server-side OCO `bracket`/`oto` (`ADR-0022 <= 2.00%`).

## Decision Outcome

- Bump `ECOSYSTEM_ORG_MANIFEST.json` `schemaVersion` to `"3.10.5"`, seal exact live 40-char `origin/main` SHAs across all `22` org repositories (`0` drift), record `sevenDomainOrcaLaneHubs`, `dedicatedLiveExtGuardianPort: 8796`, `dualMachineOrcaFolderHubsCount: 18`, `dualMachineOrcaAutomationsCount: 14`, and `canonicalWorkflowsCount: 20`.

## Alternatives Considered

- **Leaving `ECOSYSTEM_ORG_MANIFEST.json` at `v3.10.3` with drifted SHAs on `native-agent-stack`, `sota-multi-model-workflows`, and `sota-mover-ranker`:** Rejected because `sota-org-doctor --live` enforces strict zero-drift 40-char SHA parity across all `22` repositories.

## Verification Witness

- `python3 scripts/architecture_catalog.py --sync-manifest && python3 scripts/architecture_catalog.py --check` (`32` MADR 4.0 ADRs, `0` drift).
- `python3 scripts/merge_gate.py && python3 -m unittest discover -s tests -v && gitleaks git --no-banner` (`PASS`, `0` leaks).
- `~/.agents/bin/sota-org-doctor --live` (`22/22` exact SHA parity, `0` violations).
