# Independent executable verification

Candidate: [algorithm.py](algorithm.py), including canonical source validation,
dense per-coordinate algebraic decoding, and unrestricted integer conversion.
Both forward construction and backward extraction run in fresh subprocesses.
The verifier imports neither the candidate, the prepared checker, nor the
prepared product-basis oracle.

```
python3 campaigns/hadamard-decomposition/work/verify.py --candidate campaigns/hadamard-decomposition/work/algorithm.py
```

[Raw log](../rounds/013/independent-check.txt): 29 source instances, 27 YES and
two NO; 105 successful recovery calls, including five irrational gauges;
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
Five additional witnesses use a square-root-of-two left shear; exact algebraic
identities verify that its inverse preserves the already checked factor product.
The returned assignments are checked directly against source clauses.

Malformed source cases include a 5,001-digit declared variable count. The
canonical occurrence condition rejects it without creating that many variables.
The implementation explicitly removes Python's integer-to-decimal conversion
limit so that valid large binary integers do not create an artificial cutoff.

These are finite checks, not a general proof. In particular, both target NO
oracles rely on the same mathematical product-basis characterization. Independent
implementations reduce coding correlation but do not make that lemma true.
[proof.md](proof.md) must establish it for arbitrary real factors, including
nonrational entries, degeneracy, gauge changes and both choice orientations.
The executable tests cover rational and quadratic-algebraic witnesses, not every
algebraic degree. The proof supplies the all-witness statement and bit bounds.
No solver, subprocess or campaign timeout is configured.
