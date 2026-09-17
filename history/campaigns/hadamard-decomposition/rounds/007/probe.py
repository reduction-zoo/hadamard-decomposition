from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
from check import target_witness_valid
m=[[int(i==j and i<3) for j in range(4)] for i in range(4)]
u=[['1','0'],['1','0'],['0','1'],['0','0']]
v=[['1','1','0','0'],['0','0','1','0']]
x=[['1','0'],['0','1'],['1','0'],['0','0']]
y=[['1','0','1','0'],['0','1','0','0']]
assert target_witness_valid({'matrix':m,'k1':2,'k2':2},dict(u1=u,v1=v,u2=x,v2=y))
print('PASS: diag(1,1,1,0) has a (2,2) decomposition; any completion changing only (4,4) retains the fixed I3 minor and rank >= 3.')
