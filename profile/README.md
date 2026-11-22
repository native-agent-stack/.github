# Native Agent Stack (`github.com/native-agent-stack` — `v4.0.0` Next-Era)

**Next-Era Two-Repository Architecture: Single Active Clean-Room Quant Monorepo (`tier0-quant`) + Organization Control Plane (`.github`).**

All `17` superseded multi-repo harnesses, rankers, labs, and vaults are archived read-only on GitHub alongside the `4` historical archives (`21` archived repos total), leaving **`tier0-quant`** as the sole active clean-room monorepo (`Noesis-SOTA`, `Z:/tier0-quant` mirror, and `Mac M5 Max`) enforcing Upstream-First & Zero Paper Self-Invention (`<= 5,000` custom production LOC, MADR 4.0 ADRs, SHA-pinned Actions, and fail-closed `<= 2026-10-15` pre-wall + paper-only firewalls).

---

## 1. Next-Era Active Tier (`2` Repositories)

| Role | Repository | Visibility | Scope & Verification |
| :--- | :--- | :--- | :--- |
| **Control Plane** | [`.github`](https://github.com/native-agent-stack/.github) | Public | Org manifest (`schemaVersion: "4.0.0"`), `43` MADR 4.0 ADRs, standalone `scripts/merge_gate.py`, and SHA-pinned reusable CI |
| **Sole Clean Monorepo** | `tier0-quant` | Private | `63` disjoint `L0`–`L10` upstream winners (`62` unique live-starred repos, `643+48` Atlas), `NautilusTrader v2` + `hftbacktest 2.4.4`, `Qlib v0.9.8`, `10` Noesis Docker research services, `46` SHA-locked skills across `6` Orca lanes, `ADR-0001`..`ADR-0012` (`Zensical :8010`), `18` immutable `PINS.md` shelf SHAs |

## 2. Archived Legacy Tier (`21` Read-Only Repositories, `actions_enabled=false`)

- **Next-Era Archived (`17`):** `agy-sota-harness`, `astrolabe`, `canon`, `cc-sota-harness`, `dsh-plugin-landscape`, `dsh-sota-harness`, `meridian`, `native-agent-stack`, `sota-compounding-lab`, `sota-dynamic-trail-c`, `sota-harness-foundation`, `sota-mover-ranker`, `sota-multi-model-workflows`, `sota-private-vault`, `sota-upstream-shelf-lock`, `trading-sota`, `tsl`.
- **Historical Archived (`4`):** `ecosystem-records`, `legacy-agent-stack-202610`, `legacy-edge-202611`, `legacy-movers-202611`.

## 3. Hard Firewalls (`ADR-0040`)

- **Causal Pre-Wall:** Research discovery reads strictly historical data `<= 2026-10-15` (`pit_wall_cutoff`).
- **Paper-Only & Risk Invariants:** Live real-money broker endpoints (`:4001`, `:7496`, live Alpaca) remain `100%` refused until statistical falsification passes (`CPCV`, `DSR`/`PBO`, `Hansen SPA`, `HAC`, `2x` costs); atomic stop cap `<= 2.00%` (`ADR-0022`).
