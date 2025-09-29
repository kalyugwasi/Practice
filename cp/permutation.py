import sys
m = sys.stdin.readline
n = int(m())
res = []
if n == 3 or n == 2:
    print("NO SOLUTION")
else:
    for i in range(2,n+1,2):
        res.append(i)
    for i in range(1,n+1,2):
        res.append(i)
    print(*res)
