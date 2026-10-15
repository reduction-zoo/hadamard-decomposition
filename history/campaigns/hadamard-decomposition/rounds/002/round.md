# Round 002 — saturated identity does not force a common grid

## Plan

Action: continue from Round 001. Hypothesis: I4 at widths (2,2) forces a
Cartesian product basis, up to invertible changes in each factor and scalings.
Scope: one controlled-basis construction, verified exactly by the prepared
witness checker. Completion: verify the construction and count projective right
factor directions. Reuse Round 001's identity boundary; no shared experience
entry exists. No repeated external experience search is needed for the unchanged
rank/identity mechanism; the preceding search found no applicable entry.

## Evidence and diagnosis

Ran `python3 campaigns/hadamard-decomposition/rounds/002/probe.py` from the
repository root; [output](output.txt), [exact witness](witness.json).
The left product vectors use e1,e1,e2,e2, while the right vectors use
(1,0),(0,1),(1,1),(1,-1). The dual columns use the corresponding dual basis
separately in the e1 and e2 blocks. Their products give I4 exactly.

There are four distinct right projective directions, invariant under invertible
right-factor transformations and nonzero scalings. A 2-by-2 Cartesian basis
has two. Thus identity saturation does not imply a common grid, even allowing
permutations and swapping the two factors. One constructed witness, one exact
validator call, no existential solver queries, no candidate rule and no repairs.
Cause: independent basis changes inside separate left-factor fibers preserve
all identity equations. This is a concrete counterexample, not an exclusion of
every possible anchor. No independent review; time/token totals unavailable.

**Experience extraction:** pending `hadamard-identity-fiber-freedom.md` in
`research/experience/`, blocked by campaign-only writes. Claim and evidence are
the preceding counterexample. Consequence: grid-based decoding needs additional
constraints linking fiber bases. No shared entry was saved.

## Next action

Reconsider a different source of Boolean choice: the signs in square-root rank.
Before using its known hardness, test whether independent Hadamard factors can
evade the equal-factor restriction. Prospects of a full reduction remain low
(uncalibrated); neither selector nor composition is available.
