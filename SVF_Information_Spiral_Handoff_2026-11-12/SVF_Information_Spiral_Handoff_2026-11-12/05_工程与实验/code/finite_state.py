"""Pigeonhole principle demo: a deterministic finite state machine eventually repeats."""
def trajectory_mod_m(m:int=13,add:int=5,start:int=0):
    seen={}; states=[];x=start
    while x not in seen:
        seen[x]=len(states)
        states.append(x)
        x=(x+add)%m
    start_index=seen[x];period=len(states)-start_index
    assert start_index+period<=m
    return {'states':states,'transient_length':start_index,'period':period}

def run():
    a=trajectory_mod_m();assert a['period']==13
    return {'finite_state_machine':a}

if __name__=='__main__':print(run())
