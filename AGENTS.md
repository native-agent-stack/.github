# Native Agent Stack — Organization Control-Plane Charter

1. **Zero Secrets & Home-Path Firewall:** Never read, print, or commit secrets (`.env*`, keys, broker account IDs), personal home paths (`/Users/*`, `/home/*`, `C:\Users\*`), or live broker ports (`:4001`, `:7496`, `:8798`, `:8796`).
2. **40-Char SHA-Pinned Supply Chain:** Every external GitHub Action `uses:` in `.github/workflows/*.yml` must pin an immutable 40-char commit SHA with `step-security/harden-runner`, `permissions: {}` top-level, and `zizmor --offline` `0` findings.
3. **MADR 4.0 & Manifest Bijection:** Keep `ECOSYSTEM_ORG_MANIFEST.json` (`schemaVersion: "4.0.0"`, `nextEraActiveTier: {".github", "tier0-quant"}`) and `docs/adr/CATALOG.md` (LF endings) synced via `python3 scripts/architecture_catalog.py --sync-manifest`.
4. **Upstream-Only Register:** Keep `UPSTREAM.md` free of retired wrappers and `orca.yaml` free of `defaultTabs`.
5. **Merge Gates:**
   - `python3 scripts/architecture_catalog.py --check`
   - `python3 scripts/merge_gate.py`
   - `python3 -m unittest discover -s tests -v`
   - `gitleaks detect --no-git --source . && gitleaks git . && zizmor --offline .github/workflows/`
