---
title: Linear Algebra
icon: Grid3x3
---

# Linear Algebra — MATH-240

> Dr. Yuki Tanaka · Mon/Wed/Fri 14:00 · Room M-105 · 4 credits

The study of vectors, matrices, and the linear maps between them. The mechanics (solving systems) come easily; the abstract chapters (vector spaces, basis) are where the real work is.

<!-- otion:info {"color":"red","icon":"AlertTriangle","text":"Flagged *Shaky*: **vector spaces, basis, and dimension**. These are conceptual, not computational — budget extra review time."} -->

## Solving linear systems

The workhorse is **Gaussian elimination**: use row operations to reach row-echelon form, then back-substitute. A system in matrix form:

<!-- otion:math {"equation":"A\\mathbf{x} = \\mathbf{b}"} -->

Allowed row operations: swap two rows, scale a row by a nonzero constant, add a multiple of one row to another. None change the solution set.

## Matrix essentials

- **Multiplication** is row-by-column; it is **not** commutative (`AB ≠ BA` in general).
- The **identity** matrix `I` leaves vectors unchanged: `AI = A`.
- The **inverse** `A⁻¹` exists only when `A` is square and its determinant is nonzero:

<!-- otion:math {"equation":"A A^{-1} = A^{-1} A = I"} -->

## Vector spaces (the abstract core)

A **vector space** is a set closed under addition and scalar multiplication, obeying the standard axioms. Key ideas:

- **Subspace** — a subset that is itself a vector space (contains the zero vector, closed under the operations).
- **Linear independence** — no vector is a combination of the others.
- **Basis** — a linearly independent set that spans the whole space.
- **Dimension** — the number of vectors in any basis (it's always the same number).

A set of vectors is linearly independent when the only solution to

<!-- otion:math {"equation":"c_{1}\\mathbf{v}_{1} + c_{2}\\mathbf{v}_{2} + \\cdots + c_{n}\\mathbf{v}_{n} = \\mathbf{0}"} -->

is all coefficients zero.

## Key terms

- **Rank** — the number of pivots, i.e. the dimension of the column space.
- **Span** — all linear combinations of a set of vectors.
- **Null space** — all `x` with `Ax = 0`.
- **Determinant** — a scalar that is nonzero exactly when the matrix is invertible.

## Track your topics

<!-- otion:database {"path":"databases/Topics.db.json","title":"Topics","height":"320"} -->

## To do

<!-- otion:todo {"text":"Write a plain-English definition of 'basis' and check it against the textbook","id":"todo-linalg-0001","created":"2026-11-08T09:00:00.000Z"} -->
