from pathlib import Path
import sys,itertools,json
from fractions import Fraction
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
from check import target_witness_valid
import z3
pairs=[(0,1),(0,1),(0,2),(0,2),(1,2),(1,2)]
left=[(1,0),(0,1),(1,1)]
indices=[(item,e) for item in range(3) for e,pair in enumerate(pairs) if item in pair]
u=[list(left[item]) for item,e in indices]
x=[[int(j==e) for j in range(6)] for item,e in indices]
v=[[0]*12 for _ in range(2)];y=[[0]*12 for _ in range(6)]
for j,(item,e) in enumerate(indices):
 i0,i1=pairs[e];a,b=left[i0];c,d=left[i1];det=a*d-b*c
 column=[Fraction(d,det),Fraction(-c,det)] if item==i0 else [Fraction(-b,det),Fraction(a,det)]
 for r in range(2):v[r][j]=column[r]
 y[e][j]=1
edges=[(i,j) for i,j in itertools.combinations(range(12),2) if indices[i][0]==indices[j][0]]
m=[[int(i==j) for j in range(12)] for i in range(12)]
for i,j in edges:
 m.append([int(k in (i,j)) for k in range(12)])
 u.append(list(left[indices[i][0]]))
 x.append([x[i][r]+x[j][r] for r in range(6)])
w={k:[[z3.RealVal(str(z)).sexpr() for z in row] for row in a] for k,a in [('u1',u),('v1',v),('u2',x),('v2',y)]}
t={'matrix':m,'k1':2,'k2':6}
assert target_witness_valid(t,w)
assert not any(sum(s)==6 for mask in itertools.product((False,True),repeat=3) for s in [[4 for b in mask if b]])
Path(__file__).with_name('witness.json').write_text(json.dumps({'target':t,'witness':w},indent=2)+'\n')
print('PASS: three K4 components give a 30-by-12 (2,6) factorization, but items 4,4,4 cannot partition into bins 6,6.')
