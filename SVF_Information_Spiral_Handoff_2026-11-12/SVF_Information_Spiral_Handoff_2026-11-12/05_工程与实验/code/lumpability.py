"""4-bit parity exact lumpability; deterministic macro-non-closure counterexample."""
from itertools import product

def parity(bits):return sum(bits)%2

def flip_probability(x,y,p=0.1):
    flips=sum(a!=b for a,b in zip(x,y))
    return (p**flips)*((1-p)**(len(x)-flips))

def run():
    states=list(product((0,1), repeat=4))
    block={v:parity(v) for v in states}
    matrix={}
    for x in states:
        for target in (0,1):
            total=sum(flip_probability(x,y) for y in states if block[y]==target)
            matrix[(x,target)]=total
    for x in states:
        for y in states:
            if block[x]==block[y]:
                for target in (0,1):
                    assert abs(matrix[(x,target)]-matrix[(y,target)])<1e-12
    q=(1-(1-2*0.1)**4)/2
    assert abs(q-0.2952)<1e-12
    assert abs(matrix[((0,0,0,0),1)]-q)<1e-12
    def update(s):return tuple(s[(i-1)%4]^s[(i+1)%4] for i in range(4))
    first=(1,1,0,0);second=(1,0,1,0)
    assert sum(first)==sum(second)==2
    assert update(first)==(1,1,1,1)
    assert update(second)==(0,0,0,0)
    return {'q':q,'P_macro':[[1-q,q],[q,1-q]],'nonclosure':{'input_macro':2,'next_macro_A':4,'next_macro_B':0}}

if __name__=='__main__':print(run())
