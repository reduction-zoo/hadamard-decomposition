import z3
b,c,f,g=z3.Reals('b c f g')
s=z3.SolverFor('QF_NRA')
s.add(b*c==0,f*g==0,(b+f)*(c+g)==0,b*g-c*f!=0)
result=s.check()
print('Normalized triangle constraints:',s.sexpr())
print('Result:',result)
assert result==z3.unsat
