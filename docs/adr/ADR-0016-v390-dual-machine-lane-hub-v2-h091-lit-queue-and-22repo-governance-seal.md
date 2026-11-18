# ADR-0016: `v3.9.0` Dual-Machine Orca Lane Hub v2, `Trial #91` (`H091`) Lit-Queue Law, `18/18` `UPSTREAM.md` Lineage & 22-Repo Governance Seal

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Organization Control Plane, 22-Repo 40-Char SHA Manifest, Dual-Machine Lane Hub v2 & Lit-Queue Microstructure Governance (`L0–L13` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (`22/22` Exact 40-Char `origin/main` SHA Parity, `9/9` Public GitHub Actions `SUCCESS`, `18/18` Active `UPSTREAM.md` + `orca.yaml`, `prewallLakeSha256` `a253421e8734...`, `91` Completed HLZ Trials & `65` Lessons Verified)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-multi-model-workflows, https://github.com/native-agent-stack/sota-harness-foundation, https://github.com/native-agent-stack/sota-mover-ranker, https://github.com/native-agent-stack/sota-dynamic-trail-c, https://github.com/native-agent-stack/astrolabe, https://github.com/stablyai/orca
- **Revisit Trigger:** 2027-01-02

## Context and Problem Statement

Following `ADR-0015` (`v3.8.0` 9-feed PIT ranking `DF1..DF9` and two-track compounding versioning), coordinated multi-peer engineering across `native-agent-stack` closed every remaining architectural, operational, and upstream-lineage gap for `v3.9.0`:
1. **Dual-Machine Orca Lane Hub v2 (`sota-dual-machine-lanes.v2` × `sota-orca-lane-hub.v2`):** Unified `T1..T5` Trading Lanes (`8` repos) and `H0..H7` Harness Lanes (`10` repos) across `Mac M5 Max`, `Noesis` Win32, and `* Noesis-Carbon` WSL2 (`100.110.115.22`), enforcing the RTH broker-contention shield and `14/14` (`L0`–`L13`) `sota-doctor` parity across all 3 surfaces.
2. **Complete `18/18` Active-Repo `UPSTREAM.md` + `orca.yaml` Lineage & Pre-Wall Lake SHA-256:** Bound `prewallLakeSha256 = "a253421e873441740d5d4b410d993cfa7345fe34b88ec4ab7f4eecd537b3f234"` (`<= 2026-10-15`) and standardized `UPSTREAM.md` registers across all `18` active repositories.
3. **`Trial #91` (`H091`) Lit-Only Round-Lot Queue Proof & Protective Entry Shield (`sota-mover-ranker` `ADR-0017`, `astrolabe` `ADR-0009`, `canon` `0179`, `meridian` `0060-record`):** Verified across `C(6,2) = 15` disjoint split `CPCV` windows (`286 / 435 = 65.75%` lit round-lot fill rate, `-23.732 bps` net 1x when relaxing past `<= 10 bps` / `OFI >= 0.25`), enforcing `<= 10 bps` spread + `OFI >= 0.25` + losing-streak cooldown shields (`N = 91 -> t*(92) = 4.1785`, `65` compiled lessons).
4. **Live RTH Opening Protection, Dual-Machine Zlib TV Mirror & Explicit `waited_gates` (`sota-mover-ranker @ 8560ae91`, `sota-dynamic-trail-c @ d1f68404` `ADR-0014`, `sota-private-vault @ 1b22476a` `ADR-0012`):** Hardened `09:30 ET` off-hours order purge, breached-stop rescue, `200 req/min` BOATS cancel pacer, `fcntl.flock` daemon exclusivity, `2s` Win32 Orca watchlist compression, and machine-readable `waited_gates` on `:8799/api/landscape`.

## Decision Outcome

1. **Seal `ECOSYSTEM_ORG_MANIFEST.json` at `schemaVersion = "3.9.0"` (`16` Org ADRs) Across All `22` Repositories:**
   - Lock all `21` sibling 40-char `origin/main` `baselineSha` commits (including `native-agent-stack @ 0b1323365200f789373a100825f80af8c7d1bf16`, `sota-mover-ranker @ 8560ae91a968bc5f6d48eec9bfd4abf688d709d3`, `sota-dynamic-trail-c @ d1f6840485e314c8c6c7a5b205032502c952e7b1`, `astrolabe @ 4879b03b90b4bf2cf09490aa29d2433102785aff`, and `sota-private-vault @ 1b22476a...`), record `prewallLakeSha256`, `dualMachineLanesSchema`, and `orcaLaneHubSchema`, and add `UPSTREAM.md` while keeping `13/13` private and cold-archived repositories at `actionsEnabled = false` (`0` paid CI burn).

## Alternatives Considered

1. **Leave `.github` on the intermediate auto-manifest PR commit without `ADR-0016`, `UPSTREAM.md`, or `v3.9.0` schema metadata:** Rejected — full MADR 4.0 and `22/22` `baselineSha` parity is required by `sota-org-doctor --live`.
2. **Enable GitHub Actions on private execution or vault repositories:** Rejected — violates `ADR-0001` zero-private-Actions-burn policy.

## Verification Witness

- `python3 scripts/architecture_catalog.py --sync-manifest` + `python3 scripts/merge_gate.py` -> `PASS` (`16` GitHub-evidenced MADR 4.0 ADRs & `ECOSYSTEM_ORG_MANIFEST.json` `v3.9.0` verified, `0` drift, `0` leaks).
- `python3 -m unittest discover -s tests -v` -> `PASS`.
- `22/22` live `origin/main` 40-char SHA parity (`total_mismatches = 0`) & `9/9` public GitHub Actions `completed / success` verified.
