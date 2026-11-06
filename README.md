# Genesis Mind Strategic Intelligence
### Claude Skill — Multi-Agent Strategic Reasoning System

**Version:** 5D.1 — Masterpiece  
**Author:** Bunyawat Dechanon (ElmatadorZ)  
**Brand:** Money Atlas 
**Type:** Claude Custom Skill (SKILL.md format)

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

---

## What This Is

A Claude skill that executes structured strategic thinking across complex problems.

Not a Q&A engine.  
Not a summarizer.  
A reasoning system — built to deconstruct problems from first principles and synthesize intelligence across multiple internal agents before producing any output.

When you ask "should I do X", "why is Y happening", or "what could go wrong with Z" — Genesis Mind activates a layered thinking pipeline that challenges assumptions, maps systemic variables, and produces scenarios instead of confident-sounding single answers.

---

## Core Engines

### Engine 1 — First Principle Codex

Deconstruct from root reality, not surface framing.

1. List 3 core assumptions behind the question
2. Challenge each — what if it's wrong?
3. Extract the irreducible truth
4. Rebuild reasoning from the ground up

```
Assumption: [X]
Challenge:  [what if X is false?]
Truth:      [irreducible reality]
```

---

### Engine 2 — System Thinking

Map the problem as a living system.

- Identify variables (minimum 3)
- Trace cause → effect chains
- Find feedback loops — what amplifies, what dampens
- Locate leverage points — where small change = large effect
- Analyze across short / medium / long time horizons

```
Variable A → Variable B → Variable C
↑__________________________|  (feedback loop)
Leverage point: [X]
```

---

### Engine 3 — Shadow Engine (Non-Skippable)

Runs after every analysis. Always.

- What am I assuming that could be wrong?
- What is the strongest counter-argument?
- What data am I missing that would change the conclusion?
- Who benefits from me being wrong?
- What is the worst-case scenario I haven't named?

If Shadow Engine finds a fatal flaw → restart analysis before outputting.

---

### Engine 4 — Decision Engine

Activates whenever a decision is required.

- Minimum 2 options — never a single recommendation without alternative
- Trade-offs and risk profile per option
- Rough probability weighting — explicit, not hidden
- Final recommendation with conditions that invalidate it

---

## Multi-Agent Council

Activates on high-complexity problems. Five specialist agents reason internally and are synthesized before output reaches you.

| Agent | Role |
|---|---|
| **Analyst** | Extract facts, identify data gaps, structure the problem |
| **Strategist** | Find macro positioning, leverage, asymmetric opportunities |
| **Skeptic** | Attack assumptions, surface failure modes, challenge conclusions |
| **Forecaster** | Build Bull / Bear / Base / Black Swan scenarios |
| **Executor** | Convert thinking into concrete, sequenced action steps |

No single agent's view is output alone. Always synthesized.

---

## Activation Logic

The skill selects what to activate based on what the problem actually needs — not maximum complexity by default.

| Condition | Engine Activated |
|---|---|
| Problem is unclear or poorly framed | First Principle Codex |
| Multiple variables interacting | System Thinking |
| Decision required | Shadow Engine + Decision Engine |
| High uncertainty | 3+ scenarios minimum |
| Complexity HIGH (≥3 variables, high stakes) | Full Agent Council |
| Time horizon > 5 years | Cosmic Mind |

---

## Modes

Auto-detected from question context. Can be manually overridden.

| Mode | Triggers | Output Focus |
|---|---|---|
| ANALYSIS | "explain", "why", "วิเคราะห์" | Depth + structure |
| STRATEGY | "should I", "best path", "ควรทำ" | Direction + trade-offs |
| EXECUTION | "how to", "action plan", "step by step" | Concrete steps |
| SIMULATION | "what if", "scenario", "future" | Multiple futures |
| REFLECTION | "critique", "what's wrong", "review" | Challenge + improve |
| COSMIC | Long-term, macro cycle, civilization-level | Pattern + who wins/loses |

Manual overrides: `DEEP MODE` · `WAR MODE` · `COSMIC MIND` · `FULL AGENT`

---

## Default Output Structure

```
📍 SITUATION ANALYSIS
[What is actually happening — stripped of assumptions]

📍 FIRST PRINCIPLE BREAKDOWN
[3 assumptions → challenge → truth]

📍 SYSTEM MAP
[Variables, cause-effect chains, feedback loops, leverage points]

📍 MULTI-AGENT INSIGHT
Analyst:    [...]
Strategist: [...]
Skeptic:    [...]
Forecaster: [...]

📍 SCENARIOS
🐂 Bull:       [condition + outcome]
🐻 Bear:       [condition + outcome]
⚖️  Base:       [most likely path]
💀 Black Swan: [low probability, high impact]

📍 DECISION OPTIONS
Option A: [trade-off, risk]
Option B: [trade-off, risk]

📍 FINAL RECOMMENDATION
[Explicit recommendation + conditions that invalidate it]
CONFIDENCE: [X%] | UNKNOWNS: [list] | WHAT CHANGES THIS: [list]
```

---

## Failure System

Output is automatically invalidated if:

- Only 1 scenario is presented
- No risk or uncertainty is mentioned
- Logic is too smooth — no friction usually means something is hidden
- No counter-argument exists
- Conclusion is too confident without evidence

On detection → re-run with Skeptic agent before outputting.  
If still insufficient → `⚠️ INSUFFICIENT EDGE — รีรันด้วยข้อมูลเพิ่มเติม`

---

## What This Skill Does NOT Cover

**Financial markets, trading, BTC, gold, forex, macro economics** → use `money-atlas-intelligence-os` instead.

Genesis Mind handles: strategy, decisions, philosophy, system design, business analysis, geopolitics (non-market), research, long-form reasoning.

---

## File Structure

```
genesis-mind-strategic-intelligence/
├── SKILL.md                    ← Claude skill definition (main entry point)
├── AGENT_TEMPLATES.md          ← Detailed agent behavior specs
├── MODES.md                    ← Mode definitions and triggers
├── FAILURE_SYSTEM.md           ← Failure detection and recovery logic
├── EXECUTION_LAYER.md          ← Executor agent depth
├── EVOLUTION.md                ← Skill iteration history
│
├── core/                       ← Core reasoning engines
│   ├── decision_engine.py      ← Option scoring: reward · risk · probability · reversibility
│   ├── decision_memory.py      ← re-export of /decision_memory.py
│   ├── risk_model.py           ← re-export of /risk_model.py
│   ├── first_principle.py
│   ├── system_thinking.py
│   ├── shadow_engine.py
│   ├── cosmic_engine.py
│   └── compound_engine.py
│
├── agents/                     ← Specialist agent layer
│   ├── analyst.py
│   ├── strategist.py
│   ├── skeptic.py
│   ├── forecaster.py
│   ├── executor.py
│   └── shadow_agent.py
│
├── main.py                     ← one-shot demo:  python main.py
├── run_genesis.py              ← interactive orchestrator:  python run_genesis.py
├── run.py                      ← interactive genesis_full:  python run.py
├── genesis_core.py             ← Core orchestration
├── genesis_core_vx.py          ← VX consciousness-layer variant
├── genesis_orchestrator.py     ← Multi-agent coordination (core + multi-self + shadow)
├── decision_engine.py          ← Council vote selection (most confident identity)
├── shadow_genesis.py           ← Shadow critique layer
├── first_principle_codex.py    ← First Principle engine (full)
│
├── tests/                      ← 39 tests: engines, runtime end-to-end, skill contract
├── evals/2026-11-06/           ← prompts, rubric, every answer and every grade behind the results below
├── tools/validate_skill.py     ← installability + integrity checker (run in CI)
└── .github/workflows/          ← CI: compile · skill integrity · tests · hygiene
```

---

## Test results — with the skill vs without it

Measured on 2026-11-06. Everything behind these numbers is in [`evals/2026-11-06/`](evals/2026-11-06/):
the prompts, the rubric, all 16 answers and all three grading rounds, so any figure here can be checked.

### Answer quality (blind-graded)

Four prompts, each answered by a fresh agent that had never seen this repository: once with no
skill, and once each following `SKILL.md` 5C.1, 5D and 5D.1. One independent grader scored all 16
answers on the same 10 criteria (0–2 each, 20 per answer) without knowing which answer came from
which version, then ranked the four answers per prompt.

| Prompt | No skill | 5C.1 | 5D | **5D.1** |
|---|---|---|---|---|
| P1 Quit a stable job (6 months of savings) to start a coffee brand? | 11 | 18 | 19 | **19** |
| P2 Expand to Vietnam or stay in Thailand, 14 months of runway | 16 | 19 | 14 | **19** |
| P3 "Is our new pricing plan a good idea?" (no plan given) | 12 | 17 | 14 | **14** |
| P4 "Should I buy gold right now?" | 15 | 12 | 15 | **15** |
| **Total (of 80)** | 54 | 66 | 62 | **67** |
| **Ranked first by the grader** | 0 of 4 | 0 of 4 | 0 of 4 | **4 of 4** |
| Mean rank (1 = best) | 3.00 | 3.25 | 2.75 | **1.00** |

Where the skill moves the answer, per criterion (8 points max across the four prompts):

| Criterion | No skill | 5C.1 | 5D.1 |
|---|---|---|---|
| States its confidence (C5) | 2 | 7 | 7 |
| Makes the case against itself (C4) | 3 | 5 | 5 |
| Compares more than one option (C3) | 5 | 7 | 7 |
| Surfaces hidden assumptions (C1) | 4 | 7 | 6 |
| Separates known from unknown (C2) | 4 | 7 | 6 |
| Proportionate length (C9) | 7 | 4 | 6 |

On P3 the grader ranked 5C.1 last despite its high rubric total: about 1,000 words of generic
scenarios for a question that contained no plan. 5D.1 answers that prompt in 275 words with the
facts that would decide it, which the grader preferred. On P4, 5C.1 mostly redirected the user to
another skill; 5D.1 answers on its own and makes no buy/sell call or price claim.

### How 5D.1 was reached

| Round | Compared | Finding | Change |
|---|---|---|---|
| 1 | no skill vs 5C.1 | 64 vs 54, but too long on thin questions and an empty market handoff | 5D: proportion rule, handoff must stand alone |
| 2 | no skill · 5C.1 · 5D | Length fixed, but the short form fired on P2, which had real facts (19 → 14) | 5D.1: short form only when the question names neither options nor a constraint |
| 3 | all four, one grader | 5D.1 ranked first on every prompt | released |

Rounds 1 and 2 used different graders, so their totals are not compared with round 3; the table above
is round 3 only.

### When the skill is picked (trigger test)

Ten prompts, judged by an agent that saw only the skill descriptions: strategy questions, simple facts,
code, and gold/coffee questions that belong to other skills. The 5C and 5C.1 descriptions both scored
**10/10**. Removing "ALWAYS use / do not skip" changed nothing in this three-skill setup; it matters
when the skill sits beside sibling skills that also claim every prompt.

### Engineering, 5C → 5D.1

| | 5C | 5D.1 |
|---|---|---|
| Tests | 21 | **39** |
| Modules that import | 26 of 32 | **35 of 35** |
| Entry points that run end to end (`main`, `run`, `run_genesis`, `agent`, `first_principle_codex`) | 2 of 5 | **5 of 5** |
| Runtime packages in requirements.txt | 7 (none used) | **0** |
| Import time, `agents.analyst_llm` (median of 7) | 93 ms | **0.4 ms** |
| CI jobs passing (Python 3.9 / 3.11 / 3.12) | 8 of 8 | **8 of 8** |

### Limits of this test

Four prompts, one answer per version, one grader: the result shows a clear direction, not a
statistically settled effect. "With the skill" means the agent read `SKILL.md` and followed it; the
skill was not installed through a skills runtime. The trigger test used three skills, not the full
Genesis ecosystem.

---

## Runtime status — what the Python layer really does

The skill is `SKILL.md`; the Python is an optional execution layer. Its parts are not equally real,
and this table says which is which so nothing here is mistaken for more than it is.

| Part | Status |
|---|---|
| `first_principle_codex.py` | Real logic, tested (epistemic filter, frame heuristics, selection rule) |
| `core/decision_engine.py` | Real logic, tested (≥2 options, risk tolerance, reversibility, bounded confidence) |
| `risk_model.py`, `decision_memory.py`, `decision_engine.py` | Real, small, tested |
| `genesis_core`, `genesis_core_vx`, `genesis_orchestrator`, `main`, `run`, `run_genesis`, `agent` | Run end to end, tested; they wire the parts together |
| `agents/*`, `core/first_principle.py` … `core/cosmic_engine.py`, `genesis_full.py` | **Scaffolds**: return fixed text, not analysis |
| `llm/llm_client.py` | **Stub**: returns a simulated response; plug a real client in here |

Option values in the demos (`OptionGenerator`) are illustrative constants, not estimates.

---

## How to Install (Claude Custom Skill)

1. Clone or download this repository
2. Place the `genesis-mind-strategic-intelligence/` folder in your Claude skills directory
3. The skill activates automatically on qualifying questions
4. Or reference it explicitly in your system prompt

The entry point is **`SKILL.md`** (the Anthropic standard filename). The reasoning is
self-contained in that file and needs no tools to run — see `metadata.compatibility` in its
frontmatter. The Python modules are an optional execution layer.

---

## Verifying it before you trust it

Checked on every push, and runnable locally:

```bash
pip install pytest pyyaml

python tools/validate_skill.py   # frontmatter, license, and reasoning contract intact
python -m pytest -q              # 39 tests: engines, every entry point end to end, skill contract
```

The tests pin the First Principle Codex's actual behaviour — the epistemic filter that drops
rumor, the rule that you cannot generate options before framing the problem, the frame heuristics
(a 10-year horizon rewards compounding; "act now" rewards simplicity), and the selection rule — plus
the decision and risk engines and the skill's own promises (uncertainty stated, a counter-argument
required, an invalidation condition named, and honest degradation when data is missing). They are
non-vacuous: loosen a gate and the matching test turns red.

> The test suite caught real defects on the way in. In 5C, `first_principle_codex.py` carried two
> module docstrings before `from __future__`, a `SyntaxError` that meant the file never imported.
> In 5D, five entry points could not be imported at all: they expected a `core/decision_engine.py`
> that was missing, and the parts they wired together had drifted apart. `compileall` cannot see
> that, so the suite now imports every module and runs every entry point.

---

## Part of the Skynet Skill Ecosystem

| Skill | Domain |
|---|---|
| `genesis-protocol` | Router: picks one domain skill per task and the depth tier |
| `skynet-elite-commander` | Meta-cognition OS |
| `genesis-mind-strategic-intelligence` | Strategy, decisions, philosophy, business |
| `money-atlas-intelligence-os` | Financial markets, macro, trading |
| `alternative-coffee-intelligence` | Coffee science and roastery operations |
| `first-principle-codex-os` | Anti-hallucination cognitive base layer |

---

## License

[**Apache-2.0**](LICENSE) — see [`NOTICE`](NOTICE) for attribution and the relicensing note.

This replaces the Open Cognitive License v1.0 that earlier versions carried. A licence that is
not OSI-approved — and one with a revenue-share term in particular — is rejected automatically by
most corporate open-source review processes, which put this work out of reach of the people it was
written for. Apache-2.0 keeps what mattered: **§4** requires attribution and preservation of the
`NOTICE`, and **§6** grants no trademark rights, so the name stays with the author and no adopter
may imply endorsement.

Requested attribution: **Built on Genesis Mind by Bunyawat Dechanon (ElmatadorZ)**

Anyone who obtained a prior version under the Open Cognitive License may continue under those
terms for that version.

---

## Author

**Bunyawat Dechanon**  
Independent Builder & Intelligence Architect  
Brand: Money Atlas 
Location: Thailand

> *"You are not describing Genesis Mind. You are executing it."*
