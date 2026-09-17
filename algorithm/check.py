import argparse
import itertools
import json
import re
from pathlib import Path
import subprocess
import sys
import tempfile
from fractions import Fraction

import z3
import sympy as sp

sys.set_int_max_str_digits(0)


def source_shape(s):
    assert type(s['n']) is int and s['n'] >= 0
    assert s['n'] <= 3*len(s['clauses'])
    assert all(len(c) == 3 and all(type(l) is int and 1 <= abs(l) <= s['n'] for l in c) for c in s['clauses'])
    assert {abs(l) for c in s['clauses'] for l in c} == set(range(1,s['n']+1))


def source_valid(s, witness):
    source_shape(s)
    a = witness['assignment']
    assert len(a) == s['n'] and all(type(x) is bool for x in a)
    return all(any(a[abs(l)-1] == (l > 0) for l in c) for c in s['clauses'])


def source_solve(s):
    source_shape(s)
    source_valid(s, {'assignment': [False]*s['n']})
    xs = [z3.Bool(f'x{i}') for i in range(s['n'])]
    solver = z3.Solver()
    solver.add([z3.Or([xs[abs(l)-1] if l > 0 else z3.Not(xs[abs(l)-1]) for l in c]) for c in s['clauses']])
    result = solver.check()
    assert result in (z3.sat, z3.unsat), result
    if result == z3.unsat:
        return None
    witness = {'assignment': [z3.is_true(solver.model().eval(x, model_completion=True)) for x in xs]}
    assert source_valid(s, witness)
    return witness


def target_valid(t):
    assert set(t) == {'matrix', 'k1', 'k2'}
    a = t['matrix']; m = len(a); assert m > 0
    n = len(a[0]); assert n > 0 and all(len(row) == n for row in a)
    for row in a:
        for x in row:
            assert type(x) in (str, int)
            Fraction(x)
    assert all(type(t[k]) is int and 1 <= t[k] <= min(m,n) for k in ('k1','k2'))
    return m,n


def exact(text):
    if isinstance(text,dict):
        assert set(text)=={'polynomial','root'}
        cs=text['polynomial'];assert len(cs)>=2 and all(type(c) is int for c in cs) and cs[-1]!=0
        assert type(text['root']) is int and 1<=text['root']<len(cs)
        terms=['(* '+str(c)+' (^ x '+str(i)+'))' for i,c in enumerate(cs) if c]
        text='(root-obj (+ '+' '.join(terms)+') '+str(text['root'])+')'
    else:
        assert isinstance(text,str) and re.fullmatch(r'[0-9./()\s-]+',text)
    x = z3.Real('witness_value')
    parsed = z3.parse_smt2_string('(assert (= witness_value '+text+'))', decls={'witness_value': x})
    assert len(parsed) == 1 and z3.is_eq(parsed[0]) and parsed[0].arg(0).eq(x)
    v = z3.simplify(parsed[0].arg(1))
    assert z3.is_rational_value(v) or z3.is_algebraic_value(v)
    return v


def encode(v):
    v=z3.simplify(v)
    if z3.is_rational_value(v):return v.sexpr()
    assert z3.is_algebraic_value(v)
    return {'polynomial':[c.as_long() for c in v.poly()],'root':v.index()}


def target_witness_valid(t,w):
    m,n = target_valid(t)
    shapes = [(m,t['k1']), (t['k1'],n), (m,t['k2']), (t['k2'],n)]
    assert set(w) == {'u1','v1','u2','v2'}
    matrices=[]
    for key,(rows,cols) in zip(('u1','v1','u2','v2'),shapes):
        a=w[key]; assert len(a)==rows and all(len(row)==cols for row in a)
        matrices.append([[exact(x) for x in row] for row in a])
    u,v,x,y=matrices
    for i in range(m):
        for j in range(n):
            value=sum(u[i][r]*v[r][j] for r in range(t['k1']))*sum(x[i][r]*y[r][j] for r in range(t['k2']))
            if not z3.is_true(z3.simplify(value == z3.RealVal(str(t['matrix'][i][j])))):
                return False
    return True


def target_solve(t):
    m,n=target_valid(t)
    shapes=[(m,t['k1']),(t['k1'],n),(m,t['k2']),(t['k2'],n)]
    variables={key:[[z3.Real(f'{key}_{i}_{j}') for j in range(cols)] for i in range(rows)] for key,(rows,cols) in zip(('u1','v1','u2','v2'),shapes)}
    u,v,x,y=[variables[key] for key in ('u1','v1','u2','v2')]
    solver=z3.SolverFor('QF_NRA')
    solver.add([sum(u[i][r]*v[r][j] for r in range(t['k1']))*sum(x[i][r]*y[r][j] for r in range(t['k2'])) == z3.RealVal(str(t['matrix'][i][j])) for i in range(m) for j in range(n)])
    result=solver.check(); assert result in (z3.sat,z3.unsat), result
    if result==z3.unsat:
        return None
    model=solver.model()
    w={key:[[encode(model.eval(x,model_completion=True)) for x in row] for row in a] for key,a in variables.items()}
    assert target_witness_valid(t,w)
    return w


def common_witness(w):
    values={};irrationals=set();x=sp.Symbol('x')
    for key,matrix in w.items():
        values[key]=[]
        for row in matrix:
            converted=[]
            for v in row:
                v=exact(v)
                if z3.is_rational_value(v):a=sp.Rational(v.numerator_as_long(),v.denominator_as_long())
                else:
                    p=sp.Poly.from_list([c.as_long() for c in reversed(v.poly())],x)
                    a=p.real_roots()[v.index()-1];irrationals.add(a)
                converted.append(a)
            values[key].append(converted)
    if not irrationals:
        return {'field':{'polynomial':[0,1],'interval':['-1','1']},**{key:[[[str(v)] for v in row] for row in matrix] for key,matrix in values.items()}}
    primitive=sp.to_number_field(sorted(irrationals,key=str));p=primitive.minpoly
    interval=next((a,b) for (a,b),multiplicity in p.intervals() if bool(a<primitive.as_expr()) and bool(primitive.as_expr()<b))
    result={'field':{'polynomial':[int(c) for c in reversed(p.all_coeffs())],'interval':list(map(str,interval))}}
    for key,matrix in values.items():
        result[key]=[[list(map(str,reversed(sp.to_number_field(v,primitive).coeffs()))) for v in row] for row in matrix]
    return result


def run_case(path,s,oracle=target_solve):
    t=json.loads(subprocess.run([sys.executable,str(path)],input=json.dumps(s),text=True,capture_output=True,check=True).stdout)
    target_valid(t)
    expected=source_solve(s) is not None;w=oracle(t)
    assert (w is not None)==expected, {'source':s,'target':t,'expected':expected}
    calls=0
    if w is not None:
        scaled=json.loads(json.dumps(w))
        for row in scaled['u1']:
            for j in range(len(row)):row[j]=encode(2*exact(row[j]))
        for row in scaled['v1']:
            for j in range(len(row)):row[j]=encode(exact(row[j])/2)
        for solution in (w,scaled):
            assert target_witness_valid(t,solution)
            recovered=json.loads(subprocess.run([sys.executable,str(path),'--extract'],input=json.dumps({'source':s,'target_solution':common_witness(solution)}),text=True,capture_output=True,check=True).stdout)
            assert source_valid(s,recovered), {'source':s,'target_solution':common_witness(solution),'recovered':recovered}
            calls+=1
    return calls


def self_test(cases):
    for case in cases:
        s=case['source']; brute=any(source_valid(s,{'assignment':list(a)}) for a in itertools.product((False,True),repeat=s['n']))
        assert brute == case['yes'] == (source_solve(s) is not None)
    targets=[({'matrix':[[0]],'k1':1,'k2':1},True),({'matrix':[[1,2],[2,4]],'k1':1,'k2':1},True),({'matrix':[[1,0],[0,1]],'k1':1,'k2':1},False),({'matrix':[[1,0],[0,1]],'k1':1,'k2':2},True)]
    for t,yes in targets:assert (target_solve(t) is not None)==yes
    irrational={'u1':[[{'polynomial':[-2,0,1],'root':2}]],'v1':[['1']],'u2':[[{'polynomial':[-2,0,1],'root':2}]],'v2':[['1']]}
    assert target_witness_valid({'matrix':[[2]],'k1':1,'k2':1},irrational)
    assert not target_witness_valid({'matrix':[[3]],'k1':1,'k2':1},irrational)
    with tempfile.TemporaryDirectory() as d:
        p=Path(d)/'fixture.py'
        for name,payload,s in [('malformed',{'matrix':[[1]],'k1':0,'k2':1},cases[0]['source']),('decision',targets[0][0],cases[-1]['source'])]:
            p.write_text('import json\nprint(json.dumps('+repr(payload)+'))\n')
            try:run_case(p,s)
            except AssertionError:print('rejected',name)
            else:raise AssertionError('bad fixture accepted')
        p.write_text('import sys,json\nprint(json.dumps({"assignment":[False]} if "--extract" in sys.argv else {"matrix":[[1]],"k1":1,"k2":1}))\n')
        try:run_case(p,{'n':1,'clauses':[[1,1,1]]})
        except AssertionError:print('rejected recovery')
        else:raise AssertionError('bad recovery accepted')
    encoded=common_witness(irrational)
    assert encoded['field']['polynomial']==[-2,0,1] and encoded['u1'][0][0]==['0','1']
    print('PASS',len(cases),'source cases; 4 target cases; irrational witness accepted and invalid product rejected; 3 faulty subprocess fixtures rejected; Z3',z3.get_version_string())


if __name__=='__main__':
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group(required=True);g.add_argument('--self-test',action='store_true');g.add_argument('--candidate',type=Path);p.add_argument('--oracle',choices=['quartic','product-basis'],default='quartic');args=p.parse_args()
    cases=json.loads(Path(__file__).with_name('cases.json').read_text())
    if args.self_test:self_test(cases)
    else:
        if args.oracle=='product-basis':
            from product_basis_oracle import solve
            oracle=solve
        else:oracle=target_solve
        calls=sum(run_case(args.candidate,case['source'],oracle) for case in cases)
        print('PASS',len(cases),'injected instances;',calls,'recovery calls')
