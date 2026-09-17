---
status: proof-route-hold
openness: supported-within-search-coverage
difficulty: high
importance: high
tags: [matrix-factorization, compression, Hadamard, NP-hardness]
last-literature-check: 2026-09-15
---

# 3-SAT to exact Hadamard decomposition

[Board](README.md) · [Karp contract](README.md#shared-karp-contract)

**Retain as an open target; investigate the proof route before admission.**
The requested contribution is NP-hardness of exact real matrix decomposition
into two low-rank entrywise factors. Numerical decomposition algorithms do not
establish its decision complexity.

## Exact question and required rule

The source is 3-SAT. The target input is a rational matrix M of size m by n
and integers 1 ≤ k1,k2 ≤ min(m,n), with binary numeric encodings. Ask whether
there are real matrices U1,V1,U2,V2 of respective dimensions m by k1, k1 by n,
m by k2, and k2 by n such that

\[
M=(U_1V_1)\odot(U_2V_2).
\]

The product is entrywise; ordinary multiplication is used inside each factor.
There are no positivity, Boolean, orthogonality, or symmetry constraints.
Factor ranks are **at most** k1 and k2. This follows the factor-width
formulation in R1, Equation (4), rather than silently adopting the exact-rank
wording in the compendium. Zero error is essential.

Construct a total deterministic polynomial-time map F ↦ (M,k1,k2), with
F satisfiable if and only if the displayed factorization exists. Give explicit
polynomial bounds on dimensions, coefficient bits and runtime. All well-formed
formulas must yield well-formed target instances, including NO formulas.
Malformed inputs follow the shared contract. A failed construction or a
numerical optimization method does not satisfy this positive target.

A source witness is a satisfying assignment. A target witness consists of the
four factors satisfying every entry equation. The mathematical converse must
cover all real factors; exact executable checks can use real algebraic factors
encoded by a common primitive element, an isolating interval and rational
coordinate polynomials. Real feasibility of this rational polynomial system
implies algebraic feasibility, but no polynomial bound on witness length is
assumed. The rule additionally needs deterministic assignment recovery from
every encoded valid witness, polynomial in formula plus witness length.
Encoding-safe recovery, including factor rescalings, remains a proof obligation.
This extra witness requirement does not change the standard Karp definition.

## Literature and remaining gap

| Primary source and location | Result | Consequence for this question |
|---|---|---|
| R1, Sections 4 and 4.3; Section 9 | Defines the factor-width problem, places zero-error feasibility in ETR, and leaves formal complexity open | Direct origin of the target; the Boolean-semiring observation is a different problem |
| R2, abstract and algorithm description | Alternating optimization solves successive convex subproblems | Does not guarantee polynomial-time global exact feasibility |
| R3, reformulation and algorithms | Manifold and projected-gradient algorithms with numerical comparisons | The rank-one reshaping constraints remain; no matching hardness theorem located |
| R4, abstract and identifiability results | Generic identifiability of Hadamard–Hitchcock tensor decompositions | Generic identifiability and tensor-decomposition subroutines do not decide all rational matrix instances |

- **R1:** Ciaperoni, Gionis, Mannila, [The Hadamard decomposition problem](https://link.springer.com/article/10.1007/s10618-024-01033-y), Data Mining and Knowledge Discovery 38, 2306–2347 (2024), Equation (4), Sections 4.3 and 9.
- **R2:** Wertz, Vandaele, Gillis, [Efficient algorithms for the Hadamard decomposition](https://arxiv.org/abs/2504.13633), v2, 22 April 2025. Abstract and arXiv version record checked; full HTML was unavailable in this search.
- **R3:** Gillis, Saha, Sicilia, Vandaele, [Manifold-based Algorithms for the Hadamard Decomposition](https://arxiv.org/html/2605.28980v1), May 2026; formulation, algorithms and conclusions inspected.
- **R4:** Oneto, Vannieuwenhoven, [Hadamard-Hitchcock decompositions: identifiability and computation](https://arxiv.org/abs/2308.06597), arXiv record and authors' publication listing checked; journal DOI [10.1090/mcom/4174](https://doi.org/10.1090/mcom/4174). Abstract-level coverage here.

Also inspected the statements in [Hadamard ranks of algebraic varieties](https://arxiv.org/html/2510.05231v1), especially its dimension results. These concern generic complex algebraic geometry, not an exact decision algorithm for every real matrix. The compendium's A-Open9 corroborates the direction, but R1 supplies our precise definition.

## Route, initial checks and limitations

At an input zero, the entry equation forces at least one Hadamard factor to
vanish. A potential reduction would use this choice for Boolean logic and rank
constraints to link occurrences. The missing mechanism is a gauge-independent
selector and clause gadget: signed real entries and cancellation inside UjVj
can admit unintended solutions. Neither a rank-product bound nor generic
dimension counting supplies this converse.

Two elementary boundary checks exclude easy cases. A product of two rank-one
matrices is rank at most one, since (uvᵀ)⊙(xyᵀ)=(u⊙x)(v⊙y)ᵀ. Conversely,
any rank-at-most-one matrix is its own Hadamard product with the all-ones
matrix. Also, if M has no zero entries and k1=1, diagonal rescaling shows
feasibility is equivalent to rank(M)≤k2. Thus a route relying on that full-support
case alone cannot establish new hardness unless P=NP.

On 2026-09-15, Python 3 with Z3 `SolverFor('QF_NRA')` existentially quantified
eight scalar factors for two rank-one 2-by-2 matrices. The four equations
`(u[i]*v[j])*(x[i]*y[j]) == M[i][j]` were SAT for M=[[1,2],[2,4]] and UNSAT
for M=I2. Both agree with the preceding identity. These two finite checks test
the endpoint encoding only; they do not establish a useful hardness gadget.
No campaign rounds were run. Experience search for matrix, rank, algebraic,
ReLU, automaton and scheduling found no applicable repository lemma.

**Next bounded exercise:** express a two-choice zero-pattern selector with
both rank budgets at least two in Z3, and test whether every factorization
has one of the intended observable entry patterns. A surviving selector still
needs a general proof, witness decoder and composition without rank leakage.

## Assessment

| Dimension | Assessment and reason |
|---|---|
| Difficulty | High: no established selector or global rank-budget converse; elementary probes do not justify moderate difficulty |
| Importance | High within matrix compression: establish the first located NP-hardness boundary for the exact two-factor real model |
| Priority | First route-screening choice in the current five; current algorithmic activity and a precise zero-error target justify a bounded investigation |

| Gate | Result | Reason |
|---|---|---|
| 1. Precise question | Pass | Fixed languages, rank convention, encodings and universal recovery obligations |
| 2. Applicable results | Pass within coverage | Exact real feasibility distinguished from iterative optimization and generic identifiability |
| 3. Supported openness | Pass within coverage | Explicit R1 question; no matching resolution located in later searches |
| 4. Significance | Pass | New NP-hardness for a studied compression model |
| 5. Proof route | Hold | Boolean selector and sound composition missing |
| 6. Initial investigation | Not assessed for admission | Boundary checks above do not remove Gate 5 |

## Search history

2026-09-15: Web and arXiv queries included `"Hadamard decomposition" complexity open 2026`, `"Hadamard decomposition" "NP-hardness"`, `"Hadamard decomposition" "NP-hard" -quantum -668`, and `"Hadamard–Hitchcock" Oneto Vannieuwenhoven arxiv`. Checked the 2024 origin, 2025 and 2026 algorithm papers, and algebraic aliases. No matching real exact-feasibility hardness theorem was located. Unindexed work, overlooked implications and full proofs of abstract-only follow-ups remain outside coverage. This is supported openness, not a proof that no prior theorem exists.
