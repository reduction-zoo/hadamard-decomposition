# Hadamard decomposition campaign

Status: ready for expert review. The reviewed candidate and English manuscript
are complete; this does not assert publication acceptance.

Fixed question: [3-SAT to exact real Hadamard decomposition](question.md).
Campaign path chosen from the topic: `campaigns/hadamard-decomposition/`.
Budget: 40 rounds maximum; 13 started, 13 completed, 27 unstarted.
Current candidate: [algorithm](work/algorithm.py) and [general proof](work/proof.md).
The synchronized selectors and multiplicative cycle give a deterministic
3-SAT reduction with rank bounds (2,2K), with reverse witness recovery.
[Manuscript PDF](work/manuscript.pdf) and [Typst source](work/manuscript.typ).

Prepared checks pass six source cases/eight recovery calls. Independent checks
pass 29 distinct sources/109 recovery calls, including nine algebraic gauges.
See [preparation](work/preparation.md) and [verification](work/verification.md).
The [final native review](reviews/literal-rational/review.md) advances the candidate;
all three repair findings are closed. Correctness, novelty coverage and significance
remain subject to independent human assessment. Stop exploration at round 013:
a complete candidate has passed the campaign's review gate; no rounds are padded.

| Round | Hypothesis | Result |
|---|---|---|
| [001](rounds/001/round.md) | Rank-one zeros and identity boundary | Ordinary rank collapse; identity only tests pq |
| [002](rounds/002/round.md) | Identity forces a grid | Exact non-grid counterexample |
| [003](rounds/003/round.md) | Square-root-rank identity transfer | Exact 3-by-3 NO-to-YES counterexample |
| [004](rounds/004/round.md) | Product-basis graph encoding | Exact reformulation; packing converse missing |
| [005](rounds/005/round.md) | Transfer 2026 signing hardness | Equal-magnitude premise absent |
| [006](rounds/006/round.md) | High-width transfer | Universal column-splitting obstruction |
| [007](rounds/007/round.md) | Completion mask template | Fixed I3 minor gives NO-to-YES counterexample |
| [008](rounds/008/round.md) | Reciprocal selector | Continuous surviving family |
| [009](rounds/009/round.md) | Change selector constants | Nonzero reference column enlarges easy regime |
| [010](rounds/010/round.md) | Triangle/C4 graph-sum encoding | C4 YES; normalized triangle UNSAT; unrestricted oracle interrupted/unknown |
| [011](rounds/011/round.md) | Clique packing | Three-clique product-basis counterexample |
| [012](rounds/012/round.md) | Synchronized selectors | Two choices proved; 16 exact witness checks |
| [013](rounds/013/round.md) | Subset-product cycle and 3-SAT | Complete candidate; checks pass; review advances; manuscript complete |

New shared experience entries: 0; updated: 0; pending: six distinct proposals
(rank boundaries, identity fiber freedom, independent-vs-equal factors,
completion-mask leakage, synchronized selectors and common-primitive zero tests).
Claims and evidence remain in the linked rounds, with extraction details in
[round 013](rounds/013/round.md). Campaign-only writes prevent shared extraction.
Next action: independent human expert review, not another exploration round.
Time/token totals unavailable.
