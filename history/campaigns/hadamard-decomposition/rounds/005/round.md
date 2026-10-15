# Round 005 — inspect entrywise-power hardness for transferable gadgets

## Plan

Action: focused literature investigation. Scope: inspect arXiv:2607.04875,
its strong-hardness construction and the restrictions used for soundness;
check whether it proves the campaign target or gives an equality gadget.
Follow at most its directly relevant rank/signing references. Completion:
identify the exact transfer or its missing premise. Reuse Round 003's positive
matrix counterexample; do not infer independent-factor hardness from a subfamily.
This is one literature attempt, not a new experimental template family.

## Evidence and diagnosis

Read [arXiv:2607.04875v1](https://arxiv.org/html/2607.04875v1), Section 2.2,
Equation (1), Theorem 2.2 and Corollary 2.3, on 2026-09-15. It reduces
monotone NAE-3SAT to signing a matrix with n+4 columns down to rank n+3.
The converse normalizes a kernel vector and uses fixed entry magnitudes to
force its variable coordinates into {1,3}. This discreteness disappears when
the two entrywise factors vary independently. No equality-forcing gadget for
our target is given there. Its discussion of Hadamard decomposition is a
relation between models, not a hardness theorem for independent factors.

One primary proof inspected, no candidate program, no solver query, no repair.
The result neither closes our question nor repairs Round 003. A direct transfer
would assign both widths n+3, extremely close to the column dimension n+4.
Before trying to adapt its local constants, check whether that width regime is
already universally feasible for independent factors.

**Experience extraction:** none beyond the pending Round 003 distinction;
this is a literature dependency and a new diagnostic hypothesis, not a new
validated exclusion. No shared entry saved. Time/token totals unavailable.

## Next action

Continue with a universal column-partition construction to test the width
regime. This addresses the source-to-target NO direction before investing in
sign gadgets. Prospects low (uncalibrated), because the published discrete
encoding relies on a premise unavailable in our target.
