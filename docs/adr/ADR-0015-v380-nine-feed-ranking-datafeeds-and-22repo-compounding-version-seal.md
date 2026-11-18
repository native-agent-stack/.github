# ADR-0015: `v3.8.0` Nine-Feed PIT Ranking DataFeeds (`DF1`–`DF9`), Two-Track Compounding Versioning & 22-Repo Governance Seal

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Organization-Wide Control Plane, 9-Feed PIT Ranking Lineage, Two-Track Compounding Versioning & Dual-Machine Orca Governance (`L0–L12` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (`9/9` Public GitHub Actions `SUCCESS`, `22/22` `sota-org-doctor --live` `PASS`, `9` PIT Ranking Feeds `DF1..DF9`, `16` Canonical + `6` `agy` Workflows, `17` Ranker MCP Tools, `90` HLZ Trials & `62` Lessons Verified)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/agy-sota-harness, https://github.com/native-agent-stack/sota-multi-model-workflows, https://github.com/native-agent-stack/sota-compounding-lab, https://github.com/native-agent-stack/sota-harness-foundation, https://github.com/native-agent-stack/sota-upstream-shelf-lock, https://github.com/QuantConnect/Lean
- **Revisit Trigger:** 2027-01-02

## Context and Problem Statement

Following `ADR-0014` (`v3.7.0` Stage-B `Noesis-Carbon` closure, symmetric `:6770` Orca mesh, and `Trial #90`), coordinated multi-peer landings finalized the 9-feed point-in-time whole-market ranking specification (`sota-ranking-datafeeds.v3.8`, `DF1`–`DF9`), Vega (2006) / Tetlock (2007) catalyst surprise scoring (`sota-mover-ranker @ e0375c51`), deterministic `sota-version` 4-hash compounding release manifests (`sota-harness-foundation`, `sota-compounding-lab`, `meridian` `ADR 0060`, `canon` `0178`), `16` canonical + `6` native `agy` workflows (`sota-multi-model-workflows @ 283d9e50`, `agy-sota-harness @ d2e7ada2`), `sota-private-vault` `ADR-0011` (`1b78cc66`, `62` lessons), and cross-OS `orca.yaml` workspace recipes across all Trading Lane and Harness Lane repositories.

## Decision Outcome

1. **Seal `ECOSYSTEM_ORG_MANIFEST.json` (`v3.8.0`, `15` Org ADRs) Across All `22` Repositories:**
   - Lock all `21` sibling 40-char `origin/main` `baselineSha` commits across `publicUnlimitedActionsTier` (`9` repos), `privateExecutionAndVaultTier` (`9` repos, `actionsEnabled = false`), and `coldArchivedSupersededTier` (`4` repos, `archived = true`, `actionsEnabled = false`), including `native-agent-stack @ 5cc51fcdfc43363f55a30f009c6ad2046d7b28be` (`ADR-0015`), `meridian @ e2153da7baf4ae82e49626e1cf21230c9e6598c6` (`57` ADRs), `canon @ 1a6bd8b61398cdb16df30d6216fa16b070eb7f0c` (`152` ADRs), `sota-mover-ranker @ e0375c513766c5a26b12238322f33e76fc590928` (`14` ADRs, `17` MCP tools, `9` PIT feeds), and `sota-private-vault @ 1b78cc667f722536d55b9b1e2dcadec855fd6385` (`11` ADRs, `90` HLZ trials, `62` lessons).
2. **Enforce `sota-ranking-datafeeds.v3.8` (`DF1`–`DF9`) & Two-Track Compounding Versioning (`sota-version`):**
   - Bind `DF4_xnys_tod_rvol_bucket_normalizer` (`Canon 0173`, `QuantConnect/Lean` `RelativeDailyVolume.cs` trailing `20`-session `XNYS` clock-bucket `RVOL_tod`) and `DF8_finra_rule4560_settled_short_interest_t8` (FINRA Rule 4560 `T+8` `XNYS` settled short interest) alongside the 7 `sota-research-feeds.v2` streams, and require 4-hash SHA-256 provenance (`input_lake_sha256`, `upstream_18_pins_sha256`, `ranking_9feeds_sha256`, `adr_id`) plus two-track promotion (`ALPHA_STRATEGY_MINOR` vs `PROTECTIVE_FILTER_OR_GOVERNANCE` at `N >= 90`, `t*(91) = 4.1760`) under `ADR-0022 <= 2.00%` stops and `100%` live-capital refusal.

## Alternatives Considered

1. **Leave `ECOSYSTEM_ORG_MANIFEST.json` at `v3.7.0` after landing `v3.8.0` sibling commits:** Rejected — `sota-org-doctor --live` requires exact 40-char `origin/main` parity across all `22` repositories.
2. **Promote `H090` passive-bid discoveries (`+20.84 bps` 1x, `5/5` `CPCV`) on the standalone minor alpha track without `DSR >= 0.95`:** Rejected — enforced via two-track `PROTECTIVE_FILTER_OR_GOVERNANCE` classification.

## Verification Witness

- `python3 scripts/architecture_catalog.py --sync-manifest` + `python3 scripts/merge_gate.py` -> `PASS` (`15` GitHub-evidenced MADR 4.0 ADRs & `ECOSYSTEM_ORG_MANIFEST.json` `v3.8.0` verified, `0` drift, `0` leaks).
- `python3 -m unittest discover -s tests -v` -> `PASS`.
- `9/9` public GitHub Actions `completed / success` & `22/22` `origin/main` 40-char SHA parity verified.
