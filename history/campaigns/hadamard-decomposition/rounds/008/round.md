# Round 008 — reciprocal rank constraints as a selector

## Plan

Action: change from zeros to full-support reciprocal equations. Normalize the
first row and column of A to ones by the allowed Hadamard row/column gauge.
For output J3 and widths (2,2), B is the entrywise reciprocal of A. Scope:
derive both determinant equations for A=[[1,1,1],[1,a,b],[1,c,d]], with nonzero
entries; factor their joint consequences and determine whether they force a
two-valued invariant. Completion: classify or exhibit a continuous family
surviving both equations. No assumption that the gauge forces a,b,c,d themselves.
Reuse Round 002's gauge lesson and Round 007's zero-ownership failure; no relevant
shared entry was found in those searches.

## Evidence and diagnosis

Ran `python3 campaigns/hadamard-decomposition/rounds/008/probe.py` using
SymPy 1.14.0; [output](output.txt). The determinant equations are
ad−a−bc+b+c−d=0 and −abc+abd+acd−ad−bcd+bc=0.
For a≠1, eliminating d yields
−(a−b)(a−c)(b−1)(c−1)/(a−1)=0. The excluded a=1 branch was not
classified; no division-based conclusion is asserted there.

The family b=a,d=c satisfies both equations for every nonzero a,c. Its
normalized 2-by-2 cross-ratio a remains continuous. Therefore this block alone
does not give the proposed two-valued variable. Its branch structure could be
useful only if another gadget excludes unintended equalities. These are symbolic
identities, not a finite-family UNSAT claim. One elimination computation and
two symbolic substitution checks; no solver queries or complete candidate.

**Experience extraction:** none yet. The useful consequence depends on the
larger anchor interface, which is absent. Keep the exact factorization in this
round rather than save a generic warning. Time/token totals unavailable.

## Next action

Before scaling the reciprocal selector, check the whole 3-by-3 full-support
regime. A universal decomposition would show that changing its constants alone
cannot make a standalone YES/NO selector. Low uncalibrated prospects.
