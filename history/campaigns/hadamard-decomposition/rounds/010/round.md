# Round 010 — nontrivial graph-sum YES and NO outputs

## Plan

Action: continue the product-basis route from Round 004 using Round 009's
size exclusion. Scope: four identity rows and one row e_i+e_j per edge,
four columns, widths (2,2). Compare a triangle plus isolated vertex with a
four-cycle. Establish both decisions analytically and check a constructed
YES witness. Try the prepared unrestricted real oracle on the triangle as
one independent encoding check. No larger graph enumeration in this round.
Completion: decisions, test evidence and remaining SAT-composition obstruction.
Reuse the local product-basis lemma; no applicable shared entry.

## Evidence and diagnosis

The C4 construction passed exact validation in [probe.py](probe.py).
For a triangle, its three independent product vectors have decomposable pair
sums, so Round 004's lemma forces a common factor. Their span then has dimension
at most two, contradicting the identity block. This proves NO for all real factors.

The unrestricted quartic oracle run was deliberately interrupted after choosing
an algebraically normalized formulation; it returned `unknown`, which the checker
correctly rejected. The [original log](output.txt) is retained. This was an
explicit method change, not a configured timeout, and is not counted as UNSAT.

Normalize the first nonzero product vector to e1⊗e1 by invertible local maps.
The rank-one conditions for the other vectors and their sums with the first
force their bottom-right entries to vanish and bc=fg=0. Their mutual sum
requires (b+f)(c+g)=0, whereas independence requires bg−cf≠0. The
[normalized query](normalized_triangle.py) returned UNSAT; see
[log](normalized-output.txt). Normalization preserves all linear relations
and independence, so this check corroborates the analytic contradiction.

One exact YES witness; two solver attempts (one interrupted/unknown, one UNSAT).
The base checker and acceptance criteria were unchanged. No full SAT mapping.
The unrestricted oracle is expensive even for this 7-by-4 example; larger
candidate outputs will need a separately justified exact structural oracle.
No numerical tolerance was introduced. Time/token totals unavailable.

**Experience extraction:** none beyond the local product-basis lemma and pending
rank-boundaries entry. The triangle obstruction is retained here as a regression
case; no additional reusable shared file was created.

## Next action

Continue the separately declared synchronization investigation in Round 012.
This round shows the target interface can distinguish YES and NO; it does not
establish hardness or a polynomial source-witness decoder.
