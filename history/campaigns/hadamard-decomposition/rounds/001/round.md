# Round 001 — rank-one and rank-product boundaries

## Plan

Action: investigate the proposed zero-pattern route before selecting gadgets.
Hypothesis: zeros might permit Boolean choices even with one rank budget equal
to one. Scope: prove or refute this for arbitrary real matrices, and derive the
identity-matrix feasibility boundary. Two analytic claims, no candidate search.
Completion: explicit converse or counterexample. Experience retrieval using
`rg -n -i 'hadamard|rank|matrix|zero.pattern|tensor|gauge' research/experience`
found no relevant entry. Preparation is complete and reused.

## Evidence and diagnosis

The rank-one hypothesis is false for every support pattern. If
M=(uvᵀ)⊙B, then M=diag(u)B diag(v), so rank(M)≤rank(B)≤q.
Conversely M=J⊙M gives a width-(1,q) decomposition whenever rank(M)≤q.
Zeros do not change this equivalence. This strengthens the card's full-support
observation, but is elementary rather than a publishable discovery.

For arbitrary widths p,q, write A and B as sums of p and q rank-one terms.
Their entrywise product is a sum of pq rank-one terms, giving rank(M)≤pq.
For I_N this is sufficient: assign N distinct cells of a p-by-q grid to the
indices, and put Aij=1 exactly when their first coordinates agree and Bij=1
exactly when their second coordinates agree. Their ranks are at most p and q
and A⊙B=I_N. Thus I_N is feasible exactly when N≤pq.

Two general boundary claims checked analytically; zero solver queries and zero
candidate rules. No repairs. Result: exclude rank-one zero-pattern selectors;
retain saturated identity anchors as a possible interface. Confidence: direct
algebraic proofs, not independently reviewed. Time/token totals unavailable.

**Experience extraction:** pending shared entry `hadamard-rank-boundaries.md`
under `research/experience/` (writes restricted to this campaign). Claim: one
width equal to one collapses to ordinary rank for every matrix; identities only
test the product of widths. Consequence: neither supplies Boolean hardness alone.
This round is the proposed entry and its evidence; no shared entry was saved.

## Next action

Continue with a saturated identity of order four and widths (2,2): test whether
all decompositions really induce one rectangular grid. A non-grid feasible
decomposition would invalidate decoding row/column labels from the identity
alone. Short-term prospects remain unknown; this is a structural diagnostic.
