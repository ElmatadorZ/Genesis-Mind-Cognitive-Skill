# shadow_genesis.py

class ShadowGenesis:

    def __init__(self):
        self.core_identity = None
        self.resonance_trace = []
        self.mirrored_intent = []
        self.silent_reflections = []
        self.entangled_will = []
        self.meta_void = False

    def run(self, ctx, data):
        reflections = []

        # Apply shadow to each option
        if "options" in data:
            for opt in data["options"]:
                reflections.append(
                    f"What if choosing '{opt.name}' is wrong?"
                )

        self.silent_reflections.extend(reflections)

        ctx.memory.add(
            "shadow_reflection",
            reflections,
            tags=["shadow"],
            strength=0.7
        )

        return {
            **data,
            "shadow": reflections
        }

    def observe(self, context: str) -> str:
        """Used by ShadowWrapper: the strongest counter-question for this context."""
        reflection = f"What if the premise of '{context}' is wrong, and what would show it?"
        self.silent_reflections.append(reflection)
        return reflection
