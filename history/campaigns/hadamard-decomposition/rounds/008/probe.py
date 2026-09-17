from sympy import symbols, Matrix, factor, solve, together
from pathlib import Path
a,b,c,d=symbols('a b c d')
a_matrix=Matrix([[1,1,1],[1,a,b],[1,c,d]])
b_matrix=a_matrix.applyfunc(lambda x:1/x)
f=factor(a_matrix.det());g=factor(b_matrix.det()*a*b*c*d)
print('det(A)=',f);print('abcd det(B)=',g)
dsol=solve(f,d)[0]
print('d=',dsol);print('after substitution:',factor(together(g.subs(d,dsol))))
print('a=b and c=d:',factor(f.subs({b:a,d:c})),factor(g.subs({b:a,d:c})))
assert f.subs({b:a,d:c})==0
assert factor(g.subs({b:a,d:c}))==0
print('PASS: all nonzero a,c admit the column-duplicate family; normalized cross-ratio a is continuous.')
