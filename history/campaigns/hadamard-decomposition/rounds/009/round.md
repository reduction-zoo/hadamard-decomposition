# Round 009 — a nonzero reference column enlarges the trivial regime

## Plan

Action: investigate the constant-changing alternative to Round 008. Hypothesis:
if one column has no zero entries and n≤p+q−1, all matrices in that regime
are feasible. Scope: row normalization, direct splitting and a full-rank 3-by-3
example at widths (2,2). Completion: general proof and exact witness validation.
This extends Round 006's bound under a new support premise, not another
parameter sweep. Reuse its pending rank-boundaries experience proposal.

## Evidence and diagnosis

Divide each row by its nonzero reference-column entry, making that column all
ones. Partition the other columns into S,T with |S|≤p−1,|T|≤q−1. Copy their
entries into A on S and B on T, and put ones elsewhere in each factor.
The rank bounds are at most p and q. Restore the row scaling to A; its rank
does not change. This proves the asserted regime for every matrix satisfying
the reference-column premise, including arbitrary zeros elsewhere.

The construction uses O(mn) rational operations with polynomial bit length.
Ran `python3 campaigns/hadamard-decomposition/rounds/009/probe.py`;
[output](output.txt). One full-rank 3-by-3 instance was checked by exact
substitution, no solver queries. No repairs or candidate rule.
Thus changing constants in a full-support 3-by-3 output cannot make a NO
instance at widths (2,2); such a block could only work as part of a larger
shared-rank construction. This does not exclude all reciprocal gadgets.

**Experience extraction:** update the pending `hadamard-rank-boundaries.md`
proposal from Rounds 001 and 006 with this support-sensitive bound. No new
distinct entry, and no shared file written. Time/token totals unavailable.

## Next action

Return to Round 004's product-basis interface. Test a triangle and a four-cycle
using exact certificates. These have four identity columns and avoid the
three-column universal regime. The result will determine whether this interface
at least supplies a nontrivial NO obstruction. Prospects remain low.
