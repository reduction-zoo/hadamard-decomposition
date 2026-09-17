from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
from check import target_witness_valid
m=[[1,2,3,4],[0,1,0,5],[2,0,1,0],[0,3,0,1]]
u1=[[str(row[0]),str(row[1]),'1'] for row in m]
v1=[['1','0','0','0'],['0','1','0','0'],['0','0','1','1']]
u2=[['1',str(row[2]),str(row[3])] for row in m]
v2=[['1','1','0','0'],['0','0','1','0'],['0','0','0','1']]
assert target_witness_valid({'matrix':m,'k1':3,'k2':3},dict(u1=u1,v1=v1,u2=u2,v2=v2))
print('PASS: arbitrary 4-by-4 example split into two rank-at-most-3 factors.')
