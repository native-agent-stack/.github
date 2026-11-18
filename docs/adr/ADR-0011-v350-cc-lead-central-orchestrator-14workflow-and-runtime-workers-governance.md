# ADR-0011: v3.5.0 Claude Code (`cc-lead`) Central Multi-Session Orchestrator, 14-Workflow Hub & 22-Repo Runtime Worker Governance

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Full-Ecosystem Multi-Runtime Orchestration, Research & Trading Control Plane (`L0–L12` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (14 Workflows, 15/15 Hub Binaries, 28 Runtimes, 89 Trials, 51 Lessons, `sota-doctor` 12/12 & `sota-org-doctor --live` 22/22 Verified)
- **GitHub Evidence:** https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-multi-model-workflows, https://github.com/native-agent-stack/sota-harness-foundation, https://github.com/native-agent-stack/sota-compounding-lab, https://github.com/stablyai/orca, https://github.com/ComposioHQ/agent-orchestrator, https://github.com/aannoo/hcom
- **Revisit Trigger:** 2027-01-02

## Context and Problem Statement

Building on `ADR-0010` (`v3.4.0` `424`-entry research convergence and lease-safe bidirectional Orca v2.0 co-op), the `native-agent-stack` organization control plane needed to seal `v3.5.0` across all `22` repositories (`9 PUBLIC` unlimited GitHub Actions + `9 PRIVATE` execution/vault `actionsEnabled: false` + `4 PRIVATE` cold-archived seals), establishing Claude Code (`cc-lead`, `claude-fable-5-2` `xhigh` + `oh-my-claudecode` `OMC` Runtime v2) as the sovereign central multi-session orchestrator commanding heterogeneous runtime workers (`Codex OMX`, `Orca`, `Antigravity/Gemini`, `OpenCode OMO`, `DeepSeek DSH`, `Pi/OMP`, `Goose`, and `hcom`).

## Decision Outcome

1. **Claude Code (`cc-lead`) Central Orchestrator & 14-Workflow `v3.5.0` Suite:**
   - Seal `sota-multi-model-workflows` (`ADR-0012` `@ 3312afa5aa92`, `14` workflows including `cc_lead_multi_runtime_workers_workflow.py` `#14` and `src/sota_mmw/cc_lead_hub.py`), `sota-harness-foundation` (`ADR-0026` `@ 069e47db8824`, `26` ADRs, `28` runtimes in `config/multi-model-routing.json v1.1.0`), `cc-sota-harness` (`@ d7fe7d3d2fff`, `25` ADRs), `sota-private-vault` (`ADR-0009` `@ 0ad8a059d063`, `89` pre-registered trials `t*(90) = 4.1735`, `51` `E1–E4` lessons), and `native-agent-stack` (`ADR-0011`, `v3.5.0` `ECOSYSTEM_CONVERGENCE_LOCK.json`).
   - Enforce five coordinated runtime worker channels under `oneModelPerConversation = true`: (1) `omc ultragoal create-goals` + `/goal` Stop-hook, (2) `OMC_RUNTIME_V2=1 OMC_TEAM_WORKTREE_MODE=branch omc team` + `Claude OMC <-> Codex OMX` interop, (3) `omc ask` + `omx exec` (`>= 3` concrete frontier vendors `anthropic`, `openai`, `google`), (4) reactive `orca orchestration worker-start --worktree new-child --repo id:<uuid>` across `Mac M5 Max` and `Noesis` (`100.110.115.22`), and (5) non-GPT `OMO` `kimi-k3.1-pro` `Hephaestus` + `DSH` `deepseek-v4-pro` pre-wall (`<= 2026-10-15`) + `hcom` + comma/glob-aware `sota-bus` lease collision guards.
2. **Preserve Zero-Quota-Burn Two-Tier Visibility & Paper-Only Execution Firewall:**
   - Keep all `9` proprietary execution/vault repositories and `4` cold-archived seals `PRIVATE` with `actionsEnabled = false` (`0` paid GitHub Actions minutes burned) and all autonomous trading strictly on `Alpaca Paper <= 200 req/min` and `IBKR Paper :4002 <= 3,000 msg/min` (`2,700` entry / `300` protective-exit reserve, `ADR-0022 <= 2.00%` stop).

## Alternatives Considered

1. **Allow multi-model hot-swapping inside a single `cc-lead` session:** Rejected — invalidates Anthropic prompt caches and breaks clean vendor attribution (`oneModelPerConversation = true`).
2. **Poll child worker terminals in busy loops:** Rejected — `stablyai/orca` `worker_done` / `send` / `gate-create` and `hcom` push messaging wake the coordinator reactively with zero token waste.

## Verification Witness

- `python3 scripts/architecture_catalog.py --sync-manifest` + `python3 scripts/merge_gate.py` -> `PASS` (`11` GitHub-evidenced MADR 4.0 ADRs & `ECOSYSTEM_ORG_MANIFEST.json` `v3.5.0` verified, `0` drift, `0` leaks).
- `python3 -m unittest discover -s tests -v` -> `PASS`.
- Live `run_workflow` on `cc_lead_multi_runtime_workers_workflow.py` (`plan_sha256 = 678fc0cf289b00fd85f7e23a7b5c300b1284fbd1f60c0abe62a9280a0524a5d7`), `sota-doctor` (`12/12 PASS`), & `sota-org-doctor --live` (`22/22 PASS`, `0` violations).
