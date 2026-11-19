# ADR-0035: `v3.10.8` 22-Repo Zero-Drift Orca SOTA Worker Defaults, 60-Skill Red-Team/SkillEvaluator & 415-Starred Org Seal

- **Status:** Accepted
- **Date:** 2026-11-19
- **Layer:** Organization Control Plane, Dual-Machine Orca Worker Defaults (`1.4.263`), Red-Team Security & 4-Tier SkillEvaluator (`ADR-0043`), `60` Skills, `21` Workflows, `15` Standing Automations & `415+8` Starred Org Seal (`L0–L13` × `H1–H3`)
- **Evidence Grade:** E4 (`sota-harness-foundation@da6b90a3` `ADR-0043`, `sota-multi-model-workflows@3e60a76c` `ADR-0033`, `sota-upstream-shelf-lock@ce5f5ac6` `ADR-0015`, `agy-sota-harness@ed05b00c` `ADR-0034`, `cc-sota-harness@fa053bfc` `ADR-0041`, `native-agent-stack@63798ba1` `ADR-0035`, `35/35` MADR 4.0 ADRs, `merge_gate.py` + `unittest` + `gitleaks` `0` Leaks)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-harness-foundation, https://github.com/native-agent-stack/sota-multi-model-workflows, https://github.com/native-agent-stack/sota-upstream-shelf-lock, https://github.com/native-agent-stack/agy-sota-harness, https://github.com/native-agent-stack/cc-sota-harness, https://github.com/elementalsouls/Claude-BugHunter, https://github.com/NVIDIA/SkillEvaluator, https://github.com/Tencent/LoopForge
- **Revisit Trigger:** Addition of canonical runtime skills beyond `60`, Orca workflow changes beyond `21`, or modification of immutable `18`-pin `40`-char SHAs in `sota-upstream-shelf-lock`.

## Context and Problem Statement

`v3.10.8` landed across `sota-harness-foundation`, `sota-multi-model-workflows`, `sota-upstream-shelf-lock`, `agy-sota-harness`, `cc-sota-harness`, and `native-agent-stack` (`60` canonical skills with Red-Team BugHunter + 4-tier SkillEvaluator + LoopForge convergence, `parabolic-short-trade-planner` fail-closed `paper=True`, Workflow `#21` `redteam-skilleval-convergence-loop`, explicit non-stale SOTA `--extra-agent-args` across dual-machine Orca automations, and `STARRED_CONVERGENCE_CATALOG.json` covering `415` owner stars + `8` beyond-starred frameworks). `ECOSYSTEM_ORG_MANIFEST.json` required updating all baseline commit SHAs, workflow/automation/star counts, and MADR 4.0 catalog parity across all `22` organization repositories (`9` `PUBLIC` + `9` `PRIVATE` + `4` `ARCHIVED`).

## Decision Outcome

1. **Seal Org Manifest at `v3.10.8` (`22/22` Repositories):** Update `ECOSYSTEM_ORG_MANIFEST.json` to `schemaVersion: "3.10.8"`, `verifiedDate: "2026-11-19"`, `canonicalWorkflowsCount: 21`, `dualMachineOrcaAutomationsCount: 15`, `ownerTotalStarsAudited: 415`, and exact `origin/main` `baselineSha` hashes across updated repositories.
2. **Enforce Two-Tier Public CI vs Private Zero-Burn Firewall (`ADR-0001`):** Keep `actionsEnabled: false` across all `9` active proprietary `PRIVATE` and `4` cold-archived repositories while running SHA-pinned GitHub Actions CI across all `9` `PUBLIC` repositories.
3. **Zero-Drift MADR 4.0 Parity & Privacy Hygiene:** Regenerate `docs/adr/CATALOG.md` and `ECOSYSTEM_ORG_MANIFEST.json` `adrGovernance` (`35/35` ADRs) via `scripts/architecture_catalog.py --sync-manifest` and verify zero leaks via `scripts/merge_gate.py` and `gitleaks`.

## Alternatives Considered

- **Skip Org Manifest Seal After Sibling Repo Pushes:** Rejected because `test_org_manifest.py` and `sota-org-doctor --live` require exact SHA and count alignment across the 22-repository estate.

## Verification Witness

- `uv run python scripts/architecture_catalog.py --sync-manifest` & `--check` (`35` GitHub-evidenced MADR 4.0 ADRs & manifest verified, `0` drift), `uv run python scripts/merge_gate.py`, `uv run python -m unittest discover -s tests -v`, and `gitleaks git --staged --verbose` (`0` leaks).
