# ADR-0020: `v3.9.4` `Noesis` 4K Primary `TradingView.exe` Display, Auto-Keep-Up & 22-Repo Zero-Drift SHA Seal

- **Status:** Accepted
- **Date:** 2026-11-18
- **Layer:** Organization Control Plane, 22-Repo 40-Char SHA Manifest, Primary Workstation Display Routing & 3-Surface Parity (`L0–L13` × `P0–P5` × `T0–T8`)
- **Evidence Grade:** E4 (`22/22` `origin/main` 40-Char SHA Parity, `92/92` `sota-mover-ranker` & `52/52` `sota-dynamic-trail-c` `pytest`, `merge_gate.py` & `gitleaks` `0` Leaks)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/native-agent-stack, https://github.com/native-agent-stack/sota-mover-ranker, https://github.com/native-agent-stack/sota-dynamic-trail-c
- **Revisit Trigger:** 2026-12-07

## Context and Problem Statement

With Dual Native TradingView Desktop Alpaca coexistence verified under `--dual-desktop-coexist`, stationary `Noesis` (`100.110.115.22`, `3864x2100` 4K main display) serves as the owner's primary `TradingView.exe` workstation display most of the time. Organization-wide tracking and convergence needed `sota-mover-ranker @ fd572c09fee58366b61ab720e3be59bf32daad7b` (`ADR-0020`), `sota-dynamic-trail-c @ 56121965ef8f8db8f3150294dc4df658ac2ac386` (`ADR-0017`), and `native-agent-stack @ ab1ce3bbd4f8256fb878f2922f6134b3bce8f4f4` (`ADR-0020`) locked at `schemaVersion = "3.9.4"`.

## Decision Outcome

1. **Lock `ECOSYSTEM_ORG_MANIFEST.json` at `schemaVersion = "3.9.4"` (`20` Org ADRs):**
   - Bind `native-agent-stack @ ab1ce3bbd4f8256fb878f2922f6134b3bce8f4f4`, `sota-mover-ranker @ fd572c09fee58366b61ab720e3be59bf32daad7b`, and `sota-dynamic-trail-c @ 56121965ef8f8db8f3150294dc4df658ac2ac386` with `0` drift across `Mac M5 Max`, `Noesis` Win32, and `* Noesis-Carbon` (`54/54` checkouts).

## Alternatives Considered

1. **Leave `ECOSYSTEM_ORG_MANIFEST.json` pinned to pre-`ADR-0020` `sota-mover-ranker` / `sota-dynamic-trail-c` baseline SHAs:** Rejected — `22/22` 40-char SHA parity must remain exact.

## Verification Witness

- `python scripts/architecture_catalog.py --sync-manifest && python scripts/architecture_catalog.py --check` -> `PASS` (`20` ADRs).
- `python -m unittest discover -s tests && python scripts/merge_gate.py && gitleaks detect --source . --no-banner` -> `PASS` (`0` leaks).
