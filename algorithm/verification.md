# Independent executable verification

Candidate: [algorithm.py](algorithm.py), including canonical source validation,
common-primitive subresultant recovery, and unrestricted integer conversion.
Both forward construction and backward extraction run in fresh subprocesses.
The verifier imports neither the candidate, the prepared checker, nor the
prepared product-basis oracle.

```
python3 campaigns/hadamard-decomposition/work/verify.py --candidate campaigns/hadamard-decomposition/work/algorithm.py
```

[Raw log](../history/campaigns/hadamard-decomposition/rounds/013/literal-rational-check.txt): 29 source instances, 27 YES and
two NO; 109 successful recovery calls, including nine algebraic gauges;
four malformed sources rejected. Seed 13013. The finite domain includes the
empty conjunction, all eight signed repeated-variable clauses, contradictory
units, the eight-clause contradiction on three variables, and 18 generated
formulas on two through four occurring variables. Generated formulas have
n or n+2 clauses. The largest output is 682 by 88, at widths (2,44).

The source decision enumerates every Boolean assignment. The target check reads
and validates the actual output matrix, extracts its cycle coefficients, and
uses exact meet-in-the-middle subset enumeration, separate from the prepared
QF_LRA oracle. It obtains at most two distinct product selections per YES target,
constructs factor witnesses independently, and checks every matrix entry with
rational arithmetic. Recovery is challenged with a non-diagonal left change of
basis, a right shear mixing selector blocks, and signed row and column gauges.
Five additional witnesses use a square-root-of-two left shear. Four focused
recovery calls reuse the existing negative unit formula with a negative square
root, cube root, and two reducible defining polynomials. These are additional
witnesses, not new distinct sources. Exact polynomial identities verify that
each shear and its inverse preserve the already checked factor product.
The returned assignments are checked directly against source clauses.

Malformed source cases include a 5,001-digit declared variable count. The
canonical occurrence condition rejects it without creating that many variables.
Compressed-exponent strings are rejected before numeric conversion in both
coordinate coefficients and interval endpoints; two targeted invalid-encoding
checks exercise this boundary. The implementation explicitly removes Python's integer-to-decimal conversion
limit so that valid large binary integers do not create an artificial cutoff.

These are finite checks, not a general proof. In particular, both target NO
oracles rely on the same mathematical product-basis characterization. Independent
implementations reduce coding correlation but do not make that lemma true.
[proof.md](../paper/proof.md) must establish it for arbitrary real factors, including
nonrational entries, degeneracy, gauge changes and both choice orientations.
The executable tests cover rational, quadratic and cubic algebraic witnesses,
not every algebraic degree. A [targeted arithmetic check](../history/campaigns/hadamard-decomposition/rounds/013/arithmetic-check.py)
compares the implemented sign-corrected subresultant root count with SymPy's
separate rational Sturm routine on reducible, repeated-root, negative-leading
and degree-five polynomials; [log](../history/campaigns/hadamard-decomposition/rounds/013/arithmetic-check.txt). The proof supplies the all-witness statement and bit bounds.
No solver, subprocess or campaign timeout is configured.
