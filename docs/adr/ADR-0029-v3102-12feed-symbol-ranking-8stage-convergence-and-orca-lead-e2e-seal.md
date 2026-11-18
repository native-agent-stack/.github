# ADR-0029: `v3.10.2` `12`-Feed (`DF1..DF12`) Symbol Ranking Foundation, `8`-Stage SOTA Research Convergence (`413+6`), Zero-Kimi 8-Runtime Parity & `22`-Repo Zero-Drift Seal

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Organization Control Plane, `12`-Feed Symbol Ranking DataFeeds (`DF1..DF12`), `8`-Stage Convergence (`413+6`), `22`-Repo 40-Char SHA Manifest & Orca-Lead E2E (`L0–L13` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (`22/22` Live 40-Char `origin/main` SHA Parity, `9/9` Public GitHub Actions `SUCCESS`, `13/13` Private `Actions=false`, `12` Symbol Ranking Feeds -> `6` Auto Routes, `19` Canonical Workflows, Zero `kimi`/Stale Models, `54/54` Synced Checkouts)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-multi-model-workflows, https://github.com/native-agent-stack/cc-sota-harness, https://github.com/native-agent-stack/agy-sota-harness, https://github.com/native-agent-stack/sota-compounding-lab, https://github.com/native-agent-stack/sota-private-vault, https://github.com/microsoft/RD-Agent
- **Revisit Trigger:** 2026-12-06 (`23/5` SIP cutover) or next `ALPHA_STRATEGY_MINOR` promotion (`t >= 4.1905`, `DSR >= 0.95`)

## Context and Problem Statement

Sealing the `v3.10.2` cross-repository research convergence upgrade across all `22` organization repositories (`18` active + `4` cold-archived) and `54` 3-surface workstation checkouts:
1. Finalizes `DF1..DF12` (`sota-symbol-ranking-datafeeds.v3.10`) with strict bitemporal PIT ordering (`ts_event <= ts_recv <= decision_ns`) feeding all `6` auto-trading routes across research, simulation, and execution harnesses (`sota-multi-model-workflows`, `sota-compounding-lab`, `astrolabe`, `meridian`, `tsl`, `trading-sota`, `canon`, `sota-private-vault`).
2. Upgrades Research Convergence to `8` stages grounded in `413` owner starred repositories plus `6` beyond-starred SOTA anchors (`microsoft/RD-Agent`, `databento/databento-python`, `unit8co/darts`, `Nixtla/statsforecast`, `stanfordnlp/dspy`, `skfolio/skfolio` / ADIA MinTRL), retires `kimi-*`/`Moonshot AI` + stale model slugs (`deepseek-v4-pro` -> `deepseek-flash`), and activates `Workflow #19` (`orca-lead-e2e-research-convergence`) + `10th` AGY DAG (`617f37ce`, CI green).

## Decision Outcome

1. **Seal `ECOSYSTEM_ORG_MANIFEST.json` (`29` Org ADRs) Across All `22` Repositories:**
   - Stamp exact live 40-char `origin/main` `baselineSha` digests (`total_mismatches = 0`), index all `6` beyond-starred SOTA anchors in `UPSTREAM.md` and `ECOSYSTEM_ORG_MANIFEST.json`, and lock `symbolRankingDatafeedsSchema = "sota-symbol-ranking-datafeeds.v3.10"`.

## Alternatives Considered

1. **Retain separate `9`-feed datafeed metadata and `18`-workflow manifests across harnesses and vault:** Rejected — leaves `DF10..DF12` unpinned and causes multi-runtime convergence drift across `cc-lead`, `codex`, `agy`, and `dsh`.

## Verification Witness

- `python scripts/architecture_catalog.py --sync-manifest && python scripts/architecture_catalog.py --check` (`29` ADRs, `0` drift)
- `python scripts/merge_gate.py && python -m unittest discover -s tests -v && gitleaks protect --staged --no-banner -v` (`PASS`, `0` leaks)
