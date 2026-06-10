---
title: Sequences and Series
icon: FileText
---

# Sequences and Series

A **sequence** is an ordered list of numbers; a **series** is what you get when you add a sequence up. The final is mostly about deciding whether an infinite series converges.

## Sequences

A sequence converges if its terms approach a single limit:

<!-- otion:math {"equation":"\\lim_{n \\to \\infty} a_{n} = L"} -->

Quick facts:

- A bounded, monotonic sequence always converges (Monotone Convergence Theorem).
- `1/n → 0`, `r^n → 0` when `|r| < 1`, and `n^{1/n} → 1`.

## The geometric series

The one closed form everyone must know. For `|r| < 1`:

<!-- otion:math {"equation":"\\sum_{n=0}^{\\infty} a r^{n} = \\frac{a}{1 - r}"} -->

If `|r| ≥ 1` the geometric series diverges.

## Convergence tests (the exam's core)

Pick the test by the *shape* of the terms:

- **n-th term test** — if `a_n` does not go to 0, the series diverges. (Necessary, not sufficient.)
- **p-series** — the series of `1/n^p` converges exactly when `p > 1`.
- **Integral test** — compare to the integral of a matching positive, decreasing function.
- **Comparison / limit comparison** — bound against a series you already understand.
- **Ratio test** — for factorials and exponentials.

The ratio test in symbols:

<!-- otion:math {"equation":"L = \\lim_{n \\to \\infty} \\left| \\frac{a_{n+1}}{a_{n}} \\right|, \\quad L < 1 \\Rightarrow \\text{converges}"} -->

### Worked example

Does the series of `n / 2^n` converge? Use the ratio test:

<!-- otion:math {"equation":"L = \\lim_{n \\to \\infty} \\frac{n+1}{2^{n+1}} \\cdot \\frac{2^{n}}{n} = \\lim_{n \\to \\infty} \\frac{n+1}{2n} = \\frac{1}{2} < 1"} -->

Since `L = 1/2 < 1`, the series **converges**.

## To review before the final

- [ ] Make a flowchart: given a series, which test do I reach for first?
- [ ] Re-derive the geometric series sum formula from scratch
- [ ] Do 5 ratio-test problems with factorials
- [ ] Memorize the p-series rule and prove it once with the integral test

<!-- otion:todo {"text":"Quiz yourself: 8 random series, name the right convergence test in under 30 seconds each","id":"todo-seq-0001","created":"2026-11-15T09:00:00.000Z"} -->
