# Native Agent Stack (`github.com/native-agent-stack` — `v4.0.0` Next-Era)

**Next-Era Two-Repository Organization: Sole Clean-Room Monorepo (`tier0-quant`) + Org Control Plane (`.github`).**

Following `ADR-0040`, `ADR-0044`, and `ADR-0045`, all `17` superseded multi-repo repositories were sealed and archived read-only (`21` archived total alongside `4` historical archives), preserving `.github` (`public`) and `tier0-quant` in `nextEraActiveTier` while registering the live `workspacePracticeEcosystem`: public [`seathatflowsinourveins/agy-sota-convergence`](https://github.com/seathatflowsinourveins/agy-sota-convergence) (`v3.2.0` + zero-wrapper native AGY Plugin Pack & full-landscape harness guide), public [`seathatflowsinourveins/noesis`](https://github.com/seathatflowsinourveins/noesis) (active quant successor), and archived-private `tier0-quant` & `sota-research-convergence`.

- **Control Plane Manifest:** [`ECOSYSTEM_ORG_MANIFEST.json`](ECOSYSTEM_ORG_MANIFEST.json) (`schemaVersion: "4.0.0"`, `workspacePracticeEcosystem` registered)
- **Organization ADRs:** [`docs/adr/CATALOG.md`](docs/adr/CATALOG.md) (`45` MADR 4.0 ADRs)
- **Reusable GitHub SOTA Workflows:** [`reusable-agy-sota-practice.yml`](.github/workflows/reusable-agy-sota-practice.yml), [`reusable-sota-gate.yml`](.github/workflows/reusable-sota-gate.yml), [`reusable-sota-lane-maintenance.yml`](.github/workflows/reusable-sota-lane-maintenance.yml) (40-char SHA-pinned, `step-security/harden-runner v2.23.0`, `gitleaks v8.30.1`, `zizmor v1.33.1`)
- **Standalone Merge Gate:** [`scripts/merge_gate.py`](scripts/merge_gate.py) (zero leaks, `40`-char SHA-pinned GitHub Actions, `18` `PINS.md` shelf SHAs)
- **Pre-Wall & Execution Firewalls:** Strictly historical discovery `<= 2026-10-15`, `<= 2.00%` atomic initial stop (`ADR-0022`), and hard-refused live broker endpoints (`:4001`, `:7496`).

## Clean New Install
```bash
git clone https://github.com/seathatflowsinourveins/tier0-quant.git && cd tier0-quant && bash scripts/orca_workspace_setup.sh
```
