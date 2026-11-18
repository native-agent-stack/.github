# ADR-0009: 7-Feed First-Hand PIT APIs, 13-Workflow v3.3.0 AO Automation & 85-Trial Trading Governance

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Research, Orchestration & Trading Governance (`L0–L12` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (85 Trials, 13 Workflows, 7 PIT Feeds, AO Receipt & 22-Repo Org Doctor Verified)
- **GitHub Evidence:** https://github.com/native-agent-stack/sota-upstream-shelf-lock, https://github.com/native-agent-stack/sota-multi-model-workflows, https://github.com/native-agent-stack/sota-compounding-lab, https://github.com/native-agent-stack/sota-harness-foundation
- **Revisit Trigger:** 2027-01-02

## Context and Problem Statement

Building on `ADR-0008` (`424`-row starred/research-converged upstream matrix and bidirectional `sota-workstation coop`), the `native-agent-stack` organization control plane required finalization of:
1. Live first-hand early-reaction point-in-time (`PIT`) DataFeed APIs and FINRA dissemination lag gates across `:8787`, `:8799`, and `:4002`;
2. The `13`-workflow `v3.3.0` Multi-Model `AO` (`ComposioHQ/agent-orchestrator`) and End-to-End Research-Convergence automation suite;
3. Synchronization of the `85`-trial HLZ ledger (`t*(86) = 4.1631`), `43` compiled `E1–E4` root-cause lessons, and converged 22-repository commit SHAs in `ECOSYSTEM_ORG_MANIFEST.json`.

## Decision Outcome

1. **7-Feed `sota-research-feeds.v2` First-Hand PIT Contract & `DataFeedPITContract` Gate:**
   - Standardize `alpaca_sip` (`04:00–20:00` ET), `alpaca_boats` (`20:00–04:00` ET + `2026-12-06` `23/5` SIP cutover auto-probe), `alpaca_raw_vs_all_adjustment`, `sec_edgar_acceptance_datetime` (`<= 0.067 req/s` live Atom poller, `15m` half-life freshness decay, `424B*`/`S-3` dilution block below `USD 2B` float), `finra_regsho_cnmsshvol_t1` (`T-1` short-volume lag + FINRA Rule 4560 `T+8` business-day short-interest lag), `corporate_actions_split_guard`, and `ibkr_paper_4002_l1` (`127.0.0.1:4002` loopback guard, `2700`/`300` msg/min protective-exit reserve, Rule 612 `25..75 bps` `StopLimitOrder` collars).
   - Expose the `16`-tool `:8787` MCP surface (`sota_get_research_feeds`, `sota_get_first_hand_incentives`, `sota_get_converged_strategy_templates`) and 4 canonical strategy templates across `sota-mover-ranker` (`ADR-0007..0010`), `sota-compounding-lab` (`ADR-0006`), `trading-sota` (`ADR-0011`), `astrolabe` (`ADR-0004`), and `sota-harness-foundation` / `cc-sota-harness` (`ADR-0023`).
2. **13-Workflow `v3.3.0` Multi-Model `AO` & Research-Convergence Automation (`sota-multi-model-workflows` `ADR-0008..0011` + `agy-sota-harness` `ADR-0016`):**
   - Enforce Turn-0 `_sota_kit.py` `v3.3.0` bootstrap across all `13` workflows, including Workflow `#12` (`ao_multi_model_convergence_workflow.py` with `CANONICAL_MODEL_VENDORS` Stage-3 allowlist, `math.isfinite()` positive-inclusion stop gates, frozen-assertion protection, and telemetry-derived `meshState` failover) and Workflow `#13` (`research_convergence_landing_workflow.py` 4-phase `ADR-0004` SHA-256 + `18` upstream pin + 7-feed PIT validator).
3. **85-Trial Empirical HLZ Ledger & `v0.8.0` / `H085` Execution Proofs (`sota-private-vault` `ADR-0008`):**
   - Seal `Trial #84` (`sota-dynamic-trail-c` `v0.8.0` `ADR-0006`: `+19.73 bps/trade` OOS lift, `-84.4%` `CVaR_95` reduction vs static `200 bps` stops, and `PostWallCohortLedger` toward `N >= 250`) and `Trial #85` (`H085` `sota-upstream-shelf-lock` `v2.0.0` `ADR-0004`: `14,750` nanosecond SIP files, `577` dates `<= 2026-10-15`, `86.41%` passive `10:30` ET bid queue fills `1,393 / 1,612` with `bs * 100.0` CTA/UTP round-lot scaling, flipping `1x` to `+7.908 bps` and `2x` to `+2.374 bps` while honestly logging `FAILED` at `t = 0.8151 < 4.1604`).

## Alternatives Considered

1. **Permit wrapper pseudo-vendors (`multi-router`) to satisfy Stage-3 multi-model diversity:** Rejected — closed by `CANONICAL_MODEL_VENDORS` (`anthropic`, `openai`, `google`, `deepseek`) in `ADR-0023`.
2. **Enable GitHub Actions on `PRIVATE` execution/vault repositories:** Rejected — preserves `0` private CI minute burn (`actionsEnabled: false`) across all `13` private/archived repositories while running unlimited SHA-pinned CI across all `9 PUBLIC` repositories.

## Verification Witness

- `python3 scripts/architecture_catalog.py --sync-manifest` + `python3 scripts/merge_gate.py` -> `PASS` (`9` GitHub-evidenced MADR 4.0 ADRs & `ECOSYSTEM_ORG_MANIFEST.json` verified, `0` drift, `0` leaks).
- `python3 -m unittest discover -s tests -v` -> `PASS`.
- `sota-doctor` (`11/11 PASS`) & `sota-org-doctor --live` (`22/22 PASS`, `0` violations).
