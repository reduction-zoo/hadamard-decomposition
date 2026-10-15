from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
from check import target_witness_valid
m=[[1,1,1],[1,2,3],[1,3,2]]
w={'u1':[['1','1'],['1','2'],['1','3']],'v1':[['1','0','1'],['0','1','0']],'u2':[['1','1'],['1','3'],['1','2']],'v2':[['1','1','0'],['0','0','1']]}
assert target_witness_valid({'matrix':m,'k1':2,'k2':2},w)
print('PASS: full-rank 3-by-3 matrix with a nonzero reference column has widths (2,2).')
