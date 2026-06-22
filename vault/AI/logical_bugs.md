# Ai Note

Logical Bugs

Logical bugs occur when the model violates formal reasoning patterns.

Examples include:

Contradictions inside a single answer

Invalid syllogisms

Mistaken inference chains

False conclusions from true premises

True conclusions from false premises (still logically invalid)

Circular reasoning disguised as explanation


Logical bugs represent a failure of consistency — the model’s “reasoning stack” collapses under scrutiny.

Example Prompt:

> “If A is larger than B, and B is larger than C, can C be larger than A? Explain.”



Bug Pattern:

The model answers “Yes, depending on perspective,” which reveals confusion about transitivity.

This doesn’t just expose a single incorrect answer.
It exposes a faulty internal structure.