# ADR-0023: `v3.9.7` Trial `#95` (`H095`), `:8787`/`:8799` `ADR-0022`/`0019`, `27/27` Runtimes & 22-Repo Zero-Drift SHA Seal

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Organization Control Plane, 22-Repo 40-Char SHA Manifest & 3-Surface Zero-Lease Convergence (`L0–L13` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (`22/22` Exact 40-Char `origin/main` SHA Parity, `95` HLZ Trials, `27/27` Runtimes & `54/54` Synced Checkouts)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-mover-ranker, https://github.com/native-agent-stack/sota-dynamic-trail-c, https://github.com/native-agent-stack/sota-compounding-lab
- **Revisit Trigger:** 2026-12-06 (`23/5` SIP cutover) or next `ALPHA_STRATEGY_MINOR` promotion (`t >= 4.1882`, `DSR >= 0.95`)

## Context and Problem Statement

Following `ADR-0022` (`v3.9.6`), all `15` sibling repositories plus `sota-private-vault` (`ADR-0018`, `da0190f43391`) and `native-agent-stack` (`ADR-0023`, `bbdbd274ff10`) converged on `v3.9.7` (`Trial #95` `H095` two-stage collar bifurcation, `:8787` `ADR-0022` Cloud MCP sync, `:8799` `ADR-0019` 24-symbol blotter, `cc-sota-harness` `4/4` Win32 MCP & `27/27` runtime parity).

## Decision Outcome

1. **Seal `ECOSYSTEM_ORG_MANIFEST.json` at `schemaVersion = "3.9.7"` (`23` Org ADRs) Across All `22` Repositories:**
   - Lock all `21` sibling live 40-char `origin/main` `baselineSha` digests (`total_mismatches = 0`) with `0` active peer leases remaining across the organization.

## Alternatives Considered

1. **Leave `ECOSYSTEM_ORG_MANIFEST.json` at `v3.9.6`:** Rejected — `22/22` exact live `origin/main` SHA parity is mandatory.

## Verification Witness

- `python3 scripts/architecture_catalog.py --sync-manifest` + `python3 scripts/merge_gate.py` + `python3 -m unittest discover -s tests -v` -> `PASS` (`23` ADRs, `0` drift, `0` leaks).
- `sota-org-doctor --live` -> `22/22` `MATCH` (`0` violations, `0` SHA drift).
