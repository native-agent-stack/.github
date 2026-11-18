# ADR-0017: `v3.9.1` `H092`+`H093` Overnight Whipsaw Law (`7,473` Events), Live `:8787` Pipe-Deadlock/Shield Fix & 22-Repo SHA Seal

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Organization Control Plane, 22-Repo 40-Char SHA Manifest, Pre-Wall Volatility-Scaling Governance & Live RTH Reliability (`L0–L13` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (`22/22` Exact 40-Char `origin/main` SHA Parity, `9/9` Public GitHub Actions `SUCCESS`, `93` Pre-Registered HLZ Trials, `69` Compiled Lessons & `:8787`/`:8799` `HTTP 200` Verified)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-mover-ranker, https://github.com/native-agent-stack/sota-private-vault, https://github.com/native-agent-stack/sota-compounding-lab, https://github.com/native-agent-stack/dsh-sota-harness
- **Revisit Trigger:** 2027-01-02

## Context and Problem Statement

Following `ADR-0016` (`v3.9.0`), peer sessions landed `sota-mover-ranker @ e8eebd7a0570` (`81/81` `pytest` PASS: eliminating the `64KB` macOS MCP `stderr=PIPE` + blocking `readline` deadlock, wiring `ADR-0017` `protective_entry_shield` + `alloc_mult` into `alpaca_paper_e2e.py`, and blocking `1`-share dust crumbs) alongside `Trials #92`–`#93` (`H092` + `H093` `7,473`-event Kaminski–Lo overnight `-200 bps` stop-whipsaw twin proof, advancing `N = 93 -> t*(94) = 4.1834` and `69` compiled root-cause lessons).

## Decision Outcome

1. **Seal `ECOSYSTEM_ORG_MANIFEST.json` at `schemaVersion = "3.9.1"` (`17` Org ADRs) Across All `22` Repositories:**
   - Lock every 40-char `origin/main` `baselineSha` across `publicUnlimitedActionsTier` (`9` repos), `privateExecutionAndVaultTier` (`9` repos, `actionsEnabled = false`), and `coldArchivedSupersededTier` (`4` repos, `archived = true`, `actionsEnabled = false`) — including `sota-mover-ranker @ e8eebd7a05702472767d33651db55fa3da4bd2bd`, `sota-private-vault` `ADR-0013`, and `native-agent-stack` `ADR-0017` — achieving `total_mismatches = 0` and `9/9` public GitHub Actions `SUCCESS`.

## Alternatives Considered

1. **Leave `ECOSYSTEM_ORG_MANIFEST.json` with a `1`-repo SHA mismatch on `sota-mover-ranker`:** Rejected — zero SHA drift (`22/22` `MATCH`) is a hard organizational invariant.

## Verification Witness

- `python3 scripts/architecture_catalog.py --sync-manifest` + `python3 scripts/merge_gate.py` + `python3 -m unittest discover -s tests -v` -> `PASS` (`17` ADRs, `0` drift, `0` leaks).
- `22/22` live `origin/main` SHA `MATCH` (`total_mismatches = 0`) & `9/9` public GitHub Actions `completed / success`.
