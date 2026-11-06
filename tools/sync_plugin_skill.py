"""Copy the canonical SKILL.md into the Claude Code plugin layout.

Run after editing SKILL.md:  python tools/sync_plugin_skill.py
tests/test_plugin_package.py fails until the copy matches.
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    skill = ROOT / "SKILL.md"
    name = re.search(r'^name:\s*"?([^"\n]+)"?', skill.read_text(encoding="utf-8"), re.M).group(1).strip()
    dest = ROOT / "skills" / name / "SKILL.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(skill, dest)
    print(f"synced {skill.name} -> {dest.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
