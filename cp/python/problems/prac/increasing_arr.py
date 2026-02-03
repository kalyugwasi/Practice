import sys
m = sys.stdin.readline
n = int(m())
a = list(map(int, m().split()))
res = 0
for i in range(1,n):
    if a[i-1] <= a[i]:
        continue
    else:
        res += a[i-1] - a[i]
        a[i] += a[i-1] - a[i]
        
print(res)