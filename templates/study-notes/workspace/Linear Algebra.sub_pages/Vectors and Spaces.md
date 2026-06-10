---
title: Vectors and Spaces
icon: Move3d
---

# Vectors and Spaces

Lecture 1–3 notes. The whole course builds on these definitions, so keep them sharp.

## Vectors

- A vector in n-dimensional space is an ordered list of n real numbers.
- Addition and scalar multiplication happen component-wise.
- Geometric picture: arrows from the origin; addition is tip-to-tail.

The dot product measures alignment between two vectors:

<!-- otion:math {"equation":"\\mathbf{u} \\cdot \\mathbf{v} = \\sum_{i=1}^{n} u_i v_i = \\lVert \\mathbf{u} \\rVert \\, \\lVert \\mathbf{v} \\rVert \\cos\\theta"} -->

- Dot product zero means the vectors are orthogonal.
- The norm of a vector is the square root of its dot product with itself.

## Vector spaces

- A vector space is a set closed under addition and scalar multiplication, satisfying the eight axioms (associativity, commutativity, identity, inverses, distributivity).
- A **subspace** is a subset that is itself a vector space — it must contain the zero vector.
- The **span** of a set of vectors is every linear combination of them:

<!-- otion:math {"equation":"\\operatorname{span}\\{\\mathbf{v}_1, \\ldots, \\mathbf{v}_k\\} = \\left\\{ \\sum_{i=1}^{k} c_i \\mathbf{v}_i \\;\\middle|\\; c_i \\in \\mathbb{R} \\right\\}"} -->

## Linear independence and basis

- Vectors are linearly independent when the only combination giving zero is all coefficients zero.
- A **basis** is a linearly independent spanning set; every vector then has exactly one coordinate representation.
- The **dimension** of a space is the size of any basis — all bases have the same size.

## Review checklist

- [x] Prove that the intersection of two subspaces is a subspace
- [x] Practice: is the set of polynomials of degree exactly 3 a vector space? (No — not closed under addition)
- [ ] Find a basis for the null space of the example matrix from lecture 3
- [ ] Memorize the eight vector space axioms

<!-- otion:todo {"text":"Ask in section why span of the empty set is defined as the zero space","id":"todo-2026-06-10-102","created":"2026-06-10T08:35:00.000Z"} -->
