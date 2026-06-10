---
title: Matrix Operations
icon: Grid3x3
---

# Matrix Operations

Lecture 4–6 notes. Matrices as linear maps, and the algebra that goes with them.

## Matrix multiplication

- A matrix with m rows and n columns represents a linear map from n-dimensional space to m-dimensional space.
- Multiplication is composition of maps — that is why it is **not commutative**.
- Entry by entry, the product is a dot product of a row with a column:

<!-- otion:math {"equation":"(AB)_{ij} = \\sum_{k=1}^{n} a_{ik}\\, b_{kj}"} -->

- Dimensions must match: an m-by-n matrix times an n-by-p matrix gives an m-by-p matrix.

## Transpose and inverse

- Transpose swaps rows and columns; the transpose of a product reverses the order.
- A square matrix is invertible exactly when its determinant is nonzero.
- For a 2-by-2 matrix the inverse has a closed form:

<!-- otion:math {"equation":"A^{-1} = \\frac{1}{ad - bc} \\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}, \\qquad A = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}"} -->

## Determinants — key facts

- The determinant of a product is the product of determinants.
- Swapping two rows flips the sign; scaling a row scales the determinant.
- Geometrically, the absolute value of the determinant is the volume-scaling factor of the map.
- Triangular matrices: determinant is the product of the diagonal entries.

## Review checklist

- [x] Multiply two 3-by-3 matrices by hand without errors
- [x] Show by example that AB and BA can differ
- [ ] Prove that the inverse of a product reverses the order
- [ ] Compute a 3-by-3 determinant by cofactor expansion and by row reduction, compare work

<!-- otion:todo {"text":"Redo Problem Set 2 question 4 — lost points on the row-reduction bookkeeping","id":"todo-2026-06-10-103","created":"2026-06-10T08:40:00.000Z"} -->
