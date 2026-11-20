# ADR-0038: `v3.11.1` Post-ANT Whole-Market `DF1..DF12` Merit Ranking & Lossless Consolidation Org Seal

- **Status:** Accepted
- **Date:** 2026-11-20
- **Layer:** Organization Control Plane (`L0`), Two-Tier Public/Private Visibility & CI Firewall (`L9`), & `22`-Repo 40-Char SHA Manifest (`L0–L13` × `T1–T5`)
- **Evidence Grade:** E4 (`sota-mover-ranker@dd5a65aa` `ADR-0066` `66/66` ADRs `550 passed` + live reloaded `:8787` scanning `10,973` US symbols & `:6900` OpenBB HTTP 200 while Live `:8798`/`:8796` remained untouched, `sota-dynamic-trail-c@cc4348cf` `ADR-0030` `30/30` ADRs `231 passed` + live reloaded `:8799` HTTP 200, `astrolabe@801efa5a` `ADR-0016` `16/16` ADRs `97 passed` targeted / `2,489` full suite + `pyright 0`, `sota-multi-model-workflows@3b08855f` `ADR-0036` `36/36` ADRs `62 passed, 291 subtests passed`, `sota-compounding-lab@2235a827` `ADR-0028` `28/28` ADRs `290 passed, 4 skipped`, `native-agent-stack@1135dd7f` `ADR-0042` `42/42` ADRs `7 passed`, independent OpenAI Codex `gpt-6.2-astra` `xhigh` `VERDICT: PASS` with `0` findings across all 5 implementation repos, `38/38` Org MADR 4.0 ADRs, `sota-org-doctor --live` `22/22` zero-drift, `gitleaks 0` leaks)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack/commit/1135dd7f30d3c588edecc2679f5f7e9fb6d58a53, https://github.com/native-agent-stack/sota-mover-ranker/commit/dd5a65aa4bd99a8b09b808154beb797e5f1280df, https://github.com/native-agent-stack/sota-dynamic-trail-c/commit/cc4348cfd1d2c78749f505a73cbbfd65b5d05cff, https://github.com/native-agent-stack/astrolabe/commit/801efa5a5706c606a60fe0c9577702624056b26e, https://github.com/native-agent-stack/sota-multi-model-workflows/commit/3b08855f9c39a8b77d0ff24d872ef97cd1a66eed, https://github.com/native-agent-stack/sota-compounding-lab/commit/2235a8273060cf2336a0b38d3a11fba9ac89f13a
- **Revisit Trigger:** `2026-12-06` `21:00 ET` consolidated `23/5` SIP cutover verification, pre-registration of `Trial #105` (`t*(105) = 4.2084`), or next `native-agent-stack` umbrella milestone beyond `v3.11.1`.

## Context and Problem Statement

The `v3.11.1` Post-ANT consolidation wave landed six coordinated repositories on `origin/main` (`sota-mover-ranker` `ADR-0066`, `sota-dynamic-trail-c` `ADR-0030`, `astrolabe` `ADR-0016`, `sota-multi-model-workflows` `ADR-0036`, `sota-compounding-lab` `ADR-0028`, and `native-agent-stack` `ADR-0042`) after independent read-only OpenAI Codex `gpt-6.2-astra` `xhigh` audits achieved `0` P0/P1 findings across every implementation repository and Paper-only `:8787`, `:8799`, and `:6900` were reloaded and verified empirically while Live `:8798`/`:8796` remained untouched. `ECOSYSTEM_ORG_MANIFEST.json` needed promotion to `schemaVersion: "3.11.1"` locking all exact `origin/main` 40-char SHAs and `38/38` Org MADR 4.0 ADRs with zero drift.

## Decision Outcome

1. **Seal `ECOSYSTEM_ORG_MANIFEST.json` at `schemaVersion: "3.11.1"` (`22/22` Repositories):** Lock exact `origin/main` 40-char `baselineSha` hashes for `native-agent-stack@1135dd7f30d3c588edecc2679f5f7e9fb6d58a53`, `sota-mover-ranker@dd5a65aa4bd99a8b09b808154beb797e5f1280df`, `sota-dynamic-trail-c@cc4348cfd1d2c78749f505a73cbbfd65b5d05cff`, `astrolabe@801efa5a5706c606a60fe0c9577702624056b26e`, `sota-multi-model-workflows@3b08855f9c39a8b77d0ff24d872ef97cd1a66eed`, and `sota-compounding-lab@2235a8273060cf2336a0b38d3a11fba9ac89f13a` while preserving strict Two-Tier Public/Private/Archived boundaries (`9/9/4`, `actionsEnabled: false` across all `9` `PRIVATE` and `4` `ARCHIVED` repos).
2. **Preserve Live Execution & Pre-Wall Scientific Firewalls:** Maintain `liveCapitalHardRefused: true`, `maxInitialStopPctAdr0022: 2.0`, `studyWallDate: "2026-10-15"`, strict `PROTECTIVE_FILTER_OR_GOVERNANCE` classification (`standalone_alpha_claim: false`), and honest HLZ accounting (`104` trials completed, `Trial #105` unspent at `t*(105) = 4.2084`).
3. **Sync Org MADR 4.0 Catalog & Manifest (`38/38` ADRs):** Regenerate `docs/adr/CATALOG.md` and `ECOSYSTEM_ORG_MANIFEST.json` `adrGovernance` via `scripts/architecture_catalog.py --sync-manifest` and verify zero drift via `scripts/merge_gate.py`, `unittest`, `sota-org-doctor --live`, and `gitleaks`.

## Alternatives Considered

- **Leaving `ECOSYSTEM_ORG_MANIFEST.json` at `schemaVersion: "3.11.0"`:** Rejected because six `v3.11.1` commits are already landed on `origin/main` and unsealed manifest baselines cause org drift.

## Verification Witness

- `python scripts/architecture_catalog.py --sync-manifest` & `--check` (`38/38` GitHub-evidenced MADR 4.0 ADRs verified, `0` drift).
- `python scripts/merge_gate.py`, `python -m unittest discover -s tests -v`, `sota-org-doctor --live` (`22/22` PASS, `0` violations), and `gitleaks protect --staged --redact --no-banner` (`0` leaks).
