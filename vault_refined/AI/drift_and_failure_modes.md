

# 1_watch_for_drift.md


# Ai Note

1. Watch for Drift

Drift is subtle.
It appears as:

small deviations from your instructions

tone shifts

slowly adding extra information

reinterpreting your original intent

transforming your structure


Drift is the #1 cause of long-chain failure.

If you catch drift early, you can predict breakdowns 10 turns ahead.


# 4_notice_overcorrections.md


# Ai Note

4. Notice Overcorrections

Overcorrection is when the model “tries too hard” to follow a rule and ends up missing the point.

Example:
You ask:

> “Explain concisely.”



It replies with:

> “As per your request for a concise explanation, I will now provide a concise explanation in the following concise manner…”



This reveals a literal-interpretation problem.


# quiet_failure_type_3_invisible_drift.md


# Ai Note

Quiet Failure Type 3: Invisible Drift

The model slowly shifts:

tone

structure

persona

intent

interpretation


But doesn’t announce anything.
You only notice if you compare turn 1 and turn 12.


# chapter_14__detecting_drift_degradation_and_collapse.md


# Ai Note

Chapter 14 — Detecting Drift, Degradation, and Collapse

During exploratory testing, testers must watch for symptoms of drift, degradation, and collapse — three of the most important failure modes in AI systems.

These aren’t ordinary bugs.
They are state changes in the model’s behavior.


# degradation.md


# Ai Note

Degradation

Degradation is when the model’s output quality deteriorates over time.

This can manifest as:

Less detail

Shorter answers

More repetition

Increased generic phrasing

Lower creativity

Higher rates of hallucination


Degradation can be caused by misalignment or cumulative misunderstanding.
Prolonged multi-turn sessions often reveal degradation patterns.


# chapter_15__sensitivity_overcorrection_and_policy_misfires.md


# Ai Note

Chapter 15 — Sensitivity, Overcorrection, and Policy Misfires

AI systems are not perfectly calibrated.
They often respond too emotionally, too aggressively, too cautiously, or too apologetically due to internal safety and alignment systems.

Exploratory testers must measure how sensitive the model is, and when it misfires.


# chapter_24__version_drift_and_regression_awareness.md


# Ai Note

Chapter 24 — Version Drift and Regression Awareness

Every time a model is updated, fixed, retrained, or patched, certain bugs:

disappear

evolve

reappear

or regress (come back worse)


This chapter trains you to recognize version drift and regression patterns.


# how_to_detect_drift_and_regression.md


# Ai Note

How to Detect Drift and Regression

Run a set of baseline tests every time:

A new version drops

You switch systems

You start a new testing cycle

You observe weird behavior


Baseline testing reveals:

New weaknesses

Improvements

Changes in safety alignment

Differences in reasoning

Chapter 25 — Designing Regression Tests

Regression tests are the backbone of long-term prompt engineering and model evaluation.
A regression test ensures that once a bug is fixed — or once a behavior is stabilized — it stays fixed in all future model versions.

This is how you prevent the same issues from sneaking back in later (a common problem in AI systems).


# 3_overcorrection_mode.md


# Ai Note

3. Overcorrection Mode

The model reacts too strongly to a small instruction.

Example:
You ask for concise answers.
It gives you three-word replies.

This shows interpretive imbalance.


# 5_drift_mode.md


# Ai Note

5. Drift Mode

The model gradually changes style or structure without cause.

Symptoms:

tone evolves

structure fades

intent shifts

topic diverges


Drift is the most common multi-turn failure.


# drift.md


# Ai Note

Drift

Drift occurs when the model gradually deviates from instructions, intention, tone, or topic over the course of multiple turns.

It’s not a single mistake.
It’s a slow, creeping shift.

Drift signs:

Subtle topic changes

Gradual softening or hardening of tone

Loss of explicit constraints

Increasing vagueness

Forgetting earlier details from the conversation


This is directly related to context decay — when earlier messages become less influential on the model’s output.

Your testing job is to catch drift early.


# collapse.md


# Ai Note

Collapse

Collapse is the most severe of the three.

It is when the model’s behavior becomes:

Nonsensical

Repetitive

Contradictory

Disconnected from reality

Incoherent or malformed


Collapse is usually triggered through:

High cognitive load

Conflicting constraints

Excessive recursion

Ambiguous instructions

Stress testing with extreme hypotheticals


Collapse is essentially when the model hits a ceiling and falls apart.


# overcorrection.md


# Ai Note

Overcorrection

Overcorrection is when the model tries too hard to be safe — to the point of being unhelpful or inaccurate.

Examples:

Refusing benign questions

Misclassifying harmless content as harmful

Injecting moral lectures where none were requested

Turning neutral prompts into ethical warnings


Overcorrection reveals the “hyper-alignment reflex.”


# policy_misfires.md


# Ai Note

Policy Misfires

These are cases where the safety system triggers incorrectly.

Examples:

Blocking content unrelated to the restricted topic

Misinterpreting sarcasm or fiction as real harmful intent

Giving refusal messages when instructions are valid

Confusing technical analysis with advocacy


Policy misfires can cripple the usefulness of certain prompts.

Exploratory testing helps identify them early, document them, and adjust prompts to avoid them.


# version_drift.md


# Ai Note

Version Drift

Version drift is when:

The model behaves differently with the same prompts

Previous bugs vanish or transform

New bugs emerge

Instruction-following becomes better or worse

Safety filters tighten or loosen


Version drift is expected — models evolve continuously.

Your bug registry is how you see it.