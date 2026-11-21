# ADR-0040: Next-Era Single Active Monorepo (`tier0-quant`) Cutover & Read-Only Archival of `17` Legacy Repositories

- **Status:** Accepted
- **Date:** 2026-11-21
- **Layer:** L0 Org Control Plane (`L0`), Two-Tier Public/Private Visibility & CI Firewall (`L9`), & Next-Era Single-Monorepo Architecture
- **Evidence Grade:** E4 (`tier0-quant@4b02a733` green across `Noesis-SOTA`, `Mac M5 Max`, `Z:/tier0-quant`, and GitHub Actions CI `44930400960` / `44930401050` / `44930407137` / `44930407260`; `0` open PRs; `10/10` org CI green pre-archival; `17` legacy GitHub repositories archived read-only alongside `4` historical archived repositories (`21` total); standalone `~/.config/git/hooks` + `Z:/dot-github` + official `openbq-org/backends-for-openbb` `:6900` + direct upstream `codebase-memory-mcp 0.12.1` & `xerj v1.0.0-rc.104` MCPs verified)
- **GitHub Evidence:** https://github.com/native-agent-stack/.github, https://github.com/native-agent-stack/tier0-quant, https://github.com/nautechsystems/nautilus_trader, https://github.com/stablyai/orca, https://github.com/OpenBB-finance/backends-for-openbb, https://github.com/DeusData/codebase-memory-mcp
- **Revisit Trigger:** Achieving the first verified pre-wall (`<= 2026-10-15`) HLZ statistical falsification pass in `tier0-quant` (`hlz_trials_passed >= 1`, `N = 109`, `t*(109) = 4.2169`) or an explicit org-control-plane upgrade in `.github`.

## Context and Problem Statement

Maintaining `18` active repositories alongside `tier0-quant` and `.github` forced every change through redundant cross-repo registries, CI repair loops, duplicate virtual environments, and stale local runtime tethers (global `core.hooksPath`, scheduled Keep-Up interpreters, `:6900` OpenBB backend, stdio MCP launchers, and `27` hidden Orca project setups), even after `tier0-quant` had already consolidated `59` disjoint `L0`–`L10` upstream frameworks, `33` locked skills across `6` Orca lanes, `4` canonical MADR 4.0 ADRs (`ADR-0001`..`ADR-0004`), and Disk-`Z:` + `Mac M5 Max` parity. Continuing to leave the `17` superseded repositories unarchived invited ongoing multi-repo churn instead of focusing purely on pre-wall quant research inside `tier0-quant`.

## Decision Outcome

1. **Enforce a Strictly 2-Repository Active Organization (`tier0-quant` + `.github`):**
   - `native-agent-stack/tier0-quant` (`private`, `main@4b02a7337440c84f2b2125d6ac8af86ea48ab4ed`) is the sole active clean-room quant and research monorepo (`Noesis-SOTA:~/tier0-quant`, `Z:/tier0-quant` mirror, `Mac M5 Max ~/Documents/tier0-quant`), enforced at `<= 5,000` custom production LOC with Zero Self-Built Frameworks and Zero Paper Self-Invention.
   - `native-agent-stack/.github` (`public`, anchored at `Z:/dot-github`) serves strictly as the lightweight organization control plane (`ECOSYSTEM_ORG_MANIFEST.json` `schemaVersion: "4.0.0"`, MADR 4.0 catalog, and self-contained `scripts/merge_gate.py` verifying SHA-pinned GitHub Actions, `0` leaks, and `18` `PINS.md` shelf SHAs locally without importing sibling repos).
2. **Archive All `17` Legacy Repositories Read-Only (`archived=true`, `21` Total Archived):**
   - Archive `agy-sota-harness`, `astrolabe`, `canon`, `cc-sota-harness`, `dsh-plugin-landscape`, `dsh-sota-harness`, `meridian`, `native-agent-stack`, `sota-compounding-lab`, `sota-dynamic-trail-c`, `sota-harness-foundation`, `sota-mover-ranker`, `sota-multi-model-workflows`, `sota-private-vault`, `sota-upstream-shelf-lock`, `trading-sota`, and `tsl` read-only on GitHub with exact final `baselineSha` hashes recorded in `ECOSYSTEM_ORG_MANIFEST.json` alongside the `4` historical archived repositories (`ecosystem-records`, `legacy-agent-stack-202610`, `legacy-edge-202611`, `legacy-movers-202611`).
3. **Detach All `5` Runtime Tethers & Cold-Archive Local Legacy Trees to Disk `Z:`:**
   - Migrate global git hooks to self-contained `~/.config/git/hooks`, Windows Keep-Up scheduling to standalone `pythonw.exe` + `Z:/tier0-quant`, loopback `:6900` OpenBB workspace backend to unmodified upstream `backends-for-openbb`, Antigravity/IDE MCP configs directly to upstream `codebase-memory-mcp 0.12.1` + `xerj v1.0.0-rc.104`, and unregister the `27` legacy Orca project setups so only `tier0-quant` remains.
   - Preserve cold local backups strictly on Disk `Z:` (`Z:/archive/2026-11-21-legacy-sota-workstation-final/`) while keeping `~/Documents/upstream/` (`18` pins), `Z:/sota-data/`, Drive `D:`, and live real-money broker endpoints untouched.

## Alternatives Considered

- **Leaving `17` Legacy Repositories Unarchived Read-Write:** Rejected — unarchived repositories continue triggering CI workflows, Dependabot/registry checks, and multi-repo maintenance drift.
- **Keeping `sota-private-vault` Unarchived Separately:** Rejected per owner Next-Era directive — all final SHAs and `801` legacy ADRs are preserved verbatim in GitHub's read-only `sota-private-vault` archive (`2cfa851d`) and cold Disk-`Z:` storage.

## Verification Witness

- `python scripts/architecture_catalog.py --sync-manifest` & `--check` (`40/40` GitHub-evidenced MADR 4.0 ADRs verified, `0` drift).
- `python scripts/merge_gate.py`, `python -m unittest discover -s tests -v`, `gitleaks git`, and GitHub Actions `Org Control-Plane Gate` (`completed/success`).
- Live GitHub API org verification (`2` active: `tier0-quant`, `.github`; `21` archived), standalone hooks push verification, `:6900` `backends-for-openbb` HTTP `200`, `orca project setups` showing solely `tier0-quant`, and Disk-`Z:` cold archive verified.
