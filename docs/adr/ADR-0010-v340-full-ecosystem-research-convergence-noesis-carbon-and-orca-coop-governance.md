# ADR-0010: v3.4.0 Full-Ecosystem Research Convergence, Clean `Noesis-Carbon` WSL2 Guest & Lease-Safe Orca v2.0 Co-op Governance

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Full-Ecosystem Research, Workstation & Trading Control Plane (`L0–L12` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (88 Pre-Registered Trials, 51 Lessons, 56 Meridian ADRs, Live Dual-Workstation Orca v2.0 Co-op & 22-Repo Org Doctor Verified)
- **GitHub Evidence:** https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-compounding-lab, https://github.com/native-agent-stack/astrolabe, https://github.com/native-agent-stack/sota-harness-foundation, https://github.com/stablyai/orca, https://github.com/ComposioHQ/agent-orchestrator, https://github.com/nkaz001/hftbacktest, https://github.com/golang/mod
- **Revisit Trigger:** 2027-01-02

## Context and Problem Statement

Building on `ADR-0009` (`v3.3.0` 7-feed `sota-research-feeds.v2` PIT surface and `85`-trial HLZ governance), the `native-agent-stack` organization control plane needed to seal `v3.4.0` across all `22` repositories (`9 PUBLIC` unlimited GitHub Actions + `9 PRIVATE` execution/vault `actionsEnabled: false` + `4 PRIVATE` cold-archived seals) as the stationary `Noesis` workstation (`Threadripper 64c / 128 GB / RTX 4090`) brought up its clean `Ubuntu 26.04.1` `Noesis-Carbon` WSL2 guest alongside its hardened headless `orca serve` daemon and cooperated live with the portable Apple M5 Max (`64 GB`) lead cockpit.

## Decision Outcome

1. **424-Repository Research-Converged ADR Closure Across All Tiers (`v3.4.0`):**
   - Seal the `424`-entry research-converged catalog (`404` owner-starred + `20` evaluated repositories in `Meridian` `docs/adr/data/ecosystem-manifest.md`) across `native-agent-stack` (`ADR-0010` `@ 479f7f2d5fc6`), `Meridian` (`0058`–`0059` `@ ce99430fdfa8`, `56` ADRs), `sota-compounding-lab` (`ADR-0007` `@ f252bdb6fdb2`, `golang/mod` `dirhash` snapshot locks + `learnharness`/`LoopForge` postmortem compounding), `astrolabe` (`ADR-0005` `@ e1023b3e568a`, `hftbacktest::RiskAdverseQueueModel` `100x` CTA/UTP round-lot queue parity + `300 msg/min` IBKR `:4002` exit reserve), `dsh-plugin-landscape` (`ADR-0004` `@ 0703d7504731`), `sota-harness-foundation` (`@ 601f58a4fb70`, explicit Stage B owner cutover guard `stage_b_cutover_authorized`), `sota-upstream-shelf-lock` (`@ 919236e98cba`), `sota-multi-model-workflows` (`@ 76efbb8f2c87`), `agy-sota-harness` (`@ aee8325c22f4`), `dsh-sota-harness` (`@ 39c00cd63e7a`), `cc-sota-harness` (`@ 5ab50ed6b369`), `sota-mover-ranker` (`@ 0439c907a148`), `sota-dynamic-trail-c` (`@ 2f12839aa515`), `sota-private-vault` (`@ 39f0e3f71de0`), and `legacy-movers-202611` (`@ cd48e646cc26`).
   - Advance organization-wide statistical governance to `N >= 88` pre-registered trials (`t*(89) >= 4.1709`) and `51` compiled `E1–E4` root-cause lessons.
2. **SOTA Dual-Workstation Orca Co-op Practice (`sota-workstation v2.0.0` + `Noesis-Carbon`):**
   - Standardize hardened headless `orca serve --no-pairing --refuse-public` over Tailscale on stationary `Noesis` with 1-packet Tailscale idle UDP tunnel wakeup before WebSocket RPC, `ConPTY`-wrap-proof Base64 co-op messaging (`coop --inbox`, `--send`, `--sync-refs`), and remote + local `sota-bus` lease-safe fast-forward repo/workflow sync (`singleActiveBrokerHostOnly: true`).
   - Seal the deterministic multi-worker (`-n 8`) Linux/WSL2 headless Chromium `requestAnimationFrame` unthrottling fix in `Meridian` (`--disable-renderer-backgrounding`, `--disable-background-timer-throttling`, `--disable-backgrounding-occluded-windows`, `--disable-dev-shm-usage` + `xdist_group("chart_browser")` under `--dist loadgroup`, receipt `PR #9` `#6969139023`).

## Alternatives Considered

1. **Unconditional remote `git pull` across paired Orca workstations:** Rejected — clobbers in-flight remote worktrees or active `24/5` guardian leases; solved by querying remote SQLite WAL `peer_bus.db` `active_leases` and `git status --porcelain` before fast-forwarding.
2. **Line-delimited JSON scraping over Windows `ConPTY` terminals:** Rejected — `ConPTY` wraps output lines at terminal column boundaries; solved deterministically via whitespace-insensitive `@@B64:` Base64 framing.

## Verification Witness

- `python3 scripts/architecture_catalog.py --sync-manifest` + `python3 scripts/merge_gate.py` -> `PASS` (`10` GitHub-evidenced MADR 4.0 ADRs & `ECOSYSTEM_ORG_MANIFEST.json` `v3.4.0` verified, `0` drift, `0` leaks).
- `python3 -m unittest discover -s tests -v` -> `PASS`.
- `sota-workstation v2.0.0` (`status`, `sync --repo all`, `coop --inbox --sync-refs --send`), `sota-doctor` (`11/11 PASS`), & `sota-org-doctor --live` (`22/22 PASS`, `0` violations).
