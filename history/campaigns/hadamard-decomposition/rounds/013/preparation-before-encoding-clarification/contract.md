# Exact test contract

Source: `{"n": n, "clauses": [[literal, literal, literal], ...]}`.
Variables are 1 through n; negative integers denote negation. Repetitions are
allowed, clauses have length three, and the empty conjunction is true.
Source witness: `{"assignment": [false, true, ...]}` of length n.

Target: `{"matrix": [[rational, ...], ...], "k1": p, "k2": q}`.
The matrix is nonempty rectangular, entries are integer JSON values or exact
rational strings such as `"2/3"`; 1≤p,q≤min(rows,columns). Target factors
are real, unconstrained in sign. The target is YES exactly when
M=(U1 V1)⊙(U2 V2), with widths p and q.

Target witness: keys `u1`, `v1`, `u2`, `v2` containing matrices of exact
real-algebraic values. Each scalar is an SMT-LIB exact rational or Z3 `root-obj`
constant string. The parser accepts only expressions simplifying to a rational
or real algebraic constant, never free variables. This per-coordinate encoding
is used for injected tests; a completed rule must justify its recovery complexity
and the question's algebraic representation obligations. It must not assume
rational witnesses suffice. Mathematical soundness covers all real witnesses.

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
