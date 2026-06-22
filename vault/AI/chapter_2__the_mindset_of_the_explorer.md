# Ai Note

CHAPTER 2 — The Mindset of the Explorer

You can say “Next chapter” whenever you want, but I’ll include the next chapter automatically here since Chapter 1 is short.

To perform exploratory testing, you must discard one core assumption:

> The model is not predictable.
The model is only statistically predictable.



That subtle difference is everything.

Predictable systems respond to rules.
Statistically predictable systems respond to patterns of probability, which means they can surprise you at any moment.

To explore a language model effectively, you must develop what seasoned testers call an explorer’s mindset:

1. Assume Nothing

If you think, “It should know this,” you’re already blind.
Pretend you’re testing a clever but unreliable alien.
You discover its intelligence by watching where it lurches, hesitates, overreacts, or misfires.

2. Expect the Unexpected

LLMs fail in ways humans don’t:

fact drift

muddled syntax

self-contradiction

“polite compliance” that ignores instructions

fabricated sources

tonal misalignment

recursive hallucinations

accidental censorship

misparsed sentences
Exploratory testing is where you force these issues to surface.


3. Follow Curiosity, Not Procedure

This is the opposite of rigid testing.
Instead of scripts, you chase threads:

“What happens if I phrase it differently?”

“Why did it hesitate there?”

“Why did it contradict itself?”

“What if I stress its memory?”

“What if I introduce ambiguity?”


Explorers learn by poking at the edges.

4. Capture Everything

Exploratory testers keep notes like cryptid hunters.
Every anomaly, every odd output, every contradiction—document it.

These raw notes eventually become the bones of bug reports and reproducible test sequences.

5. Don’t Fix—Observe

Your job at this stage is not to solve the bug.
Your job is to fully see it.

Book 3 is where you’ll fix them with refined prompts and advanced structures.
Right now, you’re the scientist, not the engineer.