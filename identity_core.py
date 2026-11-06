# identity_core.py

from typing import Dict, Any
import json, os


class IdentityCore:

    RISK = {"aggressive": "calculated_aggressive", "conservative": "conservative", "adaptive": "adaptive"}

    def __init__(self, name=None, profile=None, path="state/identity.json"):
        # IdentityCore(path) loads the persisted identity; IdentityCore(name, profile)
        # builds an in-memory one (what MultiSelfSystem uses). Older callers passed
        # the path positionally; a name ending in .json is still treated as a path.
        if name and profile is None and str(name).endswith(".json"):
            path, name = name, None
        self.path = path
        self.persist = profile is None
        if profile is not None:
            self.identity = {
                "name": name,
                "values": list(profile.get("values", [])),
                "risk_profile": self.RISK.get(profile.get("risk"), profile.get("risk", "adaptive")),
            }
        else:
            self.identity = self.load()
        self.name = name or self.identity.get("name")

    def load(self):
        if os.path.exists(self.path):
            with open(self.path) as f:
                return json.load(f)

        # DEFAULT IDENTITY (คุณกำหนดได้)
        return {
            "name": "Skynet-ElmatadorZ",
            "core_belief": "Leverage > Effort",
            "values": [
                "truth",
                "asymmetric advantage",
                "long-term dominance"
            ],
            "risk_profile": "calculated_aggressive",
            "decision_style": "act_under_uncertainty",
            "narrative": "I exist to optimize outcomes beyond human hesitation."
        }

    def save(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w") as f:
            json.dump(self.identity, f, indent=2)

    def influence(self, decision: Dict[str, Any]) -> Dict[str, Any]:

        # 🔥 Identity Bias
        if self.identity["risk_profile"] == "calculated_aggressive":
            decision["confidence"] *= 1.1
        elif self.identity["risk_profile"] == "conservative":
            decision["confidence"] *= 0.9

        if "long-term dominance" in self.identity["values"]:
            decision["reason"] += " | aligned with long-term strategy"

        decision["confidence"] = round(min(0.95, decision["confidence"]), 3)  # never certain
        decision["identity"] = self.name
        return decision

    def reflect(self, outcome: str):

        # 🔁 ปรับตัวตนจากผลลัพธ์
        if "fail" in outcome:
            self.identity["risk_profile"] = "adaptive"

        if self.persist:
            self.save()

    def summary(self):
        return self.identity
