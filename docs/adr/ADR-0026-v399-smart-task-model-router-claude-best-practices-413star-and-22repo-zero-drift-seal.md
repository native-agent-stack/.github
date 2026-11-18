# ADR-0026: `v3.9.9` Smart Task-to-Model Suitability Router, Claude Code Best Practices, `413`-Star Atlas & 22-Repo Zero-Drift SHA Seal

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Organization Control Plane, 22-Repo 40-Char SHA Manifest & Smart Multi-Model Governance (`L0–L13` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (`22/22` Exact 40-Char `origin/main` SHA Parity, `9/9` Public GitHub Actions, `8`-Class Smart Router, `413` Stars & `54/54` Synced Checkouts)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-multi-model-workflows, https://github.com/native-agent-stack/cc-sota-harness, https://github.com/parallel-web/parallel-search-evals, https://github.com/NVIDIA/SkillEvaluator
- **Revisit Trigger:** Ecosystem `v4.0.0` promotion or `2026-12-06` `23/5` Consolidated SIP cutover

## Context and Problem Statement

Following `ADR-0025` (`v3.9.8`), all `18` active repositories converged on `v3.9.9`: `8`-class Smart Task-to-Model Suitability Routing (`sota-cc-hub smart-route` / `--worker auto` in `sota-multi-model-workflows` `ADR-0022`), Claude Code `v2.1.327` Best-Practice Charter v2 (`cc-sota-harness` `ADR-0034`), compiled `OMC 5.8.6 dist/` stop-callbacks & `2,325`-vector `qmd` retrieval (`ADR-0028`/`ADR-0033`/`ADR-0035`), own-history abnormal `RVOL_tod` size-bias purge & Wave-2 / IBKR `:4002` SAR (`ADR-0064`/`ADR-0015`/`sota-mover-ranker`), and the `413`-star (`33`-anchor) owner research & evaluation atlas (`parallel-web/parallel-search-evals`).

## Decision Outcome

1. **Seal `ECOSYSTEM_ORG_MANIFEST.json` at `schemaVersion = "3.9.9"` (`26` Org ADRs, `413` Audited Stars, `33` Curated Anchors):**
   - Lock all `21` sibling live 40-char `origin/main` `baselineSha` digests (`total_mismatches = 0`) with `0` active peer leases across the organization.

## Alternatives Considered

- **Leave `ECOSYSTEM_ORG_MANIFEST.json` at `v3.9.8`:** Rejected — `22/22` live `origin/main` SHA parity is mandatory.

## Verification Witness

- `python scripts/architecture_catalog.py --sync-manifest` + `python scripts/merge_gate.py` + `python -m unittest discover -s tests -v` -> `PASS` (`26` ADRs, `0` drift, `0` leaks).
- `sota-org-doctor --live` -> `22/22` `MATCH` (`0` violations).
