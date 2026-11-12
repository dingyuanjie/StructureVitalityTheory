"""Rule 90 on an effectively infinite line; standard library only."""
def row_as_positions(t: int) -> set[int]:
    """Return live positions after t updates from an initial live cell at 0."""
    live = {0}
    for _ in range(t):
        nxt = set()
        candidates = {p + d for p in live for d in (-1, 1)}
        for p in candidates:
            if ((p-1 in live) ^ (p+1 in live)):
                nxt.add(p)
        live = nxt
    return live

def predicted_count(t:int) -> int:
    return 2 ** t.bit_count()

def run() -> dict:
    for t in range(65):
        observed = len(row_as_positions(t))
        expect = predicted_count(t)
        assert observed == expect, (t, observed, expect)
    return {"rule90_checked_steps":65,"N_63":len(row_as_positions(63)),"formula":"2**popcount(t)"}

if __name__ == '__main__':
    print(run())
