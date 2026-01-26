import sys
inp = sys.stdin.readline

def reversort(L: list) -> int:
    cost = 0
    for i in range(len(L)-1):
        j = i + L[i:].index(min(L[i:]))
        L[i:j+1] = reversed(L[i:j+1])
        cost += (j - i + 1)
    return cost

for _ in range(int(inp())):
    n,L = int(inp()),list(map(int,inp().split()))
    print("Case #",_+1,":",reversort(L))