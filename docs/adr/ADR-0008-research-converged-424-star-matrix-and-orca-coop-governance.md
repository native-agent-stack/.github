# ADR-0008: 424-Row Starred & Research-Converged Upstream Matrix + Bidirectional `agy` Orca Co-op Governance

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Research Convergence & Dual-Workstation Co-op (`L0–L12` × `T0–T8`)
- **Evidence Grade:** E4 (`sota-org-doctor --live` `22/22` + Live E2EE Orca Co-op Verified)
- **GitHub Evidence:** https://github.com/stablyai/orca, https://github.com/QuantConnect/Lean, https://github.com/nkaz001/hftbacktest, https://github.com/ml4t/diagnostic, https://github.com/skfolio/skfolio, https://github.com/golang/mod, https://github.com/massive-com/client-python, https://github.com/louislam/uptime-kuma
- **Revisit Trigger:** 2027-02-16 or addition of new starred upstream dependencies

## Context and Problem Statement

`native-agent-stack` spans `22` repositories (`9 PUBLIC` unlimited GitHub Actions + `9 PRIVATE` zero-Actions-burn active repos + `4 PRIVATE` cold-archived seals) and two paired Orca workstations (`Apple M5 Max` portable lead `<->` `Noesis 64c/128GB/RTX4090` stationary heavy), requiring every quantitative gate and cross-workstation Antigravity (`agy`) session to share one commit-pinned upstream matrix.

## Decision Outcome

1. **Commit-Pinned Research-Converged Upstream Matrix (`Canon 0169..0176` + `Shelf-Lock ADR-0004` + `Compounding-Lab ADR-0006` + `Meridian #224` `424` Rows):**
   - Enforce `RFC-8493` BagIt + `golang/mod` `dirhash` `h1` snapshot digests, `ml4t/diagnostic` ADIA Lab `#19` `MinTRL`/`MDE` pre-registration power gates (`distinct_dates >= 60`), `hftbacktest` `RiskAdverseQueueModel` passive queue simulation, `QuantConnect/Lean` `RelativeDailyVolume.cs` cumulative same-time-of-day `RVOL`, `massive-com/client-python` PIT delisted-ticker verification, `<= 8`-symbol/`<= 8h` isolated `BOATS` bounds pre-`2026-12-06` `23/5` SIP, and `404` starred + `20` evaluated upstream placements across Layers `0–11`.
2. **Bidirectional Dual-Workstation `agy` Orca Co-op (`sota-workstation coop`, `ADR-0022`):**
   - Provision `~/.agents/bus/peer_bus.db`, `~/.agents/bin/sota-bus`, `~/.agents/bin/sota-workstation`, and `~/.agents/workflows/*` on both workstations, exchanging `agy <-> agy` handovers and inbox messages over E2EE Orca (`sota-workstation coop send|sync`) alongside `orca worktree set --comment` and `orca reference add`.

## Alternatives Considered

1. **Unindexed ad-hoc upstream adoption without MADR 4.0 or `dirhash` snapshot records:** Rejected — causes irreproducible backtests and cross-repo schema drift.

## Verification Witness

- `python3 scripts/merge_gate.py` -> `PASS`
- `sota-org-doctor --live` -> `PASS (22 repos, 0 violations)`
