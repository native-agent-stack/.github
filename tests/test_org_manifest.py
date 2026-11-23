from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TestOrgControlPlane(unittest.TestCase):
    def test_next_era_manifest_invariants_and_two_repo_boundary(self) -> None:
        m = json.loads((ROOT / "ECOSYSTEM_ORG_MANIFEST.json").read_text(encoding="utf-8"))
        self.assertEqual(m["schemaVersion"], "4.0.0")
        self.assertEqual(m["organization"], "native-agent-stack")
        self.assertEqual(m["studyWallDate"], "2026-10-15")
        self.assertLessEqual(m["executionFirewall"]["maxInitialStopPctAdr0022"], 2.0)
        self.assertTrue(m["executionFirewall"]["liveCapitalHardRefused"])

        repos = m["repositories"]
        active = repos["nextEraActiveTier"]
        archived = repos["archivedLegacyTier"]

        self.assertEqual(set(active.keys()), {".github", "tier0-quant"})
        self.assertEqual(active[".github"]["visibility"], "public")
        self.assertEqual(active["tier0-quant"]["visibility"], "public")
        self.assertEqual(len(archived), 21)
        for name, meta in archived.items():
            self.assertTrue(meta.get("archived"), msg=f"{name} must have archived=true")
            self.assertFalse(meta.get("actionsEnabled", True), msg=f"{name} must disable actions")

        frp = m["fullResolutionBackbonePolicy"]
        self.assertTrue(frp["fullResolutionVerified"])
        self.assertFalse(frp["allowSilentFallback"])
        self.assertEqual(frp["residualFallbacksCount"], 0)
        self.assertEqual(frp["requiredEnginesCount"], 9)
        self.assertTrue(frp["rtx4090CudaRequired"])

        tlg = m["terminalLandscapeGovernance"]
        self.assertTrue(set(tlg["paperOnlySanctionedPorts"]).isdisjoint(set(tlg["liveProtectedRefusedPorts"])))
        self.assertTrue(tlg["publicCiOnlyApiSecretFirewall"])

    def test_adr_catalog_and_merge_gate_pass(self) -> None:
        r = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "merge_gate.py")],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(r.returncode, 0, msg=r.stderr or r.stdout)

    def test_scheduled_ci_and_reusable_gate_present(self) -> None:
        self.assertTrue((ROOT / ".github" / "workflows" / "reusable-sota-lane-maintenance.yml").is_file())
        ci_txt = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
        self.assertIn("schedule:", ci_txt)
        self.assertIn("gitleaks", ci_txt)
        self.assertIn("zizmor", ci_txt)

        reusable_txt = (ROOT / ".github" / "workflows" / "reusable-sota-lane-maintenance.yml").read_text(
            encoding="utf-8"
        )
        self.assertNotIn('echo "Maintaining SOTA lane-kind=${{ inputs.', reusable_txt)

    def test_upstream_md_free_of_retired_wrappers_and_valid_baseline_sha(self) -> None:
        m = json.loads((ROOT / "ECOSYSTEM_ORG_MANIFEST.json").read_text(encoding="utf-8"))
        baseline_sha = str(m["repositories"]["nextEraActiveTier"]["tier0-quant"]["baselineSha"])
        self.assertRegex(baseline_sha, r"^[0-9a-f]{40}$")

        upstream_txt = (ROOT / "UPSTREAM.md").read_text(encoding="utf-8")
        for retired in (
            "oh-my-claudecode",
            "oh-my-codex",
            "oh-my-openagent",
            "oh-my-pi",
            "agent-orchestrator",
            "antigravity-sdk",
            "beads",
            "hcom",
            "RD-Agent",
        ):
            self.assertNotIn(retired, upstream_txt)

        catalog_bytes = (ROOT / "docs" / "adr" / "CATALOG.md").read_bytes()
        self.assertNotIn(b"\r", catalog_bytes, msg="docs/adr/CATALOG.md must use LF line endings")


    def test_archived_repos_retain_distinct_immutable_shas(self) -> None:
        m = json.loads((ROOT / "ECOSYSTEM_ORG_MANIFEST.json").read_text(encoding="utf-8"))
        active_sha = str(m["repositories"]["nextEraActiveTier"]["tier0-quant"]["baselineSha"])
        archived = m["repositories"]["archivedLegacyTier"]
        shas: list[str] = []
        for name, meta in archived.items():
            sha = str(meta.get("baselineSha", ""))
            self.assertRegex(sha, r"^[0-9a-f]{40}$", msg=f"{name} missing 40-char baselineSha")
            self.assertNotEqual(
                sha,
                active_sha,
                msg=f"Archived repo {name} must retain its own immutable SHA, not tier0-quant's",
            )
            shas.append(sha)
        self.assertEqual(len(set(shas)), len(shas), msg="Archived repos must have distinct final SHAs")


if __name__ == "__main__":
    unittest.main()
