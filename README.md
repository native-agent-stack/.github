# Native Agent Stack (`github.com/native-agent-stack` — `v4.0.0` Next-Era)

**Next-Era Two-Repository Organization: Sole Clean-Room Monorepo (`tier0-quant`) + Org Control Plane (`.github`).**

Following `ADR-0040` and `ADR-0044`, all `17` superseded multi-repo repositories were sealed and archived read-only (`21` archived total alongside `4` historical archives), leaving `tier0-quant` (`seathatflowsinourveins/tier0-quant`, `public` with `main-gate` ruleset) and `.github` (`public`) as the only active repositories.

- **Control Plane Manifest:** [`ECOSYSTEM_ORG_MANIFEST.json`](ECOSYSTEM_ORG_MANIFEST.json) (`schemaVersion: "4.0.0"`)
- **Organization ADRs:** [`docs/adr/CATALOG.md`](docs/adr/CATALOG.md) (`44` MADR 4.0 ADRs)
- **Standalone Merge Gate:** [`scripts/merge_gate.py`](scripts/merge_gate.py) (zero leaks, `40`-char SHA-pinned GitHub Actions, `18` `PINS.md` shelf SHAs)
- **Pre-Wall & Execution Firewalls:** Strictly historical discovery `<= 2026-10-15`, `<= 2.00%` atomic initial stop (`ADR-0022`), and hard-refused live broker endpoints (`:4001`, `:7496`).

## Clean New Install
```bash
git clone https://github.com/seathatflowsinourveins/tier0-quant.git && cd tier0-quant && bash scripts/orca_workspace_setup.sh
```
