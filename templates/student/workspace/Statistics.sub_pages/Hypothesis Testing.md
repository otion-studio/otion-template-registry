---
title: Hypothesis Testing
icon: FileText
---

# Hypothesis Testing

A formal procedure for deciding whether the data give enough evidence to reject a default claim. The exam wants the *logic*, not just a number.

## The two hypotheses

- **Null hypothesis** `H_0` — the default, "no effect / no difference."
- **Alternative hypothesis** `H_1` — what you're trying to find evidence for.

You never *prove* `H_0`; you either reject it or fail to reject it.

## The test statistic

Standardize the sample result into a z-score: how many standard errors the observed mean sits from the hypothesized mean.

<!-- otion:math {"equation":"z = \\frac{\\bar{x} - \\mu_{0}}{\\sigma / \\sqrt{n}}"} -->

The denominator is the **standard error** — the standard deviation of the sampling distribution of the mean.

## The p-value and the decision rule

The **p-value** is the probability of a result at least this extreme *if `H_0` is true*. Compare it to the significance level `α` (often 0.05):

<!-- otion:math {"equation":"p < \\alpha \\;\\Rightarrow\\; \\text{reject } H_{0}"} -->

A small p-value means the data would be surprising under the null, so you reject it.

### Worked example

Sample mean `x̄ = 52`, hypothesized `μ₀ = 50`, `σ = 8`, `n = 64`:

<!-- otion:math {"equation":"z = \\frac{52 - 50}{8 / \\sqrt{64}} = \\frac{2}{1} = 2.0"} -->

A two-tailed test gives `p ≈ 0.046 < 0.05`, so **reject `H_0`**: the mean is significantly different from 50.

## Two kinds of error

- **Type I error** — rejecting a true `H_0` (a false alarm). Probability `α`.
- **Type II error** — failing to reject a false `H_0` (a miss). Probability `β`.

Lowering `α` reduces false alarms but raises the miss rate. There's always a trade-off.

<!-- otion:info {"color":"red","icon":"AlertTriangle","text":"A non-significant result does **not** prove the null is true — it only means you lack evidence against it. Stating it the other way loses points."} -->

## To review for the final

- [ ] Write `H_0` and `H_1` for a worded scenario
- [ ] Compute a z-statistic and find the p-value
- [ ] State the decision *and* interpret it in plain language
- [ ] Explain Type I vs. Type II error with a real-world example

<!-- otion:todo {"text":"Drill the full test pipeline: hypotheses → statistic → p-value → decision → interpretation","id":"todo-hyp-0001","created":"2026-11-28T09:00:00.000Z"} -->
