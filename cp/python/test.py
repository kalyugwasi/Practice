import sys,heapq

if "input.txt" in sys.argv:
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt", "w")

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    for i in range(n):
        mx = max(p[i:])
        if p[i] != mx:
            pos = p.index(mx)
            p[i:pos+1] = reversed(p[i:pos+1])
            break

    print(*p)