import json
from pathlib import Path
import subprocess
import sys
import sympy as s
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
from algorithm import polynomial,root_count
x=s.Symbol('x');tests=0
for cs in ([0,1],[-2,0,1],[-2,0,0,1],[6,-2,-3,1],[-6,2,3,-1],[-4,0,4,0,-1],[0,0,0,1],[-1,0,0,0,0,1]):
    p=polynomial(cs)
    for a,b in ((-4,-3),(-2,-1),(-1,1),(1,2),(2,4)):
        if p.eval(a)==0 or p.eval(b)==0:continue
        assert root_count(p,s.Rational(a),s.Rational(b))==p.count_roots(a,b),(cs,a,b)
        tests+=1
print('PASS',tests,'root-count comparisons against independent SymPy Sturm routine; reducible, repeated, negative-leading and degree-five cases')
