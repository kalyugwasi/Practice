import sys
m = sys.stdin.readline
t = int(m())
a = set(map(int, m().split()))
res = 1
while res in a:
    res += 1
print(res)
