# ADR-0013: `v3.6.0` Universal `14/14` + `5/5` Workflow Research-Convergence, 6 DataFeed APIs, 4 Strategy Templates, 8 Engine Sources & 3-Surface Workstation Governance

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Organization-Wide Workflow, DataFeed, Strategy Template, Engine Source & Workstation Control Plane (`L0–L12` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (`14/14` + `5/5` Workflows Verified, `6` DataFeed APIs, `4` Strategy Templates, `8` Engine Sources, `3` Workstation Surfaces & `22/22` Org Doctor Verified)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-multi-model-workflows, https://github.com/native-agent-stack/agy-sota-harness, https://github.com/native-agent-stack/sota-harness-foundation, https://github.com/native-agent-stack/astrolabe, https://github.com/nautechsystems/nautilus_trader, https://github.com/nkaz001/hftbacktest
- **Revisit Trigger:** 2027-01-02

## Context and Problem Statement

Building on `ADR-0012` (`v3.5.1` 22-repository SHA seal), the organization control plane needed to enforce deterministic Research-Convergence (`sota-workflow-research-convergence.v3.6`) across **every workflow** (`14/14` canonical registry workflows, `5/5` native `Antigravity` workflows, and `.github/workflows/reusable-sota-gate.yml`), binding the **6 Trading Lane DataFeed APIs**, **4 canonical SOTA Strategy Templates + closed-bar Pine v6**, **8 Trading Engine Source repositories**, and **3-surface Dual-Workstation synchronization** (`Apple M5 Max`, `Noesis Win32`, and `Noesis-Carbon WSL2`).

## Decision Outcome

1. **Universal Workflow Research-Convergence & Reusable CI Catalog Gate (`v3.6.0`):**
   - Lock `sota-multi-model-workflows @ 9f7c9aa6d3` (`ADR-0013`, `14/14` workflows executing `kit.verify_workflow_research_convergence(...)`), `agy-sota-harness @ 53d5808bd4` (`ADR-0019`, `5/5` native workflows executing `verify_workflow_research_convergence`), and `.github/workflows/reusable-sota-gate.yml` (adding `scripts/architecture_catalog.py --check` / `tools/architecture_catalog.py --check` before `merge_gate.py`).
2. **6 Trading Lane DataFeed APIs, 4 Strategy Templates & 8 Trading Engine Sources:**
   - Standardize `CANONICAL_TRADING_LANE_DATAFEED_APIS` (`:8787/api/{research_feeds,first_hand_incentives,strategy_templates,research_convergence}`, `:8799/api/{status,tv-webhook}`, `127.0.0.1:4002` `astrolabe` Paper `L1` with `300/min` exit reserve), `CANONICAL_STRATEGY_TEMPLATES_MATRIX` (`PRE_TRAVEL_EARLY_IGNITION`, `FIRST_HAND_SEC_EPISODIC_PIVOT`, `MEGA_CAP_NEAR_LOSSLESS_ORB`, `CLIMAX_VWAP_MEAN_REVERSION` + non-repainting Pine v6 under `ADR-0022 <= 2.00%` stop, `ADVERSE_STOP_FIRST`, and `100x` round-lot `RiskAdverseQueueModel`), and `CANONICAL_TRADING_ENGINE_SOURCES` (`meridian`, `canon`, `tsl`, `trading-sota @ e838c5bb82`, `sota-mover-ranker`, `astrolabe`, `sota-compounding-lab`, `sota-dynamic-trail-c`).
3. **3-Surface Dual-Workstation Parity (`sota-workstation v2.1.0` + `sota-harness-foundation` `ADR-0027` + `cc-sota-harness` `ADR-0025`):**
   - Synchronize all `18` active repositories and `15` workflow files lease-safely across `Mac M5 Max` (`~/Documents/*`), `Noesis Win32` (`C:/sota-workstation/*`), and `Noesis-Carbon WSL2` (`~/sota-workstation/*`).

## Alternatives Considered

1. **Leave `reusable-sota-gate.yml` checking only `scripts/merge_gate.py` without `tools/architecture_catalog.py --check`:** Rejected — repositories using `tools/architecture_catalog.py` (`astrolabe`, `meridian` conventions) benefit from automatic MADR 4.0 catalog verification in the reusable org gate.

## Verification Witness

- `python3 scripts/architecture_catalog.py --sync-manifest` + `python3 scripts/merge_gate.py` -> `PASS` (`13` GitHub-evidenced MADR 4.0 ADRs & `ECOSYSTEM_ORG_MANIFEST.json` `v3.6.0` verified, `0` drift, `0` leaks).
- `python3 -m unittest discover -s tests -v` -> `PASS`.
