from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
from check import target_witness_valid
u1=[[1,0],[1,0],[0,1],[0,1]]
v1=[[1,1,0,0],[0,0,1,1]]
u2=[[1,0],[0,1],[1,1],[1,-1]]
v2=[[1,0,'1/2','1/2'],[0,1,'1/2','-1/2']]
def smt(x):
 from z3 import RealVal
 return RealVal(str(x)).sexpr()
w={k:[[smt(x) for x in row] for row in a] for k,a in [('u1',u1),('v1',v1),('u2',u2),('v2',v2)]}
t={'matrix':[[int(i==j) for j in range(4)] for i in range(4)],'k1':2,'k2':2}
assert target_witness_valid(t,w)
print('PASS: I4 factorization, widths 2,2; right row directions (1,0),(0,1),(1,1),(1,-1).')
import json
Path(__file__).with_name('witness.json').write_text(json.dumps({'target':t,'witness':w},indent=2)+'\n')
