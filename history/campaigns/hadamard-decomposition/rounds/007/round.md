# Round 007 — completion masking without a forcing gadget

## Plan

Action: reconsider via matrix completion. Proposed template: fill missing entries
with zero to form M, use A as the unknown completion, and let B be the 0/1 mask
of prescribed entries. Allow B width at most one plus the number of missing
positions, since B=J minus singleton matrices. Scope: derive the YES direction
and find a tiny NO completion whose Hadamard target passes using another mask.
Completion: establish a counterexample or a converse within this fixed template.
Search shared experience for completion/masking and preserve all previous rank
obstructions. No full SAT mapping is assumed.

## Evidence and diagnosis

No shared experience match. If a completion A has rank≤r, the fixed mask B
does give M=A⊙B and rank(B)≤s+1 for s missing entries. However the converse
is false even with both budgets two and outside Round 006's easy regime.
Use a 4-by-4 partial matrix with fixed leading I3, all other entries fixed zero
except the missing (4,4) entry. Every completion has rank≥3. Filling that entry
with zero gives diag(1,1,1,0), which has a (2,2) Hadamard decomposition by
the three-cell construction of Round 001.

Ran `python3 campaigns/hadamard-decomposition/rounds/007/probe.py`;
[output](output.txt). One explicit witness passed exact validation. The fixed
3-by-3 minor proves the source NO for every real value of the missing entry.
No solver queries, candidate rule, repairs or reruns. Time/token totals unavailable.
Cause: an independently chosen factor may mask additional prescribed zeros;
the output matrix specifies products, not which side is allowed to vanish.

**Experience extraction:** pending `hadamard-completion-mask-leakage.md` in
`research/experience/`; write scope prevents saving it there. This specific
counterexample excludes the zero-fill/rank-budget template, not every completion
reduction. Its YES direction may be reused only with a new mask-forcing argument.

## Next action

Investigate the reciprocal constraints on a full-support submatrix. With a rank-two
anchor, can simultaneous low-rank constraints on A and M/A force a discrete
cross-ratio, giving a route that does not depend on zero ownership? Try one
normalized 3-by-3 all-ones block before composing it. Prospects low; no missing
proof premise will be assumed from a successful local example.
