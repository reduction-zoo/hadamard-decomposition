# Round 012 — synchronize a two-choice product-basis selector

## Plan

Action: repair the interface implicated in Round 011, not its packing constants.
For n≥3 use 4n basis indices L_i,R_i,X_i,Y_i, widths p=2,q=2n. Put cliques
on the L indices and R indices; connect each X_i and Y_i to both L_i,R_i.
Use the identity-plus-edge-sum matrix of Round 004. Scope: prove that every
factorization has two globally independent left anchor lines and that X_i,Y_i
occupy opposite corners relative to L_i,R_i. Test eight constructed assignments
for n=3 by exact substitution. Completion: local soundness and completeness,
with normalization and outstanding clause obligations explicit. Reuse the
Round 011 composition failure and Round 004 independent-vector sum lemma.

## Evidence and diagnosis

The n≥3 anchor cliques force a common left direction α for L_i and β for
R_i: a common right direction cannot support three independent basis vectors
in left dimension two. If α=β, each X_i,Y_i must share that left direction
as well (the two independent anchors cannot share a right direction), violating
the rank 4n identity block. Thus α,β are independent.

Write L_i=α⊗b_i and R_i=β⊗c_i. If b_i,c_i were proportional, all four
vectors for that variable would lie in a two-dimensional fiber, contradicting
independence. The two common neighbors X_i,Y_i must therefore occupy the
opposite corners α⊗c_i and β⊗b_i, in either order, with nonzero scalar
multipliers t_i,s_i. They cannot choose the same corner. All b_i,c_i together
are independent because the 4n basis vectors span R²⊗R^(2n).

Ran `python3 campaigns/hadamard-decomposition/rounds/012/probe.py`;
[output](output.txt). All eight choices for three selectors yield valid
factorizations; each also passed after nonzero row gauge rescaling. Sixteen
exact witness validations and sixteen local direction decodings, no source
SAT reduction calls or existential solver queries. No repairs. The converse
above is an unreviewed general argument, not a consequence of these tests.

The remaining continuous multipliers are essential. An added sum row
L_i+R_i+X_i+Y_i is decomposable exactly when s_i t_i=1. After this
calibration, different weighted rows involving a selector can compare either
t_i or 1/t_i. This suggests multiplicative constraints along a cycle rather
than a direct Boolean clause gadget.

**Experience extraction:** pending `hadamard-product-basis-selectors.md` under
`research/experience/`, because writes remain campaign-local. Claim: saturated
identity, anchor cliques and four common-neighbor constraints force two opposite
corners, with the specified residual scalars. No complete-rule or novelty claim.
Time/token totals unavailable.

## Next action

Continue by encoding subset product with a cycle of rank-one sum constraints.
The discriminating check is an all-witness derivation of the cycle equation,
including the residual t_i. This uses the actual scalar freedom instead of
incorrectly suppressing it. Short-term prospects now medium, uncalibrated,
conditional on the cycle soundness argument surviving review.
