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


if __name__ == "__main__":
    unittest.main()
