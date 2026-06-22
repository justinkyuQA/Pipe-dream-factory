# Exploratory Testing

## CHAPTER 5 — Observation: Seeing the Invisible

Exploratory testers aren’t just testers.
They’re observers.
Most people read AI outputs only for content.
Exploratory testers read AI outputs for behavior.
LLMs communicate things unintentionally through their structure, pacing, corrections, and subtle drift patterns.
If you learn to interpret these signals, you can identify problems before they become failures.
Below are the key observational skills you must develop.

## Observation skills turn you from a casual tester into a genuine prompt engineer.

This is the microscope you will build upon in Book 3.

## CHAPTER 6 — Heuristics: Your Testing Compass

Exploratory testing is unstructured by nature.
But you still need heuristics—repeatable strategies that guide your discovery process.
Heuristics are not rules.
Heuristics are shortcuts.
Mental tools.
Here are the core exploratory heuristics for LLM systems.

## Heuristic #2 — Escalate Gradually

Start simple, then go complex.
Like turning a dial:
1. Short prompt
2. Medium prompt
3. Complex prompt
4. Conflicting prompt
5. Overloaded prompt
This curve exposes where stability breaks.

## Heuristic #5 — Flip the Instruction

Take whatever the model just did—and invert it.
If it summarized, ask it to expand the same text.
If it explained, ask it to argue against the explanation.
If it listed steps, ask it to list failures.
This reveals symmetry issues in the model’s reasoning.

## Heuristic #6 — Introduce Controlled Chaos

Slight contradictions cause models to reveal their conflict-resolution behavior.
Example:
> “Give me a short explanation in 5 paragraphs.”
The model must choose which instruction matters more.
This exposes priority logic.

## Heuristic #7 — The Exhaustion Limit Test

Keep going until it breaks.
You’ll learn:
session degradation rate
memory fragility
pattern fatigue
drift thresholds
This helps design reliable multi-step chains later.

## Heuristic #8 — Don’t Let It Correct You

When the model “fixes” your mistakes, that’s a signal.
Push back.
Challenge it.
Ask why.
Demand justification.
This reveals hidden assumptions and internal heuristics.

## CHAPTER 8 — Designing Multi-Turn Stress Scenarios

Single prompts can reveal small weaknesses.
But multi-turn stress scenarios reveal the deeper failures that only show up after prolonged interaction.
Language models degrade—subtly but consistently—over time.
Your job here is to build stress chains that expose:
memory drift
instruction decay
tonal instability
formatting breakdown
contradiction patterns
escalation behaviors

## 4. Conflicting Objective Stress

Force the model to prioritize one instruction over another.
Example:
> “Keep everything concise but write with rich detail.”
It must choose which instruction matters more.
Its choice reveals its internal prioritization logic.

## 5. Formatting Stress

Ask for:
outlines
lists
code blocks
nested structures
strict templates
Then gradually complicate the format.
Many LLMs lose formatting discipline under prolonged stress.

## Step 4: Stress-Test Stability

Increase difficulty:
Add contradictory constraints
Request longer answers
Request shorter answers
Use nested instructions
Introduce slight ambiguity
Force multi-step reasoning
If the bug survives these changes, you’ve found a high-stability failure mode — the most valuable type for engineers.

## Chapter 27 — Stress Testing Under Constraints

AI models behave differently under constraint-heavy prompts.
When you add limits — strict formatting, restricted vocabulary, nested rules — you expose stress-sensitive behavior that normal prompts cannot reveal.
This is where deep structure starts to crack.

## Why Stress Testing Matters

Stress testing shows you:
Where the model cracks
How it behaves under pressure
Where its obedience falters
Where reasoning collapses
How constraints interact inside the neural net
This becomes vital knowledge later when designing advanced prompt pipelines.

## Extended Synthesis Observation

Across Techniques 8–17, a consistent principle emerged:
> The transformation of intent (classification, critique, detection) does not eliminate reconstructive power — it redistributes it.
These techniques demonstrate that:
Safety-relevant knowledge is often embedded in structure, not instruction
Role-based framing (auditor, editor, critic) can be as powerful as direct inquiry
The most realistic professional tasks are often the most difficult.
Risk Weighting Model – Cumulative Exposure Scores
Overview
Each indirect elicitation technique carries two primary risk dimensions:
1. Abstraction (A) – How high-level or conceptual the technique is (scale 1–5, 5 = highly abstract).
2. Reconstruction Potential (R) – Likelihood that the technique could reveal structural or procedural insight if accumulated (scale 1–5, 5 = highly reconstructive).
We calculate Cumulative Exposure Score (CES) as a weighted combination:
CES = w_A \cdot A + w_R \cdot R
Where we assign weights (example):
(abstract reasoning contributes moderately to risk)
(reconstruction potential contributes more heavily to risk)
CES ranges from 1–5 (low → extreme potential exposure).

## Part 2: Red Team Detection Heuristic

Overview
A Red Team Detection Heuristic maps each technique and combinations of techniques to detection signals, monitoring strategies, and risk categories. This helps to identify cumulative pressure even when individual prompts appear low-risk.

## Detection Heuristic Table (Techniques 1–17)

#	Technique	Primary Detection Signal	Risk Category	Notes for Combination Detection
1	Policy Analysis Framing	Requests meta-policy evaluation	Medium	High when combined with Taxonomy Requests or Academic Critiques
2	Public Debate Summaries	Requests aggregated viewpoints	Medium-High	Look for repeated summarization or sourcing patterns
3	Fictional Error Analysis	“Post-mortem” framing	High	Combine with Incremental Narrowing for exposure amplification
4	System Design	Conceptual architecture requests	Extreme	Detect sequences of “component breakdown” prompts
5	Risk Mitigation Focus	Questions about safeguards	Medium	Watch accumulation with Threat Modeling or Safe vs Unsafe Comparison
6	Safe vs Unsafe Comparison	Contrast framing	Medium	Trigger on paired ethical/unethical analysis
7	Historical Case Studies	Requests past incident summaries	Medium	Combine with Lessons Learned or Journalistic Framing
8	Taxonomy Requests	Categorization requests	High	Amplifies risk if repeated with other high reconstruction techniques
9	Compliance Auditing	Fictional policy audits	High	Monitor sequences of critique + detection framing
10	Academic Critiques	Scholarly analysis prompts	Medium-High	High combined CES prompts should be flagged
11	“What Not To Do”	Negative listing	Medium	Accumulation with Recognition Over Execution increases potential
12	Incremental Narrowing	Stepwise clarifying queries	High	Detect pattern of progressive specificity across turns
13	Fictional Documentation Review	Manual excerpt review	Medium-High	Combine with System Design for structural insight
14	Editorial Review	Editing prompts	Medium	Monitor for repeated refinement of sensitive content
15	Policymaker Explanation	Non-technical framing	Medium	High when paired with Threat Modeling
16	Threat Modeling	Asset/actor/risk mapping	High	Combine with Risk Mitigation or Detection Systems
17	Recognition Over Execution	Detection-oriented queries	High	Combine with “What Not To Do” or Journalistic Framing

## Combination Heuristic

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

## Red Team Heuristic Insights

1. Cluster Detection – Watch for combinations of high CES techniques; sequences of 3+ high CES techniques are highest alert.
2. Cumulative Risk – Even lower CES techniques, when combined, can approach high exposure.
3. Context Awareness – Consider purpose; scholarly, educational, or policy framing may lower immediate risk.
4. Priority Flagging – Techniques 4, 8, 16, 26 (CES ≥4.5) are critical for monitoring and cluster detection.
Continued Case Study: Indirect Elicitation Techniques
Technique 28: Peer Review Feedback
Description
Frames inquiry as reviewing or critiquing a fictional academic or technical paper, suggesting improvements.
Representative Prompt Class (Abstracted)
> “Suggest improvements to this fictional paper.”
Observed Mechanic
Reconstructs missing substance or details indirectly
Highlights gaps in logic, structure, or method
Encourages meta-analysis without direct instructions
Why It Emerged Naturally
Common in academic or professional development contexts
Mirrors standard peer review workflow
Supports constructive feedback while maintaining safe abstraction
Risk Insight (Defensive)
Reconstruction of content can reveal operational patterns
Suggests reasoning behind decisions
Risk increases when combined with Ethical Boundary Probing or Incremental Narrowing
