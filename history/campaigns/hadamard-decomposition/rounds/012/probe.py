from pathlib import Path
from itertools import combinations,product
import sys,json
import z3
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
from check import target_witness_valid,exact
n=3
edges=list(combinations([4*i for i in range(n)],2))+list(combinations([4*i+1 for i in range(n)],2))+[(4*i+j,4*i+k) for i in range(n) for j in (2,3) for k in (0,1)]
for bits in product((0,1),repeat=n):
 cells=[]
 for i,bit in enumerate(bits):
  corners=[(0,2*i+1),(1,2*i)]
  cells += [(0,2*i),(1,2*i+1),corners[bit],corners[1-bit]]
 u=[[int(r==a) for r in range(2)] for a,b in cells]
 x=[[int(r==b) for r in range(2*n)] for a,b in cells]
 v=[[int(r==a) for a,b in cells] for r in range(2)]
 y=[[int(r==b) for a,b in cells] for r in range(2*n)]
 m=[[int(i==j) for j in range(4*n)] for i in range(4*n)]
 for i,j in edges:
  m.append([int(k in (i,j)) for k in range(4*n)])
  if cells[i][0]==cells[j][0]:u.append(u[i]);x.append([a+b for a,b in zip(x[i],x[j])])
  else:
   assert cells[i][1]==cells[j][1]
   x.append(x[i]);u.append([a+b for a,b in zip(u[i],u[j])])
 w={key:[[str(c) for c in row] for row in a] for key,a in [('u1',u),('v1',v),('u2',x),('v2',y)]}
 t={'matrix':m,'k1':2,'k2':2*n}
 for changed in (False,True):
  if changed:
   for i,row in enumerate(w['u1']):
    scale=2 if i%2 else -3
    w['u1'][i]=[z3.simplify(exact(c)*scale).sexpr() for c in row]
    w['u2'][i]=[z3.simplify(exact(c)/scale).sexpr() for c in w['u2'][i]]
  assert target_witness_valid(t,w)
  decoded=[]
  for i in range(n):
   a,b=[exact(v) for v in w['u1'][4*i]];c,d=[exact(v) for v in w['u1'][4*i+2]]
   decoded.append(0 if z3.is_true(z3.simplify(a*d-b*c==0)) else 1)
  assert tuple(decoded)==bits
 print('PASS',bits,'canonical and gauge-rescaled witnesses; selector bits recovered')
print('16 exact witness validations; 16 local selector decodings; no SAT clause gadget.')
