# ADR-0037: `v3.11.0` Upstream-First `24/5` OpenBB Terminal, Shared `LosslessProtectionKernel`, Paper Quarantine & Pre-Wall Alpha Factory (`Trial #104`) Org Seal

- **Status:** Accepted
- **Date:** 2026-11-20
- **Layer:** Organization Control Plane (`L0`), Two-Tier Public/Private Visibility & CI Firewall (`L9`), & `22`-Repo 40-Char SHA Manifest (`L0–L13` × `T1–T5`)
- **Evidence Grade:** E4 (`sota-upstream-shelf-lock@e3549753` `ADR-0018` `18/18` ADRs `20 passed`, `sota-compounding-lab@00178c12` `ADR-0027` `27/27` ADRs `289 passed, 4 skipped` + live WSL2 `Trial #104` receipt `5e073f98...`, `sota-dynamic-trail-c@d89ce3ac` `ADR-0029` `29/29` ADRs `230 passed`, `sota-mover-ranker@67f78638` `ADR-0062..0065` `65/65` ADRs `419 passed` + live Paper `24/5` `OVERNIGHT_BOATS` `QQQ` receipt + 12/12 live HTTP endpoints verified while Live `:8798`/`:8796` remained untouched, `native-agent-stack@8edc98a4` `ADR-0041` `41/41` ADRs `6 passed`, independent OpenAI Codex `gpt-6.2-astra` `VERDICT: PASS` across all 4 implementation repos, `37/37` Org MADR 4.0 ADRs, `sota-org-doctor --live` `22/22` zero-drift, `gitleaks 0` leaks)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack/commit/8edc98a4393786b1d1c7f3a040462851a4504fc0, https://github.com/native-agent-stack/sota-upstream-shelf-lock/commit/e3549753294874eaf4d388119ff7053c308794dd, https://github.com/native-agent-stack/sota-compounding-lab/commit/00178c12fbf318dbf4ae5ab9e59a374ba5a3a921, https://github.com/native-agent-stack/sota-dynamic-trail-c/commit/d89ce3acf0ff9c4468b790c2df4fffb8a99c3879, https://github.com/native-agent-stack/sota-mover-ranker/commit/67f786382ad81c0de3a518c23330552d55592530, https://github.com/microsoft/qlib, https://github.com/OpenBB-finance/backends-for-openbb
- **Revisit Trigger:** `2026-12-06` `21:00 ET` consolidated `23/5` SIP cutover verification, pre-registration of `Trial #105` (`t*(105) = 4.2084`), or next `native-agent-stack` umbrella milestone beyond `v3.11.0`.

## Context and Problem Statement

The `v3.11.0` architectural wave landed five coordinated repositories on `origin/main` (`sota-upstream-shelf-lock` `ADR-0018`, `sota-compounding-lab` `ADR-0027`, `sota-dynamic-trail-c` `ADR-0029`, `sota-mover-ranker` `ADR-0062..ADR-0065`, and `native-agent-stack` `ADR-0041`) after independent read-only OpenAI Codex `gpt-6.2-astra` `VERDICT: PASS` verification, real Paper `24/5` `OVERNIGHT_BOATS` live fill verification, live WSL2 Pre-Wall `Trial #104` falsification (`FAILED` -> `PROTECTIVE_FILTER_OR_GOVERNANCE`, `PBO = 0.60`), and 12/12 live HTTP endpoint proofs with Live `:8798`/`:8796` untouched. `ECOSYSTEM_ORG_MANIFEST.json` needed promotion to `schemaVersion: "3.11.0"` locking all exact `origin/main` 40-char SHAs and `37/37` Org MADR 4.0 ADRs with zero drift.

## Decision Outcome

1. **Seal `ECOSYSTEM_ORG_MANIFEST.json` at `schemaVersion: "3.11.0"` (`22/22` Repositories):** Lock exact `origin/main` 40-char `baselineSha` hashes for `native-agent-stack@8edc98a4393786b1d1c7f3a040462851a4504fc0`, `sota-upstream-shelf-lock@e3549753294874eaf4d388119ff7053c308794dd`, `sota-compounding-lab@00178c12fbf318dbf4ae5ab9e59a374ba5a3a921`, `sota-dynamic-trail-c@d89ce3acf0ff9c4468b790c2df4fffb8a99c3879`, and `sota-mover-ranker@67f786382ad81c0de3a518c23330552d55592530` while preserving strict Two-Tier Public/Private/Archived boundaries (`9/9/4`, `actionsEnabled: false` across all `9` `PRIVATE` and `4` `ARCHIVED` repos).
2. **Preserve Live Execution & Pre-Wall Scientific Firewalls:** Maintain `liveCapitalHardRefused: true`, `maxInitialStopPctAdr0022: 2.0`, `studyWallDate: "2026-10-15"`, and honest HLZ accounting (`Trial #104` `FAILED` -> `PROTECTIVE_FILTER_OR_GOVERNANCE`, `t*(105) = 4.2084`).
3. **Sync Org MADR 4.0 Catalog & Manifest (`37/37` ADRs):** Regenerate `docs/adr/CATALOG.md` and `ECOSYSTEM_ORG_MANIFEST.json` `adrGovernance` via `scripts/architecture_catalog.py --sync-manifest` and verify zero drift via `scripts/merge_gate.py`, `unittest`, `sota-org-doctor --live`, and `gitleaks`.

## Alternatives Considered

- **Leaving `ECOSYSTEM_ORG_MANIFEST.json` at `schemaVersion: "3.10.10"`:** Rejected because five `v3.11.0` commits are already landed on `origin/main` and unsealed manifest baselines cause org drift.

## Verification Witness

- `python scripts/architecture_catalog.py --sync-manifest` & `--check` (`37/37` GitHub-evidenced MADR 4.0 ADRs verified, `0` drift).
- `python scripts/merge_gate.py`, `python -m unittest discover -s tests -v`, `sota-org-doctor --live` (`22/22` PASS, `0` violations), and `gitleaks protect --staged --redact --no-banner` (`0` leaks).
