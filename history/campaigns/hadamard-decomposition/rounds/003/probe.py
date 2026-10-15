from itertools import product
from pathlib import Path
import sys
import z3
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
from check import target_witness_valid
m=[[1,1,1],[1,2,3],[1,3,5]]
roots={}
for n in (1,2,3,5):
 x=z3.Real('x');s=z3.SolverFor('QF_NRA');s.add(x*x==n,x>0);assert s.check()==z3.sat;roots[n]=s.model()[x]
for signs in product((-1,1),repeat=4):
 a=[[roots[x] for x in row] for row in m]
 for (i,j),sign in zip(((1,1),(1,2),(2,1),(2,2)),signs):a[i][j]*=sign
 det=sum(a[0][j]*(a[1][(j+1)%3]*a[2][(j+2)%3]-a[1][(j+2)%3]*a[2][(j+1)%3]) for j in range(3))
 assert z3.is_false(z3.simplify(det==0)),signs
 print(signs, z3.simplify(det).sexpr())
w={'u1':[['1','0']]*3,'v1':[['1']*3,['0']*3],'u2':[['1','0'],['1','1'],['1','2']],'v2':[['1','1','1'],['0','1','2']]}
assert target_witness_valid({'matrix':m,'k1':2,'k2':2},w)
print('PASS: 16 normalized signed square roots have rank 3; independent factors have ranks 1 and 2.')
