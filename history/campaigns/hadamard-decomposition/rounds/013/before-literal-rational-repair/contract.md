# Exact test contract

Source: `{"n": n, "clauses": [[literal, literal, literal], ...]}`.
Variables are 1 through n; negative integers denote negation. Repetitions are
allowed, clauses have length three, and the empty conjunction is true.
The declared variables are exactly those occurring, consecutively numbered;
the empty formula uses n=0. Hence n≤3 times the clause count. This canonical
encoding prevents a binary count of exponentially many unused variables from
requiring an exponentially long assignment. Renaming the occurring variables
of a conventional 3-SAT formula to this encoding is polynomial-time.
Source witness: `{"assignment": [false, true, ...]}` of length n.

Target: `{"matrix": [[rational, ...], ...], "k1": p, "k2": q}`.
The matrix is nonempty rectangular, entries are integer JSON values or exact
rational strings such as `"2/3"`; 1≤p,q≤min(rows,columns). Target factors
are real, unconstrained in sign. The target is YES exactly when
M=(U1 V1)⊙(U2 V2), with widths p and q.

Target witness: keys `field`, `u1`, `v1`, `u2`, `v2`.
`field` is `{"polynomial": [-2,0,1], "interval": ["1","2"]}`: a dense
integer defining polynomial in ascending degree, and two rational non-root
endpoints isolating exactly one distinct real root θ. The polynomial may be
reducible or have repeated roots. Each matrix entry is a nonempty dense list of
rational coefficients in ascending degree, evaluated at the same θ. For example,
`["3/2","1"]` means 3/2+θ. Rational coefficients are integer JSON values or
exact rational strings; floating-point JSON numbers and symbolic expressions are
not allowed. A rational-only witness can use polynomial `[0,1]`, interval
`["-1","1"]`, and constant coordinate polynomials. Every degree, coefficient
bit and interval endpoint bit is charged to witness length. The four matrix
shapes are the factor shapes in the fixed question.

Recovery accepts every valid witness in this common-primitive representation.
It forms coordinate-polynomial determinants, computes their gcds with the defining
polynomial using subresultants, and counts roots inside the supplied interval
with sign-corrected subresultant Sturm sequences. It never constructs a compositum
or invokes a feasibility solver. Mathematical soundness separately covers all
real witnesses, including values without a finite algebraic encoding. Rational
polynomial feasibility implies real-algebraic feasibility, but no polynomial
bound on arbitrary target-witness length is assumed.

The candidate is a standalone Python program. It reads one source JSON from
stdin and prints one target JSON. With `--extract`, it reads
`{"source": source, "target_solution": witness}` and prints a source witness.
Both modes must work in fresh processes. No solver or exponential source search
is permitted in the resulting polynomial-time reduction algorithm. The test
oracle is separate and may use Z3.

The harness runs the actual subprocess, validates its target, compares independent
source/target decisions, and tests extraction on a solver witness and a
factor-rescaled witness. All exact products and source clauses are checked
directly. Invalid encodings, unknown solver status, execution errors and wrong
witnesses fail explicitly. No runtime timeout is configured.
