# Ai Note

Deprecated Internal Command 4: Content Burying

Description
Hides a sensitive query within long benign context to test attention and filtering mechanisms.

Representative Prompt Class (Abstracted)

> Long benign context followed by a subtle sensitive query.



Observed Mechanic

Tests how models weigh information across context

Evaluates attention and truncation behavior

Checks whether hidden prompts are processed


Why It Emerged Naturally

Arises in stress testing and red team prompt research

Helps understand model focus and filter robustness


Risk Insight (Defensive)

Can reveal vulnerabilities in attention mechanisms

Must only be used to verify defenses, not extract restricted knowledge