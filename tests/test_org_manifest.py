from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TestOrgControlPlane(unittest.TestCase):
    def test_manifest_invariants_and_visibility_firewall(self) -> None:
        m = json.loads((ROOT / "ECOSYSTEM_ORG_MANIFEST.json").read_text(encoding="utf-8"))
        self.assertEqual(m["organization"], "native-agent-stack")
        self.assertEqual(m["studyWallDate"], "2026-10-15")
        self.assertLessEqual(m["executionFirewall"]["maxInitialStopPctAdr0022"], 2.0)
        self.assertTrue(m["executionFirewall"]["liveCapitalHardRefused"])
        pub = m["repositories"]["publicUnlimitedActionsTier"]
        priv = m["repositories"]["privateExecutionAndVaultTier"]
        self.assertGreaterEqual(len(pub), 6)
        self.assertGreaterEqual(len(priv), 5)
        # Ensure proprietary trading execution repos stay strictly in the Private tier
        self.assertIn("sota-mover-ranker", priv)
        self.assertIn("sota-dynamic-trail-c", priv)
        self.assertIn("sota-private-vault", priv)
        self.assertNotIn("sota-mover-ranker", pub)
        self.assertNotIn("sota-dynamic-trail-c", pub)

    def test_adr_catalog_and_merge_gate_pass(self) -> None:
        r = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "merge_gate.py")], check=False, capture_output=True, text=True
        )
        self.assertEqual(r.returncode, 0, msg=r.stderr or r.stdout)

    def test_v3103_shared_24x5_foundation_and_github_maintenance_workflows(self) -> None:
        m = json.loads((ROOT / "ECOSYSTEM_ORG_MANIFEST.json").read_text(encoding="utf-8"))
        self.assertEqual(m["schemaVersion"], "3.12.0")
        pub = m["repositories"]["publicUnlimitedActionsTier"]
        priv = m["repositories"]["privateExecutionAndVaultTier"]
        self.assertEqual(pub["native-agent-stack"]["baselineSha"], "4b1e7bb00ec1d79a7eb9e117fcc3cc459228a189")
        self.assertEqual(pub["sota-upstream-shelf-lock"]["baselineSha"], "2b833e91e690a4ecf416ce37c180f0423f769d1a")
        self.assertEqual(pub["sota-compounding-lab"]["baselineSha"], "2b840f7d536491edd72377a7e0ecdca8a96a156c")
        self.assertEqual(pub["sota-multi-model-workflows"]["baselineSha"], "f6aa16cb4248ebedff9f8c997eef4e6bdde0a2bc")
        self.assertEqual(pub["sota-harness-foundation"]["baselineSha"], "059820692e33614f4bacaaf81612ccb51f51457b")
        self.assertEqual(pub["agy-sota-harness"]["baselineSha"], "e25e6320d974ce0d446d3a3400bed6db24bf4de9")
        self.assertEqual(pub["astrolabe"]["baselineSha"], "f854c9b4488c1d7f210e204a9dbe193ee0962488")
        self.assertEqual(priv["sota-dynamic-trail-c"]["baselineSha"], "7401ce4644192c75ddc2d9bf329324a47ea9cf14")
        self.assertEqual(priv["sota-mover-ranker"]["baselineSha"], "2307f8676de2d99daab0a151d531541227346446")
        self.assertEqual(priv["sota-private-vault"]["baselineSha"], "556363d8ed62e0f181f98aeb5378cc906768a124")
        frp = m["fullResolutionBackbonePolicy"]
        self.assertTrue(frp["fullResolutionVerified"])
        self.assertFalse(frp["allowSilentFallback"])
        self.assertEqual(frp["residualFallbacksCount"], 0)
        self.assertEqual(frp["requiredEnginesCount"], 9)
        self.assertGreater(frp["nautilusIterationsVerified"], 0)
        self.assertGreater(frp["hftbacktestEventsVerified"], 0)
        self.assertTrue(frp["rtx4090CudaRequired"])
        self.assertTrue(frp["emptyBacktestEngineStubAstGateEnabled"])
        tlg = m["terminalLandscapeGovernance"]
        self.assertEqual(tlg["schemaVersion"], "sota-terminal-platform-taxonomy.v1")
        self.assertEqual(tlg["canonicalOwnerRepo"], "sota-upstream-shelf-lock")
        self.assertEqual(tlg["taxonomySha256"], "2c81665b9dba2590db3649f00dae309bf5c33704d641faa19160741c54b8c61d")
        self.assertEqual(tlg["classesCount"], 4)
        self.assertEqual(tlg["namedSurfacesCount"], 14)
        self.assertEqual(tlg["immutableCorePinsPreserved"], 18)
        self.assertTrue(set(tlg["paperOnlySanctionedPorts"]).isdisjoint(set(tlg["liveProtectedRefusedPorts"])))
        self.assertEqual(tlg["dualPoolComputeGovernanceSchema"], "sota-anthropic-keybank.v1")
        self.assertTrue(tlg["publicCiOnlyApiSecretFirewall"])
        pol = m["executionFirewall"]["stage5ProvenLosslessLivePolicy"]
        self.assertEqual(pol["goalId"], "G_SOTA_DUAL_MACHINE_MERIT_TO_LOSSLESS_LIVE_24X5")
        self.assertEqual(pol["simLanesNeverGated"], 2)
        self.assertEqual(pol["paperFarmAccountsNeverGated"], 4)
        self.assertEqual(pol["alpacaPaperAccounts"], 3)
        self.assertEqual(pol["ibkrPaperAccounts"], 1)
        self.assertTrue(pol["paperAndLiveShareSame24x5Foundation"])
        self.assertEqual(pol["primarySovereignHost"], "stationary_noesis_win32")
        self.assertEqual(pol["portableFailoverHost"], "portable_mac_m5_max")
        self.assertTrue(pol["singleActiveBrokerHostOnly"])
        self.assertEqual(pol["dedicatedLiveExtGuardianPort"], 8796)
        self.assertTrue(pol["canonicalOrcaLaneLeadsReadOnlyT5"])
        self.assertTrue(pol["adr0035UnifiedShieldActive"])
        self.assertTrue(pol["failClosed8796DirectCallDefault"])
        self.assertEqual(m["canonicalWorkflowsCount"], 21)
        self.assertEqual(m["dualMachineOrcaFolderHubsCount"], 18)
        self.assertEqual(m["dualMachineOrcaAutomationsCount"], 15)
        self.assertEqual(m["canonicalOrcaLaneLeadsCount"], 10)
        self.assertEqual(len(m["sevenDomainOrcaLaneHubs"]), 7)
        self.assertTrue((ROOT / ".github" / "workflows" / "reusable-sota-lane-maintenance.yml").is_file())
        ci_txt = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
        self.assertIn("schedule:", ci_txt)


if __name__ == "__main__":
    unittest.main()
