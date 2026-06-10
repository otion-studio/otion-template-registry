---
title: Integration Techniques
icon: FileText
---

# Integration Techniques

The four big tools for the midterm. Knowing *which* technique a problem wants is half the battle — that's the skill the exam tests.

## 1. Integration by parts

Comes straight from the product rule. The formula:

<!-- otion:math {"equation":"\\int u \\, dv = uv - \\int v \\, du"} -->

Choosing `u` and `dv`: use **LIATE** — Logarithmic, Inverse trig, Algebraic, Trigonometric, Exponential. Whatever comes first in that list, make it `u`.

### Worked example

Evaluate the integral of `x` times `e^x`. Let `u = x` (algebraic) and `dv = e^x dx`. Then `du = dx` and `v = e^x`:

<!-- otion:math {"equation":"\\int x e^{x} \\, dx = x e^{x} - \\int e^{x} \\, dx = x e^{x} - e^{x} + C"} -->

## 2. Trigonometric substitution

Use it when you see one of these forms under a root:

- `a^2 - x^2` → substitute `x = a sin θ`
- `a^2 + x^2` → substitute `x = a tan θ`
- `x^2 - a^2` → substitute `x = a sec θ`

The point is to turn the root into a single trig function via a Pythagorean identity, e.g.

<!-- otion:math {"equation":"\\sqrt{a^{2} - x^{2}} = a\\cos\\theta \\quad \\text{when } x = a\\sin\\theta"} -->

## 3. Partial fractions

For rational functions where the **degree of the numerator is less than the denominator**. Factor the denominator, then split into a sum of simpler fractions:

<!-- otion:math {"equation":"\\frac{1}{(x-1)(x+2)} = \\frac{A}{x-1} + \\frac{B}{x+2}"} -->

Solve for `A` and `B` by clearing denominators and plugging in convenient `x` values. (Here `A = 1/3`, `B = -1/3`.) If the numerator degree is too high, do polynomial long division first.

## 4. Improper integrals

When a limit of integration is infinite (or the integrand blows up), rewrite as a limit:

<!-- otion:math {"equation":"\\int_{1}^{\\infty} \\frac{1}{x^{2}} \\, dx = \\lim_{t \\to \\infty} \\int_{1}^{t} \\frac{1}{x^{2}} \\, dx = 1"} -->

If the limit is finite, the integral **converges**; otherwise it **diverges**.

## To review before the midterm

- [ ] Drill 10 mixed integrals and name the technique before solving
- [ ] Memorize the three trig-substitution forms cold
- [ ] Re-derive the partial-fractions split for a repeated linear factor
- [ ] Practice one improper integral that diverges (don't just do convergent ones)

<!-- otion:todo {"text":"Build a one-page cheat sheet: technique → when to use it → one example","id":"todo-int-0001","created":"2026-10-01T09:00:00.000Z"} -->
