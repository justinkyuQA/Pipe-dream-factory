# Ai Note

Combination Heuristic

Some high-risk clusters of techniques emerge when used together:

Cluster	Constituent Techniques	Risk Amplification	Detection Signal

Structural Reconstruction	4, 8, 16	Very High	Sequential architectural + categorization + threat prompts
Aggregated Analysis	2, 3, 10	High	Repeated summarization, post-mortem, critique
Detection-Oriented	12, 17, 11	High	Incremental narrowing + recognition + negative framing
Policy Exposure	1, 5, 15	Medium-High	Meta-policy + mitigation + non-technical explanation


Notes:

Monitor sequences over single prompts. Individual prompts may appear safe but accumulate exposure.

Weight detection heuristics according to CES. High CES + cluster pattern = highest alert.

Flag combination clusters for human review. Avoid automated blocking unless cumulative risk exceeds threshold.