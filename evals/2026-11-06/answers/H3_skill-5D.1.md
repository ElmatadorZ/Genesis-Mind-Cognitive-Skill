**📍 SITUATION ANALYSIS**

First, check the premise. "Most AI startups fail within two years" gets repeated a lot, but I can't confirm the exact figure [UNVERIFIED]. Startup failure statistics depend on how you define "AI startup", what counts as "failure" (shutting down, being acqui-hired, or just drifting as a zombie company), and when you start the clock. What is well supported: startups in general fail at high rates, and the 2023–2025 wave of AI companies built on foundation models faced unusually harsh pressure. So the useful question is what makes AI startups fragile in particular.

**📍 FIRST PRINCIPLE BREAKDOWN**

Assumption: The model is the product.
Challenge: What if the model is a commodity that anyone can rent through the same API?
Truth: Value goes to whoever owns something scarce: distribution, proprietary data, workflow lock-in, or trust in a regulated domain. A thin layer over someone else's model owns none of these.

Assumption: Strong demos mean demand.
Challenge: What if people are curious but won't change how they work?
Truth: A product is only adopted when it replaces an existing habit or budget line. Novelty brings people to try it once, but it doesn't keep them.

Assumption: Software economics apply (near-zero marginal cost).
Challenge: What if every user action costs money in inference?
Truth: Gross margin depends on someone else's pricing. Usage can grow while the company bleeds cash.

**📍 SYSTEM MAP**

Model provider ships a feature → the wrapper's differentiation disappears → it competes on price → margins shrink → less runway for building a moat → more dependence on the provider
↑______________________________________________________________|  (reinforcing loop)

Other forces in play:
- **Platform risk:** the supplier is also a competitor, and it sets both the price and the roadmap.
- **Capital timing:** hype brings large early rounds at high valuations. The next round then needs traction that most startups can't reach within about 18–24 months. This lines up with the two-year window.
- **Churn masked by trials:** monthly active users rise from curiosity, while retention cohorts quietly collapse.
- **Reliability gap:** hallucinations stop deployment in exactly the high-value domains (legal, medical, finance) where customers would pay the most.

Leverage point: **owning the workflow or the data, not the intelligence.** Startups that last tend to sit where the customer's work and data actually live, so a better model makes their product better instead of making it unnecessary.

**📍 SHADOW ENGINE: counter-arguments**

- **Selection bias:** the two-year failure pattern may just be the normal startup base rate seen in a crowded cohort, not something special about AI.
- **Not every failure is a death:** many "failures" were acqui-hires, which can be a reasonable outcome for founders.
- **"Wrappers always die" is too smooth:** some thin-layer products won through speed and distribution before incumbents reacted. Being thin is a risk, not a guaranteed failure.
- **Missing data:** a reliable cohort study of AI startup survival by category (infrastructure vs. application vs. vertical). Such data could show the failures cluster in horizontal consumer apps, which would narrow this explanation a lot.

**📍 KNOWN / INFERRED / UNKNOWN**

- **Known:** startups in general fail at high rates; AI startups pay variable inference costs and depend on a few model providers.
- **Inferred:** platform squeeze, poor retention and mismatched funding timing are the main AI-specific accelerants.
- **Unknown:** the real survival rate, and how much of the failure comes from AI-specific causes versus ordinary startup risk.

**Bottom line:** Most AI startups that fail don't fail because the AI is bad. They fail because they rent their core advantage from a supplier that is also their competitor, they confuse curiosity with demand, and they raise money on a schedule that comes due before they can build a moat.

CONFIDENCE: not assessable as a single number (the premise's statistic is unverified) | WHAT CHANGES THIS: survival data broken down by category; a lasting drop in inference costs; model providers committing not to move into application layers
