"""The Claude Code plugin package.

`claude plugin marketplace add ElmatadorZ/Genesis-Mind-Cognitive-Skill` reads
.claude-plugin/marketplace.json; `claude plugin install genesis-mind@elmatadorz`
then loads skills/genesis-mind-strategic-intelligence/SKILL.md. The root SKILL.md
stays the canonical file (claude.ai upload, validate_skill, the contract tests),
so the plugin copy must never drift from it.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
PLUGIN_SKILL = ROOT / "skills" / "genesis-mind-strategic-intelligence" / "SKILL.md"
PLUGIN = ROOT / ".claude-plugin" / "plugin.json"
MARKET = ROOT / ".claude-plugin" / "marketplace.json"


def _load(p):
    return json.loads(p.read_text(encoding="utf-8"))


def test_plugin_skill_is_identical_to_root_skill():
    assert PLUGIN_SKILL.exists(), "plugin skill copy missing; run: python tools/sync_plugin_skill.py"
    assert PLUGIN_SKILL.read_bytes() == SKILL.read_bytes(), (
        "skills/.../SKILL.md differs from SKILL.md; run: python tools/sync_plugin_skill.py")


def test_skill_folder_matches_skill_name():
    m = re.search(r'^name:\s*"?([^"\n]+)"?', SKILL.read_text(encoding="utf-8"), re.M)
    assert m and PLUGIN_SKILL.parent.name == m.group(1).strip()


def test_marketplace_points_at_the_plugin():
    market, plugin = _load(MARKET), _load(PLUGIN)
    assert market["name"] and market["owner"]["name"]
    entries = {p["name"]: p for p in market["plugins"]}
    assert plugin["name"] in entries, "marketplace entry name must match plugin.json name"
    src = entries[plugin["name"]]["source"]
    assert ".." not in src and (ROOT / src / ".claude-plugin" / "plugin.json").exists()


def test_version_is_set_in_one_place_only():
    # plugin.json wins silently when both set a version, so only plugin.json sets it.
    market, plugin = _load(MARKET), _load(PLUGIN)
    assert re.fullmatch(r"\d+\.\d+\.\d+", plugin["version"])
    assert all("version" not in p for p in market["plugins"])


def test_plugin_license_matches_repository():
    assert _load(PLUGIN)["license"] == "Apache-2.0"
    assert "Apache License" in (ROOT / "LICENSE").read_text(encoding="utf-8")
