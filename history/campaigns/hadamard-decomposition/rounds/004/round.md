# Round 004 — product-basis graph encoding

## Plan

Action: reconsider to a sum-of-product-vectors mechanism. Fix N=pq and a graph
H on N indices. Let R contain I_N and one row e_i+e_j per edge. Set M=R,
with N columns and widths p,q. Investigate whether feasibility is equivalent
to a Cartesian rook-grid embedding of H. Scope: derive the basis formulation,
the edge-sum constraint, and examine disjoint clique components as potential
bin-packing items. Stop when the exact residual characterization is identified.
No parameter sweep or candidate SAT mapping. Reuse the non-grid counterexample
from Round 002; it forbids assuming a Cartesian basis in the converse.

## Evidence and diagnosis

The identity rows give a basis z_i=a_i⊗b_i of R^p⊗R^q, and the target
columns give its dual basis c_j⊗d_j, since all N² pairings equal δij.
An edge row must equal z_i+z_j: its N pairings with the dual basis determine
it uniquely. Hence each edge requires this sum to be decomposable.

For two independent nonzero product vectors, their sum is decomposable exactly
when their left factors are proportional or their right factors are proportional.
Proof: if both pairs are independent, choose linear functionals sending each
pair to the standard basis; the sum then maps to the rank-two identity matrix.
The converse is immediate by factoring the common side.

Conversely, any product basis with a product dual and decomposable prescribed
edge sums yields a factorization of R by taking those product coordinates as
the rows and dual coordinates as columns. This is an exact reformulation,
not a SAT reduction and not a known NP-hardness theorem.

A clique of independent basis vectors must share one factor: start with two
sharing the left factor; a third not sharing it would have to share both
independent right factors, which is impossible. Such a clique has size at most
q (left common) or p (right common). Disjoint cliques therefore suggest packing
dimensions, but dimensions alone do not force at most p different left lines.
Round 002 shows why assuming a single grid is unjustified. No packing converse
or polynomial-time witness recovery was proved. Three analytic claims; no
solver query, no complete construction and no repairs.

Supporting Web queries on product bases and square-root rank located a new
primary lead: [On the Complexity of Entrywise Power Matrix Factorization](https://arxiv.org/abs/2607.04875),
July 2026. Its abstract gives strong hardness for the equal-factor signing
problem, not this target. The next round will inspect the proof for transferable
gadgets; the Round 003 counterexample remains applicable.

**Experience extraction:** none as a new shared entry. The product-basis
reformulation remains an unreviewed local route, without a construction exclusion
or a validated decoder. Its warning about a grid converse is already covered
by the pending Round 002 entry. Time/token totals unavailable.

## Next action

Investigate the newly located 2026 signing construction rather than expand the
unproved packing idea. It might provide exact rank constraints with explicit
Boolean recovery. Low uncalibrated short-term prospects; equality of factors
is still a central missing premise.
