# ADR-0042: `tier0-quant` `ADR-0009`–`ADR-0010` Convergence: 24/5 Dynamic Trailing, Whole-Market Regime Reversal, `46` SHA-Locked Skills, 4-Harness OpenCode Plugin, Stateful Risk & `643+48` Frontier Seal

- **Status:** Accepted
- **Date:** 2026-11-21
- **Layer:** L0 Org Control Plane (`L0`), Quant Execution & Risk (`L2`/`L5`), Cross-Harness Governance (`L9`/`L10`)
- **Evidence Grade:** E4 (`tier0-quant@9f9b1fbe3e5bed4be2c43f62d8f3b41ccd304fe6`, `ADR-0001..ADR-0010` (`10/12` bounded), lean SOTA Charter `AGENTS.md` SHA-256 `88bcce562e402a64...`, `v5` manifest `c9a69e10ae4e9b6c...`, `643+48` live-starred/frontier Atlas (`0` overlap) + `Chronos-2 <= 2026-10-15` PIT caution, `3,000 <= 5,000` prod LOC with untouched Z3 `UNSAT` `risk.py = 361 <= 400`, `46/46` SHA-locked upstream skills (`0` orphans across `6` Orca lanes), `docs/UNIFIED_ECOSYSTEM_INVENTORY.md`, native OpenCode ESM plugin `.opencode/plugins/tier0-harness-hook.js` + fail-closed zero-self-invented-agent/skill hooks across Claude/Codex/Gemini/OpenCode, `XNYS` `13:00 ET` early-close `SESSION_PROTECTION_24X5`, optional PIT ALFRED `VIXCLS`/`BAMLH0A0HYM2` regime stress confirmation, `Hypothesis` stateful `DrawdownBreakerMachine`/`ExitReserveMachine` & `4/8 bps` net-cost separation, `d101034` bounded CPU/GPU/DuckDB/MLflow/Compose pools & `flock check.sh`, `45/45` pytest, `15/15` Inspect AI, `16/16` Promptfoo, `21/21` immutable archived legacy SHAs intact, `gitleaks 0`, `zizmor 0`, `Noesis` <-> `Mac M5 Max` converged with `MAC_BROKER_PORTS=0`)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/tier0-quant, https://github.com/nautechsystems/nautilus_trader, https://github.com/nkaz001/hftbacktest, https://github.com/tradermonty/claude-trading-skills, https://github.com/sst/opencode, https://github.com/stablyai/orca, https://github.com/Z3Prover/z3
- **Revisit Trigger:** Achieving the first verified pre-wall (`<= 2026-10-15`) 6-gate statistical falsification pass independently on both directional and inverse-reversal legs (`hlz_trials_passed >= 1`) authorizing `Stage 4` Paper `LiveNode` (`:4002`) sign-off via `paper-gatekeeper`, or a schema-breaking Next-Era org control-plane upgrade.

## Context and Problem Statement

Following `ADR-0041` (`tier0-quant@523f0e11`, `ADR-0008`), six converged milestones landed on `native-agent-stack/tier0-quant` (`9bc25fe`, `d101034`, `b1162b2`, `3f86be5` PR #8, `7defd6c`, and `9f9b1fb` converging PR #10):

1. **24/5 Session-Aware Lossless/Dynamic Trailing & Whole-Market Regime / Peak-Exhaustion Reversal (`ADR-0009`):** Every simulated and future gated Paper position is continuously protected across `PRE_MARKET`, `RTH` (including `XNYS` `13:00 ET` early-close half-days), `AFTER_HOURS`, and `OVERNIGHT` with collared `STOP_LIMIT` (`outside_rth=True`) off-hours, monotonic breakeven+fee locking, `NATR_14` dynamic trailing inside `SignalExecutionStrategy`, causal `SPY`/`QQQ` + optional PIT ALFRED (`VIXCLS`, `BAMLH0A0HYM2`) regime crash alignment, signed extreme-mover ranking, and causal peak-exhaustion short gating (`require_peak_confirmation=True`), keeping `risk.py` (`361 <= 400` LOC, Z3 `UNSAT`) 100% untouched and total custom production code at `3,000 <= 5,000` LOC.
2. **Bounded Compute & Verification Concurrency (`d101034`):** Numba, OpenMP, CatBoost, LightGBM, DuckDB, MLflow, and Docker Compose pools are explicitly bounded with per-worktree `flock` protection in `scripts/check.sh`.
3. **Lean SOTA Charter, 4-Harness Zero-Self-Invented Enforcement & `ADR-0010` `643+48` Stateful Risk Seal (`b1162b2`, `3f86be5`, `7defd6c`, `9f9b1fb`):** `AGENTS.md` and `CLAUDE.md` were distilled to the canonical 5-point Charter (`88bcce562e402a6449f123844ee7d9c02e052002809568379185530e6a7e67b1`); `UPSTREAM_SKILLS_LOCK.json` expanded from `33` to `46/46` SHA-locked upstream skills (`+13` `MIT` `tradermonty/claude-trading-skills` mapped across Orca lanes `1`, `2`, `6` with `0` orphans); `.opencode/plugins/tier0-harness-hook.js` + `--harness opencode` + fail-closed zero-self-invented-agent/skill hooks enforce Upstream-Only provenance across all 4 harnesses (`Claude`, `Codex`, `Gemini`, `OpenCode`), unified inside `docs/UNIFIED_ECOSYSTEM_INVENTORY.md`; `ADR-0010` (`10/12`) seals `643+48` live-starred frontier coverage, `Chronos-2 <= 2026-10-15` PIT caution, and `Hypothesis` stateful `DrawdownBreakerMachine`/`ExitReserveMachine` + `4/8 bps` net-cost separation.

## Decision Outcome

1. **Advance `repositories.nextEraActiveTier.tier0-quant.baselineSha` to `9f9b1fbe3e5bed4be2c43f62d8f3b41ccd304fe6`:**
   - Synchronize `ECOSYSTEM_ORG_MANIFEST.json` (`schemaVersion 4.0.0`) to record `tier0-quant@9f9b1fbe` (`ADR-0001..ADR-0010`, `v5` manifest `c9a69e10ae4e9b6c...`, `643+48` Atlas, `46/46` SHA-locked skills, `UNIFIED_ECOSYSTEM_INVENTORY.md`, 4-harness OpenCode plugin + zero-self-invented-agent/skill hooks, `3,000 <= 5,000` LOC, `risk.py = 361 <= 400`, `45/45` pytest, `15/15` Inspect AI, `16/16` Promptfoo).
2. **Preserve All `21` Immutable Archived Legacy Repository SHAs Untouched:**
   - Retain every distinct final commit hash under `repositories.archivedLegacyTier` (`fadebba0...` through `d3eec673...`), enforced continuously by `tests/test_org_manifest.py::test_archived_repos_retain_distinct_immutable_shas`.
3. **Maintain Dual-Machine Parity (`Noesis` <-> `Mac M5 Max`) & Single Active Broker Host Boundary:**
   - Synchronize both `tier0-quant` and `.github` at identical `origin/main` SHAs across `Noesis` (Win32 + `Z:` + `Noesis-SOTA` WSL2 + `10/10` Docker + `13/13` portals) and `Mac M5 Max` (`100.93.211.101`, `6/6` portals, `MAC_BROKER_PORTS = 0`), with `paper_live_deployed == False` until all 6 falsification gates pass independently on all legs.

## Alternatives Considered

- **Leaving `.github` Pinned at `tier0-quant@523f0e11` (`ADR-0008`, `33` skills):** Rejected — leaves the org control plane out of sync with `ADR-0009`–`ADR-0010`, `643+48` stars, `46/46` locked skills, OpenCode plugin enforcement, and the distilled Charter (`88bcce56...`).
- **Adding a Separate Custom Execution Module for 24/5 Trailing:** Rejected — violates `Zero Paper Self-Invention` and `Sim == Paper == Live`; `tier0-quant` cleanly extends `SignalExecutionStrategy` inside `engine.py` at `3,000 <= 5,000` LOC with `risk.py` untouched.

## Verification Witness

- `python scripts/architecture_catalog.py --sync-manifest` & `--check` (`42/42` GitHub-evidenced MADR 4.0 ADRs verified, `0` drift, LF-only).
- `python scripts/merge_gate.py` (`PASS`: `0` leaks, 40-char SHA-pinned Actions, MADR 4.0 & `ADR-0023` `18`-pin shelf parity).
- `python -m unittest discover -s tests -v` (`5/5` PASS including `test_archived_repos_retain_distinct_immutable_shas`).
- `gitleaks git --no-banner`, `zizmor --offline .github/workflows`, and GitHub Actions `Org Control-Plane Gate` (`completed/success`), paired with `tier0-quant@9f9b1fbe` green CI (`Tier-0 SOTA Verification Gate` + `Tier-0 Docs Portal Strict Build`) and dual-machine parity (`MAC_BROKER_PORTS = 0`).
