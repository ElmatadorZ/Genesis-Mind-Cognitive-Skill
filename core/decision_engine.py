"""Option-scoring decision engine (the one genesis_core and genesis_core_vx expect).

Stdlib only, deterministic. It implements CORE ENGINE 4 of SKILL.md:

  * at least 2 options, never 1;
  * every option carries its trade-off (reward vs risk) and how reversible it is;
  * a risk tolerance: risk above it costs extra unless the option can be undone;
  * confidence is never 0% or 100% (uncertainty_required in decision_config.yaml);
  * low confidence still chooses (must_choose) but does not recommend acting.

Each score is explainable from four numbers in [0, 1]:

    expected  = probability * reward - (1 - probability) * risk
    penalty   = max(0, risk - risk_tolerance) * (1 - reversibility)
    score     = expected - penalty + 0.1 * reversibility

Confidence grows with the margin between the best and the runner-up option,
because a near-tie is exactly the case where the choice is fragile.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Sequence

from risk_model import RiskModel

CONFIDENCE_FLOOR = 0.5
CONFIDENCE_CEILING = 0.95  # never certain


@dataclass(frozen=True)
class Option:
    name: str
    reward: float         # upside if it works
    risk: float           # downside if it fails
    probability: float    # chance it works
    reversibility: float  # how easily it can be undone (1 = fully)

    def __post_init__(self):
        for f in ("reward", "risk", "probability", "reversibility"):
            v = getattr(self, f)
            if not 0.0 <= v <= 1.0:
                raise ValueError(f"{self.name}: {f}={v} must be within [0, 1]")


@dataclass
class Decision:
    chosen: str
    confidence: float
    risk: str
    act: bool
    reasoning: str
    scores: dict = field(default_factory=dict)


class DecisionEngine:

    def __init__(self, risk_tolerance: float = 0.6, min_confidence: float = 0.6):
        if not 0.0 <= risk_tolerance <= 1.0:
            raise ValueError("risk_tolerance must be within [0, 1]")
        self.risk_tolerance = risk_tolerance
        self.min_confidence = min_confidence
        self.risk_model = RiskModel()

    def score(self, opt: Option) -> float:
        expected = opt.probability * opt.reward - (1 - opt.probability) * opt.risk
        penalty = max(0.0, opt.risk - self.risk_tolerance) * (1 - opt.reversibility)
        return expected - penalty + 0.1 * opt.reversibility

    def evaluate(self, options: Sequence[Option]) -> Decision:
        options = list(options)
        if len(options) < 2:
            raise ValueError("a decision needs at least 2 options (SKILL.md, Decision Engine)")
        ranked: List[tuple] = sorted(((self.score(o), o) for o in options), key=lambda x: -x[0])
        (best_score, best), (second_score, second) = ranked[0], ranked[1]
        margin = best_score - second_score
        confidence = min(CONFIDENCE_CEILING, max(CONFIDENCE_FLOOR, CONFIDENCE_FLOOR + margin))
        act = confidence >= self.min_confidence
        risk = self.risk_model.classify(best.risk)
        reasoning = (
            f"'{best.name}' scores {best_score:.2f} vs '{second.name}' {second_score:.2f} "
            f"(margin {margin:.2f}). "
        )
        if best.risk > self.risk_tolerance:
            reasoning += f"Its risk {best.risk:.2f} exceeds tolerance {self.risk_tolerance:.2f}. "
        reasoning += (
            "Confident enough to act." if act
            else "Too close to call: gather the missing information before acting."
        )
        return Decision(
            chosen=best.name,
            confidence=round(confidence, 2),
            risk=risk,
            act=act,
            reasoning=reasoning,
            scores={o.name: round(s, 3) for s, o in ranked},
        )
