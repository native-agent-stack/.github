# ADR-0007: Dual-Machine Orca Workstation Mesh, Shared-VM WSL2 Isolation & Meridian Successor Convergence

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Multi-Machine Execution & Org Convergence (`L0` × `L1` × `L8` × `L9`)
- **Evidence Grade:** E4 (`sota-doctor` `11/11` + `sota-org-doctor --live` `22/22` Verified)
- **GitHub Evidence:** https://github.com/stablyai/orca, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-harness-foundation, https://github.com/gitleaks/gitleaks
- **Revisit Trigger:** 2027-02-16

## Context and Problem Statement

The `native-agent-stack` organization operates across a portable Apple M5 Max (`64 GB` RAM) lead workstation and a paired stationary Threadripper (`64` cores, `128 GB` RAM, RTX 4090, `100.110.115.22`) heavy workstation undergoing a clean `meridian` WSL2 distro reset (`meridian` `ADR-0055` & `ADR-0056`).

## Decision Outcome

1. **18-Repository Dual-Machine Provisioning & Offline Autonomy:** Provision all `18` active `native-agent-stack` repositories under `C:/sota-workstation/*` on the stationary Orca server while keeping the portable M5 Max 100% self-sufficient when carried offline, governed by `singleActiveBrokerHostOnly = true`.
2. **Shared-VM WSL2 & Gateway Firewalls (`ADR-0021` / `ADR-0053`):** Forbid `wsl --shutdown` and mutations to co-resident `sextant` / `D:` / `Z:`; forbid unauthenticated Tailscale Serve proxying of loopback model gateways; forbid pairing `ANTHROPIC_BASE_URL` with `CLAUDE_CODE_OAUTH_TOKEN`.
3. **Full Ecosystem Handoff Seal:** Converge `meridian` (`54` ADRs), `tsl` (`17` ADRs), `sota-private-vault` (`7` ADRs), `cc-sota-harness` (`21` ADRs), `sota-harness-foundation` (`21` ADRs), `agy-sota-harness` (`15` ADRs), and `native-agent-stack` (`7` ADRs) into `ECOSYSTEM_ORG_MANIFEST.json`.

## Alternatives Considered

1. **Single-host-only repository provisioning:** Rejected — prevents seamless cross-machine Orca worker supervision and lid-closed parked execution.

## Verification Witness

- `python3 scripts/merge_gate.py` -> `PASS`
- `sota-org-doctor --live` -> `PASS (22 repos, 0 violations)`
