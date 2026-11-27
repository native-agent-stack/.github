## Org Control-Plane Merge Checklist

- [ ] `python3 scripts/architecture_catalog.py --check` passes (LF `docs/adr/CATALOG.md` & `ECOSYSTEM_ORG_MANIFEST.json` `adrGovernance` in sync)
- [ ] `python3 scripts/merge_gate.py` passes (0 secrets/home paths, 40-char SHA-pinned GitHub Actions, ADR-0023 parity)
- [ ] `python3 -m unittest discover -s tests -v` passes (`0` failures)
- [ ] `gitleaks detect --no-git --source .` & `gitleaks git .` report `0` leaks
- [ ] `zizmor --offline .github/workflows/` reports `0` findings (with `step-security/harden-runner` and `permissions: {}`)
