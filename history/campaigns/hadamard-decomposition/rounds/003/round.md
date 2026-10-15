# Round 003 — square-root rank is a stricter problem

## Plan

Action: reconsider the mechanism. Hypothesis: square-root-rank feasibility
could transfer directly to two independent Hadamard factors of the same width.
Scope: M=[[1,1,1],[1,2,3],[1,3,5]], widths (2,2); test all 16 sign patterns
of its entrywise square root after normalizing first-row/first-column signs.
Completion: find or exclude a rank-two signed square root and give an explicit
independent-factor decomposition. This differs from the identity-grid route.
Prior local findings impose no equal-factor constraint. Search shared experience
for square-root, signs and Hadamard before the probe.

## Evidence and diagnosis

No shared experience match. Ran `python3 campaigns/hadamard-decomposition/rounds/003/probe.py`;
[raw output](output.txt). Four positive radicals were obtained with exact Z3
NRA queries. All 16 normalized sign assignments have nonzero determinants,
checked by exact algebraic simplification. Row and column sign flips normalize
any of the 512 possible sign matrices because the first row and column are
strictly nonzero, and preserve rank. Thus no signed square root has rank two.
Nevertheless M=J⊙M is feasible at widths (2,2), since M has rank two; an
explicit factor witness passed the independent validator.

This is a NO-to-YES counterexample to the direct equal-width identity mapping
from square-root rank, not a refutation of a reduction with equality-forcing
gadgets. Four solver queries, 16 determinant checks, one explicit factor witness,
zero candidate rules. No repairs or reruns. Time/token totals unavailable.

**Experience extraction:** pending `independent-hadamard-factors-do-not-enforce-square-roots.md`
under the shared experience directory. The concrete positive matrix above
excludes treating equal rank budgets as equal factors. Evidence and consequences
are complete in this round; shared writes are outside the authorized campaign path.

## Next action

Investigate a combinatorial alternative using independent product-vector bases
and sums. Try to characterize what graph constraints are enforceable before
attempting a SAT gadget. This could expose a source problem with existing hardness,
but the transformation and all-witness converse are not established.
