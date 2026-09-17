from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
from check import target_solve,target_witness_valid
edges=[(0,1),(1,3),(3,2),(2,0)]
m=[[int(i==j) for j in range(4)] for i in range(4)]+[[int(j in e) for j in range(4)] for e in edges]
u=[['1','0'],['1','0'],['0','1'],['0','1'],['1','0'],['1','1'],['0','1'],['1','1']]
x=[['1','0'],['0','1'],['1','0'],['0','1'],['1','1'],['0','1'],['1','1'],['1','0']]
v=[['1','1','0','0'],['0','0','1','1']];y=[['1','0','1','0'],['0','1','0','1']]
w=dict(u1=u,v1=v,u2=x,v2=y)
assert target_witness_valid({'matrix':m,'k1':2,'k2':2},w)
print('PASS C4 graph-sum explicit witness',flush=True)
triangle=[[int(i==j) for j in range(4)] for i in range(4)]+[[int(j in e) for j in range(4)] for e in [(0,1),(1,2),(2,0)]]
t={'matrix':triangle,'k1':2,'k2':2}
Path(__file__).with_name('triangle.json').write_text(json.dumps(t,indent=2)+'\n')
print('starting unrestricted triangle target oracle',flush=True)
assert target_solve(t) is None
print('PASS triangle target UNSAT',flush=True)
