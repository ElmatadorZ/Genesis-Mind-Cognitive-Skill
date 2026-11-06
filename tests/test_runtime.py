"""The runtime pipeline: every entry point must import and run end to end.

Before 5D five entry points (genesis_core, genesis_core_vx, genesis_orchestrator,
main, run_genesis) could not even be imported: they expected an option-scoring
core/decision_engine.py that was not in the repository, and the parts they wired
together had drifted apart (ctx.memory.add on a list, ShadowWrapper.observe,
GenesisMind.process, IdentityCore(name, profile)). CI only byte-compiled, so
nothing noticed. These tests keep the pipeline runnable.
"""
from __future__ import annotations

import importlib
import subprocess
import sys
from pathlib import Path

import pytest

from core.decision_engine import DecisionEngine, Option

ROOT = Path(__file__).resolve().parent.parent


# ------------------------------------------------------------ decision engine

def test_needs_at_least_two_options():
    with pytest.raises(ValueError):
        DecisionEngine().evaluate([Option("Only", 0.5, 0.5, 0.5, 0.5)])


def test_values_are_bounded():
    with pytest.raises(ValueError):
        Option("Bad", 1.2, 0.1, 0.5, 0.5)


def test_risk_above_tolerance_is_penalised_unless_reversible():
    eng = DecisionEngine(risk_tolerance=0.5)
    locked = Option("Locked-in", 0.8, 0.8, 0.6, 0.0)
    undoable = Option("Undoable", 0.8, 0.8, 0.6, 1.0)
    assert eng.score(undoable) > eng.score(locked)


def test_confidence_is_never_certain_and_tracks_the_margin():
    eng = DecisionEngine()
    clear = eng.evaluate([Option("Great", 1.0, 0.0, 1.0, 1.0), Option("Awful", 0.0, 1.0, 0.0, 0.0)])
    close = eng.evaluate([Option("A", 0.6, 0.3, 0.6, 0.5), Option("B", 0.6, 0.3, 0.59, 0.5)])
    assert clear.confidence <= 0.95
    assert close.confidence < clear.confidence


def test_near_tie_still_chooses_but_does_not_recommend_acting():
    d = DecisionEngine(min_confidence=0.6).evaluate(
        [Option("Act Now", 0.8, 0.6, 0.6, 0.5), Option("Wait & Observe", 0.5, 0.2, 0.5, 0.9)])
    assert d.chosen == "Act Now"
    assert d.act is False
    assert "gather" in d.reasoning


def test_reference_case_prefers_controlled_growth():
    d = DecisionEngine(risk_tolerance=0.6).evaluate([
        Option("Aggressive Expansion", 0.9, 0.7, 0.6, 0.4),
        Option("Controlled Growth", 0.7, 0.4, 0.7, 0.7),
        Option("Hold Position", 0.5, 0.2, 0.5, 0.9),
    ])
    assert d.chosen == "Controlled Growth"
    assert d.act is True
    assert set(d.scores) == {"Aggressive Expansion", "Controlled Growth", "Hold Position"}


# ------------------------------------------------------------ end to end

def test_every_module_imports():
    skip = {"tests", "tools", ".git"}
    names = []
    for f in ROOT.rglob("*.py"):
        rel = f.relative_to(ROOT)
        if skip & set(rel.parts):
            continue
        names.append(".".join(rel.with_suffix("").parts))
    failed = []
    for n in sorted(names):
        try:
            importlib.import_module(n)
        except Exception as e:  # noqa: BLE001 - report every failure at once
            failed.append(f"{n}: {type(e).__name__}: {e}")
    assert not failed, "\n".join(failed)


def test_genesis_mind_runs():
    from genesis_core import GenesisMind
    out = GenesisMind().run("Should I expand globally now?")
    assert out["decision"] in {"Aggressive Expansion", "Controlled Growth", "Hold Position"}
    assert 0.5 <= out["confidence"] <= 0.95
    assert out["debate"]["shadow"], "the shadow voice must be present"


def test_vx_runs():
    from genesis_core_vx import GenesisMindVX
    out = GenesisMindVX().run("Should we launch now?")
    assert out["decision"] in {"Act Now", "Wait & Observe"}


def test_orchestrator_runs_all_identities():
    from genesis_orchestrator import GenesisOrchestrator
    out = GenesisOrchestrator().run("Expand to a new market?")
    assert {r["identity"] for r in out["multi_self"]} == {"Skynet", "Atlas", "Eidolon"}
    assert all(r["confidence"] <= 0.95 for r in out["multi_self"])
    assert out["final_decision"]["identity"] == "Skynet"  # aggressive bias lifts it highest
    assert out["shadow"]


@pytest.mark.parametrize("script", ["main.py", "run.py", "run_genesis.py", "agent.py"])
def test_entry_points_exit_cleanly(script):
    r = subprocess.run([sys.executable, script], cwd=ROOT, input="Should I expand?\n",
                       capture_output=True, text=True, timeout=30)
    assert r.returncode == 0, r.stderr[-500:]
