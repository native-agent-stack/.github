# ADR-0033: `v3.10.6` Pre-IPO `2026-11-19` `22`-Repo Zero-Drift Org Seal — `ADR-0035` `P0-1..6` Unified Shield & `10`-Lead Multi-Model Orca Fleet

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Organization Control Plane, Pre-IPO `2026-11-19` Execution Firewall, `10`-Lead Multi-Model Orca Fleet & `22`-Repo 40-Char SHA Manifest (`L0–L13` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (`22/22` Live 40-Char `origin/main` SHA Parity, `9/9` Public GitHub Actions, `13/13` Private `Actions=false`, `sota-mover-ranker@4de58ade` `ADR-0035` `137/137 pytest`, `sota-multi-model-workflows` `ADR-0030` `10/10` Leads / `28/28 pytest`, Live Orca Run `run_5c51382bc888` `4` Active Multi-Model Workers, `0` Leaks)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-multi-model-workflows, https://github.com/native-agent-stack/sota-harness-foundation, https://github.com/stablyai/orca
- **Revisit Trigger:** `2026-11-20` Post-`NASDAQ:ANT` IPO debrief or `2026-12-06` (`23/5` SIP cutover)

## Context and Problem Statement

Seals the `v3.10.6` pre-IPO full-ecosystem convergence across all `22` organization repositories (`Mac M5 Max` `<->` `Noesis Win32 64c/128GB/RTX4090` + `Noesis-Carbon WSL2`):
1. **`ADR-0035` `P0-1..6` Closure (`sota-mover-ranker@4de58ade`, `137/137 pytest`, `35/35 ADRs`):** Wires unified `evaluate_protective_entry_shield` (`ADR-0017`/`ADR-0019`) into `:8798`, `:8797`, and `VixAndMajorGrowthRegimeEngine`; hardens `validate_stage5_atomic_order(..., dedicated_live_guardian_healthy: bool = False)` fail-closed outside RTH; ships `scripts/install-noesis-24x5-supervisor.ps1` (`2`-minute Scheduled Task keepalive with `SINGLE_BROKER_HOST_FIREWALL`).
2. **`10/10` Canonical Multi-Model Orca Lane Leads Across `7/7` Domain Hubs (`sota-multi-model-workflows` `ADR-0030`, `28/28 pytest`, `30/30 ADRs`):** Adds `D4_all_market_research_lead`, strictly read-only `D5_non_market_incentives_lead`, and `D7_beyond_skillopt_lead` alongside `T1`–`T3`, read-only `T5`, and `H1`–`H3`, with `8` live nested multi-model worktrees on Stationary `Noesis` and live multi-model Orchestration Run `run_5c51382bc888`.
3. **Autonomous Pre-IPO Goal (`G_SOTA_IPO_20261119_FULL_ECOSYSTEM_CONVERGENCE`):** `7` standing pre-market/open daemon crons (`08:00`–`09:35 ET`) + `14` dual-machine Orca Automations (`7` Mac + `7` Noesis).

## Decision Outcome

- Bump `ECOSYSTEM_ORG_MANIFEST.json` `schemaVersion` to `"3.10.6"`, seal exact live 40-char `origin/main` SHAs across all `22` org repositories (`0` drift), and record `canonicalOrcaLaneLeadsCount: 10`, `adr0035UnifiedShieldActive: true`, and `preIpoOrcaRunId: "run_5c51382bc888"`.

## Alternatives Considered

- **Deferring the `v3.10.6` manifest seal until after tomorrow's IPO open:** Rejected because `sota-org-doctor --live` enforces zero SHA drift before market open.

## Verification Witness

- `python3 scripts/architecture_catalog.py --sync-manifest && python3 scripts/architecture_catalog.py --check` (`33/33` MADR 4.0 ADRs, `0` drift).
- `python3 scripts/merge_gate.py && python3 -m unittest discover -s tests -v && gitleaks git --no-banner` (`PASS`, `0` leaks).
- `~/.agents/bin/sota-org-doctor --live` (`22/22` exact SHA parity, `0` violations).
