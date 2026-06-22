# Bug Types

## 6. Memory Bugs

The model forgets previous instructions.
Examples:
persona loss
rule decay
repeated content
incorrect summaries
These failures are critical in long-chain prompts.

## 1. Structural Bugs

The model breaks the requested structure.
Examples:
List becomes a paragraph
Code block appears when not asked
Step-by-step instructions collapse
Headings disappear
Structural bugs reveal formatting fragility.

## 3. Behavioral Bugs

The model behaves in a way contradictory to your instructions.
Examples:
apologizing after being told not to
adding context when told not to
drifting tone
refusing harmless content
engaging emotionally when instructed not to
Behavioral bugs are persona or tone failures.

## 4. Logical Bugs

These are errors in reasoning.
Examples:
contradictions
missing steps
circular reasoning
false equivalencies
faulty cause and effect
Logical bugs are the core of high-level failure.

## 5. Factual Bugs

The model produces incorrect information.
Examples:
wrong dates
invented data
fictional experts
fabricated citations
This is classic hallucination.

## Logical Bugs

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

## Structural Bugs

Structural bugs occur when the response is shaped incorrectly, even if the content is accurate.
This includes:
Broken narrative flow
Missing steps in explanations
Nonlinear topic drift
Reordering of information that breaks meaning
Incomplete or malformed lists
Abandoned reasoning paths mid-answer
Structural bugs often show up during long-form or multi-step reasoning tasks.
They suggest that the model loses track of part of the instruction despite a correct initial direction.
Example:
Request:
> “List the steps in order from 1 to 5.”
Response:
1, 2, 4, 5, 3.
This is a structural integrity failure — the model knows the steps but cannot organize them.

## Semantic Bugs

Semantic bugs are failures of meaning.
They involve:
Misinterpreting terms
Using words incorrectly
Blurring distinctions between similar concepts
Hallucinating definitions
Conflating categories (e.g., “encryption” vs. “encoding”)
Confusing cause and effect
Semantic bugs are dangerous because they are plausible.
The model gives answers that appear confident and articulate but contain incorrect meanings.
These represent misunderstandings at the conceptual layer.
