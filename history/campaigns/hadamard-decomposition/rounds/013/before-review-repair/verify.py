"""Finite independent checks; the target NO oracle uses the product-basis theorem."""
import argparse
from fractions import Fraction as Q
import itertools
import json
import math
from pathlib import Path
import random
import subprocess
import sys
import z3

sys.set_int_max_str_digits(0)


def invoke(path, payload, extract=False):
    result=subprocess.run([sys.executable,str(path)]+(['--extract'] if extract else []), input=json.dumps(payload),text=True,capture_output=True)
    if result.returncode:raise RuntimeError(result.stderr)
    return json.loads(result.stdout)


def decode_target(t):
    assert set(t)=={'matrix','k1','k2'}
    a=t['matrix'];n=len(a[0]);k=n//4
    assert k>=3 and n==4*k and t['k1']==2 and t['k2']==2*k
    assert len(a)==k*k+9*k and all(len(row)==n for row in a)
    assert all(type(v) is int and v>=0 for row in a for v in row)
    for i in range(n):assert a[i]==[int(j==i) for j in range(n)]
    edges=[]
    for i in range(k):
        for j in range(i+1,k):edges.extend(((4*i,4*j),(4*i+1,4*j+1)))
        edges.extend((4*i+b,4*i+c) for b in (0,1) for c in (2,3))
    expected={tuple(int(j in edge) for j in range(n)) for edge in edges}
    observed=a[n:-2*k]
    assert len(observed)==len(expected) and set(map(tuple,observed))==expected
    for i,row in enumerate(a[-2*k:-k]):assert row==[int(j//4==i) for j in range(n)]
    values=[a[-k+i][4*i+1] for i in range(k)];T=a[-1][2]
    assert T>0 and all(r>0 for r in values)
    for i,row in enumerate(a[-k:]):
        support={4*i+j:v for j,v in enumerate((1,values[i],1,values[i]))}
        nxt=(i+1)%k;coeff=(1,T*T,T,T) if nxt==0 else (1,1,1,1)
        support.update({4*nxt+j:v for j,v in enumerate(coeff)})
        assert row==[support.get(j,0) for j in range(n)]
    return values,T


def subsets(values):
    result=[(1,())]
    for x in values:result=[(p,b+(False,)) for p,b in result]+[(p*x,b+(True,)) for p,b in result]
    return result


def product_solutions(values,T):
    half=len(values)//2;right={}
    for p,b in subsets(values[half:]):right.setdefault(p,[]).append(b)
    found=[]
    for p,b in subsets(values[:half]):
        if T%p==0:
            for tail in right.get(T//p,[]):
                found.append(b+tail)
                if len(found)==2:return found
    return found


def mul(a,b):
    out=[[Q(0) for _ in b[0]] for _ in a]
    for i,row in enumerate(a):
        for j,x in enumerate(row):
            if x:
                for c,y in enumerate(b[j]):
                    if y:out[i][c]+=x*y
    return out


def factors(t,choice):
    rs,T=decode_target(t);k=len(rs);q=2*k;coords=[];h=Q(1)
    for i,take in enumerate(choice):
        coords.extend([(0,2*i,Q(1)),(1,2*i+1,Q(1))])
        coords.extend([(0,2*i+1,1/h),(1,2*i,h)] if take else [(1,2*i,h),(0,2*i+1,1/h)])
        if take:h*=rs[i]
    assert h==T
    u=[];w=[]
    for row in t['matrix']:
        tensor=[[Q(0)]*q for _ in range(2)]
        for coefficient,(left,right,scale) in zip(row,coords):tensor[left][right]+=coefficient*scale
        pivot=next((i,j) for i in range(2) for j in range(q) if tensor[i][j])
        i,j=pivot;right=tensor[i];left=[tensor[a][j]/right[j] for a in range(2)]
        assert all(left[a]*right[b]==tensor[a][b] for a in range(2) for b in range(q))
        u.append(left);w.append(right)
    v=[[Q(int(a==left)) for left,right,scale in coords] for a in range(2)]
    z=[[Q(int(b==right))/scale for left,right,scale in coords] for b in range(q)]
    return [u,v,w,z]


def validate(t,fs):
    u,v,w,z=fs;m=len(t['matrix']);n=len(t['matrix'][0])
    for a,r,c in zip(fs,(m,2,m,t['k2']),(2,n,t['k2'],n)):
        assert len(a)==r and all(len(row)==c for row in a)
    a=mul(u,v);b=mul(w,z)
    assert all(a[i][j]*b[i][j]==t['matrix'][i][j] for i in range(m) for j in range(n))


def encode(fs):
    def scalar(v):
        v=Q(v)
        return str(v.numerator) if v.denominator==1 else f'(/ {v.numerator} {v.denominator})'
    return {key:[[scalar(v) for v in row] for row in a] for key,a in zip(('u1','v1','u2','v2'),fs)}


def gauge(fs):
    u,v,w,z=fs
    u=mul(u,[[1,1],[1,2]]);v=mul([[2,-1],[-1,1]],v)
    # A right-coordinate shear mixes two distinct selector blocks.
    w=[row[:] for row in w];z=[row[:] for row in z]
    for row in w:row[2]+=row[0]
    z[0]=[a-b for a,b in zip(z[0],z[2])]
    for i in range(len(u)):
        scale=Q(-2 if i%2 else 3)
        u[i]=[x*scale for x in u[i]];w[i]=[x/scale for x in w[i]]
    for j in range(len(v[0])):
        scale=Q(-3 if j%2 else 2)
        for row in v:row[j]*=scale
        for row in z:row[j]/=scale
    return [u,v,w,z]


def irrational_witness(t,fs):
    matrices=[[[z3.RealVal(str(x)) for x in row] for row in a] for a in fs]
    u,v,w,z=matrices;s=z3.simplify(z3.Sqrt(2))
    u=[[a,a*s+b] for a,b in u]
    v=[[a-s*b for a,b in zip(v[0],v[1])],v[1]]
    # The shear and its inverse are checked exactly; unchanged rational products
    # were checked entry by entry before this transformation.
    for old,new in zip(matrices[0],u):
        assert z3.is_true(z3.simplify(new[0]==old[0]))
        assert z3.is_true(z3.simplify(new[1]-s*new[0]==old[1]))
    for j in range(len(v[0])):assert z3.is_true(z3.simplify(v[0][j]+s*v[1][j]==matrices[1][0][j]))
    def scalar(x):
        x=z3.simplify(x)
        if z3.is_rational_value(x):return x.sexpr()
        return {'polynomial':[a.as_long() for a in x.poly()],'root':x.index()}
    return {key:[[scalar(x) for x in row] for row in a] for key,a in zip(('u1','v1','u2','v2'),(u,v,w,z))}


def source_yes(s,a):
    return len(a)==s['n'] and all(type(x) is bool for x in a) and all(any(a[abs(l)-1]==(l>0) for l in c) for c in s['clauses'])


def main(path):
    sources=[{'n':0,'clauses':[]}]
    for signs in itertools.product((-1,1),repeat=3):sources.append({'n':1,'clauses':[list(signs)]})
    sources.extend([{'n':1,'clauses':[[1,1,1],[-1,-1,-1]]},{'n':3,'clauses':[list(c) for c in itertools.product((1,-1),(2,-2),(3,-3))]}])
    rng=random.Random(13013)
    for n in (2,3,4):
        for m in (n,n+2):
            for _ in range(3):
                occurrences=list(range(1,n+1))+[rng.randint(1,n) for _ in range(3*m-n)]
                rng.shuffle(occurrences);lits=[x*rng.choice((-1,1)) for x in occurrences]
                sources.append({'n':n,'clauses':[lits[i:i+3] for i in range(0,3*m,3)]})
    yes=no=calls=irrational=0
    for index,s in enumerate(sources):
        t=invoke(path,s);rs,T=decode_target(t)
        expected=any(source_yes(s,list(a)) for a in itertools.product((False,True),repeat=s['n']))
        selections=product_solutions(rs,T)
        assert bool(selections)==expected,{'source':s,'target':t,'source_yes':expected,'target_yes':bool(selections)}
        yes+=expected;no+=not expected
        for selection in selections:
            fs=factors(t,selection)
            for variant in (fs,gauge(fs)):
                validate(t,variant)
                recovered=invoke(path,{'source':s,'target_solution':encode(variant)},True)
                assert source_yes(s,recovered['assignment']),{'source':s,'target_solution':encode(variant),'recovered':recovered}
                calls+=1
            if index in (0,1,11):
                witness=irrational_witness(t,fs)
                recovered=invoke(path,{'source':s,'target_solution':witness},True)
                assert source_yes(s,recovered['assignment'])
                calls+=1;irrational+=1
        print('case',index,'n',s['n'],'clauses',len(s['clauses']),'target',len(t['matrix']),len(t['matrix'][0]),'YES' if expected else 'NO',flush=True)
    for bad in ({},None,{'n':2,'clauses':[[1,1,1]]},{'n':10**5000,'clauses':[]}):
        assert invoke(path,bad)=={'invalid':True}
    print('PASS',len(sources),'sources;',yes,'YES;',no,'NO;',calls,'recovery calls;',irrational,'irrational gauges; 4 malformed sources; seed 13013')
    print('Target decision uses independent exact subset enumeration after structural validation; NO correctness also depends on the general product-basis lemma.')


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--candidate',required=True,type=Path)
    main(p.parse_args().candidate)
