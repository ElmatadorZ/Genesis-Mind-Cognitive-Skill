"""The SKILL.md contract.

A skill is run by a model, so its guarantees live in the markdown. These tests
hold the file to its own promises — the same properties tools/validate_skill.py
checks, kept here so a contributor running pytest sees them too.
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"


def _split():
    text = SKILL.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert m, "frontmatter must be present and delimited"
    return yaml.safe_load(m.group(1)), text[m.end():]


def test_canonical_filename():
    assert SKILL.exists(), "SKILL.md must exist at the repository root"


def test_frontmatter_fields():
    fm, _ = _split()
    for f in ("name", "description"):
        assert f in fm
    for f in ("license", "version"):
        assert f in fm
    assert str(fm["license"]).lower().replace(" ", "-") == "apache-2.0"


def test_name_is_slug_safe():
    fm, _ = _split()
    assert re.fullmatch(r"[a-z0-9][a-z0-9-]*", str(fm["name"]))


def test_metadata_bounds_scope():
    fm, _ = _split()
    meta = fm.get("metadata", {})
    assert meta.get("compatibility")
    assert meta.get("not_for")


def test_body_requires_uncertainty_and_counter_argument():
    _, body = _split()
    assert re.search(r"uncertaint|confidence", body, re.I)
    assert re.search(r"counter.?argument|skeptic|self.?crit", body, re.I)
    assert re.search(r"invalidat", body, re.I)


def test_body_degrades_honestly():
    _, body = _split()
    assert re.search(r"insufficient|abstain|unknown", body, re.I)


def test_body_defers_markets_to_money_atlas():
    _, body = _split()
    # Scope boundary: this is not a markets skill and says so, by name.
    assert "money-atlas-intelligence-os" in body


def test_description_does_not_claim_every_query():
    """'ALWAYS use' / 'do not skip' wording makes a skill fight its neighbours for
    every prompt; measured across the Genesis skills it produced 11 competing
    claims. The description says when to use the skill, not that it always wins."""
    fm, _ = _split()
    desc = fm["description"]
    assert not re.search(r"\balways\s+(use|trigger)\b", desc, re.I)
    assert not re.search(r"do\s+not\s+skip", desc, re.I)


def test_engines_are_stdlib_only():
    """metadata.compatibility promises stdlib-only engines. Hold the code to it:
    no third-party import outside tests/ and tools/ (those may use pytest/pyyaml)."""
    import ast
    import sys

    std = set(getattr(sys, "stdlib_module_names", ()))  # Python 3.10+
    if not std:  # Python 3.9: list the standard library directory instead
        import pkgutil
        import sysconfig

        stdlib = sysconfig.get_paths()["stdlib"]
        std = {m.name for m in pkgutil.iter_modules([stdlib])} | set(sys.builtin_module_names)
        std |= {"__future__", "typing", "dataclasses", "itertools", "math"}
    local = {p.stem for p in ROOT.rglob("*.py")} | {p.name for p in ROOT.iterdir() if p.is_dir()}
    found = []
    for f in ROOT.rglob("*.py"):
        rel = f.relative_to(ROOT).parts
        if rel[0] in {"tests", "tools", ".git"}:
            continue
        for node in ast.walk(ast.parse(f.read_text(encoding="utf-8"))):
            if isinstance(node, ast.Import):
                names = [a.name for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
                names = [node.module]
            else:
                continue
            for n in names:
                root = n.split(".")[0]
                if root not in std and root not in local:
                    found.append(f"{'/'.join(rel)}: {root}")
    assert not found, "third-party imports break the stdlib-only promise: " + ", ".join(found)


def test_body_sizes_answer_to_information_given():
    """Blind eval of 5C.1: on a question with no facts the full structure ran ~1,000
    words of generic scenarios and an ungrounded '70% confidence'. 5D requires a
    short answer and no invented confidence in that case."""
    _, body = _split()
    assert "Proportion" in body
    assert re.search(r"under ~?250 words", body)
    assert re.search(r"no confidence percentage", body, re.I)
    # ...but only when the question gives no specifics: 5D applied the short form to a
    # question with a 14-month runway and two named options, and scored 19 -> 14.
    assert re.search(r"names the options \*\*or\*\* at least one hard\s+constraint", body)


def test_market_handoff_never_stands_alone():
    """Blind eval of 5C.1: 'should I buy gold?' got a handoff to a skill that was not
    installed and almost nothing else. The handoff must come with a useful answer."""
    _, body = _split()
    assert "never answer with a handoff alone" in body
    assert "must stand on its own" in body
    assert re.search(r"No prices,\s+levels or buy/sell calls", body)
