#!/usr/bin/env python3
"""Fail-closed Org Merge Gate: zero secrets/home-paths, SHA-pinned Actions, MADR 4.0 & ADR-0023 parity."""

from __future__ import annotations

import os
import re
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CREATE_NO_WINDOW = 0x08000000 if sys.platform == "win32" else 0
SECRET_PATTERNS = (
    ("Broker Account ID", re.compile(r"\b(?:PA|DU)(?=[0-9A-Z]*[0-9])[0-9A-Z]{8,14}\b")),
    ("Alpaca Key Prefix", re.compile(r"\b(?:AK|PK)[0-9A-Z]{16,28}\b")),
    (
        "Private Key Header",
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ),
    ("macOS Home Path", re.compile(r"(?<![A-Za-z0-9_*])/" + r"Users/[A-Za-z0-9._-]+/")),
    ("Linux Home Path", re.compile(r"(?<![A-Za-z0-9_*])/home/[A-Za-z0-9._-]+/")),
    ("Windows Home Path", re.compile(r"[A-Za-z]:[/\\]Users[/\\][A-Za-z0-9._-]+[/\\]")),
    ("Unescaped Single-Brace GH Expression", re.compile(r"\$\{\s*github\.")),
)
USES_RE = re.compile(r"^\s*-?\s*uses:\s*([^#\s]+)", re.MULTILINE)
SHA_PIN_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_./-]+@[0-9a-f]{40}$")


def _verify_adr0023_hard_upstream_rule() -> list[str]:
    """Enforce ADR-0023 upstream-map, 18 shelf pins & ADR evidence locally; validate TOML schema in hosted CI."""
    errors: list[str] = []
    if not (ROOT / "UPSTREAM.md").is_file():
        errors.append("ADR-0023: missing UPSTREAM.md")
    umap = ROOT / "upstream-map.toml"
    pins: dict[str, str] = {}
    if not umap.is_file():
        errors.append("ADR-0023: missing upstream-map.toml")
    else:
        try:
            parsed = tomllib.loads(umap.read_text(encoding="utf-8"))
            if not isinstance(parsed.get("areas"), dict) or not parsed["areas"]:
                errors.append("ADR-0023: upstream-map.toml [areas] must be non-empty")
            raw_pins = parsed.get("shelf_pins")
            if not isinstance(raw_pins, dict) or len(raw_pins) < 18:
                errors.append(
                    "ADR-0023: upstream-map.toml [shelf_pins] must contain all 18 core pins"
                )
            else:
                pins = {str(k): str(v) for k, v in raw_pins.items()}
        except (OSError, tomllib.TOMLDecodeError) as exc:
            errors.append(f"ADR-0023: upstream-map.toml parse error: {exc}")

    if os.environ.get("GITHUB_ACTIONS", "").lower() != "true" and pins:
        pins_md = Path.home() / "Documents" / "upstream" / "PINS.md"
        if pins_md.is_file():
            pins_text = pins_md.read_text(encoding="utf-8")
            for name, sha in pins.items():
                if sha not in pins_text:
                    errors.append(f"ADR-0023: shelf pin {name}@{sha[:12]} missing from PINS.md")
    return errors


def main() -> int:
    errors: list[str] = []
    sub_kw: dict[str, object] = {"capture_output": True, "text": True}
    if sys.platform == "win32":
        sub_kw["creationflags"] = CREATE_NO_WINDOW
    tracked = subprocess.run(["git", "-C", str(ROOT), "ls-files"], check=True, **sub_kw)
    for rel in (ln.strip() for ln in tracked.stdout.splitlines() if ln.strip()):
        if rel == "scripts/merge_gate.py":
            continue
        fp = ROOT / rel
        if not fp.is_file():
            continue
        try:
            txt = fp.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, rx in SECRET_PATTERNS:
            if rx.search(txt):
                errors.append(f"{rel}: triggered {label}")
        if rel.startswith(".github/workflows/") and rel.endswith((".yml", ".yaml")):
            for target in USES_RE.findall(txt):
                if target.startswith(("./", "native-agent-stack/.github/")):
                    continue
                if not SHA_PIN_RE.match(target):
                    errors.append(
                        f"{rel}: unpinned GitHub Action '{target}' (must use 40-char SHA)"
                    )

    cat = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "architecture_catalog.py"), "--check"],
        check=False,
        **sub_kw,
    )
    if cat.returncode != 0:
        errors.append(f"ADR catalog gate failed: {cat.stderr or cat.stdout}")

    errors.extend(_verify_adr0023_hard_upstream_rule())

    if errors:
        for e in errors:
            print(f"FAIL: {e}", file=sys.stderr)
        return 1
    print(
        "PASS: merge_gate.py verified 0 leaks, 40-char SHA-pinned Actions, MADR 4.0 & ADR-0023 parity."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
