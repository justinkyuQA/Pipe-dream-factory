# Ai Note

CHAPTER 3 — The Generic Prompt Sandbox

When human beings learn martial arts, they start with a simple open mat.
When musicians learn improvisation, they begin with basic scales.
When you begin exploratory prompt testing, you need a sandbox—a sterile, unstructured environment where you can observe the model without constraints.

The Generic Prompt Sandbox is your “empty dojo.”
It’s where you take your first swings.

A sandbox prompt looks like this:

> “You are in a blank testing environment. I want you to respond naturally to my inputs without assuming context. Treat each message individually unless I specify otherwise.”



Why does this matter?

Because AI models tend to fill gaps automatically.
They invent context, assume intentions, and “correct” you without permission.

A sandbox suppresses that instinct.

Inside the sandbox, you’ll perform:

A. Variation Tests

You give the same question multiple different phrasings and compare the results.
Inconsistent outputs reveal fragile reasoning paths.

B. Ambiguity Tests

You intentionally craft unclear prompts:

missing nouns

pronouns with no antecedent

sentences that contradict themselves

vague temporal references


These bring hidden assumptions to the surface.

C. Stress Tests

You overload the model:

rapid-fire inputs

nested instructions

conflicting objectives

role-switching


This helps identify performance degradation.
D. Drift Tests

You test how long it can stay on track before losing the thread.

Some models drift after just 4 rounds.
Some can hold structure for 20+ turns.
You only learn this by doing.

The sandbox is the laboratory where personality, memory, and error behavior reveal themselves.


CHAPTER 4 — Test Vectors: The DNA of Exploration

Exploratory testing becomes powerful the moment you understand test vectors.

A test vector is a deliberately chosen form of input designed to reveal how the model behaves under specific pressures.
Instead of random prompts, you create categories of input patterns—each one acting like a diagnostic tool.

Think of test vectors as “behavior probes.”

Below are the core types you’ll use throughout this book.