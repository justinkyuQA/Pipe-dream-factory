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