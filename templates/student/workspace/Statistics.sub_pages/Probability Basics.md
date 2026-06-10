---
title: Probability Basics
icon: FileText
---

# Probability Basics

The grammar of uncertainty. Get the four rules below right and most of the course follows.

## Sample space and events

The **sample space** is the set of all possible outcomes; an **event** is a subset of it. Probability assigns each event a number between 0 and 1:

<!-- otion:math {"equation":"0 \\le P(A) \\le 1, \\qquad P(\\text{sample space}) = 1"} -->

For equally likely outcomes, probability is just counting:

<!-- otion:math {"equation":"P(A) = \\frac{\\text{favorable outcomes}}{\\text{total outcomes}}"} -->

## The addition rule

For the probability that A *or* B happens:

<!-- otion:math {"equation":"P(A \\cup B) = P(A) + P(B) - P(A \\cap B)"} -->

Subtract the overlap so you don't double-count it. If A and B are **mutually exclusive**, the overlap is zero.

## Conditional probability

The probability of A *given* B has already happened:

<!-- otion:math {"equation":"P(A \\mid B) = \\frac{P(A \\cap B)}{P(B)}"} -->

If `P(A | B) = P(A)`, the events are **independent** — knowing B tells you nothing about A.

## Bayes' rule

Flip a conditional probability around:

<!-- otion:math {"equation":"P(A \\mid B) = \\frac{P(B \\mid A)\\, P(A)}{P(B)}"} -->

### Worked example

A test is 99% accurate for a condition that affects 1% of people. If you test positive, what's the chance you actually have it? Bayes:

<!-- otion:math {"equation":"P(\\text{sick} \\mid +) = \\frac{0.99 \\times 0.01}{0.99 \\times 0.01 + 0.01 \\times 0.99} = 0.5"} -->

Only **50%** — the base rate matters as much as the test accuracy. This is the classic exam trap.

## Key terms

- **Mutually exclusive** — events that can't both happen.
- **Independent** — one event's outcome doesn't change the other's probability.
- **Complement** — `P(not A) = 1 - P(A)`.

## To review for the quiz

- [ ] Apply the addition rule with and without overlap
- [ ] Compute a conditional probability from a two-way breakdown
- [ ] Do one full Bayes' rule problem and explain why the base rate matters

<!-- otion:todo {"text":"Re-solve the medical-test Bayes problem until the 50% result feels obvious","id":"todo-prob-0001","created":"2026-10-05T09:00:00.000Z"} -->
