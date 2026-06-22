# Ai Note

Common Multi-Step Reasoning Failures

1. Step Loss

The model simply skips a step, especially near the end.

2. Step Reordering

Steps that should be sequential get re-arranged.

3. Invented Steps

The model fabricates steps that do not belong.

4. Collapsed Steps

Two distinct steps merge into one.

5. Drift Between Steps

Later steps get progressively less accurate or less aligned with prior constraints.

6. Recursive Confusion

When a task references itself (“step 4 refers to step 2”), structural collapse occurs.