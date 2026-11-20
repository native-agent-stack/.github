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
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / "merge_gate.py")], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, msg=r.stderr or r.stdout)

    def test_v3103_shared_24x5_foundation_and_github_maintenance_workflows(self) -> None:
        m = json.loads((ROOT / "ECOSYSTEM_ORG_MANIFEST.json").read_text(encoding="utf-8"))
        self.assertEqual(m["schemaVersion"], "3.11.1")
        pub = m["repositories"]["publicUnlimitedActionsTier"]
        priv = m["repositories"]["privateExecutionAndVaultTier"]
        self.assertEqual(pub["native-agent-stack"]["baselineSha"], "1135dd7f30d3c588edecc2679f5f7e9fb6d58a53")
        self.assertEqual(pub["sota-upstream-shelf-lock"]["baselineSha"], "505b149c0acce21a2bd9661256c11c450c8660fb")
        self.assertEqual(pub["sota-compounding-lab"]["baselineSha"], "379cafae44e9cd4abfbc3302b98c66450195dcb7")
        self.assertEqual(pub["sota-multi-model-workflows"]["baselineSha"], "1cca7989d01ac3f4cbd778bc58c3ca5ea9b23134")
        self.assertEqual(pub["astrolabe"]["baselineSha"], "801efa5a5706c606a60fe0c9577702624056b26e")
        self.assertEqual(priv["sota-dynamic-trail-c"]["baselineSha"], "97796a0e88e89bdea2689e2c6f863d6e43637a8c")
        self.assertEqual(priv["sota-mover-ranker"]["baselineSha"], "1d3205f6b5e5c59c84898fe19d0925b9e51adcdf")
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
