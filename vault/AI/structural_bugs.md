# Ai Note

Structural Bugs

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