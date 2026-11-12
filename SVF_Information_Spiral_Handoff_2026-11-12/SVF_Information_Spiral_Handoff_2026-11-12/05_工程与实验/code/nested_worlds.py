"""A minimal *semantic* nested-world constructor, not an actual physical universe.
Each program is an explicitly encoded rule; the physical host remains Python.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class World:
    name:str
    bits:int
    rule:str
    state:tuple[int,...]

    def step(self)->'World':
        assert len(self.state)==self.bits
        x=self.state
        if self.rule=='xor-neighbors':
            nxt=tuple(x[(i-1)%self.bits]^x[(i+1)%self.bits] for i in range(self.bits))
        elif self.rule=='rotate-right':
            nxt=(x[-1],)+x[:-1]
        elif self.rule=='majority':
            nxt=tuple(int(x[(i-1)%self.bits]+x[i]+x[(i+1)%self.bits]>=2) for i in range(self.bits))
        else:raise ValueError(self.rule)
        return World(self.name,self.bits,self.rule,nxt)

@dataclass(frozen=True)
class EmbeddedWorld:
    host_name:str
    child:World
    next_layer:'EmbeddedWorld|None'=None

def construct_chain(depth:int)->EmbeddedWorld:
    if not (1<=depth<=15):raise ValueError('small demo only: 1<=depth<=15')
    rules=('xor-neighbors','rotate-right','majority')
    node=None
    for i in reversed(range(depth)):
        world=World(name=f'world_{i+1}',bits=5,rule=rules[i%3],state=(1,0,0,1,0))
        node=EmbeddedWorld(host_name='physical_Python' if i==0 else f'world_{i}',child=world,next_layer=node)
    return node

def run():
    chain=construct_chain(5); rules=[]; node=chain
    while node:
        rules.append(node.child.rule)
        progressed=node.child.step()
        assert len(progressed.state)==5
        node=node.next_layer
    assert len(rules)==5 and len(set(rules))==3
    return {'layers':len(rules),'different_rule_classes':len(set(rules)),
            'warning':'This is a data structure with independent rule evaluators, not a universal simulated civilization.'}

if __name__=='__main__':print(run())
