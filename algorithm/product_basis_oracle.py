from fractions import Fraction
import math
import z3


def parameters(t):
    a=t['matrix'];n=len(a[0]);assert n%4==0
    k=n//4;assert k>=3 and t['k1']==2 and t['k2']==2*k
    assert len(a)==k*k+9*k
    a=[[Fraction(x) for x in row] for row in a]
    assert all(a[i]==[int(i==j) for j in range(n)] for i in range(n))
    pair_rows=a[n:n+k*(k-1)+4*k]
    expected={tuple(sorted((4*i+side,4*j+side))) for side in (0,1) for i in range(k) for j in range(i+1,k)}
    expected|={tuple(sorted((4*i+b,4*i+c))) for i in range(k) for b in (0,1) for c in (2,3)}
    observed=[]
    for row in pair_rows:
        support=tuple(i for i,x in enumerate(row) if x)
        assert len(support)==2 and all(row[i]==1 for i in support)
        observed.append(support)
    assert len(observed)==len(expected) and set(observed)==expected
    for i,row in enumerate(a[-2*k:-k]):
        assert row==[int(j//4==i) for j in range(n)]
    items=[];target=a[-1][2]
    assert target.denominator==1 and target>0
    for i,row in enumerate(a[-k:]):
        r=row[4*i+1];assert r.denominator==1 and r>0
        expected=[Fraction(0)]*n
        expected[4*i:4*i+4]=[1,r,1,r]
        j=(i+1)%k
        expected[4*j:4*j+4]=[1,target*target,target,target] if i==k-1 else [1,1,1,1]
        assert row==expected
        items.append(int(r))
    return items,int(target)


def witness(t,selected):
    items,target=parameters(t);k=len(items);n=4*k
    assert len(selected)==k and math.prod(r for r,b in zip(items,selected) if b)==target
    cells=[];scales=[];h=Fraction(1)
    for i,(r,chosen) in enumerate(zip(items,selected)):
        ti=1/h if chosen else h
        corners=[(0,2*i+1),(1,2*i)] if chosen else [(1,2*i),(0,2*i+1)]
        cells.extend([(0,2*i),(1,2*i+1),*corners]);scales.extend([Fraction(1),Fraction(1),ti,1/ti])
        if chosen:h*=r
    us=[];xs=[]
    for row in t['matrix']:
        block=[[Fraction(0) for _ in range(2*k)] for _ in range(2)]
        for coefficient,(left,right),scale in zip(row,cells,scales):block[left][right]+=Fraction(coefficient)*scale
        j=next(j for j in range(2*k) if block[0][j] or block[1][j])
        left=[block[0][j],block[1][j]];i=0 if left[0] else 1
        right=[v/left[i] for v in block[i]]
        assert all(left[a]*right[b]==block[a][b] for a in range(2) for b in range(2*k))
        us.append(left);xs.append(right)
    vs=[[Fraction(int(a==left),scale) for (left,right),scale in zip(cells,scales)] for a in range(2)]
    ys=[[int(b==right) for left,right in cells] for b in range(2*k)]
    return {key:[[z3.RealVal(str(v)).sexpr() for v in row] for row in matrix] for key,matrix in [('u1',us),('v1',vs),('u2',xs),('v2',ys)]}


def solve(t):
    items,target=parameters(t);k=len(items)
    chosen=[z3.Bool(f'choose_{i}') for i in range(k)]
    h=[z3.Real(f'prefix_{i}') for i in range(k+1)]
    s=z3.SolverFor('QF_LRA');s.add(h[0]==1,h[-1]==target)
    s.add([h[i+1]==z3.If(chosen[i],r*h[i],h[i]) for i,r in enumerate(items)])
    result=s.check();assert result in (z3.sat,z3.unsat),result
    if result==z3.unsat:return None
    selection=[z3.is_true(s.model().eval(c,model_completion=True)) for c in chosen]
    return witness(t,selection)
