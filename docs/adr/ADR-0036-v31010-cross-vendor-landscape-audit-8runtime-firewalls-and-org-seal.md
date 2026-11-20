# ADR-0036: `v3.10.10` Cross-Vendor Full-Landscape Audit, 8-Runtime Firewalls, 3-OS Privacy Merge Gate & 22-Repo Org Seal

- **Status:** Accepted
- **Date:** 2026-11-19
- **Layer:** Organization Control Plane, 3-OS Privacy Merge Gate (`L9`), 8-Runtime Upstream-Native Firewalls (`L4`/`L9`), Tier-3 Full-Manifest SkillEvaluator (`L8`), & `22`-Repo 40-Char SHA Manifest (`L0–L13` × `H1–H3`)
- **Evidence Grade:** E4 (`cc-sota-harness@85f54cd1` `ADR-0043` `43/43` ADRs, `sota-harness-foundation@8b2ce535` `ADR-0044` `44/44` ADRs, `agy-sota-harness@df8e6b7d` `ADR-0035` `35/35` ADRs, `dsh-sota-harness@ab0e5ff8` `ADR-0016` `16/16` ADRs, `native-agent-stack@bfad87a9` `ADR-0039` `39/39` ADRs, `36/36` Org MADR 4.0 ADRs, OpenAI Codex `gpt-6.2-astra` Cross-Vendor Red-Team Closed `0` P0/P1, `sota-doctor` `18/18` Win32 & WSL2, `evaluate_skills.py --check-mounts` `60/60` across `8/8` mounts, `merge_gate.py` + `unittest` + `gitleaks` `0` Leaks)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/cc-sota-harness, https://github.com/native-agent-stack/sota-harness-foundation, https://github.com/native-agent-stack/agy-sota-harness, https://github.com/native-agent-stack/dsh-sota-harness, https://github.com/NVIDIA/SkillEvaluator, https://github.com/anomalyco/opencode, https://github.com/google-gemini/gemini-cli
- **Revisit Trigger:** Addition of a 9th active runtime target, next `native-agent-stack` umbrella milestone beyond `v3.10.10`, or `2026-12-06` `23/5` Consolidated SIP cutover.

## Context and Problem Statement

Following the four-track cross-vendor full-landscape audit and independent OpenAI Codex `gpt-6.2-astra` adversarial red-team review across Win32, `* Noesis-Carbon` WSL2, and Portable `Apple M5 Max`, five organization repositories landed coordinated security, verification, and upstream-parity upgrades (`cc-sota-harness` `ADR-0043`, `sota-harness-foundation` `ADR-0044`, `agy-sota-harness` `ADR-0035`, `dsh-sota-harness` `ADR-0016`, `native-agent-stack` `ADR-0039`). Meanwhile `dot-github` (`native-agent-stack/.github`) also hardened `scripts/merge_gate.py` to detect macOS, Windows, and Linux concrete home paths uniformly alongside digit-required broker account regexes, and `ECOSYSTEM_ORG_MANIFEST.json` needed promotion from `schemaVersion: "3.10.8"` to `"3.10.10"` locking all exact `origin/main` 40-char SHAs and `36/36` MADR 4.0 ADRs.

## Decision Outcome

1. **Seal `ECOSYSTEM_ORG_MANIFEST.json` at `schemaVersion: "3.10.10"` (`22/22` Repositories):** Update exact `origin/main` 40-char `baselineSha` hashes for `native-agent-stack@bfad87a924a0ff976e9d6604ec9b8d12b4aa5437`, `cc-sota-harness@85f54cd1b0b9a0bc6686559dd1b693e4a9376c92`, `sota-harness-foundation@8b2ce5352018d377e32b3e234d7106a843d68285`, `agy-sota-harness@df8e6b7dd92c508947cd228243b260a482a80fe8`, and `dsh-sota-harness@ab0e5ff84f3ef6cd79d817bd611653179e8292b2` while preserving strict Two-Tier Public/Private/Archived boundaries (`9/9/4`, `actionsEnabled: false` across all `9` `PRIVATE` and `4` `ARCHIVED` repos).
2. **Enforce 3-OS Privacy Merge Gate & Zero-False-Positive Regexes (`scripts/merge_gate.py`):** Block macOS, Windows, and Linux concrete home paths across all tracked files, enforce 40-char SHA-pinned GitHub Actions, and require at least one digit in broker paper-account ID regexes (`PA`/`DU`).
3. **Sync MADR 4.0 Catalog & Manifest (`36/36` ADRs):** Regenerate `docs/adr/CATALOG.md` and `ECOSYSTEM_ORG_MANIFEST.json` `adrGovernance` via `scripts/architecture_catalog.py --sync-manifest` and verify zero drift via `scripts/merge_gate.py`, `unittest`, and `gitleaks`.

## Alternatives Considered

- **Deferring Org Manifest Seal Until Peer Wave-A Repos Land:** Rejected because leaving the 5 newly landed harness & umbrella repositories unsealed in `ECOSYSTEM_ORG_MANIFEST.json` would immediately cause `sota-org-doctor --live` baseline SHA drift.

## Verification Witness

- `uv run python scripts/architecture_catalog.py --sync-manifest` & `--check` (`36` GitHub-evidenced MADR 4.0 ADRs & manifest verified, `0` drift).
- `uv run python scripts/merge_gate.py`, `uv run python -m unittest discover -s tests -v`, `redteam_audit.py` (`0` P0/P1/P2), and `gitleaks protect --staged --no-banner` (`0` leaks).
