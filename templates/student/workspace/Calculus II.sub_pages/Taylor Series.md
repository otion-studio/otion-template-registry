---
title: Taylor Series
icon: FileText
---

# Taylor Series

The idea: approximate any smooth function near a point by an infinite polynomial built from its derivatives. This ties together everything from the series unit.

## The Taylor series

Centered at `a`, the Taylor series of `f` is:

<!-- otion:math {"equation":"f(x) = \\sum_{n=0}^{\\infty} \\frac{f^{(n)}(a)}{n!} (x - a)^{n}"} -->

When `a = 0` it's called a **Maclaurin series** — the most common case on the exam.

## The three you must memorize

These come up constantly; know them cold.

<!-- otion:math {"equation":"e^{x} = \\sum_{n=0}^{\\infty} \\frac{x^{n}}{n!} = 1 + x + \\frac{x^{2}}{2!} + \\frac{x^{3}}{3!} + \\cdots"} -->

<!-- otion:math {"equation":"\\sin x = \\sum_{n=0}^{\\infty} \\frac{(-1)^{n} x^{2n+1}}{(2n+1)!}"} -->

<!-- otion:math {"equation":"\\cos x = \\sum_{n=0}^{\\infty} \\frac{(-1)^{n} x^{2n}}{(2n)!}"} -->

## Worked example

Find the Maclaurin series for `f(x) = e^{2x}`. Substitute `2x` into the known series for `e^x`:

<!-- otion:math {"equation":"e^{2x} = \\sum_{n=0}^{\\infty} \\frac{(2x)^{n}}{n!} = 1 + 2x + 2x^{2} + \\frac{4x^{3}}{3} + \\cdots"} -->

Substitution beats recomputing derivatives — always check whether you can reuse a known series first.

## Radius of convergence

A Taylor series only equals the function inside its **radius of convergence** `R`, found with the ratio test on the series terms. Outside `R` the series diverges and the approximation is meaningless.

<!-- otion:info {"color":"green","icon":"Lightbulb","text":"Exam tip: most Taylor questions are really *substitution + a known series*. Spot the standard form before reaching for derivatives."} -->

## To review before the final

- [ ] Write out `e^x`, `sin x`, `cos x` series from memory, no notes
- [ ] Practice deriving a series by substitution (e.g. `cos(x^2)`)
- [ ] Find the radius of convergence for two different series
- [ ] Connect this back to the convergence tests page

<!-- otion:todo {"text":"Flashcard the three core Maclaurin series and test recall twice this week","id":"todo-taylor-0001","created":"2026-11-22T09:00:00.000Z"} -->
