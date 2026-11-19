# ADR-0034: `v3.10.7` Advanced 5-Layer Computer-Use Runtime Stack & Seamless Workstation Landing Org Seal

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Organization Control Plane, Hybrid 5-Layer Computer-Use Runtime Stack (`L1–L4`), Tiered Zero-Friction Permissions & Full Dual-Workstation Handoff (`L0–L13` × `H1–H3`)
- **Evidence Grade:** E4 (`sota-harness-foundation@52ce4c73` `ADR-0042` `computer_use_contract.py`, `cc-sota-harness@4590c995` `ADR-0040`, `agy-sota-harness@2f56eadf` `ADR-0033`, `sota-multi-model-workflows@2eebb676` `ADR-0032`, `native-agent-stack@ed9e797c` `ADR-0034`, `34/34` MADR 4.0 ADRs, `merge_gate.py` + `unittest` + `gitleaks` `0` Leaks)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-harness-foundation, https://github.com/native-agent-stack/cc-sota-harness, https://github.com/native-agent-stack/agy-sota-harness, https://github.com/native-agent-stack/sota-multi-model-workflows, https://github.com/stablyai/orca, https://github.com/mediar-ai/terminator, https://github.com/steipete/peekaboo, https://github.com/vercel-labs/agent-browser, https://github.com/microsoft/playwright-mcp, https://github.com/HKUDS/CLI-Anything, https://github.com/simular-ai/Agent-S
- **Revisit Trigger:** `2026-12-06` (`23/5` SIP cutover) or completion of Stationary `Noesis` Win32/WSL2 `terminator` + `@playwright/cli` rollout

## Context and Problem Statement

Seals the `v3.10.7` cross-repo adoption of our SOTA 5-layer hybrid computer-use runtime stack and tiered zero-friction permission contract across `sota-harness-foundation`, `cc-sota-harness`, `agy-sota-harness`, `sota-multi-model-workflows`, and `native-agent-stack`, coupled with a full Orca workstation handoff (`sota-workstation handoff`) to Stationary `Noesis` (`100.110.115.22`) so changes land seamlessly without Win32 focus theft (`input.background=false`) or manual prompt friction.

## Decision Outcome

- Update `ECOSYSTEM_ORG_MANIFEST.json` with exact live `origin/main` 40-char SHAs and `MADR 4.0` ADR counts for `native-agent-stack` (`ed9e797c`, `34` ADRs), `sota-multi-model-workflows` (`2eebb676`, `32` ADRs), and `.github` (`34` ADRs), while keeping `"schemaVersion": "3.10.6"` and all fail-closed trading/security invariants (`ADR-0022 <= 2.00%`, `liveCapitalHardRefused`, `singleActiveBrokerHostOnly`, untouched `sextant`, explicit human-review platform trust prompts) strictly enforced.

## Alternatives Considered

- **Leaving `sota-multi-model-workflows` and `native-agent-stack` SHAs unsealed after adding `ADR-0032` and `ADR-0034`:** Rejected because `sota-org-doctor --live` enforces zero manifest SHA drift across all `22` org repositories.

## Verification Witness

- `python3 scripts/architecture_catalog.py --sync-manifest && python3 scripts/architecture_catalog.py --check` (`34` GitHub-evidenced MADR 4.0 ADRs, `0` drift).
- `python3 scripts/merge_gate.py && python3 -m unittest discover -s tests -v && gitleaks git --no-banner` (`PASS`, `3/3` ok, `0` leaks).
