# Testing foundation

`check.py` uses Z3 5.1.0 for exact source SAT and target feasibility. Source
encodings, algebraic witness encodings and both subprocess modes are specified
in [contract.md](contract.md). The current self-test passed after the explicit
canonical-variable, common-primitive and target-shape repairs:

```
python3 campaigns/hadamard-decomposition/work/check.py --self-test
```

[Current log](../history/campaigns/hadamard-decomposition/rounds/013/common-primitive-self-test.txt): six source cases
checked against exhaustive assignments, four defining target equations, exact
irrational witness acceptance and wrong-product rejection, and three faulty
subprocess fixtures rejected. Earlier cited implementations and logs remain
in the owning rounds.

The default `quartic` target oracle writes exactly the unrestricted real entry
equations and invokes QF_NRA. It has no normalization or sign assumptions.
SAT witnesses are checked entry by entry; UNSAT is infeasibility; unknown fails
explicitly. Its practical scope is tiny matrices. The larger graph-sum attempt
in Round 010 was interrupted after a proof normalization became available;
its unknown outcome is not negative mathematical evidence.

The explicitly selected `product-basis` oracle validates the actual output
matrix against the synchronized-selector family, reads its item integers and
target, and solves Boolean-controlled linear prefix equations with QF_LRA.
It does not receive the SAT formula or import the candidate. Every returned
factorization is independently multiplied against every matrix entry. Its
NO decisions depend on the general structural theorem in [proof.md](../paper/proof.md),
which requires independent proof review; this is not a generic Hadamard solver.
Unsupported matrices fail instead of switching methods.

The [structural oracle check](../history/campaigns/hadamard-decomposition/rounds/013/structural-oracle-check.py) compares
32 three-item targets with exhaustive subset enumeration: 16 YES and 16 NO,
all YES products checked, one corrupted cycle rejected. Its
[log](../history/campaigns/hadamard-decomposition/rounds/013/structural-oracle-check.txt) records the finite scope.

The solver's internal scalars remain native exact algebraic numbers. Before
extraction, `common_witness` serializes them through SymPy's number-field routines
into the fixed common-primitive interface. This conversion belongs only to the
test oracle; it is not a step of the reduction algorithm. The self-test checks
its square-root serialization. Prepared injected witnesses are rational;
independent checks exercise nonconstant common-primitive coordinates directly.

The final prepared candidate command is:

```
python3 campaigns/hadamard-decomposition/work/check.py --oracle product-basis --candidate campaigns/hadamard-decomposition/work/algorithm.py
```

[Log](../history/campaigns/hadamard-decomposition/rounds/013/literal-rational-prepared-check.txt): six injected formulas,
four YES and two NO, and eight actual recovery subprocess calls. The largest
output is 682 by 88, with widths 2 and 44. Each YES case uses both an exact
oracle witness and a factor-rescaled witness. No configured timeouts are used.
