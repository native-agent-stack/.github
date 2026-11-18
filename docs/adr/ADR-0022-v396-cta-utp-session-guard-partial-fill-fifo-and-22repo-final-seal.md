# ADR-0022: `v3.9.6` CTA/UTP Single-Session Guard (`ADR-0021`), Partial-Fill FIFO Attribution (`8e01ec17`) & 22-Repo Zero-Drift SHA Seal

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Organization Control Plane, 22-Repo 40-Char SHA Manifest & 3-Surface Zero-Lease Convergence (`L0–L13` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (`22/22` Exact 40-Char `origin/main` SHA Parity, `9/9` Public GitHub Actions, `94/94` `sota-mover-ranker` `pytest` & `54/54` Synced Checkouts)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-mover-ranker, https://github.com/native-agent-stack/sota-private-vault
- **Revisit Trigger:** 2026-12-06 (`23/5` SIP cutover) or next `ALPHA_STRATEGY_MINOR` promotion (`t >= 4.1858`, `DSR >= 0.95`)

## Context and Problem Statement

Following `ADR-0021` (`v3.9.5`), the final two active peer commits in `sota-mover-ranker` landed and released (`ADR-0021` CTA/UTP single-session guard @ `7de8ce22c57f` + partial-fill `filled_qty > 0` FIFO attribution & fast collars @ `8e01ec178404`, `94/94` `pytest` PASS), alongside `sota-private-vault` (`ADR-0017`, `77` lessons) and `native-agent-stack` (`ADR-0022`, `v3.9.6`).

## Decision Outcome

1. **Seal `ECOSYSTEM_ORG_MANIFEST.json` at `schemaVersion = "3.9.6"` (`22` Org ADRs) Across All `22` Repositories:**
   - Lock all `21` sibling live 40-char `origin/main` `baselineSha` digests (`total_mismatches = 0`) with `0` active peer leases remaining across the organization.

## Alternatives Considered

1. **Leave `ECOSYSTEM_ORG_MANIFEST.json` at `v3.9.5` (`fd572c09`):** Rejected — `22/22` exact live `origin/main` SHA parity is mandatory.

## Verification Witness

- `python3 scripts/architecture_catalog.py --sync-manifest` + `python3 scripts/merge_gate.py` + `python3 -m unittest discover -s tests -v` -> `PASS` (`22` ADRs, `0` drift, `0` leaks).
- `sota-org-doctor --live` -> `22/22` `MATCH` (`0` violations, `0` SHA drift).
