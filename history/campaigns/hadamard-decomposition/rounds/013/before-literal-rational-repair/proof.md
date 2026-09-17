# Candidate proof: 3-SAT to exact Hadamard decomposition

Status: complete candidate argument, pending independent review. Finite testing
cannot establish the lemmas below. The target permits arbitrary-sign real
factors and rank at most the given bounds.

## 1. Prime encoding of 3-SAT

Let F have n occurring variables, m three-literal clauses, consecutive variable
indices, and repetitions allowed. Choose distinct primes p_i for variables and
q_j for clauses. For variable i create two integers

    r(i,b) = p_i product_j q_j^(number of occurrences made true by x_i=b).

For each clause j also create integers q_j and q_j². Set

    T = (product_i p_i)(product_j q_j^4).

An exact-product subset chooses exactly one assignment integer for each variable,
by the exponent of p_i. Its contribution to clause prime q_j is the count c_j
of true literal occurrences, in {0,1,2,3}. The two slack integers contribute
0,1,2 or 3. Achieving exponent four is possible exactly when c_j≥1. Thus F
is satisfiable if and only if some subset of these integers has product T.
Recovery reads which true/false integer was selected. This is the familiar
prime-exponent encoding, not claimed as an original contribution.

Pad the item list with ones to length K≥3; otherwise K=2n+2m. Padding changes
neither feasibility nor recovery. The empty formula gives T=1 and three ones.

## 2. Matrix construction from positive integers r_0,...,r_(K-1), T

There are 4K column indices L_i,R_i,X_i,Y_i in that order for each i. Let
N=4K, q=2K and p=2. Construct a matrix M whose rows are the following
coefficient vectors in R^N:

1. The N unit vectors, giving a leading I_N.
2. e_(L_i)+e_(L_j) for every i<j, and likewise for all R pairs.
3. e_(X_i)+e_(L_i), e_(X_i)+e_(R_i), e_(Y_i)+e_(L_i), e_(Y_i)+e_(R_i).
4. C_i=e_(L_i)+e_(R_i)+e_(X_i)+e_(Y_i).
5. K cycle rows. At block i the coefficients are (1,r_i,1,r_i).
   At block i+1 they are (1,1,1,1), except the last row wraps to block zero
   with coefficients (1,T²,T,T). All other coefficients are zero.

The output is (M,2,2K). It has K²+9K rows and 4K columns. Its entries are
nonnegative integers, but the factors are not constrained to be nonnegative.
No target entry, including a zero, is a free or missing entry.

## 3. Saturation determines product vectors and their sums

Suppose M=(UV)⊙(WZ) at the stated widths. For each row a let its product
vector be u_a⊗w_a in R²⊗R^(2K); for each column b take v_b⊗z_b in the
same dual space. Their pairing is precisely M_ab.

The leading identity means that its N row product vectors z_Li,z_Ri,z_Xi,z_Yi
form a basis, and that the column product vectors form its dual basis. A later
row with coefficients c must therefore have product vector sum_j c_j z_j:
all its pairings with the dual basis are fixed. In particular, every prescribed
sum is decomposable. This argument uses full rank N=pq and covers arbitrary
factor coordinates, gauges and cancellations. At-most widths are sufficient:
the identity itself forces the required full ambient dimension.

If nonzero independent product vectors a⊗b and c⊗d have a decomposable sum,
then a,c are proportional or b,d are proportional. Otherwise local linear
functionals map their sum to the 2-by-2 identity, of rank two. The converse is
immediate. Further, three or more independent product vectors with decomposable
pairwise sums must share one factor. If the first two share the left but have
independent right factors, a third without that left line would have to share
both right lines, a contradiction. The other case is symmetric.

## 4. Globally synchronized selectors

The L clique, of size K≥3, must share a left line: a common right line would
confine K independent vectors to a two-dimensional space. Write z_Li=α⊗b_i.
Likewise z_Ri=β⊗c_i. The left vectors α,β are independent. If they were
proportional, each independent pair z_Li,z_Ri would have independent right
factors, and its common neighbors z_Xi,z_Yi would share the same left line.
Then all N basis vectors would lie in a space of dimension 2K<N.

For each i, b_i,c_i are independent. If they were proportional, the common
neighbors would also have that right line (they cannot have both independent
left lines), placing four independent vectors in dimension two.

The common-neighbor conditions therefore force precisely two possibilities,
with nonzero scalars t_i,s_i:

    selected:   z_Xi=t_i α⊗c_i,   z_Yi=s_i β⊗b_i;
    unselected: z_Xi=t_i β⊗b_i,   z_Yi=s_i α⊗c_i.

The two neighbors cannot occupy the same corner because they are independent.
The right vectors b_i,c_i over all i form a basis of R^(2K): otherwise the
N product vectors could not span the tensor product. Thus different blocks
have independent right coordinates, not merely different names.

The calibration row C_i is decomposable exactly when s_i t_i=1, by taking
its 2-by-2 determinant in the α,β and b_i,c_i coordinates. Both diagonal
entries are one, so neither coefficient row vanishes.

## 5. Cycle soundness

For a row whose block-i coefficients are (a,b,c,d), the coordinate matrix is

    selected:   [[a, c t_i], [d/t_i, b]];
    unselected: [[a, d/t_i], [c t_i, b]].

All coefficient patterns used below have ab=cd and no zero entries. Their
blocks have rank one with a well-defined ratio (β coefficient)/(α coefficient).
Define h_i=1/t_i if selected, and h_i=t_i otherwise. Then:

- coefficients (1,1,1,1) have ratio h_i;
- coefficients (1,r_i,1,r_i) have ratio r_i h_i if selected, h_i otherwise;
- coefficients (1,T²,T,T) have ratio T h_i.

Because the two blocks of a cycle row have independent right supports, that
whole row is decomposable only when their ratios agree. Thus, writing
ε_i=1 for selected and zero otherwise, the rows force

    h_(i+1) = r_i^ε_i h_i                 (0≤i<K−1),
    T h_0   = r_(K−1)^ε_(K−1) h_(K−1).

Every h_i is nonzero. Multiplying and cancelling gives product_i r_i^ε_i=T.
No positivity of t_i or factor entries was used. By Section 1, the recovered
selection determines a satisfying assignment of F. This proves the NO direction
for every real factorization, not just the constructed witnesses.

## 6. Completeness

Given an exact-product subset, take independent left vectors α=e_1,β=e_2
and right vectors b_i=e_(2i+1),c_i=e_(2i+2). Set h_0=1 and successively
h_(i+1)=r_i^ε_i h_i. Set t_i=1/h_i for selected items and t_i=h_i otherwise,
and s_i=1/t_i. The four product vectors per selector are scaled, permuted
standard tensor basis vectors. Their duals are also product vectors.

Use their product coordinates for the leading rows and the duals for columns.
The anchor and neighbor rows are product vectors by their common factors;
calibration rows are product vectors by s_i t_i=1. The cycle rows are product
vectors by the ratio identities and the exact-product condition. Factoring each
rank-one 2-by-2K coordinate matrix gives U,W for its row; the dual coordinates
give V,Z. Their entrywise product is exactly M. All these factors can be rational.
This is only a YES witness construction, not a restriction on accepted solutions.

## 7. Executable recovery and bounds

`algorithm.py --extract` compares the left-factor row for L_0 with the row for
X_i. The determinant of these two length-two vectors vanishes exactly for a
selected item, by Section 4. It reads the first 2n selector bits and returns
true exactly when the true-assignment item is selected. Section 1 proves exactly
one item per variable and satisfaction of every clause. This test is invariant
under invertible left-coordinate changes and nonzero Hadamard row gauges.
No solver query, source search, enumeration of subsets or hidden process state
is used by either mode. Recovery uses SymPy's exact univariate polynomial
arithmetic and sign-corrected subresultant Sturm sequences.

Let L be the canonical source bit length and S=n+m+2≤O(L+1). The first n+m
primes have magnitude O(S log S); trial division therefore generates them in
polynomial time. For a primary explicit bound, see Rosser and Schoenfeld,
[Approximate formulas for some functions of prime numbers](https://doi.org/10.1215/ijm/1255631807),
Theorem 3 and its corollary. Small prime indices are checked separately.
Every item has O(S log S) bits; T and T² have O(S log S) bits. K=O(S).
Consequently the dense target has O(S³) entries and O(S⁴ log S) bits, a loose
bound allowing the maximum entry length at every position. A conservative
schoolbook bit-operation bound for prime generation, item products and dense
output is O((L+2)^8); output length is O((L+2)^5). No numeric value is expanded
in unary. Completeness witnesses have polynomial bit length since each h_i is
an item subproduct, with O(S² log S) bits by a loose bound.

A common-primitive target witness specifies an integer polynomial P, a rational
interval (a,b) containing exactly one distinct real root θ of P with non-root
endpoints, and dense rational coordinate polynomials in θ. P may be reducible
or nonsquare-free. Given a determinant polynomial D, D(θ)=0 holds exactly when
gcd(P,D) has a root in (a,b). Every root of this gcd is a root of P, so the
isolating premise makes the count zero or one. The zero determinant is handled
by gcd(P,0)=P; a constant gcd has zero roots. This proves the encoded zero test
without changing the unrestricted-real recovery argument.

The executable obtains the gcd, up to nonzero scale, as the last nonzero term
of `Poly.subresultants`. Its `root_count` clears rational denominators, takes a
primitive integer polynomial, removes repeated factors using the subresultant
gcd with its derivative, and calls SymPy's `sturm_amv` with method=1. This returns
a sign-corrected subresultant sequence. The difference between its sign-variation
counts at a and b is the number of distinct real roots in the interval. Zero
sequence evaluations are omitted. The initial field validation uses the same
procedure; endpoints are checked not to be roots. No univariate factorization,
root approximation, algebraic-number multiplication or feasibility solver is
needed in the candidate. The polynomial operations implement the proof's test.

Here are conservative bit bounds for the actual procedure. Let W be the entire
encoded witness length and B=W+2. Degrees and rational input heights are bounded
by B. Coordinate determinants have degree O(B); clearing denominators gives
coefficient heights O(B²). A subresultant coefficient is a determinant of a
Sylvester submatrix of order O(B), so the first gcd has height O(B³), up to an
irrelevant rational scale. Primitive normalization removes that scale before
root counting. The square-free part has height O(B³) by the polynomial factor
bound; its sign-corrected subresultants have height O(B⁴). The defining polynomial
and derivative satisfy the same bounds. Intermediate exact polynomial divisions
in a subresultant step have degree O(B) and polynomial height; allowing O(B⁸)
bits per intermediate numerator or denominator is a loose upper bound obtained
by O(B) elimination steps on coefficients of height O(B⁴). There are O(B³)
rational coefficient operations per sequence. Schoolbook rational arithmetic
therefore fits within O(B²⁴) bit operations, including input conversion and
endpoint evaluation. Rational normalization uses ordinary integer gcd, also
polynomial. This deliberately loose bound covers the controlled subresultant
procedure actually called, not an unspecified replacement algorithm.

The standard coefficient and operation bounds are supported by Emiris, Mourrain
and Tsigaridas, [Real Algebraic Numbers: Complexity Analysis and Experimentation](https://who.paris.inria.fr/Elias.Tsigaridas/files/emt-lncs-2006.pdf),
Theorems 2.1–2.4 and Section 6. For the sign-corrected sequence used by the
implementation, see Akritas, [Anna Johnson and Her Seminal Theorem of 1917](https://faculty.e-ce.uth.gr/akritas/publications/100.pdf),
Section 2.4.3, Theorem 5 and the immediately following identification of
`sturm_amv`; and SymPy 1.14.0's installed `subresultants_qq_zz.py` routine.
The implementation uses the mature polynomial library, not a new root solver.

There are 2n determinant queries and one field check. The backward algorithm
thus takes O((L+1)(W+2)²⁴) bit operations and outputs O(L+1) bits. Dense encoding
is essential: sparse exponents cannot hide uncharged degree. The procedure is
polynomial in the supplied witness length, not necessarily in formula length
alone. Soundness of the abstract determinant recovery holds for every real
witness; the executable covers the fixed common-primitive algebraic interface.
A nonempty rational polynomial solution set has a real-algebraic point by real
closed field transfer. No rational-witness assumption is made.

Malformed source strings map to a designated invalid target encoding, outside
the target language. Source JSON uses exactly the occurring variables; this is
a polynomially obtainable canonical representation of ordinary 3-SAT formulas.

## 8. Novelty, significance and limits

The proposed new component is the synchronized product-basis selector and its
multiplicative cycle in Sections 2–6. The prime encoding, tensor-product rank
identity and elementary rank-one sum lemma are credited as standard ingredients.
Wertz, Vandaele and Gillis (arXiv:2504.13633v2, Appendix B, Lemma 2) already
give identity factorizations. Gillis, Saha, Sicilia and Vandaele
(arXiv:2605.28980v1, Lemmas 2.3–2.4) give the face-splitting/rank-one reshape
formulation. These are explicit prior ingredients, not claimed discoveries.
If correct and novel, the construction establishes NP-hardness of exact real
Hadamard decomposition even when one rank bound is two and the target matrix
is nonnegative integer. It does not establish ∃R-completeness or NP membership
of the unrestricted problem. Only the constructed family has the discrete
certificate characterization above.

The campaign question records the 2024 open question and subsequent numerical
algorithms. The additional July 2026 entrywise-power paper, discussed in Round
005, fixes magnitudes of a single factor and does not prove independent-factor
hardness. Web/arXiv queries on 2026-09-15 additionally checked Hadamard decomposition
with subset product, product basis and NP-hardness. No matching theorem was found;
unindexed work and overlooked equivalent reductions remain outside coverage.
