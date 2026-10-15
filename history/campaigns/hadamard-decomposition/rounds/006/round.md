# Round 006 — universal column-splitting obstruction

## Plan

Action: investigate the high-width transfer from Round 005. Hypothesis: every
m-by-n matrix admits a Hadamard decomposition with widths p,q whenever
n≤p+q−2. Scope: direct construction, rank proof and a rational 4-by-4
example at widths (3,3). If true, apply it to the n+4-column signing reduction.
Completion: general construction plus exact witness check. This is a rank-budget
diagnostic, not a new SAT candidate. Reuse the existing rank experience search
and Round 001; the source has no relevant shared entry.

## Evidence and diagnosis

Partition the columns into S,T with |S|≤p−1 and |T|≤q−1. Set A[:,S]=M[:,S],
A[:,T]=1 and B[:,S]=1,B[:,T]=M[:,T]. Then A⊙B=M, rank(A)≤|S|+1≤p
and rank(B)≤|T|+1≤q. The construction is deterministic and uses only copied
entries and ones; its encoding size and arithmetic cost are O(mn) entries.
Explicit rectangular factors are formed by the exceptional columns plus one
all-ones column. The same argument applies to rows by transposition.

Ran `python3 campaigns/hadamard-decomposition/rounds/006/probe.py`;
[output](output.txt). One explicit 4-by-4 witness at widths (3,3) passed exact
validation. No existential queries or complete reduction candidates.
No repairs; time/token totals unavailable. The general proof is elementary
and unreviewed, not claimed as original mathematical discovery.

Round 005's matrix has n+4 columns and would have widths (n+3,n+3).
Since n+4≤2n+4, **all** these independently factored targets are YES,
irrespective of their NAE formula. This excludes the direct transfer of that
published construction, more strongly than the isolated Round 003 example.

**Experience extraction:** add this general regime to the pending
`hadamard-rank-boundaries.md` entry from Round 001. No second entry count.
Consequence: require both min(m,n)>p+q−2 and rank(M)≤pq for a potentially
discriminating target; these are necessary screening conditions, not sufficient
hardness conditions. Shared extraction remains pending due to write scope.

## Next action

Reconsider rank-completion encodings with low-rank masks rather than high-width
signing. The first check is whether a proposed mask is forced in all solutions,
or whether a different mask leaks the rank budget. Prospects remain low.
