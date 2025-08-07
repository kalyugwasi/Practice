import sys
o = sys.stdin.readline
t = int(o())
for h in range(t):
    n = int(o())
    L = list(map(int,o().split()))
    def reversort(L:list)->int:
        cost = 0
        for i in range(len(L)-1):
            j = i + L[i:].index(min(L[i:]))
            L[i:j+1] = reversed(L[i:j+1])
            cost += (j-i+1)
        return cost
    print("#Case", h+1,":",reversort(L))