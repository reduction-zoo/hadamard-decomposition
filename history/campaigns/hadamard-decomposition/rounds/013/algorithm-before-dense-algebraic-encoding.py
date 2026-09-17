import json
import math
import sys

import z3


def primes(count):
    result=[]
    candidate=2
    while len(result)<count:
        if all(candidate%p for p in result if p<=math.isqrt(candidate)):
            result.append(candidate)
        candidate+=1
    return result


def subset_product(source):
    n=source['n'];clauses=source['clauses'];m=len(clauses)
    ps=primes(n+m);items=[]
    for v in range(1,n+1):
        for truth in (True,False):
            number=ps[v-1]
            for j,clause in enumerate(clauses):
                number*=ps[n+j]**sum(abs(l)==v and (l>0)==truth for l in clause)
            items.append(number)
    for j in range(m):items.extend((ps[n+j],ps[n+j]**2))
    target=math.prod(ps[:n])*math.prod(p**4 for p in ps[n:])
    items.extend([1]*max(0,3-len(items)))
    return items,target


def construct(source):
    items,target=subset_product(source);k=len(items);size=4*k
    rows=[[int(i==j) for j in range(size)] for i in range(size)]
    for side in (0,1):
        for i in range(k):
            for j in range(i+1,k):
                row=[0]*size;row[4*i+side]=row[4*j+side]=1;rows.append(row)
    for i in range(k):
        for x in (2,3):
            for anchor in (0,1):
                row=[0]*size;row[4*i+x]=row[4*i+anchor]=1;rows.append(row)
    for i in range(k):
        row=[0]*size;row[4*i:4*i+4]=[1]*4;rows.append(row)
    for i,r in enumerate(items):
        row=[0]*size;row[4*i:4*i+4]=[1,r,1,r]
        j=(i+1)%k;row[4*j:4*j+4]=[1,target*target,target,target] if i==k-1 else [1]*4
        rows.append(row)
    return {'matrix':rows,'k1':2,'k2':2*k}


def constant(text):
    x=z3.Real('witness_value')
    parsed=z3.parse_smt2_string('(assert (= witness_value '+text+'))',decls={'witness_value':x})
    if len(parsed)!=1 or not z3.is_eq(parsed[0]) or not parsed[0].arg(0).eq(x):
        raise ValueError('Expected one exact algebraic scalar')
    value=z3.simplify(parsed[0].arg(1))
    if not (z3.is_rational_value(value) or z3.is_algebraic_value(value)):
        raise ValueError('Expected an exact real algebraic constant')
    return value


def extract(source,witness):
    u=witness['u1'];a,b=map(constant,u[0]);selected=[]
    for i in range(2*source['n']):
        c,d=map(constant,u[4*i+2]);selected.append(z3.is_true(z3.simplify(a*d-b*c==0)))
    assignment=[]
    for i in range(source['n']):
        if selected[2*i]==selected[2*i+1]:raise ValueError('Invalid assignment selector pair')
        assignment.append(selected[2*i])
    if not all(any(assignment[abs(l)-1]==(l>0) for l in c) for c in source['clauses']):
        raise ValueError('Recovered assignment does not satisfy the source')
    return {'assignment':assignment}


def legal(source):
    if not isinstance(source,dict) or set(source)!={'n','clauses'}:return False
    n=source['n'];clauses=source['clauses']
    if type(n) is not int or n<0 or not isinstance(clauses,list) or n>3*len(clauses):return False
    if not all(isinstance(c,list) and len(c)==3 and all(type(l) is int and 1<=abs(l)<=n for l in c) for c in clauses):return False
    return {abs(l) for c in clauses for l in c}==set(range(1,n+1))


if __name__=='__main__':
    try:data=json.load(sys.stdin)
    except json.JSONDecodeError:
        print(json.dumps({'invalid':True}));sys.exit(0)
    if '--extract' in sys.argv:
        if not legal(data['source']):raise ValueError('Invalid source encoding')
        output=extract(data['source'],data['target_solution'])
    else:output=construct(data) if legal(data) else {'invalid':True}
    print(json.dumps(output))
