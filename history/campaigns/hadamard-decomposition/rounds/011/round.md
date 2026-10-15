# Round 011 — disjoint clique packing can split across product fibers

## Plan

Action: reconsider the unresolved packing converse from Round 004. Round 010's
triangle oracle remains in progress; its analytic basis lemma is already available.
Hypothesis: disjoint clique components sharing left factors must pack as whole
items into p bins of capacity q. Scope: three cliques of size four, p=2,q=6,
using different two-dimensional left bases in six independent right fibers.
Completion: either build a valid product basis and graph-sum factorization,
or identify the obstruction. This is a new composition test, not an expanded
triangle search. Reuse Round 002's exact fiber-freedom counterexample and Round
004's product-basis equivalence; these are local unreviewed findings, not shared
published theorems. No new relevant shared experience entry is available.

## Evidence and diagnosis

Ran `python3 campaigns/hadamard-decomposition/rounds/011/probe.py`;
[output](output.txt), [full rational witness](witness.json). One 30-by-12
target at widths (2,6) passed exact substitution. The 12 identity coordinates
are incidences of a triangle with each edge doubled. Each right fiber carries
the two endpoint left directions, chosen from (1,0),(0,1),(1,1), with its own
dual basis. The four incidences at a vertex share a left direction, so all
six pair sums in each K4 are product vectors. The 18 added rows are valid.

Items 4,4,4 cannot be assigned whole to two capacity-six bins. Thus the
product-basis graph encoding has a NO-to-YES counterexample to the suggested
packing interpretation. Exact substitution and eight subset sums checked;
no solver query or full SAT candidate. No repairs; time/token totals unavailable.
Cause: different right fibers may use different left bases, splitting the
dimension consumed by one item across fibers. This is the dual version of
Round 002's freedom. Global dimension saturation alone does not fix it.

**Experience extraction:** extend pending `hadamard-identity-fiber-freedom.md`
with this composition counterexample. No new distinct shared proposal or file.

## Next action

Try to force a common pair of left directions before encoding clauses. Two
product-vector anchors with independent factors constrain a common neighbor
to the two opposite corners. Test whether anchor cliques can synchronize this
two-choice interface across three variables. This changes the missing premise
implicated by the counterexample. Prospects low but the next lemma is concrete.
