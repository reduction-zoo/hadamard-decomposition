import itertools
import math
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
import check
import product_basis_oracle as oracle


def matrix(rs,T):
    k=len(rs);n=4*k;rows=[[int(i==j) for j in range(n)] for i in range(n)]
    edges=[(4*i+s,4*j+s) for s in (0,1) for i in range(k) for j in range(i+1,k)]
    edges += [(4*i+a,4*i+b) for i in range(k) for a in (2,3) for b in (0,1)]
    rows += [[int(j in e) for j in range(n)] for e in edges]
    rows += [[int(j//4==i) for j in range(n)] for i in range(k)]
    for i,r in enumerate(rs):
        row=[0]*n;row[4*i:4*i+4]=[1,r,1,r]
        nxt=(i+1)%k;row[4*nxt:4*nxt+4]=[1,T*T,T,T] if nxt==0 else [1]*4
        rows.append(row)
    return {'matrix':rows,'k1':2,'k2':2*k}

count=yes=0
for rs in ((1,1,1),(2,3,5),(2,2,3),(4,6,9)):
    for T in (1,2,3,4,5,6,12,30):
        expected=any(math.prod(r for r,b in zip(rs,bits) if b)==T for bits in itertools.product((False,True),repeat=3))
        t=matrix(rs,T);check.target_valid(t);w=oracle.solve(t)
        assert (w is not None)==expected
        if w is not None:assert check.target_witness_valid(t,w)
        count+=1;yes+=expected
bad=matrix((2,3,5),6);bad['matrix'][-1][1]+=1
try:oracle.solve(bad)
except AssertionError:pass
else:raise AssertionError('Corrupt wrap coefficients accepted')
print('PASS',count,'standalone subset-product targets;',yes,'YES;',count-yes,'NO; all YES witnesses entrywise checked; corrupted cycle rejected')
print('Finite oracle cross-check, not a proof of unrestricted real-factor NO outcomes.')
